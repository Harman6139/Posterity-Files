"""Exact rational copositive separation and Ryshkov primitives.

Python 3.10+, standard library only. No floating-point mathematical decisions.
Resource limits raise ResourceLimit; they never certify infeasibility.
The nonlocal separator uses classical support enumeration and a rationally
rounded ellipsoid. It is NOT an adjacent-pivot implementation in disguise.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import combinations, product
from math import gcd, isqrt, lcm
from typing import Sequence

class ResourceLimit(RuntimeError):
    pass

def matrix(a: Sequence[Sequence[object]]) -> list[list[F]]:
    n = len(a)
    if not n or any(len(row) != n for row in a):
        raise ValueError("A nonempty square matrix is required")
    if any(isinstance(x, float) for row in a for x in row):
        raise TypeError("Use integers, Fraction objects, or rational strings, not floats")
    q = [[F(x) for x in row] for row in a]
    if any(q[i][j] != q[j][i] for i in range(n) for j in range(n)):
        raise ValueError("The matrix must be symmetric")
    return q

def dot(a, b):
    return sum((x*y for x,y in zip(a,b)), F(0))

def quad(q, x):
    return sum((q[i][j]*x[i]*x[j] for i in range(len(q)) for j in range(len(q))), F(0))

def pairing(a, b):
    return sum((x*y for ar,br in zip(a,b) for x,y in zip(ar,br)), F(0))

def add(a,b,t=F(1)):
    return [[x+t*y for x,y in zip(ar,br)] for ar,br in zip(a,b)]

def trace(a):
    return sum((a[i][i] for i in range(len(a))), F(0))

def norm1(a):
    return sum((abs(x) for row in a for x in row), F(0))

def ceil_sqrt(q: F) -> int:
    q=F(q)
    if q<0: raise ValueError("Negative radicand")
    k=isqrt(q.numerator//q.denominator)
    return k if k*k*q.denominator == q.numerator else k+1

def solve_det(a, b):
    """Return (unique solution, determinant), or (None, 0)."""
    n=len(a)
    z=[[F(x) for x in row]+[F(b[i])] for i,row in enumerate(a)]
    det=F(1)
    for k in range(n):
        r=next((i for i in range(k,n) if z[i][k]),None)
        if r is None: return None,F(0)
        if r!=k: z[r],z[k]=z[k],z[r]; det=-det
        pivot=z[k][k]; det*=pivot
        z[k]=[v/pivot for v in z[k]]
        for i in range(k+1,n):
            t=z[i][k]
            if t: z[i]=[x-t*y for x,y in zip(z[i],z[k])]
    x=[F(0)]*n
    for k in range(n-1,-1,-1):
        x[k]=z[k][-1]-sum((z[k][j]*x[j] for j in range(k+1,n)),F(0))
    return x,det

def simplex_min(q, certificate=False):
    """Exact min x^T Q x on x>=0, sum x=1, including singular cases.

    Singular bordered systems are skipped, not interpreted as positive.
    A minimum-support global minimizer has a nonsingular bordered system.
    """
    q=matrix(q); n=len(q); best=None; arg=None; table=[]
    for mask in range(1,1<<n):
        s=[i for i in range(n) if mask>>i&1]; r=len(s)
        b=[[q[i][j] for j in s]+[F(-1)] for i in s]
        b.append([F(1)]*r+[F(0)])
        sol,det=solve_det(b,[F(0)]*r+[F(1)])
        row={"support":[i+1 for i in s],"determinant":str(det)}
        if sol is not None:
            x,t=sol[:-1],sol[-1]
            row.update(x=[str(v) for v in x],value=str(t))
            if all(v>=0 for v in x):
                xx=[F(0)]*n
                for i,v in zip(s,x): xx[i]=v
                if quad(q,xx)!=t or sum(xx)!=1: raise ArithmeticError("KKT identity failure")
                if best is None or t<best: best,arg=t,xx
        if certificate: table.append(row)
    if best is None: raise ArithmeticError("Singleton supports must supply candidates")
    return best,arg,table

def integer_negative_witness(q):
    m,x,_=simplex_min(q)
    if m>=0: return None
    den=lcm(*(v.denominator for v in x))
    w=tuple(int(den*v) for v in x)
    g=0
    for v in w: g=gcd(g,v)
    w=tuple(v//g for v in w)
    if quad(q,w)>=0: raise ArithmeticError("Invalid negative witness")
    return w

def pairs(n): return [(i,j) for i in range(n) for j in range(i,n)]

def from_coords(z,n):
    q=[[F(0)]*n for _ in range(n)]
    for v,(i,j) in zip(z,pairs(n)): q[i][j]=q[j][i]=F(v)
    return q

def normal(x):
    return [F(x[i]*x[j]*(1 if i==j else 2)) for i,j in pairs(len(x))]

def objective(a):
    return [a[i][j]*(1 if i==j else 2) for i,j in pairs(len(a))]

def null_vector(rows,d):
    """A one-dimensional rational nullspace, or None."""
    z=[[F(x) for x in row] for row in rows]; piv=[]; r=0
    for col in range(d):
        k=next((i for i in range(r,len(z)) if z[i][col]),None)
        if k is None: continue
        z[r],z[k]=z[k],z[r]; t=z[r][col]; z[r]=[x/t for x in z[r]]
        for i in range(len(z)):
            if i!=r and z[i][col]:
                t=z[i][col]; z[i]=[x-t*y for x,y in zip(z[i],z[r])]
        piv.append(col); r+=1
        if r==len(z): break
    free=[j for j in range(d) if j not in piv]
    if len(free)!=1: return None
    x=[F(0)]*d; x[free[0]]=1
    for i,j in enumerate(piv): x[j]=-z[i][free[0]]
    den=lcm(*(v.denominator for v in x)); y=[int(den*v) for v in x]
    g=0
    for v in y: g=gcd(g,abs(v))
    return tuple(v//g for v in y)

def lattice_box(b,n,max_vectors):
    count=(b+1)**n-1
    if max_vectors is not None and count>max_vectors:
        raise ResourceLimit(f"Enumeration requires a box with {count} nonzero vectors")
    for v in product(range(b+1),repeat=n):
        if any(v): yield v

def ryshkov_minima(p,max_vectors=2_000_000):
    """Certify membership in R and enumerate its active constraints exactly."""
    p=matrix(p); n=len(p); m,_,_=simplex_min(p)
    if m<=0: raise ValueError("The input is not strictly copositive")
    b=ceil_sqrt(1/m); out=[]
    for v in lattice_box(b,n,max_vectors):
        if m*sum(x*x for x in v)>1: continue
        val=quad(p,v)
        if val<1: raise ValueError(f"Not a Ryshkov point: violating vector {v}")
        if val==1: out.append(v)
    return out

def tangent_rays(active,n,max_subsets=2_000_000):
    d=n*(n+1)//2; rows=[normal(v) for v in active]; out=set(); seen=0
    for inds in combinations(range(len(rows)),d-1):
        seen+=1
        if max_subsets is not None and seen>max_subsets: raise ResourceLimit("Too many ray subsets")
        z=null_vector([rows[i] for i in inds],d)
        if z is None: continue
        for sign in (1,-1):
            w=tuple(sign*v for v in z)
            if all(dot(a,w)>=0 for a in rows): out.add(w)
    return [from_coords(z,n) for z in sorted(out)]

def effective_ir_bound(n,M):
    q=ceil_sqrt(4*n*F(M))
    return q,F(1,2*n*q**(2*(n-1))),2*n*q**(n-1)

def neighbor(p,r,w=None,max_vectors=2_000_000):
    """Exact neighbor for a known Ryshkov vertex and non-COP tangent extreme ray.

    Uses the universal effective-IR cutoff; an exact positive simplex margin
    at the witness cutoff is an optional acceleration, not an assumption.
    """
    p=matrix(p); r=matrix(r); n=len(p)
    if w is None: w=integer_negative_witness(r)
    if w is None or quad(r,w)>=0: raise ValueError("A negative integer witness is required")
    s0=(quad(p,w)-1)/(-quad(r,w))
    if s0<=0: raise ValueError("The supplied direction is not a feasible outgoing edge")
    M0=norm1(p)+s0*norm1(r)
    _,_,b=effective_ir_bound(n,M0)
    q=add(p,r,s0); mq,_,_=simplex_min(q)
    if mq>0: b=min(b,ceil_sqrt(1/mq))
    ell=None; blocker=None
    for v in lattice_box(b,n,max_vectors):
        rv=quad(r,v)
        if rv>=0: continue
        val=(quad(p,v)-1)/(-rv)
        if val<=0: raise ValueError("Nonpositive candidate edge length")
        if ell is None or val<ell: ell,blocker=val,v
    if ell is None or ell>s0: raise ArithmeticError("The cutoff omitted a blocking constraint")
    return add(p,r,ell),ell,blocker

def canonical(n):
    return [[F(1) if i==j else (F(-1,2) if abs(i-j)==1 else F(0)) for j in range(n)] for i in range(n)]

def anchor(n):
    return [[F(min(i+1,j+1)*(n-max(i,j))) for j in range(n)] for i in range(n)]

def shadow_separate(a,max_pivots=1000,max_vectors=2_000_000,max_ray_subsets=2_000_000):
    """Specified minimum-ratio rule, with an exact support-based COP ray test.

    Intended input: a nonmember of CP. No false conclusion is returned if a
    resource limit is reached. The routine can also return a local CP membership
    indication when no decreasing tangent ray exists.
    """
    a=matrix(a); n=len(a); p=canonical(n); c=anchor(n); path=[]
    k=0
    while True:
        path.append(p)
        if pairing(a,p)<0: return p,path,"vertex"
        active=ryshkov_minima(p,max_vectors)
        rays=tangent_rays(active,n,max_ray_subsets)
        choices=[r for r in rays if pairing(a,r)<0]
        if not choices: return None,path,"in_current_normal_cone"
        r=min(choices,key=lambda r:(pairing(c,r)/(-pairing(a,r)),tuple(objective(r))))
        w=integer_negative_witness(r)
        if w is None: return r,path,"ray"
        if max_pivots is not None and k==max_pivots: raise ResourceLimit("Pivot budget exhausted")
        p,_,_=neighbor(p,r,w,max_vectors)
        k+=1

def floor_log2(q):
    q=F(q)
    if q<=0: raise ValueError("Positive argument required")
    k=q.numerator.bit_length()-q.denominator.bit_length()
    p=F(2**k) if k>=0 else F(1,2**(-k))
    if q<p: k-=1
    return k

def pow2(k): return F(2**k) if k>=0 else F(1,2**(-k))

def reciprocal_sqrt_lower(sigma,d):
    k=floor_log2(sigma)//2
    lo,hi=pow2(-k-1),pow2(-k)
    rho=F(1,64*d)
    while hi-lo>rho*lo:
        mid=(lo+hi)/2
        if mid*mid*sigma<=1: lo=mid
        else: hi=mid
    return lo

def dyadic_floor(x,p):
    scale=1<<p
    return F((x.numerator*scale)//x.denominator,scale)

def ellipsoid_update(c,q,a,t):
    """Rational central-cut update. Requires a != 0 and d >= 2.

    E(c,q) intersect {a^T(z-c)<=0} is contained in the returned ellipsoid.
    The volume decreases by at least exp(-1/(4d)).
    """
    d=len(c)
    v=[dot(row,a) for row in q]; sigma=dot(a,v)
    if sigma<=0: raise ArithmeticError("Nonpositive ellipsoid directional variance")
    r=reciprocal_sqrt_lower(sigma,d)
    center=[c[i]-r*v[i]/(d+1) for i in range(d)]
    alpha=F(d*d,d*d-1); gamma=F(2,d+1)
    qp=[[alpha*(q[i][j]-gamma*v[i]*v[j]/sigma) for j in range(d)] for i in range(d)]
    clog=(d-1).bit_length()
    p=2*(t+1)+10+2*clog
    tau=F(1,1<<p)
    center=[dyadic_floor(x,p) for x in center]
    b=[[F(0)]*d for _ in range(d)]
    for i in range(d):
        for j in range(i,d): b[i][j]=b[j][i]=dyadic_floor(qp[i][j],p)
        b[i][i]+=d*tau
    inflate=(1+F(1,16*d*d))**2
    return center,[[inflate*x for x in row] for row in b]

def encoding_bound(a):
    n=len(a)
    return max(1,n.bit_length()+sum(abs(a[i][j].numerator).bit_length()+a[i][j].denominator.bit_length()+2 for i,j in pairs(n)))

def separation_oracle(c,a,eps):
    n=len(a); d=len(c)
    for i,v in enumerate(c):
        if abs(v)>1:
            cut=[F(0)]*d; cut[i]=1 if v>1 else -1
            return cut,None
    cost=objective(a)
    if dot(cost,c)>-eps: return cost,None
    w=from_coords(c,n)
    q=[row[:] for row in w]
    for i in range(n): q[i][i]-=eps
    m,x,_=simplex_min(q)
    if m<0: return [-v for v in normal(x)],None
    return None,w

def nonlocal_separate(a,initial_precision=None,max_iterations=100_000):
    """Exact strict COP separator for rational A outside CP, ||A||_F <= 1.

    Unknown gaps are handled by doubling the precision exponent. A failed
    ellipsoid stage is NOT a membership certificate. Every returned matrix has
    both margins at least epsilon. Complexity is polynomial in binary precision
    for fixed n, with 2^n support enumeration per oracle call.
    """
    a=matrix(a); n=len(a)
    if pairing(a,a)>1: raise ValueError("Normalize A to Frobenius norm at most one")
    if n==1:
        if a[0][0]<0:
            return [[F(1)]],{"iterations":0,"precision":0,"epsilon":str(min(F(1),-a[0][0]))}
        raise ValueError("Input is completely positive")
    if not any(x for row in a for x in row): raise ValueError("Zero is completely positive")
    d=n*(n+1)//2
    s=encoding_bound(a) if initial_precision is None else int(initial_precision)
    if s<1: raise ValueError("initial_precision must be positive")
    total=0; stages=[]
    J=(128*n*d-1).bit_length()
    while True:
        eps=F(1,32*n*(1<<s)); N=8*d*d*(s+J+1)
        c=[F(0)]*d; q=[[F(d) if i==j else F(0) for j in range(d)] for i in range(d)]
        for t in range(N):
            if max_iterations is not None and total>=max_iterations: raise ResourceLimit("Ellipsoid budget exhausted")
            total+=1
            cut,w=separation_oracle(c,a,eps)
            if w is not None:
                if pairing(a,w)>-eps: raise ArithmeticError("Target margin failure")
                qq=[row[:] for row in w]
                for i in range(n): qq[i][i]-=eps
                m,_,cert=simplex_min(qq,True)
                if m<0: raise ArithmeticError("Cone margin failure")
                stages.append({"precision":s,"iterations":t+1,"accepted":True})
                return w,{"iterations":total,"precision":s,"epsilon":str(eps),"stages":stages,"cop_certificate_for_W_minus_epsilon_I":cert}
            c,q=ellipsoid_update(c,q,cut,t)
        stages.append({"precision":s,"iterations":N,"accepted":False})
        s*=2

def serialize_matrix(q): return [[str(x) for x in row] for row in q]
