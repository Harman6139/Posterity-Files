#!/usr/bin/env python3
"""Exact supplementary audit for Milestone 137's general survivor-table theorem.

Python standard library only. Checks arbitrary (including non-prefix) schedules,
repeated valuation grades split across steps, original ambient stress pairings,
independent initial forms, symbolic positive separation, and all collision and
maximality premises. The finite audit is not the all-dimensional proof.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import product
from math import factorial
import argparse
import json


def add(A, key, value):
    A[key] = A.get(key, Q(0)) + Q(value)
    if not A[key]:
        del A[key]


def inner(A, B):
    """Real Hermitian trace pairing in independent D/R/I coordinates."""
    return sum((value * B.get(key, Q(0)) * (1 if key[2] == 'D' else 2)
                for key, value in A.items()), Q(0))


def gen(n, child, edges, lam):
    A = {(child, child, 'D'): Q(1), (0, 0, 'D'): Q(-1)}
    for a, b, channel in edges:
        assert 0 <= a < b < n
        add(A, (a, b, channel), lam)
    return A


def solve_policy(P):
    """Solve one rational harmonic boundary system; reject unordered solutions."""
    h = len(P)
    k = h + 1
    M = [[Q(0) for _ in range(h + 1)] for _ in range(h)]
    for i, (a, b) in enumerate(P, 1):
        M[i-1][i-1] = Q(2)
        for v in (a, b):
            if v == k:
                M[i-1][-1] += 1
            elif v:
                M[i-1][v-1] -= 1
    for col in range(h):
        pivot = next((row for row in range(col, h) if M[row][col]), None)
        assert pivot is not None, 'Harmonic boundary matrix must be nonsingular'
        M[col], M[pivot] = M[pivot], M[col]
        z = M[col][col]
        M[col] = [x/z for x in M[col]]
        for row in range(h):
            if row != col and M[row][col]:
                z = M[row][col]
                M[row] = [x-z*y for x, y in zip(M[row], M[col])]
    w = [Q(0)] + [M[i][-1] for i in range(h)] + [Q(1)]
    return w if all(a < b for a, b in zip(w, w[1:])) else None


def all_tables(w,m):
    coord_grade=[0]
    for g,mm in enumerate(m,1):coord_grade.extend([g]*mm)
    theta=[w[g] for g in coord_grade]
    terminal={a for a,g in enumerate(coord_grade) if g==len(w)-1}
    def dfs(S,removed,layers):
        if S=={0}:yield layers;return
        M=max(theta[a] for a in S)
        mandatory={a for a in S if theta[a]==M}
        candidates=sorted(S-mandatory-{0})
        mu=min(theta[a] for a in removed)
        for bits in product((0,1),repeat=len(candidates)):
            F={0}|{a for a,b in zip(candidates,bits) if b}
            C=S-F
            if any(2*theta[a]<mu for a in C):continue
            prev=Q(0)
            ok=True
            for a in sorted(F-{0}):
                if 2*theta[a]>M+prev:ok=False;break
                prev=theta[a]
            if ok:yield from dfs(F,removed|C,layers+[sorted(C)])
    yield from dfs(set(range(len(theta)))-terminal,terminal,[sorted(terminal)])

def check(P,w,m,layers,v=None):
    grade=[0]
    for g,mm in enumerate(m,1):grade.extend([g]*mm)
    theta=[w[g] for g in grade];n=len(theta);k=len(w)-1
    rep={g:grade.index(g) for g in range(k+1)}
    parent={i:(rep[P[grade[i]-1][0]],rep[P[grade[i]-1][1]]) for i in range(1,n) if grade[i]<k}
    Pset=set(parent.values())
    time={a:t for t,C in enumerate(layers,1) for a in C}
    S=[set(range(n))]
    for C in layers:S.append(S[-1]-set(C))
    assert S[-1]=={0} and set(layers[0])=={a for a in range(1,n) if grade[a]==k}
    rel={};block={}
    for i in parent:
        t=time[i]
        removed=set(range(n))-S[t-1]
        r=min(removed,key=lambda a:(theta[a],time[a],a))
        e=(0,r) if theta[i]<theta[r] else tuple(sorted((r,i)))
        rel[i]=e
        a=max(x for x in S[t-1] if x<i)
        old=S[t-2]
        b=min(x for x in old if theta[x]==max(theta[y] for y in old))
        assert theta[a]<=theta[i]<theta[b]
        block[i]=(a,b)
        assert sum(theta[x]for x in e)<=2*theta[i]
        assert theta[a]+theta[b]>=2*theta[i]
    assert len(set(block.values()))==len(block)
    Rset=set(rel.values())
    for e in Rset:assert len({time[i]for i in rel if rel[i]==e})==1
    lam=Q(1,100*n*n)
    H=[];degrees=[];indices=[];channels={};omit=[]
    for i in parent:
        H.append(gen(n,i,[(*parent[i],'R'),(*rel[i],'I')],lam));degrees.append(theta[i]);indices.append(('H',i))
    for i,B in block.items():
        if B in Pset and B in Rset:
            assert B[0]==0 and B==parent[i]==rel[i]
            assert theta[i]==theta[B[1]]/2
            assert all(time[j]==time[i]for j in rel if rel[j]==B)
            omit.append(i);continue
        ch='I' if B in Pset else 'R';channels[i]=ch
        H.append(gen(n,i,[(*B,ch)],lam));degrees.append(sum(theta[x]for x in B)/2);indices.append(('N',i))
    alpha=w[1]
    if v is not None and w[v]/2<w[1]:
        alpha=w[v]/2
        H.append({(0,rep[v],'R'):lam});degrees.append(alpha);indices.append(('G',0))
    def eta(e):return (theta[e[0]]+theta[e[1]])/2
    init=[{e:x for e,x in A.items()if eta(e)==de} for A,de in zip(H,degrees)]
    for j,(kind,i)in enumerate(indices):
        if kind=='N':pivot=(*block[i],channels[i])
        elif kind=='G':pivot=(0,rep[v],'R')
        else:continue
        assert all(B.get(pivot,0)==(lam if a==j else 0)for a,B in enumerate(init))
    Hids=[a for a,x in enumerate(indices)if x[0]=='H']
    for a in Hids:
        i=indices[a][1]
        assert all(init[b].get((i,i,'D'),0)==(1 if a==b else 0)for b in Hids)
    W={(a,a,'D'):{grade[a]:Q(1)}for a in range(n)}
    for i,p in parent.items():
        e=(*p,'R');value={grade[i]:-1/(2*lam)}
        if e in W:assert W[e]==value
        W[e]=value
    for i,ch in channels.items():
        B=block[i]
        if sum(theta[x]for x in B)==2*theta[i]:
            e=(*B,ch);value={grade[i]:-1/(2*lam)}
            if e in W:assert W[e]==value
            W[e]=value
    for A in init:
        pol={}
        for e,c in A.items():
            for g,z in W.get(e,{}).items():pol[g]=pol.get(g,0)+c*z*(1 if e[2]=='D'else 2)
        assert all(z==0 for z in pol.values())
    for e,pol in W.items():
        if e[2]=='D':continue
        for g,c in pol.items():assert (theta[e[0]]**2+theta[e[1]]**2)/2>w[g]**2
    for t,C in enumerate(layers,1):
        Z={(i,i,'D'):Q(1)for i in C}
        if t>1:
            for e in set(rel[i]for i in C):add(Z,(*e,'I'),-1/(2*lam))
            for i in C:
                if i in channels:add(Z,(*block[i],channels[i]),-1/(2*lam))
        assert all(inner(Z,A)==0 for A in H)
        assert {e:c for e,c in Z.items()if e[0]in S[t-1] and e[1]in S[t-1]}=={(i,i,'D'):Q(1)for i in C}
        for i in S[t]-{0}:
            if i in channels:
                a,b=block[i];assert a in S[t]and a<i and b in S[t-1]
            else:
                assert i in omit and parent[i]==rel[i]==block[i]and block[i][0]==0 and block[i][1]in S[t-1]
    assert min(degrees)==alpha
    split = any(len({time[a] for a in range(1,n) if grade[a]==g})>1
                for g in range(1,k+1))
    prefix = all((not (current-{0})) or
                 max(theta[a] for a in current-{0}) <=
                 min(theta[b] for b in set(range(1,n))-current)
                 for current in S[1:-1])
    # Equal-grade splits are tracked separately. 'non_prefix' here means a
    # genuinely lower-weight coordinate was removed while a higher survives.
    return {'omitted_blockers':len(omit), 'split_grade':split,
            'non_prefix':not prefix, 'kernel_dimension':len(H),
            'profile':list(map(len,layers)), 'alpha':str(alpha),
            'generator_stress_pairings':len(H)*len(layers)}



def explicit_examples():
    # A genuine non-prefix profile already realizable over R (Milestone 134).
    P = [(0,3),(0,5),(0,6),(2,5),(4,6)]
    w = solve_policy(P)
    m = [1]*6
    layers = [[6],[3,5],[1,2,4]]
    nonprefix = check(P,w,m,layers,3)
    assert nonprefix['non_prefix'] and nonprefix['profile'] == [1,2,3]
    # A repeated grade split between two stages.
    P2 = [(0,2),(0,4),(2,4)]
    w2 = solve_policy(P2)
    assert w2 == [Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)]
    m2 = [1,2,1,1]
    layers2 = [[5],[2,4],[3],[1]]
    split = check(P2,w2,m2,layers2,2)
    assert split['split_grade'] and split['profile'] == [1,2,1,1]
    return {'non_prefix':{'weights':list(map(str,w)), 'multiplicities':m,
                          'layers':layers, **nonprefix},
            'split_grade':{'weights':list(map(str,w2)), 'multiplicities':m2,
                           'layers':layers2, **split}}


def run(max_h=4):
    rows=[]
    total=split=omitted=nonprefix=pairings=0
    for h in range(1,max_h+1):
        policies=cases=tables=0
        choices=[[(a,b) for a in range(i) for b in range(i+1,h+2)]
                 for i in range(1,h+1)]
        for P in product(*choices):
            w=solve_policy(P)
            if w is None:
                continue
            policies+=1
            k=h+1
            # Simple grades, followed by one extra coordinate in each grade.
            multiplicities=[[1]*k]+[[1+(a==g) for a in range(k)] for g in range(k)]
            for m in multiplicities:
                for layers in all_tables(w,m):
                    tables+=1
                    for v in range(1,k+1):
                        if w[v]/2>w[1]:
                            continue
                        result=check(P,w,m,layers,v)
                        cases+=1
                        total+=1
                        omitted+=bool(result['omitted_blockers'])
                        split+=result['split_grade']
                        nonprefix+=result['non_prefix']
                        pairings+=result['generator_stress_pairings']
        rows.append({'internal_grades':h,'parent_assignments':factorial(h)**2,
                     'strict_policies':policies,'labelled_schedules':tables,
                     'exponent_schedule_checks':cases})
    return {'status':'PASS','arithmetic':'fractions.Fraction; no floating-point tests',
            'scope':'Finite supplementary construction audit, not a proof by enumeration.',
            'multiplicity_family':'All simple grades, plus one extra coordinate in each grade.',
            'counting_convention':'Labelled coordinate schedules; not distinct attainable tuples.',
            'families':rows,'total_exponent_schedule_checks':total,
            'split_grade_cases':split,'non_prefix_cases':nonprefix,
            'redundant_source_blocker_cases':omitted,
            'generator_stress_pairings_checked':pairings,
            'explicit_examples':explicit_examples()}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-h',type=int,default=4)
    parser.add_argument('--output',help='Optional JSON output path')
    args=parser.parse_args()
    if not 1<=args.max_h<=6:
        parser.error('--max-h must lie between 1 and 6')
    result=run(args.max_h)
    output=json.dumps(result,indent=2)+'\n'
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:
            f.write(output)
    print(output,end='')
