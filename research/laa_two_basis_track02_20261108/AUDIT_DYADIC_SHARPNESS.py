#!/usr/bin/env python3
"""Numerical audit for Milestone 27: exactly sharp exponent halving, all k.
Run: python AUDIT_DYADIC_SHARPNESS.py
Requires numpy, scipy. These floating-point checks do NOT replace analytic proof.
"""
import json
import numpy as np
from scipy.linalg import null_space


def graph_frame_and_gram(k, t):
    s=1/np.sqrt(2)
    m=2*k+2
    e=np.eye(k+2)
    edges=[(i,j) for i in range(k+2) for j in range(i+1,k+2)]
    edges += [(0 if i==1 else k+i,k+1+i) for i in range(1,k+1)]
    edges += [(i,k+1+i) for i in range(1,k+1)]
    D=np.zeros((m,k+2))
    D[:k+2]=e
    for i in range(1,k+1):
        D[k+1+i]=s*(D[0 if i==1 else k+i]+e[i])
    T=np.zeros_like(D)
    T[:k+2]=e
    T[k+2]=s*np.sqrt(1-t*t)*(e[0]+e[1])+t*e[2]
    for i in range(2,k+1):
        a=T[k+i]@e[i]
        T[k+1+i]=s/(1+a)*(T[k+i]+e[i])+np.sqrt(a/(1+a))*e[i+1]
    deg=np.zeros(m)
    for i,j in edges:
        deg[i]+=1
        deg[j]+=1
    h=1/(4*np.sqrt(max(deg)+1))
    E=np.eye(m)
    cols=[np.sqrt(1-2*h*h*deg[i])*E[:,i] for i in range(m)]
    for i,j in edges:
        cols.extend([h*(E[:,i]+E[:,j]),h*(E[:,i]-E[:,j])])
    G=np.column_stack(cols)
    assert np.linalg.norm(G@G.T-np.eye(m))<1e-9
    assert np.min(np.diag(G.T@D@D.T@G))>0
    return G,D,T


def test_curve(k,t,seed=71):
    G,D,T=graph_frame_and_gram(k,t)
    m,M=G.shape
    z=M-m
    n=2*M-m
    K=null_space(G).T
    F=np.column_stack([G,np.zeros((m,z))])
    U0=np.block([[K.T,G.T@G],[np.zeros((z,z)),K]])
    assert np.linalg.norm(U0.T@U0-np.eye(n))<1e-9
    S=np.block([[K.T,np.zeros((M,z))],[np.zeros((z,z)),np.eye(z)]])
    rng=np.random.default_rng(seed)
    W=rng.standard_normal((2*z,2*z))
    A=W-W.T
    h=.01
    Omega=np.linalg.solve(np.eye(2*z)-h*A,np.eye(2*z)+h*A)
    U=(F.T@F+S@Omega@S.T)@U0
    assert np.min(np.abs(U))>0
    # Under a small exterior rotation, Q1 and rotated Q2 remain complementary.
    Q1=np.vstack([np.eye(z),np.zeros((z,z))])
    C=np.column_stack([Q1,Omega[:,z:]])
    assert abs(np.linalg.det(C))>1e-8
    # Solve the restricted source-support cross correction, proven surjective in Milestone 27.
    R,_=np.linalg.qr(T,mode="reduced")
    err=np.diag(G.T@(T@T.T-D@D.T)@G)
    B=np.stack([(R.T@G)[a]*K[b] for a in range(R.shape[1])
                for b in range(z)],axis=1)
    sol=np.linalg.lstsq(B,-err/2,rcond=1e-12)[0]
    mismatch=np.linalg.norm(B@sol+err/2)
    assert mismatch<1e-10
    X=R@sol.reshape(R.shape[1],z)
    # Source block remains rank k+2 and has positive eigenvalue gap.
    P=np.linalg.lstsq(T,X,rcond=None)[0]
    out=np.hstack([P,P])@np.linalg.inv(C)
    Gram=F.T@T+S@out.T
    Y=Gram@Gram.T
    Ystar=F.T@D@D.T@F
    residual=np.r_[np.diag(Y-Ystar),np.diag(U.T@(Y-Ystar)@U)]
    res=float(np.linalg.norm(residual))
    source_dist=float(np.linalg.norm(T@T.T-D@D.T))
    assert abs(np.trace(T@T.T-D@D.T))<1e-9
    assert res>0
    assert np.linalg.eigvalsh(Y).min()>-1e-8
    assert np.linalg.matrix_rank(Y,tol=1e-8)==k+2
    return dict(k=k,t=t,source_order=m,frame_vectors=M,two_zero_order=n,
                final_positive_order=5*n+4,source_rank=k+2,final_rank=k+3,
                rank_of_cross_map=np.linalg.matrix_rank(B,tol=1e-9),
                expected_cross_rank=M-1,cross_cancellation_residual=mismatch,
                minimum_basis_overlap=float(np.min(np.abs(U))),
                source_distance=source_dist,ambient_residual=res,
                residual_divided_by_t_fourth=res/t**4)


def main():
    results=[test_curve(k,t) for k in (1,2,3,4)
             for t in (.2,.1,.05)]
    print(json.dumps(results,indent=2))


if __name__=="__main__":
    main()
