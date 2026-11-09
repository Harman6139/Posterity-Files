#!/usr/bin/env python3
"""Exact Fraction audit for Milestone 125:
- the unique strict 5-internal harmonic policy with weights
  (1/4,3/7,1/2,17/28,5/7);
- two-sided integer peeling bounds L=3,U=5;
- every possible off-face terminal block of H3 and H4;
- the forbidden grade-aligned proposed exposure {6},{4,5},{2,3},{1};
- a distinct-edge tied-game construction with same weights,
  sharp alpha=1/4 and actual exposing layers {6},{5},{2,3,4},{1}.
The dense impossibility itself follows from positive coefficient/stress
orthogonality in checkpoint 125, independent of game enumeration.
"""
from fractions import Fraction as F
from itertools import product

def solve(policy):
    h=len(policy);rows=[]
    for i,(a,b) in enumerate(policy,1):
        r=[F(0)]*(h+1);r[i-1]=2
        for p in (a,b):
            if p==h+1:r[-1]+=1
            elif p:r[p-1]-=1
        rows.append(r)
    for j in range(h):
        p=next(i for i in range(j,h) if rows[i][j])
        rows[p],rows[j]=rows[j],rows[p]
        c=rows[j][j];rows[j]=[x/c for x in rows[j]]
        for i in range(h):
            if i!=j:
                c=rows[i][j]
                rows[i]=[x-c*y for x,y in zip(rows[i],rows[j])]
    return (F(0),)+tuple(r[-1] for r in rows)+(F(1),)

def integer_bounds(w):
    k=len(w)-1
    lo=[k,k-1];j=k-1
    while j:
        j=sum(1 for i in range(1,j) if 2*w[i]<w[j+1])
        lo.append(j)
    hi=[k,k-1];j=k-1
    while j:
        p=next(i for i in range(1,j+1) if 2*w[i]>w[j]+w[i-1])
        j=p-1;hi.append(j)
    return lo,hi

def exact_peeling(modes):
    h=len(modes);remain=set(range(h+2));layers=[]
    while remain!={0}:
        C=remain-{0}
        while True:
            bad={i for i in C if i<=h and any(
                all(a in remain and b in remain for a,b in mode) and
                not any(a in C and b in C for a,b in mode)
                for mode in modes[i-1])}
            if not bad:break
            C-=bad
        assert C
        layers.append(tuple(sorted(C)));remain-=C
    return tuple(layers)

def main():
    P=((0,3),(1,4),(0,6),(3,5),(2,6))
    w=solve(P)
    expected=(F(0),F(1,4),F(3,7),F(1,2),F(17,28),F(5,7),F(1))
    assert w==expected
    assert integer_bounds(w)==([6,5,2,0],[6,5,4,3,1,0])

    # Exact midpoint pair and terminal off-face supports.
    h=5
    for child,exact_midpoint in [(3,(0,6)),(4,(3,5))]:
        pairs=[(a,b) for a in range(child) for b in range(child+1,h+2)
               if w[a]+w[b]==2*w[child]]
        assert pairs==[exact_midpoint],(child,pairs)
        terminal=[(a,6) for a in range(child) if w[a]+w[6]<=2*w[child]]
        assert terminal==[(0,6)],(child,terminal)
        assert all(w[a]+w[b]>2*w[child]
                   for a,b in [(4,4),(4,5),(5,5)]
                   if child==3 or (a,b)!=(4,4))

    # Realized alternate degree-4 schedule, all physical edges DISTINCT.
    modes=(
        (((0,3),),),
        (((0,5),(1,4)),),
        (((0,6),),((2,4),)),
        (((3,5),),),
        (((2,6),),)
    )
    edges=[e for group in modes for mode in group for e in mode]
    assert len(edges)==len(set(edges))
    for i,group in enumerate(modes,1):
        assert min(max((w[a]+w[b])/2 for a,b in mode)
                   for mode in group)==w[i]
    assert exact_peeling(modes)==((6,),(5,),(2,3,4),(1,))
    print('PASS: dense two-coefficient off-face bottleneck and alternate tied-game schedule')
    print('weights:',', '.join(map(str,w)))
    print('primal/dual grade bounds:',integer_bounds(w))
    print('realized degree-4 layers:',exact_peeling(modes))
if __name__=='__main__':main()
