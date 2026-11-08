#!/usr/bin/env python3
"""Exact SymPy audit of a dense nullity-3 depth-3 PSD witness.
The universal stress argument is in 20_UNIVERSAL_DENSE_NULLITY3_DEPTH3.md.
"""
import sympy as sp

def E(i, j, n=4):
    R = sp.zeros(n); R[i,j]=1
    return R

def F(i,j,n=4):
    return E(i,j,n)+E(j,i,n)

t=sp.symbols('t',positive=True)
A=E(1,1)-E(0,0)+F(0,3)
B=E(2,2)-E(0,0)+F(1,3)
C=F(0,3)+F(0,2)
Xstar=E(0,0)
X=sp.simplify(Xstar+t*(A-C)+2*t**2*B+5*t**3*E(3,3))
expected=sp.Matrix([[1-t-2*t**2,0,-t,0],[0,t,0,2*t**2],[-t,0,2*t**2,0],[0,2*t**2,0,5*t**3]])
assert X==expected
XP=X.extract([0,2,1,3],[0,2,1,3])
assert XP[:2,2:]==sp.zeros(2)
assert sp.simplify(XP[:2,:2].det()-t**2*(1-2*t-4*t**2))==0
assert sp.factor(XP[2:,2:].det())==t**4
assert all(H[3,3]==0 for H in [A,B,C])
# First stress is E33. Second has E22 compression; third has E11 compression.
Zsecond=E(2,2)-sp.Rational(1,2)*F(1,3)
assert all(sp.trace(Zsecond*H)==0 for H in [A,B,C])
assert Zsecond.extract([0,1,2],[0,1,2])==E(2,2,3)
Zthird=E(1,1)-sp.Rational(1,2)*F(0,3)+sp.Rational(1,2)*F(0,2)
assert all(sp.trace(Zthird*H)==0 for H in [A,B,C])
assert Zthird.extract([0,1],[0,1])==E(1,1,2)
print('PASS: dense nullity-3, exact 3-step dual stresses and cubic PSD arc')
