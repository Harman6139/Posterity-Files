#!/usr/bin/env python3
"""Exact rational, one-sided PSD-factor approximation of a positive table.

Input JSON: {"matrix": [["1", "2"], ["2", "3"]], "epsilon": "1/10"}
Run: python rational_psd_approximation.py input.json > output.json
All factors are represented as a nonnegative rational weight times vv^T.
The algorithm is polynomial in explicit table size for fixed dynamic range
and relative accuracy. It does not compute minimum PSD rank.
"""
from __future__ import annotations
import argparse
import json
import math
from fractions import Fraction
from typing import Any


def rational(value: Any) -> Fraction:
    if isinstance(value, float):
        raise TypeError("Use integer values or rational strings, not binary floats.")
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"Invalid rational value: {value!r}") from exc


def rank_factor(matrix: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[list[Fraction]]]:
    """Return U,V with matrix[i][j] == dot(U[i],V[j]), over Q."""
    a, b = len(matrix), len(matrix[0])
    rr = [row[:] for row in matrix]
    pivots: list[int] = []
    row = 0
    for col in range(b):
        pivot = next((i for i in range(row, a) if rr[i][col]), None)
        if pivot is None:
            continue
        rr[row], rr[pivot] = rr[pivot], rr[row]
        value = rr[row][col]
        rr[row] = [v / value for v in rr[row]]
        for i in range(a):
            if i != row and rr[i][col]:
                multiple = rr[i][col]
                rr[i] = [x - multiple*y for x, y in zip(rr[i], rr[row])]
        pivots.append(col)
        row += 1
        if row == a:
            break
    U = [[original[j] for j in pivots] for original in matrix]
    V = [[rr[k][j] for k in range(len(pivots))] for j in range(b)]
    return U, V


def construct(raw_matrix: Any, raw_epsilon: Any, max_degree: int | None = None) -> dict[str, Any]:
    if not isinstance(raw_matrix, list) or not raw_matrix or not isinstance(raw_matrix[0], list) or not raw_matrix[0]:
        raise ValueError("matrix must be a nonempty rectangular array")
    columns = len(raw_matrix[0])
    if any(not isinstance(row, list) or len(row) != columns for row in raw_matrix):
        raise ValueError("matrix must be rectangular")
    M = [[rational(x) for x in row] for row in raw_matrix]
    if any(x <= 0 for row in M for x in row):
        raise ValueError("Every matrix entry must be strictly positive")
    eps = rational(raw_epsilon)
    if not 0 < eps <= 1:
        raise ValueError("epsilon must belong to (0,1]")
    if max_degree is not None and max_degree < 0:
        raise ValueError("max_degree must be nonnegative")
    lower = min(x for row in M for x in row)
    upper = max(x for row in M for x in row)
    K, q = upper/lower, 1-lower/upper
    # Equivalent to sqrt(K) q^(t+1) <= eps/4, using only rationals.
    t, power = 0, q*q
    while 16*K*power > eps*eps:
        t += 1
        if max_degree is not None and t > max_degree:
            raise ValueError("Required polynomial degree exceeds the requested max_degree")
        power *= q*q
    coefficients = [Fraction(1)]
    aj = Fraction(1, 2)
    for j in range(1, t+1):
        coefficients.append(-aj)
        aj *= Fraction(2*j-1, 2*(j+1))

    def evaluate(x: Fraction) -> Fraction:
        z, ans = 1-x/upper, coefficients[-1]
        for coefficient in reversed(coefficients[:-1]):
            ans = coefficient + z*ans
        return ans

    R = [[evaluate(x) for x in row] for row in M]
    N = [[upper*x*x for x in row] for row in R]
    U, V = rank_factor(R)
    input_U, _ = rank_factor(M)
    r, d = len(input_U[0]), len(U[0])
    assert d <= math.comb(r+t, t)
    for i in range(len(M)):
        for j in range(columns):
            amplitude = sum((x*y for x, y in zip(U[i], V[j])), Fraction(0))
            assert amplitude == R[i][j]
            assert M[i][j] <= N[i][j] <= (1+eps)*M[i][j]
            assert upper*amplitude*amplitude == N[i][j]
    return {
        "input_rank": r,
        "dynamic_range": str(K),
        "epsilon": str(eps),
        "degree": t,
        "theoretical_factor_order_bound": math.comb(r+t, t),
        "returned_factor_order": d,
        "approximant": [[str(x) for x in row] for row in N],
        "row_factors": [{"weight": str(upper), "vector": [str(x) for x in row]} for row in U],
        "column_factors": [{"weight": "1", "vector": [str(x) for x in row]} for row in V],
        "factor_convention": "Each factor is weight * vector * vector^T. Pairings equal the approximant exactly.",
        "guarantee": "M <= approximant <= (1+epsilon) M entrywise, with exact rational rank-one PSD factors.",
        "scope": "This is a constructive approximation upper bound, not a minimum-rank solver.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON file containing matrix and epsilon")
    parser.add_argument("--max-degree", type=int, default=None, help="Optional explicit resource limit; no limit by default")
    args = parser.parse_args()
    try:
        with open(args.input, encoding="utf-8") as handle:
            source = json.load(handle)
        result = construct(source["matrix"], source["epsilon"], args.max_degree)
    except (OSError, KeyError, ValueError, TypeError, json.JSONDecodeError) as exc:
        parser.exit(2, f"error: {exc}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
