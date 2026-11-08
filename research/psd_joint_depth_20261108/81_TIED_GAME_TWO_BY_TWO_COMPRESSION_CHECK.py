#!/usr/bin/env python3
"""Pure-Fraction audit of checkpoint 79's bounded-mode/edge compression and
checkpoint 80's sharpness examples. Run with Python 3. No external modules.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

def harm(P):
    n=len(P);rows=[]
    for i,(a,b) in enumerate(P):
        row=[F(0)]*(n+1);row[i]=2
        for p in (a,b):
            if p==n+1:row[-1]+=1
            elif p:row[p-1]-=1
        rows.append(row)
    for j in range(n):
        k=next(z for z in range(j,n) if rows[z][j])
        rows[k],rows[j]=rows[j],rows[k]
        c=rows[j][j];rows[j]=[v/c for v in rows[j]]
        for i in range(n):
            if i!=j:
                c=rows[i][j]
                rows[i]=[x-c*y for x,y in zip(rows[i],rows[j])]
    return (F(0),)+tuple(row[-1] for row in rows)+(F(1),)

def game_value(modes):
    n=len(modes)
    for selections in product(*(range(len(A)) for A in modes)):
        choices=[modes[i][a] for i,a in enumerate(selections)]
        for edge_choices in product(*(range(len(E)) for E in choices)):
            w=harm([choices[i][z] for i,z in enumerate(edge_choices)])
            if all(w[i]==min(max((w[a]+w[b])/2 for a,b in mode)
                  for mode in modes[i-1]) for i in range(1,n+1)):
                return w
    raise AssertionError('No game fixed point')

def peel(modes):
    n=len(modes);rem=set(range(n+2));layers=[]
    while rem!={0}:
        C=rem-{0}
        while True:
            blocked={i for i in C if i<=n and any(
                all(u in rem and v in rem for u,v in mode) and
                not any(u in C and v in C for u,v in mode)
                for mode in modes[i-1])}
            if not blocked:break
            C-=blocked
        assert C
        layers.append(tuple(sorted(C)));rem-=C
    return layers

def compress(modes,w):
    n=len(modes);layers=peel(modes);d=len(layers)
    t={0:d+2}
    for j,C in enumerate(layers,1):
        for v in C:t[v]=j
    selected={}
    for j in range(d-1,0,-1):
        H={0}|{v for v in range(1,n+2) if t[v]>j+1}
        L={v for v in range(1,n+1) if t[v]==j+1}
        R={0}|{v for v in range(1,n+2) if t[v]>=j}
        reached=set(H)
        while L-reached:
            hit=False
            for i in sorted(L-reached):
                options=[a for a,mode in enumerate(modes[i-1])
                         if all(u in R and v in R for u,v in mode)
                         and all(u in reached or v in reached for u,v in mode)]
                if options:
                    selected[i]=options[0];reached.add(i);hit=True
            assert hit,('dual witness failure',j,modes,layers)
    out=[]
    for i,ms in enumerate(modes,1):
        primal=min(range(len(ms)),
                   key=lambda a:max((w[u]+w[v])/2 for u,v in ms[a]))
        assert max((w[u]+w[v])/2 for u,v in ms[primal])==w[i]
        new=[]
        for a in sorted({selected[i],primal}):
            mode=ms[a]
            max_edge=max(mode,key=lambda e:(w[e[0]]+w[e[1]])/2)
            current={0}|{v for v in range(1,n+2) if t[v]>=t[i]}
            stage={v for v in range(1,n+2) if t[v]==t[i]}
            releasing=next(e for e in mode if
                           e[0] not in current or e[1] not in current
                           or (e[0] in stage and e[1] in stage))
            new.append(tuple(sorted({max_edge,releasing})))
        out.append(tuple(new))
    return tuple(out)

def examples():
    E=((((0,3),),),(((0,4),(1,3)),),(((2,4),),))
    w=game_value(E);layers=peel(E)
    assert w==(F(0),F(2,5),F(3,5),F(4,5),F(1))
    assert layers==[(4,),(2,3),(1,)]
    E0=E[:1]+((((0,4),),),)+E[2:]
    E1=E[:1]+((((1,3),),),)+E[2:]
    assert game_value(E0)!=w and peel(E1)!=layers
    M=((((0,3),),),(((1,4),),),(((0,5),),((2,4),)),(((1,5),),))
    W=game_value(M);L=peel(M)
    assert W==(F(0),F(1,4),F(7,16),F(1,2),F(5,8),F(1))
    assert L==[(5,),(4,),(2,3),(1,)]
    M0=M[:2]+( (((0,5),),), )+M[3:]
    M1=M[:2]+( (((2,4),),), )+M[3:]
    assert peel(M0)!=L and game_value(M1)!=W

def randomized():
    rng=Random(256);count=0
    for n in (3,4,5):
        pairs=[[(a,b) for a in range(i) for b in range(i+1,n+2)]
               for i in range(1,n+1)]
        for _ in range(2000):
            P=tuple(rng.choice(A) for A in pairs);w=harm(P)
            if not all(x<y for x,y in zip(w,w[1:])):continue
            used=set(P);modes=[]
            for i,p in enumerate(P):
                candidates=[e for e in pairs[i] if e not in used
                            and (w[e[0]]+w[e[1]])/2<=w[i+1]]
                rng.shuffle(candidates);mode=[p]
                for e in candidates[:rng.randrange(min(2,len(candidates))+1)]:
                    mode.append(e);used.add(e)
                modes.append([tuple(mode)])
            for i in range(n):
                candidates=[e for e in pairs[i] if e not in used
                            and (w[e[0]]+w[e[1]])/2>=w[i+1]]
                rng.shuffle(candidates)
                if candidates and rng.random()<.7:
                    take=rng.randrange(1,min(3,len(candidates))+1)
                    mode=tuple(candidates[:take])
                    modes[i].append(mode);used.update(mode)
            modes=tuple(tuple(M) for M in modes)
            assert game_value(modes)==w
            reduced=compress(modes,w)
            assert game_value(reduced)==w
            assert peel(reduced)==peel(modes)
            assert all(len(ms)<=2 and all(len(E)<=2 for E in ms)
                       for ms in reduced)
            count+=1
    assert count==1923,count
    print('PASS:',count,'exact-rational strict minmax game compression tests')

if __name__=='__main__':
    examples()
    randomized()
    print('PASS: two-mode and two-edge sharpness instances')
