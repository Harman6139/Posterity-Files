#!/usr/bin/env python3
"""Exact certificates for fixed-block local-search hardness (standard library).
The finite tests check formulas, not the universal theorems.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import factorial, gcd, lcm, ceil
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def zeros(n,m=None): return [[Q(0) for _ in range(n if m is None else m)] for _ in range(n)]
def eye(n): return [[Q(i==j) for j in range(n)] for i in range(n)]
def tr(A): return list(map(list,zip(*A)))
def mm(A,B): return [[sum((x*y for x,y in zip(row,col)),Q(0)) for col in zip(*B)] for row in A]
def add(A,B): return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def scale(A,t): return [[t*x for x in row] for row in A]
def outer(v): return [[x*y for y in v] for x in v]
def gram(atoms,n):
    A=zeros(n)
    for w,v in atoms: A=add(A,scale(outer(v),w))
    return A

def dot(A,B): return sum((x*y for a,b in zip(A,B) for x,y in zip(a,b)),Q(0))
def solve(A,b):
    m=[list(map(Q,a))+[Q(v)] for a,v in zip(A,b)]; n=len(m)
    for j in range(n):
        p=next((i for i in range(j,n) if m[i][j]),None)
        if p is None: raise ValueError('singular system')
        m[j],m[p]=m[p],m[j]; t=m[j][j]; m[j]=[x/t for x in m[j]]
        for i in range(n):
            if i!=j:
                t=m[i][j]; m[i]=[x-t*y for x,y in zip(m[i],m[j])]
    return [a[-1] for a in m]
def inv(A): return tr([solve(A,[int(i==j) for j in range(len(A))]) for i in range(len(A))])
def principal(A,S): return [[A[i][j] for j in S] for i in S]
def intervals(n): return [[Q(a<=i<=b) for i in range(n)] for a in range(n) for b in range(a,n)]
def canonical(n):
    A=eye(n)
    for i in range(n-1): A[i][i+1]=A[i+1][i]=-Q(1,2)
    return A

def coefficient(A,i,j):
    n=len(A)
    def f(a,b): return A[a][b] if 0<=a<n and 0<=b<n else Q(0)
    return f(i,j)-f(i-1,j)-f(i,j+1)+f(i-1,j+1)

def make_seed(n,weighted=False):
    t=Q(1,2)+Q(1,16*n*n); F=eye(n)
    for i in range(n):
        if weighted: F[i][i]+=Q(i%3,256*n**3)
        w=t+(Q(i+1,256*n**4) if weighted else 0)
        F[i][(i+1)%n]=F[(i+1)%n][i]=w
    M=[[F[i][j] if i==j else -F[i][j] for j in range(n-1)] for i in range(n-1)]
    h=solve(M,[1]*(n-1)); D=h+[Q(1)]
    C=gram([(Q(1),v) for v in intervals(n)],n); eps=Q(1,32*n**5)
    B=add([[D[i]*F[i][j]*D[j] for j in range(n)] for i in range(n)],scale(C,eps))
    W=[[Q(-1 if ((i-j)%n in (1,n-1)) else 1)/(D[i]*D[j]) for j in range(n)] for i in range(n)]
    mu=Q(1,4*n*n); gamma=-dot(W,B)/2; omega=Q(n); beta=sum(sum(row) for row in B)
    tb=gamma/(4*sum(B[i][i] for i in range(n))); eta=min(Q(1),mu/2,min(min(row) for row in B)/2,gamma/(4*(omega+tb)),eps/8)
    proper=[]
    for drop in range(n):
        S=[i for i in range(n) if i!=drop]; FS=principal(F,S)
        MS=[[FS[i][j] if i==j else -FS[i][j] for j in range(n-1)] for i in range(n-1)]
        v=solve(MS,[1]*(n-1)); atoms=[]
        for i in range(n-1):
            u=[Q(0)]*(n-1);u[i]=D[S[i]];atoms.append((Q(1)/v[i],u))
        for i,j in combinations(range(n-1),2):
            if FS[i][j]:
                u=[Q(0)]*(n-1);u[i]=D[S[i]]/v[i];u[j]=D[S[j]]/v[j]
                atoms.append((FS[i][j]*v[i]*v[j],u))
        for u in intervals(n):
            vv=[u[i] for i in S]
            if any(vv):atoms.append((eps,vv))
        assert gram(atoms,n-1)==principal(B,S)
        proper.append(dict(drop=drop,atoms=atoms))
    B0=principal(B,list(range(n-1))); exposure=[(coefficient(B0,i,j),[int(i<=k<=j) for k in range(n-1)]) for i in range(n-1) for j in range(i,n-1)]
    assert gram(exposure,n-1)==B0 and all(w>0 for w,v in exposure)
    return dict(n=n,weighted=weighted,t=t,F=F,comparison=M,h=h,C=C,epsilon=eps,B=B,W=W,
                mu=mu,gamma=gamma,omega=omega,beta=beta,eta=eta,t_B=tb,proper=proper,exposure=exposure)

def constants(seed,m):
    n=seed['n'];r=n-1;d=n*(n+1)//2; H=canonical(r);Hi=inv(H)
    K=max(sum(abs(x) for x in row) for row in Hi);Y=2*(2*n)**r;MH=Y+n
    FH=factorial(d-1)*(2*MH*MH)**(d-1);qb=lcm(*(x.denominator for row in seed['B'][:r] for x in row[:r]))
    B=seed['B'];T=2*sum(B[i][-1] for i in range(r))+B[-1][-1]+n+1
    sm=1+r*K*(Q(1,2)+Q(5,2)*m+Q(1,2));N=ceil(8*qb*FH*T*sm)
    return dict(m=str(m),q_B=str(qb),F_H=str(FH),s_m=sm,N=str(N),N_bits=N.bit_length(),K_H=K)

def rays_of_canonical(n):
    ids=list(combinations(range(n),2));positions=[(i,i) for i in range(n)]+ids
    A=[[v[i]*v[j]*(1 if i==j else 2) for i,j in positions] for v in intervals(n)]
    cols=tr(inv(A));out=[]
    for values in cols:
        den=lcm(*(x.denominator for x in values)); iv=[int(x*den) for x in values];g=gcd(*iv);iv=[x//g for x in iv]
        R=zeros(n)
        for (i,j),x in zip(positions,iv):R[i][j]=R[j][i]=Q(x)
        out.append(R)
    return out

def shear_cases(seed):
    n=seed['n'];r=n-1;out=[]
    for k in ([0]*r,[i+1 for i in range(r)],[2**64 if i==0 else 0 for i in range(r)]):
        m=max(1,max(k));cs=constants(seed,m);N=int(cs['N'])
        U=eye(n)
        for i in range(r):U[i][-1]=-Q(k[i])
        P=mm(tr(U),mm(canonical(n),U)); Ui=eye(n)
        for i in range(r): Ui[i][-1]=Q(k[i])
        active=[[row[0] for row in mm(Ui,[[x] for x in v])] for v in intervals(n)]
        rays=[mm(tr(U),mm(R,U)) for R in rays_of_canonical(n)]
        BN=[[seed['B'][i][j]*(N if i<r else 1)*(N if j<r else 1) for j in range(n)] for i in range(n)]
        costs=[dot(BN,R) for R in rays]
        out.append(dict(k=list(map(str,k)),P=P,active=active,rays=rays,costs=costs,constants=cs))
    return out

def spn_cases():
    out=[]
    for G in ([[2,1,0],[1,3,0],[0,0,1]],[[1,0,0],[0,0,0],[0,0,2]]):
        G=[[Q(x) for x in row] for row in G];z=[Q(1),Q(0),Q(2)]; ell=[Q(0),Q(3),Q(0)]
        L=eye(3)+[[-x for x in z]]; P=mm(L,mm(G,tr(L)));N=zeros(4)
        for i in range(3):N[i][-1]=N[-1][i]=ell[i]
        N[-1][-1]=2;A=add(P,N)
        out.append(dict(G=G,z=z,ell=ell,PSD=P,nonnegative=N,matrix=A))
    return out

def graph_cases():
    records=[]
    for k in product(range(5),repeat=2):
        records.append(dict(k=list(k),b=[-Q(x)-Q(1,2) for x in k],c=Q(1+sum(x*(x+1) for x in k)),active=[[a,b,1] for a in (k[0],k[0]+1) for b in (k[1],k[1]+1)]))
    return dict(vertices=records,ball_counts=[(R,(R+1)*(R+2)//2) for R in range(8)],huge_k=[str(2**64),str(2**64+1)])

def encode(x):
    if isinstance(x,Q):return str(x)
    if isinstance(x,dict):return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def main():
    seeds=[make_seed(n,w) for n,w in [(5,False),(7,False),(9,False),(11,False),(7,True)]]
    scales=[dict(seed=i,cases=[constants(s,m) for m in (1,16,2**64)]) for i,s in enumerate(seeds)]
    shears=[dict(seed=i,cases=shear_cases(seeds[i])) for i in (0,1)]
    R=zeros(3);R[0][1]=R[1][0]=Q(1,2);R[0][2]=R[2][0]=-Q(1,2)
    B=eye(3);B[0][2]=B[2][0]=Q(1,4)
    data=dict(schema='finite_templates_hardness_v1',seeds=seeds,scales=scales,shears=shears,spn=spn_cases(),graph=graph_cases(),boundary=dict(B=B,R=R,canonical=canonical(3)))
    p=ROOT/'certificates'/'exact_certificates.json';p.parent.mkdir(exist_ok=True);p.write_text(json.dumps(encode(data),indent=2)+'\n')
    print('wrote',p, 'bytes',p.stat().st_size)
    print('scale bits',[(s['seed'],[x['N_bits'] for x in s['cases']]) for s in scales])
if __name__=='__main__':main()
