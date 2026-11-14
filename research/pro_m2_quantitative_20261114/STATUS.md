# PROVED / NOT ESTABLISHED

## Proved in the manuscript

1. The proposed polynomial adjacent-pivot theorem is false for the canonical start: a rational O(log N)-bit nonmember forces exactly N adjacent pivots, without degeneracy or ties. Its exact distance is (sqrt(1+N^-2)−1)/4. The least-grid correction rule makes N−1 pivots; every admissible-grid version makes at least N−1.
2. Every Ryshkov point P with ||P||_F<=M has orthant quadratic margin at least 1/[2n ceil(sqrt(4nM))^(2(n−1))]. The exponent n−1 and the associated active-vector height exponent (n−1)/2 are sharp among perfect matrices in every order.
3. An explicit quantitative version holds for finitely generated rational cones, with a bound in their integer generator heights and span dimension.
4. The canonical minimum-ratio shadow procedure has an explicit finite arithmetic implementation, including degeneracies, boundary copositivity tests, and exact neighbors. Its worst-case pivot count is at most 2^{O(n^4(h+log n))}, its visited-object bit heights are O(n^7(H+log n)), and its total bit cost is at most 2^{O(n^7(H+log n))}. The manuscript also gives finite formulas rather than only asymptotic notation.
5. A nonlocal rational separator has a conservative O(2^n n^24 B^6) bit bound, where B=L+h+ceil(log2(n+1))+4. It returns an explicit strict cone margin and negative target margin. This is a complete classical-architecture replacement, not a new claim that fixed-dimensional separation is polynomial.

## Actually executed

Eight exact test groups passed. Generic adjacent paths were executed for N=1,2,3,5,8. A five-dimensional nonlocal run returned after 85 center tests, with epsilon=1/2560 and a 31-support rational certificate. A separately implemented checker verified it and rejected four corrupted versions. Formula checks at N=2^100 are not a full pivot simulation.

## Not established; do not claim

- A polynomial bound for the stated adjacent rule: it is disproved, not merely unproved.
- An exponential lower bound after doubly nonnegative preprocessing. The lower-bound inputs here are indefinite.
- A new polynomial general separation paradigm, a polynomial algorithm in variable dimension, or a new universal rational boundary CP-factorization theorem.
- Optimal dependence on dimension in the runtime estimates.
- A polynomial nonlocal perfect-matrix jump algorithm.
- Independent historical priority of the precise new results; binary Farey paths and qualitative Diophantine IR arguments have close antecedents.
- Completion of the required full-proof ten-paper-per-venue comparison, an 8/10 comparative pass, or an 80th-percentile quality certification.
- Independent human or proof-assistant verification, or guaranteed editorial handling times.

The mathematical negative answer and quantitative replacements are delivered. The user's entire flagship success criterion, which additionally requires a defensible upper-quintile comparison, is not claimed satisfied.
