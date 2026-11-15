#!/usr/bin/env python3
"""Exact checks for rational conic optimization hiding and its prefix minimax law.

Standard library only. All construction, moment, spectral, and probability checks
use fractions or Q(sqrt(2)); no floating-point tolerance is used.
Run: python verify_minimax.py --max-depth 6 --output VERIFICATION_RESULTS.json
These finite checks support, and do not replace, the analytical proofs.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
from math import comb, isqrt
from pathlib import Path
import json

H, A, LAM = F(1, 8), F(1, 4), F(1, 64)
ETA = LAM * H * H
LEFT = (F(-1), F(-3, 4), F(-1, 2))
RES = {-1: (2665, 2942, 2457), 1: (2121, 4286, 1657)}
MOM_MINUS = (F(1, 2), F(-3, 8), F(29, 96))
MOM_PLUS = (F(1, 2), F(3, 8), F(29, 96))

@dataclass(frozen=True)
class Q2:
    a: F
    b: F = F(0)
    def __add__(self, other: object) -> 'Q2':
        o = other if isinstance(other, Q2) else Q2(F(other))
        return Q2(self.a + o.a, self.b + o.b)
    __radd__ = __add__
    def __neg__(self) -> 'Q2': return Q2(-self.a, -self.b)
    def __sub__(self, other: object) -> 'Q2': return self + (-lift(other))
    def __rsub__(self, other: object) -> 'Q2': return lift(other) - self
    def __mul__(self, other: object) -> 'Q2':
        o = lift(other)
        return Q2(self.a * o.a + 2*self.b*o.b, self.a*o.b+self.b*o.a)
    __rmul__ = __mul__
    def sign(self) -> int:
        a, b = self.a, self.b
        if not b: return (a > 0) - (a < 0)
        if not a: return (b > 0) - (b < 0)
        if a > 0 and b > 0: return 1
        if a < 0 and b < 0: return -1
        d = a*a - 2*b*b
        return ((d > 0)-(d < 0)) * (1 if a > 0 else -1)


def lift(x: object) -> Q2:
    return x if isinstance(x, Q2) else Q2(F(x))


def words(n: int):
    return product((-1, 1), repeat=n)


@lru_cache(None)
def four_squares(n: int) -> tuple[int, int, int, int]:
    if n < 0: raise ValueError('negative input')
    pairs = {}
    for a in range(isqrt(n)+1):
        for b in range(isqrt(n-a*a)+1):
            pairs.setdefault(a*a+b*b, (a,b))
    for v, ab in pairs.items():
        if n-v in pairs: return (*ab, *pairs[n-v])
    raise AssertionError('four-square representation not found')


# Atom format: (threshold, weight, side), side -1 for (threshold-x)_+^2.
@lru_cache(None)
def atoms(word: tuple[int, ...]) -> tuple[tuple[F,F,int], ...]:
    offset, scale, mass = F(0), F(1), F(1)
    out = []
    for bit in word:
        for side in (-1, 1):
            nums = RES[bit if side == -1 else -bit]
            nodes = LEFT if side == -1 else tuple(-u for u in LEFT)
            for node, num in zip(nodes, nums):
                out.append((offset+scale*node, mass*F(num,16384), side))
        offset += scale*A*bit
        scale *= H
        mass *= LAM
    for side in (-1,1):
        for node in LEFT if side == -1 else tuple(-u for u in LEFT):
            out.append((offset+scale*node, mass*F(1,6), side))
    return tuple(out)


def center(word: tuple[int, ...]) -> F:
    return sum((A*bit*H**j for j,bit in enumerate(word)),F(0))


def oracle(word: tuple[int, ...], x: F | Q2) -> tuple[Q2, Q2]:
    x = lift(x)
    val, grad = Q2(F(0)), Q2(F(0))
    for t,w,side in atoms(word):
        diff = side*(x-t)
        if diff.sign() > 0:
            val += (w/2)*diff*diff
            grad += (w*side)*diff
    return val, grad


def exterior(x: F | Q2, side: int) -> tuple[Q2,Q2]:
    x = lift(x)
    return x*x*F(1,4)-side*x*F(3,8)+F(29,192), x*F(1,2)-side*F(3,8)


def revealed_prefix(word: tuple[int, ...], x: F) -> tuple[int, ...]:
    if abs(x)>1: return ()
    for j in range(1,len(word)+1):
        prefix=word[:j]
        if abs(x-center(prefix))>H**j: return prefix
    return word


def epsilon(n: int) -> F: return F(5,384)*ETA**n


@lru_cache(None)
def game_success(n: int,t: int) -> F:
    if n==0: return F(1)
    if t==0: return F(1,2**n)
    return sum((F(1,2**j)*game_success(n-j,t-1) for j in range(1,n)),F(0))+F(2,2**n)


def binomial_success(n: int,t: int) -> F:
    return F(sum(comb(n,j) for j in range(min(n,t)+1)),2**n)


def posterior_risk(n: int,t: int) -> F:
    if n==0 or t>=n: return F(0)
    v0=F(77,192)*ETA
    if t==0: return v0
    return v0*sum((F(comb(k-1,t-1),2**k)*ETA**k for k in range(t,n)),F(0))


@lru_cache(None)
def game_risk(n: int,t: int) -> F:
    if n==0: return F(0)
    if t==0: return F(77,192)*ETA
    return sum((F(1,2**j)*ETA**j*game_risk(n-j,t-1) for j in range(1,n)),F(0))


def pencil_factors(word: tuple[int,...]) -> list[tuple[F,F]]:
    # Each item is the constant and x coefficient of a scalar matrix block.
    out=[]
    offset, scale=F(0), F(1)
    for j,bit in enumerate(word):
        for side in (-1,1):
            nums=RES[bit if side==-1 else -bit]
            nodes=LEFT if side==-1 else tuple(-u for u in LEFT)
            for node,num in zip(nodes,nums):
                t=offset+scale*node
                for integer in four_squares(num):
                    b=F(integer,128*8**j)
                    out.append((side*b*t,-side*b))
        offset += scale*A*bit
        scale *= H
    for side in (-1,1):
        for node in LEFT if side==-1 else tuple(-u for u in LEFT):
            t=offset+scale*node
            for integer in (1,1,2,0):
                b=F(integer,6*8**len(word))
                out.append((side*b*t,-side*b))
    return out


def run(max_depth:int) -> dict:
    counts={}
    def check(name:str,condition:bool):
        if not condition: raise AssertionError(name)
        counts[name]=counts.get(name,0)+1
    for n in range(max_depth+1):
        allw=list(words(n))
        for word in allw:
            ats=atoms(word)
            for side,moms in [(-1,MOM_MINUS),(1,MOM_PLUS)]:
                for k,target in enumerate(moms):
                    check('moments',sum((w*t**k for t,w,sgn in ats if sgn==side),F(0))==target)
            check('positive_weights',all(w>0 for _,w,_ in ats))
            check('bounded_thresholds',all(abs(t)<=1 for t,_,_ in ats))
            cw=center(word)
            check('zero_center',oracle(word,cw)==(Q2(F(0)),Q2(F(0))))
            check('zero_interval_left',oracle(word,cw-H**n/2)[0]==Q2(F(0)))
            check('zero_interval_right',oracle(word,cw+H**n/2)[0]==Q2(F(0)))
            if n:
                check('constant_value_at_origin',oracle(word,F(0))[0]==Q2(F(77,192)*ETA))
            for x in (F(-2)**1001,F(-3),F(-1),F(1),F(3),F(2)**1000):
                check('exact_exterior_value_gradient',oracle(word,x)==exterior(x,1 if x>0 else -1))
            for x in (cw-H**n,cw+H**n):
                check('leaf_boundary_barrier',oracle(word,x)[0].a>=2*epsilon(n))
            # Construct the entire rational affine pencil and verify its metric.
            factors=pencil_factors(word)
            check('matrix_order',len(factors)+2==24*(n+1)+2)
            check('isometry',sum((b*b for _,b in factors),F(0))==1)
            check('offset_orthogonality',sum((c*b for c,b in factors),F(0))==0)
            check('offset_norm',2+sum((c*c for c,_ in factors),F(0))==F(125,48))
            for x in (F(-2),F(0),cw,F(2)):
                direct=sum((min(c+b*x,F(0))**2/2 for c,b in factors),F(0))
                check('natural_psd_scalar_value',oracle(word,x)[0]==Q2(direct))
        # Exact exterior/descendant indistinguishability on a diverse rational grid.
        for x in tuple(F(j,16) for j in range(-20,21))+(F(2)**200,F(-2)**201):
            grouped={}
            for word in allw:
                key=revealed_prefix(word,x)
                reply=oracle(word,x)
                if key in grouped: check('prefix_locality',reply==grouped[key])
                else: grouped[key]=reply
        # Finite number-field verification of every full-word probe, manageable n<=5.
        if n<=5:
            for guess in allw:
                q=Q2(center(guess),H**n/F(16))
                for word in allw:
                    val,g=oracle(word,q)
                    if word==guess:
                        check('algebraic_exact_match',g==Q2(F(0)) and val==Q2(F(0)))
                    else:
                        j=next(j for j,(u,v) in enumerate(zip(guess,word),1) if u!=v)
                        check('algebraic_first_mismatch',g.b/q.b==LAM**j/2)
        for t in range(n+2):
            check('binomial_minimax_identity',game_success(n,t)==binomial_success(n,t))
            check('expected_risk_identity',game_risk(n,t)==posterior_risk(n,t))
    # Exact inverse-tail relation, eigenvalue and derivative identities.
    for r in (F(1,2),F(1,4),F(1,8),F(1,100)):
        z=1/r-r
        check('tail_spectrum',(-r)**2-z*(-r)-1==0 and (1/r)**2-z/r-1==0)
        s=r*r/2
        check('radius_upper',F(4,49)+z*z <=1/s)
        check('radius_lower_squared',z*z >=1/(4*s))
    # Some horizons give the requested 2/3 failure constant, at EXPONENTIAL accuracy.
    for t in range(50):
        n=4*(t+1)
        check('fixed_prior_failure_two_thirds',binomial_success(n,t)<F(1,3))
    return {'status':'PASS','max_depth':max_depth,'exact_checks':sum(counts.values()),
            'counts':counts,'lambda':str(LAM),'spatial_scale':str(H),'energy_scale':str(ETA),
            'epsilon_n':'(5/384)*4096^(-n)',
            'scope':'Finite exact checks, not an independent proof review. The full dimension-uniform power-law lower bound remains unproved.',
            'four_square_templates':{str(k):four_squares(k) for nums in RES.values() for k in nums},
            'success_examples':[{'n':n,'T':t,'success':str(binomial_success(n,t))} for n in (4,8,16) for t in (0,n//4,n//2,n)]}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--max-depth',type=int,default=6)
    p.add_argument('--output',type=Path,default=Path('VERIFICATION_RESULTS.json'))
    args=p.parse_args()
    if not 0<=args.max_depth<=9: p.error('max-depth must be between 0 and 9')
    report=run(args.max_depth)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'exact_checks':report['exact_checks'],'output':str(args.output)},indent=2))

if __name__=='__main__': main()
