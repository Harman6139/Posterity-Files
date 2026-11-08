#!/usr/bin/env python3
"""Diagnostic numerical verification for Milestone 26.
Analytic statements/proofs are in 26_SHARP_EXPONENT_HALVING_COUNTEREXAMPLE.md.
Requires numpy and scipy. Results are NOT the proof.
"""
import numpy as np
from scipy.linalg import null_space

eta=zeta=.25
cols=[];coeff=[]
for h,sgn in [(0,-1),(2,1)]:
    for s in (-1,1):
        for t in (-1,1):
            g=np.zeros(4)
            g[h]=.5;g[1]=s*eta/2;g[3]=t*zeta/2
            cols.append(g);coeff.append(-sgn*s/(4*eta))
cols.extend([np.sqrt(1-2*eta*eta)*np.eye(4)[:,1],
             np.sqrt(1-2*zeta*zeta)*np.eye(4)[:,3]])
coeff.extend([0,0])
G=np.column_stack(cols);c=np.array(coeff)
K=null_space(G).T;P=G.T@G;F=np.hstack([G,np.zeros((4,6))])
U=np.block([[K.T,P],[np.zeros((6,6)),K]])
phi=F.T@np.eye(4)[:,1]
v=np.r_[c,K@c]
Zstar=np.diag([1.,1.,0.,0.])
Ystar=F.T@Zstar@F
meas=lambda Y:np.r_[np.diag(Y),np.diag(U.T@Y@U)]
tri=np.triu_indices(4)
rank=np.linalg.matrix_rank(np.column_stack([np.outer(g,g)[tri] for g in G.T]))
assert rank==9
assert np.allclose(G@G.T,np.eye(4))
assert np.allclose(G@c,0)
assert np.allclose(U.T@U,np.eye(16))
assert abs(v@v-16)<1e-10
print("Frame rank",rank,"N",U.shape[0],"||G c||",np.linalg.norm(G@c))
print("t, residual/t^4, compressed_error/t, polynomial_identity_error, rank-three_eig")
for t in (.4,.2,.1,.03,.01):
    w=np.sqrt(1-t*t)*np.eye(4)[:,0]+t*np.eye(4)[:,2]
    Y=np.outer(F.T@w,F.T@w)+np.outer(phi+t*t*v,phi+t*t*v)
    dY=Y-Ystar
    residual=meas(dY)
    exact=t**4*meas(np.outer(v,v))
    err=np.linalg.norm(F@Y@F.T-Zstar)
    assert np.linalg.norm(residual-exact)<1e-10
    assert abs(err-np.sqrt(2)*t)<1e-10
    assert np.linalg.eigvalsh(Y)[-3]<1e-10
    print(t,np.linalg.norm(residual)/t**4,err/t,
          np.linalg.norm(residual-exact),np.linalg.eigvalsh(Y)[-3])
