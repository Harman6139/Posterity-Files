# Milestone 110 — ALL admissible primal/dual peeling depths are attainable for EVERY harmonic valuation vector, with linear nullity overhead

**2026-11-08. Fully proved dimension-independent theorem, checked exhaustively on every strict harmonic graph with up to five internal vertices.** This is a strong uniform version of Milestone 109: it realizes not just the TWO bounds L(w), U(w), but **EVERY integer in between**, preserving the entire rational value vector and the designated sharp exponent. It does **NOT** yet give a fixed-nullity theorem; up to 2h new positive null coordinate clones may be used to resolve edge collisions.

## Precise theorem

Let h>=1, k=h+1, and fix any strict rational harmonic midpoint system
\[
0=w_0<w_1<\cdots<w_h<w_k=1,\qquad
2w_i=w_{a_i}+w_{b_i},\quad 0\le a_i<i<b_i\le k.
\]
Fix any admissible leading full-matrix exponent \(\alpha=w_v/2\le w_1\), \(1\le v\le k\). Let L(w) and U(w) be the universal original-kernel primal forced-survivor and dual exposing-truncation integer bounds of checkpoint 99.

**Theorem.** For EVERY integer
\[
\boxed{L(w)\le d\le U(w)}
\]
there is an explicit rational finite-dimensional uniquely solvable PSD inverse problem with
- target rank one (or any prescribed positive target rank after fully measured support padding);
- exactly the SAME strict scalar Bellman/Shapley values w_i (with repeated cloned diagonal coordinates allowed);
- exact optimal full-matrix Hölder exponent \(\alpha\), against EVERY ambient PSD competitor;
- **exact MINIMAL singularity degree d**, with a specified grouped exposing schedule;
- target nullity at most \(3h+1=3k-2\).

The construction uses one tight harmonic parent mode and at most one tied release edge plus at most one independent safe blocking mode at each internal vertex. Each additional edge is placed on a unique newly cloned positive parent coordinate, ensuring globally distinct edges and preserving the exact same scalar weights and exposing times.

In particular, the formerly conjectural interval-filling principle is **now proved if a controlled linear increase in nullity is allowed**, for each individual harmonic weight vector. The remaining all-n original problem is to replace these virtual parent clones by a construction at the original nullity k (or to show that another harmonic vector with the same exponent avoids them).

## Part I. A complete local integer transition interval

For each j=1,...,k-1 put
\[
\ell(j)=\#\{1\le i<j:2w_i<w_{j+1}\},\qquad
p(j)=\min\{1\le i\le j:2w_i>w_j+w_{i-1}\},\quad
u(j)=p(j)-1.
\]
Then
\[
\boxed{0\le\ell(j)\le u(j)\le j-1.}
\tag{110.1}
\]
**Proof of the nontrivial inequality:** If i satisfies \(2w_i<w_{j+1}\), take its tight harmonic parents \((a_i,b_i)\). Since \(w_{b_i}=2w_i-w_{a_i}\le2w_i<w_{j+1}\), one has \(b_i\le j\). Therefore
\[
2w_i=w_{a_i}+w_{b_i}\le w_{i-1}+w_j.
\]
This holds for every i≤ℓ(j) because the strict inequalities form an initial prefix. Hence none of i≤ℓ(j) satisfies the strict condition defining p(j), so p(j)>ℓ(j). Also p=j always satisfies \(2w_j>w_j+w_{j-1}\). QED.

Both \(\ell(j)\) and \(u(j)\) are nondecreasing in j: the threshold \(w_{j+1}\) rises in ℓ, and the inequality \(2w_i>w_j+w_{i-1}\) becomes harder as j grows, so the first satisfying index p(j) cannot decrease.

## Part II. A rigorous NO-GAP PATH-LENGTH LEMMA

Define a directed acyclic interval graph on vertices 0,1,...,k-1: for every j>=1 one may make a transition
\[
\boxed{j\longrightarrow q,\qquad \ell(j)\le q\le u(j).}
\tag{110.2}
\]
Let T(j) be the set of lengths of all directed paths from j to 0; T(0)={0}.

**Lemma.** For EVERY j, T(j) is an interval of consecutive integers. In fact
\[
\boxed{
T(j)=\{\mathfrak l(j),\mathfrak l(j)+1,\ldots,\mathfrak u(j)\},
}
\]
where \(\mathfrak l(j)=1+\mathfrak l(\ell(j))\) and \(\mathfrak u(j)=1+\mathfrak u(u(j))\), with both zero at j=0. The min and max functions are nondecreasing in j.

**Proof:** Induct on j. Assume the result for all q<j, and assume their min/max endpoints are nondecreasing in q. Then
\[
T(j)=1+\bigcup_{q=\ell(j)}^{u(j)}T(q).
\]
Adjacent intervals \(T(q)\) and \(T(q+1)\) cannot leave a missing integer: because \(\ell(q+1)\le q\), the induction and monotonic minimum imply
\[
\min T(q+1)
=1+\min T(\ell(q+1))
\le1+\min T(q)
\le1+\max T(q).
\]
Their other endpoints are nondecreasing, so the union of consecutive T(q)'s is again one integer interval. Its smallest/largest endpoints are attained at q=ℓ(j) and q=u(j) by monotonicity. Since ℓ(j),u(j) themselves are nondecreasing with j, the new min/max endpoints remain nondecreasing, completing the induction.

At the full graph, the very first facial step removes the terminal k and reaches prefix k−1. Therefore allowable TOTAL schedule lengths are \(1+T(k-1)\), a contiguous integer interval. Its minimum and maximum follow the deterministic original-kernel recurrences L(w) and U(w) (choose ℓ or u at each transition). Hence EVERY integer d between L(w) and U(w) has an explicit prefix schedule
\[
k=j_0>j_1=k-1>j_2>\cdots>j_d=0
\]
whose transitions satisfy \(\ell(j_{t-1})\le j_t\le u(j_{t-1})\).

## Part III. Realize ANY such schedule by one safe blocker and one tied release per vertex

Fix one of those schedules and let each internal vertex i have exposure time \(t(i)\in\{2,\ldots,d\}\), determined by
\[
j_{t(i)}<i\le j_{t(i)-1}.
\]
At vertex i with t=t(i), take its given TIGHT parent pair \(P_i=(a_i,b_i)\) and define two extra parent pairs:
\[
\boxed{
B_i=(i-1,j_{t-2})
\qquad\text{and}\qquad
R_i=(0,j_{t-1}+1).
}
\tag{110.3}
\]
The index j_(t−2) is the largest vertex removed in the PREVIOUS exposure stage, and j_(t−1)+1 is its smallest removed vertex; both are greater than i. Hence the ordered-parent restrictions \(a<i<b\) hold.

**Bellman inequalities:**
- \(B_i\) is SAFE: \(w_{i-1}+w_{j_{t-2}}\ge2w_i\). For t=2 this follows from the tight harmonic parents and \(j_0=k\). For t>=3 it follows because i survives the previous stage \(j_{t-2}\to j_{t-1}\) and \(j_{t-1}\le u(j_{t-2})\); hence \(i<p(j_{t-2})\), which is exactly \(2w_i\le w_{i-1}+w_{j_{t-2}}\).
- \(R_i\) is RELEASE (weakly unsafe): \(w_{j_{t-1}+1}\le2w_i\). The selected stage removes i with \(i>j_t\ge\ell(j_{t-1})\); the defining threshold and harmonic adjacent-spacing imply the stated inequality, including i=j_(t−1).

At child i retain one mode with tight edge P_i together with the TIED release edge R_i (omit a duplicate if equal). Its mode's MAX of parent midpoint values remains exactly w_i. Add a second, independent mode on safe edge B_i when \(B_i\ne P_i\). Thus the MIN-over-modes Shapley value remains w_i exactly.

**Exact exposing schedule, independent of coefficients:** At its appointed stage t, both B_i and R_i have a higher endpoint removed in stage t−1. The independent safe mode is inactive, and the tied tight mode is inactive because R_i touches a removed endpoint. Hence the entire desired layer \(C_t=\{j_t+1,\ldots,j_{t-1}\}\) can be removed in one PSD stress.

Conversely, at any earlier stage s<t, the higher endpoint j_(t−2) of B_i remains in the face, and so does its lower parent i−1; the release endpoint j_(t−1)+1 also remains. If the independent B_i mode is present, its active lower-parent dependency prevents i from being exposed ahead of time. If B_i=P_i and no separate mode is present, the TIED base mode is still active and ALL its edges have lower parents below i, also preventing early exposure. Formally, in any putative larger exposing set choose the SMALLEST vertex from a later layer; the active blocker forces a still smaller vertex (or the source) into that set, a contradiction. Thus no later-layer vertex can join C_s, which is therefore the **maximal** exposable set. The canonical greedy peeling stages are exactly \(C_1,\ldots,C_d\).

This proves the desired schedule within the abstract globally edge-disjoint tied-game rule, once collisions are resolved.

## Part IV. Resolve ALL edge collisions by ≤2h coordinate clones

A strict scalar graph has h+1 positive vertices (h internals plus terminal). The two extra parent pairs B_i,R_i may coincide with another child's base edge, with each other, or even (when i=1) with the optional leading source edge. To make EVERY physical offdiagonal edge unique without changing its scalar midpoint weights, do the following:

For every i whose R_i differs from P_i, add ONE fresh clone of its HIGHER parent vertex \(j_{t-1}+1\), and place R_i on the new clone rather than on its original representative. If B_i differs from P_i, add another fresh clone of its HIGHER parent \(j_{t-2}\), and place B_i on that new clone. Give every new clone the same diagonal variable and valuation weight as the original vertex. Each clone is uniquely associated to ONE additional edge, so the physical edges are globally distinct from all base edges, from one another and from the optional independent leading edge (which uses original representatives). The higher endpoint is always a positive null vertex, never the target source.

At most TWO clones per internal vertex are added:
\[
\boxed{\nu_{\mathrm{constructed}}
 \le(h+1)+2h=3h+1.}
\]
The vertex-blow-up theorem (checkpoint 52) and its tied-game extension (checkpoint 83) prove that the full-matrix global recovery exponent, the scalar Shapley vector and the exact GROUPWISE exposing layers survive this cloning. Each eligible vertex group is exposed in its entirety by a PSD stress with strongly graded positive clone diagonals; no arbitrary stress can expose a clone of an ineligible vertex prematurely. The independent leading edge is realized on original representatives, and its collision with a BASE harmonic edge is impossible when alpha<w1 (otherwise a child would have weight alpha<w1).

Take a sufficiently small positive rational coefficient λ on each generator's offdiagonal edges, and let L be Frobenius orthogonal projection to K⊥. Each generator has a clone-diagonal sum minus its trace at source, so identity and terminal diagonal are measured. The global PSD upper estimate and matching diagonally-dominant strictly PD monomial curve in checkpoint 74/83 give the desired unique PSD recovery and exact alpha. Hence the exposing schedule's minimal degree is exactly the prescribed d. QED.

## Computational validation

The complete standard-library Fraction checker in checkpoint 111:
- enumerates all (h!)² harmonic parent graphs with h=1,...,5 internal vertices;
- retains every strict rational solution (counts 1,3,18,165,2099);
- computes EVERY directed schedule path with transitions (110.2);
- checks no missing depth between L and U;
- checks BOTH arithmetic inequalities for every construction edge (110.3);
- independently runs the exact tied-game AND/OR greedy exposing closure, confirming the ENTIRE desired layer partition.
It processed exactly **5,833 schedules** at h=5, with ZERO counterexamples. The proof itself applies for arbitrary h, and all values are rational.

## What remains genuinely OPEN

1. This theorem settles the strongest "all depths between L and U" schedule conjecture **when a linear nullity overhead is allowed** and when one starts from ANY fixed strict harmonic vector.
2. It is NOT a fixed-original-dimension realization: \(3h+1\) null dimensions may be needed instead of \(h+1\). A rational family of matrix kernels permitting *shared* physical parent edges, a dimension-preserving choice of alternative harmonic weights, or a new signed/determinantal mechanism is necessary to eliminate the clones.
3. The earlier single-edge interpolation lemma is FALSE (checkpoint107): one action can jump degree by two. The proof here succeeds by designing the entire target exposing schedule **simultaneously**, rather than interpolating generators sequentially.
4. The user-requested full all-nullity fixed-(n,r,d,alpha) arithmetic classification and exact arbitrary rank-profile spectra remain UNPROVED. This milestone eliminates the combinatorial path-length gap but isolates the specific **edge-collision/dimension** obstruction.

**Novelty / audit:** Standard facial reduction, stochastic Bellman games and PSD diagonal normalization are prior ingredients; all new closure/path/schedule claims have direct proofs and exact tests. They require independent referee review before journal novelty claims.