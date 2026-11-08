# Milestone 54 — universal forced-peeling depth lower bound from sharp PSD valuation weights

Date 2026-11-08. **PROVED for arbitrary dense real PSD measurement kernels**, without the project's weighted-flag-to-midpoint theorem and without sparsification. Uses only an actual semialgebraic/Puiseux PSD arc, elementary PSD Cauchy–Schwarz and linear algebra. The result is a finite combinatorial obstruction on each **simple** (one-dimensional valuation grade) sharp arc; it is not yet an all-value joint spectrum formula.

## Theorem A — spacing and deterministic forced-peeling recurrence

Let L:S^n→R^m have unique PSD solution X* with target rank r≥1 and nullity ν≥2. Suppose there exists a Puiseux PSD curve X(t)→X* whose measurement residual is O(t^Q), such that after adding a harmless positive multiple of t^Q I its null-space quadratic-form filtration has **ν distinct one-dimensional grades** with rational orders
\[
0<w_1<\cdots<w_\nu=Q.
\]
Here e_i is an orthonormal null basis adapted to the quadratic-form filtration: the first diagonal coefficient at t^{w_i} is strictly positive, and each (i,j) block has order at least (w_i+w_j)/2. Every coefficient H_i of the arc at t^{w_i}, i<ν, belongs to K=ker L.

Then:

1. **Universal adjacent-order spacing.** For every i<ν,
\[
\boxed{w_{i+1}\le2w_i.}
\tag{A}
\]
2. Define, for j=1,...,ν, the *forced-survivor function*
\[
k(\nu)=\nu-1,\qquad
k(j)=\#\{1\le i\le j-1:2w_i<w_{j+1}\}
\quad(1\le j<\nu).
\tag{B}
\]
The count is a prefix because w_i is strictly increasing. Starting from j_0=ν, iterate j_{m+1}=k(j_m), until the first index j_\ell=0. Every valid facial-reduction chain has **at least \ell strict exposing steps**. In fact, after its first m steps, its current face still contains the coordinate PSD face on
\[
U+\operatorname{span}(e_1,\ldots,e_{j_m}),
\qquad U=\operatorname{range}X_*.
\]
3. **Two-step gap rigidity.** If
\[
\boxed{w_{i+2}>2w_i\quad(1\le i\le\nu-2),}
\tag{C}
\]
then k(j)=j-1 for all j=1,...,ν. Consequently every exposing chain needs ν steps, and
\[
\boxed{d=\nu.}
\tag{D}
\]
The first stress must remove only the terminal valuation direction, and every subsequent stress removes only its last remaining coordinate direction.

These statements hold even if the kernel K contains arbitrarily many additional dense matrices unrelated to the Puiseux coefficient matrices.

## Proof, step 1 — exact kernel support constraints

For every i<ν let H_i denote the coefficient of t^{w_i}. The residual is O(t^Q) and w_i<Q, hence H_i∈K. Let U_0=U have weight zero. PSD Cauchy–Schwarz gives, for any vectors u,v in valuation grades w_a,w_b,
\[
|u^\top X(t)v|^2\le (u^\top X(t)u)(v^\top X(t)v)
=O(t^{w_a+w_b}).
\]
Therefore
\[
(H_i)_{ab}=0\quad\text{if }w_a+w_b>2w_i,
\tag{1}
\]
including all support-to-null blocks with a=0. In particular, every H_i is supported on
\[
W_{\rho_i}=U+\operatorname{span}(e_1,\ldots,e_{\rho_i}),
\qquad \rho_i=\max\{j:w_j\le2w_i\}.
\tag{2}
\]
Furthermore, its null–null blocks involving some index j>i can only involve a *second* index k<i, since w_j>w_i and w_k≥w_i would violate (1). The (i,i) null coefficient of H_i is strictly positive.

## Proof, step 2 — adjacent spacing forced by uniqueness

Suppose for some i<ν that w_(i+1)>2w_i. Then rho_i=i. Because w_1<...<w_i, each earlier coefficient H_j, j<=i, has rho_j<=i and hence is supported on W_i. On W_i, form the finite generalized polynomial
\[
Y(t)=X_*+\sum_{j=1}^i t^{w_j}H_j.
\]
Each coefficient at order w_j has positive (j,j) leading diagonal and satisfies the full all-block order restriction 2w_j≥w_a+w_b for its nonzero entries. The established elementary coefficient-rescaling lemma (diagonal normalization followed by exponentially suppressing distinct-weight offdiagonals) therefore makes
\[
Y_\sigma(t)=X_*+\sum_{j=1}^i e^{\sigma w_j^2}t^{w_j}H_j
\]
positive semidefinite (strictly positive on W_i, identically zero outside W_i) for sufficiently small t>0. Every H_j∈K and the first coefficient H_1 is nonzero, so Y_sigma(t) is a **nonconstant EXACT PSD solution** to the original measurements, contradicting uniqueness. Thus w_(i+1)≤2w_i for all i<ν.

In particular rho_i≥i+1 for i<ν. This makes k(j)≤j-1 and guarantees finite termination of the recurrence.

## Proof, step 3 — a triangular stress-annihilation lemma

For any j, suppose the current reduced PSD face contains W_j. Let S be the PSD compression on that face of any exposing stress Z∈K^\perp annihilating X*. Define k=k(j). Because rho_i≤j for every 1≤i≤k, the actual matrix H_i∈K is supported on W_j, a subspace of the current face. Thus
\[
\langle S,H_i\rangle=\langle Z,H_i\rangle=0,\quad i=1,\ldots,k.
\]
Since S annihilates U, its source blocks vanish. Pairing H_1 gives
\[
0=(H_1)_{11}S_{11},
\]
because (1) forbids every null-null block of H_1 involving an index >1. Hence S_11=0, and PSD positivity forces the entire e_1 row and column of S to vanish. Inductively suppose rows 1,...,i-1 of S vanish. In the null-null blocks of H_i, any index >i can pair only with an index <i, whose row of S is already zero. All remaining nontrivial entries are among indices <i, or the positive (i,i) entry. Hence
\[
0=\langle S,H_i\rangle=(H_i)_{ii}S_{ii}
\]
and S_ii=0, killing that row. Thus
\[
\boxed{S e_i=0\text{ for all }1\le i\le k(j).}
\tag{3}
\]
Any exposing stress therefore annihilates W_(k(j)) when its current face contains W_j. The next exposed face still contains W_(k(j)).

Starting from W_ν=R^n, induction on the exposing stages shows that after m steps the face contains W_(j_m). If j_m>0 that face is larger than the target minimal face, so the chain cannot be complete. Since j_(ell-1)>0 and j_ell=0, its length is at least ell. This proves the forced-survivor recurrence.

## Proof, step 4 — maximal-depth criterion

If w_(i+2)>2w_i for all i≤ν-2, then for any 2≤j≤ν-1 we have
    w_j≤2w_(j-1)   from (A),
    w_(j+1)>2w_(j-1) from (C).
Therefore rho_(j-1)=j, so k(j)=j-1. At j=ν, k(ν)=ν-1 by definition; at j=1, k(1)=0. Thus j_m=ν-m for all m≤ν, forcing at least ν strict exposing steps. Facial reduction always terminates in at most ν steps (each removes at least one null dimension), hence d=ν. This also forces each exposing step to remove exactly one coordinate direction, as only ν dimensions are available. QED.

## Examples and significance

- Weights (1/7,2/7,4/7,1) meet every strict two-step gap, so ANY dense PSD instance possessing such a sharp valuation flag has exact degree four. This recovers the earlier nullity-four α=1/7 rigidity using only the flag orders and the actual kernel coefficients.
- For all ν≥3, the Mersenne orbit weights (1/q,2/q,4/q,...,2^(ν-2)/q,1), q=2^(ν-1)-1, satisfy (C), giving a short direct proof of maximal degree once the orbit is known.
- For weights (3/8,1/2,3/4,1), the strict gap fails at the first index because 3/4=2(3/8). The recurrence gives only d≥3, consistent with sparse depth-three realizations; maximal depth is not asserted.
- For evenly spaced weights (1/5,2/5,3/5,4/5,1), the forced recurrence gives d≥4, while a particular sparse completion has d=5. The theorem is a universal **lower** bound, not an exact depth formula from weights alone.

**This is not a full combinatorial classification.** It proves a new necessary valuation/depth compatibility condition, and a broad maximal-depth rigidity criterion, for arbitrary dense kernels. It does not state that every weighted flag is achievable at its forced lower depth, or that sharp midpoint networks can be sparsified preserving exact degree. Bibliographic novelty of general valuation methods is not claimed.