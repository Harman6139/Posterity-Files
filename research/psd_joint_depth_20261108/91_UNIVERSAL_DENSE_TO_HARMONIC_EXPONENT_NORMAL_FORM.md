# Milestone 91 — UNCONDITIONAL dense-to-harmonic universality for the sharp RECOVERY EXPONENT at SAME target nullity

**2026-11-08. FULLY PROVED for arbitrary finite-dimensional uniquely solvable real PSD inverse problems, using only the independent universal maxdet monomial-chart theorem (checkpoint 89) and its downshift proof, not the previously load-bearing weighted-flag-to-midpoint extraction.** This is a *complete exponent-preserving* constructive universality theorem. It is deliberately NOT a facial-degree-preserving theorem: earlier counterexamples show that a SINGLE harmonic parent network cannot generally preserve minimal facial degree.

## Main theorem

Let L:S^n→R^m be real linear with uniquely recoverable positive-rank PSD target X*, rank r>=1 and nullity ν=n-r. Let α be its exact sharp full ambient Hölder recovery exponent. Then there exists a **finite strict one-action harmonic midpoint incidence PSD recovery problem** with:
- EXACT target rank r;
- EXACT target nullity ν (no increase of matrix order);
- EXACT sharp full ambient recovery exponent α.

This statement is necessary-and-sufficient for possible exponents at fixed (n,r), because every harmonic incidence system is itself a valid PSD inverse problem. It DOES NOT state that minimal singularity degree d, exact exposing rank profile, measurements or geometric fibre are preserved.

In particular, the complete fixed-nullity exponent spectrum is the finite combinatorial set
\[
\boxed{
\Sigma_\nu
=\{1\}\cup
\left\{w_v/2:
\begin{array}{l}
0=w_0<w_1<\cdots<w_h<w_{h+1}=1,\\
0\le h\le\nu-1,\quad 2w_i=w_{a_i}+w_{b_i},\\
0\le a_i<i<b_i\le h+1,\quad w_v/2\le w_1
\end{array}
\right\}.}
\]
For h=0, take w_1=1 (terminal), giving the square-root exponent 1/2; exponent 1 is realized by injective measurements. For h>=1, the value w1 is automatically a listed half-weight: vertex1's lower harmonic parent is the source and its upper parent's weight equals 2w1. This graph certificate requires at most ν−1 internal scalar vertices, and any unused nullity is filled by positive coordinate clones of its terminal or internal vertices.

## 1. Canonical maxdet chart and a UNIVERSAL downshift lemma

The shifted maxdet center Cε (unique, semialgebraic, and convergent to X*) has the fixed orthogonal valuation decomposition from checkpoint 89:
\[
\mathbb R^n=U_0\oplus U_1\oplus\cdots\oplus U_k,\quad
U_0=\operatorname{range}X_*,\quad
0=w_0<w_1<\cdots<w_k=1,
\]
with each positive grade Ui of dimension mi≥1 and
\[
c\bigoplus_i\epsilon^{w_i}I_{U_i}
 \preceq C_\epsilon\preceq
C\bigoplus_i\epsilon^{w_i}I_{U_i}.
\tag{91.1}
\]
Write its finite real Puiseux expansion through exponent one as
\[
C_\epsilon=X_*+\sum_{0<e\le1}\epsilon^e A_e
            +O(\epsilon^{1+\xi}),\qquad \xi>0,
\]
where A_e∈K=ker L whenever e<1 and A_1−I∈K. Each positive-grade diagonal first occurs at e=w_i with \(P_{U_i}A_{w_i}P_{U_i}\succ0\), while PSD Cauchy–Schwarz gives the **all-block** coefficient restriction
\[
P_{U_a}A_eP_{U_b}=0\quad\text{when }w_a+w_b>2e.
\tag{91.2}
\]

**Universal downshift lemma.** Fix an internal grade i<k. Suppose for some w'_i∈(w_(i−1),w_i) the grade weight can be lowered to w'_i and an actual H∈K with \(P_{U_i}H P_{U_i}\succ0\) has NO nonzero block whose new endpoint-weight sum exceeds 2w'_i. Then the finite curve
\[
Y_\epsilon
=X_*+\sum_{0<e\le1}\exp(\sigma e^2)\epsilon^e A_e
 +\exp(\sigma (w'_i)^2)\epsilon^{w'_i}H
\]
(after combining coefficients of equal exponents) is positive definite for sufficiently small ε when σ is sufficiently large and fixed. Proof: the rescaling lemma from checkpoint 89 normalizes each orthogonal grade by \(\exp(-\sigma w_j^2/2)\epsilon^{-w_j/2}\); the diagonal limiting blocks are PD and cross blocks of distinct weights are exponentially suppressed.

The residual is exactly ε expσ ||L I||, since all added coefficients with exponent below one lie in K. Meanwhile \(P_{U_i}Y_\epsilon P_{U_i}\succeq c\epsilon^{w'_i}I\), but the original maxdet center obeys \(P_{U_i}C_\epsilon P_{U_i}\preceq C\epsilon^{w_i}I\). The universal maxdet Loewner envelope says ANY PSD competitor of residual O(ε) is bounded by a fixed multiple of Cε. This contradiction proves the lemma: **a successful lower-grade positive kernel mode cannot be downshifted**.

This is a general dense-kernel argument; it does not assume a sparse matrix basis or simultaneous diagonalization of generators.

## 2. Every internal grade is a GENUINE harmonic midpoint, including multidimensional grades

For each i<k the actual Puiseux coefficient H_i=A_(w_i) lies in K, has PD compression on Ui, and obeys (91.2) with e=w_i.

Suppose H_i has NO nonzero offdiagonal block between two DIFFERENT grades Ua,Ub satisfying
\[
a<i<b,\qquad w_a+w_b=2w_i.
\]
Any offdiagonal block of H_i with weighted average equal to w_i must have indices one below and one above i: pairs both ≤i have strictly smaller average unless they are in the same Ui block, while pairs both ≥i have strictly larger average unless they are within Ui. Blocks entirely within Ui (including their offdiagonal matrix entries) pose NO problem when the ENTIRE weight of Ui is lowered.

Consequently every block of H_i joining distinct grades has weight average STRICTLY below w_i, except impossible blocks whose average exceeds w_i (forbidden by (91.2)). There are finitely many such blocks. Choose w'_i just below w_i and above w_(i−1) so that every nonzero H_i block, including all Ui×Ui blocks (new average precisely w'_i), meets the lowered support-order test. Then H=H_i satisfies the downshift lemma, contradicting the maxdet envelope.

Therefore there MUST be a nonzero cross-grade block with
\[
\boxed{0\le a<i<b\le k,\qquad 2w_i=w_a+w_b.}
\tag{91.3}
\]
Choose one such pair for every internal grade. Each pair is a distinct unordered edge across different i, because the strict weight w_i is uniquely determined by the average of its parent weights. This is a **strict harmonic midpoint network on h=k−1 internal grades**, extracted from the ORIGINAL arbitrary dense problem. The positive multiplicity mi of a grade does not affect its scalar midpoint equality.

## 3. The exact sharp EXPONENT is one of the graph's half-weights

Checkpoint 89 independently proves the exact Dikin-weighted-kernel rank formula
\[
\alpha=\min\{1,\tau(K,w)\},\qquad
\tau(K,w)=\min_{H\in K\setminus0}
           \max_{\{a,b:H_{ab}\ne0\}}\tfrac12(w_a+w_b).
\]
For k>=2, \(H_1=A_{w_1}\in K\) is nonzero and has maximal nonzero pair-weight exactly w1, so \(\alpha\le w_1<1\).

If α=w1, the midpoint relation for the lowest grade i=1 has lower parent source a=0, and its higher parent v satisfies \(w_v=2w_1\); hence α=w_v/2.

If α<w1, select H∈K attaining the finite support threshold τ=α. A positive-null diagonal block or a null-null offdiagonal block has weight >=w1 and therefore cannot appear in H. Every H entry outside the target-support block is consequently **support-to-null**. If H had no support-to-null entry it would be supported entirely in U0, impossible because uniqueness forces \(K\cap S(U_0)=\{0\}\). Thus some support-to-null block is nonzero, and α is precisely w_v/2 for the largest weight vertex v appearing in such a block.

For k=1, w1=1, the kernel support threshold is either ≥1 (Lipschitz α=1) or equals 1/2 (from a support-to-null direction), so α∈{1,1/2}. This separately covers h=0.

## 4. Converse and exact target-nullity preservation by clone blow-up

Take the extracted strict scalar harmonic parent graph with h=k−1 internal vertices and terminal k. Its vertex weights are w1,...,wk. By the known exact sparse-incidence theorem, the rank-one target E00 is uniquely PSD recoverable, with a global matching rate α=w1 without a leading edge; when α=w_v/2<w1 an unused independent leading source-to-v edge gives the rate α instead. This edge cannot collide with a harmonic parent edge: any such edge (0,v) at child i would force w_i=w_v/2=α<w1, contradiction.

The scalar graph uses one null coordinate per positive grade, total k. To preserve EXACT original nullity ν=Σ_(i=1)^k mi, clone each positive grade vertex i to mi tied diagonal coordinates. The proven vertex-blow-up theorem (checkpoint 52) shows that clone multiplicities preserve the exponent and control EVERY ambient PSD competitor. Its nullity is exactly ν. Finally append a fully measured positive definite support block of dimension r−1 and all cross entries, giving an exactly rank-r target in S^(r+ν).

Thus the original dense problem and the constructed harmonic problem have exactly the SAME (n,r,alpha). This proves the full unconditioned exponent universality, without an assumption on the original kernel's sparsity. QED.

## A stronger relationship to facial reduction

The same central dual path \(Z_\epsilon=\epsilon C_\epsilon^{-1}\in K^\perp\) yields a VALID (not necessarily minimum-length) facial-reduction chain by taking its leading Puiseux coefficient on successive valuation-grade face compressions (checkpoint 90 Step1). Hence
\[
\boxed{ d\le k\le\nu,\qquad
  \operatorname{rank}(\text{first maximal PSD exposing stress})=\dim U_k.}
\]
At maximal degree d=nu this chain is forced to be minimal, with one-dimensional aligned grades; checkpoint 90 then proves universal discrete convexity and complete integer-gap exponent classification.

At NONMAXIMAL d<nu, several grades may be exposed simultaneously by an alternative stress. In general, the original dense kernel's *dual face-compression structure* is not determined by the harmonic graph extracted from its primal valuation flag. The degree-3 versus degree-4 tied-edge counterexample (checkpoint 75) demonstrates precisely this gap.

**Remaining UNSOLVED universal problem:** equality of the full arbitrary-dense exponent/rank-profile spectrum with the bounded tied-edge game certificate of checkpoint 83, at unchanged target nullity. This theorem proves equality of the exponent-only spectra and the full maximal-depth spectra, which are substantial but strictly weaker projections.

## Literature/provenance

The maxdet barrier, real Puiseux growth, SDP facial reduction, and harmonic midpoint identities are established mathematical mechanisms. The proof above is self-contained given the earlier analytically proved center envelope, coefficient-balancing lemma and sparse construction; bibliographic priority is not established. Do not advertise a complete nonmaximal all-degree joint spectrum on the basis of this milestone.
