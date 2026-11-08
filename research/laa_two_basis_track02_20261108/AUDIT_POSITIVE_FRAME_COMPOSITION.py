#!/usr/bin/env python3
"""Independent numerical checks of Milestone 24; requires numpy, scipy.
Run from this directory. NOT a replacement for analytic proof.
"""
import numpy as np
from AUDIT_TWO_ZERO_NAIMARK import tetrahedron, double_zero_dilation


def positive_dilation(V):
    n=V.shape[0]
    G=np.hstack([np.eye(n)/np.sqrt(2),V/np.sqrt(2)])
    G=np.hstack([G[:,:1]/np.sqrt(2),G[:,:1]/np.sqrt(2),G[:,1:]])
    M=G.shape[1];h=.1
    a=np.sqrt((5+3*h*h)/7);b=np.sqrt((1-5*h*h)/7)
    cols=[]; weights=[]
    for i in range(n):
        e=np.eye(n)[:,i]
        cols.extend([a*e,b*e,b*e]);weights.extend([-1,2,3])
    for g in G.T:
        cols.append(h*g);weights.append(4)
    A=np.column_stack(cols);weights=np.array(weights,dtype=float)
    assert np.linalg.norm(A@A.T-np.eye(n))<1e-8
    assert np.linalg.norm((A*weights)@A.T)<1e-8
    rs=h*G.sum(axis=1); t=2*np.sqrt(M+1)
    z=np.zeros(A.shape[1])
    for i in range(n):
        z[3*i]=(2*rs[i]+t)/(3*a)
        z[3*i+1]=-(5*rs[i]+4*t)/(3*b)
        z[3*i+2]=t/b
    z[3*n:]=1
    assert np.linalg.norm(A@z)<1e-8
    assert np.linalg.norm(A@(weights*z))<1e-8
    ss=z@z; qq=(weights*z)@z
    eta=1/(1e7*len(z)*(M+1))
    for k in range(1,5000):
        e2=eta*(1+k/5000)
        Gram=A.T@A+e2*np.outer(z,z)
        if (np.min(np.abs(Gram[np.triu_indices(len(z),1)]))>1e-13
            and np.min(np.abs(np.diag(Gram)-.5))>.05):
            break
    else: raise RuntimeError("anchor separation failed")
    v2=.01
    x2=(2+e2*(qq-2*ss)+2*v2)/3
    y2=(1-e2*(ss+qq)-5*v2)/3
    assert x2>0 and y2>0
    F=np.block([[A,np.zeros((n,3))],
                [np.sqrt(e2)*z[None,:],np.array([[np.sqrt(x2),np.sqrt(y2),np.sqrt(v2)]])]])
    D=np.r_[weights,-1,2,4]
    P=F.T@F;Q=np.eye(F.shape[1])-P;R=P-Q
    cert=np.diag(D)+R@np.diag(D)@R
    ev=np.linalg.eigvalsh(Q@cert@Q)
    gap=min(ev[ev>1e-7])
    assert gap>=1.999
    i=3*n;j=len(D)-1
    theta=.007
    O=np.eye(len(D))
    O[i,i]=np.cos(theta);O[j,j]=np.cos(theta)
    O[i,j]=np.sin(theta);O[j,i]=-np.sin(theta)
    U=R@O
    assert np.linalg.norm(F@F.T-np.eye(n+1))<1e-8
    assert np.linalg.norm((F*D)@F.T)<1e-8
    assert np.linalg.norm(np.diag(D)+U@np.diag(D)@U.T-cert)<1e-8
    assert np.min(np.abs(U))>1e-13
    return F,U,float(gap)


def main():
    G=tetrahedron()
    F0,U0,gap0=double_zero_dilation(G)
    F1,U1,gap1=positive_dilation(U0)
    n=U0.shape[0]
    source=np.array([[1.,.2,.1],[.2,1.,.4],[.1,.4,.8]])
    Y0=F0.T@source@F0
    W=F1.T@np.block([[Y0,np.zeros((n,1))],[np.zeros((1,n)),np.ones((1,1))]])@F1
    a1=np.diag(W);a2=np.diag(U1.T@W@U1)
    assert np.min(np.r_[a1,a2])>0
    assert U1.shape[0]==5*n+4
    print({"source_order":3,"source_frame_size":4,"zero_layer_order":n,
           "positive_layer_order":U1.shape[0],
           "min_basis_overlap":float(np.min(np.abs(U1))),
           "min_observation":float(np.min(np.r_[a1,a2])),
           "two_list_difference":float(np.linalg.norm(a1-a2)),
           "frame_error":float(np.linalg.norm(F1@F1.T-np.eye(n+1))),
           "exposing_gap":gap1,"zero_layer_gap":gap0})


if __name__=="__main__":
    main()
