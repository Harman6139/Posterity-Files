"""Exact contraction and leading-forcing bounds for the invariant tube.
Keep this file beside exact_series.py and run with Python 3 / SymPy.
"""
from fractions import Fraction as Q
from math import isqrt
import sympy as sp
from exact_series import calculate,vars,varnames,kappa
leads=calculate()
x,y,B,h,ec,eg,echi,eac,eag,eq,ej,ad,bd,fa,efs=vars
q=sp.Rational(999,1000)
Ms=sp.Matrix([[leads[o].diff(i).as_expr() for i in [ec,eg]] for o in ['ec','eg']])
Ma=sp.Matrix([[leads[o].diff(i).as_expr() for i in [eac,eag,eq]] for o in ['eac','eag','eq']])
D=10**15; lo=sp.Rational(isqrt(3*D*D),D); hi=lo+sp.Rational(1,D)
assert lo**2<3<hi**2

def lower(e):
    e=sp.expand(e); aa=e.coeff(sp.sqrt(3),0); bb=e.coeff(sp.sqrt(3),1)
    assert sp.expand(e-aa-bb*sp.sqrt(3))==0
    return aa+bb*(lo if bb>=0 else hi)

for name,M,W in [('Ms',Ms,sp.diag(1,2)),('Ma',Ma,sp.diag(2,4,1))]:
    defect=sp.simplify(q*q*W-M.T*W*M)
    for j in range(1,M.rows+1):
        assert lower(sp.simplify(defect[:j,:j].det()))>0
    print(name,': exact weighted operator norm < 999/1000')

weights=[Q(1),Q(1),Q(1),Q(10**5),Q(2000),Q(2000),Q(10**6),
         Q(10**11),Q(10**11),Q(10**11),Q(10**13),
         Q(1000),Q(1000),Q(1000),Q(10**6)]

def coeffabs(a):
    a=[Q(int(z.numerator),int(z.denominator)) for z in a.to_list()]
    if len(a)==1: return abs(a[0])
    return max(abs(a[1]+a[0]*Q(int(lo.p),int(lo.q))),
               abs(a[1]+a[0]*Q(int(hi.p),int(hi.q))))

def bound(p):
    out=Q(0)
    for mon,a in p.items():
        z=coeffabs(a)
        for w,n in zip(weights,mon):
            if n: z*=w**n
        out+=z
    return out

out={}
for key in ['ad','bd','fa']:
    out[key]=bound(leads[key]); assert out[key]<999
sym_force=[leads[k]-leads[k].diff(ec)*ec-leads[k].diff(eg)*eg for k in ['ec','eg']]
out['sym_weighted']=bound(sym_force[0])+2*bound(sym_force[1])
assert out['sym_weighted']<Q(3,2)
out['h_force']=bound(leads['h']+kappa*h); assert out['h_force']<10**5-1000
out['chi_reset']=bound(leads['echi']); assert out['chi_reset']<10**6-1000
asym_force=[leads[k]-sum(leads[k].diff(z)*z for z in [eac,eag,eq]) for k in ['eac','eag','eq']]
out['asym_weighted']=2*bound(asym_force[0])+2*bound(asym_force[1])+bound(asym_force[2])
assert out['asym_weighted']<10**8-1000
out['j_force']=bound(leads['ej']+kappa*ej); assert out['j_force']<10**13-1000
out['fs_reset']=bound(leads['efs']); assert out['fs_reset']<10**6-1000
for key,val in out.items(): print(key,': rational upper bound',val)
print('All leading inward margins are positive; smallest fast margin >1/2.')
