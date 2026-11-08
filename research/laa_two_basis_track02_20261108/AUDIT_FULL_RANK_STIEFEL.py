#!/usr/bin/env python3
"""Milestone 28: numerical exact-covariance / full-rank Stiefel span audit.
Requires numpy, scipy. Random rotations are only numerical diagnostics.
"""
import numpy as np
from scipy.linalg import hadamard

def twirl(r):
    size=1<<int(np.ceil(np.log2(r)))
    H=hadamard(size)
    return [np.diag(H[a,:r])@np.roll(np.eye(r),j,axis=1)
            for a in range(size) for j in range(r)]

def sqrtm(B):
    w,V=np.linalg.eigh(B)
    assert min(w)>0
    return (V*np.sqrt(w))@V.T

def test(m):
    r=m+1
    d=m*r
    H=np.diag([.4,-.4]) if m==2 else np.diag([.3,-.3]+[0]*(m-2))
    Bs=[np.eye(m),np.eye(m)+H,np.eye(m)-H]
    c=[r/2,r/4,r/4]
    Ts=twirl(r)
    # Each SINGLE twirl is a tight block with scalar covariance B tensor I/r.
    one=[]
    for B,w in zip(Bs,c):
        V=np.column_stack([sqrtm(B),np.zeros((m,1))])
        for O in Ts:
            one.append(np.sqrt(w/len(Ts))*(V@O).reshape(-1))
    G=np.column_stack(one)
    frame_error=np.linalg.norm(G@G.T-np.eye(d))
    assert frame_error<1e-10
    rng=np.random.default_rng(4)
    orbit=[]
    for B in Bs:
        V=np.column_stack([sqrtm(B),np.zeros((m,1))])
        for j in range(16):
            O,_=np.linalg.qr(rng.normal(size=(r,r)))
            for S in Ts:
                orbit.append((V@O@S).reshape(-1))
    tri=np.triu_indices(d)
    A=np.stack([np.outer(v,v)[tri] for v in orbit])
    rank=int(np.linalg.matrix_rank(A,tol=1e-9))
    source_measurements=2
    s=m*(m+1)//2-source_measurements
    expected=d*(d+1)//2-s
    assert rank==expected
    return {'m':m,'ancilla_r':r,'tensor_order_d':d,'twirl_size':len(Ts),
            'one_twirl_parseval_error':float(frame_error),
            'projector_span_rank':rank,'expected_operator_system_rank':expected}

if __name__=='__main__':
    import json
    print(json.dumps([test(2),test(3)],indent=2))
