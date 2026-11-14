#!/usr/bin/env python3
"""Exact illustrations of Milestone 25, using only the standard library.

All-dimensional claims are proved in the manuscript. Small graph checks use the
weaker sufficient half-degree 4*n*n*(n+1), not the much larger production p(n),
so they test the same inequalities without generating enormous rationals.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product
from math import comb
import json


def validate_graph(n: int, edges: list[tuple[int, int]]) -> None:
    if n < 2 or len(set(edges)) != len(edges):
        raise ValueError("Require n>=2 and distinct edges.")
    if any(not (0 <= i < j < n) for i, j in edges):
        raise ValueError("Edges must satisfy 0<=i<j<n.")


def production_half_degree(n: int) -> int:
    if n < 2:
        raise ValueError("n must be at least two")
    target = (1 << 16) * n**4
    return 1 << (target - 1).bit_length()


def cut_histogram(n: int, edges: list[tuple[int, int]]) -> list[int]:
    validate_graph(n, edges)
    hist = [0] * (len(edges) + 1)
    for s in product((-1, 1), repeat=n):
        hist[sum(s[i] != s[j] for i, j in edges)] += 1
    return hist


def graph_query(n: int, edges: list[tuple[int, int]], k: int) -> list[Fraction]:
    validate_graph(n, edges)
    m = len(edges)
    if not (m > 0 and m / 2 < k <= m):
        raise ValueError("Use a nontrivial threshold m/2<k<=m.")
    h = 2 * k - 1
    edge_set = set(edges)
    return ([Fraction(m, h)] + [Fraction(0)] * n
            + [Fraction(-int((i, j) in edge_set), h)
               for i, j in combinations(range(n), 2)])


def moment_from_histogram(hist: list[int], exponent: int, shift: int = 0) -> int:
    if exponent < 0 or exponent % 2:
        raise ValueError("Use a nonnegative even exponent.")
    return sum(count * (shift + 2 * j)**exponent
               for j, count in enumerate(hist))


def query_value(n: int, edges: list[tuple[int, int]], k: int, p: int) -> Fraction:
    """Exact P value at the Max-Cut query, at a specified half-degree p."""
    if p < 1:
        raise ValueError("p must be positive")
    x = graph_query(n, edges, k)
    hist = cut_histogram(n, edges)
    h = 2*k - 1
    return sum(t*t for t in x)/(4*len(x)) + Fraction(
        moment_from_histogram(hist, 2*p), h**(2*p))


def recover_counts(moment_value: int, radix: int, exponent: int, m: int) -> list[int]:
    """Recover the cut histogram from one radix-encoded moment evaluation."""
    if radix < 2 or exponent < m or exponent % 2 or m < 0:
        raise ValueError("Invalid radix, degree or edge count")
    mu = []
    for j in range(m+1):
        digit = (moment_value // radix**(exponent-j)) % radix
        divisor = comb(exponent, j) * (2**j)
        quotient, remainder = divmod(digit, divisor)
        if remainder:
            raise ValueError("Moment digits are inconsistent with the model")
        mu.append(quotient)
    counts = []
    for t in range(m+1):
        coeff = [Fraction(1)]
        for v in range(m+1):
            if v == t:
                continue
            new = [Fraction(0)] * (len(coeff)+1)
            for j, c in enumerate(coeff):
                new[j] -= c * Fraction(v, t-v)
                new[j+1] += c * Fraction(1, t-v)
            coeff = new
        count = sum(c*a for c, a in zip(coeff, mu))
        if count.denominator != 1 or count < 0:
            raise ValueError("Reconstruction was not a nonnegative integer")
        counts.append(count.numerator)
    return counts


def encode_histogram(n: int, hist: list[int], exponent: int) -> tuple[int, int]:
    m = len(hist)-1
    if exponent < m or exponent % 2:
        raise ValueError("Need an even exponent >= edge count")
    radix = 1 << (n + exponent*(2*m).bit_length() + 2)
    return moment_from_histogram(hist, exponent, radix), radix


def modular_cancellation_demo(squarings: int = 200) -> Fraction:
    """Evaluate (1/3)^(2^s)-(1/3)^(2^s)+(7/5)^2 without huge intermediates."""
    if squarings < 0:
        raise ValueError("Negative number of squarings")
    G, q, H1 = 3, 5, 20
    D0 = G * q**2
    modulus = 1 + (1 << (H1+2))*G*q
    huge = pow(3, -1, modulus)
    for _ in range(squarings):
        huge = huge*huge % modulus
    x = 7*pow(5, -1, modulus) % modulus
    output = (huge-huge+x*x) % modulus
    numerator = output*D0 % modulus
    if numerator > modulus//2:
        numerator -= modulus
    return Fraction(numerator, D0)


def run_checks() -> dict:
    graph_count = query_count = count_checks = 0
    for n in range(2, 5):
        possible = list(combinations(range(n), 2))
        p = 4*n*n*(n+1)
        D = 1+n+len(possible)
        assert Fraction(2**n)*(1-Fraction(7, 8*n*n))**(2*p) <= Fraction(1,4)
        assert production_half_degree(n) >= p
        for mask in range(1 << len(possible)):
            edges = [e for j, e in enumerate(possible) if mask >> j & 1]
            hist = cut_histogram(n, edges)
            graph_count += 1
            m = len(edges)
            exponent = max(2, m + m % 2)
            value, radix = encode_histogram(n, hist, exponent)
            assert recover_counts(value, radix, exponent, m) == hist
            count_checks += 1
            if not m:
                continue
            maximum = max(j for j, c in enumerate(hist) if c)
            for k in range(m//2+1, m+1):
                x = graph_query(n, edges, k)
                assert len(x) == D and sum(t*t for t in x) <= 2
                h = 2*k-1
                for signs in product((-1,1), repeat=n):
                    w = (1, *signs, *(signs[i]*signs[j] for i,j in possible))
                    pairing = sum(a*b for a,b in zip(x,w))
                    cut = sum(signs[i] != signs[j] for i,j in edges)
                    assert pairing == Fraction(2*cut,h)
                val = query_value(n, edges, k, p)
                if maximum >= k:
                    assert val >= 2
                    assert Fraction(1, h*n) > Fraction(1,n**3)
                else:
                    assert val <= Fraction(1,2)
                query_count += 1
    assert modular_cancellation_demo() == Fraction(49,25)
    return {
        "graphs_checked": graph_count,
        "promised_gap_queries_checked": query_count,
        "single_evaluation_histograms_recovered": count_checks,
        "graph_orders": [2,3,4],
        "gap_test_half_degree": "4*n^2*(n+1), a proved sufficient weaker value",
        "production_half_degree": "least power of two >= 2^16*n^4",
        "modular_cancellation_squarings": 200,
        "modular_exact_output": "49/25",
        "scope": "Exact finite illustrations only. Universal results are the analytic proofs in milestone 25. The full succinct fixed-error smooth-body target is NOT proved."
    }


if __name__ == "__main__":
    print(json.dumps(run_checks(), indent=2))
