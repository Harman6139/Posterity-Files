"""Exact algebraic audit of the one-switch construction; no SDP or numerical fitting.

This program validates a deterministic construction on supplied harmonic policies.
It is a regression check, not the proof of the all-nullity theorem.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from fractions import Fraction as F
from typing import Sequence

Edge = tuple[int, int]

def harmonic_weights(parents: Sequence[Edge]) -> tuple[F, ...]:
    h = len(parents); k = h + 1
    A = [[F(2 * (i == j)) for j in range(1, k)] + [F(0)] for i in range(1, k)]
    for i, (a, b) in enumerate(parents, 1):
        if not (0 <= a < i < b <= k):
            raise ValueError(f"Invalid ordered parents at {i}: {(a,b)}")
        for p in (a, b):
            if 0 < p < k: A[i-1][p-1] -= 1
            elif p == k: A[i-1][-1] += 1
    for c in range(h):
        p = next((r for r in range(c, h) if A[r][c]), None)
        if p is None: raise ValueError("Singular harmonic system")
        A[c], A[p] = A[p], A[c]
        z = A[c][c]; A[c] = [x/z for x in A[c]]
        for r in range(h):
            if r != c:
                z = A[r][c]
                A[r] = [x-z*y for x,y in zip(A[r],A[c])]
    w = (F(0), *(A[i][-1] for i in range(h)), F(1))
    if not all(w[i] < w[i+1] for i in range(k)):
        raise ValueError("Harmonic solution is not strictly ordered")
    return w

def lower(w: Sequence[F], j: int) -> int:
    return sum(2*w[i] < w[j+1] for i in range(1,j))

def upper(w: Sequence[F], j: int) -> int:
    return next(i for i in range(1,j+1) if 2*w[i] > w[j]+w[i-1]) - 1

def tail(w: Sequence[F], j: int, use_upper: bool=False) -> list[int]:
    out = [j]
    while j:
        j = upper(w,j) if use_upper else lower(w,j)
        out.append(j)
    return out

@dataclass
class Generator:
    main: Edge
    children: set[int]
    owner: int | None = None
    release: Edge | None = None

    @property
    def edges(self) -> set[Edge]:
        return {self.main} | ({self.release} if self.release is not None else set())

@dataclass
class Construction:
    parents: tuple[Edge,...]
    w: tuple[F,...]
    cut: int
    q: int
    b: int
    states: list[int]
    generators: list[Generator]
    alpha: F
    leading: Edge | None
    upper_states: list[int]
    tail_states: list[int]
    blocker_data: list[tuple[int,Edge,str]] = field(default_factory=list)


def construct(parents: Sequence[Edge], cut: int, v: int) -> Construction:
    P=tuple(parents); w=harmonic_weights(P); k=len(w)-1; h=k-1
    us=[k]+tail(w,k-1,True)
    U=len(us)-1
    if not 1 <= cut <= U: raise ValueError("Invalid cut")
    if not 1 <= v <= k: raise ValueError("Invalid distinguished vertex")
    alpha=w[v]/2
    if alpha > w[1]: raise ValueError("Invalid halfweight")
    q,b=us[cut],us[cut-1]
    ls=tail(w,q)
    states=us[:cut+1]+ls[1:]
    leading=(0,v) if alpha < w[1] else None
    gens=[Generator(P[i-1],{i},i) for i in range(1,k)]
    owns={g.main:g for g in gens}
    blockers=[]
    for i in range(1,k):
        if i>q:
            c=next(c for c in range(i+1,k+1) if w[i-1]+w[c]>=2*w[i])
            e=(i-1,c); kind="upper"
        elif P[i-1][1]>b:
            e=(i-1,b); kind="switch"
        else:
            continue
        blockers.append((i,e,kind))
        if e in owns:
            owns[e].children.add(i)
        else:
            g=Generator(e,{i}); gens.append(g); owns[e]=g
    for g in gens:
        if g.owner is not None and g.owner<=q:
            i=g.owner
            J=next(J for J,Q in zip(ls,ls[1:]) if Q<i<=J)
            e=(0,J+1)
            if e != g.main and e != leading: g.release=e
    return Construction(P,w,cut,q,b,states,gens,alpha,leading,us,ls,blockers)


def grade_layer(states: Sequence[int], i: int) -> int:
    return next(s for s,(J,Q) in enumerate(zip(states,states[1:]),1) if Q < i <= J)

def pair(g: Generator, z: Sequence[F], t: dict[Edge,F]) -> F:
    # t_ab = 2*lambda*Z_ab; all generators use +lambda on each edge.
    return sum(z[i] for i in g.children) + sum(t.get(e,F(0)) for e in g.edges)

def audit(c: Construction) -> dict[str,int]:
    w=c.w; k=len(w)-1; h=k-1; q,b=c.q,c.b
    mains={g.main:g for g in c.generators}
    assert len(mains)==len(c.generators)
    assert all(len(g.children)<=2 for g in c.generators)
    assert all(c.leading not in g.edges for g in c.generators)
    # Every generator preserves trace by subtracting its child count at source.
    # Anchor orders, safe child orders, and triangular sharing.
    for g in c.generators:
        a,z=g.main; eta=(w[a]+w[z])/2
        for i in g.children:
            assert a<i<z and w[i]<=eta
        if g.owner is not None:
            assert eta==w[g.owner]
            assert all(i<=g.owner for i in g.children)
            if g.release:
                assert (w[g.release[0]]+w[g.release[1]])/2<=w[g.owner]
        else:
            assert g.main[0]>0 # no independent source blocker
        for other in c.generators:
            if other.release==g.main:
                assert g.owner is not None and other.owner is not None
                assert other.owner>g.owner
    # Blocker ownership synchronization.
    for i,e,kind in c.blocker_data:
        g=mains[e]
        if kind=="upper":
            assert all(grade_layer(c.upper_states,l)==grade_layer(c.upper_states,i) for l in g.children)
            assert all(l>q for l in g.children)
        else:
            assert i>=2 and e[1]==b and c.parents[i-1][1]>b
            assert (w[e[0]]+w[e[1]])/2>=w[i]
            first=range(lower(w,q)+1,q+1)
            assert all(l in first for l in g.children)
            assert e[1]>q
    # Exact stresses. Symbolic z_i can be tested one unit coordinate at a time
    # when a graded PD stress is needed; active edges are checked structurally.
    repairs=0; switch_merges=0
    for s,(J,Q) in enumerate(zip(c.states,c.states[1:]),1):
        C=set(range(Q+1,J+1))
        if s==1:
            z=[F(0)]*(k+1); z[k]=F(1); t={}
            assert all(pair(g,z,t)==0 for g in c.generators)
            continue
        final_repair=(s>c.cut and c.leading==(0,J+1))
        if s<=c.cut or final_repair:
            if final_repair: repairs+=1; assert Q==0
            for cidx in C:
                z=[F(0)]*(k+1); z[cidx]=F(1)
                t={g.main:-sum(z[i] for i in g.children) for g in c.generators}
                assert all(pair(g,z,t)==0 for g in c.generators), (c,s,"graded pairing")
                assert c.leading is None or t.get(c.leading,0)==0
            # Full symbolic support / convex-square PD criterion.
            for g in c.generators:
                included=g.children & C
                a,z=g.main
                if included and z<=J:
                    assert a in C and z in C, (c,s,g,"active edge escapes block")
                    for i in included:
                        assert (w[a]**2+w[z]**2)/2>w[i]**2
        else:
            z=[F(i in C) for i in range(k+1)]
            release=(0,J+1); t={release:F(-1)}
            # Correct the first-tail blockers on their private, off-face main edges.
            for g in c.generators:
                residual=pair(g,z,t)
                if residual:
                    assert g.main[0]>0 and g.main[1]>J, (c,s,g,residual,"not free off-face")
                    t[g.main]=t.get(g.main,F(0))-residual
            assert all(pair(g,z,t)==0 for g in c.generators), (c,s,"diagonal pairing")
            assert all(z0>J for (a,z0),val in t.items() if val)
            assert c.leading is None or t.get(c.leading,0)==0
        # Check the minimal-positive-diagonal obstruction for every survivor.
        for i in range(1,Q+1):
            if s<=c.cut:
                if i>q:
                    e=next(e for child,e,kind in c.blocker_data if child==i)
                    g=mains[e]
                    assert g.release is None and e[1]<=J and e[0]<i
                    assert all(l<=J for l in g.children)
                elif c.parents[i-1][1]>b:
                    e=(i-1,b); g=mains[e]
                    assert e[1]<=J and e[0]<i and all(l<=J for l in g.children)
                    assert g.release is None or (g.release[0]==0 and g.release[1]<=J)
                else:
                    g=mains[c.parents[i-1]]
                    assert g.main[1]<=J and g.main[0]<i and all(l<=J for l in g.children)
                    assert g.release is None or (g.release[0]==0 and g.release[1]<=J)
            else:
                g=mains[c.parents[i-1]]
                assert g.children=={i}
                assert 2*w[i]<w[J+1]
                assert g.main[1]<=J and g.main[0]<i
                assert g.release is None or g.release[1]<=J
    return {"cuts":1,"stresses":len(c.states)-1,"repairs":repairs,
            "switch_blockers":sum(kind=="switch" for _,_,kind in c.blocker_data),
            "switch_merges":sum(kind=="switch" and mains[e].owner is not None for _,e,kind in c.blocker_data)}


def check_policy(P: Sequence[Edge]) -> dict[str,int]:
    w=harmonic_weights(P); k=len(w)-1
    us=[k]+tail(w,k-1,True)
    L=1+len(tail(w,k-1))-1; U=len(us)-1
    depths=[]; stats={"policies":1,"cuts":0,"stresses":0,"repairs":0,"switch_blockers":0,"switch_merges":0}
    for cut in range(1,U+1):
        depths.append(cut+len(tail(w,us[cut]))-1)
        for v in range(1,k+1):
            if w[v]/2<=w[1]:
                for key,value in audit(construct(P,cut,v)).items(): stats[key]+=value
    assert set(depths)==set(range(L,U+1))
    assert all(b-a in (0,1) for a,b in zip(depths,depths[1:]))
    assert w[1]/2>=F(1,2**L)
    return stats


def main() -> None:
    examples={
      "no_internal_grade_boundary": (),
      "one_internal_grade": ((0,2),),
      "quarter_chain": ((0,2),(0,3)),
      "leading_release_collision": ((0,3),(1,3),(2,4)),
      "milestone_107_increase": ((0,2),(0,6),(2,4),(3,5),(4,6)),
      "milestone_107_decrease": ((0,2),(1,4),(2,5),(3,5),(4,6)),
      "milestone_116_collision": ((0,3),(0,5),(1,4),(0,6),(1,6)),
      "milestone_125_forbidden_schedule": ((0,3),(1,4),(0,6),(3,5),(2,6)),
      "switch_merge_and_leading_collision": ((0,4),(0,6),(1,5),(2,5),(4,6)),
    }
    total={}
    for name,P in examples.items():
        stats=check_policy(P)
        for key,value in stats.items(): total[key]=total.get(key,0)+value
        print(name, "weights=", [str(v) for v in harmonic_weights(P)], "PASS",stats)
    # Infinite symbolic families specialized only to sanity-check the implementation.
    for k in (4,8,16,32):
        P=tuple((0,i+1) for i in range(1,k))
        stats=check_policy(P)
        for key,value in stats.items(): total[key]=total.get(key,0)+value
        print("dyadic_family",k,"PASS",stats)
    print("TOTAL",total)

if __name__=="__main__": main()
