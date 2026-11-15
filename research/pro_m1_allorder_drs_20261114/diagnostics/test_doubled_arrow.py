#!/usr/bin/env python3
"""Exploratory floating-point diagnostic, NOT an asymptotic proof.

Rational affine U in S^7: X00=A, X33=B, X11=c, X44=d, X66=r,
X02=-c/2+gamma*r, X35=-d/2-gamma*r, X01=X34=-1/2,
X06=u, with symmetric counterparts and all other entries zero.
Run: python test_doubled_arrow.py --steps 200000 --output results.json
Dependencies: Python 3, numpy, numba. No network or external data.
"""
import argparse
import json
import os
import time
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
os.environ.setdefault('OMP_NUM_THREADS', '1')
import numpy as np
from numba import njit


def setup(gamma):
    B = np.zeros((6, 7, 7)); a = np.zeros((7, 7))
    B[0, 0, 0] = 1; B[1, 3, 3] = 1
    B[2, 1, 1] = 1; B[2, 0, 2] = B[2, 2, 0] = -.5
    B[3, 4, 4] = 1; B[3, 3, 5] = B[3, 5, 3] = -.5
    B[4, 6, 6] = 1; B[4, 0, 2] = B[4, 2, 0] = gamma
    B[4, 3, 5] = B[4, 5, 3] = -gamma
    B[5, 0, 6] = B[5, 6, 0] = 1
    a[0, 1] = a[1, 0] = a[3, 4] = a[4, 3] = -.5
    flat = B.reshape(6, 49)
    inv = np.linalg.inv(flat @ flat.T)
    return B, inv, a


@njit
def proj_L(Z, B, inv):
    c = np.zeros(6)
    for i in range(6):
        for j in range(7):
            for l in range(7):
                c[i] += B[i, j, l] * Z[j, l]
    c = inv @ c
    out = np.zeros((7, 7))
    for i in range(6):
        out += c[i] * B[i]
    return out


@njit
def run(B, inv, a, z0, checkpoints):
    Z = z0.copy()
    out = np.zeros((len(checkpoints), 14))
    zs = np.zeros((len(checkpoints), 7, 7)); ds = zs.copy()
    slot = 0
    for k in range(checkpoints[-1] + 1):
        X = proj_L(Z, B, inv); U = a + X
        R = 2 * U - Z
        vals, vecs = np.linalg.eigh(R)
        vals = np.maximum(vals, 0)
        cone = (vecs * vals) @ vecs.T
        d = cone - U
        if k == checkpoints[slot]:
            scale = (k + 1.) ** .25
            odd = Z[:6, 6]; dodd = d[:6, 6]
            out[slot, 0] = k
            out[slot, 1] = np.linalg.norm(Z) / scale
            out[slot, 2] = np.linalg.norm(d) * (k + 1.) ** .75
            out[slot, 3] = np.linalg.norm(odd) * scale
            out[slot, 4] = np.linalg.norm(dodd) * (k + 1.) ** .75
            out[slot, 5] = Z[0, 0] / scale
            out[slot, 6] = Z[2, 2] / scale
            out[slot, 7] = Z[3, 3] / scale
            out[slot, 8] = Z[5, 5] / scale
            out[slot, 9] = Z[6, 6] * (k + 1.) ** .75
            out[slot, 10] = Z[0, 6] * scale
            out[slot, 11] = Z[2, 6] * scale
            out[slot, 12] = Z[1, 6] * scale
            out[slot, 13] = np.linalg.norm(d - proj_L(d, B, inv)) * (k + 1.) ** .75
            zs[slot] = Z; ds[slot] = d
            slot += 1
            if slot == len(checkpoints):
                break
        Z += d
        Z = (Z + Z.T) / 2
    return out, zs, ds


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--steps', type=int, default=200000)
    parser.add_argument('--gamma', type=float, default=1.)
    parser.add_argument('--epsilon', type=float, default=.1)
    parser.add_argument('--output', default='doubled_arrow.json')
    args = parser.parse_args()
    if args.steps < 20 or args.gamma <= 0:
        parser.error('steps must be at least 20 and gamma must be positive')
    B, inv, a = setup(args.gamma)
    z = a.copy(); z[0, 6] = z[6, 0] = args.epsilon
    z[2, 6] = z[6, 2] = args.epsilon * .3
    checkpoints = np.unique(np.rint(np.geomspace(20, args.steps, 80)).astype(np.int64))
    start = time.time()
    out, zs, ds = run(B, inv, a, z, checkpoints)
    names = ['k', 'state_scaled', 'step_scaled', 'odd_amplitude_scaled',
             'odd_step_scaled', 'H1', 'G1', 'H2', 'G2', 'new_diag_scaled',
             'odd_A_scaled', 'odd_B_scaled', 'odd_C_scaled', 'normal_step_scaled']
    payload = {'status': 'Exploratory floating-point diagnostic, not a counterexample proof',
               'gamma': args.gamma, 'epsilon': args.epsilon,
               'elapsed_seconds': time.time() - start, 'columns': names,
               'records': out.tolist(), 'last_state': zs[-1].tolist(),
               'last_step': ds[-1].tolist()}
    with open(args.output, 'w', encoding='utf-8') as stream:
        json.dump(payload, stream, indent=2)
    print('elapsed', payload['elapsed_seconds'])
    for row in out[-12:]:
        print(dict(zip(names, row)))


if __name__ == '__main__':
    main()
