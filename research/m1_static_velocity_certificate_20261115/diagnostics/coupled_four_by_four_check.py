"""Diagnostic for a coupled 4x4 family with data-independent speed V=I.
All conclusions are proved statically; these runs only check the implementation.
"""
import json
from pathlib import Path
import numpy as np
from numba import njit

@njit(cache=True)
def orbit(z,a,B,steps):
    data=np.zeros((3,4));j=0
    for k in range(steps):
        u=a+(B@(B.T@z.reshape(16))).reshape(4,4)
        vals,ev=np.linalg.eigh(2*u-z)
        v=(ev*np.maximum(vals,0.))@ev.T
        d=v-u;z=z+d
        if k+1==1000 or k+1==10000 or k+1==100000:
            data[j]=np.array([k+1,np.linalg.norm(z/np.sqrt(k+1)-np.eye(4)),
                              np.linalg.norm(np.sqrt(k+1)*d-np.eye(4)/2),
                              np.sqrt(k+1)*np.linalg.norm(d)])
            j+=1
    return data

def setup(q):
    C=np.diag([1.,0.]);a0=np.block([[np.zeros((2,2)),C],[C.T,np.zeros((2,2))]])
    l0=np.diag([1.,1.,0.,0.])
    S1=np.diag([1.,-1.]);S2=np.array([[0.,1.],[1.,0.]])
    D1=q*np.array([[1.,2.],[-1.,1.]])
    D2=q*np.array([[0.,1.],[2.,-2.]])
    A1=q*np.array([[1.,-1.],[-1.,-1.]])
    A2=q*np.array([[0.,2.],[2.,1.]])
    l1=np.block([[A1,D1],[D1.T,S1]])
    l2=np.block([[A2,D2],[D2.T,S2]])
    B=np.linalg.qr(np.column_stack([l0.ravel(),l1.ravel(),l2.ravel()]))[0]
    a=a0-(B@(B.T@a0.ravel())).reshape(4,4)
    return a,B

if __name__=='__main__':
    out=[]
    for q in [0.,1.,3.]:
        a,B=setup(q)
        out.append(dict(coupling=q,columns=['n','state_error','scaled_step_error','scaled_step_norm'],
                        results=orbit(np.zeros((4,4)),a,B,100000).tolist(),
                        predicted_scaled_step_norm=1.))
    Path(__file__).with_name('coupled_four_by_four_results.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
