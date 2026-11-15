"""Exact Q(sqrt(3), gamma) checks for Checkpoint 16.
These identities support, but do not replace, the analytic trapping proof.
Run: python gamma_family_algebra.py (requires SymPy).
"""
import sympy as s
q=s.Rational; root=s.sqrt(3)
g=s.symbols('g', positive=True)
xi,eta,j=s.symbols('xi eta j', real=True)
ca,ga,Q=s.symbols('ca ga Q',real=True)
b=1/root; N=q(9,16); kap=9*root/8
r=(3*Q+4*g*ca+8*g*ga)/(3+8*g*g)
cf=q(2,3)*(ca-ga+g*r); gf=-cf/2+g*r
nextv=s.Matrix([cf+3*j/2,(b*ga+(1-b)*gf+(j-xi*eta)/2)/(1+b),Q+3*xi**2-r])
M=nextv.jacobian([ca,ga,Q]).applyfunc(s.simplify)
R0=3*xi**2; CF=2*root*j+2*g*R0+root*xi*eta
star=s.Matrix([CF+3*j/2,g*R0-CF/2+3*j/2,R0-6*g*j])
assert all(s.simplify(x)==0 for x in (nextv.subs(dict(zip([ca,ga,Q],star)))-star))
D=s.diag(2,4,1); defect=(D-M.T*D*M).applyfunc(s.simplify)
minors=[(16*g*g-18+16*root)/(3+8*g*g)**2,((-128+96*root)*g*g-64+44*root)/(3+8*g*g)**2,(-64+44*root)/(3+8*g*g)**2]
for k in range(1,4): assert s.simplify(defect[:k,:k].det()-minors[k-1])==0
A=root*g*(14*g+1)/2; B=root*g*(2*g-1)/2; C=-3*g*(2*g-1)
S=A*xi**2+B*eta**2+C*xi*eta
J=-S/(6*g)
rot=lambda f:s.expand(N*(eta*s.diff(f,xi)-xi*s.diff(f,eta)))
assert s.simplify(rot(J)+kap*J+q(9,2)*g*xi**2+3*root*xi*eta/4)==0
loss=(3*A+B)*q(3,4)
assert s.simplify(loss-3*root*g*(22*g+1)/4)==0
P=C/N*(q(15,16)*xi**4-q(9,8)*xi**2*eta**2-q(9,16)*eta**4)+(loss-6*A)/N*xi**3*eta-loss/N*xi*eta**3
assert s.simplify(rot(P)-6*xi**2*S+loss*(xi**2+eta**2)**2)==0
margin=s.Matrix([[A,C/2],[C/2,B-root]])
assert s.simplify(margin.det()-q(3,2)*g*(8*g**3-16*g-1))==0
c0=27*root/256; a0=2*c0-N*N
Fstar=s.simplify(a0/loss)
assert s.simplify(Fstar-9*(2-root)/(64*g*(22*g+1)))==0
print('M_gamma =',M)
print('Gram-defect leading principal minors =',minors)
print('S_gamma =',s.expand(S))
print('J_gamma =',s.expand(J))
print('P_gamma =',s.expand(P))
print('B_gamma =',s.factor(loss))
print('Fstar_gamma =',Fstar)
print('All exact identities passed. Trapping is proved separately.')
