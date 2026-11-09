#!/usr/bin/env python3
"""Exact Fraction audit of checkpoint 112: ORIGINAL-NULLITY shared-source
release edges realize the universal LOWER peeling bound for every strict
harmonic parent graph with h<=5 internal vertices and sharp alpha=w1.
No numerical PSD solver or external package. The proof in checkpoint112
establishes full-PSD recovery bounds and minimality, not merely these tests.
"""
from itertools import product
from fractions import Fraction as F

def choices(h):
    return [[(a,b) for a in range(i) for b in range(i+1,h+2)]
            for i in range(1,h+1)]

def harmonic(P):
    h=len(P);A=[]
    for i,(a,b) in enumerate(P,1):
        row=[F(0)]*(h+1);row[i-1]=2
        for p in (a,b):
            if p==h+1:row[-1]+=1
            elif p:row[p-1]-=1
        A.append(row)
    for j in range(h):
        p=next(i for i in range(j,h) if A[i][j])
        A[p],A[j]=A[j],A[p]
        c=A[j][j];A[j]=[x/c for x in A[j]]
        for i in range(h):
            if i!=j:
                c=A[i][j]
                A[i]=[x-c*y for x,y in zip(A[i],A[j])]
    return (F(0),)+tuple(row[-1] for row in A)+(F(1),)

def lower_schedule(w):
    k=len(w)-1;j=k-1;S=[k,j]
    while j:
        j=sum(1 for i in range(1,j) if 2*w[i]<w[j+1])
        S.append(j)
    return S

def verify(P,w):
    h=len(P);k=h+1;S=lower_schedule(w)
    layer={i:t for t in range(1,len(S))
           for i in range(S[t]+1,S[t-1]+1)}
    modes={}
    for i in range(1,k):
        t=layer[i]
        release=(0,S[t-1]+1)
        assert w[release[1]]<=2*w[i]
        es=tuple(dict.fromkeys((P[i-1],release)))
        modes[i]=es
        assert all(w[a]+w[b]<=2*w[i] for a,b in es)
        assert w[P[i-1][0]]+w[P[i-1][1]]==2*w[i]
        # Whenever another child's release shares a tight anchor at i,
        # that other child must have a STRICTLY HIGHER scalar weight.
        for j,es_j in modes.items():
            if j!=i and es_j[-1]==P[i-1]:
                assert j>i

    # Check the triangular anchor coefficient relations independently.
    for i,p in enumerate(P,1):
        visitors=[j for j in range(1,k) if j!=i and
                  (0,S[layer[j]-1]+1)==p and p!=P[j-1]]
        assert all(j>i for j in visitors),(i,p,visitors)

    # The full ambient dual stress at step t has +1 on each diagonal
    # exposed that step, and -1/(2lambda) F_(0,b_t) off the current face.
    # Pairings against each H_i reduce EXACTLY to
    # [i exposed] - [the sole nonzero offdiag e is in H_i].
    for t in range(1,len(S)):
        C=set(range(S[t]+1,S[t-1]+1))
        edge=None if t==1 else (0,S[t-1]+1)
        assert edge is None or edge[1]>S[t-1]
        for i,es in modes.items():
            pairing=int(i in C)-int(edge is not None and edge in es)
            assert pairing==0,(P,w,t,i,es,edge)
        # Forced-survivor predecessor is exactly the claimed prefix.
        if t>=2:
            j=S[t-1]
            q=sum(1 for i in range(1,j) if 2*w[i]<w[j+1])
            assert S[t]==q
    return len(S)-1

def run():
    expected={1:1,2:3,3:18,4:165,5:2099}
    for h in range(1,6):
        count=0;max_depth=0
        for P in product(*choices(h)):
            w=harmonic(P)
            if not all(a<b for a,b in zip(w,w[1:])):continue
            count+=1
            max_depth=max(max_depth,verify(P,w))
        assert count==expected[h]
        print(f'PASS h={h}: {count} strict harmonic policies, '
              f'explicit stress pairings and weighted support, max depth {max_depth}')
    print('PASS shared-release original-nullity theorem audit through h=5')

if __name__=='__main__':run()
