# Universal dyadic filtration alignment for every stage of dense PSD facial reduction

**2026-11-07. PROVED.** An intrinsic rank-profile/valuation-flag compatibility theorem valid for **all** real PSD linear inverse problems with unique positive-rank targets, not relying on sparse midpoint models. It strengthens the first-stress alignment theorem (checkpoint 23).

## Theorem (dyadic dual–primal alignment)

Let X*≥0 be uniquely recoverable, let a sharp PSD perturbation arc X(t) have residual ||L(X(t)-X*)||=O(t^Q) and an orthogonal PSD diagonal-leading null-space valuation flag
    R^n=U_0⊕U_1⊕...⊕U_k,
    0=w_0<w_1<...<w_k=Q,
where U0=range X*, every Ui (i>=1) has a positive definite first diagonal coefficient at order wi, and all cross blocks obey the PSD Cauchy–Schwarz order restriction. Let
    W_0=R^n ⊋ W_1 ⊋ ... ⊋ W_d=U0
be **any** valid PSD facial-reduction chain, with successive removed spaces
    R_j=W_(j-1)∩W_j^perp,
    F_j=R_1⊕...⊕R_j=W_j^perp,
    s_j=dim R_j.
Every exposing stress Z_j∈K^perp annihilates X*, and has PSD compression on W_(j-1), with range R_j.

Then, for all j=1,...,d,
\[
\boxed{F_j\subseteq\bigoplus_{i:\ w_i\ge 2^{-(j-1)}Q} U_i.}
\]
In particular the number of null directions with valuation *strictly below* 2^{-(j-1)} Q is bounded by the number of unexposed dimensions:
\[
\boxed{\sum_{i:\ w_i<2^{-(j-1)}Q}\dim U_i
       \le \nu-\sum_{\ell=1}^{j}s_\ell.}
\]
At the final step j=d, all null weight orders satisfy wi>=2^{-(d-1)}Q. This recovers the strengthened diagonal form of Sturm's bound, while the intermediate inequalities retain the **individual facial rank drops**.

## Complete proof

Normalize Q=1 by rescaling the curve parameter; the general statement follows by restoring Q.

**Stage 1.** The first stress Z1 is globally PSD, belongs to K^perp and annihilates X*. Therefore tr(Z1 X(t))=O(t). Decompose it as a positive sum of rank-one terms. Every vector v in its range satisfies v^T X(t)v=O(t), whereas any nonzero component on a weight Ui with wi<1 would give v^T X(t)v=Theta(t^{w_min}) by positivity of diagonal-leading coefficients and strictly higher orders for cross terms involving different weights. Thus range(Z1)=F1 lies in the terminal weight-one block.

**Induction.** Assume the removed subspace F_(j-1) is contained in the direct sum of valuation subspaces with weights >=tau, with tau=2^{-(j-2)}. PSD Cauchy–Schwarz and boundedness of X(t) imply
  ||P_F X(t) P_F||_op=O(t^tau),
  ||P_F X(t) P_W||_F=O(t^(tau/2)),
where F=F_(j-1), W=W_(j-1)=F^perp. The second bound follows e.g. by applying X(t)^{1/2} and the PSD trace Cauchy–Schwarz inequality: the F-block trace is O(t^tau) and the whole trace is O(1).

Write Z_j in F⊕W block form. Its W×W compression S_j is PSD, has range exactly R_j⊂W, and annihilates U0. Because Z_j∈K^perp and <Z_j,X*>=0, one has
  tr(Z_j X(t))=O(t).
Its off-face terms, including its F×F and F×W blocks, are O(t^(tau/2)) or smaller. Hence
  0<=tr(S_j P_W X(t)P_W)=O(t^(tau/2)).
Diagonalize S_j as a strictly positive linear combination of rank-one matrices v v^T with v∈R_j. Every such v satisfies v^T X(t)v=O(t^(tau/2)), so the weighted-flag leading diagonal comparison implies v has no component in any weight space with wi<tau/2. Therefore R_j⊂ ⊕_{wi>=tau/2}Ui. Together with the induction hypothesis F_(j-1)⊂⊕_{wi>=tau}Ui, and since tau>tau/2, this proves the assertion for F_j.

The rank inequality follows from taking orthogonal-complement dimensions. QED.

## Consequences for the joint spectrum

1. The first step (j=1) forces dim(U_terminal)>=s1, yielding the reduced denominator bound denominator(2alpha)<=2^(nu-s1) of checkpoint 23.

2. A proposed sharp flag with many small-weight blocks is incompatible with exposing chains that remove too many null dimensions early. Thus some exponent–rank-profile pairs can be rejected *combinatorially* without any real quantifier elimination. This is stronger than knowing d alone.

3. For nu=4, sharp maximal-dyadic-denominator weights (1/4,3/8,1/2,1) have only **two** null directions with weight at least 1/2. Therefore an exposing rank profile whose first two steps remove >=3 directions cannot realize that flag. A profile with s1=2 is independently excluded by the first-step denominator bound.

4. In every degree-d problem, the diagonal valuation threshold is 2^{-(d-1)}. The leading offdiagonal sharp exponent can be half of that, giving Sturm's 2^{-d} bound. The present theorem makes the intermediate face-rank compatibility explicit.

## Scope and audit

The proof uses only globally PSD competitors, support/valuation asymptotics, the exact dual orthogonality of exposing stresses and PSD block Cauchy–Schwarz. It does **not** assume coefficient rescaling, midpoint-network completeness, any sparse depth preservation, or genericity. It does not give a sufficient characterization of realizable exponent–depth triples; the exact arithmetic catalogue for all nu>=4 remains open.

The general dyadic Sturm error bound and facial reduction framework are established prior work. The per-step rank-profile/valuation flag inclusion is presented with a direct proof; bibliographic priority requires an audit.