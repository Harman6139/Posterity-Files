#!/usr/bin/env python3
"""Exact SymPy checks for three universal Dikin–Hessian classifier test cases.
This verifies symbolic central branches and barrier metric rates, not the
general theorem (which has a self-contained proof in checkpoint 10).
"""
import sympy as s
e=s.symbols('epsilon',positive=True)
# n=2, rank-one target, kernel span F12: alpha=1/2
A=s.diag(1+e,e)
F=s.Matrix([[0,1],[1,0]])/s.sqrt(2)
g=s.factor(s.trace(A.inv()*F*A.inv()*F))
assert g==1/(e*(1+e))
print('alpha 1/2: lambda=',g,'rho=',s.sqrt(1/g))
# n=3, rank-one target, kernel bottom indefinite: alpha=1
B=s.diag(1+e,e,e)
H=s.diag(0,1,-1)/s.sqrt(2)
g=s.factor(s.trace(B.inv()*H*B.inv()*H))
assert g==1/e**2
print('alpha 1: lambda=',g,'rho=',s.sqrt(1/g))
# n=3, rank-one target, K=span(H0,F12), alpha=1/4
# X*=E11; H0=-E11+E22+F13; stationarity t_F12=0
# and 3s^2+4 epsilon*s-epsilon=0.
s0=(s.sqrt(4*e**2+3*e)-2*e)/3
M=s.Matrix([[1+e-s0,0,s0],[0,e+s0,0],[s0,0,e]])
H0=s.Matrix([[-1,0,1],[0,1,0],[1,0,0]])
Ht=s.Matrix([[0,1,0],[1,0,0]])/s.sqrt(2)
V=M.inv()
gtt=s.factor(s.trace(V*Ht*V*Ht))
gss=s.factor(s.trace(V*H0*V*H0))
assert s.factor(s.trace(V*H0*V*Ht))==0
assert s.limit(gtt*s.sqrt(e),e,0,dir='+')==3*s.sqrt(3)/2
assert s.limit(gss*e,e,0,dir='+')==9
print('alpha 1/4: lambda_min ~',s.limit(gtt*s.sqrt(e),e,0,dir='+'),'* epsilon^-1/2')
print('PASS: symbolic center and Hessian valuations agree with 1, 1/2, 1/4')
