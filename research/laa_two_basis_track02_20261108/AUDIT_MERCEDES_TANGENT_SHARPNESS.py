#!/usr/bin/env python3
"""Numerical consistency audit for Milestone 29, not its mathematical proof."""
import numpy as np
v=np.array([[1,-.5,-.5],[0,np.sqrt(3)/2,-np.sqrt(3)/2]])
c=.5
G=np.column_stack([np.sqrt(2/3)*np.r_[v[:,j],c] for j in range(3)]+[np.array([0.,0.,1/np.sqrt(2)])])
q=np.array([np.outer(g,g)[np.triu_indices(3)] for g in G.T]).T
assert np.linalg.norm(G@G.T-np.eye(3))<1e-12
assert np.linalg.matrix_rank(q)==4
A=np.diag([1.,-1.]); x=np.array([-1.,0.])
H=np.zeros((3,3));H[:2,:2]=A;H[:2,2]=x;H[2,:2]=x
meas=lambda Z:np.einsum('ij,ij->j',G,Z@G)
T=[]
for i in range(2):
    for j in range(i,2):
        B=np.zeros((3,3));B[i,j]=B[j,i]=1;T.append(meas(B))
for i in range(2):
    B=np.zeros((3,3));B[i,2]=B[2,i]=1;T.append(meas(B))
T=np.array(T).T
print('frame_error',np.linalg.norm(G@G.T-np.eye(3)))
print('source_measurement_rank',np.linalg.matrix_rank(q))
print('tangent_kernel_residual',np.linalg.norm(meas(H)))
print('tangent_rank',np.linalg.matrix_rank(T),'tangent_nullity',5-np.linalg.matrix_rank(T))
Zstar=np.diag([1.,1.,0.])
for t in [.4,.2,.1,.03,.01]:
    Z=np.block([[np.eye(2)+t*A,(t*x)[:,None]],[(t*x)[None,:],np.array([[t*t/(1+t)]])]])
    rr=np.linalg.norm(meas(Z-Zstar));err=np.linalg.norm(Z-Zstar)
    print(dict(t=t,data_over_t2=float(rr/t**2),
               error_over_t=float(err/t),min_eigen=float(np.linalg.eigvalsh(Z)[0])))
    assert np.linalg.eigvalsh(Z).min()>-1e-12
