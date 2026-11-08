#!/usr/bin/env python3
"""Exact profile-aware PSD midpoint spectrum of checkpoint 55.
Pure standard-library rational arithmetic. Enumerates strict harmonic graphs,
their exact peeling layers and all facial-rank-profile vertex blow-ups.
"""
from itertools import product
from collections import defaultdict
from fractions import Fraction as F

def solve(a,b):
    n=len(b)
    rows=[list(map(F,row))+[F(b[i])] for i,row in enumerate(a)]
    for j in range(n):
        p=next((i for i in range(j,n) if rows[i][j]),None)
        if p is None:return None
        rows[p],rows[j]=rows[j],rows[p]
        c=rows[j][j];rows[j]=[v/c for v in rows[j]]
        for i in range(n):
            if i==j:continue
            c=rows[i][j]
            if c:rows[i]=[v-c*w for v,w in zip(rows[i],rows[j])]
    return tuple(z[-1] for z in rows)

def networks(h):
    if not h:
        yield (),()
        return
    choices=[[(a,b) for a in range(i) for b in range(i+1,h+2)]
             for i in range(1,h+1)]
    for par in product(*choices):
        a=[[F(0) for _ in range(h)] for _ in range(h)]
        b=[F(0)]*h
        for i,(u,v) in enumerate(par):
            a[i][i]=2
            for z in (u,v):
                if z==h+1:b[i]+=1
                elif z:a[i][z-1]-=1
        w=solve(a,b)
        if w is not None and all(x<y for x,y in zip((F(0),)+w,w+(F(1),))):
            yield w,par

def peel(par):
    h=len(par)
    remain=set(range(h+2))
    layers=[]
    while remain!={0}:
        C=remain-{0}
        while True:
            bad={i for i in C if i<=h
                 and all(z in remain for z in par[i-1])
                 and not all(z in C for z in par[i-1])}
            if not bad:break
            C-=bad
        assert C
        layers.append(tuple(sorted(C)))
        remain-=C
    return tuple(layers)

def compositions(n,k):
    if k==1:yield(n,)
    else:
        for first in range(1,n-k+2):
            for tail in compositions(n-first,k-1):
                yield(first,)+tail

def profile_catalogue(nullity):
    out=defaultdict(dict)
    for h in range(nullity):
        for w,par in networks(h):
            layers=peel(par)
            c=tuple(len(x) for x in layers)
            d=len(c)
            wmin=w[0] if w else F(1)
            for doubled in w+(F(1),):
                alpha=doubled/2
                if alpha>wmin:continue
                for s in compositions(nullity,d):
                    if all(x>=y for x,y in zip(s,c)):
                        out[s].setdefault(alpha,(w,par,layers))
    return out

def check():
    expect={
        3:{1:1,2:3,3:4},
        4:{1:1,2:7,3:12,4:9},
        5:{1:1,2:23,3:49,4:32,5:20},
        6:{1:1,2:81,3:190,4:161,5:80,6:43}
    }
    for nu in range(3,7):
        ans=profile_catalogue(nu)
        for s,data in ans.items():
            assert all(len(p)==len(s) for _,_,p in data.values())
            assert all(alpha>0 for alpha in data)
        for d in range(1,nu+1):
            got={a for s,values in ans.items() if len(s)==d for a in values}
            assert len(got)==expect[nu][d],(nu,d,len(got))
        print('PASS nu=',nu,'profiles=',len(ans),'degrees',expect[nu])
if __name__=='__main__':check()
