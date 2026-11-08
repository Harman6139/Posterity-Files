#!/usr/bin/env python3
"""Independent exact integer check of Milestone 59's max-τ fixed point.
Exhaustive 17,169 collision-free h=4 multi-action systems plus 24,821
one-slack-action extensions of all strictly harmonic h=5 base networks.
Run from this directory with network reference helpers, or use the self-
contained loops below. No numerical SDP is used.
"""
from itertools import product
from fractions import Fraction as F

def tau(a,b):
    return a if a==b else min(a,b)+1

def fixed_times(actions):
    h=len(actions);inf=h+3
    t=[inf]+[1]*h+[1]
    for _ in range((h+2)**2+1):
        z=[inf]+[max(tau(t[a],t[b]) for a,b in ac) for ac in actions]+[1]
        if z==t:return tuple(z[1:-1])
        assert all(z[i]>=t[i] for i in range(1,h+1))
        t=z
    raise AssertionError('no stabilization')

def closure_times(actions):
    h=len(actions);rem=set(range(h+2));times={}
    for step in range(1,h+2):
        if rem=={0}:break
        C=rem-{0}
        while True:
            bad={v for v in C if v<=h and any(
                a in rem and b in rem and (a not in C or b not in C)
                for a,b in actions[v-1])}
            if not bad:break
            C-=bad
        assert C
        for v in C:times[v]=step
        rem-=C
    assert rem=={0}
    return tuple(times[v] for v in range(1,h+1))

def candidates(h):
    return [[(a,b) for a in range(i) for b in range(i+1,h+2)]
            for i in range(1,h+1)]

def harmonic(policy):
    h=len(policy)
    rows=[]
    for i,(a,b) in enumerate(policy,1):
        row=[F(0)]*(h+1);row[i-1]=2
        for p in (a,b):
            if p==h+1:row[-1]+=1
            elif p:row[p-1]-=1
        rows.append(row)
    for j in range(h):
        p=next(i for i in range(j,h) if rows[i][j])
        rows[j],rows[p]=rows[p],rows[j]
        v=rows[j][j];rows[j]=[x/v for x in rows[j]]
        for i in range(h):
            if i!=j:
                v=rows[i][j]
                rows[i]=[a-v*b for a,b in zip(rows[i],rows[j])]
    return tuple(row[-1] for row in rows)

def check():
    h=4
    alloptions=[]
    for choices in candidates(h):
        alloptions.append([
            (tuple(choices[j] for j in range(len(choices)) if mask>>j&1),
             set(choices[j] for j in range(len(choices)) if mask>>j&1))
            for mask in range(1,1<<len(choices))])
    c=0
    def dfs(i,actions,used):
        nonlocal c
        if i==h:
            assert fixed_times(actions)==closure_times(actions)
            c+=1;return
        for aa,edges in alloptions[i]:
            if not used.intersection(edges):
                dfs(i+1,actions+(aa,),used|edges)
    dfs(0,(),set())
    assert c==17169
    print('PASS:',c,'collision-free h=4 action hypergraphs')
    h=5; choices=candidates(h);count=0
    for policy in product(*choices):
        w=harmonic(policy);v=(F(0),)+w+(F(1),)
        if not all(a<b for a,b in zip(v,v[1:])):continue
        used=set(policy)
        for i in range(1,h+1):
            for edge in choices[i-1]:
                if edge in used:continue
                a,b=edge
                if v[a]+v[b]<2*v[i]:continue
                actions=tuple((policy[j-1],edge) if j==i else (policy[j-1],)
                              for j in range(1,h+1))
                assert fixed_times(actions)==closure_times(actions)
                count+=1
    assert count==24821
    print('PASS:',count,'h=5 strict graphs with one nonimproving action')
if __name__=='__main__':check()
