"""Exact reconstruction of the gamma-family weighted spectral chart.
Rational functions only; no floating-point eigenvectors. Analytic trapping is separate.
Run with Python 3 and SymPy. Writes a JSON verification record next to this file.
"""
from pathlib import Path
import json
import sympy as sp
s3=sp.sqrt(3); rr=sp.Rational
T,b,x,y,z,w,x2,y2,E,C,G,H,xi,eta,chi,Ca,Ga,Q,j,ad,bd,fa,f,g=sp.symbols('tau b x y zeta omega x2 y2 E C G H xi eta chi Ca Ga Q j ad bd fa f gamma',real=True)
unknown=[b,x,y,z,w,x2,y2];params=[T,E,C,G,H,xi,eta,chi,Ca,Ga,Q,j,ad,bd,fa,f,g]
c=2*(C-G)/3;den=3+8*g*g;r=(3*Q+4*g*Ca+8*g*Ga)/den;caf=2*(Ca-Ga+g*r)/3;gaf=-caf/2+g*r

def eqns(sign=1,coupling=True):
 a=1-sign*T**3*ad;B=b-sign*T**3*bd;beta=rr(1,2)+T*f+sign*T**2*fa
 d=2*c-C+sign*T*(2*caf-Ca);h=H+sign*T*j;K=c+G-sign*T*(2*gaf-Ga);q=2*r-Q
 if coupling:
  return [-K-(a+B)*x+beta*y-T*eta*z+T*x*y*h+T**2*x*x*K-T**2*z*(x*xi-y*chi),-h-B*y+T*(-eta*w+beta*x-d*y+y*y*h)+T**2*(x*y*K-w*(x*xi-y*chi)),xi-a*z+beta*w+T*(-eta*x+x*w*h)+T**2*(q*z+x*z*K-z*(z*xi-w*chi)),-chi-eta*y+beta*z-d*w+y*w*h+T*(q*w+y*z*K-w*(z*xi-w*chi))]
 return [-K-(a+B)*x2+beta*y2+T*x2*y2*h+T**2*x2*x2*K,-h-B*y2+T*(beta*x2-d*y2+y2*y2*h)+T**2*x2*y2*K]

t=sp.symbols('t',positive=True)
aa=1-T**3*ad;bb=b-T**3*bd;be=rr(1,2)+T*f+T**2*fa
dd=2*c-C+T*(2*caf-Ca);hh=H+T*j;kk=c+G-T*(2*gaf-Ga);qq=2*r-Q
Rpp=sp.Matrix([[aa/t,-be],[-be,t*dd]]);Rqq=sp.Matrix([[-bb/t,-t*eta],[-t*eta,t**3*qq]])
Rqp=sp.Matrix([[-t*kk,-hh],[t*xi,-t*t*chi]]);X=sp.Matrix([[t*t*x,t*y],[t*t*z,t*w]])
Riccati=Rqp+Rqq*X-X*Rpp-X*Rqp.T*X
for ind,div in zip([(0,0),(0,1),(1,0),(1,1)],[t,1,t,t*t]):
 assert sp.cancel(sp.expand(Riccati[ind]/div).subs(t*t,T)-eqns()[2*ind[0]+ind[1]])==0
charge=b*b-rr(1,3)+T*(E+8*H*H)/6+T**2*(2*C*C+4*G*G+4*eta*eta)/6+T**3*(8*j*j+2*chi*chi)/6+T**4*(2*Ca*Ca+4*Ga*Ga+Q*Q)/6-T**6*(2*ad*ad-6*bd*bd)/6
Fr=[charge]+eqns()+eqns(-1,False)
F=[sp.expand(sp.cancel(v*den)) if i else sp.expand(v) for i,v in enumerate(Fr)]
polys=[sp.Poly(v,*(unknown+params)) for v in F];counts=[len(p.terms()) for p in polys];degrees=[p.total_degree() for p in polys];coeff=max(abs(k) for p in polys for k in p.coeffs())
assert sum(counts)<500 and max(degrees)<=10 and coeff<1000
y0=-H/b;x0=(-c-G+y0/2)/(1+b);delta=2*c-C+H*H/b-rr(1,4);w0=(xi/2-chi+H*eta/b)/delta;z0=xi+w0/2
base={T:0,x:x0,y:y0,z:z0,w:w0,x2:x0,y2:y0};JJ=sp.Matrix(Fr).jacobian(unknown).subs(base);D=sp.factor(JJ.det());expected=2*b**3*(1+b)**2*delta
assert sp.simplify(D-expected)==0 or sp.simplify(D+expected)==0
b0=s3/3;H0=s3/4;C0=rr(3,8)+3*s3/16;G0=3*(s3-1)/16;N=rr(9,16);ell=rr(3,4);f0=9*s3/64
Rf=3*xi*xi;cf0=2*s3*j+2*g*Rf+s3*xi*eta;ca0=cf0+3*j/2;ga0=g*Rf-cf0/2+3*j/2;Q0=Rf-6*g*j
refs={b:b0,H:H0,C:C0,G:G0,chi:ell*eta,Ca:ca0,Ga:ga0,Q:Q0,f:f0,ad:0,bd:0,fa:0};ref_graph={x:-N,y:-ell,z:3*xi,w:4*xi,x2:-N,y2:-ell}
F6=sp.Matrix(Fr[1:]);graph=[x,y,z,w,x2,y2]
J6=sp.simplify(F6.jacobian(graph).subs(T,0).subs(refs).subs(ref_graph));Ft=sp.simplify(F6.diff(T).subs(T,0).subs(refs).subs(ref_graph));u1=[sp.simplify(e) for e in -J6.inv()*Ft]
B=b-T**3*bd;h=H+T*j;K=c+G-T*(2*gaf-Ga);q=2*r-Q
Dg=1+T*(y*y+w*w)+T**2*(x*x+z*z)+T**3*(x*w-y*z)**2
J00=1+T*w*w+T**2*z*z;J01=-T*y*w-T**2*x*z;J11=1+T*y*y+T**2*x*x
n00=((B-T*h*y-T*T*K*x)*J00+T*(eta-h*w-T*K*z)*J01)/Dg
n01=((B-T*h*y-T*T*K*x)*(-y*w-T*x*z)+(eta-h*w-T*K*z)*J11)/Dg
n11=((eta+T*(xi*x-chi*y))*(-y*w-T*x*z)+(-q+xi*z-chi*w)*J11)/Dg

def leading(expr):return sp.simplify(expr.subs(T,0).subs(refs).subs(ref_graph))
def deriv(expr):return leading(expr.diff(T)+sum(expr.diff(v)*dv for v,dv in zip(graph,u1)))
assert sp.simplify(leading(n01)-eta)==0
assert sp.simplify(deriv(n01)+N*xi)==0
assert sp.simplify(leading(n11)+6*g*j)==0
assert sp.simplify(leading(n00*x*x)-27*s3/256)==0
assert sp.simplify(deriv(n00))==0
sub1={v:ref_graph[v]+T*d for v,d in zip(graph,u1)}
f2=[sp.simplify(sp.Poly(sp.expand(expr.subs(refs).subs(sub1,simultaneous=True)),T).coeff_monomial(T**2)) for expr in F6]
u2=[sp.simplify(e) for e in -J6.inv()*sp.Matrix(f2)]
K0=sp.simplify((c+G).subs(refs));D0=sp.simplify((2*c-C+H*H/b).subs(refs))
def slow(block):
 if block==0:
  xx,yy,zz,ww=-N,-ell,3*xi,4*xi;xx1,yy1,zz1,ww1=u1[:4];yy2=u2[1];jj,ee=j,eta
 else:
  xx,yy,zz,ww=-N,-ell,0,0;xx1,yy1=u1[4:];zz1=ww1=0;yy2=u2[5];jj,ee=-j,0
 n002=sp.expand(-b0*xx*xx+H0*yy1-jj*yy-K0*xx-ee*yy*ww)
 n011=sp.expand((xx-yy/2)*zz+(D0*yy-xx/2)*ww)
 return sp.expand(-b0*yy2-n002*yy-ee*ww1-n011*ww)
jf=sp.simplify((slow(0)-slow(1))/2)
assert sp.simplify(jf+9*s3*j/8+rr(9,2)*g*xi*xi+3*s3*xi*eta/4)==0
out={'term_counts':counts,'total_terms':sum(counts),'degrees':degrees,'max_coefficient':str(coeff),'jacobian_unscaled':str(D),'filter':str(sp.factor(jf)),'status':'All exact assertions passed; uniform nonlinear trapping is proved separately.'}
print(json.dumps(out,indent=2));Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
