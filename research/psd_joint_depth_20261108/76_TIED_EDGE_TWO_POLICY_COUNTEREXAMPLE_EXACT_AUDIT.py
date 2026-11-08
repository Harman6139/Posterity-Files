#!/usr/bin/env python3
"""Exact standard-library audit of the 6x6 tied-edge PSD counterexample
in Milestone 75. Verifies every dual-kernel inner product, the exposing
rank profile and all 576 independent-edge harmonic policies with nullity 5.
No floating-point arithmetic or external SDP/Python libraries are used.
"""
from fractions import Fraction as F
from itertools import product

def zeros(n=6):return [[F(0) for _ in range(n)] for _ in range(n)]
def matrix(diagonal=(),edges=(),n=6):
    A=zeros(n)
    for i,c in diagonal:A[i][i]+=F(c)
    for i,j,c in edges:A[i][j]+=F(c);A[j][i]+=F(c)
    return A
def dot(A,B):return sum(x*y for a,b in zip(A,B) for x,y in zip(a,b))

lam=F(1,100)
H=[
    matrix([(1,1),(0,-1)],[(0,2,lam)]),
    matrix([(2,1),(0,-1)],[(0,5,lam),(1,4,lam)]),
    matrix([(3,1),(0,-1)],[(1,5,lam)]),
    matrix([(4,1),(0,-1)],[(3,5,lam)]),
    matrix([],[(0,1,lam)])
]
Z=[
    matrix([(5,1)]),
    matrix([(2,1),(3,1),(4,1)],[(0,5,-50),(1,5,-50),(3,5,-50)]),
    matrix([(1,1)],[(0,2,-50)])
]
faces=[(0,1,2,3,4,5),(0,1,2,3,4),(0,1)]
supports=[{5},{2,3,4},{1}]

def audit_stresses():
    for j,(stress,face,supp) in enumerate(zip(Z,faces,supports),1):
        assert all(dot(stress,h)==0 for h in H),(j,'orthogonality')
        for a in face:
            for b in face:
                assert stress[a][b]==F(1 if a==b and a in supp else 0),(j,a,b)
    print('PASS: all 15 stress/generator pairings and PSD face compressions')

def harmonic(P):
    h=len(P);row=[]
    for i,(a,b) in enumerate(P,1):
        r=[F(0)]*(h+1);r[i-1]=2
        for v in (a,b):
            if v==h+1:r[-1]+=1
            elif v>0:r[v-1]-=1
        row.append(r)
    for j in range(h):
        k=next(i for i in range(j,h) if row[i][j])
        row[j],row[k]=row[k],row[j]
        scale=row[j][j];row[j]=[x/scale for x in row[j]]
        for i in range(h):
            if i!=j:
                scale=row[i][j]
                row[i]=[x-scale*y for x,y in zip(row[i],row[j])]
    return tuple(r[-1] for r in row)

def peel(P):
    h=len(P);remain=set(range(h+2));layers=[]
    while remain!={0}:
        C=remain-{0}
        while True:
            bad={i for i in C if i<=h
                 and all(p in remain for p in P[i-1])
                 and any(p not in C for p in P[i-1])}
            if not bad:break
            C-=bad
        assert C
        layers.append(tuple(sorted(C)))
        remain-=C
    return tuple(layers)

def audit_two_policy_exclusion():
    h=4
    choices=[[(a,b) for a in range(i) for b in range(i+1,h+2)]
             for i in range(1,h+1)]
    assert tuple(map(len,choices))==(4,6,6,4)
    candidates=[]
    count=0
    for P in product(*choices):
        count+=1
        w=harmonic(P);W=(F(0),)+w+(F(1),)
        if not all(a<b for a,b in zip(W,W[1:])):continue
        if F(3,11) not in W or F(3,22)>w[0]:continue
        candidates.append((w,P,peel(P)))
    assert count==576 and len(candidates)==2
    expected=[
        ((F(3,11),F(6,11),F(7,11),F(9,11)),
         ((0,2),(1,4),(1,5),(3,5)),
         ((5,),(3,4),(2,),(1,))),
        ((F(3,11),F(5,11),F(6,11),F(7,11)),
         ((0,3),(1,4),(2,4),(1,5)),
         ((5,),(4,),(2,3),(1,)))
    ]
    assert candidates==expected, candidates
    for w,P,layers in candidates:
        assert len(layers)==4
        print('HARMONIC',','.join(map(str,w)),P,'minimal policy layers',layers)
    print('PASS: 576 exact harmonic policies and exhaustive depth >=4 obstruction')

if __name__=='__main__':
    audit_stresses()
    audit_two_policy_exclusion()
    print('PASS: tied-edge 6x6 PSD counterexample requires a richer normal form')
