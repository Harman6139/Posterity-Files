#!/usr/bin/env python3
"""Exact bounded integer-composition certificate test for maximal PSD facial
depth in the strict multi-action incidence family; checkpoint 72.

No numerical optimization or external modules.
"""
from fractions import Fraction as F
from functools import reduce
from math import gcd

def primitive_nondecreasing_parts(parts,total,least=1):
    if parts==0:
        if total==0:yield ()
        return
    for first in range(least,total//parts+1):
        for rest in primitive_nondecreasing_parts(parts-1,total-first,first):
            yield (first,)+rest

def parents_for(g,i):
    h=len(g)-1
    return [(a,b) for a in range(i) for b in range(i+1,h+2)
            if sum(g[a:i])==sum(g[i:b])]

def catalogue(h):
    out=set();certs=[]
    for D in range(h+1,2**h+1):
        for g in primitive_nondecreasing_parts(h+1,D):
            if reduce(gcd,g)!=1:continue
            choices=[parents_for(g,i) for i in range(1,h+1)]
            if any(not options for options in choices):continue
            certs.append((D,g,choices))
            S=[0]+[sum(g[:i]) for i in range(1,h+2)]
            for v in range(1,h+2):
                if S[v]<=2*g[0]:out.add(F(S[v],2*D))
    return out,certs

def check():
    expected={
        1:(1,2,()),
        2:(2,4,()),
        3:(6,9,()),
        4:(25,20,()),
        5:(132,46,(F(3,46),F(3,23),F(2,15)))
    }
    for h in range(1,6):
        values,certs=catalogue(h)
        exotic=tuple(sorted(x for x in values if x.numerator!=1))
        assert (len(certs),len(values),exotic)==expected[h]
        for D,g,opts in certs:
            w=(F(0),)+tuple(F(sum(g[:i]),D) for i in range(1,h+2))
            assert all(2*w[i]==w[a]+w[b] for i, choices in
                       enumerate(opts,1) for a,b in choices)
            assert all(g[i]<=g[i+1] for i in range(h))
            assert sum(g)==D and reduce(gcd,g)==1
        print(f'PASS: nullity={h+1}, integer gaps={len(certs)}, '
              f'exponents={len(values)}, nonreciprocals={list(map(str,exotic))}')
    print('PASS exact integer-gap classification through nullity 6')

if __name__=='__main__':check()
