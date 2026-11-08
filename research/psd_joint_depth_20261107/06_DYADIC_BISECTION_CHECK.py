#!/usr/bin/env python3
"""Exact Fraction reproducibility test for 05_UNIVERSAL_DYADIC_RIGIDITY.md.
The theorem is proved symbolically; this is not a proof by enumeration.
"""
from fractions import Fraction as F

def bisection(nu,a):
    assert nu>=2 and a%2==1 and 1<=a<2**(nu-1)
    x=F(a,2**(nu-1)); lo=F(0); hi=F(1)
    w={"O":F(0),"T":F(1)}; parents={}
    for j in range(1,nu):
        m=(lo+hi)/2
        v="v"+str(j)
        pa=next(z for z,u in w.items() if u==lo)
        pb=next(z for z,u in w.items() if u==hi)
        parents[v]=(pa,pb); w[v]=m
        if m<x:lo=m
        elif m>x:hi=m
        else:assert j==nu-1
    assert w["v"+str(nu-1)]==x
    assert min(w[z] for z in parents)>=x/2
    return x/2,w,parents

def peel_depth(w,parents):
    remaining=set(w); layers=[]
    while remaining!={"O"}:
        C=remaining-{"O"}
        while True:
            bad={v for v in C if v in parents
                 and all(p in remaining for p in parents[v])
                 and not all(p in C for p in parents[v])}
            if not bad:break
            C-=bad
        assert C
        layers.append(tuple(sorted(C)))
        remaining-=C
    return len(layers)

def run():
    count=0
    for nu in range(2,11):
        for a in range(1,2**(nu-1),2):
            alpha,w,parents=bisection(nu,a)
            assert all(2*w[v]==w[p]+w[q] for v,(p,q) in parents.items())
            degree=peel_depth(w,parents)
            lower=min(d for d in range(1,nu+1) if alpha>=F(1,2**d))
            assert degree==lower,(nu,a,degree,lower)
            count+=1
    print("PASS",count,"exact dyadic bisection/degree checks")
if __name__=="__main__":run()
