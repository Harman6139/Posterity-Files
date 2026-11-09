#!/usr/bin/env python3
"""Exact Fraction verification of Milestone 107: one Bellman-neutral
edit can change MINIMAL PSD facial-reduction degree by TWO. Requires
only Python 3 standard library; no numerical SDP.
"""
from fractions import Fraction as Q

def harmonic(P):
    n=len(P);rows=[]
    for i,(a,b) in enumerate(P,1):
        row=[Q(0)]*(n+1);row[i-1]=2
        for p in (a,b):
            if p==n+1:row[-1]+=1
            elif p:row[p-1]-=1
        rows.append(row)
    for j in range(n):
        p=next(i for i in range(j,n) if rows[i][j])
        rows[j],rows[p]=rows[p],rows[j]
        c=rows[j][j];rows[j]=[v/c for v in rows[j]]
        for i in range(n):
            if i!=j:
                c=rows[i][j]
                rows[i]=[x-c*y for x,y in zip(rows[i],rows[j])]
    return (Q(0),)+tuple(row[-1] for row in rows)+(Q(1),)

def peel(P,extras=()):
    n=len(P);modes=[[(p,)] for p in P]
    for i,edge,kind in extras:
        if kind=='I':modes[i-1].append((edge,))
        elif kind=='T':modes[i-1][0]+= (edge,)
        else:raise ValueError(kind)
    R=set(range(n+2));layers=[]
    while R!={0}:
        C=R-{0}
        while True:
            bad={i for i in C if i<=n and any(
                all(a in R and b in R for a,b in mode)
                and not any(a in C and b in C for a,b in mode)
                for mode in modes[i-1])}
            if not bad:break
            C-=bad
        assert C
        layers.append(tuple(sorted(C)));R-=C
    return tuple(layers)

def run():
    P=((0,2),(0,6),(2,4),(3,5),(4,6))
    w=harmonic(P)
    assert w==(Q(0),Q(1,4),Q(1,2),Q(5,8),Q(3,4),Q(7,8),Q(1))
    assert (w[1]+w[4])/2==w[2]
    assert peel(P)==((6,),(2,3,4,5),(1,))
    assert peel(P,((2,(1,4),'I'),))==((6,),(5,),(4,),(2,3),(1,))
    assert (0,1) not in set(P)|{(1,4)}
    assert w[1]/2==Q(1,8)
    print('PASS: single independent action increases degree 3 to 5 at fixed sharp 1/8')

    P=((0,2),(1,4),(2,5),(3,5),(4,6))
    w=harmonic(P)
    assert w==(Q(0),Q(3,11),Q(6,11),Q(8,11),Q(9,11),Q(10,11),Q(1))
    assert (w[0]+w[6])/2<w[2]
    assert peel(P)==((6,),(5,),(3,4),(2,),(1,))
    assert peel(P,((2,(0,6),'T'),))==((6,),(2,3,4,5),(1,))
    assert (0,1) not in set(P)|{(0,6)}
    assert w[1]/2==Q(3,22)
    print('PASS: single tied edge decreases degree 5 to 3 at fixed sharp 3/22')

if __name__=='__main__':run()
