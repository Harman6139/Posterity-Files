"""Exact frozen small-eigenvalue switching identities. No orbit asymptotics asserted."""
import sympy as s
R=s.Rational; rt=s.sqrt(3)
g=s.symbols('gamma',positive=True); ca,ga,Q,j,x,y=s.symbols('Ca Ga Q j xi eta',real=True)
z=s.Matrix([ca,ga,Q]); W=s.diag(2,4,1); b=1/rt
r=(3*Q+4*g*ca+8*g*ga)/(3+8*g*g); cf=R(2,3)*(ca-ga+g*r); gf=-cf/2+g*r
p=3*x*x; lam=2*r-Q-p+rt*y*y; gap=6*g*j+rt*y*y
Fminus=s.Matrix([cf+3*j/2,(b*ga+(1-b)*gf+(j-x*y)/2)/(1+b),Q+p-r])
Fplus=Fminus+s.Matrix([0,0,lam])
Mminus=Fminus.jacobian(z).applyfunc(s.simplify);Mplus=Fplus.jacobian(z).applyfunc(s.simplify)
n=s.Matrix([2*g,0,1]);cov=n.T*W
assert all(s.simplify(v)==0 for v in Mplus*n-n)
assert s.simplify((cov*(Fplus-z))[0]-gap)==0
assert s.simplify((cov*(Fminus-z))[0]-(gap-lam))==0
print('neutral vector:',n.T); print('positive branch neutral drift:',gap)
for name,M in [('negative',Mminus),('positive',Mplus)]:
 B=(W-(2*M-s.eye(3)).T*W*(2*M-s.eye(3))).applyfunc(s.simplify)
 ell=s.Matrix([1,(1-8*g*g)/2,-2*g])
 expected=32*(2*rt-3)/(3+8*g*g)**2*ell*ell.T
 assert all(s.simplify(v)==0 for v in B-expected)
 print(name,'reflected contraction defect rank',B.rank())
 print('matrix=',B.applyfunc(lambda e:s.simplify(s.radsimp(e))))
 import itertools
 for k in range(1,4):
  for I in itertools.combinations(range(3),k):
   val=s.factor(B.extract(I,I).det(),extension=rt)
   print(I,val)
print('All exact identities passed; no gamma=1 trajectory claim is made.')
