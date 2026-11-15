#!/usr/bin/env python3
"""Exact family certificates. No pivot trajectory is simulated."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def zeros(n): return [[F(0) for _ in range(n)] for _ in range(n)]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def transpose(a): return [list(c) for c in zip(*a)]
def multiply(a,b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0))
             for j in range(len(b[0]))] for i in range(len(a))]
def scaled(a,s): return [[s*x for x in row] for row in a]
def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,int): return str(x)
    if isinstance(x,list): return [encode(t) for t in x]
    if isinstance(x,dict): return {k:encode(v) for k,v in x.items()}
    return x

def active_subset(n,k,common=False):
    r=n-2; out=[]
    def add(t,y,z=None): out.append([t]+([0]*r if z is None else z)+[y])
    add(1,0)
    for j in range(r):
        for sign in (-1,1):
            z=[0]*r; z[j]=sign; add(1,0,z)
    for i in range(r):
        for j in range(i+1,r):
            z=[0]*r; z[i]=z[j]=1; add(1,0,z)
    t=k+1 if common else k
    add(t,1)
    for j in range(r):
        z=[0]*r; z[j]=1; add(t,1,z)
    if not common: add(k+1,1)
    return out

def case(n,m):
    d=n*(n+1)//2; N=100*factorial(d-1)*(2*(m+1)**2)**(d-1)
    B=zeros(n); B[0][0]=N*N; B[-1][-1]=F(29,10)
    for j in range(1,n-1):B[j][j]=F(9,10)*N*N
    for j,value in ((0,F(1)),(1,F(9,10)),(2,F(-9,10))):
        B[j][-1]=B[-1][j]=value*N
    Q=zeros(n); ids=[0,1,2,n-1]
    small=[[4,2,-2,0],[2,0,-2,-2],[-2,-2,0,2],[0,-2,2,1]]
    for i in range(4):
        for j in range(4):Q[ids[i]][ids[j]]=F(small[i][j])
    D=[F(N)]*(n-1)+[F(1)]
    W=[[Q[i][j]/(D[i]*D[j]) for j in range(n)] for i in range(n)]
    eta=F(3,40*n*N*N)
    for j in range(n): W[j][j]+=eta
    S=eye(n); T=eye(n)
    for j in range(1,n-1):S[j][0]=2;T[j][0]=-2
    S[-1][0]=1;T[-1][0]=-1
    A=scaled(B,F(1,2*n*N*N))
    Ap=scaled(multiply(multiply(S,B),transpose(S)),F(1,6*n*N*N))
    Wp=multiply(multiply(transpose(T),W),T)
    crossings=[]
    for k in sorted({1,max(1,m//2),m}):
        P=zeros(n);P[0][0]=1;P[0][-1]=P[-1][0]=-F(2*k+1,2);P[-1][-1]=k*k+k+1
        ray=zeros(n);ray[0][-1]=ray[-1][0]=-1;ray[-1][-1]=2*(k+1)
        Ek=factorial(d-1)*(2*(k+1)**2)**(d-1)
        crossings.append(dict(k=k,perfect_form=P,forward_ray=ray,ray_height_bound=Ek,
                              active_basis=active_subset(n,k),common_basis=active_subset(n,k,True),
                              off_face_cost_lower=F(N*N,10)-F(28,5)*N*Ek-F(29,10)*Ek,
                              forward_cost=-2*N+F(29,5)*(k+1),
                              backward_cost=2*N-F(29,5)*k,
                              mixed_cost_lower=F(N,5)))
    return dict(n=n,m=m,N=N,raw_target=B,target=A,strict_separator=W,cone_margin=eta,
                transform=S,inverse_transform=T,positive_target=Ap,positive_separator=Wp,
                positive_radius=F(1,30000*n**3*N*N),
                positive_margin=F(3,200*n*n*N*N),
                negative_pairing_bound=-F(1,80*n*N*N),
                distance_lower=F(1,3600*n*n*N*N),crossings=crossings)

def main():
    payload=dict(description='Symbolic prefix theorem with exact finite identity checks; not a trajectory simulation',
                 cases=[case(n,m) for n,m in ((4,1),(4,7),(4,2**64),(5,3),(6,257),(8,2**16))])
    out=ROOT/'certificates'/'all_local_certificates.json';out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(encode(payload),indent=2)+'\n')
    print('Wrote',out)

if __name__=='__main__':main()
