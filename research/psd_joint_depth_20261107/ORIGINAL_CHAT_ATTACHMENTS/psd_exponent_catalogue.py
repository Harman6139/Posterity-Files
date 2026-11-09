#!/usr/bin/env python3
"""Exact midpoint-network catalogue for sharp PSD recovery exponents.

Uses only Python's standard library.  All calculations use Fraction.

Examples:
  python psd_exponent_catalogue.py --nullity 4
  python psd_exponent_catalogue.py --target 2/7 --max-nullity 6
  python psd_exponent_catalogue.py --nullity 5 --json catalogue.json

The enumeration is finite but factorial: with h internal nodes it examines
(h!)^2 ordered parent assignments. It is intended for small nullities.
"""
from __future__ import annotations
import argparse
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterator

F = Fraction

def solve(a: list[list[F]], b: list[F]) -> tuple[F, ...]:
    """Exact Gaussian elimination, raising ValueError for a singular matrix."""
    n = len(b)
    rows = [list(map(F, row)) + [F(rhs)] for row, rhs in zip(a, b)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j]), None)
        if pivot is None:
            raise ValueError('Singular harmonic system')
        rows[j], rows[pivot] = rows[pivot], rows[j]
        c = rows[j][j]
        rows[j] = [v / c for v in rows[j]]
        for i in range(n):
            if i != j and rows[i][j]:
                c = rows[i][j]
                rows[i] = [x - c * y for x, y in zip(rows[i], rows[j])]
    return tuple(rows[i][-1] for i in range(n))

def networks(h: int) -> Iterator[tuple[tuple[F, ...], tuple[tuple[int, int], ...]]]:
    """Yield strictly increasing harmonic networks on vertices 0,...,h+1."""
    if h == 0:
        yield (), ()
        return
    choices = [tuple(itertools.product(range(i), range(i + 1, h + 2)))
               for i in range(1, h + 1)]
    for parents in itertools.product(*choices):
        a = [[F(0) for _ in range(h)] for _ in range(h)]
        b = [F(0) for _ in range(h)]
        for i, (lo, hi) in enumerate(parents):
            a[i][i] = F(2)
            for j in (lo, hi):
                if j == h + 1:
                    b[i] += 1
                elif j != 0:
                    a[i][j - 1] -= 1
        w = solve(a, b)
        if all(x < y for x, y in zip((F(0),) + w, w + (F(1),))):
            yield w, parents

def catalogue(nullity: int) -> dict[F, dict]:
    if nullity < 0:
        raise ValueError('Nullity must be nonnegative')
    out: dict[F, dict] = {F(1): {'minimum_nullity': 0, 'weights': [], 'parents': []}}
    for h in range(nullity):
        for w, parents in networks(h):
            minimum = w[0] if w else F(1)
            for x in w + (F(1),):
                alpha = x / 2
                if alpha <= minimum and alpha not in out:
                    out[alpha] = {
                        'minimum_nullity': h + 1,
                        'weights': [str(v) for v in w],
                        'parents': [list(p) for p in parents],
                        'leading_doubled_weight': str(x),
                        'extra_offdiagonal_variable': alpha < minimum,
                    }
    return out

def verify_witness(alpha: F, record: dict) -> None:
    if alpha == 1:
        return
    w = tuple(F(s) for s in record['weights'])
    v = (F(0),) + w + (F(1),)
    assert len(w) + 1 == record['minimum_nullity']
    assert all(x < y for x, y in zip(v, v[1:]))
    for i, (a, b) in enumerate(record['parents'], 1):
        assert a < i < b
        assert 2 * v[i] == v[a] + v[b]
    assert 2 * alpha in w + (F(1),)
    assert alpha <= (w[0] if w else F(1))

def sparse_pencil(alpha: F, record: dict) -> dict[str, list[list[F]]]:
    """Return exact coefficient matrices for a rank-one sharp realization.

    The target is E_00. Measurements are projection perpendicular to this
    pencil's span, matrix trace, and the last diagonal entry.
    """
    verify_witness(alpha, record)
    if alpha == 1:
        return {'x0': [[F(1)]]}
    w = tuple(F(s) for s in record['weights'])
    n = len(w) + 2
    lam = F(1, 2*n)
    def zero(): return [[F(0) for _ in range(n)] for _ in range(n)]
    result = {}
    for i in range(n):
        result[f'x{i}'] = zero()
        result[f'x{i}'][i][i] = F(1)
    for i, (a,b) in enumerate(record['parents'], 1):
        result[f'x{i}'][a][b] = result[f'x{i}'][b][a] = lam
    if alpha not in w:
        j = ((F(0),) + w + (F(1),)).index(2*alpha)
        result['z'] = zero()
        result['z'][0][j] = result['z'][j][0] = lam
    return result

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--nullity', type=int, default=4)
    parser.add_argument('--target', type=F)
    parser.add_argument('--max-nullity', type=int, default=6)
    parser.add_argument('--json', type=Path)
    args = parser.parse_args()
    nu = args.max_nullity if args.target is not None else args.nullity
    if nu < 0:
        parser.error('Nullity must be nonnegative')
    if nu > 7:
        parser.error('This reference enumerator limits nullity to 7; its cost is factorial.')
    out = catalogue(nu)
    for alpha, rec in out.items(): verify_witness(alpha, rec)
    if args.target is not None:
        if args.target not in out:
            print(f'{args.target}: not realizable at nullity <= {nu}')
        else:
            record = out[args.target]
            print(f'{args.target}: minimum nullity {record["minimum_nullity"]}')
            print(json.dumps(record, indent=2))
    else:
        print(f'Nullity <= {nu}: {len(out)} exponents')
        print(', '.join(map(str, sorted(out))))
    if args.json:
        args.json.write_text(json.dumps({str(a): out[a] for a in sorted(out)}, indent=2) + '\n')

if __name__ == '__main__':
    main()