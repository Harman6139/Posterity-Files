"""Exact finite-grid CP/COP certificates (standard library only).

The correction is proved in manuscript 37. Enumeration and exact simplex can
be exponentially expensive. Resource-limit errors are not infeasibility.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
from math import isqrt
from typing import Sequence

Matrix = list[list[F]]


def matrix(A: Sequence[Sequence[object]]) -> Matrix:
    B = [[F(x) for x in row] for row in A]
    n = len(B)
    if not n or any(len(row) != n for row in B):
        raise ValueError("A nonempty square matrix is required")
    if any(B[i][j] != B[j][i] for i in range(n) for j in range(n)):
        raise ValueError("The matrix must be symmetric")
    return B


def trace(A: Matrix) -> F:
    return sum((A[i][i] for i in range(len(A))), F(0))


def pairing(A: Matrix, B: Matrix) -> F:
    return sum((A[i][j]*B[i][j] for i in range(len(A))
                for j in range(len(A))), F(0))


def quadratic(A: Matrix, v: Sequence[int]) -> F:
    return sum((A[i][j]*v[i]*v[j] for i in range(len(A))
                for j in range(len(A))), F(0))


def shifted(A: Matrix, delta: F) -> Matrix:
    return [[x + (delta if i == j else 0) for j, x in enumerate(row)]
            for i, row in enumerate(A)]


def rays(n: int, q: int) -> list[tuple[int, ...]]:
    if n < 1 or q < 1:
        raise ValueError("n and q must be positive integers")
    return [v for v in product(range(q+1), repeat=n) if max(v) == q]


def check_grid(A: Matrix, q: int) -> tuple[bool, tuple[int, ...] | None, int]:
    count = 0
    for v in rays(len(A), q):
        count += 1
        if quadratic(A, v) < 0:
            return False, v, count
    return True, None, count


def integer_sqrt_ceiling(r: F) -> int:
    if r < 0:
        raise ValueError("Negative radicand")
    k = isqrt(r.numerator // r.denominator)
    return k if F(k*k) >= r else k+1


def descent_or_separator(A0, R0) -> dict:
    """Return an integer non-COP witness or a strict COP separator of A.

    Given <A,R><0, the cutoff uses the sharp constant without radicals:
    eta_q <= alpha iff 4*q*q*alpha*(1+alpha) >= 1.
    In the separator outcome R itself need not be copositive.
    """
    A, R = matrix(A0), matrix(R0)
    if len(A) != len(R):
        raise ValueError("Incompatible dimensions")
    g = -pairing(A, R)
    if g <= 0:
        raise ValueError("A strict descent direction <A,R><0 is required")
    h = trace(A)*trace(R)
    alpha = g/(2*h) if h > 0 else F(1,4)
    q = max(1, integer_sqrt_ceiling(1/(4*alpha*(1+alpha))))
    assert 4*q*q*alpha*(1+alpha) >= 1
    ok, v, count = check_grid(R, q)
    if not ok:
        assert v is not None and quadratic(R,v) < 0
        return {"kind":"negative_integer_vector", "q":q, "vector":v,
                "value":quadratic(R,v), "tested":count}
    if trace(R) > 0:
        W = shifted(R, alpha*trace(R))
        margin = trace(R)*(alpha*(1+alpha)-F(1,4*q*q))/(1+2*alpha)
        diagonal_shift = alpha*trace(R)
        assert margin > 0
    else:
        assert trace(R) == 0 and all(x >= 0 for row in R for x in row)
        diagonal_shift = g/(2*(1+abs(trace(A))))
        W = shifted(R, diagonal_shift)
        margin = diagonal_shift
    assert pairing(A,W) < 0
    return {"kind":"copositive_separator", "q":q, "alpha":alpha,
            "base":R, "separator":W, "pairing":pairing(A,W),
            "diagonal_shift":diagonal_shift, "strict_margin":margin,
            "grid_tests":count}


def strict_margin(A0, max_q: int = 128) -> dict:
    """Return a positive exact copositivity margin using doubling grids.

    Complete for strict COP inputs if the cutoff is removed. A boundary
    input may never get a positive certificate. Hitting the cap raises.
    """
    A = matrix(A0)
    n, q = len(A), 1
    while q <= max_q:
        vs = rays(n,q)
        beta = min(quadratic(A,v)/sum(t*t for t in v) for v in vs)
        if beta < 0:
            v = next(v for v in vs if quadratic(A,v) < 0)
            return {"kind":"negative_integer_vector", "q":q, "vector":v}
        u = F(1,4*q*q)
        lower = (1+n*u)*beta-u*trace(A)
        if lower > 0:
            return {"kind":"strict_copositivity", "q":q,
                    "margin":lower, "grid_minimum":beta,
                    "grid_tests":len(vs)}
        q *= 2
    raise RuntimeError("No conclusion within max_q; increase the resource cap")


def grid_cone_phase_one(B0, q: int, max_pivots: int = 20000) -> dict:
    """Exact phase-I simplex for the finite integer-generated CP cone.

    Uses Bland's rules. Returns a verified weighted factor or finite-cone
    separating form. Weighted factors are not floating-point Gram columns.
    """
    B = matrix(B0)
    n = len(B)
    coords = [(i,j) for i in range(n) for j in range(i,n)]
    vs = rays(n,q)
    m, N = len(coords), len(vs)
    rhs = [B[i][j] for i,j in coords]
    signs = [F(1) if b >= 0 else F(-1) for b in rhs]
    tab = []
    for k,(i,j) in enumerate(coords):
        row = [signs[k]*v[i]*v[j] for v in vs]
        row += [F(int(k == l)) for l in range(m)]
        row += [signs[k]*rhs[k]]
        tab.append(row)
    basis = list(range(N,N+m))
    rc = [-sum((tab[k][j] for k in range(m)),F(0)) for j in range(N)]
    rc += [F(0)]*m
    value = sum((row[-1] for row in tab),F(0))
    pivots = 0
    while True:
        enter = next((j for j,c in enumerate(rc) if c < 0), None)
        if enter is None:
            break
        candidates = [(tab[i][-1]/tab[i][enter],basis[i],i)
                      for i in range(m) if tab[i][enter] > 0]
        if not candidates:
            raise ArithmeticError("Unexpected unbounded phase-I objective")
        leave = min(candidates)[2]
        pivot = tab[leave][enter]
        tab[leave] = [v/pivot for v in tab[leave]]
        newrow = tab[leave]
        for i in range(m):
            if i != leave and tab[i][enter]:
                a = tab[i][enter]
                tab[i] = [v-a*w for v,w in zip(tab[i],newrow)]
        a = rc[enter]
        value += a*newrow[-1]
        rc = [v-a*w for v,w in zip(rc,newrow[:-1])]
        basis[leave] = enter
        pivots += 1
        if pivots > max_pivots:
            raise RuntimeError("Exact simplex resource cap reached; no conclusion")
    if value == 0:
        terms = [(tab[i][-1],vs[j]) for i,j in enumerate(basis)
                 if j < N and tab[i][-1] > 0]
        exact = [[sum((w*v[i]*v[j] for w,v in terms),F(0))
                  for j in range(n)] for i in range(n)]
        assert exact == B and len(terms) <= m
        return {"kind":"factor", "terms":terms, "pivots":pivots,
                "generators":N, "matrix":B}
    assert value > 0
    y = [-signs[i]*(1-rc[N+i]) for i in range(m)]
    W = [[F(0) for _ in range(n)] for _ in range(n)]
    for k,(i,j) in enumerate(coords):
        W[i][j] = W[j][i] = y[k] if i == j else y[k]/2
    assert all(quadratic(W,v) >= 0 for v in vs)
    assert pairing(W,B) == -value < 0
    return {"kind":"grid_separator", "separator":W,
            "pairing":-value, "pivots":pivots, "generators":N}


def finite_accuracy_alternative(A0, q: int, max_pivots: int = 20000) -> dict:
    """Return factor of A+tr(A)/(4q^2)I or true COP separator of A."""
    A = matrix(A0)
    u = F(1,4*q*q)
    B = shifted(A, u*trace(A))
    out = grid_cone_phase_one(B,q,max_pivots=max_pivots)
    if out["kind"] == "factor":
        out.update({"input":A,"diagonal_shift":u*trace(A),"q":q})
        return out
    W = out["separator"]
    Y = shifted(W,u*trace(W))
    assert pairing(A,Y) == pairing(B,W) < 0
    out.update({"kind":"copositive_separator", "input":A,
                "base":W,"separator":Y,"alpha":u,"q":q,
                "pairing":pairing(A,Y)})
    return out
