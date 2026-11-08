#!/usr/bin/env python3
"""Exact SymPy + Fraction audit of Milestone 68.
Checks dual stress orthogonality/compression in the 7x7 example,
and the strictly ordered Bellman values / exact peeling of suspensions.
No floating point or numerical SDP solver is used.
"""
from fractions import Fraction as Q
from sympy import zeros, Rational, trace

def E(i,j,n):
    a=zeros(n);a[i,j]=1
    return a

def F(i,j,n):return E(i,j,n)+E(j,i,n)

def first_example():
    n=7; lam=Rational(1,100)
    actions=[[(0,2)],[(1,3)],[(0,5),(2,4)],[(1,6),(3,5)],[(4,6)]]
    H=[E(i,i,n)-E(0,0,n)+lam*F(a,b,n)
       for i,AA in enumerate(actions,1) for a,b in AA]
    H.append(lam*F(0,1,n))
    Z=[
        E(6,6,n),
        E(5,5,n)-50*F(4,6,n),
        E(4,4,n)-50*(F(1,6,n)+F(3,5,n)),
        E(3,3,n)-50*(F(0,5,n)+F(2,4,n)),
        E(2,2,n)-50*F(1,3,n),
        E(1,1,n)-50*F(0,2,n)
    ]
    assert len(H)==8
    for stage,z in enumerate(Z):
        assert all(trace(z*h)==0 for h in H)
        current=n-stage
        assert z[:current,:current]==E(current-1,current-1,current)
    return actions

def harmonic(actions):
    h=len(actions)
    rows=[]
    for i,AA in enumerate(actions,1):
        a,b=AA[0]
        row=[Q(0)]*(h+1);row[i-1]=2
        for p in (a,b):
            if p==h+1:row[-1]+=1
            elif p:row[p-1]-=1
        rows.append(row)
    for j in range(h):
        p=next(i for i in range(j,h) if rows[i][j])
        rows[j],rows[p]=rows[p],rows[j]
        c=rows[j][j];rows[j]=[x/c for x in rows[j]]
        for i in range(h):
            if i!=j:
                c=rows[i][j]
                rows[i]=[x-c*y for x,y in zip(rows[i],rows[j])]
    w=(Q(0),)+tuple(row[-1] for row in rows)+(Q(1),)
    assert all(a<b for a,b in zip(w,w[1:]))
    for i,AA in enumerate(actions,1):
        assert all(2*w[i]<=w[a]+w[b] for a,b in AA)
    return w

def peeling(actions):
    n=len(actions)+2
    remain=set(range(n)); layers=[]
    while remain!={0}:
        C=remain-{0}
        while True:
            blocked={i for i in C if i<n-1 and any(
                a in remain and b in remain and (a not in C or b not in C)
                for a,b in actions[i-1])}
            if not blocked:break
            C-=blocked
        assert C
        layers.append(tuple(sorted(C)))
        remain-=C
    return tuple(layers)

def test():
    actions=first_example()
    for extra in range(9):
        if extra:
            old_terminal=len(actions)+1
            actions=actions+[[(0,old_terminal+1)]]
        w=harmonic(actions)
        nu=len(actions)+1
        assert w[1]/2==Q(3,46*2**extra)
        assert peeling(actions)==tuple((i,) for i in range(nu,0,-1))
        print('PASS: nullity',nu,'alpha',w[1]/2,'depth',nu)
    print('PASS: exact 7x7 dual stress audit and all nine suspensions')

if __name__=='__main__':test()
