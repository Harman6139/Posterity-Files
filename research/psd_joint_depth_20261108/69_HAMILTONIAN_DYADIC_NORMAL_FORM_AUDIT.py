#!/usr/bin/env python3
"""Exact-rational audit of denominator-saturated harmonic normal form (68).
Enumerates h! Hamiltonian parent circuits through h=7, verifies reduced
denominator at each stage and that every odd dyadic target is attained.
"""
from fractions import Fraction as F
from math import factorial

def circuits(h):
    def rec(w, parent):
        j=len(w)
        if j==h+1:
            yield w,parent
            return
        choices=[('O',F(0)),('T',F(1))]+[(f'X{k}',w[k]) for k in range(1,j-1)]
        assert len(choices)==j
        for name,y in choices:
            value=(w[j-1]+y)/2
            assert value.denominator==2**j
            yield from rec(w+[value],parent+[(f'X{j-1}',name)])
    yield from rec([F(0),F(1,2)],[])

def check():
    for h in range(1,8):
        c=list(circuits(h))
        assert len(c)==factorial(h)
        target_set={F(a,2**h) for a in range(1,2**h,2)}
        assert {w[-1] for w,_ in c}==target_set
        admissible=sum(w[-1]/2<=min(w[1:]) for w,_ in c)
        print(f'PASS h={h}: {len(c)} exact circuits; {len(target_set)} odd targets; {admissible} full-state-admissible circuits')
if __name__=='__main__':check()
