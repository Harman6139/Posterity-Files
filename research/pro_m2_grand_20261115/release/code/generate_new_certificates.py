#!/usr/bin/env python3
"""Exact examples for the new angular-grid and interior-path theorems.
Only standard-library arithmetic. These certificates do not simulate long paths
and do not implement the general real-algebraic decision procedure.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from math import isqrt
import json
ROOT=Path(__file__).resolve().parents[1]

def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,dict): return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [encode(v) for v in x]
    return x

def gram(atoms,n):
    return [[sum((w*v[i]*v[j] for w,v in atoms),F(0)) for j in range(n)] for i in range(n)]

def scalar_grid(q):
    return sorted({sign*F(q*q-j*j,q*q+j*j) for j in range(q+1) for sign in (-1,1)})

def distribution(grid,y,e):
    if y in (-1,1): return [(F(1),y)]
    a,b=next((a,b) for a,b in zip(grid,grid[1:]) if a<=y<=b)
    v=(y-a)*(b-y); vmax=1-y*y
    beta=(e*vmax-v)/(vmax-v) if vmax!=v else F(0)
    if not 0<=beta<=1: raise ValueError('invalid variance interpolation')
    out={x:F(0) for x in grid}
    out[a]+=(1-beta)*(b-y)/(b-a); out[b]+=(1-beta)*(y-a)/(b-a)
    out[-1]+=beta*(1-y)/2; out[1]+=beta*(1+y)/2
    return [(w,x) for x,w in out.items() if w]

def angular_cases():
    cases=[]
    for q in (1,2,3,5,11):
        G=scalar_grid(q); e=F(1,q*q+1); y=[F(2,7),F(-3,5)]
        laws=[distribution(G,a,e) for a in y]
        atoms=[(w1*w2,[F(1),x1,x2]) for w1,x1 in laws[0] for w2,x2 in laws[1]]
        target=[[F(1),y[0],y[1]],[y[0],y[0]**2+e*(1-y[0]**2),y[0]*y[1]],
                [y[1],y[0]*y[1],y[1]**2+e*(1-y[1]**2)]]
        eps_bad=e/2; a=G[-2]; u=1-e/2
        value=(u-a)*(u-1)+eps_bad*(1-u*u)
        if value>=0: raise AssertionError('bad sharpness witness')
        cases.append(dict(q=q,grid=G,epsilon=e,target=target,atoms=atoms,
                          bad_epsilon=eps_bad,witness_mean=u,sharp_value=value))
    return cases

def lifted_atoms(base,r,v):
    out=[]
    for w,t,y in base:
        for signs in product((-1,0,1),repeat=r):
            mass=w
            for s in signs: mass*=1-v if s==0 else v/2
            out.append((mass,[F(t)]+[F(s*t) for s in signs]+[F(y)]))
    return out

def path_cases():
    out=[]
    for r,N in ((2,4),(2,2**64),(3,2**32)):
        a=2*3**r+4*5**r; b=3**r+2*5**r; c=3**r+5**r
        zeta=4*3**(r-1)+10*5**(r-1); U=F(N*N+N+1); T=F(2*N+1,2); n=r+2
        atoms=lifted_atoms([(F(1,2),1,0),(F(1,2),N,1),(F(1,2),N+1,1)],r,F(1,2))
        A=gram(atoms,n); crossings=[]
        for s in sorted({2,3,N//2,N}):
            if not 2<=s<=N: continue
            lam=F(s*c-b,T-s); chi=a-s*b+lam*(U-s*T)
            v=(zeta+lam*U/2)/(a+lam*U)
            normals=lifted_atoms([(chi,1,0),(c+lam,s,1)],r,v)
            crossings.append(dict(s=s,lambda_value=lam,chi=chi,variance=v,normals=normals))
        out.append(dict(r=r,N=str(N),n=n,anchor_parameters=[a,b,c,zeta],objective=A,
                        target_atoms=atoms,crossings=crossings,pivots=str(N-1),
                        normalization_square_root=2*n*(N+1),
                        certificate_kind='symbolic N-1 theorem with sampled exact facet identities, not a simulation'))
    return out

def obstruction():
    A0=[[0,2,0,0],[2,0,0,0],[0,0,2,0],[0,0,0,1]]
    A1=[[1,0,0,0],[0,2,0,0],[0,0,0,1],[0,0,1,0]]
    W0=[[2,0,0,0],[0,1,0,0],[0,0,0,-2],[0,0,-2,0]]
    W1=[[0,-1,0,0],[-1,0,0,0],[0,0,1,0],[0,0,0,2]]
    return dict(A0=A0,A1=A1,W0=W0,W1=W1,rational_kernel_determinant=-8,
                field_polynomial=[-2,0,1],positive_root_interval=['7/5','3/2'])

def main():
    data=dict(angular_grids=angular_cases(),interior_paths=path_cases(),arithmetic_obstruction=obstruction())
    path=ROOT/'certificates'/'new_exact_certificates.json'; path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(encode(data),indent=2)+'\n')
    print(path)
if __name__=='__main__': main()
