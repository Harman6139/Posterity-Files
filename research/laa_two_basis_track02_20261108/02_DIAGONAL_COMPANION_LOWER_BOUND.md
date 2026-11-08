# Milestone 02 — normal form for positive block lifts and a generic quartic diagonal-companion no-go

Date 2026-11-08. Proved results are architecture-relative. They do NOT rule out general O(m^2+p) two-basis representations with noncommuting matrix-valued positive auxiliaries or nonlinear/face-dependent embeddings.

Let D=m(m+1)/2 and L <= S^m be a measurement space containing I, with dim L=ell, codim s=D-ell. Let b=A(I) so the original fibre has an interior point I.

## Theorem 1 — positive block-lift normal form

Let J:S^m -> S^{m+k} be a linear map preserving PSD and whose leading principal m-by-m block equals X:
  J(X)=[ X C(X); C(X)^T H(X) ].
Then there exists a FIXED m-by-k matrix B such that C(X)=X B for all symmetric X, and
  T(X)=H(X)-B^T X B
is a positive linear map S_+^m -> S_+^k.
Equivalently J(X) is congruent by a fixed invertible block-triangular matrix to X direct-sum T(X).

**Proof.** Fix one column c of C. For every u in R^m, J(uu^T)>=0 with top block uu^T, so c(uu^T) belongs to span(u), as the range of a PSD off-diagonal block must lie in the range of its diagonal principal block. Each component p_i(u)=c_i(uu^T) is homogeneous quadratic. The polynomial relations u_i p_j(u)-u_j p_i(u)=0 hold identically. Since u_i and u_j are relatively prime in R[u_1,...,u_m], for m>=2 these identities force p_i(u)=u_i ell(u) with a common linear homogeneous polynomial ell(u)=b^T u. Therefore c(uu^T)=u(b^T u)=(uu^T)b. Rank-one symmetric matrices span S^m, so c(X)=Xb for all symmetric X. Repeat over all k columns to get C(X)=XB. Congruence by [I -B;0 I] sends J(X) to X direct-sum [H(X)-B^TXB]. This block is PSD for every PSD X, hence T is positive. For m=1 the conclusion follows by direct linearity. QED.

## Theorem 2 — generic rank-one-generation covering lower bound

Define q=ell+k, with 0<=k<=s. A linear subspace W <= S^m is rank-one generated if it is spanned by matrices aa^T (the coefficients of linear combinations can have arbitrary sign).

Consider the Grassmannian G_I(ell,D) of ell-dimensional L containing I, of dimension
  dim G_I=(ell-1)(D-ell)=(ell-1)s.

The family of such L contained in SOME rank-one-generated W of dimension at most ell+k has semialgebraic dimension at most
  (ell+k)(m-1)+(ell-1)k.

**Proof.** Every rank-one-generated W of dimension q'<=ell+k can be extended to a rank-one-generated W of dimension q=ell+k: add independent rank-one projectors one at a time, possible because all rank-one projectors span S^m. Parameterize such q-dimensional W by q projective real vectors [a_j] in RP^(m-1), giving dimension at most q(m-1). For fixed W containing I, the family of ell-dimensional subspaces L with I in L subset W has dimension (ell-1)(q-ell)=(ell-1)k. Taking the incidence image cannot increase dimension. QED.

Therefore if
  (ell+k)(m-1)+(ell-1)k < (ell-1)s,     (*)
then a full-measure, semialgebraically generic set of trace-controlled L containing I is not contained in ANY rank-one-generated super-space of codimension gap <=k. In particular, its complement includes dense rational examples.

For ell=floor(D/2), s=D-ell and m sufficiently large, inequality (*) holds for every k<=s/2. Indeed the right-minus-left equals
 (ell-1)(s-k)-(ell+k)(m-1),
which for k<=s/2 is at least (ell-1)s/2-(ell+s/2)(m-1), positive of order m^4. Thus generic L requires k>s/2=Omega(m^2) to admit a rank-one-generated W containing L with dim W<=ell+k.

## Theorem 3 — quartic two-basis lower bound for positive diagonal-companion lifts

Suppose a finite two-orthonormal-basis PSD recovery problem represents the strictly feasible original fibre F_b for a given L and b=A(I) through a globally positive linear encoding
  J(X)=[ X C(X); C(X)^T H(X) ] in S^{m+k},
whose Schur-normal-form complement T(X) is DIAGONAL for every X, and whose full ambient fibre is exactly the embedded F_b after an isometric face compression. The decoder is the leading principal m-by-m block. Assume every compressed measured projector, after the fixed normalizing congruence from Theorem 1, factors through the source measurement map A (this is necessary if its value is constant along the relatively open source fibre around I).

Let transformed frame vectors be g_j=(a_j,b_j). Since
  T(X)=diag(<T_1,X>,...,<T_k,X>),  T_i>=0,
the source pullback of each compressed rank-one projector is
  a_j a_j^T + sum_i (b_j)_i^2 T_i in L.
Consequently a_j a_j^T belongs to W=L+span{T_i}, a space of dimension <=ell+k.

Because J(I)>0 on its m+k dimensional support (drop any zero T_i), exact fidelity at I requires the compressed measurement kernel to equal J(ker A). Its orthogonal complement contains every matrix supported on the original top-left block with top block H in L. Since all compressed measured projectors span this orthogonal complement, their top-left rank-one projectors a_j a_j^T span a subspace W' containing L. As every a_j a_j^T lies in W, W' is rank-one-generated and dim W'<=ell+k.

Choose generic L of ell=floor(D/2). Theorem 2 forces k>s/2=Omega(m^2). The compressed full-rank order d=m+k is thus Omega(m^2). The exact fibre through J(I) has affine tangent dimension s, so the restricted compressed measurement rank must be at least dim S^d-s. Since two orthonormal bases in ambient order N supply at most 2N-1 independent linear measurements,
  N >= [d(d+1)/2-s+1]/2 = Omega(m^4).

This lower bound also applies with a globally positive off-diagonal cross map C(X), because Theorem 1 congruence-eliminates it; rank-one projectors remain rank-one under congruence. It does NOT apply to non-diagonal matrix-valued positive companions, where the number of auxiliary source matrices is k(k+1)/2 rather than k.

## Consequences

1. The tensor-purification route and the entire class of globally positive principal-block-decoded diagonal-companion lifts BOTH generically require quartic ambient two-basis dimension.
2. An unrestricted near-quadratic theorem must use a genuinely matrix-valued positive companion T:S_+^m -> S_+^{O(m)}, a non-principal positive decoder, a nonlinear/feasible-fibre-specific embedding, or a different multistage PSD gadget.
3. A positive cross block cannot evade this obstruction: its form XB is forced and can be removed by a constant congruence.
4. The result is a dimension/geometry theorem, not a blanket complexity lower bound for SDP or a refutation of arbitrary two-basis universality.

## Adversarial audit

The dimension count is over measurement spaces containing I, not the full unconstrained Grassmannian; its dimension is (ell-1)s. The rank-one family uses projective vectors and arbitrary signed spans, so it is at least as broad as PSD frame-generated subspaces. The proof requires a strictly feasible source point to infer equality of linear kernels; b=A(I) supplies one. The nonzero diagonal auxiliary outputs at I ensure full-rank compressed image. The factorization condition for compressed projectors is necessary on a relatively open original fibre, and exact data equality implies it. The conclusion is architecture-specific, not universal.
