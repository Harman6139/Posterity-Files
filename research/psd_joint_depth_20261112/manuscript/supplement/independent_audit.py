#!/usr/bin/env python3
"""Independent finite checks for the consolidated tangency manuscript.

Uses standard-library arithmetic, apart from no external dependencies.
The all-rank theorems are proved in the manuscript. These checks do not replace
those proofs. In particular, this script does not solve unknown real profiles.
"""
from fractions import Fraction as F
from itertools import product
import argparse, json

def cyclic(selection):
    """Whether a functional graph on 0,...,4 has an internal directed cycle."""
    for start in range(5):
        seen=set(); v=start
        while 0 <= v < 5:
            if v in seen: return True
            seen.add(v); v=selection[v]
    return False

def graph_types():
    choices=[[j for j in range(5) if j not in (i,(i+1)%5)]+[5,6]
             for i in range(5)]
    counts={'single_distance_three_chord':0,'adjacent_distance_two_chords':0}
    tested=0
    for seconds in product(*choices):
        tested+=1
        bad=sum(cyclic([seconds[i] if bit[i] else (i+1)%5 for i in range(5)])
                for bit in product((0,1),repeat=5))
        if bad != 5: continue
        chords=[(i,(j-i)%5) for i,j in enumerate(seconds) if j < 5]
        if len(chords)==1 and chords[0][1]==3:
            counts['single_distance_three_chord']+=1
        elif len(chords)==2 and all(d==2 for _,d in chords):
            a,b=[i for i,_ in chords]
            assert (a-b)%5 in (1,4)
            counts['adjacent_distance_two_chords']+=1
        else: raise AssertionError((seconds,chords))
    assert tested==3125 and counts=={'single_distance_three_chord':80,'adjacent_distance_two_chords':40}
    return {'anchored_hamiltonian_graphs_checked':tested,'determinant_27_graphs_by_type':counts}

def solve(A,b):
    B=[[F(v) for v in row]+[F(y)] for row,y in zip(A,b)]
    for i in range(len(B)):
        j=next(j for j in range(i,len(B)) if B[j][i]);B[i],B[j]=B[j],B[i]
        z=B[i][i]; B[i]=[v/z for v in B[i]]
        for j in range(len(B)):
            if j!=i:
                z=B[j][i];B[j]=[u-z*v for u,v in zip(B[j],B[i])]
    return [row[-1] for row in B]

def two_systems():
    mats=[[[8,4,10,5],[14,7,4,2],[1,14,8,4],[2,1,16,8],[4,2,5,16]],
          [[12,10,5],[9,12,6],[15,8,4],[3,16,8],[6,5,16]]]
    accepted=[]
    for kind,M in enumerate(mats):
        vals=[]
        for b in product((0,1),repeat=len(M[0])):
            # Five-cycle in 1-based notation; boundary terms go on the RHS.
            Q=[[2*int(i==j)-int(j==(i+1)%5) for j in range(5)] for i in range(5)]
            if kind==0:
                Q[0][3]-=1; rhs=[0,*b]
            else:
                Q[0][2]-=1;Q[1][3]-=1;rhs=[0,0,*b]
            x=solve(Q,rhs); expected=[F(sum(a*z for a,z in zip(row,b)),27) for row in M]
            assert x==expected
            if F(10,27) in x and min(x)>=F(5,27): vals.append(sorted(x))
        accepted.append(vals)
    assert accepted==[[list(map(lambda x:F(x,27),(5,10,13,16,20)))],
                      [list(map(lambda x:F(x,27),(5,8,10,12,16)))]]
    return [[list(map(str,row)) for row in case] for case in accepted]

def witness():
    lam=F(1,100);c=F(50)
    def gen(child,edges):
        return {(child,child,'D'):F(1),(0,0,'D'):F(-1),**{e:lam for e in edges}}
    H=[gen(1,[(0,3,'R')]),gen(2,[(0,5,'R')]),gen(3,[(2,4,'R'),(0,5,'I')]),
       gen(4,[(2,5,'R')]),gen(5,[(1,6,'R')]),gen(2,[(1,4,'R')])]
    Z=[{(6,6,'D'):F(1)}, {(5,5,'D'):F(1),(1,6,'R'):-c},
       {(3,3,'D'):F(1),(4,4,'D'):F(1),(0,5,'I'):-c,(2,5,'R'):-c},
       {(1,1,'D'):F(1),(2,2,'D'):F(1),(0,3,'R'):-c,(0,5,'R'):-c,(1,4,'R'):-c}]
    pairing=lambda A,B:sum(v*B.get(e,0)*(1 if e[2]=='D' else 2) for e,v in A.items())
    assert all(pairing(A,B)==0 for A in H for B in Z)
    current=set(range(7))
    for S,layer in zip(Z,({6},{5},{3,4},{1,2})):
        comp={e:v for e,v in S.items() if e[0] in current and e[1] in current}
        assert comp=={(a,a,'D'):1 for a in layer};current-=layer
    nums=[0,5,8,10,12,16,27]
    # A strictly diagonally dominant normalized sharp arc, for 0<s<=1/4.
    s=F(1,4); source=1-s**5-s**8-s**10-s**12-s**16
    assert source>F(1,2)
    for A,g in zip(H[:5],(5,8,10,12,16)):
        assert all(nums[a]+nums[b]<=2*g for (a,b,_),v in A.items())
    # Cut capacity calculation at the third stage.
    allowed=[(a,b) for a in range(7) for b in range(a,7)
             if ({a,b}&{5,6}) and nums[a]+nums[b]<=20]
    assert allowed==[(0,5)]
    return {'exact_pairings':24,'successive_compressions':'exact coordinate identities',
            'sharp_arc_source_lower_bound_at_s=1/4':str(source),'off_face_cut':allowed}

def terminal_exception():
    # K=span R_01, target E_00: C_t=diag(1+t,t), Z=E_11 valid.
    # At the full face off-face projection is zero, so every cut rank is zero.
    # A_1=I is NOT in K. The strict-jump lemma therefore requires 0<tau<1.
    return {'counterexample':'X*=E00, K=span(R01) in S^2',
            'first_exposure':'E11','terminal_weight':1,'cut_rank_before':0,
            'cut_rank_after':0,'required_repair':'restrict weighted jump to internal 0<tau<1'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',default='independent_audit.json');a=p.parse_args()
    data={'status':'PASS','scope':'independent finite checks, not an all-dimensional proof',
          'graph_types':graph_types(),'boundary_systems':two_systems(),
          'witness':witness(),'terminal_exception':terminal_exception()}
    with open(a.output,'w') as f:json.dump(data,f,indent=2);f.write('\n')
    print(json.dumps(data,indent=2))
if __name__=='__main__':main()
