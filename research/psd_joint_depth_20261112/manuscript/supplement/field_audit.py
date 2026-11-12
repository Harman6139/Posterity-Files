#!/usr/bin/env python3
"""Exact certificates for the 5/27 real/complex profile separation.

Standard library only. The finite checks certify the denominator-27 lemma,
explicit witnesses, and the separate computer-assisted minimum-nullity claim.
They are not an enumeration-based proof of an all-dimensional real spectrum.
Run: python 140_FIELD_ERASURE_EXACT_AUDIT.py --output results.json
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import combinations, product
from collections import Counter
import argparse
import json


def add(A, key, value):
    A[key] = A.get(key, Q(0)) + Q(value)
    if not A[key]:
        del A[key]


def inner(A, B):
    return sum((v * B.get(k, 0) * (1 if k[2] == 'D' else 2)
                for k, v in A.items()), Q(0))


def gen(child, edges, lam, source=0):
    A = {(child, child, 'D'): Q(1), (source, source, 'D'): Q(-1)}
    for a, b, ch in edges:
        assert a < b
        add(A, (a, b, ch), lam)
    return A


def solve(P):
    h = len(P); k = h + 1
    A = [[Q(0) for _ in range(h + 1)] for _ in range(h)]
    for i, parents in enumerate(P):
        A[i][i] = Q(2)
        for a in parents:
            if a == k:
                A[i][-1] += 1
            elif a:
                A[i][a-1] -= 1
    det = Q(1)
    for col in range(h):
        row = next(j for j in range(col, h) if A[j][col])
        if row != col:
            A[row], A[col] = A[col], A[row]; det = -det
        z = A[col][col]; det *= z
        A[col] = [x / z for x in A[col]]
        for j in range(h):
            if j != col and A[j][col]:
                z = A[j][col]
                A[j] = [x-z*y for x, y in zip(A[j], A[col])]
    assert all(isinstance(x,Q) for row in A for x in row)
    w = (Q(0), *(A[i][-1] for i in range(h)), Q(1))
    return w, det


def harmonic_sets(h):
    choices = [[(a,b) for a in range(i) for b in range(i+1,h+2)]
               for i in range(1,h+1)]
    seen = {}
    for P in product(*choices):
        w, det = solve(P)
        if all(a < b for a,b in zip(w,w[1:])):
            assert det.denominator == 1 and 1 <= det <= 2**h
            seen.setdefault(w, P)
    return list(seen.items())


def compositions(n, k):
    if k == 1:
        yield (n,); return
    for a in range(1,n-k+2):
        for rest in compositions(n-a,k-1):
            yield (a,) + rest


def tables(w, m):
    theta = [Q(0)]
    for wi, mi in zip(w[1:],m):
        theta.extend([wi]*mi)
    terminal = {a for a in range(1,len(theta)) if theta[a] == 1}
    def dfs(S, removed, layers):
        if S == {0}:
            yield layers; return
        M = max(theta[a] for a in S)
        mandatory = {a for a in S if theta[a] == M}
        optional = sorted(S - mandatory - {0})
        mu = min(theta[a] for a in removed)
        for bits in product((0,1),repeat=len(optional)):
            W = {0} | {a for a,b in zip(optional,bits) if b}
            C = S - W
            if any(2*theta[a] < mu for a in C):
                continue
            lower = Q(0)
            for wi in sorted({theta[a] for a in W-{0}}):
                if 2*wi > M+lower:
                    break
                lower = wi
            else:
                yield from dfs(W, removed | C, layers+[sorted(C)])
    yield from dfs(set(range(len(theta)))-terminal,terminal,[sorted(terminal)])


def one_switch_paths(w):
    k = len(w)-1
    def ell(j):
        return sum(2*w[i] < w[j+1] for i in range(1,j))
    def upper(j):
        return next(i-1 for i in range(1,j+1) if 2*w[i] > w[j]+w[i-1])
    states = [k,k-1]
    while states[-1]:
        states.append(upper(states[-1]))
    for s in range(1,len(states)-1):
        path = states[:s+1]
        while path[-1]:
            path.append(ell(path[-1]))
        yield [list(range(b+1,a+1)) for a,b in zip(path,path[1:])]


def single_policy_path(w,P):
    S = set(range(len(w))); layers=[]
    while len(S) > 1:
        blocked = {0}
        while True:
            old = set(blocked)
            for i,(a,b) in enumerate(P,1):
                if i in S and a in S and b in S and ({a,b}&blocked):
                    blocked.add(i)
            if old == blocked:
                break
        C = S-blocked
        assert C
        layers.append(sorted(C)); S -= C
    return layers


def denominator_lemma():
    accepted=[]; checked=0
    for rest in combinations([i for i in range(5,27) if i != 10],4):
        A=tuple(sorted((*rest,10))); S={0,27,*A}; checked+=1
        if all(any(a<x<2*x-a and 2*x-a in S for a in S) for x in A):
            accepted.append(A)
    expected=[(5,8,10,12,16),(5,10,13,16,20)]
    assert sorted(accepted)==expected and checked==5985
    data=[]
    for A in expected:
        nums=(0,*A,27); P=[]
        for i,x in enumerate(A,1):
            parents=[(a,b) for a in range(i) for b in range(i+1,7)
                     if nums[a]+nums[b]==2*x]
            assert len(parents)==1
            P.append(parents[0])
        w,det=solve(P)
        assert det==27 and w==tuple(Q(a,27) for a in nums)
        schedules=[L for L in tables(w,[1]*6) if tuple(map(len,L))==(1,1,2,2)]
        data.append({'numerators':list(nums),'determinant':int(det),
                     'parents':P,'admissible_profile_tables':schedules})
    assert data[0]['admissible_profile_tables']==[[[6],[5],[3,4],[1,2]]]
    assert data[1]['admissible_profile_tables']==[]
    nums=(0,5,8,10,12,16,27); removed={5,6}
    cut=[(a,b) for a in range(7) for b in range(a,7)
         if ({a,b}&removed) and nums[a]+nums[b] <= 20]
    assert cut==[(0,5)]
    return {'integer_subsets_checked':checked,'surviving_spectra':data,
            'real_cut_coordinates_at_10_over_27':cut,
            'mandatory_lower_mode':'H_(8/27), unique tight entry (0,5)'}


def near_extremal_graph_lemma():
    M1=[[8,4,10,5],[14,7,4,2],[1,14,8,4],[2,1,16,8],[4,2,5,16]]
    M2=[[12,10,5],[9,12,6],[15,8,4],[3,16,8],[6,5,16]]
    answer=[]
    for name,M in [('one_skip_three_chord',M1),('two_adjacent_skip_two_chords',M2)]:
        survivors=[];ten_patterns=[]
        for bits in product((0,1),repeat=len(M[0])):
            roots=[6*b for b in bits]
            if len(bits)==4:
                P=[(2,4),(3,roots[0]),(4,roots[1]),(5,roots[2]),(1,roots[3])]
            else:
                P=[(2,3),(3,4),(4,roots[0]),(5,roots[1]),(1,roots[2])]
            w,det=solve(P)
            nums=[sum(a*b for a,b in zip(row,bits)) for row in M]
            assert det==27 and list(w[1:-1])==[Q(x,27) for x in nums]
            if 10 in nums:
                ten_patterns.append({'bits':list(bits),'numerators':nums})
                if min(nums)>=5:
                    survivors.append(sorted(nums))
        answer.append({'type':name,'coefficient_matrix':M,'patterns_containing_10':ten_patterns,
                       'barrier_admissible_sets':survivors})
    assert answer[0]['barrier_admissible_sets']==[[5,10,13,16,20]]
    assert answer[1]['barrier_admissible_sets']==[[5,8,10,12,16]]
    return {'proof':'Five bad parent selections force precisely these two graph types; see manuscript.',
            'independent_model_checks':answer}


def main_witness():
    lam=Q(1,100); c=1/(2*lam)
    specs=[(1,[(0,3,'R')]),(2,[(0,5,'R')]),
           (3,[(2,4,'R'),(0,5,'I')]),(4,[(2,5,'R')]),
           (5,[(1,6,'R')]),(2,[(1,4,'R')])]
    H=[gen(i,E,lam) for i,E in specs]
    Z=[{(6,6,'D'):Q(1)},
       {(5,5,'D'):Q(1),(1,6,'R'):-c},
       {(3,3,'D'):Q(1),(4,4,'D'):Q(1),(0,5,'I'):-c,(2,5,'R'):-c},
       {(1,1,'D'):Q(1),(2,2,'D'):Q(1),(0,3,'R'):-c,
        (0,5,'R'):-c,(1,4,'R'):-c}]
    layers=[[6],[5],[3,4],[1,2]]; S=set(range(7))
    assert all(inner(A,B)==0 for A in H for B in Z)
    for B,C in zip(Z,layers):
        assert {e:v for e,v in B.items() if e[0] in S and e[1] in S}=={
            (a,a,'D'):Q(1) for a in C}
        S-=set(C)
    assert S=={0}
    nums=[0,5,8,10,12,16,27]; theta=[Q(x,27) for x in nums]
    degrees=[theta[i] for i in range(1,6)]+[Q(17,54)]
    initial=[{e:v for e,v in A.items() if (theta[e[0]]+theta[e[1]])/2==g}
             for A,g in zip(H,degrees)]
    W={(i,i,'D'):Q(2)**(2*a*a) for i,a in enumerate(nums)}
    parents=[(0,3),(0,5),(2,4),(2,5),(1,6)]
    rowbounds=[Q(0)]*7
    for i,(a,b) in enumerate(parents,1):
        W[a,b,'R']=-c*W[i,i,'D']
        power=nums[a]**2+nums[b]**2-2*nums[i]**2
        assert power>0
        bound=c/Q(2)**power
        rowbounds[a]+=bound; rowbounds[b]+=bound
    assert all(inner(A,W)==0 for A in initial)
    assert max(rowbounds)<Q(25,64)<1
    # Every monomial-arc coefficient respects its PSD weight order.
    for A,g in zip(H[:5],degrees[:5]):
        assert all(theta[a]+theta[b] <= 2*g for a,b,ch in A)
    # Convert the one imaginary release to a second real source, at index 7.
    def real2(A):
        return {(5,7,'R') if key==(0,5,'I') else key:val for key,val in A.items()}
    HR=list(map(real2,H)); ZR=list(map(real2,Z))
    assert all(inner(A,B)==0 for A in HR for B in ZR)
    # Real rank-one comparison: same exponent and degree, different profile.
    Href=[]
    for A in H[:5]:
        B={}
        for key,val in A.items():
            add(B,(0,5,'R') if key==(0,5,'I') else key,val)
        Href.append(B)
    Zref=[Z[0],Z[1],
          {(2,2,'D'):Q(1),(3,3,'D'):Q(1),(4,4,'D'):Q(1),
           (0,5,'R'):-c,(2,5,'R'):-c},
          {(1,1,'D'):Q(1),(0,3,'R'):-c}]
    assert all(inner(A,B)==0 for A in Href for B in Zref)
    S=set(range(7))
    for B,C in zip(Zref,[[6],[5],[2,3,4],[1]]):
        assert {e:z for e,z in B.items() if e[0] in S and e[1] in S}=={
            (a,a,'D'):Q(1) for a in C}
        S-=set(C)
    # Exact algebra of the direct arbitrary-competitor bounds.
    assert Q(1,15)+Q(8,27)*Q(2,5)==Q(5,27)
    assert Q(4,15)/(1-Q(1,10))==Q(8,27)
    assert Q(1,6)/(1-Q(1,2))==Q(1,3)>Q(8,27)
    return {'complex_order':7,'real_two_source_order':8,
            'nullity':6,'profile':[1,1,2,2],'alpha':'5/27',
            'kernel_dimension':6,'exact_pairings':48,
            'real_rank_one_comparison':{'profile':[1,1,3,1],'alpha':'5/27',
                                       'degree':4,'exact_pairings':20},
            'separator_max_normalized_row_sum':str(max(rowbounds)),
            'arc_integer_orders':nums,'residual_arc_order':27,
            'greedy_minimality':'proved by source-row zero and N_2 equation in manuscript'}


def extra_real_witnesses():
    lam=Q(1,100);c=Q(50);out=[]
    specs=[([Q(0),Q(2,7),Q(4,7),Q(5,7),Q(6,7),Q(1)],2,[None]),
           ([Q(0),Q(3,8),Q(5,8),Q(3,4),Q(7,8),Q(1)],3,[2]),
           ([Q(0),Q(4,9),Q(2,3),Q(7,9),Q(8,9),Q(1)],4,[3,None])]
    for w,p,vlist in specs:
        P=[(0,p),(1,4),(2,4),(3,5)]
        assert all(w[a]+w[b]==2*w[i] for i,(a,b) in enumerate(P,1))
        base=[gen(i,[(*edge,'R')]+([(0,5,'R')] if i==3 else []),lam)
              for i,edge in enumerate(P,1)]
        Z=[{(5,5,'D'):Q(1)},
           {(3,3,'D'):Q(1),(4,4,'D'):Q(1),(0,5,'R'):-c,(3,5,'R'):-c}]
        if p==2:
            Z += [{(2,2,'D'):Q(1),(1,4,'R'):-c},
                  {(1,1,'D'):Q(1),(0,2,'R'):-c}]
            layers=[[5],[3,4],[2],[1]]
        else:
            Z += [{(1,1,'D'):Q(1),(2,2,'D'):Q(1),(0,p,'R'):-c,(1,4,'R'):-c}]
            layers=[[5],[3,4],[1,2]]
        for v in vlist:
            H=base+([{(0,v,'R'):lam}] if v is not None else [])
            assert all(inner(A,B)==0 for A in H for B in Z)
            S=set(range(6))
            for B,C in zip(Z,layers):
                assert {e:z for e,z in B.items()if e[0]in S and e[1]in S}=={
                    (a,a,'D'):Q(1) for a in C}
                S-=set(C)
            alpha=w[1] if v is None else w[v]/2
            assert alpha<=w[1]
            assert w[3]>=Q(1,2)
            out.append({'w':list(map(str,w)),'parents':P,
                        'profile':list(map(len,layers)),'alpha':str(alpha)})
    return out


def minimum_nullity(extra):
    spectra={h:harmonic_sets(h) for h in range(1,5)}
    rows=[]
    extra_keys={(tuple(x['profile']),Q(x['alpha'])) for x in extra}
    expected_counts=[2,4,11,48,292]
    for nu in range(1,6):
        C={((nu,),Q(1)),((nu,),Q(1,2))}; R=set(C)
        for k in range(2,nu+1):
            for w,P in spectra[k-1]:
                exps={x/2 for x in w[1:] if x/2<=w[1]}
                for m in compositions(nu,k):
                    for L in tables(w,m):
                        C.update((tuple(map(len,L)),a)for a in exps)
                    for L in list(one_switch_paths(w))+[single_policy_path(w,P)]:
                        profile=tuple(sum(m[i-1]for i in layer)for layer in L)
                        R.update((profile,a)for a in exps)
        missing=C-R
        if nu==5:
            assert missing==extra_keys
            R|=extra_keys
        else:
            assert not missing
        assert C==R and len(C)==expected_counts[nu-1]
        rows.append({'nullity':nu,'complex_necessary_tuples':len(C),
                     'real_one_switch_or_single_policy':len(C)-len(missing),
                     'additional_tied_edge_witnesses':len(missing),
                     'equality_verified':True})
    return {'status':'PASS (computer-assisted finite minimum-nullity certificate)',
            'depends_on':'Milestone 137 necessity; 128/132 one-switch multiplicity realization; standard single-policy construction',
            'distinct_harmonic_weight_sets':{str(h):len(x)for h,x in spectra.items()},
            'rows':rows,'first_separation_nullity':6}


def product_witness_checks(max_q=5):
    cases=pairings=0
    for q in range(1,max_q+1):
        for d in range(1,q+1):
            for sizes in compositions(q,d):
                groups=[];a=0
                for s in sizes:
                    groups.append(list(range(a,a+s)));a+=s
                parent={a:groups[t-1][0] for t in range(1,d)for a in groups[t]}
                lam=Q(1,100*q*q)
                H=[gen(2*a+1,[(2*b,2*b+1,'R')],lam,source=2*a)
                   for a,b in parent.items()]
                for lower in (False,True):
                    HH=H+([{(2*groups[-1][0],2*groups[-1][0]+1,'R'):lam}] if lower else [])
                    Z=[]
                    for t,C in enumerate(groups):
                        B={(2*a+1,2*a+1,'D'):Q(1) for a in C}
                        if t:
                            b=groups[t-1][0];B[2*b,2*b+1,'R']=-1/(2*lam)
                        Z.append(B)
                    assert all(inner(A,B)==0 for A in HH for B in Z)
                    pairings+=len(HH)*len(Z);cases+=1
    return {'rank_two_boundary_product_cases':cases,'exact_pairings':pairings,
            'scope':'supplementary tests of the all-q proof; q<=5'}


def run():
    extra=extra_real_witnesses()
    return {'status':'PASS','arithmetic':'fractions.Fraction; no numerical PSD tests',
            'main_result':'Coarse real/complex profile spectra first separate at nullity six.',
            'not_claimed':'Complete all-dimensional real-profile or arbitrary-product classification.',
            'denominator_27_certificate':denominator_lemma(),
            'analytic_graph_normal_form_checks':near_extremal_graph_lemma(),
            'explicit_main_witness':main_witness(),
            'four_small_nullity_real_witnesses':extra,
            'minimum_nullity_certificate':minimum_nullity(extra),
            'product_checks':product_witness_checks()}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='140_FIELD_ERASURE_EXACT_AUDIT_RESULTS.json')
    args=parser.parse_args()
    results=run()
    with open(args.output,'w',encoding='utf-8') as f:
        json.dump(results,f,indent=2);f.write('\n')
    print(json.dumps(results,indent=2))
