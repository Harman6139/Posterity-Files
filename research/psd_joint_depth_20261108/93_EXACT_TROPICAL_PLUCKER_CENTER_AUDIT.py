#!/usr/bin/env python3
"""Exact SymPy/Fraction audit of universal Dikin–Plucker bridge (86–92).
Quarter-power 3x3 centre/initial Slater; tied vs independent 6x6
identical top Plucker tier, first signed difference at order 1/22.
"""
from fractions import Fraction as Q
from itertools import combinations
import sympy as s

def E(i,j,n):
    x=s.zeros(n);x[i,j]=1;return x
def F(i,j,n):
    return E(i,j,n)+E(j,i,n) if i!=j else E(i,i,n)
def pd(A):
    return all(s.simplify(A[:i,:i].det())>0 for i in range(1,A.rows+1))

def quarter():
    n=3
    H1=-E(0,0,n)+E(1,1,n)+F(0,2,n)
    H2=F(0,1,n)
    theta=(Q(0),Q(1,2),Q(1))
    rows=[(i,j) for i in range(n) for j in range(i,n)]
    B=s.Matrix([[H[i,j] for H in (H1,H2)] for i,j in rows])
    vals=[]
    for I in combinations(range(len(rows)),2):
        det=B.extract(list(I),[0,1]).det()
        if det:
            val=sum((theta[rows[k][0]]+theta[rows[k][1]])/2 for k in I)
            vals.append((val,I,det))
    high=max(v for v,I,d in vals)
    top=[I for v,I,d in vals if v==high]
    assert high==Q(3,4) and len(top)==2
    assert all((0,1) in [rows[j] for j in I] for I in top)
    B0=E(0,0,n)+E(2,2,n)
    a=1/s.sqrt(3)
    M0=B0+a*(E(1,1,n)+F(0,2,n))
    W=M0.inv()
    assert pd(M0) and pd(W)
    assert all(s.simplify(s.trace(W*H))==0 for H in
               [E(1,1,n)+F(0,2,n),F(0,1,n)])
    ep=s.symbols('ep',positive=True)
    t=(s.sqrt(4*ep**2+3*ep)-2*ep)/3
    C=E(0,0,n)+ep*s.eye(n)+t*H1
    Din=s.diag(1,ep**(-s.Rational(1,4)),ep**(-s.Rational(1,2)))
    limit=(Din*C*Din).applyfunc(lambda x:s.limit(x,ep,0,dir='+'))
    assert s.simplify(limit-M0)==s.zeros(n)
    print('PASS: quarter-power exact central Slater/Plucker cone limit')

def tied():
    n=6;lam=s.Rational(1,100)
    H1=E(1,1,n)-E(0,0,n)+lam*F(0,2,n)
    H2=E(2,2,n)-E(0,0,n)+lam*F(1,4,n)
    H3=E(3,3,n)-E(0,0,n)+lam*F(1,5,n)
    H4=E(4,4,n)-E(0,0,n)+lam*F(3,5,n)
    G=lam*F(0,1,n)
    A=(H1,H2,H3,H4,G)
    T=(H1,H2+lam*F(0,5,n),H3,H4,G)
    w=(Q(0),Q(3,11),Q(6,11),Q(7,11),Q(9,11),Q(1))
    I0=((1,1),(2,2),(3,3),(4,4),(0,1))
    I1=((1,1),(0,5),(3,3),(4,4),(0,1))
    def determinant(generators,I):
        return s.Matrix([[H[i,j] for H in generators] for i,j in I]).det()
    def weight(I):return sum((w[i]+w[j])/2 for i,j in I)
    assert determinant(A,I0)==determinant(T,I0)==lam
    assert determinant(A,I1)==0 and determinant(T,I1)==lam**2
    assert weight(I0)==Q(53,22)
    assert weight(I0)-weight(I1)==Q(1,22)
    def maxsupport(H):
        return max((w[i]+w[j])/2 for i in range(n)
                   for j in range(i,n) if H[i,j])
    levels=(w[1],w[2],w[3],w[4],w[1]/2)
    assert tuple(map(maxsupport,A))==tuple(map(maxsupport,T))==levels
    assert sum(levels)==weight(I0)
    for H,J in zip(A,T):
        for i in range(n):
            for j in range(i,n):
                if (w[i]+w[j])/2==maxsupport(H):
                    assert H[i,j]==J[i,j]
    def peel(actions):
        remain=set(range(n));out=[]
        while remain!={0}:
            C=remain-{0}
            while True:
                bad={i for i in C if 1<=i<=4
                     and all(a in remain and b in remain for a,b in actions[i-1])
                     and not any(a in C and b in C for a,b in actions[i-1])}
                if not bad:break
                C-=bad
            assert C
            out.append(tuple(sorted(C)));remain-=C
        return tuple(out)
    assert peel([((0,2),),((1,4),),((1,5),),((3,5),)])==((5,),(3,4),(2,),(1,))
    assert peel([((0,2),),((1,4),(0,5)),((1,5),),((3,5),)])==((5,),(2,3,4),(1,))
    print('PASS: 6x6 same leading Plucker, first difference order 1/22')
    print('PASS: same Bellman-weight Dikin filtration, different 4 vs 3 facial steps')

if __name__=='__main__':
    quarter();tied()
    print('PASS ALL exact tropical/Plucker centre and facial depth checks')
