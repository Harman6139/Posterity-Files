#!/usr/bin/env python3
"""Numerical illustrations of the proved anchored DRS rates.
No floating-point slope is used as a premise of manuscript 28.
"""
import json,math
from pathlib import Path
import numpy as np

def psd(x):
    w,v=np.linalg.eigh((x+x.T)/2)
    return (v*np.maximum(w,0))@v.T

def ent(m,i,j):
    a=np.zeros((m,m)); a[i,j]=a[j,i]=1 if i==j else .5
    return a

def make(m,which):
    if which=='fast':
        mats=[ent(m,0,0),ent(m,0,1)];b=[0.,1.]
        for i in range(1,m-1):mats.append(ent(m,i,i)-ent(m,0,i+1));b.append(0.)
        exponent=2**(m-1)-1
    else:
        mats=[ent(m,m-1,m-1),ent(m,0,1)];b=[0.,-.5]
        for i in range(2,m):mats.append(2*ent(m,0,i)+ent(m,i-1,i-1));b.append(0.)
        for i in range(1,m):
            for j in range(i+1,m):mats.append(ent(m,i,j));b.append(0.)
        exponent=1/(2**(m-1)-1)
    A=np.array(mats).reshape(len(b),-1);b=np.array(b)
    correction=A.T@np.linalg.pinv(A@A.T)
    def aff(x):return (x.ravel()+correction@(b-A@x.ravel())).reshape((m,m))
    def T(x):
        u=aff(x);v=psd(2*u-x)
        return x+v-u,u,v
    return A,b,aff,T,exponent

def run(m,family,iters=60000):
    A,b,aff,T,exponent=make(m,family)
    x0=aff(np.zeros((m,m)));x=x0.copy();records=[];max_potential_violation=0.
    checks=set(np.unique(np.geomspace(20,iters,100).astype(int)))
    for k in range(iters):
        tx,u,v=T(x)
        if k>=1:
            diff=x-tx; vv=x-x0
            pot=k*np.sum(diff*diff)+2*np.sum(diff*vv)
            scale=max(1,k*np.sum(diff*diff),2*np.linalg.norm(diff)*np.linalg.norm(vv))
            max_potential_violation=max(max_potential_violation,float(pot/scale))
        if k in checks:
            records.append([k,float(np.linalg.norm(x-tx)),float(np.linalg.norm(x-x0)),
                            float(np.linalg.norm(u-psd(u))),float(np.linalg.norm(A@v.ravel()-b))])
        x=(x0+(k+1)*tx)/(k+2)
    tx,u,v=T(x);records.append([iters,float(np.linalg.norm(x-tx)),float(np.linalg.norm(x-x0)),
                              float(np.linalg.norm(u-psd(u))),float(np.linalg.norm(A@v.ravel()-b))])
    rr=np.array(records);sel=rr[:,0]>=iters/3
    slopes=[float(np.polyfit(np.log(rr[sel,0]),np.log(rr[sel,j]),1)[0]) for j in range(1,5)]
    assert max_potential_violation<1e-9
    return dict(order=m,family=family,escape_exponent=exponent,iterations=iters,
                predicted_residual_power=-1/(1+exponent),predicted_state_power=exponent/(1+exponent),
                observed_tail_slopes_residual_state_shadow_equations=slopes,
                largest_normalized_potential_violation=max_potential_violation,last=records[-1])

def scalar_probe(a,iters=30000):
    # T(x)=x+tau*(1+max(x,0))^(-1/a), nonexpansive for tau<=a.
    tau=min(1,a)/2; x=0.
    vals=[]
    for k in range(iters):
        tx=x+tau*(1+max(x,0))**(-1/a)
        if k>1000 and k%100==0:vals.append((k,abs(tx-x),x))
        x=(k+1)*tx/(k+2)
    ar=np.array(vals);sel=ar[:,0]>iters/2
    return dict(a=a,predicted_residual_power=-1/(a+1),
                observed_residual_power=float(np.polyfit(np.log(ar[sel,0]),np.log(ar[sel,1]),1)[0]))

if __name__=='__main__':
    result={'anchored_DRS':[run(2,'fast'),run(3,'fast'),run(3,'slow')],
            'nonexpansive_scalar_maps':[scalar_probe(a) for a in [.25,.5,1,2,4]],
            'scope':'Floating-point diagnostics; all-dimensional proofs and model qualifications are in manuscript 28.'}
    Path(__file__).with_name('HALPERN_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
