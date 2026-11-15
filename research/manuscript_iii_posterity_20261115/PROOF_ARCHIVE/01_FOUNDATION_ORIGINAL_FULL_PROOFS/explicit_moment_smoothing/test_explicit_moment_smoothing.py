"""Finite exact diagnostic identities for Milestone 24; not a lower-bound proof."""
from fractions import Fraction as F
from itertools import product, combinations
from math import factorial, comb
import json
from explicit_moment_smoothing import (
    coordinates, vectors, coefficient, value, derivatives, soc_witness, metadata
)


def compositions(total, count):
    if count == 1:
        yield (total,)
    else:
        for a in range(total + 1):
            for rest in compositions(total - a, count - 1):
                yield (a,) + rest


def check_covariance(n):
    ws = list(vectors(n))
    d = len(ws[0])
    for i in range(d):
        for j in range(d):
            assert sum(w[i] * w[j] for w in ws) == (1 << n) * (i == j)
    return {"n": n, "D": d, "orthogonality": "exact"}


def check_coefficients(n=2, p=2):
    ws = list(vectors(n))
    d = len(ws[0])
    checked = 0
    nonzero = 0
    for alpha in compositions(2 * p, d):
        denom = 1
        for ai in alpha:
            denom *= factorial(ai)
        multinomial = factorial(2*p) // denom
        expected = 0
        for w in ws:
            term = multinomial
            for wi, ai in zip(w, alpha):
                term *= wi**ai
            expected += term
        observed = coefficient(n, alpha, p)
        assert observed == expected
        checked += 1
        nonzero += (observed != 0)
    return {"n": n, "p": p, "monomials_checked": checked,
            "nonzero_homogeneous_coefficients": nonzero, "parity_rule": "exact"}


def check_differential_and_soc(n=3, p=4):
    d = len(coordinates(n))
    x = [F((-1)**i, 16 * d) for i in range(d)]
    h = [F(i+1, d) for i in range(d)]
    grad, hess = derivatives(n, x, p)
    beta_norm = sum(a*a for a in x)/(4*d)
    homogeneous = value(n, x, p)-beta_norm
    assert sum(a*b for a,b in zip(x,grad)) == 2*p*homogeneous+2*beta_norm
    quad = sum(h[i]*hess[i][j]*h[j] for i in range(d) for j in range(d))
    gram = sum(a*a for a in h)/(2*d)
    for w in vectors(n):
        ell = sum(a*b for a,b in zip(w,x))
        wh = sum(a*b for a,b in zip(w,h))
        gram += 2*p*(2*p-1)*ell**(2*p-2)*wh**2
    assert quad == gram and quad > 0
    witness = soc_witness(n,x,p)
    assert witness["feasible"] and witness["final_slack"] == 1-value(n,x,p)
    for w, chain in zip(vectors(n), witness["chains"]):
        previous = sum(a*b for a,b in zip(w,x))
        for current in chain:
            assert current-previous*previous == 0
            previous = current
    return {"n": n, "p": p, "Euler_identity": "exact", "Hessian_Gram_identity": "exact",
            "SOC_chain_determinants": "all zero exactly", "SOC_final_slack_positive": True}


def check_robust_slacks(n=5,m=3):
    cs = coordinates(n)
    S = set(range(m))
    H = F(m*m,4)
    a = [F(0) for _ in cs]
    a[0] = F(m,4)-F(1,8)
    for index, subset in enumerate(cs):
        if len(subset)==2 and set(subset)<=S:
            a[index]=F(1,2)
    b=a[:]; b[0]-=H
    assert sum(x*x for x in b)<=m**4
    delta=F(1,256*n*n)
    shift=2*delta*m*m
    assert shift<=F(1,128)
    min_slack=None
    for s in product((-1,1),repeat=n):
        w=(1,)+s+tuple(s[i]*s[j] for i,j in combinations(range(n),2))
        exact = F(sum(s[:m])**2,4)-F(1,8)
        assert H+sum(x*y for x,y in zip(b,w))==exact
        for e in (-1,1):
            ell=H+e*sum(x*y for x,y in zip(b,w))
            assert ell>=0
            min_slack=ell if min_slack is None else min(min_slack,ell)
    return {"n":n,"m":m,"minimum_vertex_slack":str(min_slack),
            "uniform_shift":str(shift),"affine_slacks":"exact"}


def check_pseudodensity(m):
    half=F(m,2)
    lagrange=[]
    for w in range(m+1):
        coeff=F(1)
        for j in range(m+1):
            if j!=w:
                coeff *= (half-j)/(w-j)
        lagrange.append(coeff)
    assert sum(lagrange)==1
    square=sum(lagrange[w]*(F(w)-half)**2 for w in range(m+1))
    assert square==0
    D=[(1<<m)*lagrange[w]/comb(m,w) for w in range(m+1)]
    assert max(abs(a) for a in D)**2<=m**3
    shift=F(1,128)
    expect=sum(lagrange[w]*((F(w)-half)**2-F(1,8)+shift)/(m*m) for w in range(m+1))
    assert expect==(-F(1,8)+shift)/(m*m) and expect<-F(1,16*m*m)
    return {"m":m,"normalization":"exact","formal_centered_square":str(square),
            "negative_pairing":str(expect),"max_abs_density":str(max(abs(a) for a in D)),
            "degree_positive_pseudodensity_property":"imported LRS theorem, not inferred from this test"}


def run():
    return {"covariance":[check_covariance(n) for n in range(2,7)],
            "coefficients":[check_coefficients(2,2),check_coefficients(3,2)],
            "differential_and_soc":[check_differential_and_soc(2,4),check_differential_and_soc(3,4)],
            "robust_slacks":check_robust_slacks(),
            "pseudodensity_identities":[check_pseudodensity(m) for m in (3,5,7)],
            "theoretical_parameters":[metadata(n) for n in (2,4,8,16)],
            "scope":"Exact finite identities only; all-dimensional hardness is proved using the cited LRS input. Test exponents are deliberately smaller than the theoretical p."}


if __name__=="__main__":
    print(json.dumps(run(),indent=2))
