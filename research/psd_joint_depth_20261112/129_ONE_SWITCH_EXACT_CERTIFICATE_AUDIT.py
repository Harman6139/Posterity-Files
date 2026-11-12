#!/usr/bin/env python3
"""Exact, targeted audit of the one-switch PSD construction.

This checks a uniform construction, not an enumerative proof search.  All
arithmetic is rational.  Stress orthogonality is checked as a polynomial
identity in formal positive diagonal entries.  Positive definiteness is
certified by strict weighted diagonal-dominance inequalities.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction as F
from typing import Dict, Tuple, List, Optional
import json
import argparse
from pathlib import Path
from math import lcm

Edge = Tuple[int,int]
Matrix = Dict[Edge,F] # one copy of each symmetric entry
Form = Dict[int,F]   # linear form in formal z_i; -1 means constant 1
Stress = Dict[Edge,Form]

def add_form(a:Form,b:Form,c:F=F(1))->Form:
    out=dict(a)
    for i,x in b.items():
        out[i]=out.get(i,F(0))+c*x
        if not out[i]: del out[i]
    return out

def scale(a:Form,c:F)->Form: return {i:c*x for i,x in a.items() if c*x}

def add_entry(M:Matrix,e:Edge,x:F):
    e=tuple(sorted(e)); M[e]=M.get(e,F(0))+x
    if not M[e]: del M[e]

def set_stress(S:Stress,e:Edge,x:Form):
    e=tuple(sorted(e))
    if e in S: assert S[e]==x, ('stress conflict',e,S[e],x)
    S[e]=dict(x)

def pairing(H:Matrix,S:Stress)->Form:
    ans={}
    for (a,b),x in H.items():
        ans=add_form(ans,S.get((a,b),{}),x*(1 if a==b else 2))
    return ans

@dataclass
class Construction:
    w:Tuple[F,...]
    P:Tuple[Edge,...] # indices 0..k-2 correspond to children 1..k-1
    s:int
    v:Optional[int]=None
    def __post_init__(self):
        self.k=len(self.w)-1; k=self.k
        assert k>=2 and self.w[0]==0 and self.w[-1]==1
        assert all(self.w[i]<self.w[i+1] for i in range(k))
        assert len(self.P)==k-1 and len(set(self.P))==k-1
        for i,(a,b) in enumerate(self.P,1):
            assert 0<=a<i<b<=k and self.w[a]+self.w[b]==2*self.w[i]
        self.ell=lambda j: sum(2*self.w[i]<self.w[j+1] for i in range(1,j))
        self.u=lambda j: next(i for i in range(1,j+1) if 2*self.w[i]>self.w[j]+self.w[i-1])-1
        self.up=[k,k-1]
        while self.up[-1]: self.up.append(self.u(self.up[-1]))
        assert 1<=self.s<len(self.up)-1
        self.q=self.up[self.s]; self.J=self.up[self.s-1]
        self.path=self.up[:self.s+1]
        while self.path[-1]: self.path.append(self.ell(self.path[-1]))
        self.depth=len(self.path)-1
        self.release={}
        for t in range(self.s+1,len(self.path)):
            j,q=self.path[t-1:t+1]
            for i in range(q+1,j+1): self.release[i]=(0,j+1)
        self.alpha=self.w[1] if self.v is None else self.w[self.v]/2
        if self.v is not None: assert self.alpha<self.w[1]
        self.Gedge=None if self.v is None else (0,self.v)
        self.repair=self.Gedge is not None and self.Gedge in self.release.values()
        if self.repair:
            assert self.Gedge==(0,self.path[-2]+1)
            for i in range(1,self.path[-2]+1): self.release.pop(i,None)
        self.B={}
        for i in range(2,k):
            if i<=self.q: b=self.J
            else: b=next(b for b in range(i+1,k+1) if self.w[i-1]+self.w[b]>=2*self.w[i])
            self.B[i]=(i-1,b)
            assert i-1<i<b and self.w[i-1]+self.w[b]>=2*self.w[i]
        self.extra={}; self.new={}
        owner={p:i for i,p in enumerate(self.P,1)}
        for i,b in self.B.items():
            if b in owner:
                j=owner[b]
                if i!=j:
                    assert j>i and j not in self.extra
                    self.extra[j]=i
                    if i<=self.q:
                        assert self.ell(self.q)<j<=self.q
                        assert b[1]==self.J>self.q
                    else:
                        assert j>self.q
                        layer=lambda x:next(t for t in range(1,len(self.up)) if self.up[t]<x<=self.up[t-1])
                        assert layer(i)==layer(j)
            else: self.new[i]=b
        self.lam=F(1,100*(k+1)**2)
        self.H={}
        for i,p in enumerate(self.P,1):
            M={(i,i):F(1),(0,0):F(-1),p:self.lam}
            if i in self.extra:
                c=self.extra[i];add_entry(M,(c,c),F(1));add_entry(M,(0,0),F(-1))
            r=self.release.get(i)
            if r is not None and r!=p:add_entry(M,r,self.lam)
            self.H[i]=M
        self.N={i:{(i,i):F(1),(0,0):F(-1),b:self.lam} for i,b in self.new.items()}
        self.generators=[('H'+str(i),self.H[i],self.w[i]) for i in self.H]
        self.generators += [('J'+str(i),self.N[i],sum(self.w[t] for t in self.new[i])/2) for i in self.N]
        if self.Gedge is not None:
            self.generators.append(('G',{self.Gedge:self.lam},self.alpha))
        self.audit_leading_forms()
        self.audit_stresses()

    def audit_leading_forms(self):
        """Check distinct leading pivots and an explicit strictly PD separator."""
        B=[];piv=[];W={}
        for i in range(self.k+1):W[(i,i)]={i:F(1)}
        for i,p in enumerate(self.P,1):set_stress(W,p,{i:-1/(2*self.lam)})
        for i,b in self.new.items():
            eta=sum(self.w[t] for t in b)/2
            set_stress(W,b,{i:-1/(2*self.lam)} if eta==self.w[i] else {})
        for name,H,deg in self.generators:
            assert all((self.w[a]+self.w[b])/2<=deg for a,b in H)
            lead={e:x for e,x in H.items() if sum(self.w[t] for t in e)/2==deg}
            p=self.P[int(name[1:])-1] if name[0]=='H' else self.new[int(name[1:])] if name[0]=='J' else self.Gedge
            B.append(lead);piv.append(p)
            assert not pairing(lead,W),(name,lead,pairing(lead,W))
        for j,p in enumerate(piv):
            assert B[j].get(p,0)!=0
            assert all(p not in BB for t,BB in enumerate(B) if t!=j),('nonunique initial pivot',j,p,B)
        # Each nonzero W off-diagonal is asymptotically negligible versus its diagonal.
        for (a,b),form in W.items():
            if a!=b:
                for i,x in form.items():
                    assert (self.w[a]**2+self.w[b]**2)/2>self.w[i]**2
        self.leading_count=len(B)

    def audit_stresses(self):
        self.stress_checks=[]
        self.stresses=[]
        for t in range(1,len(self.path)):
            j,q=self.path[t-1:t+1];C=set(range(q+1,j+1))
            S={}
            ordinary=(t>self.s and not (self.repair and t==len(self.path)-1))
            z={i:({-1:F(1)} if ordinary else {i:F(1)}) if i in C else {} for i in range(self.k+1)}
            for i in range(self.k+1):set_stress(S,(i,i),z[i])
            if t==1:
                assert C=={self.k}
            elif t<=self.s:
                # Early upper-peeling stresses: cancel sums of child diagonals on unique edges.
                for i,p in enumerate(self.P,1):
                    zsum=add_form(z[i],z.get(self.extra.get(i,-2),{}))
                    set_stress(S,p,scale(zsum,-1/(2*self.lam)))
                for i,b in self.new.items():set_stress(S,b,scale(z[i],-1/(2*self.lam)))
                for r in self.release.values():set_stress(S,r,{})
            elif ordinary:
                f=(0,j+1)
                for r in self.release.values():set_stress(S,r,{-1:-1/(2*self.lam)} if r==f else {})
                for i,p in enumerate(self.P,1):
                    if p not in self.release.values():
                        set_stress(S,p,scale(z.get(self.extra.get(i,-2),{}),-1/(2*self.lam)))
                for i,b in self.new.items():set_stress(S,b,scale(z[i],-1/(2*self.lam)))
            else:
                assert self.repair and C==set(range(1,j+1))
                for i,p in enumerate(self.P,1):
                    zsum=add_form(z[i],z.get(self.extra.get(i,-2),{}))
                    set_stress(S,p,scale(zsum,-1/(2*self.lam)))
                for i,b in self.new.items():set_stress(S,b,scale(z[i],-1/(2*self.lam)))
                for r in self.release.values():set_stress(S,r,{})
            if self.Gedge is not None:set_stress(S,self.Gedge,{})
            for name,H,deg in self.generators:
                assert not pairing(H,S),('orthogonality',t,j,q,name,pairing(H,S),self.w,self.path,self.extra,self.release)
            for (a,b),form in S.items():
                if a==b or not form or max(a,b)>j:continue
                assert a in C and b in C,('wrong compressed range',t,(a,b),C)
                assert not ordinary,('ordinary lower compression not diagonal',t,(a,b))
                for i,coeff in form.items():
                    assert i in C and (self.w[a]**2+self.w[b]**2)/2>self.w[i]**2
            # For every delayed early child, certify an active lower-endpoint blocker.
            if t<=self.s and t>1:
                for i in range(1,q+1):
                    b=self.P[0] if i==1 else self.B[i]
                    assert max(b)<=j and min(b)<i
                    # Positive diagonal children of the blocking generator remain on face.
                    owner=next((a for a,p in enumerate(self.P,1) if p==b),None)
                    if owner is not None:
                        assert owner<=j and self.extra.get(owner,owner)<=j
                        r=self.release.get(owner)
                        assert r is None or r[1]<=j
            # Forced lower survivors: H_i has no off-face entries and only its own diagonal
            # after rows < i vanish.
            if t>self.s:
                assert q==self.ell(j)
                for i in range(1,q+1):
                    assert all(max(a,b)<=j for a,b in self.H[i])
                    assert all((a,b)==(i,i) or min(a,b)<i for a,b in self.H[i])
            self.stress_checks.append({'step':t,'face':j,'survivor':q,'diagonal_compression':ordinary or t==1})
            self.stresses.append(S)


def choose_policy(w):
    k=len(w)-1
    return tuple(next((a,b) for a in range(i) for b in range(i+1,k+1) if w[a]+w[b]==2*w[i]) for i in range(1,k))

def audit_family(w,P=None,name=''):
    w=tuple(map(F,w));P=choose_policy(w) if P is None else tuple(P)
    seed=Construction(w,P,1)
    D=len(seed.up)-1
    lengths=[];records=[]
    for s in range(1,D):
        c=Construction(w,P,s);lengths.append(c.depth)
        leading=[None]+[v for v in range(1,c.k+1) if w[v]/2<w[1]]
        for v in leading:
            c=Construction(w,P,s,v)
            records.append({'s':s,'depth':c.depth,'alpha':str(c.alpha),'path':c.path,'extra_children':c.extra,'leading_collision_repair':c.repair,'generator_count':len(c.generators)})
    assert lengths[0]==len(seed.path)-1 and lengths[-1]==D
    assert all(b-a in (0,1) for a,b in zip(lengths,lengths[1:]))
    assert set(lengths)==set(range(lengths[0],D+1))
    return {'family':name,'weights':list(map(str,w)),'upper_path':seed.up,'one_switch_depths':lengths,'checks':len(records),'records':records}


def run_regressions():
    reports=[]
    reports.append(audit_family([0,F(1,4),F(3,7),F(1,2),F(17,28),F(5,7),1],
                   [(0,3),(1,4),(0,6),(3,5),(2,6)],'Milestone 125 forbidden-schedule regression'))
    reports.append(audit_family([0,F(3,32),F(3,16),F(3,8),F(1,2),F(9,16),F(3,4),1],
                   [(0,2),(0,3),(0,6),(0,7),(3,6),(4,7)],'Milestone 123 early collision regression'))
    # Nonadjacent tight anchors deliberately create cross-layer merged children.
    for k in [6,8,12]:
        pp=[(0,2*i) if 2*i<=k else (2*i-k,k) for i in range(1,k)]
        reports.append(audit_family([F(i,k) for i in range(k+1)],pp,f'Uniform nonadjacent anchors k={k}'))
    # Closed-form families, not a search over graph assignments.
    for k in [2,3,4,6,8,12,20]:
        reports.append(audit_family([F(i,k) for i in range(k+1)],[(i-1,i+1) for i in range(1,k)],f'Uniform harmonic chain k={k}'))
    for k in [3,6,10]:
        reports.append(audit_family([F(0)]+[F(1,2**(k-i)) for i in range(1,k+1)],[(0,i+1) for i in range(1,k)],f'Dyadic harmonic chain k={k}'))
    for d,M in [(4,2),(6,3)]:
        A=2**M-1; beta=F(A,2*A+d-2); delta=F(1,2*A+d-2); T0=2*beta+delta
        k=M+d-1
        ww=[F(0),beta]+[T0-(T0-beta)/2**(i-1) for i in range(2,M+2)]
        ww += [2*beta+(i-M-1)*delta for i in range(M+2,k+1)]
        pp=[(0,M+1)]+[(i-1,M+2) for i in range(2,M+2)]
        pp += [(i-1,i+1) for i in range(M+2,k)]
        rr=audit_family(ww,pp,f'Closed-form depth helper d={d}, M={M}')
        assert len(rr['upper_path'])-1==d
        reports.append(rr)
    report={'status':'PASS','method':'Exact identities and strict rational positivity inequalities; no exhaustive graph search',
            'family_count':len(reports),'construction_checks':sum(r['checks'] for r in reports),'families':reports}
    return report


def construct_for_depth(weights, parents, degree, alpha=None):
    """Construct a certified kernel from a strict harmonic certificate.

    weights: exact rational strings, integers, or Fraction objects, including 0 and 1.
    parents: pairs (a_i,b_i) in order for internal children i=1,...,k-1.
    degree: requested integer between L(w) and U(w).
    alpha: optional admissible half-weight; defaults to w_1.
    """
    w=tuple(F(x) for x in weights)
    if len(w)<3:
        raise ValueError('This constructor takes k>=2; k=1 boundary matrices are given in the theorem.')
    P=tuple(tuple(map(int,p)) for p in parents)
    seed=Construction(w,P,1)
    a=[0]*seed.k
    for j in range(1,seed.k): a[j]=1+a[seed.ell(j)]
    switches=[s for s in range(1,len(seed.up)-1) if s+a[seed.up[s]]==degree]
    if not switches:
        raise ValueError(f'Degree {degree} is outside [{seed.depth},{len(seed.up)-1}].')
    alpha=w[1] if alpha is None else F(alpha)
    if alpha==w[1]: v=None
    else:
        values=[v for v in range(1,seed.k+1) if w[v]/2==alpha and alpha<w[1]]
        if not values: raise ValueError('Exponent is not an admissible leading half-weight.')
        v=values[0]
    return Construction(w,P,switches[0],v)


def export_construction(c):
    """Export upper-triangular rational matrix entries and formal exact stresses."""
    M=lcm(*(x.denominator for x in c.w))
    mi=[int(M*x) for x in c.w]
    T=1+int(4*(c.k+1)/c.lam)**2
    def entries(H):
        return [{'row':a,'column':b,'value':str(x)} for (a,b),x in sorted(H.items())]
    stress=[]
    for metadata,S in zip(c.stress_checks,c.stresses):
        terms=[]
        for (a,b),form in sorted(S.items()):
            if not form:continue
            terms.append({'row':a,'column':b,'terms':[
                {'coefficient':str(x),'factor':'1' if i==-1 else f'z_{i}'}
                for i,x in sorted(form.items())]})
        stress.append(dict(metadata,entries=terms))
    return {
        'status':'EXACT_CERTIFICATES_CHECKED',
        'matrix_order':c.k+1,'rank':1,'nullity':c.k,'minimal_degree':c.depth,
        'sharp_exponent':str(c.alpha),'lambda':str(c.lam),'weights':list(map(str,c.w)),
        'parents':c.P,'upper_path':c.up,'switch_after_steps':c.s,'exposing_path':c.path,
        'leading_release_repaired':c.repair,'extra_children':c.extra,
        'target':{'entries':[{'row':0,'column':0,'value':'1'}]},
        'measurement':'Frobenius orthogonal projection onto the complement of the kernel span',
        'matrix_entry_convention':'Upper triangle is listed; copy off-diagonal entries symmetrically.',
        'kernel_generators':[{'name':name,'weighted_degree':str(deg),'entries':entries(H)}
                             for name,H,deg in c.generators],
        'stress_diagonal_parameters':{'T':T,'M':M,'z_i_equals_T_power':[i*i for i in mi]},
        'ambient_exposing_stresses':stress,
        'polynomial_sharp_arc':{
            'parameter':'s','residual_power':2*M,
            'formula':'E_00 + sum_i s^(2*M*w_i) H_i + s^(2*M) E_kk, plus s^(2*M*alpha) G when present',
            'tight_generator_powers':{f'H{i}':2*mi[i] for i in range(1,c.k)},
            'leading_power':None if c.Gedge is None else int(2*M*c.alpha),
            'all_new_blocker_coefficients':'0'}
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--construct',type=Path,help='JSON containing weights, parents, degree, and optional alpha.')
    parser.add_argument('--output',type=Path,default=Path('one_switch_audit_results.json'))
    args=parser.parse_args()
    try:
        if args.construct:
            data=json.loads(args.construct.read_text())
            c=construct_for_depth(data['weights'],data['parents'],int(data['degree']),data.get('alpha'))
            report=export_construction(c)
            print(f"Certified nullity {c.k}, minimal degree {c.depth}, sharp exponent {c.alpha}.")
        else:
            report=run_regressions()
            print(json.dumps({k:v for k,v in report.items() if k!='families'},indent=2))
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(report,indent=2)+'\n')
        print(f'Wrote {args.output}')
    except (ValueError,KeyError,AssertionError,OSError) as exc:
        parser.exit(1,f'Certificate construction/audit failed: {exc}\n')

if __name__=='__main__': main()
