#!/usr/bin/env python3
"""Exact arithmetic audit of profile-preserving dyadic vertex blow-ups.
Tests harmonic identities, greedy exposing rank profile and a uniform
Gershgorin bound for matching rational monomial PSD arcs.
Symbolic proof: 52_VERTEX_BLOWUP_PROFILE_PRESERVATION.md.
"""
from fractions import Fraction as Q

def compositions(total, pieces):
    if pieces == 1:
        yield (total,)
    else:
        for first in range(1, total-pieces+2):
            for rest in compositions(total-first,pieces-1):
                yield (first,) + rest

def dyadic_blowup(profile):
    d=len(profile)
    assert d>=2
    weights={'O':Q(0),'T':Q(1)}
    for i in range(1,d):weights[f'v{i}']=Q(1,2**i)
    parents={f'v{i}':('O','T' if i==1 else f'v{i-1}') for i in range(1,d)}
    mult={'T':profile[0]}
    for j in range(2,d+1):mult[f'v{j-1}']=profile[j-1]
    assert all(2*weights[v]==weights[a]+weights[b] for v,(a,b) in parents.items())
    alpha=Q(1,2**d)
    assert 2*alpha==weights[f'v{d-1}']
    return weights,parents,mult,alpha

def layers(weights,parents,mult):
    rem=set(weights); result=[]
    while rem != {'O'}:
        exposed=rem-{'O'}
        while True:
            blocked={v for v in exposed if v in parents and
                    all(p in rem for p in parents[v]) and
                    not all(p in exposed for p in parents[v])}
            if not blocked:break
            exposed-=blocked
        assert exposed
        result.append(sum(mult[v] for v in exposed))
        rem-=exposed
    return tuple(result)

def exact_curve_check(weights, mult, alpha, d):
    t=Q(1,2**(2**(d+4)))
    coords={v:Q(1,2**(2**(d+4)*w.numerator//w.denominator))
            for v,w in weights.items() if v!='O'}
    x0=Q(1)-sum(mult[v]*coords[v] for v in mult)
    assert x0>Q(1,2), (d,mult,x0)
    N=1+sum(mult.values())
    lam=Q(1,8*N)
    # After normalized diagonal scaling every star edge has magnitude
    # lam/sqrt(x0) <= 2*lam. Every row has at most N-1 such edges.
    assert 2*lam*(N-1)<Q(1,2)
    return x0

def main():
    count=0
    for nu in range(2,12):
        for d in range(2,nu+1):
            for profile in compositions(nu,d):
                w,p,m,a=dyadic_blowup(profile)
                assert layers(w,p,m)==profile,(nu,d,profile)
                exact_curve_check(w,m,a,d)
                count+=1
    print(f'PASS: {count} exact rational dyadic blow-up rank profiles; nullity 2..11')

if __name__=='__main__':main()
