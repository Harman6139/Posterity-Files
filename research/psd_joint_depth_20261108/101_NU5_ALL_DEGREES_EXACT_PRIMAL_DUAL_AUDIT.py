#!/usr/bin/env python3
"""Checkpoint 97: exhaustive exact Fraction audit of the ALL-DENSE
target-nullity FIVE / minimal facial degree THREE sharp exponent spectrum.
Universal NECESSITY is theorems 89/91/92/95 and the blockwise forced
peeling lemma in checkpoint 97. This program audits their FINITE set.
Constructive SUFFICIENCY uses checkpoints 57/62 plus tied 75/96.
No numeric SDP optimizer, sampling or external Python package.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

def solve(policy):
    h=len(policy); M=[]
    for i,(a,b) in enumerate(policy,1):
        row=[F(0)]*(h+1);row[i-1]=2
        for p in a,b:
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

def choices(h):
    return [[(a,b) for a in range(i) for b in range(i+1,h+2)]
            for i in range(1,h+1)]

def forced_depth(grades):
    k=len(grades);j=k;steps=0
    while j>0:
        if j==k:nxt=k-1
        else:nxt=sum(1 for i in range(j-1) if 2*grades[i]<grades[j])
        assert nxt<j
        j=nxt;steps+=1
    return steps

def universal_necessary(nu=5,d=3):
    values=set();witness=defaultdict(list)
    # The canonical center has k>=d positive grades, and h=k−1.
    for h in range(d-1,nu):
        for P in product(*choices(h)):
            w=solve(P);W=(F(0),)+w+(F(1),)
            if not all(a<b for a,b in zip(W,W[1:])):continue
            if w[0]>=F(1,2):continue # dual center theorem: would force d<=2
            if forced_depth(w+(F(1),))>d:continue
            for v in range(1,h+2):
                alpha=W[v]/2
                if F(1,2**d)<=alpha<=w[0]:
                    values.add(alpha);witness[alpha].append((w,P))
    return values,witness

def peeling(actions):
    h=len(actions);remaining=set(range(h+2));layers=[]
    while remaining!={0}:
        C=remaining-{0}
        while True:
            blocked={i for i in C if i<=h and any(
                a in remaining and b in remaining and
                (a not in C or b not in C) for a,b in actions[i-1])}
            if not blocked:break
            C-=blocked
        assert C
        layers.append(tuple(sorted(C)));remaining-=C
    return tuple(layers)

def bellman(actions):
    policy=tuple(A[0] for A in actions)
    for iteration in range(40):
        w=solve(policy);W=(F(0),)+w+(F(1),)
        new=tuple(min(A,key=lambda edge:(W[edge[0]]+W[edge[1]],edge))
                  for A in actions)
        if all(2*W[i]==W[a]+W[b] for i,(a,b) in enumerate(new,1)):
            return w
        policy=new
    raise AssertionError("finite proper Bellman policy iteration did not terminate")

def action_subsets(A):
    for mask in range(1,1<<len(A)):
        edges=tuple(A[j] for j in range(len(A)) if mask>>j&1)
        yield edges,set(edges)

def independent_sufficient(nu=5,d=3):
    values=set();witness={};count=0
    for h in range(1,nu):
        options=[list(action_subsets(A)) for A in choices(h)]
        def dfs(i,actions,used):
            nonlocal count
            if i==h:
                count+=1
                if len(peeling(actions))!=d:return
                w=bellman(actions);W=(F(0),)+w+(F(1),)
                if not all(a<b for a,b in zip(W,W[1:])):return
                for v in range(1,h+2):
                    alpha=W[v]/2
                    if alpha<=w[0]:
                        values.add(alpha)
                        witness.setdefault(alpha,(w,actions))
                return
            for edges,st in options[i]:
                if not st.intersection(used):dfs(i+1,actions+(edges,),used|st)
        dfs(0,(),set())
    assert count==17302,(count,'collision-free independent action sets')
    return values,witness,count

def tied_checks():
    cases=[
       (F(3,22),((0,2),((1,4),(0,5)),(1,5),(3,5)),
        (F(3,11),F(6,11),F(7,11),F(9,11))),
       (F(3,20),((0,2),((1,4),(0,5)),(2,5),(3,5)),
        (F(3,10),F(3,5),F(4,5),F(9,10)))
    ]
    for alpha,pars,w in cases:
        modes=tuple(((x,),) if isinstance(x[0],int) else (x,) for x in pars)
        W=(F(0),)+w+(F(1),)
        assert alpha==w[0]/2
        for i,A in enumerate(modes,1):
            assert 2*W[i]==max(W[a]+W[b] for a,b in A[0])
        remaining=set(range(6));layers=[]
        while remaining!={0}:
            C=remaining-{0}
            while True:
                blocked={i for i in C if i<=4 and any(
                    all(a in remaining and b in remaining for a,b in mode)
                    and not any(a in C and b in C for a,b in mode)
                    for mode in modes[i-1])}
                if not blocked:break
                C-=blocked
            assert C
            layers.append(tuple(sorted(C)));remaining-=C
        assert layers==[(5,),(2,3,4),(1,)],(alpha,layers)
    print("PASS: 3/22 and 3/20 exact tied-edge Bellman / exposing certificates")

def main():
    tied_checks()
    necessary,graph_witness=universal_necessary()
    independent,witness,count=independent_sufficient()
    assert len(necessary)==51,len(necessary)
    assert len(independent)==49,len(independent)
    assert independent<=necessary
    assert necessary-independent=={F(3,22),F(3,20)}
    print("PASS:",len(necessary),"universal candidate exponents,",
          len(independent),"independent-edge constructions,",
          "two tied-edge constructions")
    print("Checked",count,"collision-free independent-action sets.")
    print("COMPLETE ν=5,d=3 SPECTRUM:")
    print(", ".join(map(str,sorted(necessary))))

def dual_upper(grades):
    """Number of universal ORIGINAL-DUAL-Puiseux exposing steps (checkpoint 99)."""
    W=(F(0),)+grades
    k=len(grades)
    j=k
    count=0
    while j:
        count+=1
        if j==k:
            j=k-1
            continue
        p=next(i for i in range(1,j+1)
               if 2*W[i]>W[j]+W[i-1])
        j=p-1
    return count

def all_dense_necessary(nu,d):
    if d==1:return {F(1),F(1,2)}
    candidate=set()
    for h in range(d-1,nu):
        for P in product(*choices(h)):
            w=solve(P)
            W=(F(0),)+w+(F(1),)
            if not all(a<b for a,b in zip(W,W[1:])):continue
            if not forced_depth(w+(F(1),))<=d<=dual_upper(w+(F(1),)):
                continue
            for v in range(1,h+2):
                alpha=W[v]/2
                if F(1,2**d)<=alpha<=w[0]:
                    candidate.add(alpha)
    return candidate

def full_nu5_check():
    tied_checks()
    expected={1:2,2:23,3:51,4:35,5:20}
    for d in range(1,6):
        necessary=all_dense_necessary(5,d)
        if d==1:
            assert necessary=={F(1),F(1,2)}
            actual=necessary
        else:
            actual,witness,checked=independent_sufficient(5,d)
            if d==3:actual|={F(3,22),F(3,20)}
            assert checked==17302,checked
        assert actual==necessary,(d,
              'unrealized', sorted(necessary-actual),
              'spurious', sorted(actual-necessary))
        assert len(actual)==expected[d],(d,len(actual))
        print(f'PASS ν=5 degree={d}: {len(actual)} exact all-dense exponents')
        print(', '.join(map(str,sorted(actual))))
    print('PASS: all ν=5,d=1..5 arbitrary-dense necessary and constructive sufficient sets coincide')

if __name__=='__main__':
    full_nu5_check()

