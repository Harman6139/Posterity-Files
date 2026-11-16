"""Exact rational certificate, with separate floating-point DRS checks.

The Fraction assertions are exact. The trajectories are diagnostics only.
No simulation is used to establish an asymptotic theorem.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import numpy as np
from numba import njit


def exact_certificate():
    weights = [2, 2, 3, 4, 4, 5, 5, 5]
    rhs = F(5)
    h = [F(w*w, 50) for w in weights]
    c = [F(w**3, 500) for w in weights]
    W = [ci/hi for ci, hi in zip(c, h)]
    G = F(1)
    S = sum(ci*wi for ci, wi in zip(c, W))
    assert sum(w**4 for w in weights) == 2500
    assert all(x > 0 for x in h)
    assert sum(F(w)*ci for w, ci in zip(weights, c)) == rhs
    assert all(hi/2 == wi*wi*G for hi, wi in zip(h, W))
    assert all(wi == F(w,10) for w, wi in zip(weights, W))
    assert S == G/2
    # PSD primal block by H>0 and zero Schur complement.
    assert S-sum(ci*ci/hi for ci,hi in zip(c,h)) == 0
    # PSD dual is [-W;1][-W;1]^T; its cross block is -weights/10.
    primal = sum(hi*hi for hi in h)/4+(G/2)**2
    dual = -sum((hi/2)**2 for hi in h)-G*G/4+2*rhs/10
    assert primal == dual == F(1,2)
    return dict(order=9, weights=weights, rhs=str(rhs),
                H_diagonal=[str(x) for x in h], G=str(G),
                cross=[str(x) for x in c], primal=str(primal),
                dual=str(dual), gap='0', verified=True)


@njit(cache=True)
def run_drs(weights, rhs, z, steps):
    r = len(weights); m = r+1
    denom = np.sum(weights*weights)
    records = np.zeros((5,6)); counter=0
    cstar = rhs*weights**3/np.sum(weights**4)
    Spow = np.sum(np.abs(cstar)**(4.0/3.0))
    h = np.sqrt(2.0)*Spow**0.25*np.abs(cstar)**(2.0/3.0)
    g = np.sqrt(2.0)*Spow**0.75
    V = np.zeros((m,m))
    for i in range(r): V[i,i]=h[i]
    V[r,r]=g
    for k in range(steps):
        u=np.zeros((m,m))
        mismatch=rhs
        for i in range(r): mismatch-=weights[i]*z[i,r]
        for i in range(r):
            u[i,i]=z[i,i]
            u[i,r]=u[r,i]=z[i,r]+weights[i]*mismatch/denom
        R=2*u-z
        ev, Q=np.linalg.eigh(R)
        v=(Q*np.maximum(ev,0.0))@Q.T
        d=v-u
        z=z+d
        n=k+1
        if n==100 or n==1000 or n==10000 or n==100000 or n==steps:
            if counter < 5:
                records[counter,0]=n
                records[counter,1]=np.linalg.norm(z/np.sqrt(n)-V)
                records[counter,2]=np.linalg.norm(np.sqrt(n)*d-V/2)
                records[counter,3]=np.linalg.norm(v[:r,r]-cstar)
                records[counter,4]=np.sqrt(n)*np.linalg.norm(d)
                records[counter,5]=np.linalg.norm(V)/2
                counter+=1
    return records[:counter], z


if __name__ == '__main__':
    cert=exact_certificate()
    rng=np.random.default_rng(7152026)
    output={'exact_certificate':cert,'numerical_runs':[]}
    for w,rhs in [(np.array([1.,2.,3.]),1.),
                  (np.array(cert['weights'],dtype=np.float64),5.)]:
        for start in ['zero','random']:
            m=len(w)+1
            z=np.zeros((m,m)) if start=='zero' else rng.normal(size=(m,m))
            z=(z+z.T)/2
            records,_=run_drs(w,rhs,z,100000)
            output['numerical_runs'].append(dict(weights=w.tolist(),rhs=rhs,
                start=start,columns=['iteration','state_error','scaled_step_error',
                'cross_selection_error','scaled_step_norm','predicted_step_norm'],
                records=records.tolist()))
    out=Path(__file__).with_name('certificate_and_drs_results.json')
    out.write_text(json.dumps(output,indent=2))
    print(json.dumps(output,indent=2))
