#!/usr/bin/env python3
"""Exact Fraction audit of Milestone 114: at the ORIGINAL nullity, an
independent source-to-v leading edge can collide with an off-face release
edge ONLY at the FINAL exposing stage. Omitting that last release edge
and using an explicit harmonic-anchor positive final stress resolves
all rank-one cases. No numerical semidefinite solver is needed.

Checks 2,286 strict harmonic graphs with 1..5 internal vertices and all
5,269 admissible alpha=w_v/2<w_1; 933 exhibit the collision.
"""
from fractions import Fraction as F
from itertools import product

def choices(h):
    return [[(a,b) for a in range(i) for b in range(i+1,h+2)]
            for i in range(1,h+1)]

def harmonic(P):
    h=len(P);A=[]
    for i,(a,b) in enumerate(P,1):
        row=[F(0)]*(h+1);row[i-1]=2
        for v in (a,b):
            if v==h+1:row[-1]+=1
            elif v:row[v-1]-=1
        A.append(row)
    for j in range(h):
        p=next(i for i in range(j,h) if A[i][j])
        A[p],A[j]=A[j],A[p]
        c=A[j][j];A[j]=[x/c for x in A[j]]
        for i in range(h):
            if i!=j:
                c=A[i][j]
                A[i]=[x-c*y for x,y in zip(A[i],A[j])]
    return (F(0),)+tuple(r[-1] for r in A)+(F(1),)

def fastest(w):
    k=len(w)-1;j=k-1;S=[k,j]
    while j:
        j=sum(1 for i in range(1,j) if 2*w[i]<w[j+1])
        S.append(j)
    return S

def audit(P,w,v):
    h=len(P);k=h+1;S=fastest(w);d=len(S)-1
    assert w[v]/2<w[1]
    layers=[set(range(S[t]+1,S[t-1]+1)) for t in range(1,d+1)]
    release={t:(0,S[t-1]+1) for t in range(2,d+1)}
    colliding=[t for t,e in release.items() if e==(0,v)]
    assert len(colliding)<=1
    if colliding:
        assert colliding==[d]
        assert S[d-1]==v-1
    gens={}
    for i in range(1,k):
        t=next(t for t,C in enumerate(layers,1) if i in C)
        edges=[P[i-1]]
        if release[t]!=P[i-1] and not (colliding and t==d):
            edges.append(release[t])
        gens[i]=tuple(edges)
        assert all(w[a]+w[b]<=2*w[i] for a,b in edges)
    if colliding:
        assert all((0,v) not in E for E in gens.values())

    def dual_pairing(diag,off,i):
        return diag.get(i,F(0))-diag.get(0,F(0))+2*sum(
            (off.get(e,F(0)) for e in gens[i]),F(0))

    for t in range(1,d+1):
        C=layers[t-1];j=S[t-1]
        if colliding and t==d:
            # The actual final stress may use z_i=B^(D*w_i)^2 for large
            # integer B, which makes the compressed stress PD by
            # normalizing the active harmonic-anchor offdiagonals.
            # Distinct symbolic positive diagonal values 2^i suffice
            # for exact ORTHOGONALITY tests here.
            diag={i:F(2)**i for i in C};off={}
            for i in C:
                e=P[i-1]
                assert e not in off
                off[e]=-diag[i]/2
                if e[1]<=j:
                    assert e[0]>=1 and e[0] in C and e[1] in C
                    assert 2*w[i]==w[e[0]]+w[e[1]]
            assert (0,v) not in off
        else:
            diag={i:F(1) for i in C}
            off={} if t==1 else {release[t]:F(-1,2)}
        for i in range(1,k):
            assert dual_pairing(diag,off,i)==0,(P,w,v,S,t,i)
        assert (0,v) not in off
    return bool(colliding)

def main():
    expected={1:1,2:3,3:18,4:165,5:2099}
    total=0;collisions=0;graphs=0
    for h in range(1,6):
        local=0;cnt=0
        for P in product(*choices(h)):
            w=harmonic(P)
            if not all(a<b for a,b in zip(w,w[1:])):continue
            cnt+=1;graphs+=1
            for v in range(1,h+2):
                if w[v]/2>=w[1]:continue
                total+=1
                repaired=audit(P,w,v)
                local+=repaired;collisions+=repaired
        assert cnt==expected[h]
        print('PASS h=',h,'strict graphs=',cnt,'repaired collisions=',local)
    assert (graphs,total,collisions)==(2286,5269,933)
    print('PASS: 2,286 graphs, 5,269 halfweights, 933 rank-one collisions all repaired')

if __name__=='__main__': main()
