# Milestone 66 — INFINITE family requiring two-action midpoint geometry: exponent 7/2^nu at depth nu−1

**2026-11-08. FULLY PROVED.** For every target nullity nu>=5 there exists an explicit finite-dimensional uniquely solvable real PSD inverse problem with a rank-one target, sharp full-matrix exponent alpha=7/2^nu and minimal facial-reduction degree exactly d=nu−1. **No** single-action strict harmonic midpoint network of that nullity, even with vertex blow-ups, realizes that exponent–depth pair. This converts the six-by-six example from checkpoint 58 into an infinite structural separation and proves a useful general combinatorial rigidity lemma for all maximal-denominator dyadic fractions.

The theorem is about *the insufficiency of single-action normal forms*, not a claim that all arbitrary dense kernels reduce to two-action graphs.

## Part I — explicit two-action construction at every nullity

Let nu=5+ell, ell>=0, h=nu−1=4+ell, with vertices 0 (source), 1,...,h (internal), T=h+1 (terminal). Assign these action sets:
\[
\begin{aligned}
A_1&=\{(0,3)\},\\
A_2&=\{(1,4)\},\\
A_3&=\{(0,5),(2,4)\},\\
A_4&=\{(1,5)\},\\
A_j&=\{(0,j+1)\}\quad(5\le j\le h).
\end{aligned}
\]
Add an independent source-to-vertex-2 leading edge (0,2). All unordered action edges are distinct, as is this leading edge. Fix lambda=1/[100(1+nu)] and construct the linear PSD kernel pencil with action generators
    H_(i,a,b)=E_ii-E_00+lambda F_ab,
an optional G=lambda F_02, target X*=E00, and measurements the Frobenius orthogonal projection onto the kernel complement, exactly as in checkpoint 57.

The unique controlled harmonic value vector is STRICT and rational. Its first four entries are
\[
w_1=2^{-(\ell+2)},\quad
w_2=7\,2^{-(\ell+4)},\quad
w_3=2^{-(\ell+1)},\quad
w_4=5\,2^{-(\ell+3)}.
\]
For j>=5 one has w_j=2^{-(\ell+5-j)}, and the terminal has w_T=1. These satisfy 0<w1<w2<...<wh<1 and, at vertex 3, the slack action is strictly nonoptimal:
\[
(w_2+w_4)/2=17\,2^{-(\ell+5)}>w_3=16\,2^{-(\ell+5)}.
\]
The optional leading variable has weight p=w2/2=7/2^(ell+5), which is less than the minimum internal weight w1=8/2^(ell+5). The proven exact global multiaction recovery theorem therefore gives
\[
\boxed{\alpha=\frac7{2^{5+\ell}}=\frac7{2^\nu}}
\]
for the **entire ambient PSD inverse problem**, with a matching positive-definite monomial curve.

The all-action peeling stages are, in order:
- terminal T and then each newly inserted vertex h,h−1,...,5 singly (ell+1 stages total from the new terminal chain);
- original vertex 4 singly;
- vertices 2,3 simultaneously;
- vertex 1 singly.
Thus the exact exposed-rank profile is
\[
\boxed{(\underbrace{1,\ldots,1}_{\ell+2\text{ steps}},2,1)},
\]
with total nullity (ell+2)+2+1=ell+5=nu and exact minimal degree
    d=(ell+2)+2=ell+4=nu−1.
This is not just a proposed chain: checkpoint 57 proves greedy exposing closure equals the canonical maximal-rank facial reduction, and checkpoint 59 gives the identical tropical max–tau time calculation.

## Part II — a universal SINGLE-ACTION arithmetic depth-rigidity lemma

**Lemma.** Let G be a strict harmonic midpoint network with h internal vertices, one source of weight 0, one terminal of weight 1, one distinct parent pair per internal vertex, and optional independent leading edge. Suppose
\[
\alpha=\frac a{2^{h+1}},\qquad a\text{ odd},\quad a\ge5,
\]
is a valid sharp full-state exponent with \(\operatorname{den}(2\alpha)=2^h\). Then its *exact sparse* greedy facial-reduction degree is **at most h−1**.

**Proof.** The denominator of 2alpha divides the determinant of the h×h integer midpoint matrix. That determinant is the count of cycle-free parent-choice functions and lies in [1,2^h]. Divisibility by 2^h therefore forces det=2^h, i.e. **every parent-choice function is acyclic**, so the entire directed parent graph is acyclic.

Let D(x) be the reduced power-of-two denominator depth of a dyadic rational x, i.e. the least j>=0 with 2^j x integer. We have D(2alpha)=h. Each parent-average gate can increase D by at most one over its parents. Therefore a directed dependency path from the doubled-weight vertex to a boundary has length **exactly h**, using ALL h internal vertices. Reorder these internal vertices by their (necessarily distinct) denominator depths:
    X_1,...,X_h, with D(w_(X_j))=j.
The first is X1=(0+1)/2=1/2. For every j>=2, one parent of X_j must be X_(j−1); the second, say Y_j, must be source 0, terminal 1, or some X_k with k<=j−2 (distinct parents, and no directed cycles).

Write
    w_(X_j)=A_j/2^j,
where each A_j is an odd positive integer, A_1=1. Then
\[
A_j=A_{j-1}+2B_j,\qquad
B_j=2^{j-2}w_{Y_j}\in\mathbb Z_{\ge0}.
\]
The second parent is source iff B_j=0. Hence a=A_h=1+2Σ_(j=2)^h B_j.

Let t_j be the greedy exposing stage of X_j and assign times t_source=infinity,t_terminal=1. Since the parent graph is acyclic, its exposing-time recurrence is exactly
    t_1=2,   t_j=τ(t_(j−1),t_(Y_j)),
where τ(u,v)=u if u=v, and min(u,v)+1 otherwise (checkpoint 59). By induction t_j<=j+1. If Y_j is the source, t_j=t_(j−1)+1. Otherwise Y_j is terminal or X_k with k<=j−2, so t_(Y_j)<=j−1 and therefore t_j<=j (a *deficit* of at least one relative to maximal time j+1).

If the previous stage already has deficit one, t_(j−1)=j−1, then ANY further non-source second parent has t_(Y_j)<=j−1 and gives t_j<=j−1, a deficit of at least two. Thus any chain ending with t_h>=h can have at most one non-source second parent. To preserve exactly one-unit (not larger) deficit when it occurs for the first time at j, its second parent's time must be j−1; because earlier stages have maximal times, this forces either Y_2=terminal at j=2, or Y_j=X_(j−2) with w_(X_(j−2))=1/2^(j−2). In both cases B_j=1. Therefore if t_h>=h, necessarily A_h∈{1,3}.

Now assume the **overall peeling degree** were >=h. Because t_j<=j+1 for every j, the only vertices possibly exposed at time >=h are X_(h−1) and X_h. If t_h>=h we just proved A_h<=3. If instead t_(h−1)=h, all earlier second parents must be the source, so
    w_(X_(h−1))=1/2^(h−1).
But alpha=A_h/2^(h+1) is a *valid full-matrix sharp exponent*, so it cannot exceed the smallest internal diagonal weight, in particular
    A_h/2^(h+1)=alpha<=w_(X_(h−1))=1/2^(h−1).
Hence A_h<=4; as A_h is odd this again gives A_h<=3. Either way, degree >=h implies a<=3. Contraposition proves that a>=5 forces **degree <=h−1**. QED.

**Audit point:** This is not merely an argument using the numerator's binary popcount. It uses (i) saturation of the harmonic determinant, (ii) the resulting Hamiltonian denominator-depth dependency chain, (iii) the exact tropical exposing-time recursion, AND (iv) the full-state auxiliary-coordinate barrier alpha<=min internal weight. Omitting (iv) would make the conclusion false.

## Part III — no single-action representation at the same nullity

Take nu>=5, h=nu−1 and alpha=7/2^nu. Suppose a strict single-action harmonic PSD system **with vertex blow-ups** of total nullity nu had this exponent. The reduced denominator of 2alpha=7/2^h is exactly 2^h. The harmonic determinant bound requires at least h internal vertices; total nullity nu permits at most h, so the system must have exactly h distinct internal vertices and one terminal, **with no blow-up**. The single-action lemma with a=7 then gives
    singularity degree <=h−1=nu−2.
But the two-action construction in Part I has degree nu−1. Contradiction.

Thus for EVERY nu>=5 the triple (rank-one target, nullity nu, exponent 7/2^nu, minimal degree nu−1) is attainable by two-action incidence PSD recovery but **impossible in the entire earlier single-action+blow-up family**.

## Exact-arithmetic check

The companion self-contained Python generator verifies the Bellman rational weights, strict slack inequality, optional-edge noncollision and the exact tropical/greedy exposing profile for ell=0,...,12, i.e. target nullity 5 through 17. It agrees with an independent exhaustive single-action harmonic enumeration at h=4,5 (nullities 5,6), which finds maximum single-action degrees 3,4 for exponents 7/32 and 7/64 respectively. The theorem itself is symbolic and holds for all nu.

## Scope and interpretation

This proves that any complete universal exponent–depth combinatorial theory cannot consist of one active harmonic parent graph plus vertex multiplicities, **in infinitely many dimensions**. At least one additional constraint layer—represented here by a primal-slack but dual-active parent action—is genuinely needed.

It remains UNKNOWN whether every arbitrary dense PSD measurement kernel admits a realization by the **two-policy** controlled incidence model of checkpoints 61–62 with the same sharp exponent and minimal degree/profile. A counterexample to that stronger claim would require an even richer geometry.

No novelty is claimed for ordinary dyadic circuits, stochastic Bellman theory or facial reduction separately; the infinite exact PSD separation and the full-state arithmetic-depth rigidity lemma are proved directly.