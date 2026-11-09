# Milestone 107 — one Bellman-nonimproving edit can jump TWO minimal PSD facial steps

**2026-11-08. PROVED for explicitly specified sparse real PSD problems.** This rules out a tempting proof by adding or deleting one action at a time and assuming its degree changes by at most one. It does NOT refute the all-nullity sufficiency conjecture.

## Exact increase from three to five

On S^7 index vertices 0 (source), 1,...,5 (internal), 6 (terminal), put target X*=E00, lambda=1/100, with kernel generators H_i=Eii−E00+lambda F_(a_i,b_i), parent policy

    P=((0,2),(0,6),(2,4),(3,5),(4,6)).

Add an independent leading G=lambda F01. Measurements are orthogonal projection onto K-perp. The strict harmonic weights are

    w=(0,1/4,1/2,5/8,3/4,7/8,1).

The sharp full ambient PSD recovery exponent is alpha=1/8 from the independent source-to-vertex-1 edge; all other internal weights are >=1/4. The exact greedy maximal exposing layers are

    ({6},{2,3,4,5},{1}), degree 3.

Now add ONE new independently controlled generator

    J2=E22−E00+lambda F14.

Its parent average (w1+w4)/2=1/2 equals w2, so it is Bellman-tied and leaves the entire strict w vector and alpha unchanged. All parent edges remain distinct, including G. But the new exact greedy exposing layers are

    ({6},{5},{4},{2,3},{1}), degree 5.

Therefore a SINGLE Bellman-nonimproving generator has increased the TRUE minimal facial-reduction degree by TWO. The global full PSD recovery/exposing equivalences are proved for these incidence systems in checkpoints 57 and 74, not assumed from a purely abstract schedule.

## Exact decrease from five to three

Take instead base policy

    P'=((0,2),(1,4),(2,5),(3,5),(4,6))

with weights

    w'=(0,3/11,6/11,8/11,9/11,10/11,1).

Add the same independent G=lambda F01. The sharp exponent is alpha=3/22 and the greedy exposing layers are

    ({6},{5},{3,4},{2},{1}), degree 5.

REPLACE just the vertex-2 generator

    E22−E00+lambda F14

by ONE tied-edge generator

    E22−E00+lambda(F14+F06).

The new (0,6) edge has midpoint average 1/2 < w2=6/11. The Shapley MAX over the tied mode still equals 6/11; consequently all weights and alpha remain fixed. Its edge is disjoint from all other edges. Yet greedy exposing layers become

    ({6},{2,3,4,5},{1}), degree 3.

One tied-edge modification DECREASES minimum facial degree by TWO.

## General obstruction to elementary interpolation

Adding a parent action can propagate a delay through a whole cycle of the least integer exposing-time fixed point. Tying a subleading edge into a generator can disable an entire constraint after an earlier facial step, releasing several vertices at once. Thus the proposed lemma "one permissible action changes singularity degree by at most one" is FALSE in both directions.

This does not disprove the conjecture that every integer d between the universal original-kernel bounds L(w) and U(w) is attainable: it shows an induction must exploit GLOBAL reconfiguration, not a one-edge Lipschitz bound.

## Infinite suspension

Replace terminal T with an internal vertex whose parents are (0,Tnew), introducing a new measured terminal Tnew; repeat m times. All old weights are divided by 2, and the new terminal contributes one extra exposing step while retaining the old difference of TWO. For every m>=0 the increased-degree pair has exponent 2^(-m-3), degrees m+3 versus m+5. The tied-release pair has exponent 3/(22*2^m), degrees m+5 versus m+3. These are finite rational PSD examples in arbitrarily high dimension.

## Audit and limitations

The companion checkpoint 108 exact Fraction program directly recomputes both rational harmonic systems, verifies each extra edge's Bellman inequality and all four exact exposing layer partitions. The analytic PSD recovery and exposing correspondence is provided in 57/74.

This is a verified negative finding with immediate relevance to the global sufficiency proof strategy. Bibliographic priority is not checked.