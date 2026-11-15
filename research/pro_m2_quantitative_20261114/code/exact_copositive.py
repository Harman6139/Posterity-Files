"""Exact rational copositivity and precision-controlled separation.

No third-party packages. All accepted certificates are checked with Fraction.
The ellipsoid routine is an alternative to adjacent Ryshkov pivots, not an
implementation of the original pivot rule. Its classical ingredients are
identified in the accompanying manuscript.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
from math import gcd, isqrt
from typing import Optional, Sequence

Matrix = list[list[F]]


def rational_matrix(a: Sequence[Sequence[object]]) -> Matrix:
    n = len(a)
    if n == 0 or any(len(row) != n for row in a):
        raise ValueError("A nonempty square matrix is required")
    q = [[F(x) for x in row] for row in a]
    if any(q[i][j] != q[j][i] for i in range(n) for j in range(n)):
        raise ValueError("The matrix must be symmetric")
    return q


def pairing(a: Matrix, b: Matrix) -> F:
    return sum((a[i][j] * b[i][j] for i in range(len(a))
                for j in range(len(a))), F(0))


def quadratic(a: Matrix, x: Sequence[F]) -> F:
    return sum((a[i][j] * x[i] * x[j] for i in range(len(a))
                for j in range(len(a))), F(0))


def solve_nonsingular(a: Matrix, rhs: Sequence[F]) -> Optional[list[F]]:
    """Fraction-free Bareiss elimination; None means singular, never infeasible.

    The caller uses this ONLY to identify nonsingular stationary systems.
    Row permutations are allowed and exact divisibility is checked.
    """
    m = len(a)
    den = 1
    for row in a:
        for value in row:
            den = den * value.denominator // gcd(den, value.denominator)
    for value in rhs:
        den = den * value.denominator // gcd(den, value.denominator)
    mat = [[int(value * den) for value in a[i]] + [int(rhs[i] * den)]
           for i in range(m)]
    previous = 1
    for k in range(m - 1):
        pivot_row = next((i for i in range(k, m) if mat[i][k]), None)
        if pivot_row is None:
            return None
        if pivot_row != k:
            mat[k], mat[pivot_row] = mat[pivot_row], mat[k]
        pivot = mat[k][k]
        for i in range(k + 1, m):
            for j in range(k + 1, m + 1):
                num = pivot * mat[i][j] - mat[i][k] * mat[k][j]
                quotient, remainder = divmod(num, previous)
                if remainder:
                    raise ArithmeticError("Bareiss exact-division invariant failed")
                mat[i][j] = quotient
            mat[i][k] = 0
        previous = pivot
    if mat[-1][-2] == 0:
        return None
    result = [F(0)] * m
    for i in range(m - 1, -1, -1):
        result[i] = (F(mat[i][m]) - sum((mat[i][j] * result[j]
                                       for j in range(i + 1, m)), F(0))) / mat[i][i]
    return result


def simplex_minimum(a: Sequence[Sequence[object]], transcript: bool = False):
    """Return the exact minimum of x^T A x on x>=0, sum x=1.

    A global minimizer of minimum support has a nonsingular bordered
    stationary system. All nonempty supports are checked, including singular
    and boundary cases. This is exponential in n, polynomial in bit length.
    """
    q = rational_matrix(a)
    n = len(q)
    best: Optional[F] = None
    best_x: Optional[list[F]] = None
    records = []
    systems = 0
    for size in range(1, n + 1):
        for support in combinations(range(n), size):
            systems += 1
            bordered = [[q[i][j] for j in support] + [F(-1)] for i in support]
            bordered.append([F(1)] * size + [F(0)])
            solution = solve_nonsingular(bordered, [F(0)] * size + [F(1)])
            record = {"support": list(support)}
            if solution is None:
                record["status"] = "singular"
            else:
                weights, value = solution[:-1], solution[-1]
                record.update(status="stationary", x=[str(v) for v in weights],
                              value=str(value))
                if all(v > 0 for v in weights):
                    full = [F(0)] * n
                    for i, value_i in zip(support, weights):
                        full[i] = value_i
                    if sum(full, F(0)) != 1 or quadratic(q, full) != value:
                        raise ArithmeticError("Stationary solution failed exact verification")
                    if best is None or value < best:
                        best, best_x = value, full
            if transcript:
                records.append(record)
    if best is None or best_x is None:
        raise ArithmeticError("Singleton supports must provide a candidate")
    return {"minimum": best, "minimizer": best_x, "systems": systems,
            "records": records}


def ceil_log2_integer(x: int) -> int:
    if x <= 0:
        raise ValueError("Positive integer required")
    return (x - 1).bit_length()


def round_dyadic(value: F, bits: int) -> F:
    """Nearest dyadic, with ties rounded upward; absolute error <=2^(-bits-1)."""
    scale = 1 << bits
    quotient = (value.numerator * scale * 2 + value.denominator) // (2 * value.denominator)
    return F(quotient, scale)


def center_update(c: list[F], v: list[F], norm_squared: F,
                  dimension: int, bits: int) -> list[F]:
    """Approximate c-v/((d+1)sqrt(norm_squared)) to <=2^-bits per coordinate.

    Root enclosures use integer square roots and exact rational comparisons.
    """
    if norm_squared <= 0:
        raise ArithmeticError("Positive definite shape and nonzero cut required")
    eps = F(1, 1 << bits)
    scaled = [value / (dimension + 1) for value in v]
    amplitude = max(abs(value) for value in scaled)
    def floor_log2_positive(value: F) -> int:
        exponent = value.numerator.bit_length() - value.denominator.bit_length()
        below = (value.numerator < (value.denominator << exponent)) if exponent >= 0 \
            else ((value.numerator << (-exponent)) < value.denominator)
        return exponent - int(below)

    exponent_q = floor_log2_positive(norm_squared)
    exponent_v = floor_log2_positive(amplitude)
    root_bits = max(0, bits + exponent_v + 4 - exponent_q,
                    (-exponent_q + 1) // 2 + 2)
    scale = 1 << root_bits
    integer_floor = isqrt((norm_squared.numerator << (2 * root_bits))
                         // norm_squared.denominator)
    if not integer_floor:
        raise ArithmeticError("Root lower bound invariant failed")
    lower = F(integer_floor, scale)
    if lower * lower == norm_squared:
        return [round_dyadic(ci - vi / lower, bits)
                for ci, vi in zip(c, scaled)]
    upper = F(integer_floor + 1, scale)
    inv_low, inv_high = 1 / upper, 1 / lower
    if amplitude * (inv_high - inv_low) > eps:
        raise ArithmeticError("Root enclosure precision invariant failed")
    inv_mid = (inv_low + inv_high) / 2
    return [round_dyadic(ci - vi * inv_mid, bits)
            for ci, vi in zip(c, scaled)]


def rounded_central_cut(c: list[F], shape: Matrix, a: list[F], iteration: int):
    """Rational, outward-rounded central ellipsoid update.

    The invariant requires shape_0=I. iteration is zero based. The retained
    halfspace is a dot (x-c)<=0. Every arithmetic decision is exact.
    """
    d = len(c)
    if d < 2 or not any(a):
        raise ValueError("Dimension >=2 and a nonzero cut are required")
    theta = F(1, 100 * (d + 1) ** 2)
    bits = 4 * (iteration + 1) + ceil_log2_integer(1000 * (d + 1) ** 4)
    eps = F(1, 1 << bits)
    v = [sum((shape[i][j] * a[j] for j in range(d)), F(0)) for i in range(d)]
    q = sum((a[i] * v[i] for i in range(d)), F(0))
    if q <= 0:
        raise ArithmeticError("Ellipsoid shape lost positive definiteness")
    factor = F(d * d, d * d - 1)
    exact_shape = [[factor * (shape[i][j] - F(2, d + 1) * v[i] * v[j] / q)
                    for j in range(d)] for i in range(d)]
    new_c = center_update(c, v, q, d, bits)
    inflation = (1 + theta) ** 2
    new_shape = [[round_dyadic(inflation * exact_shape[i][j], bits)
                  + (d * eps if i == j else 0) for j in range(d)] for i in range(d)]
    return new_c, new_shape, bits


def unpack(vector: Sequence[F], n: int) -> Matrix:
    result = [[F(0)] * n for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(i, n):
            result[i][j] = result[j][i] = vector[k]
            k += 1
    return result


def linear_coordinates(a: Matrix) -> list[F]:
    return [a[i][j] * (1 if i == j else 2)
            for i in range(len(a)) for j in range(i, len(a))]


def separation_stage(a: Sequence[Sequence[object]], precision: int,
                     resource_cap: Optional[int] = None,
                     collect_trace: bool = False):
    """Find a norm-one strict COP separator at scale rho=2^-precision.

    When dist(A,CP)>=rho, success within the proved budget is guaranteed.
    Exhaustion means only 'scale unsuccessful', NEVER exact CP membership.
    A resource cap raises RuntimeError rather than a mathematical conclusion.
    """
    target = rational_matrix(a)
    n = len(target)
    if precision < 0:
        raise ValueError("Nonnegative integer precision required")
    if pairing(target, target) > 1:
        raise ValueError("Input must be normalized to Frobenius norm at most one")
    if n == 1:
        if target[0][0] < 0:
            return {"status": "separator", "matrix": [[F(1)]],
                    "gap": -target[0][0], "margin": F(1), "iterations": 0,
                    "support_systems": 0, "trace": []}
        return {"status": "scale_unsuccessful", "iterations": 0}
    if not any(value for row in target for value in row):
        return {"status": "scale_unsuccessful", "iterations": 0}
    d = n * (n + 1) // 2
    rho = F(1, 1 << precision)
    epsilon = rho / (16 * n * n)
    budget = 8 * d * (d + 1) * (precision + ceil_log2_integer(32 * n * n) + 1)
    c = [F(0)] * d
    shape = [[F(int(i == j)) for j in range(d)] for i in range(d)]
    objective_cut = linear_coordinates(target)
    trace = []
    system_count = 0
    for iteration in range(budget):
        if resource_cap is not None and iteration >= resource_cap:
            raise RuntimeError("Explicit resource cap reached; no feasibility conclusion")
        w = unpack(c, n)
        norm_squared = pairing(w, w)
        objective = pairing(target, w)
        if norm_squared > 1:
            cut, kind = linear_coordinates(w), "norm"
        elif objective > -rho / 4:
            cut, kind = objective_cut, "objective"
        else:
            check = simplex_minimum(w)
            system_count += check["systems"]
            if check["minimum"] >= epsilon:
                certificate = simplex_minimum(w, transcript=True)
                return {"status": "separator", "matrix": w, "gap": -objective,
                        "margin": check["minimum"], "rho": rho,
                        "norm_squared": norm_squared, "iterations": iteration,
                        "budget": budget, "support_systems": system_count,
                        "support_certificate": certificate["records"], "trace": trace}
            x = check["minimizer"]
            rank_one = [[x[i] * x[j] for j in range(n)] for i in range(n)]
            cut, kind = [-v for v in linear_coordinates(rank_one)], "copositive"
        if collect_trace:
            trace.append({"iteration": iteration, "kind": kind,
                          "objective": str(objective), "norm_squared": str(norm_squared)})
        c, shape, _ = rounded_central_cut(c, shape, cut, iteration)
    return {"status": "scale_unsuccessful", "iterations": budget,
            "support_systems": system_count, "trace": trace}


def separate_nonmember(a: Sequence[Sequence[object]], max_stages: Optional[int] = None,
                       resource_cap_per_stage: Optional[int] = None):
    """Promise algorithm: terminates for every normalized rational nonmember.

    For CP inputs no termination is asserted. Optional caps raise exceptions.
    """
    target = rational_matrix(a)
    n = len(target)
    precision = max(1, ceil_log2_integer(32 * n * n))
    stage = 0
    total_iterations = 0
    while max_stages is None or stage < max_stages:
        result = separation_stage(target, precision, resource_cap_per_stage)
        total_iterations += result["iterations"]
        if result["status"] == "separator":
            result.update(stages=stage + 1, total_iterations=total_iterations,
                          precision=precision)
            return result
        precision *= 2
        stage += 1
    raise RuntimeError("Stage cap reached; no membership conclusion")
