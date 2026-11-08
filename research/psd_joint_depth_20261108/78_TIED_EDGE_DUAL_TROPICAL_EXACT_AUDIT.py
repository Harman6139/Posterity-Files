#!/usr/bin/env python3
"""Exact integer audit: tied-edge exposing time = least max-mode/min-edge
tau fixed point. No floating-point or SDP calculation.
"""
from itertools import combinations,product

def candidates(h):
    return [[(a,b) for a in range(i) for b in range(i+1,h+2)]
            for i in range(1,h+1)]

def tau(a,b):
    return a if a==b else min(a,b)+1

def fixed(modes):
    h=len(modes)
    x=[h+3]+[1]*h+[1]
    for _ in range((h+1)**2):
        y=[h+3]+[min(tau(x[a],x[b]) for a,b in E) for E in modes]+[1]
        if y==x:
            return tuple(y)
        assert all(y[i]>=x[i] for i in range(1,h+1))
        x=y
    raise AssertionError('iteration did not terminate')

def peel(modes):
    h=len(modes); remain=set(range(h+2)); layers=[]
    while remain!={0}:
        C=remain-{0}
        while True:
            bad={i for i in C if i<=h and
                 all(a in remain and b in remain for a,b in modes[i-1]) and
                 not any(a in C and b in C for a,b in modes[i-1])}
            if not bad: break
            C-=bad
        assert C
        layers.append(tuple(sorted(C)))
        remain-=C
    return tuple(layers)

def check():
    for h,expected in [(3,104),(4,6902)]:
        opts=[[tuple(E) for k in (1,2) for E in combinations(A,k)]
              for A in candidates(h)]
        count=0
        for modes in product(*opts):
            edges=[edge for E in modes for edge in E]
            if len(edges)!=len(set(edges)): continue
            layers=peel(modes)
            stages={0:h+3}
            for j,vs in enumerate(layers,1):
                for v in vs: stages[v]=j
            assert fixed(modes)[1:-1]==tuple(stages[i] for i in range(1,h+1))
            count+=1
        assert count==expected,(h,count,expected)
        print('PASS h',h,'tied-edge systems',count)
    print('PASS 7,006 exact max-min tropical / PSD peeling checks')

if __name__=='__main__':check()
