#!/usr/bin/env python3
"""Numerical sanity tests for Milestone 31. Requires numpy; not a proof."""
import numpy as np
import json

def compiler(G):
    d,M=G.shape
    assert np.allclose(G@G.T,np.eye(d))
    A=[np.r_[G[:,j],s*G[:,k]]/np.sqrt(2*M)
       for j in range(M) for k in range(M) for s in (-1,1)]
    B=[v for j in range(M) for v in
       (np.r_[G[:,j],np.zeros(d)],np.r_[np.zeros(d),G[:,j]])]
    hs=[np.eye(d)[:,i]/np.sqrt(d) for i in range(d)]
    hs += [v for i in range(d) for k in range(i+1,d)
           for v in ((np.eye(d)[:,i]+np.eye(d)[:,k])/np.sqrt(2*d),
                     (np.eye(d)[:,i]-np.eye(d)[:,k])/np.sqrt(2*d))]
    C=[np.r_[h,s*h]/np.sqrt(2) for h in hs for s in (-1,1)]
    return np.column_stack(A+B+C)/np.sqrt(3)

def symvec(H):
    return H[np.triu_indices(H.shape[0])]

def test(G,name):
    d,M=G.shape
    Q=compiler(G)
    originals=np.column_stack([symvec(np.outer(v,v)) for v in G.T])
    compiled=np.column_stack([symvec(np.outer(v,v)) for v in Q.T])
    q=np.linalg.matrix_rank(originals,tol=1e-9)
    expected=d*(d+1)//2+d*d+q
    observed=np.linalg.matrix_rank(compiled,tol=1e-9)
    assert observed==expected
    assert np.linalg.norm(Q@Q.T-np.eye(2*d))<1e-10
    maxerr=0
    for f in Q.T:
        a,b=f[:d],f[d:]
        pull=np.outer(a,a)-np.outer(b,b)+np.dot(b,b)*np.eye(d)
        coeff=np.linalg.lstsq(originals,symvec(pull),rcond=None)[0]
        maxerr=max(maxerr,np.linalg.norm(originals@coeff-symvec(pull)))
    assert maxerr<1e-10
    return dict(name=name,d=d,M=M,q=q,raw_frame=Q.shape[1],
                expected_span=expected,actual_span=observed,
                parseval_error=float(np.linalg.norm(Q@Q.T-np.eye(2*d))),
                max_source_pullback_error=float(maxerr),
                final_N_bound=int(3*d*d+7*d+2*q+4))

def main():
    tetra=np.array([[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]],float)/2
    et=1/4
    cols=[]
    for j in (0,2):
        for s in (-1,1):
            for t in (-1,1):
                v=np.zeros(4);v[j]=.5;v[1]=s*et/2;v[3]=t*et/2
                cols.append(v)
    cols += [np.sqrt(1-2*et*et)*np.eye(4)[:,1],
             np.sqrt(1-2*et*et)*np.eye(4)[:,3]]
    print(json.dumps([test(tetra,"tetrahedron_no_admissible_source_ONB"),
                      test(np.column_stack(cols),"missing_edge_half_Holder"),
                      test(np.eye(2),"two_diagonal_measurements")],indent=2))

if __name__=="__main__": main()
