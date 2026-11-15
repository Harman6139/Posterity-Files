"""Exact definitions for Milestone 24. Standard library only.

The family is explicit coefficient-by-coefficient, NOT an efficient evaluator:
evaluation enumerates 2**n Boolean assignments and may return very large integers.
The theoretical degree is large. Use small p for diagnostic identities.
No numerical optimization or finite experiment certifies the LRS lower bound.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import combinations, product
from math import factorial
from typing import Iterator, Sequence


def coordinates(n: int) -> tuple[tuple[int, ...], ...]:
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    return ((),) + tuple((i,) for i in range(n)) + tuple(combinations(range(n), 2))


def theoretical_p(n: int) -> int:
    coordinates(n)
    lower = (1 << 16) * n**4
    return 1 << (lower - 1).bit_length()


def vectors(n: int) -> Iterator[tuple[int, ...]]:
    """Yield w(s), without storing the exponential list."""
    for s in product((-1, 1), repeat=n):
        yield (1,) + s + tuple(s[i] * s[j] for i, j in combinations(range(n), 2))


def _check_p(p: int) -> None:
    if not isinstance(p, int) or p < 2:
        raise ValueError("p must be an integer at least two")


def coefficient(n: int, alpha: Sequence[int], p: int | None = None) -> Fraction:
    """Exact monomial coefficient, using parity rather than enumeration."""
    cs = coordinates(n)
    p = theoretical_p(n) if p is None else p
    _check_p(p)
    if len(alpha) != len(cs) or any(not isinstance(a, int) or a < 0 for a in alpha):
        raise ValueError("alpha must have D nonnegative integer entries")
    degree = sum(alpha)
    if degree == 2:
        return Fraction(1, 4 * len(cs)) if max(alpha, default=0) == 2 else Fraction(0)
    if degree != 2 * p:
        return Fraction(0)
    parity = [0] * n
    for power, subset in zip(alpha, cs):
        if power & 1:
            for i in subset:
                parity[i] ^= 1
    if any(parity):
        return Fraction(0)
    denom = 1
    for power in alpha:
        denom *= factorial(power)
    return Fraction((1 << n) * factorial(2 * p) // denom)


def _point(n: int, x: Sequence[int | Fraction]) -> tuple[Fraction, ...]:
    if len(x) != len(coordinates(n)):
        raise ValueError("x must have D=1+n+binom(n,2) coordinates")
    return tuple(Fraction(a) for a in x)


def value(n: int, x: Sequence[int | Fraction], p: int | None = None) -> Fraction:
    p = theoretical_p(n) if p is None else p
    _check_p(p)
    x = _point(n, x)
    out = sum(a * a for a in x) / (4 * len(x))
    for w in vectors(n):
        ell = sum(a * b for a, b in zip(w, x))
        out += ell ** (2 * p)
    return out


def derivatives(n: int, x: Sequence[int | Fraction], p: int) -> tuple[list[Fraction], list[list[Fraction]]]:
    _check_p(p)
    x = _point(n, x)
    d = len(x)
    grad = [a / (2 * d) for a in x]
    hess = [[Fraction(i == j, 2 * d) for j in range(d)] for i in range(d)]
    for w in vectors(n):
        ell = sum(a * b for a, b in zip(w, x))
        g = 2 * p * ell ** (2 * p - 1)
        h = 2 * p * (2 * p - 1) * ell ** (2 * p - 2)
        for i in range(d):
            grad[i] += g * w[i]
            for j in range(d):
                hess[i][j] += h * w[i] * w[j]
    return grad, hess


def soc_witness(n: int, x: Sequence[int | Fraction], p: int) -> dict:
    """Exact equality choices in all repeated-square cones.

    This returns a feasible formulation witness only when value(n,x,p)<=1.
    For an infeasible point it returns the negative final slack transparently.
    """
    _check_p(p)
    if p & (p - 1):
        raise ValueError("the displayed repeated-square lift requires power-of-two p")
    x = _point(n, x)
    length = (2 * p).bit_length() - 1
    chains = []
    for w in vectors(n):
        ell = sum(a * b for a, b in zip(w, x))
        chain = []
        previous = ell
        for _ in range(length):
            previous = previous * previous
            chain.append(previous)
        chains.append(chain)
    squares = [a * a for a in x]
    slack = 1 - sum(c[-1] for c in chains) - sum(squares) / (4 * len(x))
    return {"chains": chains, "coordinate_squares": squares,
            "final_slack": slack, "feasible": slack >= 0,
            "soc_blocks": len(chains) * length + len(x)}


def metadata(n: int) -> dict:
    d = len(coordinates(n))
    p = theoretical_p(n)
    return {"n": n, "dimension": d, "p": p, "degree": 2 * p,
            "Boolean_summands": 1 << n,
            "tolerance": str(Fraction(1, (1 << 20) * n**4)),
            "soc_blocks": (1 << n) * ((2 * p).bit_length() - 1) + d,
            "evaluation_is_exponential_in_n": True,
            "polynomial_length_arithmetic_circuit_proved": False}


if __name__ == "__main__":
    import argparse
    import json
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int, nargs="?", default=4)
    args = parser.parse_args()
    print(json.dumps(metadata(args.n), indent=2))
