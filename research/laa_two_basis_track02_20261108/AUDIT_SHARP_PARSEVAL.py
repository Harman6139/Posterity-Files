#!/usr/bin/env python3
"""Milestone 26 independent numerical audit, requires numpy/scipy.
Checks the tetrahedral example (NO admissible ONB in source), the balanced
frame, positive final two-basis data, and an exact quadratic invisible curve.
Numerical evidence is not a proof; analytical argument is in Milestone 26.
"""
import numpy as np
from scipy.linalg import null_space

def source():
    G=np.array([[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]],float)/2
    d,M=G.shape;P=G.T@G
    H=null_space(G)
    T=np.column_stack([np.eye(M)/np.sqrt(2),P/np.sqrt(2),H/np.sqrt(2)])
    assert np.linalg.norm(G@G.T-np.eye(d))<1e-10
    assert np.linalg.norm(T@T.T-np.eye(M))<1e-10
    return G,T

def outer(T):
    n,L=T.shape
    # Split one admissible column; keep exact Parseval tightness.
    T=np.column_stack([T[:,0]/np.sqrt(2),T[:,0]/np.sqrt(2),T[:,1:]])
    L=T.shape[1];h=.1
    a=np.sqrt((5+3*h*h)/7)
    b=np.sqrt((1-5*h*h)/7)
    vec=[];weights=[]
    for i in range(n):
        e=np.eye(n)[:,i]
        vec.extend([a*e,b*e,b*e])
        weights.extend([-1,2,3])
    for t in T.T:
        vec.append(h*t);weights.append(4)
    A=np.column_stack(vec);D=np.array(weights)
    assert np.linalg.norm(A@A.T-np.eye(n))<1e-10
    assert np.linalg.norm((A*D)@A.T)<1e-10
    ri=h*T.sum(axis=1);t0=2*np.sqrt(L+1)
    z=np.zeros(A.shape[1])
    for i in range(n):
        z[3*i]=(2*ri[i]+t0)/(3*a)
        z[3*i+1]=-(5*ri[i]+4*t0)/(3*b)
        z[3*i+2]=t0/b
    z[3*n:]=1
    assert np.linalg.norm(A@z)<1e-10
    assert np.linalg.norm(A@(D*z))<1e-10
    ee=1e-9
    s0=z@z; q0=(D*z)@z
    anchor_v=.01
    x=(2+ee*(q0-2*s0)+2*anchor_v)/3
    y=(1-ee*(s0+q0)-5*anchor_v)/3
    assert min(x,y)>0
    F=np.block([[A,np.zeros((n,3))],
                [np.sqrt(ee)*z[None,:],np.array([[np.sqrt(x),np.sqrt(y),np.sqrt(anchor_v)]])]])
    D=np.r_[D,-1,2,4]
    R=2*F.T@F-np.eye(len(D))
    Q=np.eye(len(D))-F.T@F
    S=np.diag(D)+R@np.diag(D)@R
    eigs=np.linalg.eigvalsh(Q@S@Q)
    gap=float(min(eigs[eigs>1e-7]))
    assert gap>=1.999
    O=np.eye(len(D))
    ii=3*n;jj=len(D)-1;theta=.013
    O[ii,ii]=np.cos(theta);O[jj,jj]=np.cos(theta)
    O[ii,jj]=np.sin(theta);O[jj,ii]=-np.sin(theta)
    U=R@O
    assert np.linalg.norm(F@F.T-np.eye(n+1))<1e-10
    assert np.linalg.norm(U.T@U-np.eye(len(D)))<1e-10
    assert np.linalg.norm(np.diag(D)+U@np.diag(D)@U.T-S)<1e-10
    return F,U,gap,T

def measurement(U,Y):
    return np.r_[np.diag(Y),np.diag(U.T@Y@U)]

def test():
    G,T=source();F,U,gap,Tsplit=outer(T)
    d,M=G.shape;n=M;N=F.shape[1]
    X=np.array([[1.,.2,.1],[.2,1.,.4],[.1,.4,.8]])
    def encode(A):
        W=G.T@A@G
        Z=np.block([[W,np.zeros((n,1))],[np.zeros((1,n)),np.ones((1,1))]])
        return F.T@Z@F
    Y0=encode(X);obs=measurement(U,Y0)
    assert min(obs)>0 and np.min(np.abs(U))>0
    assert np.linalg.norm(F@Y0@F.T-np.block([[G.T@X@G,np.zeros((n,1))],[np.zeros((1,n)),np.ones((1,1))]]))<1e-9
    # Source-only projectors measure the source even when inner P/Q cross terms exist.
    P=G.T@G; W=(F@Y0@F.T)[:n,:n]
    pure_errors=[(P[:,j]@W@P[:,j])-(G[:,j]@X@G[:,j]) for j in range(M)]
    assert np.linalg.norm(pure_errors)<1e-9
    # Find an outer support-to-exterior cross direction invisible to both lists.
    _,B=np.linalg.eigh(Y0);support=B[:,-2:]
    Qout=null_space(F)
    cols=[]
    for a in range(2):
        for b in range(Qout.shape[1]):
            v=support[:,a];w=Qout[:,b]
            cols.append(np.r_[2*v*w,2*(U.T@v)*(U.T@w)])
    Zmat=np.column_stack(cols)
    c=null_space(Zmat)[:,0]
    K=sum(c[a*Qout.shape[1]+b]*np.outer(support[:,a],Qout[:,b])
          for a in range(2) for b in range(Qout.shape[1]))
    assert np.linalg.norm(measurement(U,K+K.T))<1e-9
    repair=K.T@np.linalg.pinv(Y0,hermitian=True)@K
    curves=[]
    for t in [1e-2,1e-3,1e-4]:
        Y=Y0+t*(K+K.T)+t*t*repair
        delta=np.linalg.norm(measurement(U,Y)-obs)
        assert np.linalg.eigvalsh(Y).min()>-1e-12
        curves.append({"t":t,"data_residual":delta,"residual_over_t_squared":delta/t**2,
                       "off_face_distance_lower":np.sqrt(2)*t*np.linalg.norm(K)})
    print({"source_d":d,"source_M":M,"outer_N":N,
           "new_frame_columns":Tsplit.shape[1],
           "min_overlap":float(np.min(np.abs(U))),
           "min_positive_measurement":float(min(obs)),
           "basis_data_difference":float(np.linalg.norm(obs[:N]-obs[N:])),
           "exposing_gap":gap,
           "source_only_moment_error":float(np.linalg.norm(pure_errors)),
           "curves":curves})

if __name__=="__main__":test()
