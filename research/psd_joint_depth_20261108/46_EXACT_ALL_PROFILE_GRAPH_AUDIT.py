#!/usr/bin/env python3
"""Exact-rational check of the universal endpoint graph for every facial
rank profile through nullity 10. Proof is in checkpoint 45; this tests
construction, harmonic identities, greedy peeling and closed exponent.
"""
from fractions import Fraction as F

def compositions(n, d):
    if d==1:
        yield (n,)
    elif d<=n:
        for x in range(1,n-d+2):
            for rest in compositions(n-x,d-1):
                yield (x,)+rest

def graph(s):
    d=len(s)
    q={j:2**s[j-1]-1 for j in range(2,d+1)}
    p={1:1}
    for j in range(2,d+1):p[j]=p[j-1]*q[j]
    D=sum(p.values())
    delta={j+1:F(p[j],D) for j in range(1,d+1)}
    M={1:F(1), d+1:F(0)}
    for j in range(d,1,-1): M[j]=M[j+1]+delta[j+1]
    weights={'O':F(0),'T':F(1)}
    parents={}
    for j in range(2,d+1):
        for h in range(1,s[j-1]+1):
            node=f'{j}:{h}'
            low=('O' if j==d else f'{j+1}:{s[j]}') if h==1 else f'{j}:{h-1}'
            high='T' if j==2 else f'{j-1}:{s[j-2]}'
            weights[node]=M[j-1]-F(1,2**h)*(M[j-1]-M[j+1])
            parents[node]=(low,high)
    assert len({tuple(sorted(t)) for t in parents.values()})==len(parents)
    assert all(weights[a]<weights[node]<weights[b] and
               weights[a]+weights[b]==2*weights[node]
               for node,(a,b) in parents.items())
    beta=F(2**(s[-1]-1)*p[d-1],D)
    assert min(weights[node] for node in parents)==beta
    return weights,parents,beta

def peel(weights,parents):
    remaining=set(weights);out=[]
    while remaining!={'O'}:
        expose=remaining-{'O'}
        while True:
            forbidden={v for v in expose if v in parents and
              all(a in remaining for a in parents[v]) and
              any(a not in expose for a in parents[v])}
            if not forbidden:break
            expose-=forbidden
        assert expose
        out.append(expose);remaining-=expose
    return out

def check():
    count=0
    for nu in range(2,11):
        for d in range(2,nu+1):
            for s in compositions(nu,d):
                weights,parents,beta=graph(s)
                layers=peel(weights,parents)
                assert len(layers)==d
                assert [len(x) for x in layers]==[1]+list(s[1:]),s
                count+=1
    print(f'PASS: {count} rational harmonic/peeling/profile checks, 2 <= nullity <= 10')

if __name__=='__main__':check()
