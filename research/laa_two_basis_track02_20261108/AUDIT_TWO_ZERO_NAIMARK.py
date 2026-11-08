#!/usr/bin/env python3
"""Numerical consistency audit of Milestone 21.
Requires numpy and scipy. Does not substitute for the exact proof.
"""
import numpy as np
from scipy.linalg import null_space


def double_zero_dilation(G, seed=0):
    d,M=G.shape
    assert M>d and np.linalg.norm(G@G.T-np.eye(d))<1e-9
    assert np.min(np.linalg.norm(G,axis=0))>0
    assert np.max(np.linalg.norm(G,axis=0))<1-1e-9
    z=M-d
    N=2*M-d
    K=null_space(G).T
    P=G.T@G
    F=np.hstack((G,np.zeros((d,z))))
    U0=np.block([[K.T,P],[np.zeros((z,z)),K]])
    Qb=np.block([[K.T,np.zeros((M,z))],[np.zeros((z,z)),np.eye(z)]])
    assert np.linalg.norm(U0.T@U0-np.eye(N))<1e-9
    rng=np.random.default_rng(seed)
    for trial in range(1000):
        C=rng.normal(size=(2*z,2*z))
        C-=C.T
        R=np.linalg.solve(np.eye(2*z)+.025*C,np.eye(2*z)-.025*C)
        Om=np.eye(N)+Qb@(R-np.eye(2*z))@Qb.T
        U=Om@U0
        if np.min(np.abs(U))>1e-7:break
    else:raise RuntimeError("generic overlap search failed")
    Q=np.eye(N)-F.T@F
    Z1=np.diag(np.r_[np.zeros(M),np.ones(z)])
    Z2=U[:,:z]@U[:,:z].T
    ev=np.linalg.eigvalsh(Q@(Z1+Z2)@Q)
    gap=float(np.min(ev[ev>1e-7]))
    assert gap>.5
    assert np.linalg.norm(F@U[:,z:]-G)<1e-8
    assert np.linalg.norm(F@U[:,:z])<1e-8
    return F,U,gap


def tetrahedron():
    S=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float).T
    return S/2  # 3x4, Parseval; projectors span equal-diagonal subspace


def run():
    G=tetrahedron()
    F,U,gap=double_zero_dilation(G)
    d,M=G.shape;N=U.shape[0];z=M-d
    X=np.array([[1,.2,.1],[.2,1,.4],[.1,.4,.8]])
    assert np.linalg.eigvalsh(X).min()>0
    Y=F.T@X@F
    b1=np.diag(Y)
    b2=np.diag(U.T@Y@U)
    assert np.allclose(b1[:M],b2[z:],atol=1e-12)
    assert np.max(abs(b1[M:]))<1e-12
    assert np.max(abs(b2[:z]))<1e-12
    print(dict(d=d,M=M,N=N,full_overlap_min=float(np.min(np.abs(U))),
               exposing_gap=gap,first_zero_count=z,second_zero_count=z,
               frame_error=float(np.linalg.norm(F@F.T-np.eye(d))),
               max_embedded_nonzero_list_error=float(np.max(abs(b1[:M]-b2[z:])))))


if __name__=="__main__":
    run()
