#!/usr/bin/env python3
"""Construct exact certificates. These finite checks do not replace the universal proof."""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial, gcd, lcm
from pathlib import Path
import json, sys, hashlib
if hasattr(sys, 'set_int_max_str_digits'): sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'certificates'
def zero(n): return [[F(0) for _ in range(n)] for _ in range(n)]
def eye(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def pair(A,B): return sum((dot(x,y) for x,y in zip(A,B)),F(0))
def encode(x):
    if isinstance(x,F): return str(x)
    if isinstance(x,int) and abs(x)>2**53: return str(x)
    if isinstance(x,dict): return {k:encode(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)): return [encode(v) for v in x]
    return x
def rref(a):
    A=[list(map(F,row)) for row in a]; piv=[]; i=0
    for j in range(len(A[0])):
        p=next((k for k in range(i,len(A)) if A[k][j]),None)
        if p is None: continue
        A[i],A[p]=A[p],A[i]; v=A[i][j]; A[i]=[t/v for t in A[i]]
        for k in range(len(A)):
            if k!=i and A[k][j]:
                v=A[k][j]; A[k]=[x-v*y for x,y in zip(A[k],A[i])]
        piv.append(j); i+=1
        if i==len(A): break
    return A,piv
def solve(A,b):
    M,p=rref([list(row)+[v] for row,v in zip(A,b)])
    if p[:len(A)]!=list(range(len(A))): return None
    return [M[i][-1] for i in range(len(A))]
def primitive(v):
    den=lcm(*(x.denominator for x in v)); a=[int(x*den) for x in v]
    g=gcd(*a); return tuple(x//g for x in a)
def interval_vector(n,a,b): return [int(a<=i<=b) for i in range(n)]
def tridiag(n):
    T=eye(n)
    for i in range(n-1): T[i][i+1]=T[i+1][i]=F(-1,2)
    return T
def data(n,m):
    r=n-1; d=n*(n+1)//2; q=2*n; Y=2*q**r; U=2*Y*n*n*(m+1)
    E=factorial(d-1)*(2*U*U)**(d-1); N=20000*n**3*E*E
    eps=F(1,100*n**3); rho=F(1,1600*n**4*N*N)
    ds=[F(1)]*n; ds[1]=ds[2]=F(8,5)
    C=[[F((min(i,j)+1)*(n-max(i,j))) for j in range(n)] for i in range(n)]
    base=eye(n); H=zero(n); ids=[0,1,2,3,n-1]
    for i in ids:
        for j in ids: H[i][j]=1
    for k,i in enumerate(ids):
        j=ids[(k+1)%5]; base[i][j]=base[j][i]=F(3,5); H[i][j]=H[j][i]=-1
    B=[[ds[i]*base[i][j]*ds[j]+eps*C[i][j] for j in range(n)] for i in range(n)]
    W0=[[H[i][j]/(ds[i]*ds[j]) for j in range(n)] for i in range(n)]
    sn=[N]*r+[1]
    BN=[[sn[i]*B[i][j]*sn[j] for j in range(n)] for i in range(n)]
    A=[[x/(4*n*N*N) for x in row] for row in BN]
    W=[[W0[i][j]/(sn[i]*sn[j])+F(i==j,20*n*N*N) for j in range(n)] for i in range(n)]
    weights={(a,b):eps*(1+(b==r-1)) for a in range(r) for b in range(a,r)}
    for i,w in enumerate([F(1,25),F(8,125),F(8,125),F(1,25)]): weights[i,i]+=w
    for i,w in enumerate([F(24,25),F(192,125),F(24,25)]): weights[i,i+1]+=w
    for i in range(4,r): weights[i,i]+=1
    return dict(n=n,m=m,r=r,d=d,q=q,Y=Y,U=U,E=E,N=N,N_bits=N.bit_length(),
                epsilon=eps,radius=rho,B=B,A=A,W=W,interval_weights=[[a,b,w] for (a,b),w in weights.items()],
                max_center_coordinate_bits=max(max(abs(x.numerator).bit_length(),x.denominator.bit_length()) for row in A for x in row),
                guaranteed_pivots=m,scope='Universal proof prefix, not a simulated trajectory')
def canonical_rays(n, family):
    intervals=[(a,b) for a in range(n) for b in range(a,n)]
    pairs=[(i,j) for i in range(n) for j in range(i,n)]
    normals=[]
    for a,b in intervals:
        v=interval_vector(n,a,b)
        normals.append([v[i]*v[j]*(1 if i==j else 2) for i,j in pairs])
    out=[]; B=family['B']; N=family['N']; sn=[N]*(n-1)+[1]
    for k,iv in enumerate(intervals):
        x=solve(normals,[int(i==k) for i in range(len(intervals))]); x=primitive(x)
        R=zero(n)
        for (i,j),v in zip(pairs,x): R[i][j]=R[j][i]=F(v)
        cost=sum((sn[i]*B[i][j]*sn[j]*R[i][j] for i in range(n) for j in range(n)),F(0))
        out.append(dict(interval=iv,ray=R,improving=cost<0))
    return dict(n=n,rays=out)
def kkt(b):
    r=len(b); T=tridiag(r)
    for size in range(r+1):
        for S in combinations(range(r),size):
            z=[F(0)]*r
            if S:
                vals=solve([[T[i][j] for j in S] for i in S],[-b[i] for i in S])
                for i,x in zip(S,vals): z[i]=x
            ell=[b[i]+dot(T[i],z) for i in range(r)]
            if min(z)>=0 and min(ell)>=0 and all(z[i]*ell[i]==0 for i in range(r)):
                return z,ell
    raise AssertionError('no KKT point')
def tq(u): return sum(x*x for x in u)-sum(x*y for x,y in zip(u,u[1:]))
def point(b,c):
    r=len(b); z,ell=kkt(b); gamma=c-tq(z)
    assert gamma>F(1,4), 'test driver uses the short exact y>=2 exclusion'
    bounds=[range(max(0,x.numerator//x.denominator-2),-(-x.numerator//x.denominator)+3) for x in z]
    active=[]; count=0
    for u in product(*bounds):
        v=tq(u)+2*dot(b,u)+c
        assert v>=1, ('infeasible finite-box neighbor',b,c,u)
        if v==1: active.append(list(u))
        count+=1
    assert len(rref([[2*x for x in u]+[1] for u in active])[1])==r+1
    return dict(b=b,c=c,z=z,ell=ell,gamma=gamma,active=active,finite_values_checked=count)
def rays_face(active):
    r=len(active[0]); rows=[[F(2*x) for x in u]+[F(1)] for u in active]; ans=set()
    for subset in combinations(rows,r):
        mat,piv=rref(subset)
        if len(piv)!=r: continue
        free=next(j for j in range(r+1) if j not in piv); v=[F(0)]*(r+1); v[free]=1
        for i,p in enumerate(piv): v[p]=-mat[i][free]
        v=primitive(v)
        for sgn in (1,-1):
            w=tuple(sgn*x for x in v)
            if all(dot(row,w)>=0 for row in rows): ans.add(w)
    return sorted(ans)
def branching(family, depth=3):
    n=family['n']; r=n-1; assert r==4
    b=[F(0)]*r; b[-1]=F(-1,2)
    pts=[point(b,F(1))]; levels=[0]; lookup={(tuple(b),F(1)):0}; edges=[]
    c0=[family['B'][i][-1] for i in range(r)]; a=family['B'][-1][-1]; N=family['N']
    pool=list(product(range(7),repeat=r)); i=0
    while i<len(pts):
        p=pts[i]; level=levels[i]; rays=rays_face(p['active']); p['all_face_rays']=[list(v) for v in rays]
        improving=[v for v in rays if 2*N*dot(c0,v[:-1])+a*v[-1]<0]
        p['improving_face_rays']=[list(v) for v in improving]
        if level<depth:
            for v in improving:
                ts=[]
                for u in pool:
                    rv=2*dot(v[:-1],u)+v[-1]
                    if rv<0:
                        slack=tq(u)+2*dot(p['b'],u)+p['c']-1
                        ts.append(slack/(-rv))
                assert ts
                t=min(ts); assert t>0
                nb=[x+t*y for x,y in zip(p['b'],v[:-1])]; nc=p['c']+t*v[-1]
                key=(tuple(nb),nc)
                if key not in lookup:
                    lookup[key]=len(pts); pts.append(point(nb,nc)); levels.append(level+1)
                j=lookup[key]; edges.append(dict(start=i,end=j,direction=list(v),length=t))
        i+=1
    return dict(n=n,depth=depth,vertices=pts,levels=levels,edges=edges)
def main():
    families=[data(n,m) for n,m in [(5,1),(5,8),(5,2**64),(6,7),(8,2**16),(10,3)]]
    cert=dict(kind='ordinary_CP_canonical_all_rules',families=families,
              canonical=[canonical_rays(5,families[1]),canonical_rays(6,families[3])],
              branching_prefix=branching(families[1],3))
    OUT.mkdir(exist_ok=True)
    path=OUT/'exact_certificates.json'; path.write_bytes((json.dumps(encode(cert),indent=2)+'\n').encode('utf-8'))
    print(json.dumps(dict(sha256=hashlib.sha256(path.read_bytes()).hexdigest(),bytes=path.stat().st_size,
                         families=len(families),vertices=len(cert['branching_prefix']['vertices']),edges=len(cert['branching_prefix']['edges']),
                         largest_prefix=str(2**64),largest_prefix_N_bits=families[2]['N_bits']),indent=2))
if __name__=='__main__': main()
