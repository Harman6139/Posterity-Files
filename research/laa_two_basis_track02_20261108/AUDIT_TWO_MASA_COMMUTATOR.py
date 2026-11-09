#!/usr/bin/env python3
"""Numerical sanity tests for Milestones 49-53 (not a proof).
Tests the exact reduced-skew tight-frame identity and samples the
fourth commutator-form singular value for generic real operator systems.
Requires NumPy, no internet.
"""
import numpy as np


def symmetric_basis(m):
    basis=[]
    for i in range(m):
        x=np.zeros((m,m));x[i,i]=1.;basis.append(x)
    for i in range(m):
        for j in range(i+1,m):
            x=np.zeros((m,m));x[i,j]=x[j,i]=1./np.sqrt(2);basis.append(x)
    return basis


def skew_basis(m):
    basis=[]
    for i in range(m):
        for j in range(i+1,m):
            x=np.zeros((m,m));x[i,j]=1./np.sqrt(2);x[j,i]=-1./np.sqrt(2)
            basis.append(x)
    return basis


def random_traceless_subspace(m,ell,rng):
    n=m*m
    q=np.eye(m).reshape(n)/np.sqrt(m)
    M=rng.normal(size=(n,ell))
    M-=q[:,None]*(q@M)[None,:]
    O,_=np.linalg.qr(M)
    return [O[:,j].reshape(m,m) for j in range(ell)]


def commutator_form(basis,T):
    p=len(basis);out=np.zeros((p,p))
    for i in range(p):
        for j in range(i+1,p):
            out[i,j]=np.trace(T@(basis[i]@basis[j]-basis[j]@basis[i]))
            out[j,i]=-out[i,j]
    return out


def test():
    rng=np.random.default_rng(20261109)
    results=[]
    for m in (4,5,6):
        ell=m+2 # p=m+3 source measurements, including scalar identity
        B=random_traceless_subspace(m,ell,rng)
        K=skew_basis(m)
        lowest=float('inf')
        for _ in range(100):
            c=rng.normal(size=len(K))
            c/=np.linalg.norm(c)
            T=sum(x*y for x,y in zip(c,K))
            sval=np.linalg.svd(commutator_form(B,T),compute_uv=False)
            lowest=min(lowest,float(sval[3]))
        # This is sampling ONLY, not a certificate for all T.
        results.append({"m":m,"source_measurement_dimension":ell+1,
                        "sample_count":100,
                        "smallest_sampled_fourth_singular":lowest})
    m,r=4,2
    N=m*r;O,_=np.linalg.qr(rng.normal(size=(N,N)))
    K=skew_basis(m); S=np.zeros((len(K),len(K)))
    for i in range(N):
        for j in range(i+1,N):
            ui=O[:,i].reshape(m,r);uj=O[:,j].reshape(m,r)
            A=ui@uj.T
            T_ij=(A-A.T)/2
            v=np.array([np.sum(T*T_ij) for T in K])
            S+=np.outer(v,v)
    error=np.linalg.norm(S-r/2*np.eye(len(K)))
    assert error<1e-10
    print({"generic_sampling":results,
           "reduced_skew_frame_m":m,"ancilla_r":r,
           "tight_frame_error":float(error)})
if __name__=="__main__":test()
