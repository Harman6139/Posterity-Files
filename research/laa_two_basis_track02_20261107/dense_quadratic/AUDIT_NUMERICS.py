#!/usr/bin/env python3
"""Reproducible numerical audit for the dense-quadratic Track 02 results.
Requires numpy and scipy. These tests check identities; proofs are in the memo.
"""
from itertools import combinations
import json
import numpy as np
from scipy.linalg import hadamard, qr


def gf_mul(a,b,t,poly):
    z=0
    while b:
        if b&1: z^=a
        b>>=1
        a<<=1
        if a&(1<<t): a^=poly
    return z


def sign_family(m):
    t=max(1,int(np.ceil(np.log2(m))))
    q=1<<t
    poly={1:3,2:7,3:11,4:19,5:37,6:67}[t]
    labels=[(x,gf_mul(gf_mul(x,x,t,poly),x,t,poly)) for x in range(m)]
    S=np.empty((q*q,m))
    for i in range(q*q):
        a,b=divmod(i,q)
        for j,(x,y) in enumerate(labels):
            S[i,j]=1 if ((a&x).bit_count()+(b&y).bit_count())%2==0 else -1
    chars=np.column_stack([np.ones(len(S))]+[S[:,i]*S[:,j] for i,j in combinations(range(m),2)])
    assert np.allclose(chars.T@chars,q*q*np.eye(chars.shape[1]))
    return S


def commuting_frame(m,diagonal_source_basis):
    # Traceless vectors spanning the allowed extra diagonal directions.
    k=1<<int(np.ceil(np.log2(m)))
    r=k-m
    S=sign_family(m)
    M=len(S)
    h=len(diagonal_source_basis)
    hh=max(1,h)
    hs=list(diagonal_source_basis) if h else [np.zeros(m)]
    _,_,piv=qr(S.T,pivoting=True,mode="economic")
    picked=set(piv[:m]) if r else set()
    eta=1/(16*M*(r+1)) if r else 0
    vec=[]
    for j in range(M):
        w=1/(2*M)-(2*eta*r if j in picked else 0)
        assert w>0
        vec.append(np.r_[np.sqrt(w)*S[j],np.zeros(r)])
    for v in hs:
        assert abs(sum(v))<1e-10 and max(abs(v))<=1+1e-10
        for s in (-1,1):
            d=np.sqrt(1+s*v/2)
            for row in S:
                vec.append(np.r_[row*d/np.sqrt(4*hh*M),np.zeros(r)])
    for j in picked:
        for a in range(r):
            for s in (-1,1):
                v=np.zeros(k)
                v[:m]=np.sqrt(eta)*S[j]
                v[m+a]=s*np.sqrt(eta)
                vec.append(v)
    zeta=1/(8*(r+1)**2) if r else 0
    for a,b in combinations(range(r),2):
        for s in (-1,1):
            v=np.zeros(k)
            v[m+a]=np.sqrt(zeta)
            v[m+b]=s*np.sqrt(zeta)
            vec.append(v)
    for a in range(r):
        w=1-2*eta*m-2*zeta*(r-1)
        assert w>.5
        v=np.zeros(k)
        v[m+a]=np.sqrt(w)
        vec.append(v)
    G=np.asarray(vec).T
    assert np.linalg.norm(G@G.T-np.eye(k))<1e-9
    A=np.stack([np.outer(v,v)[np.triu_indices(k)] for v in G.T])
    dim=int(np.linalg.matrix_rank(A,tol=1e-9))
    expected=k*(k+1)//2-(m-1-h)
    assert dim==expected,(dim,expected)
    return G,hadamard(k)/np.sqrt(k),dim


def sparsify_parseval(G):
    # Numerical conic-Caratheodory analogue of the exact proof.
    d,M=G.shape
    tri=np.triu_indices(d)
    A=np.stack([np.outer(v,v)[tri] for v in G.T],axis=1)
    q=int(np.linalg.matrix_rank(A,tol=1e-9))
    _,_,piv=qr(A,pivoting=True,mode="economic")
    reserve=np.zeros(M)
    reserve[piv[:q]]=.5
    w=np.ones(M)-reserve
    while (w>1e-11).sum()>q:
        active=np.flatnonzero(w>1e-11)
        _,_,vh=np.linalg.svd(A[:,active],full_matrices=False)
        h=vh[-1]
        if not np.any(h>1e-12):h=-h
        pos=h>1e-12
        t=np.min(w[active[pos]]/h[pos])
        w[active]-=t*h
        w[np.abs(w)<1e-10]=0
        assert np.min(w)>-1e-9
        w=np.maximum(w,0)
    w+=reserve
    mask=w>1e-11
    Z=G[:,mask]*np.sqrt(w[mask])[None,:]
    assert Z.shape[1]<=2*q
    assert np.linalg.norm(Z@Z.T-np.eye(d))<1e-8
    return Z,q


def signed_anchor(G,U):
    # Signed frame with a third, weight-4 pure anchor for symmetry breaking.
    d,M=G.shape
    h=.1
    a=np.sqrt((5+3*h*h)/7)
    b=np.sqrt((1-5*h*h)/7)
    cols=[]
    weights=[]
    for i in range(d):
        cols.extend([a*U[:,i],b*U[:,i],b*U[:,i]])
        weights.extend([-1,2,3])
    for v in G.T:
        cols.append(h*v)
        weights.append(4)
    A=np.column_stack(cols)
    weights=np.asarray(weights)
    ri=h*U.T@np.sum(G,axis=1)
    t=2*np.sqrt(M+1)
    z=np.zeros(A.shape[1])
    for i in range(d):
        z[3*i]=(2*ri[i]+t)/(3*a)
        z[3*i+1]=-(5*ri[i]+4*t)/(3*b)
        z[3*i+2]=t/b
    z[3*d:]=1
    n=A.shape[1]
    theta=1/(1e8*(n+1)*(M+1))
    L=2*n*n+2
    ip=A.T@A
    e2=None
    for j in range(1,L):
        candidate=theta*(1+j/L)
        off=np.abs((ip+candidate*np.outer(z,z))[np.triu_indices(n,1)])
        if np.min(off)>theta/(36*L):
            e2=candidate
            break
    assert e2 is not None
    c2=.01
    ss=z@z
    qq=(weights*z)@z
    x2=(2+e2*(qq-2*ss)+2*c2)/3
    y2=(1-e2*(ss+qq)-5*c2)/3
    F=np.block([[A,np.zeros((d,3))],
                [np.sqrt(e2)*z[None,:],np.array([[np.sqrt(x2),np.sqrt(y2),np.sqrt(c2)]])]])
    D=np.r_[weights,-1,2,4]
    P=F.T@F
    Q=np.eye(len(D))-P
    R=P-Q
    cert=np.diag(D)+R@np.diag(D)@R
    positive=np.linalg.eigvalsh(Q@cert@Q)
    positive=positive[positive>1e-6]
    assert np.min(positive)>1.999
    return {"N":int(F.shape[1]),
            "frame_error":float(np.linalg.norm(F@F.T-np.eye(d+1))),
            "signed_error":float(np.linalg.norm((F*D)@F.T)),
            "orthogonality_error":float(np.linalg.norm(R.T@R-np.eye(len(D)))),
            "exposing_gap":float(min(positive)),
            "min_absolute_overlap":float(np.min(np.abs(R)))}


def main():
    cases=[(3,[np.array([1.,-1.,0.])]),
           (5,[np.array([1.,-1.,0.,0.,0.]),np.array([0.,0.,1.,-1.,0.])]),
           (4,[])]
    out=[]
    for m,hs in cases:
        G,U,q=commuting_frame(m,hs)
        before=G.shape[1]
        G,q2=sparsify_parseval(G)
        assert q==q2
        # Tests use compressed old basis without the duplicate required
        # specifically for the final non-reflection rotation.
        cert=signed_anchor(G,U)
        bound=(2*m)**2+4*(2*m)+5
        assert cert["N"]<=bound
        out.append({"m":m,"rank":q,"original_columns":int(before),
                    "sparse_columns":int(G.shape[1]),**cert})
    print(json.dumps(out,indent=2))


if __name__=="__main__":
    main()
