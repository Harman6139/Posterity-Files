#!/usr/bin/env python3
"""Exact Fraction audit for the dimension-unrestricted exponent/depth spectrum.
Tests the dyadic-spine-plus-affine-grid base, layered high-depth helper and
source-gluing of checkpoint 85 on 960 rational (alpha,d) pairs.
All tests are combinatorial exact; the general full-PSD proof is in 85.
"""
from fractions import Fraction as F

def base(alpha):
    e=2
    while F(1,2**e)>alpha:e+=1
    c=F(1,2**(e-1))
    z=(2*alpha-c)/(1-c)
    assert 0<=z<1
    vals={F(0):'O',F(1):'BT'}
    for j in range(1,e):vals[F(1,2**j)]=f'bs{j}'
    a,b=z.numerator,z.denominator
    for k in range(1,b):
        v=c+F(k,b)*(1-c)
        if v not in vals:vals[v]=f'bg{k}'
    parents={}
    for j in range(1,e):
        v=F(1,2**j)
        parents[vals[v]]=('O',vals[2*v])
    grid=[c+F(k,b)*(1-c) for k in range(b+1)]
    for k in range(1,b):
        v=grid[k];node=vals[v]
        if node not in parents:parents[node]=(vals[grid[k-1]],vals[grid[k+1]])
    w={v:x for x,v in vals.items()}
    assert all(w[a]+w[b]==2*w[i] for i,(a,b) in parents.items())
    assert len({tuple(sorted(p)) for p in parents.values()})==len(parents)
    assert len(parents)==len(w)-2
    assert min(w[i] for i in parents)>=alpha
    assert 2*alpha in vals
    assert tuple(sorted(('O',vals[2*alpha]))) not in {
        tuple(sorted(p)) for p in parents.values()}
    return e,w,parents,{'BT'}

def helper(d,M):
    s=(1,)+(1,)*(d-3)+(M,1)
    q={j:2**s[j-1]-1 for j in range(2,d+1)}
    p={1:1}
    for j in range(2,d+1):p[j]=p[j-1]*q[j]
    D=sum(p.values())
    delta={j+1:F(p[j],D) for j in range(1,d+1)}
    levels={1:F(1),d+1:F(0)}
    for j in range(d,1,-1):levels[j]=levels[j+1]+delta[j+1]
    w={'O':F(0),'HT':F(1)};parents={}
    for j in range(2,d+1):
        for h in range(1,s[j-1]+1):
            v=f'h{j}_{h}'
            w[v]=levels[j-1]-F(1,2**h)*(levels[j-1]-levels[j+1])
            low='O' if j==d else f'h{j+1}_{s[j]}'
            if h>1:low=f'h{j}_{h-1}'
            high='HT' if j==2 else f'h{j-1}_{s[j-2]}'
            parents[v]=(low,high)
    assert all(w[a]+w[b]==2*w[i] for i,(a,b) in parents.items())
    beta=min(w[i] for i in parents)
    assert beta==F(2**M-1,2*(2**M-1)+d-2)
    return beta,w,parents,{'HT'}

def peel(w,parents):
    remaining=set(w);layers=[]
    while remaining!={'O'}:
        C=remaining-{'O'}
        while True:
            bad={i for i in C if i in parents and
                 all(v in remaining for v in parents[i])
                 and not all(v in C for v in parents[i])}
            if not bad:break
            C-=bad
        assert C
        layers.append(tuple(sorted(C)));remaining-=C
    return layers

def construct(alpha,d):
    e,w,parents,T=base(alpha)
    assert e<=d and len(peel(w,parents))==e
    if e==d:return
    M=1
    while F(2**M-1,2*(2**M-1)+d-2)<=alpha:M+=1
    beta,ww,pp,TT=helper(d,M)
    assert beta>alpha and len(peel(ww,pp))==d
    w.update({v:x for v,x in ww.items() if v!='O'})
    parents.update(pp)
    assert len(parents)==len(w)-1-len(T|TT)
    assert len(peel(w,parents))==d

def main():
    count=0
    for d in range(2,8):
        for b in range(2,29):
            for a in range(1,b//2+1):
                x=F(a,b)
                if F(1,2**d)<=x<F(1,2):
                    construct(x,d)
                    count+=1
    assert count==960
    print('PASS:',count,'rational exponent/depth pairs (d=2..7, b<=28)')

if __name__=='__main__':main()
