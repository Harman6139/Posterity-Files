#!/usr/bin/env python3
"""Exact rational construction and peeling checker for depth d>=3.

This is an exact-arithmetic *verification script*; mathematical proof is in
02_ALL_DEPTHS_INTERIOR_REALIZATION.md. No floating-point eigentests.
"""
from fractions import Fraction as F

def ladder(d, m):
    assert d >= 3 and m >= 1
    s = d - 3
    q = F(2**s, 2**s + 1)
    alpha = (1 - q**m) / (2 - q**m)
    xs = [alpha] + [1-q**i*(1-alpha) for i in range(1, m+1)]
    weight = {"O": F(0), "T": F(1), "R": alpha}
    parents = {"R": ("O", f"X{m}")}
    for i in range(1, m+1):
        u = f"X{i}"
        weight[u] = xs[i]
        previous = "R" if i == 1 else f"X{i-1}"
        if s == 0:
            parents[u] = (previous, "T")
        else:
            parents[u] = (previous, f"Y{i},1")
            for j in range(1, s+1):
                y = f"Y{i},{j}"
                weight[y] = xs[i] + (1-xs[i])/2**(s-j+1)
                parents[y] = (u, f"Y{i},{j+1}" if j < s else "T")
    assert len(set(weight.values())) == len(weight)
    for v, (a, b) in parents.items():
        assert weight[a] < weight[v] < weight[b], (v, a, b)
        assert weight[a] + weight[b] == 2*weight[v], (v, a, b)
    return alpha, weight, parents

def peel(weight, parents):
    remaining = set(weight)
    layers = []
    while remaining != {"O"}:
        candidate = remaining - {"O"}
        while True:
            forbidden = {v for v in candidate
                if v in parents
                and all(p in remaining for p in parents[v])
                and not all(p in candidate for p in parents[v])}
            if not forbidden:
                break
            candidate -= forbidden
        assert candidate
        layers.append(sorted(candidate))
        remaining -= candidate
    return layers

def check():
    for d in range(3, 10):
        last = F(0)
        for m in range(1, 7):
            alpha, weights, parents = ladder(d,m)
            assert alpha > last
            assert alpha < F(1,2)
            assert len(peel(weights,parents)) == d
            last = alpha
            print(f"d={d} m={m} alpha={alpha} nullity={len(weights)-1}")
    print("PASS: all checks exact")

if __name__ == "__main__":
    check()
