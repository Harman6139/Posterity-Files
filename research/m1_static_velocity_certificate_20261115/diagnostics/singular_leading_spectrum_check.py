"""Singular-spectrum example of Checkpoint 08. Floating-point diagnostics only."""
from pathlib import Path
import json
import numpy as np
from numba import njit

@njit(cache=True)
def run(z, steps):
    # r=2,s=3, cross space is all 2x3 matrices with C[0,0]=1.
    target=np.zeros((5,5));target[0,0]=target[2,2]=np.sqrt(2.)
    cross=np.zeros((2,3));cross[0,0]=1.
    records=np.zeros((3,5)); j=0
    for k in range(steps):
        u=np.zeros((5,5));u[:2,:2]=z[:2,:2]
        u[:2,2:]=z[:2,2:];u[2:,:2]=z[2:,:2]
        u[0,2]=u[2,0]=1.
        values,Q=np.linalg.eigh(2*u-z)
        v=(Q*np.maximum(values,0.))@Q.T
        d=v-u;z+=d
        n=k+1
        if n==1000 or n==10000 or n==100000:
            records[j]=np.array([n,np.linalg.norm(z/np.sqrt(n)-target),
                np.linalg.norm(np.sqrt(n)*d-target/2),
                np.linalg.norm(v[:2,2:]-cross),np.sqrt(n)*np.linalg.norm(d)])
            j+=1
    return records

if __name__=='__main__':
    rng=np.random.default_rng(20261115);out=[]
    for name in ['zero','random']:
        z=np.zeros((5,5)) if name=='zero' else rng.normal(size=(5,5))
        z=(z+z.T)/2
        out.append(dict(start=name,leading_rank=2,matrix_order=5,
            columns=['n','state_error','scaled_step_error','cross_selection_error','scaled_step_norm'],
            records=run(z,100000).tolist(),predicted_scaled_step_norm=1.))
    Path(__file__).with_name('singular_leading_spectrum_results.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
