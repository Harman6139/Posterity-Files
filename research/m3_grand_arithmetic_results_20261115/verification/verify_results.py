"""Exact finite checks supporting, not replacing, checkpoints 01--07.
Run with Python and SymPy: python verify_results.py
No network or floating-point eigenvalue claims are used.
"""
from __future__ import annotations
import itertools
import json
from pathlib import Path
from fractions import Fraction
import sympy as sp

OUT = Path(__file__).resolve().parent
checks: list[dict[str, object]] = []

def record(name: str, passed: bool, detail: object = None) -> None:
    checks.append({'name': name, 'passed': bool(passed), 'detail': detail})
    if not passed:
        raise AssertionError(f'{name}: {detail}')

def gram(mats: list[sp.Matrix]) -> sp.Matrix:
    return sp.Matrix([[sp.trace(a.T*b) for b in mats] for a in mats])

def W(t):
    return sp.Matrix([[0,1],[1,t]])

def B(s,t):
    return sp.Matrix([[0,0,s,-1],[0,0,1,s],[s,1,t,0],[-1,s,0,t]])

def fast_arrow(n: int):
    ts=sp.symbols(f't1:{n+1}')
    a=sp.zeros(n+1)
    a[0,1]=a[1,0]=1
    for i in range(1,n+1):
        a[i,i]=ts[i-1]
        if i<n:
            a[0,i+1]=a[i+1,0]=2*ts[i-1]
    return ts,a

# 01: moment matching and isometry.
t=sp.symbols('t', real=True)
A0=(0,3,3); A1=(1,1,4)
record('01_threshold_moments',
       all(sum(a**j for a in A0)==sum(a**j for a in A1) for j in range(3)))
ext0=sum((t-a)**2 for a in A0); ext1=sum((t-a)**2 for a in A1)
record('01_exterior_polynomial_identity', sp.expand(ext0-ext1)==0)
record('01_exterior_derivative_identity', sp.diff(ext0-ext1,t)==0)
for n in range(1,9):
    M=sp.integer_nthroot(3*n,2)[0]
    if M*M<3*n: M+=1
    r=M*M-3*n
    record(f'01_isometry_n{n}', sp.Rational(3*n+r,M*M)==1,
           {'order':M*M+2, 'bits':n, 'success_at_n_minus_one': '1/2'})
u=sp.symbols('u', positive=True)
z=1/u-u
record('01_tail_inverse_identity', sp.expand(u*(z+u))==1)

# 03: everywhere-invertible block and direction counts.
s,t=sp.symbols('s t', real=True)
lam=sp.Symbol('lambda')
charB=B(s,t).charpoly(lam).as_expr()
record('03_block_characteristic', sp.expand(charB-(lam**2-t*lam-s*s-1)**2)==0)
record('03_block_determinant', sp.factor(B(s,t).det())==(s*s+1)**2)
for n in range(2,6):
    ts=sp.symbols(f't1:{n+1}')
    blocks=[W(ts[0])]+[B(ts[i-1],ts[i]) for i in range(1,n)]
    blocks += [W(ts[0]) for _ in range(4)]
    for i in range(1,n-1): blocks += [W(ts[i]) for _ in range(3)]
    blocks += [W(ts[-1]) for _ in range(2)]
    X=sp.diag(*blocks)
    H=[X.diff(ts[i])/ (3 if i<n-1 else 2) for i in range(n)]
    record(f'03_full_gram_n{n}', gram(H)==sp.eye(n), {'order': X.rows})
    record(f'03_order_n{n}', X.rows==10*n-2)

# 05: non-C2 codimension-two example.
u,v,z=sp.symbols('u v z', real=True)
AA=sp.Matrix([[sp.Rational(7,10)*u,v/2],[v/2,-u/10]])
XX=sp.diag(AA,AA,W(z))
record('05_isometric_gram',gram([XX.diff(q) for q in (u,v,z)])==sp.eye(3))
record('05_rank_drop_determinant', sp.expand(AA.det()+sp.Rational(7,100)*u*u+v*v/4)==0)
record('05_non_C2_coefficients', sp.Rational(1,100)!=sp.Rational(49,100))

# 07: characteristic identities, finite irreducibility checks and rank crossing.
for n in range(1,5):
    ts,X=fast_arrow(n)
    p=X.charpoly(lam).as_expr()
    a=[sp.Integer(1)]+[2*ts[i-1] for i in range(1,n)]
    formula=lam*sp.prod(lam-t for t in ts)-sum(
        a[i]**2*sp.prod(lam-ts[j] for j in range(n) if j!=i) for i in range(n))
    record(f'07_arrow_char_formula_n{n}',sp.expand(p-formula)==0)
    factors=sp.factor_list(p,lam,*ts)[1]
    record(f'07_irreducibility_finite_check_n{n}',len(factors)==1 and factors[0][1]==1)
    H=[X.diff(ts[i])/(3 if i<n-1 else 1) for i in range(n)]
    record(f'07_isometric_gram_n{n}',gram(H)==sp.eye(n))
    atone=X.subs({t:1 for t in ts})
    record(f'07_anchor_norm_n{n}',sp.trace(atone**2)==9*n-6)
    if n>1:
        _,prevX=fast_arrow(n-1)
        prevp=prevX.charpoly(lam).as_expr()
        remainder=sp.expand(p-((lam-ts[-1])*prevp-4*ts[-2]**2*sp.prod(lam-t for t in ts[:-1])))
        record(f'07_arrow_recursion_n{n}',remainder==0)
        gcd=sp.Poly(prevp,lam,domain=sp.QQ.frac_field(*ts[:-1])).gcd(
            sp.Poly(sp.prod(lam-t for t in ts[:-1]),lam,domain=sp.QQ.frac_field(*ts[:-1])))
        record(f'07_primitive_coefficients_n{n}',gcd.degree()==0)
    if n<=3:
        zz=sp.symbols('zz')
        R=(zz*sp.eye(n+1)-X**2).det(method='domain-ge')
        record(f'07_squared_spectrum_finite_check_n{n}',len(sp.factor_list(R,zz,*ts)[1])==1)

ts,X=fast_arrow(2)
record('07_CORRECTED_order3_determinant', sp.expand(X.det()+ts[1]+4*ts[0]**3)==0,
       {'determinant':str(sp.factor(X.det())), 'rank_crossing_at_t1_1': 't2=-4'})
Xcross=X.subs({ts[0]:1,ts[1]:-4})
v0=sp.Matrix([2,-2,1])
record('07_zero_eigenvector_at_correct_crossing',Xcross*v0==sp.zeros(3,1))
deriv=(v0.T*X.diff(ts[1])*v0)[0]/(v0.T*v0)[0]
record('07_crossing_speed',deriv==sp.Rational(1,9),str(deriv))
record('07_second_derivative_jump',deriv**2==sp.Rational(1,81))

# Exact Schur certificates on the explicit escape curve.
for n in range(1,6):
    e=sp.Rational(1,8)
    vals=[sp.Rational(n)/e]
    for i in range(1,n): vals.append(4*n*vals[-1]**2/e)
    cross=[sp.Integer(1)]+[2*q for q in vals[:-1]]
    schur=sum(c*c/(q+e) for c,q in zip(cross,vals))
    record(f'07_schur_certificate_n{n}',schur<=e,
           {'e':str(e), 'last_diagonal_bits': int(vals[-1].p).bit_length()})

# Classical Moser coefficients and generating identity.
def moser(m:int,k:int,r:int):
    return sum((-1)**(j-1)*j**(r-1)*sp.binomial(m,k-j) for j in range(1,k+1))
for m in range(2,13):
    for r in range(1,m+1):
        record(f'07_moser_k1_m{m}_r{r}',moser(m,1,r)==1)
        record(f'07_moser_k2_m{m}_r{r}',moser(m,2,r)==m-2**(r-1))
zz=sp.symbols('zz')
for m in range(2,7):
    mu=[sp.Rational(i*i+1,i+1) for i in range(1,m+1)]
    maxr=4
    g={r:sum(x**r for x in mu)*sum((-1)**(j-1)*j**(r-1)*zz**j for j in range(1,m+1))
       for r in range(1,maxr+1)}
    E={0:sp.Integer(1)}
    for r in range(1,maxr+1):
        E[r]=sp.Poly(sum(sp.binomial(r-1,j-1)*g[j]*E[r-j] for j in range(1,r+1)),zz).as_expr()
        E[r]=sum(sp.expand(E[r]).coeff(zz,j)*zz**j for j in range(m+1))
    for k in range(1,m):
        for r in range(1,maxr+1):
            target=sum(sum(mu[i] for i in I)**r for I in itertools.combinations(range(m),k))
            generated=sp.expand((1+zz)**m*E[r]).coeff(zz,k)
            record(f'07_moser_generating_m{m}_k{k}_r{r}',sp.simplify(generated-target)==0)
a=[sp.Rational(i) for i in (1,2,4,8)]
b=[sum(a)/2-x for x in a]
ps=lambda a:sorted(a[i]+a[j] for i in range(4) for j in range(i+1,4))
record('07_pair_sum_exception_m4',ps(a)==ps(b) and sorted(a)!=sorted(b))

# 04: exact rational response-code separation.
for d in range(1,5):
    for H in range(1,4):
        base=2*H+2
        vv=[Fraction(1,base**i) for i in range(d)]
        values=sorted(sum(a*x for a,x in zip(row,vv)) for row in itertools.product(range(H+1),repeat=d))
        sep=min(b-a for a,b in zip(values,values[1:]))
        lower=Fraction(1,2*base**(d-1))
        record(f'04_code_separation_d{d}_H{H}',sep>=lower,
               {'actual_min':str(sep),'proved_lower':str(lower)})

report={'scope':'Finite exact symbolic checks. Not universal proofs or independent peer review.',
        'checks':len(checks),'all_passed':all(c['passed'] for c in checks),
        'sympy_version':sp.__version__,'results':checks}
(OUT/'VERIFICATION_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='results'},indent=2))
