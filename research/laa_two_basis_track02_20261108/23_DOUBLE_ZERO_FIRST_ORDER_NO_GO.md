# Milestone 23 — exact cross-image rank and first-order cancellation obstruction for the double-zero Naimark dilation

Date 2026-11-08. This gives an exact sharp linear-algebraic obstruction for the construction in Milestone 21. It explains why exact two-basis fibres need not preserve the source noisy recovery modulus, even though the bases have no zero overlaps.

## 1. Rank theorem for compressed/exterior cross measurements

Let G in R^{d x M}, GG^T=I_d, and K in R^{(M-d) x M} complete [G;K] to an orthogonal matrix. Let P=G^T G be the M-by-M Gram projector and z=M-d. Define the source/exterior cross-analysis map
  T_G:R^{d x z} -> R^M,
  T_G(X)=diag(G^T X K).

Define the undirected Gram support graph Gamma(P) on {1,...,M}, with an edge {i,j} whenever P_ij!=0. Let c(P) be its number of connected components.

**Theorem 1.**
  rank T_G = M-c(P).
Equivalently, the left kernel of T_G consists exactly of vectors lambda in R^M that are constant on each connected component of Gamma(P). In particular, if Gamma(P) is connected, then
  ran T_G={v in R^M:1^T v=0}.

**Proof.** The adjoint map sends lambda to
  T_G*(lambda)=G diag(lambda) K^T.
This vanishes iff P diag(lambda)(I-P)=0, because G,K are isometries identifying ran P and ker P. Since diag(lambda) is symmetric, vanishing of this off-block part is equivalent to [P,diag(lambda)]=0. Its (i,j) entry is P_ij(lambda_j-lambda_i). Thus the commutator vanishes iff lambda is constant across every edge of Gamma(P), equivalently on each connected component. The dimension of the adjoint nullspace is c(P), so rank T_G=M-c(P). Also 1 is always in the left kernel since GK^T=0. QED.

This theorem requires NO random genericity. A generic tight frame with nonzero pairwise inner products has connected Gamma(P), but many deterministic frames (including the tetrahedron) do too.

## 2. Exact output cross-image of the two-zero two-basis construction

Use Milestone 21 with d<M and N=2M-d. The embedded support V has dimension d and its exterior Q has orthogonal decomposition Z_2 direct-sum Z_1, each of dimension z=M-d. In the unrotated bases, the two nonzero measurement lists on an embedded source perturbation H in S^d equal
  (M_G(H), M_G(H)) in R^M direct-sum R^M,
while the zero columns carry no source signal.

Every source/exterior cross block has two independently selectable matrices X_1,X_2 in R^{d x z}, supported on V-to-Z_2 and V-to-Z_1. The first nonzero measurement-list cross term is 2 T_G(X_1); the second is 2 T_G(X_2). The two zero-output slots in the respective lists vanish to first order for any cross term, because the corresponding basis vectors lie entirely in Q.

If Gamma(P) is connected, the full cross-data image on the nonzero positions is EXACTLY
  K_out=1^perp direct-sum 1^perp.
Its dimension is 2(M-1). An arbitrary orthogonal change of basis inside Q (used in Milestone 21 to make all transition entries nonzero) is an invertible linear change of the cross-block input parameters and does not alter this image.

Meanwhile the embedded source-data subspace is
  V_out={(v,v):v in ran M_G}.
Since the frame is Parseval, 1^T M_G(H)=tr H, and M_G has rank q=dim span{g_jg_j^T}. Therefore
  V_out intersect K_out
    = {(v,v):v in ran M_G, 1^T v=0}
has dimension q-1.

**Corollary.** If q>=2, the cross/source transversality margin from Milestone 22 is ZERO for this two-zero dilation, regardless of the exterior rotation used to remove basis overlap zeros. No bounded linear operator on the two lists can recover the entire compressed source residual while annihilating every first-order off-face cross signal. The only universally transverse source observable is the TRACE.

This is a complete explanation of the Milestone 21 noise-estimate caveat; one cannot upgrade its omega_source(C sqrt(delta)) term to omega_source(C delta) merely by an averaging identity or a linear decoder.

## 3. Explicit first-order hiding curve at a positive-definite source

Assume Z_*>0 on R^d and q>=2, and Gamma(P) connected. Choose any nonzero H in S^d with tr H=0 and M_G(H)!=0. Put r=M_G(H), so 1^T r=0. By Theorem 1 choose X_1,X_2 with
  2 T_G(X_1)=-r,   2 T_G(X_2)=-r.
Let K_0 be the corresponding V-to-Q cross block, and let A=F_0^T H F_0. Then
  B(A+K_0+K_0^T)=0
for the complete two-basis measurement map B. The first-order perturbation has a nonzero compressed H component.

For sufficiently small t>0, choose a fixed positive-definite G_Q on Q satisfying
  G_Q >= 2 K_0^T (F_0^T Z_* F_0)^dagger K_0
on Q. Then
  Y(t)=F_0^T(Z_*+tH)F_0 +t(K_0+K_0^T)+t^2G_Q
is PSD for all sufficiently small t, by the Schur complement (the positive source block Z_*+tH remains uniformly positive definite). Its two-basis residual is EXACTLY
  B(Y(t)-Y_*)=t² B(G_Q),
while its decoded source error is ||F_0Y(t)F_0^T-Z_*||_F=t||H||_F.

Because G_Q>=0 and trace is measured, B(G_Q)!=0. Thus
  t||H|| ~ sqrt(||B(Y(t)-Y_*)||).
Even at a strictly feasible source point, the two-basis data can hide an O(t) source displacement behind O(t²) residual. When the original source map is injective (q=D_d), its source recovery modulus is Lipschitz but its rank-d lifted target is uniquely recoverable with sharp exponent 1/2 (the Milestone 21 upper bound gives the matching upper exponent).

The same construction works after the generic exterior rotation because the cross-data image remains unchanged. It demonstrates that the extra square root is an actual geometric mechanism, not just a proof-estimate artifact.

## 4. Scope and hostile audit

- The left-kernel formula is exact and depends on Gram-projector connectivity; no approximate rank argument is used.
- The full cross-output image is a direct sum because the two exterior subspaces Z_1,Z_2 are independent. An exterior rotation changes input coordinates but not which output vectors can be generated.
- The source residual trace vanishes for H by construction, so its first-order signal is in the cross image. Trace alone cannot be canceled by off-face cross blocks.
- The Schur complement repair uses the positive-definiteness of Z_*, and G_Q can be chosen fixed, so the error scaling is rigorously quadratic.
- The result does NOT claim every singular-source non-Lipschitz exponent is halved; such claims would require controlling the smallest positive eigenvalue along singular source curves.
- The original double-zero exact-fibre theorem remains valid and has no rank restrictions. The failure is quantitative FIRST-ORDER data separation, not exact feasibility.
- The new transversality criterion of Milestone 22 is sufficient, and this theorem exhibits a natural general construction where it fails maximally for all trace-free source signals.
