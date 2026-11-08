# Milestone 59 — dual Bellman–tropical fixed points determine exact PSD exponent and exposing times

**2026-11-08, PROVED for all finite multiaction midpoint-incidence PSD systems with distinct action edges and strictly increasing rational Bellman values.** This theorem sharpens checkpoint 57 by replacing iterative set-valued exposing closure with a **single monotone integer fixed point**. It gives a rigorous structural explanation of why non-optimal actions can change facial degree without changing the sharp exponent. This is not (yet) a necessity theorem for arbitrary dense measurement kernels.

## Definitions

Let vertices be source O=0, internals 1,...,h and terminal T=h+1. Internal vertex i has a nonempty action set A_i of parent pairs (a,b) with 0<=a<i<b<=T. Each action edge is globally unique; the optional leading source-to-target vertex edge is distinct from the action edges. The real PSD pencil, measurements, and unique rank-one target are exactly as in checkpoint 57.

The **primal fractional Bellman value** w is the unique solution
    w_O=0, w_T=1, w_i=min_{(a,b)∈A_i} (w_a+w_b)/2.
Assume 0<w_1<...<w_h<1. By checkpoint 57, the exact full-PSD recovery exponent is min(w_1,w_v/2 if there is an optional source-to-v edge).

Define the **tropical exposing-time operation** on integers >=1 plus infinity by
    τ(a,b)=a  if a=b,
    τ(a,b)=min(a,b)+1 if a≠b;
    τ(infinity,b)=b+1 for finite b,
    τ(infinity,infinity)=infinity.
For any integer vector t with t_O=infinity,t_T=1, define
    (\mathcal T t)_i=max_{(a,b)∈A_i} τ(t_a,t_b)  (1<=i<=h).
Starting with t_i^(0)=1 for all internal i, iterate
    t^(k+1)=\mathcal T t^(k).
(The boundary times remain fixed.)

## Theorem A — exposing time equals the LEAST tropical fixed point

The iteration is pointwise nondecreasing and stabilizes after finitely many integer steps to an integer vector t* with 2<=t*_i<=h+1. If C_j={i: t*_i=j}, together with the terminal in C_1, then:
- C_1,...,C_d are exactly the **canonical maximum-rank PSD exposing layers** of checkpoint 57;
- the exact minimal facial degree is d=max_i t*_i;
- its exact rank-drop profile is (|C_1|,...,|C_d|).
In particular the entire facial-reduction invariant is computed by **finite max/min integer arithmetic**, with no SDP solver.

### Proof

1. The operation τ(a,b) is nondecreasing in each argument, including infinity. Thus \mathcal T is monotone. Since all internal coordinates start at 1 and \mathcal T(1)_i>=1, its iterates are pointwise nondecreasing.

2. A finite stage assignment t with t_O=infinity,t_T=1 is a valid **all-actions closed exposing schedule** iff, for every vertex i and every action (a,b)∈A_i,
   t_i>=τ(t_a,t_b).
Indeed, if i is exposed at stage t_i while both parents are still present, then they must be exposed at that *same* stage; this is equivalent to the displayed inequality. Conversely, the inequality guarantees that whenever both parents remain at the start of stage t_i, their times equal t_i, so the stage is exposing-closed. The exact stress existence theorem in checkpoint 57 realizes every such closed stage.

3. The canonical greedy peeling removes at least one non-source vertex at each step. To see this, let i be the largest-index remaining non-source vertex: all its action higher-index parents b>i have already been exposed, so i is individually eligible. Thus every vertex is exposed by stage h+1. Let t^g be its stage vector. It satisfies t^g_i>=\mathcal T(t^g)_i for each i.

4. Since t^(0)<=t^g and \mathcal T is monotone, every iterate t^(k)<=t^g<=h+1. The integer sequence stabilizes after finitely many steps at a fixed point t*. Such a fixed point defines a valid all-actions closed schedule by item 2. Since greedy peeling produces the earliest cumulative exposing support at each stage, t^g<=t*. Therefore t*=t^g, proving the theorem. The maximal-rank greedy rule gives minimal facial degree, and the layer cardinalities are the exact exposed ranks. QED.

**Subtlety:** The number of fixed-point iterations may exceed d because cycles in the parent-action dependency graph can propagate time updates through several passes; finite termination, not an O(d) iteration count, is asserted. The potential sum_i(t_i-1) increases in each strict pass and is bounded by h².

## Theorem B — positive slack actions preserve the sharp exponent and weakly delay exposing times

Suppose an additional previously unused action (a,b) at i satisfies
    (w_a+w_b)/2 >= w_i
for the existing strictly ordered Bellman values. Then the old value vector w remains a fixed point of the *new* Bellman operator (the minimum now includes one additional value at least the old minimum). By uniqueness of the proper finite Bellman system, the new sharp recovery exponent is unchanged.

On the tropical side, the new operator \mathcal T' takes the maximum over *more* actions, so \mathcal T't>=\mathcal T t pointwise for every t. Starting both from the same all-ones vector and iterating monotonically gives
    t_i^*(new)>=t_i^*(old)
for every vertex. Thus additional slack actions cannot make any vertex **earlier** to expose. They may strictly increase its time, or make previously simultaneous vertices expose in separate steps; the total singularity degree may increase.

This is a clean, exact **primal–dual asymmetry**:
  primal α is governed by a MIN of midpoint averages;
  dual facial time is governed by a MAX of τ-values.
An action can be inactive for the primal optimal exponent and simultaneously active in delaying the dual exposures.

## Example

The six-by-six example of checkpoint 58 has Bellman weights
    (1/4,7/16,1/2,5/8,1)
and optional leading edge (0,2), giving exact sharp exponent 7/32. With the four base actions only, tropical times are (3,3,2,2,1), degree three. Adding the slack action (2,4) at internal vertex 3 makes times (4,3,3,2,1), degree four, even though (w_2+w_4)/2=17/32>w_3=1/2. The complete full-PSD upper and lower bounds and exact facial stresses are proved in checkpoint 58.

## Exact finite audit

A standalone Fraction/integer script reproduces this recurrence for **all 17,169 collision-free h=4 multiaction action sets**, and for all **24,821** one-safe-extra-action variations of strict h=5 graphs. Each tropical time vector agrees with an independent direct maximal exposing-closure implementation. The calculations are reproducibility checks, not substitutes for the proof.

## Scope and novelty

The theorem is exact for arbitrary finite action sets in the explicit incidence class, and its rank profiles are *minimal facial ranks*, not merely scheduling analogies. It does not assert that every arbitrary dense measurement kernel admits such a fixed point representation without real-algebraic coefficients. Stochastic shortest-path Bellman equations, tropical min/max operations and facial reduction are prior methods; bibliographic priority of this exact PSD exponent/exposure-time duality requires a separate audit.