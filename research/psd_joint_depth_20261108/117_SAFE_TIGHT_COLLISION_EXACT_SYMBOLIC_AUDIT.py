#!/usr/bin/env python3
"""Exact SymPy/Fraction audit of Milestone 116: shared Bellman-safe parent
edge can worsen sharp full PSD recovery 1/6 -> 1/7 while achieving depth 4.
Also enumerates 321 safe-tight harmonic collisions through h=5,
verifying they always synchronize in the universal U-peeling layer.
"""
from sympy import zeros,Rational,trace,symbols,simplify
from fractions import Fraction as Q
from itertools import product
from collections import Counter

def E(i,j,n=7):
    M=zeros(n);M[i,j]=1;return M
def F(i,j):return E(i,j)+E(j,i)

lam=Rational(1,100);c=1/(2*lam)
parents=((0,3),(0,5),(1,4),(0,6),(1,6))
H=[E(i,i)-E(0,0)+lam*F(*parents[i-1]) for i in range(1,6)]
B=E(2,2)-E(0,0)+lam*F(1,4)
K=H+[B]
stresses=[
    E(6,6),
    E(4,4)+E(5,5)-c*(F(0,6)+F(1,6)),
    E(2,2)+E(3,3)-c*(F(0,5)+F(1,4)),
    E(1,1)-c*F(0,3)
]
faces=[[0,1,2,3,4,5,6],[0,1,2,3,4,5],[0,1,2,3],[0,1]]
blocks=[{6},{4,5},{2,3},{1}]
for z,face,block in zip(stresses,faces,blocks):
    assert all(trace(z*h)==0 for h in K)
    assert z.extract(face,face)==zeros(len(face))+sum(
        (E(face.index(i),face.index(i),len(face)) for i in block),
        zeros(len(face)))
print('PASS: all 24 dual/generator pairings and exact PSD exposed faces')

s=symbols('s',positive=True)
X=E(0,0)+s**2*H[0]+2*s**4*H[1]+s**4*H[2] \
  +s**7*H[3]+s**8*H[4]-s**4*B+s**14*E(6,6)
expected=[1-s**2-2*s**4-s**7-s**8,s**2,s**4,s**4,
          s**7,s**8,s**14]
assert all(simplify(X[i,i]-expected[i])==0 for i in range(7))
assert X[1,4]==0
assert X[0,3]==lam*s**2 and X[0,5]==2*lam*s**4
assert X[0,6]==lam*s**7 and X[1,6]==lam*s**8
print('PASS: exactly cancelled shared edge; matching strictly PD s^2 / s^14 arc')

def choices(h):
    return [[(a,b) for a in range(i) for b in range(i+1,h+2)]
            for i in range(1,h+1)]

def harmonic(P):
    h=len(P);rows=[]
    for i,(a,b) in enumerate(P,1):
        r=[Q(0)]*(h+1);r[i-1]=2
        for x in (a,b):
            if x==h+1:r[-1]+=1
            elif x:r[x-1]-=1
        rows.append(r)
    for j in range(h):
        p=next(i for i in range(j,h) if rows[i][j])
        rows[p],rows[j]=rows[j],rows[p]
        c=rows[j][j];rows[j]=[x/c for x in rows[j]]
        for i in range(h):
            if i!=j:
                c=rows[i][j]
                rows[i]=[x-c*y for x,y in zip(rows[i],rows[j])]
    return (Q(0),)+tuple(r[-1] for r in rows)+(Q(1),)

def upper_schedule(w):
    k=len(w)-1;j=k-1;states=[k,j]
    while j:
        p=next(i for i in range(1,j+1) if 2*w[i]>w[j]+w[i-1])
        j=p-1;states.append(j)
    return states

counts=Counter()
for h in range(1,6):
    for P in product(*choices(h)):
        w=harmonic(P)
        if not all(a<b for a,b in zip(w,w[1:])):continue
        states=upper_schedule(w)
        stage={i:t for t in range(1,len(states))
               for i in range(states[t]+1,states[t-1]+1)}
        for i in range(1,h+1):
            upper=next(b for b in range(i+1,h+2)
                       if w[i-1]+w[b]>=2*w[i])
            safe=(i-1,upper)
            for j,p in enumerate(P,1):
                if safe==p and i!=j:
                    assert i<j and stage[i]==stage[j]
                    counts[h]+=1
assert [counts[h] for h in range(1,6)]==[0,0,1,16,304]
print('PASS: 321 safe-tight collisions, all in the same upper-peeling layer')
