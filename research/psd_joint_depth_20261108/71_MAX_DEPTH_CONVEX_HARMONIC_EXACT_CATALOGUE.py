#!/usr/bin/env python3
"""Exact standard-library convex-harmonic maximum-depth PSD catalogue.
Checks Milestone 70, with explicit rational parent policies and slack completion.
No numerical SDP, continuous optimization, or floating-point arithmetic.
"""
from itertools import product
from fractions import Fraction as F
from collections import defaultdict

def linear_solve(A,b):
    h=len(b);rows=[list(map(F,A[i]))+[F(b[i])] for i in range(h)]
    for j in range(h):
        k=next(i for i in range(j,h) if rows[i][j])
        rows[k],rows[j]=rows[j],rows[k]
        c=rows[j][j];rows[j]=[x/c for x in rows[j]]
        for i in range(h):
            if i!=j:
                c=rows[i][j]
                rows[i]=[x-c*y for x,y in zip(rows[i],rows[j])]
    return tuple(row[-1] for row in rows)

def harmonic_graphs(h):
    if h==0:yield (),();return
    opts=[[(a,b) for a in range(i) for b in range(i+1,h+2)]
          for i in range(1,h+1)]
    for P in product(*opts):
        A=[[F(0) for _ in range(h)] for _ in range(h)]
        rhs=[F(0)]*h
        for i,(a,b) in enumerate(P,1):
            A[i-1][i-1]=2
            for parent in (a,b):
                if parent==h+1:rhs[i-1]+=1
                elif parent:A[i-1][parent-1]-=1
        w=linear_solve(A,rhs)
        if all(x<y for x,y in zip((F(0),)+w,w+(F(1),))):
            yield w,P

def peel(actions):
    h=len(actions)
    remain=set(range(h+2));layers=[]
    while remain!={0}:
        C=remain-{0}
        while True:
            bad={i for i in C if 1<=i<=h and any(
                a in remain and b in remain and (a not in C or b not in C)
                for a,b in actions[i-1])}
            if not bad:break
            C-=bad
        assert C
        layers.append(tuple(sorted(C)));remain-=C
    return tuple(layers)

def check():
    expected={1:(1,2,0),2:(2,4,0),3:(7,9,0),
              4:(34,20,0),5:(208,46,3)}
    for h in range(1,6):
        count=0;values=defaultdict(list)
        for w,P in harmonic_graphs(h):
            W=(F(0),)+w+(F(1),)
            gaps=[W[i+1]-W[i] for i in range(h+1)]
            if any(a>b for a,b in zip(gaps,gaps[1:])):continue
            count+=1
            nearest=tuple((i-1,i+1) for i in range(1,h+1))
            actions=tuple(tuple(set((P[i],nearest[i])))
                          for i in range(h))
            edges=[e for A in actions for e in A]
            assert len(edges)==len(set(edges))
            assert all(2*W[i]<=W[a]+W[b]
                       for i,A in enumerate(actions,1) for a,b in A)
            assert peel(actions)==tuple((i,) for i in range(h+1,0,-1))
            used=set(edges)
            # w1 itself can always be attained by the diagonal
            values[w[0]].append((w,P))
            for idx in range(1,h+2):
                alpha=W[idx]/2
                if alpha>w[0]:continue
                if alpha<w[0]:assert (0,idx) not in used
                values[alpha].append((w,P))
        exotic=sorted(a for a in values if a.numerator!=1)
        assert (count,len(values),len(exotic))==expected[h],(h,count,len(values),exotic)
        print('nullity',h+1,'convex graphs',count,'attainable',len(values),
              'nonreciprocal',list(map(str,exotic)))
    print('PASS: exact convexity/greedy/Bellman checks through nullity 6')

if __name__=='__main__':check()
