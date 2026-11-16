"""Floating-point checks of centered-shadow efficiency and exact ADMM conjugacy.
Neither test is an asymptotic or interval certificate.
"""
import json
from pathlib import Path
import numpy as np
from numba import njit

@njit(cache=True)
def averaged_two_by_two(n):
    h=int(n/np.log(n)); z=np.zeros((2,2)); total=np.zeros((2,2))
    for k in range(n+h):
        u=np.array([[z[0,0],1.],[1.,0.]])
        R=2*u-z
        vals,Q=np.linalg.eigh(R)
        v=(Q*np.maximum(vals,0.))@Q.T
        if n-h <= k < n+h: total+=v
        z+=v-u
    vbar=total/(2*h)
    r=vbar[0,0]
    # The exact static optimum is characterized by c+c^3/r^2=1.
    c=1.
    for _ in range(10): c-=(c+c**3/r**2-1)/(1+3*c*c/r**2)
    D=np.sqrt(2*(c-1)**2+c**4/r**2)
    delta=np.sqrt(2*(vbar[0,1]-1)**2+vbar[1,1]**2)
    return np.array([n,h,delta/D, np.log(n)**2*(delta/D-1),1/12])


def psd(z):
    d,q=np.linalg.eigh((z+z.T)/2)
    return (q*np.maximum(d,0))@q.T

def admm_conjugacy_check():
    weights=np.array([1.,2.,3.]);rhs=1.;m=4
    def pu(z):
        u=np.zeros_like(z);u[np.arange(3),np.arange(3)]=np.diag(z)[:3]
        c=z[:3,3]+weights*(rhs-weights@z[:3,3])/(weights@weights)
        u[:3,3]=c;u[3,:3]=c
        return u
    rng=np.random.default_rng(42)
    z=rng.normal(size=(m,m));z=(z+z.T)/2
    rev=2*pu(z)-z;v=psd(rev);lam=rev-v
    error=0.
    for _ in range(200):
        ud=pu(z);vd=psd(2*ud-z);zn=z+vd-ud
        x=pu(v-lam);vn=psd(x+lam);ln=lam+x-vn
        rn=vn+ln
        error=max(error,np.linalg.norm(rn-(2*pu(zn)-zn)),np.linalg.norm(v-vd))
        z,v,lam=zn,vn,ln
    return error

if __name__=='__main__':
    out={'columns':['center','half_width','efficiency_ratio','log_squared_loss','predicted_limit'],
         'averaging':[averaged_two_by_two(n).tolist() for n in [1000,10000,100000,1000000]],
         'max_admm_conjugacy_discrepancy':admm_conjugacy_check()}
    Path(__file__).with_name('averaging_admm_results.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
