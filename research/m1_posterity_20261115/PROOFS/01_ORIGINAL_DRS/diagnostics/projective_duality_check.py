#!/usr/bin/env python3
"""Numerical checks of exact self-dual-cone DRS identities, not asymptotic proof."""
import numpy as np
from numpy.linalg import norm


def main():
    rng = np.random.default_rng(20261114)
    n = 4
    basis = []
    for i in range(n):
        b = np.zeros((n, n)); b[i, i] = 1; basis.append(b)
        for j in range(i):
            b = np.zeros((n, n))
            b[i, j] = b[j, i] = 1 / np.sqrt(2)
            basis.append(b)
    B = np.array(basis)
    dim = len(B)
    M = np.linalg.qr(rng.normal(size=(dim, dim)))[0]
    L = M[:, :4]; P = L @ L.T; Q = np.eye(dim) - P
    a = Q @ rng.normal(size=dim); sig = a @ a
    E = np.outer(a, a) / sig; Pd = Q - E; ad = -a / sig

    def cone(z):
        X = np.einsum('i,ijk->jk', z, B)
        e, u = np.linalg.eigh(X)
        Y = (u * np.maximum(e, 0)) @ u.T
        return np.einsum('ijk,jk->i', B, Y)

    def T(z, A, PP):
        u = A + PP @ z
        return z + cone(2 * u - z) - u

    errs = {key: 0. for key in
            ['projector', 'reflection', 'operator', 'residual', 'involution', 'radial']}
    errs['projector'] = max(norm(Pd @ Pd - Pd), norm(Pd - Pd.T), norm(Pd @ ad))
    for _ in range(1000):
        z = rng.normal(size=dim) * rng.uniform(.01, 10)
        h = sig - a @ z
        if h < .2:
            z -= (.2 - h) / sig * a
            h = sig - a @ z
        w = z / h; tz = T(z, a, P); tw = T(w, ad, Pd); d = tz - z
        hd = ad @ ad - ad @ w
        vals = {
            'reflection': norm((2 * ad + (2 * Pd - np.eye(dim)) @ w)
                               + (2 * a + (2 * P - np.eye(dim)) @ z) / h),
            'operator': norm(tw - tz / h),
            'residual': norm((tw - w) - d / h),
            'involution': norm(w / hd - z),
            'radial': abs(h - tz @ d),
        }
        for key, val in vals.items():
            errs[key] = max(errs[key], val)
    for key, val in errs.items():
        print(f'{key}: {val:.4e}')
    assert max(errs.values()) < 1e-9
    print('PASS: 1000 random inputs; floating-point corroboration only.')


if __name__ == '__main__':
    main()
