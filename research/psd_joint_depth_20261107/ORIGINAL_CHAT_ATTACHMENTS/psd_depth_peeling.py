#!/usr/bin/env python3
"""Exact facial-peeling degree of sparse harmonic PSD-network pencils.

Network vertices: 0(source), 1..h(internal), h+1(terminal).
Parents are ordered a(i)<i<b(i), and internal weights obey midpoint equations.
The associated PSD measurement problem is the sparse construction in
Sharp_PSD_Stability_Weighted_Flags_Memorandum.md, Section 5.
"""
from __future__ import annotations
from fractions import Fraction
from psd_exponent_catalogue import networks


def peel(parents):
    h = len(parents)
    terminal = h+1
    removed = set()
    layers = []
    while len(removed)<h+1:
        current = set(range(h+2))-removed
        candidates = current - {0}
        while True:
            bad = set()
            for i in candidates:
                if i==terminal:
                    continue
                a,b=parents[i-1]
                if a in current and b in current and not ({a,b}<=candidates):
                    bad.add(i)
            if not bad:
                break
            candidates-=bad
        if not candidates:
            raise AssertionError('No exposing stress, contradicts uniqueness')
        layers.append(tuple(sorted(candidates)))
        removed |= candidates
    return layers


def example_stats(max_h=4):
    stats={}
    examples={}
    for h in range(max_h+1):
        for weights,parents in networks(h):
            p=peel(parents)
            w0=weights[0] if weights else Fraction(1)
            for t in weights+(Fraction(1),):
                a=t/2
                if a<=w0:
                    stats[(a,len(p))] = stats.get((a,len(p)),0)+1
                    examples.setdefault((a,len(p)),(weights,parents,p))
    return stats,examples

if __name__=='__main__':
    stats,examples=example_stats(4)
    for alpha in [Fraction(1,2),Fraction(1,3),Fraction(1,4),Fraction(2,7),Fraction(3,8),Fraction(1,8)]:
        print('alpha:',alpha)
        for (a,d),count in sorted(stats.items()):
            if a==alpha:
                print('  depth',d,'networks',count,'witness',examples[(a,d)])
    print('All distinct (alpha,degree) for nullity<=5:',len(stats))