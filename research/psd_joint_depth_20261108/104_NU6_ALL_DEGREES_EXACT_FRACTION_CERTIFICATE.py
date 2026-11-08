#!/usr/bin/env python3
"""Exact ν=6 arbitrary-dense PSD exponent/depth catalogue certificate.
Necessary: canonical harmonic grades + primal/dual peeling (89,91,99).
Sufficient: exhaustive zero/one/two independent/tied-edge augmentations
plus the explicit three-extra-edge 13/64,d5 witness (102).
No floating-point arithmetic, randomized search, or numerical SDP.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import defaultdict
from hashlib import sha256

def choices(h):
    return [[(a,b) for a in range(i) for b in range(i+1,h+2)]
            for i in range(1,h+1)]

def harmonic(P):
    h=len(P);M=[]
    for i,(a,b) in enumerate(P,1):
        row=[F(0)]*(h+1);row[i-1]=2
        for p in (a,b):
            if p==h+1:row[-1]+=1
            elif p:row[p-1]-=1
        M.append(row)
    for j in range(h):
        p=next(i for i in range(j,h) if M[i][j])
        M[p],M[j]=M[j],M[p]
        c=M[j][j];M[j]=[x/c for x in M[j]]
        for i in range(h):
            if i!=j:
                c=M[i][j]
                if c:M[i]=[x-c*y for x,y in zip(M[i],M[j])]
    return tuple(row[-1] for row in M)

def lower(W):
    k=len(W)-1;j=k;steps=0
    while j:
        steps+=1
        if j==k:j=k-1
        else:j=sum(1 for i in range(1,j) if 2*W[i]<W[j+1])
    return steps

def upper(W):
    k=len(W)-1;j=k;steps=0
    while j:
        steps+=1
        if j==k:j=k-1
        else:
            p=next(i for i in range(1,j+1)
                   if 2*W[i]>W[j]+W[i-1])
            j=p-1
    return steps

def peel(modes):
    h=len(modes);R=set(range(h+2));layers=[]
    while R!={0}:
        C=R-{0}
        while True:
            forbidden={i for i in C if 1<=i<=h and any(
                all(a in R and b in R for a,b in mode) and
                not any(a in C and b in C for a,b in mode)
                for mode in modes[i-1])}
            if not forbidden:break
            C-=forbidden
        assert C
        layers.append(tuple(sorted(C)))
        R-=C
    return tuple(layers)

def audit():
    nu=6;nec=defaultdict(set);real=defaultdict(set)
    witness={};counts={}
    for h in range(1,nu):
        valid=0
        opts=choices(h)
        for P in product(*opts):
            w=harmonic(P);W=(F(0),)+w+(F(1),)
            if any(W[i]>=W[i+1] for i in range(h+1)):continue
            valid+=1
            leads={W[v]/2:v for v in range(1,h+2)
                   if W[v]/2<=w[0]}
            lo,hi=lower(W),upper(W)
            assert lo<=hi
            for d in range(lo,hi+1):
                for a in leads:
                    if a>=F(1,2**d):nec[d].add(a)
            used=set(P)
            alternatives=[]
            for i in range(1,h+1):
                for edge in opts[i-1]:
                    if edge in used:continue
                    avg=(W[edge[0]]+W[edge[1]])/2
                    if avg>=W[i]:alternatives.append((i,edge,'I'))
                    if avg<=W[i]:alternatives.append((i,edge,'T'))
            base=[[(p,)] for p in P]
            def visit(extras):
                edges=used|{e for _,e,_ in extras}
                modes=[list(M) for M in base]
                for i,edge,kind in extras:
                    if kind=='I':modes[i-1].append((edge,))
                    else:modes[i-1][0]=tuple(sorted(modes[i-1][0]+(edge,)))
                layers=peel(tuple(tuple(M) for M in modes))
                d=len(layers)
                for alpha,v in leads.items():
                    if alpha<w[0] and (0,v) in edges:continue
                    if alpha<F(1,2**d):continue
                    real[d].add(alpha)
                    witness.setdefault((d,alpha),(h,P,extras,layers))
            visit(())
            for x in alternatives:visit((x,))
            for x,y in combinations(alternatives,2):
                if x[1]!=y[1]:visit((x,y))
        counts[h]=valid
    assert counts=={1:1,2:3,3:18,4:165,5:2099},counts
    missing={d:sorted(nec[d]-real[d]) for d in range(2,7)}
    assert missing=={2:[],3:[],4:[],5:[F(13,64)],6:[]},missing

    P=((0,3),(0,5),(0,6),(1,6),(4,6))
    extras=((2,(1,4),'I'),(3,(2,4),'I'),(4,(3,5),'I'))
    w=harmonic(P);W=(F(0),)+w+(F(1),)
    assert w==(F(1,4),F(13,32),F(1,2),F(5,8),F(13,16))
    assert all(W[a]+W[b]>2*W[i] for i,(a,b),_ in extras)
    assert (0,2) not in set(P)|{e for _,e,_ in extras}
    modes=[[(p,)] for p in P]
    for i,e,_ in extras:modes[i-1].append((e,))
    layers=peel(modes)
    assert layers==((6,),(5,),(4,),(2,3),(1,))
    real[5].add(F(13,64))
    witness[5,F(13,64)]=(5,P,extras,layers)

    expect={2:81,3:206,4:174,5:107,6:46}
    assert {d:len(nec[d]) for d in range(2,7)}==expect
    assert all(nec[d]==real[d] for d in range(2,7))
    digest=sha256('\n'.join(f'{d}:{a}' for d in range(2,7)
                            for a in sorted(nec[d])).encode()).hexdigest()
    assert digest=='cfbdc113e81b88a59d5bf31eff111802eeea23ad82d467d2ca7176b194468151'
    print('PASS strict harmonic graph counts:',counts)
    for d in range(2,7):
        print('PASS degree',d,'exact exponents',len(nec[d]))
    print('PASS 13/64 depth-five exceptional three-extra-edge certificate')
    print('SHA256 catalogue',digest)

if __name__=='__main__':audit()
