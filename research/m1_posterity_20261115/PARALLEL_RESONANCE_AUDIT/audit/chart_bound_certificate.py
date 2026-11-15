"""Rational majorants for the weighted Riccati analytic chart.
All assertions use exact rational arithmetic; decimal output is illustrative.
"""
from fractions import Fraction as Q
import sympy as sp
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
K=QQ.algebraic_field(sp.sqrt(3))
names='u,x,y,B,h,ec,eg,echi,eac,eag,eq,ej,ad,bd,fa,efs,X,Y,Z,W'
R,*v=ring(names,K)
u,x,y,B,h,ec,eg,echi,eac,eag,eq,ej,ad,bd,fa,efs,X,Y,Z,W=v

def c(z): return R.ground_new(K.from_sympy(sp.sympify(z)))
s=c(sp.sqrt(3)); b0=s/3; H0=s/4; ell=c(sp.Rational(3,4))
be=c(sp.Rational(1,2)); fs0=9*s/64
b=b0+u*B; H=H0+u*h; b2=b*b
cfN=2*H*H-H*b
Cn=cfN+H*H*b+u*ec*b2
Gn=H*H*b-cfN/2+u*eg*b2
caffN=2*(Cn-Gn)/3
Dn=2*caffN-Cn; Kn=-caffN-Gn
j=-(29*s*x*x+3*s*y*y-18*x*y)/12+u*ej
rr=3*x*x; cf_a=2*s*j+4*rr+s*x*y
Ca=cf_a+3*j/2+u*eac
Ga=2*rr-cf_a/2+3*j/2+u*eag
Qn=rr-12*j+u*eq
Raff=(3*Qn+8*Ca+16*Ga)/35
Cafa=2*(Ca-Ga+2*Raff)/3; Gafa=-Cafa/2+2*Raff
Da=2*Cafa-Ca; Ka=2*Gafa-Ga; D6=2*Raff-Qn
alpha=1-u**3*ad; Bp=-be-u*fs0-u*u*(efs+fa)
hn=-H-u*j; qn=-b+u**3*bd; chi=ell*y+u*echi
KK=Kn+u*Ka*b2; DD=Dn+u*Da*b2
# These are b^2 times the four weighted Riccati equations.
FN=[
KK+(qn-alpha)*b2*X-Bp*b2*Y-u*y*Z*b2-u*X*Y*hn*b2-u*u*(X*X*KK+X*x*Z*b2-Y*chi*Z*b2),
hn*b2+qn*Y*b2-u*(X*Bp*b2+Y*DD+Y*Y*hn*b2)-u*u*(X*KK*Y+X*x*W*b2-Y*chi*W*b2),
x*b2-alpha*Z*b2-Bp*W*b2+u*(-y*X-W*X*hn)*b2+u*u*(D6*Z*b2-Z*X*KK-Z*Z*x*b2+W*chi*Z*b2),
(-chi-y*Y-Z*Bp-W*Y*hn)*b2-W*DD+u*(D6*W*b2-Z*KK*Y-Z*x*W*b2+W*W*chi*b2)
]
rad=Q(1,10**100); BIG=Q(10**20); delta=Q(1,10**12)
weights=[rad,1,1,1]+[BIG]*12+[5]*4
assert len(weights)==len(v)

def abscoeff(a):
    vals=[Q(int(q.numerator),int(q.denominator)) for q in a.to_list()]
    if len(vals)==1: return abs(vals[0])
    assert len(vals)==2
    return 2*abs(vals[0])+abs(vals[1])

def bound(p):
    z=Q(0)
    for mon,a in p.items():
        term=abscoeff(a)
        for w,n in zip(weights,mon):
            if n: term*=w**n
        z+=term
    return z

# |b|>=1/2. Differentiation of FN/b^2 gives denominator b^3.
ft=max(bound(f.diff(u)*b-2*B*f)*8 for f in FN)
fut=max(sum((bound(f.diff(z).diff(u)*b-2*B*f.diff(z))*8 for z in [X,Y,Z,W]),Q(0)) for f in FN)
fuu=max(sum((bound(f.diff(z).diff(w))*4 for z in [X,Y,Z,W] for w in [X,Y,Z,W]),Q(0)) for f in FN)
assert ft<10**8*BIG and fut<10**8*BIG and fuu<10**6
assert 100*(fut*rad+fuu*delta)<Q(1,2)
assert 100*ft*rad<delta/2
print('First block: exact uniform contraction and displacement bounds passed.')
print('Analytic tau disk radius: 10^-100; graph radius: 10^-12.')

# Independent unbordered second-arrow equations.
alpha2=1+u**3*ad; Bp2=-be-u*fs0-u*u*(efs-fa)
hn2=-H+u*j; qn2=-b-u**3*bd
KK2=Kn-u*Ka*b2; DD2=Dn-u*Da*b2
FN2=[
KK2+(qn2-alpha2)*b2*X-Bp2*b2*Y-u*X*Y*hn2*b2-u*u*X*X*KK2,
hn2*b2+qn2*Y*b2-u*(X*Bp2*b2+Y*DD2+Y*Y*hn2*b2)-u*u*X*KK2*Y]
ft2=max(bound(f.diff(u)*b-2*B*f)*8 for f in FN2)
fut2=max(sum((bound(f.diff(z).diff(u)*b-2*B*f.diff(z))*8 for z in [X,Y]),Q(0)) for f in FN2)
fuu2=max(sum((bound(f.diff(z).diff(w))*4 for z in [X,Y] for w in [X,Y]),Q(0)) for f in FN2)
assert ft2<10**8*BIG and fut2<10**8*BIG and fuu2<10**6
assert 100*(fut2*rad+fuu2*delta)<Q(1,2)
assert 100*ft2*rad<delta/2
print('Second block: all identical conservative bounds passed.')
