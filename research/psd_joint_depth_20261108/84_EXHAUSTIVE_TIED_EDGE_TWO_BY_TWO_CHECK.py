#!/usr/bin/env python3
"""Exhaustive exact rational check of Milestone 79 for EVERY one-mode,
up-to-two-edge tied PSD system with three or four internal vertices.
Expected 104 + 6902 = 7006 edge-disjoint systems, of which 91 + 4665
have strictly ordered Shapley values. Use alongside checkpoint 81's
randomized multi-mode test (1923 strict systems).
All calculations use Fraction; no numerical SDP.
"""
from fractions import Fraction as F
from itertools import product,combinations

def harmonize(P):
    h=len(P);rows=[]
    for i,(a,b) in enumerate(P,1):
        row=[F(0)]*(h+1);row[i-1]=2
        for v in (a,b):
            if v==h+1:row[-1]+=1
            elif v:row[v-1]-=1
        rows.append(row)
    for j in range(h):
        k=next(i for i in range(j,h) if rows[i][j])
        rows[k],rows[j]=rows[j],rows[k]
        c=rows[j][j];rows[j]=[x/c for x in rows[j]]
        for i in range(h):
            if i!=j:
                c=rows[i][j]
                rows[i]=[x-c*y for x,y in zip(rows[i],rows[j])]
    return (F(0),)+tuple(row[-1] for row in rows)+(F(1),)

def game(modes):
    h=len(modes)
    for selected in product(*(range(len(M)) for M in modes)):
        choices=[modes[i][a] for i,a in enumerate(selected)]
        for selected_edges in product(*(range(len(E)) for E in choices)):
            w=harmonize([choices[i][a] for i,a in enumerate(selected_edges)])
            if all(w[i]==min(max((w[a]+w[b])/2 for a,b in mode)
                      for mode in modes[i-1]) for i in range(1,h+1)):
                return w
    raise AssertionError('No fixed point')

def peel(modes):
    h=len(modes);rem=set(range(h+2));stages=[]
    while rem!={0}:
        C=rem-{0}
        while True:
            bad={i for i in C if i<=h and any(
                all(a in rem and b in rem for a,b in E) and
                not any(a in C and b in C for a,b in E)
                for E in modes[i-1])}
            if not bad:break
            C-=bad
        assert C
        stages.append(tuple(sorted(C)));rem-=C
    return stages

def compress(modes,w):
    h=len(modes);stages=peel(modes);d=len(stages)
    times={0:d+3}
    for j,layer in enumerate(stages,1):
        for v in layer:times[v]=j
    dual={}
    for j in range(d-1,0,-1):
        H={0}|{v for v in range(1,h+2) if times[v]>j+1}
        L={v for v in range(1,h+1) if times[v]==j+1}
        R={0}|{v for v in range(1,h+2) if times[v]>=j}
        reached=set(H)
        while L-reached:
            progress=False
            for i in sorted(L-reached):
                opts=[a for a,E in enumerate(modes[i-1])
                      if all(u in R and v in R for u,v in E)
                      and all(u in reached or v in reached for u,v in E)]
                if opts:
                    dual[i]=opts[0];reached.add(i);progress=True
            assert progress
    reduced=[]
    for i,M in enumerate(modes,1):
        primal=min(range(len(M)), key=lambda j:
                   max((w[a]+w[b])/2 for a,b in M[j]))
        current={0}|{v for v in range(1,h+2) if times[v]>=times[i]}
        group={v for v in range(1,h+2) if times[v]==times[i]}
        kept=[]
        for j in sorted({dual[i],primal}):
            E=M[j]
            maximize=max(E,key=lambda e:(w[e[0]]+w[e[1]])/2)
            release=next(e for e in E if
                         e[0] not in current or e[1] not in current
                         or (e[0] in group and e[1] in group))
            kept.append(tuple(sorted({maximize,release})))
        reduced.append(tuple(kept))
    return tuple(reduced)

def check():
    for h,count_expected,strict_expected in ((3,104,91),(4,6902,4665)):
        choices=[[(a,b) for a in range(i) for b in range(i+1,h+2)]
                 for i in range(1,h+1)]
        mode_options=[list(combinations(P,1))+list(combinations(P,2))
                      for P in choices]
        total=0;strict=0
        for E in product(*mode_options):
            edges=[e for mode in E for e in mode]
            if len(edges)!=len(set(edges)):continue
            total+=1
            modes=tuple((mode,) for mode in E)
            w=game(modes)
            if not all(x<y for x,y in zip(w,w[1:])):continue
            strict+=1
            smaller=compress(modes,w)
            assert game(smaller)==w
            assert peel(smaller)==peel(modes)
            assert all(len(M)<=2 and all(len(e)<=2 for e in M)
                       for M in smaller)
        assert (total,strict)==(count_expected,strict_expected)
        print(f'PASS: h={h}, all={total}, strict={strict}')
    print('PASS: 7,006 tied-edge exact rational systems and 4,756 strict cases')

if __name__=='__main__':check()
