#!/usr/bin/env python3
"""Numerical sanity checks for Milestone 34 (not part of the proof).
Run: python AUDIT_BALANCED_THREE_BLOCK.py  [requires numpy].
"""
import numpy as np
import json

def build(G):
    d,M=G.shape; I=np.eye(d); sel=[]
    for j in range(M):
        if np.linalg.matrix_rank(G[:,sel+[j]],tol=1e-9)>len(sel):sel.append(j)
        if len(sel)==d:break
    eps=1/(16*d)
    A=[]
    for a,b in ((0,1),(0,2),(1,2)):
        for j in sel:
            for k in sel:
                for sign in (-1,1):
                    v=np.zeros((3,d));v[a]=np.sqrt(eps)*G[:,j]
                    v[b]=sign*np.sqrt(eps)*G[:,k]
                    A.append(v.ravel())
    B=[]
    for j in range(M):
        for a in range(3):
            v=np.zeros((3,d))
            v[a]=np.sqrt(.75 if j in sel else 1)*G[:,j]
            B.append(v.ravel())
    H=[I[:,j]/np.sqrt(d) for j in range(d)]
    for j in range(d):
        for k in range(j+1,d):
            H.extend([(I[:,j]+I[:,k])/np.sqrt(2*d),
                      (I[:,j]-I[:,k])/np.sqrt(2*d)])
    def h(theta):
        return np.array([1/np.sqrt(3),
          np.sqrt(2/3)*np.cos(theta),np.sqrt(2/3)*np.sin(theta)])
    iso=[h(2*np.pi*j/3)/np.sqrt(2) for j in range(3)]
    iso +=[h(2*np.pi*j/5)*np.sqrt(3/10) for j in range(5)]
    C=[np.kron(z,u) for z in iso for u in H]
    return np.column_stack(A+B+C)/np.sqrt(2)

def audit(G,label):
    d,M=G.shape;F=build(G)
    tri=np.triu_indices(d)
    S=np.column_stack([np.outer(g,g)[tri] for g in G.T])
    q=np.linalg.matrix_rank(S,tol=1e-9)
    tri3=np.triu_indices(3*d)
    measured=np.column_stack([np.outer(f,f)[tri3] for f in F.T])
    rank=np.linalg.matrix_rank(measured,tol=1e-9)
    assert rank==4*d*d+d+q
    assert np.linalg.norm(F@F.T-np.eye(3*d))<1e-10
    worst=0.
    for f in F.T:
        a,b,c=f.reshape(3,d)
        pull=(np.outer(a,a)-.5*(np.outer(b,b)+np.outer(c,c))
              +(b@b+c@c)*np.eye(d))
        z=pull[tri]
        worst=max(worst,np.linalg.norm(S@np.linalg.lstsq(S,z,rcond=None)[0]-z))
    assert worst<1e-10
    u=np.eye(d)[:,0]
    assert np.linalg.eigvalsh(np.eye(d)-np.outer(u,u)/2)[0]>.49
    return dict(case=label,compressed_order=3*d,frame_cols=int(F.shape[1]),
                projector_rank=int(rank),predicted_rank=int(4*d*d+d+q),
                frame_error=float(np.linalg.norm(F@F.T-np.eye(3*d))),
                worst_source_pullback_error=float(worst),
                rankone_auxiliary_gap=.5)

def main():
    tet=np.array([[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]],float)/2
    print(json.dumps([audit(np.eye(2),'diagonal_d2'),audit(tet,'tetra_d3')],indent=2))

if __name__=="__main__":main()
