#!/usr/bin/env python3
"""Exact construction of every reciprocal exponent at maximal sparse depth.
Each nu>=2, nu<=q<=2**(nu-1), yields exact depth nu, exponents 1/q,1/(2q).
All arithmetic is rational; companion proof: 17_MAXIMAL_DEPTH_RECIPROCAL_SPECTRUM.md.
"""
from fractions import Fraction as F

def build(nu, q):
    assert nu >= 2 and nu <= q <= 2**(nu-1)
    ell={}
    if nu==2:
        ell[2]=3
    elif q<=2*nu-2:
        k=q-nu
        for j in range(2,nu+1):ell[j]=j+1
        if k:ell[k+1]=k+3
    else:
        old=build(nu-1,(q+1)//2)
        for j in range(3,nu+1):ell[j]=old['ell'][j-1]+1
        ell[2]=nu+1 if q%2==0 else nu

    c={nu+1:1}
    for j in range(nu,1,-1):
        assert j+1<=ell[j]<=nu+1
        c[j]=sum(c[i] for i in range(j+1,ell[j]+1))
    assert sum(c.values())==q
    w={nu+1:F(0),1:F(1)}
    for j in range(nu,1,-1):
        w[j]=F(sum(c[i] for i in range(j+1,nu+2)),q)
    parents={j:(j-1,ell[j]) for j in range(2,nu+1)}
    assert w[nu]==F(1,q)
    assert all(w[a]+w[b]==2*w[j] for j,(a,b) in parents.items())
    assert all(w[j-1]>w[j] for j in range(2,nu+2))
    return {'ell':ell,'c':c,'w':w,'parents':parents}

def peeling(parents,nu):
    remaining=set(range(1,nu+2));layers=[]
    while remaining!={nu+1}:
        candidate=remaining-{nu+1}
        while True:
            bad={j for j in candidate if j in parents
                 and all(p in remaining for p in parents[j])
                 and not all(p in candidate for p in parents[j])}
            if not bad:break
            candidate-=bad
        assert candidate
        layers.append(tuple(sorted(candidate)))
        remaining-=candidate
    return layers

if __name__=='__main__':
    trials=0
    for nu in range(2,13):
        for q in range(nu,2**(nu-1)+1):
            d=build(nu,q)
            assert peeling(d['parents'],nu)==[(j,) for j in range(1,nu+1)]
            trials+=1
    print(f'PASS: {trials} exact all-q midpoint and peeling checks (2<=nu<=12)')
