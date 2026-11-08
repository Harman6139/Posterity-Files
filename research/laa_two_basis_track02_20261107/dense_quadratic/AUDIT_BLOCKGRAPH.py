#!/usr/bin/env python3
"""Exact SymPy audit of a genuinely noncommuting dense block-graph example.
Does not rely on floating-point rank thresholds.
"""
import sympy as s
H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
B=s.diag(H,H,s.eye(1))
def rotate(B,i,j):
    C=B.copy()
    x=B[:,i]
    y=B[:,j]
    C[:,i]=(x+y)/s.sqrt(2)
    C[:,j]=(x-y)/s.sqrt(2)
    return C

bases=[B]+[rotate(B,i,j) for i in (0,1) for j in (2,3)]+[rotate(B,j,4) for j in (2,3)]
K1=s.diag(1,-1,0,0,0)
K2=s.diag(0,0,1,-1,0)
rows=[]
for A in bases:
    assert s.simplify(A.T*A-s.eye(5))==s.zeros(5)
    for j in range(5):
        v=A[:,j]
        P=v*v.T
        assert s.simplify((v.T*K1*v)[0])==0
        assert s.simplify((v.T*K2*v)[0])==0
        assert all(s.simplify(P[i,4])==0 for i in (0,1))
        rows.append([P[i,k]*(1 if i==k else 2) for i in range(5) for k in range(i,5)])
span_rank=s.Matrix(rows).rank()
assert span_rank==11
R=s.eye(5)-2*s.Matrix([1,2,3,4,5])*s.Matrix([[1,2,3,4,5]])/55
missing=s.zeros(5)
missing[0,4]=missing[4,0]=1
A=R*K1*R.T
C=R*missing*R.T
assert R.T*R==s.eye(5)
assert A*C!=C*A
assert all(x!=0 for x in A)
assert all(x!=0 for x in C)
print({"block_graph_dimension":5,"span_rank":span_rank,"annihilator_noncommuting":True,
       "generic_dense_conjugation_exact":True})
