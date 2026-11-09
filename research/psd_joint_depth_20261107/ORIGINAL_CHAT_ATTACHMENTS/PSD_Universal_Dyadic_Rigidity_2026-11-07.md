# Research checkpoint: dyadic rigidity and joint dimension–depth optimality in arbitrary PSD recovery

**Date:** 2026-11-07. **Status:** full rigorous results stated below, contingent on the dense weighted-flag-to-mediated extraction theorem proved in the prior project memorandum. This is a universal *extremal structural theorem*, not a complete sparse-depth preservation theorem for all rational exponents. No unreviewed priority claim is made about existing mediated-graph results.

## Basic setting

Let \(\mathcal L:\mathbb S^n\to\mathbb R^m\), \(X_*\succeq0\) be uniquely recoverable, \(r=\operatorname{rank}X_*\ge1\), and \(\nu=n-r\ge1\). Assume equivalently that \(\ker\mathcal L\cap\mathbb S^n_+=\{0\}\) and that the affine measurement fibre meets the PSD cone in \(X_*\) alone. Write \(\alpha\) for the optimal full-Frobenius recovery exponent and \(d\) for minimal facial-reduction degree. The established Sturm estimate implies \(\alpha\ge2^{-d}\) and \(d\le\nu\).

Use the following **dense-PSD structural extraction lemma**, whose proof is in `Sharp_PSD_Stability_Weighted_Flags_Memorandum.md`, Sections 2–4. Every such uniquely recoverable problem with \(0<\alpha\le1/2\) admits a finite strictly ordered harmonic midpoint set \(S\subseteq[\alpha,1)\), with \(|S|\le\nu-1\), satisfying \(2\alpha\in S\cup\{1\}\). Moreover, the set is extracted as the active constraints of an extremal weighted flag of *actual kernel matrices*: one coefficient matrix per positive diagonal weight with positive definite corresponding diagonal compression, and an optional earlier kernel coefficient with leading support-to-null block. At a strict weight, an active midpoint equality \(2w_i=w_a+w_b\) comes from a nonzero block of the kernel coefficient at order \(w_i\).

For completeness, the mechanism of this lemma is: (1) choose a sharp semialgebraic Puiseux arc and recursively compress its PSD diagonal leading coefficients to construct an orthogonal flag with at most \(\nu\) null levels; (2) positivity imposes \(2e\ge w_i+w_j\) on every nonzero \((i,j)\)-block of an order-\(e\) coefficient; (3) conversely, arbitrary strictly feasible weights in the resulting rational support polytope can be realized by multiplying each coefficient of order \(e\) by \(\exp(\sigma e^2)\), because after PSD diagonal congruence its surviving off-diagonal contributions scale as \(\exp[-\sigma(w_i-w_j)^2/4]\); (4) the componentwise-minimum point of the closed rational polytope has active midpoint equalities at each distinct intermediate weight. This supplies a finite mechanism, not quantification over all possible curves.

## Theorem A: a universal feedback/dyadic dichotomy

For any harmonic set \(S=\{w_1,\ldots,w_h\}\) with endpoints \(0,1\) and pairwise distinct parent pairs \(a(i),b(i)\) satisfying \(2w_i=w_{a(i)}+w_{b(i)}\), orient the two parent arrows from each internal vertex to its parents. Then:

1. If this parent-directed graph has no directed cycle among internal vertices, **all** weights \(w_i\) are dyadic rationals.
2. If a dense PSD recovery problem has a non-dyadic sharp exponent \(\alpha\), **every** mediated network extracted from any sharp weighted flag must contain a directed feedback cycle.
3. Write \(M\in\mathbb Z^{h\times h}\) for the harmonic system, with rows \(2e_i-e_{a(i)}-e_{b(i)}\) after deleting boundary columns. Then
   \[\det M=\#\{\text{choices of one parent at each internal vertex forming an absorbing acyclic functional graph}\}.\]
   In particular \(1\le\det M\le2^h\), every weight denominator divides \(\det M\), and \(\det M=2^h\) **if and only if** the full parent-directed graph is acyclic.

**Proof.** In a directed acyclic graph, topologically order vertices so that each parent's weight is evaluated before the child's. The boundary weights are \(0,1\), so successive midpoint averaging gives only dyadic rationals. For the second assertion, \(2\alpha\) equals one of these weights or the terminal; if all were dyadic, \(\alpha\) would be dyadic, a contradiction.

For the determinant identity, write each reduced row as \((e_i-e_{a(i)})+(e_i-e_{b(i)})\), treating boundary columns as zero. Expanding multilinearly gives one determinant for each of \(2^h\) parent choices. If the selected functional graph has an internal directed cycle, the selected rows sum to zero around that cycle and its determinant vanishes. If it is acyclic, simultaneously permute rows and columns into a topological order; the matrix is triangular with all diagonal entries one, so its determinant equals one. The larger-parent arrow strictly increases weight and eventually reaches terminal \(1\), so at least one selection is acyclic; hence \(\det M>0\). The harmonic matrix is invertible and Cramer's rule gives denominator divisibility. Every choice is acyclic exactly when the full parent-directed graph has no internal cycle. QED.

## Theorem B: complete rigidity at the extremal Sturm exponent in minimal nullity

Assume \(\nu\ge2\). If an **arbitrary dense** uniquely solvable PSD problem has
\[\boxed{\alpha=2^{-\nu}},\]
then **necessarily**:

(a) its minimal facial-reduction degree is **exactly** \(d=\nu\);

(b) every sharp weighted-flag extraction has exactly \(\nu-1\) distinct intermediate scalar diagonal levels and, after ordering, these levels are
\[\boxed{2^{-(\nu-1)},\ 2^{-(\nu-2)},\ \ldots,\ 2^{-1}};\]

(c) the midpoint parents are uniquely forced:
\[2(2^{-j})=0+2^{-(j-1)},\qquad 1\le j\le\nu-1,\]
where \(2^0=1\) represents the terminal, and the directed harmonic graph is the **unique dyadic chain**;

(d) all \(\nu\) nullspace diagonal weight blocks in the sharp flag are one-dimensional, and its earliest coefficient (at order \(2^{-\nu}\)) is a nonzero kernel matrix with support-to-first-null-block coupling. For each intermediate level \(2^{-j}\), its leading kernel coefficient has a strictly positive diagonal compression at that level and a nonzero support-to-next-level coupling corresponding to the forced active midpoint constraint.

**Proof.** Sturm gives \(\alpha\ge2^{-d}\), while each facial-reduction step must remove at least one nullspace dimension, so \(d\le\nu\). Equality \(\alpha=2^{-\nu}\) therefore forces \(d=\nu\), proving (a).

Apply dense-to-mediated extraction. Since \(2\alpha=2^{-(\nu-1)}<1\), that weight belongs to \(S\). Let \(h=|S|\le\nu-1\). By Theorem A, its denominator \(2^{\nu-1}\) divides \(\det M\) and \(1\le\det M\le2^h\le2^{\nu-1}\). Thus \(h=\nu-1\) and \(\det M=2^h\), so the entire parent-directed graph is acyclic.

All internal weights are positive. For **any** internal vertex there is a strictly increasing-parent path of length at most \(h\) to terminal \(1\). Choosing its designated parent on each of at most \(h\) independent unbiased steps has probability at least \(2^{-h}\). Since the vertex weight equals the probability of absorption at terminal \(1\), every weight is at least \(2^{-h}\). The vertex with weight \(2\alpha=2^{-h}\) attains equality. Hence its increasing-parent path must have **exactly** \(h\) steps; it visits all \(h\) internal vertices. The probability of following that successful path already equals its entire terminal absorption probability \(2^{-h}\). Therefore the alternate parent at **each** vertex on this path must have zero probability of terminal absorption. Each internal vertex has strictly positive absorption probability, so the alternate parent can only be boundary \(0\). Each path vertex consequently has parents \((0,\text{next vertex})\). Solving this chain backwards from terminal weight \(1\) gives exactly the weights in (b) and parents in (c). The claimed uniqueness of the parent network follows.

The sharp flag has at most \(\nu\) nonzero diagonal levels. There are exactly \(h+1=\nu\) distinct levels, including the terminal at weight \(1\), so every block has dimension one. The leading exponent \(\alpha=2^{-\nu}\) is below the smallest diagonal level \(2^{-(\nu-1)}\), so the flag is off-diagonal-leading. The earliest kernel coefficient must have a support-to-null block; its order inequality \(2\alpha\ge w_j\) forces the **first** null block. The active midpoint at each intermediate diagonal level comes from a nonzero support block of the corresponding kernel coefficient; by the unique chain, this block joins target support to the next diagonal level. This proves (d). QED.

**Consequence.** The most unstable possible exponent at a given target nullity has a rigid, dimension-saturating kernel incidence mechanism even when the original measurement map is dense. This is stronger than knowing its value \(2^{-\nu}\) or its degree \(d=\nu\) alone. It does **not** imply the whole kernel can be transformed into a sparse midpoint pencil.

## Theorem C: joint dimension–depth optimality for every full-denominator dyadic exponent

Fix \(\nu\ge2\), an odd integer \(1\le a<2^{\nu-1}\), and
\[\alpha=\frac{a}{2^\nu}.\]
Then the following two minima are **simultaneously attained** by one explicit rank-one sparse PSD recovery construction:
\[
\boxed{\text{minimum target nullity}=\nu,\qquad
\text{minimum singularity degree}=e=\left\lceil\log_2\frac1\alpha\right\rceil.}
\]
For any prescribed target rank \(r\ge1\), the simultaneous minimum ambient matrix size is \(n=r+\nu\). Furthermore, **every** exact minimal-nullity realization of \(\alpha\) admits at least one sharp harmonic certificate with exactly \(\nu-1\) internal nodes and an acyclic parent graph.

**Proof of necessity.** The denominator of \(2\alpha=a/2^{\nu-1}\) in lowest terms is \(2^{\nu-1}\). If \(h\) is the size of a harmonic certificate extracted from an arbitrary target of nullity \(\nu'\), Theorem A gives \(2^{\nu-1}\le\det M\le2^h\le2^{\nu'-1}\). Hence \(\nu'\ge\nu\). At equality \(\nu'=\nu\), necessarily \(h=\nu-1\) and \(\det M=2^h\), proving the acyclicity claim. Sturm gives \(\alpha\ge2^{-d}\), hence \(d\ge\lceil\log_2(1/\alpha)\rceil=e\).

**Constructive sufficiency.** Set \(x=2\alpha=a/2^{\nu-1}\). Perform binary bisection of \([0,1]\) toward \(x\). On step \(j=1,\ldots,\nu-1\), create midpoint \(m_j=(L_{j-1}+R_{j-1})/2\) of the current nested interval, and replace its left or right endpoint according to whether \(x>m_j\) or \(x<m_j\). Because \(a\) is odd and its denominator is exactly \(2^{\nu-1}\), the first equality \(x=m_j\) occurs at \(j=\nu-1\). All created midpoints are distinct, each is the average of the two previous interval endpoints (which are boundary vertices or earlier midpoints), and the parent graph is acyclic.

For every midpoint \(m_j=(L+R)/2\), with \(0\le L\le x\le R\le1\), we have \(m_j\ge R/2\ge x/2=\alpha\). Thus the construction meets **the full-state recovery barrier**, not merely a projected-variable condition. The target value \(2\alpha=x=m_{\nu-1}\) is present. The constrained mediated-set PSD pencil in the prior project memorandum (diagonal variables \(x_v\), weak off-diagonal \(\lambda x_v\) on parent edges, a free leading off-diagonal coordinate on edge \((0,x)\), and measurements of all off-pencil entries, trace and terminal diagonal) has target rank one, nullity exactly \(\nu\), and exponent **exactly** \(\alpha\). Its upper bound holds for arbitrary ambient PSD competitors, and its sharpness curve is positive definite after diagonal congruence. The extra leading edge is distinct from all parent edges: if it were a parent edge, its midpoint would be \(\alpha\), but \(\alpha\) has denominator \(2^\nu\) and is not among the \(\nu-1\) intermediate bisection values.

To show exact degree, let \(k=\lceil\log_2(1/x)\rceil\). The first \(k\) bisection midpoints have source vertex \(0\) as a parent: they are \(1/2,1/4,\ldots,2^{-k}\). No later vertex has source \(0\) as a parent. Using the proved sparse facial-peeling criterion, make a valid chain of \(k+1\) exposures: first remove terminal \(1\); then remove each of the first \(k-1\) source-parent midpoints singly; finally remove every remaining internal vertex simultaneously. All closure constraints are satisfied, because any vertex with both parents remaining has those parents in the final removed set, while the last source-parent vertex has its non-source parent already removed. Thus \(d\le k+1\). But \(k+1=\lceil\log_2(1/\alpha)\rceil=e\), so Sturm gives the reverse inequality, and \(d=e\).

Appending a fully observed positive definite block (and measuring all cross entries to the original matrix) raises the target rank to arbitrary \(r\) without changing its nullity, exponent, or facial depth. QED.

**Examples:** for \(\nu=5\), the exponents \(1/32,3/32,5/32,7/32,9/32,\ldots,15/32\) have jointly dimension-minimal and depth-minimal constructions, with degrees respectively \(5,4,3,3,2,\ldots,2\). All eight odd-numerator values are covered in matrix size \(r+5\).

## Adversarial audit

- The determinant is not an arbitrary bound: its exact expansion counts absorbing functional parent choices, with no potentially cancelling negative summands.
- The acyclic conclusion uses *saturation* of the denominator inequality, not merely the dyadic nature of an exponent. The non-dyadic converse is asserted only for the presence of a directed cycle, never a characterization by cycle count alone.
- The rigidity conclusion concerns every sharp **weight-extraction pattern**, not all original kernel matrices or every arbitrary facial-reduction chain.
- The bisection path obeys the auxiliary-coordinate barrier \(\min m_j\ge\alpha\), so the claimed rate is for the **full matrix**.
- The exact degree is proved using an explicit exposing schedule and the lower bound from Sturm; it is not inferred from numerical peeling.
- The construction is compatible with a dense-map source because the necessity theorem uses a dense weighted-flag extraction; the converse construction is allowed to be sparse, and no dense-to-sparse **depth-preservation** of a given instance is asserted.
- Enumeration was performed with exact Fraction arithmetic for \(511\) bisection cases at \(2\le\nu\le10\) and unique extremal chains through \(\nu=6\); the mathematical proof does not rely on enumeration.

## Unresolved beyond these exact frontier theorems

A complete closed combinatorial joint spectrum \(\Sigma_{n,r,d}\) for arbitrary degrees \(d\ge3\), the necessity of sparse peeling for general dense kernels, and the possible occurrence of exponent \(1/2\) at degree \(d\ge3\) are **not** resolved here. The previously established finite real-algebraic kernel/stress/flag decision theorem still handles each fixed triple algorithmically but does not answer those sharper structural questions.