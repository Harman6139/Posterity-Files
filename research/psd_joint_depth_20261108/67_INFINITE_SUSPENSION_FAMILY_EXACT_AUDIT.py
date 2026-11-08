#!/usr/bin/env python3
"""Exact Fraction/integer verification of the infinite two-action separation
family in checkpoint 66. Uses no numerical SDP or external packages.
"""
from fractions import Fraction as F

def tau(a,b):return a if a==b else min(a,b)+1

def harmonic(actions):
    h=len(actions);w=[F(0)]*(h+2);w[-1]=1
    # Bellman value iteration from the all-ones subsolution (monotone finite
    # stochastic-shortest-path iteration); for exact rational output solve the
    # explicitly optimal policy, taking action index 0 at each vertex.
    rows=[]
    for i,aa in enumerate(actions,1):
        a,b=aa[0]
        row=[F(0)]*(h+1);row[i-1]=2
        for p in a,b:
            if p==h+1:row[-1]+=1
            elif p:row[p-1]-=1
        rows.append(row)
    for j in range(h):
        p=next(i for i in range(j,h) if rows[i][j])
        rows[j],rows[p]=rows[p],rows[j]
        c=rows[j][j];rows[j]=[x/c for x in rows[j]]
        for i in range(h):
            if i!=j:
                c=rows[i][j];rows[i]=[a-c*b for a,b in zip(rows[i],rows[j])]
    for i in range(1,h+1):w[i]=rows[i-1][-1]
    assert all(w[a]+w[b]>=2*w[i] for i,aa in enumerate(actions,1) for a,b in aa)
    return tuple(w)

def peeling_times(actions):
    h=len(actions)
    t=[h+3]+[1]*h+[1]
    for _ in range((h+2)**2):
        u=[h+3]+[max(tau(t[a],t[b]) for a,b in aa) for aa in actions]+[1]
        if u==t:return tuple(u)
        assert all(u[i]>=t[i] for i in range(1,h+1))
        t=u
    raise AssertionError('tropical fixed point not reached')

def family(ell):
    actions=[
        ((0,3),), ((1,4),),
        ((0,5),(2,4)), ((1,5),)
    ]
    for j in range(5,5+ell):
        actions.append(((0,j+1),))
    h=len(actions);nu=h+1
    w=harmonic(actions)
    assert all(a<b for a,b in zip(w,w[1:]))
    alpha=w[2]/2
    assert alpha==F(7,2**nu)
    assert alpha<w[1]
    assert (0,2) not in {e for A in actions for e in A}
    assert w[2]+w[4]>2*w[3]
    t=peeling_times(actions)
    times=t[1:-1]+(1,)
    d=max(times)
    profile=tuple(sum(stage==j for stage in times) for j in range(1,d+1))
    assert d==nu-1
    assert profile==(1,)*(ell+2)+(2,1)
    return nu,d,alpha,profile

if __name__=='__main__':
    for ell in range(13):
        print('PASS',family(ell))
    print('PASS: 13 exact suspension levels, nullity 5..17')
