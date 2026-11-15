"""Exact symbolic checks for the gamma=2 resonance draft.
These certify only the displayed algebraic identities, not nonlinear trapping.
Run with Python 3 and SymPy installed.
"""
import sympy as s
q=s.sqrt(3)
x,y,j,H,b=s.symbols('x y j H b', real=True)
N=s.Rational(9,16); kap=9*q/8
Cf=2*H**2/b**2-H/b
C=Cf+H**2/b;G=H**2/b-Cf/2
xx=(-Cf-G-H/(2*b))/(1+b);yy=-H/b
assert s.simplify(xx+H**2/b**2)==0
assert s.simplify(-xx/2+Cf*yy-H**2*(3*b/2-2*H)/b**3)==0
S=29*q*x**2+3*q*y**2-18*x*y
js=-S/12
rot=lambda f:s.expand(N*(y*s.diff(f,x)-x*s.diff(f,y)))
assert s.simplify(rot(js)+kap*js+9*x**2+3*q*x*y/4)==0
P=18*y**4-120*q*y**3*x+36*y**2*x**2-s.Rational(568,3)*q*y*x**3-30*x**4
assert s.simplify(rot(P)-6*x**2*S+(135*q/2)*(x*x+y*y)**2)==0
Ms=s.Matrix([[s.Rational(2,3),-s.Rational(2,3)],[-s.Rational(2,3)+q/3,(1+q)/6]])
Ma=s.Matrix([[s.Rational(34,35),-s.Rational(2,35),s.Rational(4,35)],
             [(-2+q)/35,(97-31*q)/70,(8-4*q)/35],
             [-s.Rational(8,35),-s.Rational(16,35),s.Rational(32,35)]])
for name,M,W in [('Ms',Ms,s.diag(1,2)),('Ma',Ma,s.diag(2,4,1))]:
    D=s.simplify(W-M.T*W*M)
    mins=[s.simplify(D[:i,:i].det())for i in range(1,M.rows+1)]
    assert all(z.is_positive for z in mins)
    print(name,'positive Gram-defect leading minors:',mins)
R=3*x*x;cfa=2*q*j+4*R+q*x*y
Ca=cfa+3*j/2;Ga=2*R-cfa/2+3*j/2;Q=R-12*j
r=(3*Q+8*Ca+16*Ga)/35
assert s.simplify(r-R)==0
assert s.simplify(2*(Ca-Ga+2*r)/3-cfa)==0
c0=27*q/256;a0=s.simplify(2*c0-N*N);B0=135*q/2
assert s.simplify(a0/B0-(2-q)/640)==0
print('All exact algebraic checks passed.')
