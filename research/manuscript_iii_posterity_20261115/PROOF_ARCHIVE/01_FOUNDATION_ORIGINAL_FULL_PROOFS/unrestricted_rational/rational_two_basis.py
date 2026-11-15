"""Exact rational one-scale normal form for arbitrary real SDPs.

Input: rational symmetric source measurement matrices. No trace certificate.
Output: two rational complete orthonormal bases (I,U), rational affine-line
observation data W*b+t*v, and a rational globally positive compression decoder.

Requires Python 3 and SymPy. No numerical solver or Internet is used.
This is an implementation of the accompanying algebraic proof, not its proof.
"""
from dataclasses import dataclass
from typing import Sequence
import sympy as sp

@dataclass
class RationalTwoBasis:
    A: tuple
    m: int
    p: int
    d: int
    N: int
    rho: sp.Rational
    alpha: sp.Rational
    F: sp.Matrix
    U: sp.Matrix
    Rdecoder: sp.Matrix  # D(Y)=Rdecoder*Y*Rdecoder.T/2
    S: sp.Matrix
    source_scale: sp.Rational
    W: sp.Matrix
    v: sp.Matrix
    ctrace: sp.Rational
    f: sp.Rational
    Delta: sp.Matrix
    R0: sp.Matrix
    raw: sp.Matrix
    raw_targets: sp.Matrix
    L: sp.Rational
    G: sp.Matrix

    def encode(self, X: sp.Matrix) -> sp.Matrix:
        X = sp.Matrix(X)
        if X.shape != (self.m, self.m) or X != X.T:
            raise ValueError("X must be a real symmetric source matrix")
        m = self.m
        t = sp.trace(X)
        B = X-self.rho*t*sp.eye(m)/2
        x = sp.Matrix([B[i,j] for i in range(m) for j in range(m)])
        base = (self.rho*t*sp.eye(m)/2).row_join(B).col_join(
            B.row_join(self.rho*t*sp.eye(m)/2))
        arrow = sp.Matrix([[t]]).row_join(x.T).col_join(
            x.row_join(self.alpha*t*sp.eye(m*m)))
        J = sp.diag(base,arrow)
        return self.F.T*self.S*J*self.S*self.F/self.source_scale**2

    def decode(self, Y: sp.Matrix) -> sp.Matrix:
        if Y.shape != (self.N,self.N):
            raise ValueError("Y has the wrong order")
        return self.Rdecoder*Y*self.Rdecoder.T/2

    def measure(self, Y: sp.Matrix) -> sp.Matrix:
        second = self.U.T*Y*self.U
        return sp.Matrix([Y[i,i] for i in range(self.N)] +
                         [second[i,i] for i in range(self.N)])

    def centered_measure(self, Y: sp.Matrix) -> sp.Matrix:
        return (self.measure(Y)-self.v*sp.trace(Y)/self.ctrace)/self.f

    def source_measure(self, X: sp.Matrix) -> sp.Matrix:
        return sp.Matrix(self.p, 1, [sp.trace(a*X) for a in self.A])

    def centered_target(self, b: sp.Matrix) -> sp.Matrix:
        b = sp.Matrix(b)
        if len(b) != self.p:
            raise ValueError("b has the wrong dimension")
        b = sp.Matrix(self.p, 1, list(b))
        return self.W*b/self.f

    def lift_cost(self, C: sp.Matrix) -> sp.Matrix:
        return self.Rdecoder.T*C*self.Rdecoder/2


def construct(measurements: Sequence[sp.Matrix], m: int | None = None) -> RationalTwoBasis:
    """Construct exactly over the rationals, including redundant/zero rows."""
    A = tuple(sp.Matrix(a) for a in measurements)
    if m is None:
        if not A:
            raise ValueError("m is required for an empty measurement list")
        m = A[0].rows
    if m < 1:
        raise ValueError("m must be positive")
    for a in A:
        if a.shape != (m,m) or a != a.T or any(not x.is_Rational for x in a):
            raise ValueError("Measurements must be rational symmetric matrices of order m")
    p = len(A)
    aug = A+(sp.eye(m),)
    q = p+1
    rho = sp.Integer(2*m)
    alpha = sp.Integer(4*m**3)
    k = m*m
    d = 2*m+1+k
    e = sp.eye(d)
    anchor = 2*m
    start = anchor+1
    theta = sp.Matrix([rho/2]*(2*m)+[sp.Integer(1)]+[alpha]*k)
    cols, targets, invcols = [], [], []
    def put(vector, target, inv):
        cols.append(vector); targets.append(target); invcols.append(inv)
    def trace_target(value):
        a = sp.zeros(q,1); a[p] = value; return a

    # All coordinates.
    for j in range(d):
        inv = sp.zeros(q,1)
        if j < 2*m:
            for a in range(q):
                inv[a] = aug[a][j % m,j % m]/2
        put(e[:,j],trace_target(theta[j]),inv)
    # Fix each of the two source-coordinate blocks.
    for offset in (0,m):
        for i in range(m):
            for j in range(i+1,m):
                for sign in (-1,1):
                    put(e[:,offset+i]+sign*e[:,offset+j], trace_target(rho),
                        sp.Matrix([sign*a[i,j]/4 for a in aug]))
    # Four-character entry-copy identities.
    for i in range(m):
        for j in range(m):
            for s in (-1,1):
                for u in (-1,1):
                    vector=e[:,anchor]+s*e[:,start+i*m+j]+u*e[:,i]-s*u*e[:,m+j]
                    put(vector, trace_target(1+alpha+rho),
                        sp.Matrix([-s*a[i,j]/8 for a in aug]))
    # All original equations and the added trace equation.
    for a,mat in enumerate(aug):
        av = sp.zeros(d,1)
        for i in range(m):
            for j in range(m):
                av[start+i*m+j] = mat[i,j]
        norm2 = sum(x*x for x in mat)
        for sign in (1,-1):
            tar=trace_target(1+alpha*norm2-sign*rho*sp.trace(mat))
            tar[a] += 2*sign
            inv=sp.zeros(q,1); inv[a]=sp.Rational(sign,4)
            put(e[:,anchor]+sign*av,tar,inv)
    raw=sp.Matrix.hstack(*cols)
    C0=sp.Matrix.hstack(*targets).T
    R0=sp.Matrix.hstack(*invcols)
    M0=raw.cols
    assert M0 == 7*m*m+1+2*q
    S_A=sum(sum(x*x for x in a) for a in aug)
    L=sp.Integer(4*m*m+6*m+2*q+6)+2*S_A
    sigma=1/(2*L)
    Braw=sigma*raw
    Q=Braw*Braw.T
    S=sp.eye(d)+Q
    source_scale=1+sigma**2*(6*m-1)
    Sinv=S.inv()
    G=(sp.eye(d)-Q)*Sinv
    G=G.row_join(2*Sinv*Braw)
    eta=4*sigma**2/source_scale**2
    theta_hat=sp.Matrix([(S*sp.diag(*theta)*S)[i,i]/source_scale**2 for i in range(d)])
    comp=sp.Matrix([theta[j]*sum((sp.eye(d)-Q)[i,j]**2 for i in range(d))/source_scale**2 for j in range(d)])
    CG=sp.zeros(d,q); CG[:,p]=comp
    CG=CG.col_join(eta*C0)
    a,b=sp.Rational(4,5),sp.Rational(3,5)
    F=(a*sp.eye(d)).row_join(b*G)
    N=F.cols
    U=2*F.T*F-sp.eye(N)
    Yfirst=sp.zeros(d,q); Yfirst[:,p]=a*a*theta_hat
    Yfirst=Yfirst.col_join(b*b*CG)
    Phi=Yfirst.col_join(Yfirst)
    W,v=Phi[:,:p],Phi[:,p]
    ctrace=sum(theta_hat)
    f=4*b*b*eta
    Rbase=sp.zeros(m,d)
    for i in range(m):
        Rbase[i,i]=1; Rbase[i,m+i]=1
    Rdecoder=Rbase*F
    Delta=sp.diag(*([-b*b]*d+[a*a]*G.cols))
    assert N == 9*m*m+4*m+5+2*p
    return RationalTwoBasis(A,m,p,d,N,rho,alpha,F,U,Rdecoder,S,
                            source_scale,W,v,ctrace,f,Delta,R0,raw,C0,L,G)


def exact_checks() -> dict:
    # A weakly infeasible 2x2 source: X11=0, X12=1.
    A=[sp.diag(1,0),sp.Matrix([[0,sp.Rational(1,2)],[sp.Rational(1,2),0]])]
    inst=construct(A)
    Z=lambda mat: all(x == 0 for x in mat)
    checks={}
    checks['rational_U']=all(x.is_Rational for x in inst.U)
    checks['rational_data']=all(x.is_Rational for x in list(inst.W)+list(inst.v))
    checks['parseval']=Z(inst.G*inst.G.T-sp.eye(inst.d))
    checks['coisometry']=Z(inst.F*inst.F.T-sp.eye(inst.d))
    checks['signed_isotropy']=Z(inst.F*inst.Delta*inst.F.T)
    checks['data_inverse']=Z(inst.R0*inst.raw_targets-sp.eye(3))
    checks['isometric_target']=Z(inst.W.T*inst.W-inst.f**2*sp.eye(inst.p))
    checks['positive_scale_direction']=all(x > 0 for x in inst.v)
    checks['trace_scale']=sum(inst.v[:inst.N]) == inst.ctrace
    checks['decoder_coisometry']=Z(inst.Rdecoder*inst.Rdecoder.T-2*sp.eye(inst.m))
    # Verify adjoint extraction, without a symbolic ambient matrix.
    Rbase=sp.zeros(inst.m,inst.d)
    for i in range(inst.m): Rbase[i,i]=Rbase[i,inst.m+i]=1
    for j,a in enumerate(A+[sp.eye(inst.m)]):
        observed=sum((inst.R0[j,k]*(inst.raw[:,k]*inst.raw[:,k].T) for k in range(inst.raw.cols)),sp.zeros(inst.d))
        checks[f'raw_adjoint_{j}']=Z(observed-Rbase.T*a*Rbase/2)
    curves=[]
    for eps in (sp.Rational(1,2),sp.Rational(1,3),sp.Rational(1,4)):
        X=sp.Matrix([[eps,1],[1,1/eps]])
        Y=inst.encode(X)
        b=sp.Matrix([0,1])
        r=inst.centered_measure(Y)-inst.centered_target(b)
        exact_target=inst.W*(inst.source_measure(X)-b)/inst.f
        assert Z(r-exact_target)
        assert Z(inst.decode(Y)-X)
        assert sp.trace(Y)==inst.ctrace*sp.trace(X)
        curves.append({'epsilon':str(eps),'source_trace':str(sp.trace(X)),
                       'squared_centered_residual':str((r.T*r)[0]),
                       'trace_identity':True})
    assert all(checks.values()),checks
    # An exact order-one construction, no original constraints.
    scalar=construct([],m=1)
    checks['zero_measurement_input']=scalar.N == 18
    assert checks['zero_measurement_input']
    return {'status':'passed','m':inst.m,'p':inst.p,'N':inst.N,
            'c_trace':str(inst.ctrace),'forward_physical_factor':str(inst.f),
            'checks':checks,'weak_infeasibility_curves':curves,
            'scope':'Exact rational finite-instance identities; the general theorem is proved separately.'}

if __name__=='__main__':
    import json
    print(json.dumps(exact_checks(),indent=2))
