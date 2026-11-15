#!/usr/bin/env python3
"""Exact finite identities and transcript-consistency diagnostics.
The all-dimensional lower bound is proved in manuscript 27, not by this script.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import numpy as np

C=F(1,64)
def dyadic_power(i:int,t:F)->F:
    if i<1: raise ValueError('i must be positive')
    if t==0: return F(1)
    a,b=t.numerator,t.denominator
    power=i**abs(a)
    fl=(power.bit_length()-1)//b
    if a>=0: exponent=fl
    else: exponent= -(fl if power==2**(b*fl) else fl+1)
    return F(2**exponent) if exponent>=0 else F(1,2**(-exponent))

def scales(beta:F,N:int):
    t=(2*beta-1)/(2*(2*beta+1))
    return [dyadic_power(i,t) for i in range(1,N+1)]

def energy(x,sigma):
    return C*((x[0]-1)**2+sum((x[i]-sigma[i]/sigma[i+1]*x[i+1])**2 for i in range(len(x)-1)))

def prefix_point(sigma,k):
    n=len(sigma)
    if not 0<=k<n: raise ValueError('need 0<=k<N')
    resist=[s**-2 for s in sigma[:k]]
    R=F(1)+sum(resist)
    xx=[F(0)]*n
    for i in range(k): xx[i]=sigma[i]*sum(resist[i:])/R
    return xx,R

def quadratic_value_grad(x,sigma):
    n=len(x); ratio=sigma[:-1]/sigma[1:]
    dif=x[:-1]-ratio*x[1:]
    val=float(C)*((x[0]-1)**2+dif@dif)
    g=np.zeros(n);g[0]=2*float(C)*(x[0]-1)
    g[:-1]+=2*float(C)*dif
    g[1:]-=2*float(C)*ratio*dif
    return val,g

def complement_direction(v,basis,rng):
    w=v.copy()
    for _ in range(2):
        for e in basis: w-=e@w*e
    if np.linalg.norm(w)<1e-10:
        w=rng.normal(size=len(v))
        for _ in range(2):
            for e in basis:w-=e@w*e
    return w/np.linalg.norm(w)

def resisting_demo(beta=F(2),calls=9):
    rng=np.random.default_rng(20261113);n=2*calls+2
    ss=np.array([float(s) for s in scales(beta,n)])
    basis=[];transcript=[];previous_g=np.zeros(n)
    for k in range(calls):
        # Arbitrary dense, adaptive, unbounded-in-principle query; not a span algorithm.
        x=3*rng.normal(size=n)-(.3+k)*previous_g
        basis.append(complement_direction(x,basis,rng))
        basis.append(complement_direction(rng.normal(size=n),basis,rng))
        U=np.array(basis).T
        coords=np.zeros(n);coords[:len(basis)-1]=U[:,:-1].T@x
        value,g=quadratic_value_grad(coords,ss)
        assert np.linalg.norm(g[len(basis):])==0
        returned=U@g[:len(basis)]
        transcript.append((x.copy(),value,returned.copy()))
        previous_g=returned
    out=5*rng.normal(size=n)-previous_g
    basis.append(complement_direction(out,basis,rng))
    basis.append(complement_direction(rng.normal(size=n),basis,rng))
    U=np.array(basis).T
    errors=[]
    for x,value,g in transcript:
        vnew,gnew=quadratic_value_grad(U.T@x,ss)
        errors.append(max(abs(vnew-value),float(np.linalg.norm(U@gnew-g))))
    vv,_=quadratic_value_grad(U.T@out,ss)
    minval=float(C)/(1+sum(1/ss[:2*calls+1]**2))
    assert max(errors)<1e-10
    assert vv>=minval-1e-12
    return {'calls':calls,'chain_dimension':n,'max_transcript_discrepancy':max(errors),
            'basis_orthogonality_error':float(np.linalg.norm(U.T@U-np.eye(n))),
            'output_value':vv,'proved_prefix_minimum':minval}

def main():
    exact=[]
    for beta in [F(1,4),F(1,2),F(1),F(2),F(4)]:
        sigma=scales(beta,40)
        assert all(sigma[i]/sigma[i+1] in (F(1,2),F(1),F(2)) for i in range(39))
        tested=0
        for k in [0,1,2,3,7,19,39]:
            xx,R=prefix_point(sigma,k)
            assert energy(xx,sigma)==C/R
            assert sum(a*a for a in xx)<=sum(s*s for s in sigma[:k])
            # Exact stationarity in each allowed coordinate.
            for i in range(k):
                plus=xx.copy();minus=xx.copy();plus[i]+=1;minus[i]-=1
                assert energy(plus,sigma)==energy(minus,sigma)
            tested+=1
        sv=np.array([float(s) for s in sigma]);N=len(sigma)
        B=np.zeros((N,N));B[0,0]=1
        for i in range(N-1):B[i+1,i]=1;B[i+1,i+1]=-sv[i]/sv[i+1]
        maxeig=float(np.linalg.eigvalsh(2*float(C)*B.T@B)[-1]); assert maxeig<1
        exact.append({'beta':str(beta),'exact_prefix_minima_tested':tested,
                      'couplings':sorted(set(str(sigma[i]/sigma[i+1]) for i in range(39))),
                      'numerical_Hessian_max_eigenvalue':maxeig})
    result={'exact_prefix_checks':exact,'arbitrary_query_resisting_oracle_demo':resisting_demo(),
            'scope':'Exact rational finite identities and numerical transcript diagnostics; universal proof is manuscript 27.'}
    path=Path(__file__).with_name('WEIGHTED_CHAIN_RESULTS.json');path.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
