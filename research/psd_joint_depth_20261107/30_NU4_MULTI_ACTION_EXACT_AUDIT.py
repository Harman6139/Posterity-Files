#!/usr/bin/env python3
"""Exact Fraction audit for the multiaction theorem in checkpoint 29."""
from fractions import Fraction as F
from itertools import combinations

def solve(policy):
    h=len(policy); a=[[F(0) for _ in range(h)] for _ in range(h)];b=[F(0)]*h
    for i,(p,q) in enumerate(policy):
        a[i][i]=F(2)
        for j in p,q:
            if j==h+1:b[i]+=1
            elif j:a[i][j-1]-=1
    rows=[a[i]+[b[i]] for i in range(h)]
    for j in range(h):
        p=next((i for i in range(j,h) if rows[i][j]),None)
        if p is None:return None
        rows[p],rows[j]=rows[j],rows[p]
        c=rows[j][j];rows[j]=[x/c for x in rows[j]]
        for i in range(h):
            if i!=j:
                c=rows[i][j];rows[i]=[x-c*y for x,y in zip(rows[i],rows[j])]
    return tuple(row[-1] for row in rows)

def peel(actions):
    h=len(actions);remain=set(range(h+2));layers=[]
    while remain!={0}:
        C=remain-{0}
        while True:
            bad={i for i in C if 1<=i<=h and any(p in remain and q in remain and
                (p not in C or q not in C) for p,q in actions[i-1])}
            if not bad:break
            C-=bad
        if not C:return None
        layers.append(tuple(sorted(C)));remain-=C
    return tuple(layers)

cases=[
(F(3,16),(F(3,8),F(1,2),F(3,4)),((0,3),(0,4),(2,4)),1,
{(1,(0,2)):F(1,8),(3,(0,2)):F(1,16),(3,(1,2)):F(1,12),(3,(1,4)):F(1,6)},()),
(F(3,16),(F(1,4),F(3,8),F(1,2)),((0,3),(1,3),(0,4)),2,
{(2,(0,1)):F(1,16)},((3,(0,1)),(3,(1,2)))),
(F(3,14),(F(3,7),F(5,7),F(6,7)),((0,3),(1,4),(2,4)),1,
{(1,(0,2)):F(1,6),(2,(0,4)):F(3,16),(2,(1,3)):F(1,5),
 (3,(0,2)):F(1,14),(3,(0,4)):F(1,8),(3,(1,2)):F(1,10)},()),
]

def test():
    total=0
    for alpha,w,base,target,proper,improper in cases:
        assert solve(base)==w
        v=(F(0),)+w+(F(1),)
        assert v[target]==2*alpha
        used=set(base)|{(0,target)}
        safe={};unsafe={};nonproper=set()
        for j in range(1,4):
            for edge in combinations([x for x in range(5) if x!=j],2):
                if edge in used:continue
                if v[edge[0]]+v[edge[1]]>=2*v[j]:
                    safe.setdefault(j,[]).append(edge)
                else:
                    policy=list(base);policy[j-1]=edge
                    u=solve(policy)
                    if u is None or min(u)<=0:nonproper.add((j,edge))
                    else:unsafe[(j,edge)]=u[target-1]/2
        assert unsafe==proper,(w,unsafe,proper)
        assert nonproper==set(improper),(w,nonproper)
        assert all(x<alpha for x in unsafe.values())
        maximal=tuple(tuple([base[j-1]]+safe.get(j,[])) for j in range(1,4))
        layers=peel(maximal)
        if w[0]==F(3,7):assert layers==((4,),(2,3),(1,))
        else:assert layers==((4,),(3,),(1,2))
        total+=len(unsafe)+len(nonproper)+sum(map(len,safe.values()))
        print('PASS',alpha,w,'safe depth',len(layers),'unsafe',len(unsafe)+len(nonproper))
    print('PASS',total,'exact candidate edges')

if __name__=='__main__':test()
