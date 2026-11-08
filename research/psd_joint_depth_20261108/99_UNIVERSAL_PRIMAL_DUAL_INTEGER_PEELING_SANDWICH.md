# Milestone 99 — UNIVERSAL dense PSD facial degree lies between TWO explicit integer peeling recurrences on the canonical Dikin weights

**2026-11-08. PROVED for every arbitrary dense uniquely solvable real PSD inverse problem, independently of all sparsity or game representation conjectures.** The lower bound generalizes the actual-kernel-coefficient forced-peeling theorem (checkpoint 54) to arbitrary grade multiplicities (checkpoint 97); the UPPER bound is NEW, obtained by a finite **positive DUAL maxdet Puiseux coefficient truncation**. This gives the first pair of purely integer combinatorial DENSE compatibility inequalities involving the same canonical primal/dual weights, without continuous SDP testing.

## Theorem

Let L:S^n→R^m uniquely recover a positive-rank PSD target X*, with K=ker L. Let the universal fixed monomial maxdet-center valuation grades of checkpoint 89 be
\[
\mathbb R^n=U_0\oplus U_1\oplus\cdots\oplus U_k,\qquad
U_0=\operatorname{range}X_*,
\quad0=w_0<w_1<\cdots<w_k=1,
\]
where all positive grades have positive integer multiplicities and \(\sum_{i=1}^k\dim U_i=\nu\).

**Primal forced-survivor recurrence \(L(w)\).** Set j=k, steps=0. The first transition is j→k−1. At subsequent j≥1 set
\[
\boxed{
j\ \longmapsto\
\ell(j):=\#\{\,1\le i<j:\ 2w_i<w_{j+1}\,\}.
}
\tag{99.1}
\]
Stop at j=0. Let \(L(w)\) be its number of transitions. Then **every** valid dense minimal facial reduction satisfies \(d\ge L(w)\). The complete block-grade proof is in checkpoint 97, Section 2: actual invisible Puiseux coefficients H_i with PD Ui diagonal and weighted support \(w_a+w_b\le2w_i\) annihilate the first \(\ell(j)\) rows of ANY PSD compressed stress.

**Dual exposing-suffix recurrence \(U(w)\).** Again set j=k, steps=0, and use j→k−1 first. At every subsequent j≥1 choose
\[
\boxed{
p(j)=\min\{1\le p\le j:\ 2w_p>w_j+w_{p-1}\},
\qquad j\longmapsto p(j)-1.
}
\tag{99.2}
\]
The set is nonempty (p=j works), and the transitions strictly lower j until zero. Let \(U(w)\) count these transitions. Then for EVERY dense inverse problem,
\[
\boxed{L(w)\ \le\ d\ \le\ U(w)\ \le\ k\ \le\ \nu.}
\tag{99.3}
\]
The NEW upper bound does **not** use a harmonic incidence representation, a graph stress, or numerical semidefinite optimization. It constructs an actual exposing stress from the original dual maxdet curve at every step.

## Complete proof of the NEW upper bound

The stationarity dual path \(Z_\epsilon=\epsilon C_\epsilon^{-1}\) satisfies \(Z_\epsilon\in K^\perp\cap\mathbb S_+^n\). With the universal fixed center chart \(C_\epsilon=D_\epsilon M_\epsilon D_\epsilon,\ M_\epsilon\to M_0\succ0\),
\[
Z_\epsilon=\epsilon D_\epsilon^{-1}M_\epsilon^{-1}D_\epsilon^{-1}.
\]
Thus in the fixed orthogonal grade frame, every diagonal block on Ui has first positive-definite dual Puiseux coefficient at exponent
\[
v_i=1-w_i,
\]
and every cross block Ui×Ua has valuation at least
\[
1-\tfrac12(w_i+w_a)=\tfrac12(v_i+v_a).
\]
All full dual Puiseux coefficients lie in the fixed linear space \(K^\perp\).

**First step.** The ε^0 coefficient is PSD, PD on terminal grade Uk and zero elsewhere. It exposes the face \(W_{k-1}=U_0\oplus\cdots\oplus U_{k-1}\).

**Generic step from a coordinate face W_j.** Assume the current face is exactly
\(W_j=U_0\oplus\cdots\oplus U_j\), with 1≤j≤k−1. Choose p=p(j) by (99.2), and set
\[
E=1-w_p,\qquad V=U_p\oplus\cdots\oplus U_j,\qquad
L=U_0\oplus\cdots\oplus U_{p-1}.
\]
Compress the entire dual path to W_j:
\(S_\epsilon=P_{W_j}Z_\epsilon P_{W_j}\succeq0\).
For each grade Ui⊂V, its first dual diagonal order v_i=1−wi satisfies \(v_i\le E\), and its leading coefficient is PD. Every lower grade Ua⊂L has v_a>E and hence no diagonal coefficient through order E.

Every potential lower–upper cross block Ua×Ui, a<p≤i≤j, has valuation at least
\[
1-\frac{w_a+w_i}{2}\ \ge\
1-\frac{w_{p-1}+w_j}{2}\ >\ 1-w_p=E,
\]
where the strict inequality is EXACTLY the defining condition of p(j). Lower–lower blocks likewise have valuation >E, because both weights are <w_p. Hence **the FINITE Puiseux truncation of \(S_\epsilon\) through order E is identically ZERO on the lower rows L and their crosses**.

Write this truncated dual series as \(\sum_{0\le e\le E}\epsilon^e S_e\). Each \(S_e=P_{W_j}Z_eP_{W_j}\) is the compression of an ACTUAL ambient stress \(Z_e\in K^\perp\), so ANY fixed linear combination is a valid facial-reduction measurement stress. On V the first diagonal coefficient at v_i is PD on each Ui, and every offdiagonal coefficient obeys \(2e\ge v_i+v_a\) by PSD Cauchy–Schwarz for \(S_\epsilon\).

Apply the fully proved finite positive coefficient-rescaling lemma (checkpoint 89) to obtain, for sufficiently large fixed σ and sufficiently small positive fixed t, the single compressed matrix
\[
T=\sum_{0\le e\le E}e^{\sigma e^2}t^e S_e
\]
which is PD on V and identically ZERO on L. Thus \(T\succeq0\) on the FULL current face W_j, annihilates X*, and exposes EXACTLY the suffix \(U_p\oplus\cdots\oplus U_j\). One valid facial step reaches the smaller coordinate face
\[
W_{p-1}.
\]
Repeat. The recurrence reaches U0 after precisely U(w) valid steps. Since the MINIMAL facial degree is at most the length of this valid (possibly non-greedy) chain, \(d\le U(w)\). QED.

## A combinatorial interpretation: maximal "weight-safe parent" peeling

For any strictly increasing rational weights 0=w0<...<wk=1 arising from a harmonic network, define for each internal i the set of ALL "safe" parent pairs
\[
A_i^{\mathrm{safe}}=
\{(a,b): 0\le a<i<b\le k,\
  w_a+w_b\ge2w_i\}.
\]
Temporarily regard these as abstract parent-action constraints, even if edges collide and hence do NOT define an independent-generator PSD incidence pencil.

**Lemma.** The maximal all-safe abstract exposing-closure process removes at each remaining prefix W_j exactly the suffix
\[
\{p(j),p(j)+1,\ldots,j\}
\]
and therefore has EXACTLY U(w) stages (including terminal).

**Proof.** For any i≥p(j), and any safe active pair (a,b) at i with b≤j, if its lower parent a<p(j) then
\(w_a+w_b\le w_{p-1}+w_j<2w_p\le2w_i\),
contradicting safeness. Hence all active safe parent pairs at vertices in the suffix have BOTH endpoints in the suffix, making the suffix exposable. Conversely, by the MINIMALITY of p(j), for every i<p(j) one has \(2w_i\le w_{i-1}+w_j\), so the edge (i−1,j) is a safe ACTIVE action. Any exposed set containing such an i must contain i−1; iterating forces source0, impossible. Therefore no i<p(j) can be exposed. The entire suffix is the unique maximal exposable set. Repeat on W_(p−1). QED.

This explains why U(w) was observed computationally to coincide with the largest peeling degree obtained from *all safe actions* in every one-policy network through h=5. Crucially, the **actual universal dense upper bound is proved independently by the DUAL Puiseux truncation**, so edge collisions in this abstract safe graph cause no logical gap.

## Examples: the sandwich is sharp at both ends

The explicit 6×6 BASE and TIED systems of checkpoints 87–88 have the same canonical weights
\[
(w_1,w_2,w_3,w_4,w_5)
=(3/11,6/11,7/11,9/11,1).
\]
Direct integer recurrence gives
\[
L(w)=3,\qquad U(w)=4.
\]
The BASE system has minimal degree four; the TIED system has minimal degree three. Therefore BOTH endpoints of the universal interval (99.3) can occur with the EXACT SAME intrinsic weights, target rank and nullity. No scalar-weight-only rule can tell which degree occurs without supplementary signed/off-face dual incidence.

For grade weights w1≥1/2, p(k−1)=1 by strict \(2w_1>w_{k-1}\), so \(U(w)\le2\), recovering checkpoint 95's sharp dual threshold.

## Consequences and limitation

- Every arbitrary dense PSD problem has a finite **two-sided combinatorial interval certificate** for its exact minimal facial degree derived solely from its canonical maxdet valuation weights. It is computable with O(k²) rational comparisons, once the weights are obtained.
- The lower and upper recurrences are proved by constructions from *actual original primal and dual Puiseux matrices*, not from hoped-for graph representations.
- This theorem does **not** say that every integer in [L(w),U(w)] occurs for the same weights, nor that the upper and lower limits suffice to determine exact depth in every dimension. A tied-edge realization conjecture for all weight-interval pairs remains unproved.
- It does not determine which profile/rank drops occur at each intermediate stage; retaining actual signed dual face-compression data is indispensable.
- The separate universal fixed-(ν,d) all-value arithmetic catalogue beyond currently classified small nullities remains open.

## Provenance

Puiseux, maxdet center and coefficient rescaling are established tools. The new universal dual-truncation recurrence is fully proved here, but bibliographic priority/novelty requires outside review. The abstract safe-edge lemma is elementary combinatorial and independent of SDP theory.