#!/usr/bin/env python3
"""Fixed-first-basis two-MASA compatibility test (Milestone 20).

Given p real symmetric n x n matrices H[a] already expressed in the first
basis, the existence of a second ONB such that span(H[a]) lies in the sum
of the two MASA spaces is equivalent to a LINEAR system for pn diagonal
corrections.  This script evaluates its normalized least-squares gap.

Use exact rational Gaussian elimination for a formal certificate. Floating
point output is diagnostic and never substitutes for the mathematical proofs.

Requires: numpy; scipy optional (only for specialized numerical experiments).
"""
from __future__ import annotations
import numpy as np


def linear_compatibility(Hs: list[np.ndarray]) -> dict:
    p = len(Hs)
    assert p >= 2
    n = Hs[0].shape[0]
    for H in Hs:
        assert H.shape == (n,n) and np.allclose(H,H.T)
    M = np.zeros((p*(p-1)//2*n*(n-1)//2, p*n))
    b = np.zeros(M.shape[0])
    row = 0
    for a in range(p):
        for c in range(a+1,p):
            C = Hs[a]@Hs[c]-Hs[c]@Hs[a]
            for i in range(n):
                for j in range(i+1,n):
                    M[row,a*n+i] += Hs[c][i,j]
                    M[row,a*n+j] -= Hs[c][i,j]
                    M[row,c*n+i] -= Hs[a][i,j]
                    M[row,c*n+j] += Hs[a][i,j]
                    b[row] = -C[i,j]
                    row += 1
    x,*_ = np.linalg.lstsq(M,b,rcond=1e-11)
    e=np.linalg.norm(M@x-b)
    norm=np.linalg.norm(b)
    # A true solution has zero residual.  A positive least-squares gap is
    # a numerical obstruction, not an exact rational certificate.
    return {
        "n":n, "generator_count":p,
        "linear_unknowns":int(M.shape[1]),
        "linear_equations":int(M.shape[0]),
        "analysis_rank":int(np.linalg.matrix_rank(M,tol=1e-9)),
        "commutator_rhs_norm":float(norm),
        "least_squares_gap":float(e),
        "relative_gap":float(e/max(norm,1e-15)),
        "compatible_to_1e_9":bool(e<1e-9),
    }


def real_weyl_maxent_basis(m:int)->np.ndarray:
    """Columns are normalized realified Weyl purifications, size 2m²."""
    vectors=[]
    for a in range(m):
        for b in range(m):
            W=np.zeros((m,m),dtype=complex)
            for j in range(m):
                W[j,(j+a)%m]=np.exp(2j*np.pi*b*j/m)
            vectors.extend([
                np.concatenate([W.real,W.imag],axis=1).ravel()/np.sqrt(m),
                np.concatenate([-W.imag,W.real],axis=1).ravel()/np.sqrt(m),
            ])
    B=np.array(vectors).T
    assert np.linalg.norm(B.T@B-np.eye(2*m*m))<1e-9
    return B


def edge(m,i,j):
    H=np.zeros((m,m))
    H[i,j]=H[j,i]=1
    return H


def demo():
    print("Commuting diagonal source observables, first basis product:")
    print(linear_compatibility([np.diag([1.,0.,-1.]),
                                np.diag([0.,1.,-1.])]))
    print("Noncommuting source path, first basis product:")
    print(linear_compatibility([edge(3,0,1),edge(3,1,2)]))
    print("Noncommuting source path, maximally entangled first basis:")
    for m in (2,3,4):
        B=real_weyl_maxent_basis(m)
        H=edge(m,0,1)
        K=edge(m,1,2) if m>2 else np.diag([1.,-1.])
        r=2*m
        A=B.T@np.kron(H,np.eye(r))@B
        C=B.T@np.kron(K,np.eye(r))@B
        print(m,linear_compatibility([A,C]))


if __name__=="__main__":
    demo()
