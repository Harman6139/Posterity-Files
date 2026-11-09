#!/usr/bin/env python3
"""Exact Fraction audit for Milestone 110: every integer depth between
the canonical original-kernel primal/dual grade bounds admits a complete
two-mode/one-tied-edge abstract exposing schedule. Physical edge collisions
are removed by at most two unique positive-parent coordinate clones per
internal vertex; the clone theorem supplies full PSD realizations.
No float, randomization, SDP or external modules.
"""
from fractions import Fraction as F
from itertools import product
from collections import Counter

def choices(h):
    return [[(a,b) for a in range(i) for b in range(i+1,h+2)]
            for i in range(1,h+1)]

def harmonic(P):
    h=len(P);rows=[]
    for i,(a,b) in enumerate(P,1):
        row=[F(0)]*(h+1);row[i-1]=2
        for p in a,b:
            if p==h+1:row[-1]+=1
            elif p:row[p-1]-=1
        rows.append(row)
    for j in range(h):
        p=next(i for i in range(j,h) if rows[i][j])
        rows[p],rows[j]=rows[j],rows[p]
        c=rows[j][j];rows[j]=[x/c for x in rows[j]]
        for i in range(h):
            if i!=j:
                c=rows[i][j]
                rows[i]=[x-c*y for x,y in zip(rows[i],rows[j])]
    return (F(0),)+tuple(row[-1] for row in rows)+(F(1),)

def edges(j,w):
    ell=sum(1 for i in range(1,j) if 2*w[i]<w[j+1])
    p=next(i for i in range(1,j+1) if 2*w[i]>w[j]+w[i-1])
    assert 0<=ell<=p-1<j
    return range(ell,p)

def schedules(w):
    k=len(w)-1
    def rec(j,states):
        if j==0:
            yield states
        else:
            for q in edges(j,w):
                yield from rec(q,states+(q,))
    yield from rec(k-1,(k,k-1))

def compressed_exposing(modes):
    h=len(modes);remaining=set(range(h+2));out=[]
    while remaining!={0}:
        C=remaining-{0}
        while True:
            forbidden={i for i in C if i<=h and any(
                all(a in remaining and b in remaining for a,b in mode)
                and not any(a in C and b in C for a,b in mode)
                for mode in modes[i-1])}
            if not forbidden:break
            C-=forbidden
        assert C
        out.append(tuple(sorted(C)));remaining-=C
    return tuple(out)

def build_schedule(P,w,js):
    k=len(w)-1;h=k-1;d=len(js)-1
    assert js[0]==k and js[1]==k-1 and js[-1]==0
    exposed_at={i:t for t in range(1,d+1)
                for i in range(js[t]+1,js[t-1]+1)}
    assert set(exposed_at)==set(range(1,k+1))
    modes=[];total_clones=0
    for i in range(1,k):
        t=exposed_at[i]
        assert t>=2
        release=(0,js[t-1]+1)
        blocker=(i-1,js[t-2])
        assert release[1]>i and blocker[1]>i
        assert (w[release[0]]+w[release[1]])/2<=w[i]
        assert (w[blocker[0]]+w[blocker[1]])/2>=w[i]
        tied=tuple(dict.fromkeys((P[i-1],release)))
        mi=[tied]
        if blocker!=P[i-1]:mi.append((blocker,))
        modes.append(tuple(mi))
        total_clones+=int(release!=P[i-1])+int(blocker!=P[i-1])
    assert total_clones<=2*h
    return tuple(modes),total_clones

def run():
    expected={1:(1,1),2:(3,3),3:(18,24),4:(165,310),
              5:(2099,5833)}
    for h in range(1,6):
        valid=0;checked=0;max_clones=0;depth_ranges=Counter()
        for P in product(*choices(h)):
            w=harmonic(P)
            if any(x>=y for x,y in zip(w,w[1:])):continue
            valid+=1
            schedules_here=list(schedules(w))
            depths={len(js)-1 for js in schedules_here}
            assert depths==set(range(min(depths),max(depths)+1))
            for js in schedules_here:
                modes,c=build_schedule(P,w,js)
                expected_layers=tuple(tuple(range(js[t]+1,js[t-1]+1))
                                      for t in range(1,len(js)))
                assert compressed_exposing(modes)==expected_layers,(P,w,js)
                checked+=1;max_clones=max(max_clones,c)
            depth_ranges[min(depths),max(depths)]+=1
        assert valid==expected[h][0]
        assert checked==expected[h][1]
        print(f'PASS h={h} strict={valid} schedules={checked} '
              f'max_extra_clones={max_clones} depth_ranges={dict(depth_ranges)}')
    print('PASS all 2,099 h=5 harmonic graphs and all 5,833 admissible depth schedules')

if __name__=='__main__':run()
