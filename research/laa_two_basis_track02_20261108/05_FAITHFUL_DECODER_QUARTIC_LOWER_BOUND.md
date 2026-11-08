# Milestone 05 — a generic quartic lower bound for ALL faithful positive retracts

2026-11-08. This strengthens the tensor-specific no-go: it applies to ANY globally positive linear encoder J and globally positive linear decoder D with a faithful decoder on the encoded support. The conclusion remains architecture-relative; it does NOT rule out nonfaithful positive decoders, which are the essential freedom in matrix-valued companion constructions.

## Definitions and hypotheses

Let m>=2, D_m=m(m+1)/2 and s=floor(m^2/4). Let L <= S^m be a generic codimension-s linear subspace containing I_m. Let A be a linear measurement map with range(A*)=L, and take b=A(I_m), so F_b contains a positive definite original matrix.

Suppose J:S^m -> S^d and Delta:S^d -> S^m are positive linear maps such that Delta J=id and J(I_m)>0 in S^d. Assume the decoder is **faithful**:
  Delta(Y)=0 and Y>=0 imply Y=0.
Equivalently, Delta*(I_m)>0.

Suppose a two-orthonormal-basis problem on S^N_+ has a face isometry F with FF^T=I_d, and encoded solutions F^T J(X) F, X in F_b, comprise its ENTIRE exact PSD fibre. Assume every individual two-basis measurement on embedded inputs depends only on A(X), a consequence of exact equality along the relatively open fibre near I.

## Theorem — quartic lower bound for faithful decoders

For all sufficiently large m and generic L as above,
  d=Omega(m^2),  N=Omega(m^4).

**Proof.** Apply the Jordan-amplification rigidity theorem from Milestone 04. Because Delta is faithful on S^d, its adjoint effect has full support, so after congruence normalization J(I_m)^(-1/2) and an orthogonal change of coordinates, the map J becomes exactly
  J(X)=X tensor I_t
on S^{mt}, with d=mt, t>=1. An arbitrary ambient rank-one basis projector, compressed to this face and conjugated by the normalizing congruence, pulls back through J to VV^T for an m-by-t matrix V. This is PSD of rank at most t.

Every such pullback lies in L: for any K in ker A, I+epsilon K>=0 for sufficiently small positive and negative epsilon, and exact fibre equality requires every coordinate measurement to be constant on those embedded points. Hence the pullback annihilates ker A. Since some compressed basis column is nonzero (their sum is the identity on the face), L contains a nonzero PSD matrix of rank at most t.

By the projective determinantal incidence theorem from Milestone 01, a generic L of codimension s contains no nonzero symmetric matrix of rank <=r when
  s>v_r=mr-r(r-1)/2-1.
For r=floor(m/5) and all sufficiently large m, v_r < s=floor(m^2/4). Therefore t>m/5, so d=mt=Omega(m^2).

At the point F^T J(I) F the encoded matrix is positive definite on the d-dimensional face. The source exact affine fibre has tangent dimension dim ker A=s. If the compressed measurement linear map had kernel larger than the embedded J(ker A), a nonzero additional kernel direction H could be added to this positive definite target for small positive and negative parameters, producing ambient PSD exact solutions outside the encoded fibre. Thus the compressed two-basis measurement rank is at least
  d(d+1)/2-s.
Two bases on order N supply at most 2N-1 independent linear measurements; consequently
  N >= [d(d+1)/2-s+1]/2 = Omega(m^4).
QED.

## Corollary — an exact kernel is necessary in every positive quadratic architecture

In any family of positive retract encodings of generic dense SDPs with d=O(m) and N=O(m^2), the decoder's effect Delta*(I) MUST have a nontrivial kernel on the full support of J(I). It is not enough merely to make its smallest eigenvalue small: faithfulness is a qualitative, algebraically sharp obstruction. The extra matrix-valued companion must be invisible to the decoder on a genuine positive-dimensional support.

This is compatible with the positive principal-block decoder J(X)=X direct-sum T(X), Delta(Y)=Y_top-left, whose adjoint effect vanishes on the whole auxiliary block.

## Hostile audit

- Faithfulness is tested on the full compressed S^d_+ cone and is equivalent to positive definiteness of Delta*(I), not injectivity of Delta as a linear map.
- The Jordan structure is exact only after normalizing J(I) and, if necessary, compressing to support of Delta*(I). Here faithfulness makes that support the whole compressed space.
- Nonzero PSD low-rank pullback is guaranteed by the Parseval identity of compressed first-basis columns. A zero compressed column does not affect the argument.
- The dimension count uses the fact b=A(I) contains a relative open neighbourhood of I in the affine fibre, not just one isolated feasible point.
- The genericity and incidence rank estimate are proved in Milestone 01. No assumption on rationality of the generic L is necessary; the generic nonempty open class includes rational points by density.
- The conclusion does NOT cover positive decoders with a kernel on PSD, nonlinear decoders, nonlinear embeddings, or non-face-embedded affine correspondences.
