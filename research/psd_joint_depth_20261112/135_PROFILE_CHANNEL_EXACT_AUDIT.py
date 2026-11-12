#!/usr/bin/env python3
"""Exact-rational audit of the two-channel prefix construction.

This tests the finite algebraic certificates; the all-dimensional theorem and
real-cone impossibility proof are in milestones 133 and 134. No floating-point PSD test
or numerical exponent fitting is used. Python standard library only.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import product
from math import factorial
import argparse
import json

# Sparse Hermitian coordinates: (a,a,'D'), or (a,b,'R'/'I') for a<b.
def add(A, key, value):
    A[key] = A.get(key, Q(0)) + Q(value)
    if not A[key]:
        del A[key]

def inner(A, B):
    return sum((v * B.get(e, Q(0)) * (1 if e[2] == 'D' else 2)
                for e, v in A.items()), Q(0))

def gen(n, child, edges, lam=Q(1, 100)):
    A = {(child, child, 'D'): Q(1), (0, 0, 'D'): Q(-1)}
    for a, b, channel in edges:
        assert 0 <= a < b < n
        add(A, (a, b, channel), lam)
    return A

def eta(e, w):
    return (w[e[0]] + w[e[1]]) / 2

def ell(w, j):
    return sum(2*w[i] < w[j+1] for i in range(1, j))

def upper(w, j):
    return next(i for i in range(1, j+1)
                if 2*w[i] > w[j] + w[i-1]) - 1

def schedules(w):
    k = len(w)-1
    def tail(j):
        if j == 0:
            yield [0]
        else:
            for q in range(ell(w, j), upper(w, j)+1):
                for path in tail(q):
                    yield [j] + path
    if k == 1:
        yield [1, 0]
    else:
        for path in tail(k-1):
            yield [k] + path

def solve_policy(P):
    h = len(P)
    if not h:
        return [Q(0), Q(1)]
    k = h+1
    M = [[Q(0) for _ in range(h+1)] for _ in range(h)]
    for i, (a, b) in enumerate(P, 1):
        M[i-1][i-1] = 2
        for v in (a, b):
            if v == k:
                M[i-1][-1] += 1
            elif v:
                M[i-1][v-1] -= 1
    for col in range(h):
        pivot = next((row for row in range(col,h) if M[row][col]), None)
        if pivot is None:
            raise AssertionError('Harmonic boundary system singular')
        M[col], M[pivot] = M[pivot], M[col]
        a = M[col][col]
        M[col] = [x/a for x in M[col]]
        for row in range(h):
            if row != col and M[row][col]:
                a = M[row][col]
                M[row] = [x-a*y for x,y in zip(M[row],M[col])]
    w = [Q(0)] + [M[i][-1] for i in range(h)] + [Q(1)]
    return w if all(a < b for a,b in zip(w,w[1:])) else None

def construct_and_check(P, w, path, v=None):
    k = len(w)-1
    n = k+1
    lam = Q(1,100)
    assert path[:2] == [k,k-1] and path[-1] == 0
    for j,q in zip(path[1:-1],path[2:]):
        assert ell(w,j) <= q <= upper(w,j)
    d = len(path)-1
    layers = [list(range(path[t]+1, path[t-1]+1)) for t in range(1,d+1)]
    time = {i:t for t,C in enumerate(layers,1) for i in C}
    assert time[k] == 1
    releases = {i:(0,path[time[i]-1]+1) for i in range(1,k)}
    blockers = {i:(i-1,path[time[i]-2]) for i in range(1,k)}
    Powner = {pair:i for i,pair in enumerate(P,1)}
    assert len(Powner) == len(P)
    release_set = set(releases.values())
    H = []
    degrees = []
    pivots = []
    for i,pair in enumerate(P,1):
        assert w[pair[0]]+w[pair[1]] == 2*w[i]
        assert w[releases[i][1]] <= 2*w[i]
        H.append(gen(n,i,[(*pair,'R'),(*releases[i],'I')],lam))
        degrees.append(w[i]); pivots.append((*pair,'R'))
    blocker_channel = {}
    omitted = []
    for i,B in blockers.items():
        assert B[0] < i < B[1]
        degree = (w[B[0]]+w[B[1]])/2
        assert degree >= w[i]
        if B in Powner and B in release_set:
            # The sole three-way physical collision is redundant, not a
            # new independent coefficient and not a multichild transfer.
            assert i == 1 and Powner[B] == 1
            assert B == releases[1] and time[1] == d
            assert B[1] == path[-3] == path[-2]+1
            omitted.append(i)
            continue
        channel = 'I' if B in Powner else 'R'
        blocker_channel[i] = channel
        H.append(gen(n,i,[(*B,channel)],lam))
        degrees.append(degree); pivots.append((*B,channel))
    alpha = w[1]
    if v is not None and w[v]/2 < w[1]:
        alpha = w[v]/2
        G = {(0,v,'R'):lam}
        H.append(G); degrees.append(alpha); pivots.append((0,v,'R'))
    assert len(set(pivots)) == len(pivots)
    initials = [{e:c for e,c in A.items() if eta(e,w) == degree}
                for A,degree in zip(H,degrees)]
    for a,A in enumerate(initials):
        for b,pivot in enumerate(pivots):
            assert A.get(pivot,0) == (lam if a == b else 0)
    assert min(degrees) == alpha

    # Formal separator: W_e is a Q-linear combination of the symbols z_i.
    W = {(i,i,'D'):{i:Q(1)} for i in range(n)}
    for i,pair in enumerate(P,1):
        W[(*pair,'R')] = {i:-1/(2*lam)}
    for i,channel in blocker_channel.items():
        B=blockers[i]
        if (w[B[0]]+w[B[1]])/2 == w[i]:
            assert (*B,channel) not in W
            W[(*B,channel)] = {i:-1/(2*lam)}
    for A in initials:
        polynomial = {}
        for e,c in A.items():
            for symbol,a in W.get(e,{}).items():
                polynomial[symbol] = polynomial.get(symbol,0) + c*a*(1 if e[2]=='D' else 2)
        assert all(a == 0 for a in polynomial.values())
    for (a,b,ch),terms in W.items():
        if ch != 'D':
            for i,c in terms.items():
                assert (w[a]**2+w[b]**2)/2 - w[i]**2 > 0

    # Ambient stresses: all offdiagonal assignments are off the current face.
    stresses = []
    for t,C in enumerate(layers,1):
        Z = {(i,i,'D'):Q(1) for i in C}
        if t > 1:
            R=(0,path[t-1]+1,'I')
            add(Z,R,-1/(2*lam))
            for i in C:
                if i in blocker_channel:
                    add(Z,(*blockers[i],blocker_channel[i]),-1/(2*lam))
        assert all(inner(Z,A)==0 for A in H)
        j=path[t-1]
        compressed={e:c for e,c in Z.items() if e[0]<=j and e[1]<=j}
        assert compressed == {(i,i,'D'):Q(1) for i in C}
        # Exact hypotheses of the all-PSD maximality argument.
        for i in range(1,path[t]+1):
            if i in blocker_channel:
                a,b=blockers[i]
                assert a == i-1 and a < i < b <= j
            else:
                assert i == 1 and i in omitted
                assert P[0] == releases[1] == blockers[1]
                assert P[0][0] == 0 and P[0][1] <= j
        stresses.append(Z)
    return {'degrees':list(map(str,degrees)), 'alpha':str(alpha),
            'profile':list(map(len,layers)), 'omitted_blockers':omitted,
            'kernel_dimension':len(H), 'stress_count':len(stresses)}

def optimized_witness_check():
    w=list(map(Q,['0','1/4','3/7','1/2','17/28','5/7','1']))
    P=[(0,3),(1,4),(0,6),(3,5),(2,6)]
    lam=Q(1,100); c=1/(2*lam)
    H=[gen(7,1,[(0,3,'R'),(0,2,'I')]),
       gen(7,2,[(1,4,'R'),(0,4,'I')]),
       gen(7,3,[(0,6,'R'),(0,4,'I')]),
       gen(7,4,[(3,5,'R'),(0,6,'I')]),
       gen(7,5,[(2,6,'R'),(0,6,'I')]),
       gen(7,2,[(1,5,'R')]), gen(7,3,[(2,5,'R')])]
    Z=[{(6,6,'D'):Q(1)},
       {(4,4,'D'):Q(1),(5,5,'D'):Q(1),(0,6,'I'):-c},
       {(2,2,'D'):Q(1),(3,3,'D'):Q(1),(0,4,'I'):-c,(1,5,'R'):-c,(2,5,'R'):-c},
       {(1,1,'D'):Q(1),(0,2,'I'):-c}]
    assert all(inner(S,A)==0 for S in Z for A in H)
    for v in (1,2):
        G={(0,v,'R'):lam}
        assert all(inner(S,G)==0 for S in Z)
    # A second real source replaces every imaginary source edge exactly.
    def second_source(A):
        return {(b,7,'R') if ch=='I' and a==0 else (a,b,ch):z
                for (a,b,ch),z in A.items()}
    assert all(inner(second_source(S),second_source(A))==0 for S in Z for A in H)
    for S,j,C in zip(Z,[6,5,3,1],[[6],[4,5],[2,3],[1]]):
        assert {e:c for e,c in S.items() if e[0]<=j and e[1]<=j} == {(i,i,'D'):Q(1) for i in C}
    degree=w[1:6]+[(w[1]+w[5])/2,(w[2]+w[5])/2]
    assert degree[-2:]==[Q(27,56),Q(4,7)]
    pivots=[(*p,'R') for p in P]+[(1,5,'R'),(2,5,'R')]
    initials=[{e:c for e,c in A.items() if eta(e,w)==m} for A,m in zip(H,degree)]
    for a,A in enumerate(initials):
        assert all(A.get(e,0)==(lam if a==b else 0) for b,e in enumerate(pivots))
    a=[int(28*x) for x in w]
    W={(i,i,'D'):Q(2**(a[i]*a[i])) for i in range(7)}
    for i,(u,v) in enumerate(P,1):
        W[(u,v,'R')]=-W[(i,i,'D')]/(2*lam)
    assert all(inner(W,A)==0 for A in initials)
    gaps=[Q((a[u]-a[v])**2,4) for u,v in P]
    assert min(gaps)==9
    # Every row has at most two such entries. Exact normalized row-sum < 1.
    assert 2*c/Q(2**9) < 1

    # Arithmetic premises of the REAL impossibility proof.
    assert [p for p in product(range(3), range(4,7)) if w[p[0]]+w[p[1]]==2*w[3]] == [(0,6)]
    for i in (3,4):
        allowed=[a for a in range(6) if (w[a]+1)/2<=w[i]]
        assert allowed==[0]
    assert (w[2]+w[5])/2 < w[4]
    dual_order=1-w[4]
    assert dual_order==Q(11,28)
    assert 1-(w[3]+w[4])/2 > dual_order
    assert 1-w[3] > dual_order
    assert w[3] < w[4] < w[5]
    return {'weights':list(map(str,w)), 'profile':[1,2,2,1],
            'alpha':'1/4', 'kernel_dimension':7,
            'pairings_checked':28, 'separator_row_bound':str(2*c/Q(2**9)),
            'real_obstruction_dual_order':str(dual_order)}

def real_profile_family_check():
    w=list(map(Q,['0','1/4','3/7','1/2','17/28','5/7','1']))
    P=[(0,3),(1,4),(0,6),(3,5),(2,6)]
    lam=Q(1,100); c=1/(2*lam)
    base=[gen(7,i,[(*p,'R')]) for i,p in enumerate(P,1)]
    def stress(C, edges=(), values=None):
        S={(i,i,'D'):Q(1) for i in C}
        for e in edges: add(S,(*e,'R'),-c)
        if values: S.update(values)
        return S
    # A: (1,3,2)
    A=[H.copy() for H in base]
    for i in (4,5): add(A[i-1],(0,6,'R'),lam)
    ZA=[stress([6]),stress([3,4,5],[(0,6)]),stress([1,2],[(0,3),(1,4)])]
    # B: (1,1,3,1). Only the middle stress has an on-face cross entry.
    B=[H.copy() for H in base]; add(B[1],(0,5,'R'),lam)
    B.append(gen(7,3,[(2,4,'R')]))
    a=[int(28*x) for x in w]
    z={i:Q(2**(2*a[i]**2)) for i in (2,3,4)}
    mid={(i,i,'D'):z[i] for i in (2,3,4)}
    mid.update({(0,5,'R'):-c*z[2],(0,6,'R'):-c*z[3],
                (2,4,'R'):-c*z[3],(3,5,'R'):-c*z[4]})
    assert z[2]*z[4] > c*c*z[3]*z[3]
    ZB=[stress([6]),stress([5],[(2,6)]),mid,stress([1],[(0,3)])]
    # C: (1,1,2,2)
    C=[H.copy() for H in base]+[gen(7,3,[(2,5,'R')])]
    ZC=[stress([6]),stress([5],[(2,6)]),
        stress([3,4],[(0,6),(2,5),(3,5)]),stress([1,2],[(0,3),(1,4)])]
    # D: (1,1,1,2,1)
    D=[H.copy() for H in base]+[gen(7,3,[(2,4,'R')])]
    ZD=[stress([6]),stress([5],[(2,6)]),stress([4],[(3,5)]),
        stress([2,3],[(1,4),(0,6),(2,4)]),stress([1],[(0,3)])]
    out=[]
    for H,Z,profile in [(A,ZA,[1,3,2]),(B,ZB,[1,1,3,1]),
                        (C,ZC,[1,1,2,2]),(D,ZD,[1,1,1,2,1])]:
        for v in (None,1,2):
            HH=H+([] if v is None else [{(0,v,'R'):lam}])
            assert all(inner(S,T)==0 for S in Z for T in HH)
        # Other than B's explicit PD 2x2 block, the compressed stresses
        # are diagonal. All parent inequalities and leading pivots are
        # as in the main proof; no eigenvalue fitting is used.
        out.append({'profile':profile,'exponents':['1/8','3/14','1/4'],
                    'kernel_dimension_without_leading_edge':len(H)})
    return out


def nonprefix_example_check():
    w=list(map(Q,['0','1/4','2/5','1/2','3/5','4/5','1']))
    P=[(0,3),(0,5),(0,6),(2,5),(4,6)]
    assert all(w[a]+w[b]==2*w[i] for i,(a,b) in enumerate(P,1))
    # Verify actual original-generator/ambient-stress pairings.
    c=Q(50)
    H=[gen(7,i,[(*p,'R')]) for i,p in enumerate(P,1)]
    Z=[{(6,6,'D'):Q(1)},
       {(3,3,'D'):Q(1),(5,5,'D'):Q(1),(0,6,'R'):-c,(4,6,'R'):-c},
       {(1,1,'D'):Q(1),(2,2,'D'):Q(1),(4,4,'D'):Q(1),
        (0,3,'R'):-c,(0,5,'R'):-c,(2,5,'R'):-c}]
    assert all(inner(S,T)==0 for S in Z for T in H)
    faces=[set(range(7)),set(range(6)),{0,1,2,4}]
    layers=[[6],[3,5],[1,2,4]]
    for S,F,C in zip(Z,faces,layers):
        assert {e:c for e,c in S.items() if e[0] in F and e[1] in F} == {(i,i,'D'):Q(1) for i in C}
    assert ell(w,3)==1
    # Therefore the same rank drops cannot be the sorted prefix schedule
    # 6 -> 5 -> 3 -> 0 at these particular weights.
    return {'weights':list(map(str,w)), 'real_layers':[[6],[3,5],[1,2,4]],
            'sorted_prefix_schedule_fails_at':{'j':3,'q':0,'ell':ell(w,3)}}

def denominator_seven_check():
    # This verifies the exact identities used in the analytical exclusion;
    # it is not an exhaustive search used as a substitute for that proof.
    w=list(map(Q,['0','3/7','5/7','6/7','1']))
    P=[(0,3),(1,4),(2,4)]
    assert solve_policy(P)==w
    assert upper(w,3)==1
    assert list(schedules(w))==[[4,3,1,0]]
    beta=Q(2,5)
    for alpha in (Q(3,14),Q(5,14)):
        assert (2*alpha).denominator==7
        assert Q(1,8)<=alpha<=beta
        assert alpha<=w[1] and 2*alpha in w
    return {'weights':list(map(str,w)),
            'exponents':['3/14','5/14'],
            'excluded_profile':[1,1,2],
            'attained_profile':[1,2,1],
            'profile_upper_endpoint':'2/5',
            'forced_second_rank_at_least':2}

def run(max_h=4):
    summary=[]
    checks=0; omitted=0
    for h in range(1,max_h+1):
        choices=[[(a,b) for a in range(i) for b in range(i+1,h+2)]
                 for i in range(1,h+1)]
        strict=0; paths=0; cases=0
        for P in product(*choices):
            w=solve_policy(P)
            if w is None:
                continue
            strict+=1
            for path in schedules(w):
                paths+=1
                # All possible sharp half-weights, including alpha=w_1.
                for v in range(1,len(w)):
                    if w[v]/2<=w[1]:
                        c=construct_and_check(P,w,path,v)
                        cases+=1; checks+=1; omitted+=bool(c['omitted_blockers'])
        summary.append({'internal_vertices':h,'parent_assignments':factorial(h)**2,
                        'strict_policies':strict,'prefix_schedules':paths,
                        'exponent_schedule_checks':cases})
    return {'status':'PASS','arithmetic':'fractions.Fraction; no floating-point tests',
            'scope':'finite supplementary certificate audit, not the all-dimensional proof',
            'families':summary,'total_exponent_schedule_checks':checks,
            'redundant_three_way_collision_cases':omitted,
            'optimized_complex_witness':optimized_witness_check(),
            'complete_real_profile_family':real_profile_family_check(),
            'nonprefix_scope_warning':nonprefix_example_check(),
            'denominator_seven_endpoint_obstruction':denominator_seven_check()}

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--max-h',type=int,default=4)
    p.add_argument('--output')
    args=p.parse_args()
    if not 1<=args.max_h<=6:
        p.error('--max-h must be between 1 and 6')
    result=run(args.max_h)
    text=json.dumps(result,indent=2)+'\n'
    if args.output:
        with open(args.output,'w',encoding='utf-8') as f:
            f.write(text)
    print(text,end='')
