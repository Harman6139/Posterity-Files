# Milestone 01 — a generic quartic lower bound for tensor-purification two-basis normal forms

Date 2026-11-08. This is a proved *architecture-restricted* obstruction, NOT a no-go theorem for unrestricted two-basis SDP representation.

## Definitions

Let m>=2 and D=m(m+1)/2. Fix 1<=s<=D-2. Let Gr_I(D-s,S^m) denote the real Grassmannian of codimension-s linear subspaces L of S^m that contain I_m. It is a smooth real algebraic manifold of dimension s(D-s-1). Every such L gives a trace-controlled PSD inverse problem: choose a basis of L as measurement matrices, so I is measured and b=A(I) admits the positive-definite solution I.

For 1<=r<m, let V_r be the projective determinantal variety of nonzero complex symmetric m-by-m matrices of rank at most r. Its complex projective dimension is
  v_r = mr-r(r-1)/2-1.

## Theorem 1 (generic absence of low-rank matrices)

If s>v_r, then a Zariski-open dense subset of codimension-s subspaces L containing I contains no nonzero real symmetric matrix of rank at most r. In particular it contains no nonzero PSD matrix of rank <=r.

**Proof.** Work first over C. Since I has rank m>r, the variety V_r avoids [I]. Let G be the Grassmannian of projective (D-s-1)-planes through [I] in P^(D-1). The dimension of G is s(D-s-1). For each fixed [X] in V_r, containing both [I] and [X] reduces the dimension by exactly s, because after quotienting by span(I), the condition that a (D-s-1)-dimensional vector subspace contain the fixed independent class [X mod I] has codimension s. Hence the incidence
 Z={(L,[X]):L in G, [X] in V_r, [X] in P(L)}
has dimension at most dim(G)-s+v_r<dim(G). Its image is closed under the projective projection, and is proper. Its complement is a nonempty Zariski-open set, defined over R. Real Grassmannian points are Zariski dense (the standard affine charts have real open cells), so this open set contains a Euclidean-open dense collection of real L. For these L the claimed rank-r intersection is empty. QED.

## Corollary 2 (purification ancilla lower bound)

For generic L as in Theorem 1, any nonzero vector g=vec(V) in R^m tensor R^r for which its rank-one projector gg^T has allowed source partial trace must obey
  T(gg^T)=V V^T in L,  V V^T!=0,  rank(V V^T)<=r.
Therefore no such vector exists if s>v_r.

In particular, for s=floor(m^2/4), there is a generic trace-controlled L for which EVERY admissible purification requires r>m/5 for all sufficiently large m. Consequently compressed tensor order d=mr is Omega(m^2). This applies to every exact rank-one frame compiler whose source pullback is the ordinary partial trace, independently of its choice of weights, sampling, Naimark completion, or basis rotations.

## Corollary 3 (quartic two-basis order within tensor-face embeddings)

Suppose a two-basis recovery problem has an exact affine fibre model
 E(X)=F^T[(X tensor I_r) direct-sum [a]]F
with FF^T=I_{mr+1}, a>0, and the original measurement space L is generic as above, with b=A(I). Suppose every compressed rank-one measurement factors through A (a necessary condition when it is constant on the whole exact fibre). Then r=Omega(m) by Corollary 2.

Even without the factorization hypothesis, any two-basis fibre equal to E(F_b) has ambient dimension
  N >= (dim S^(mr+1) - dim ker A + 1)/2.
Indeed the model contains E(I)>0 on its (mr+1)-dimensional compressed face. The exact affine fibre has tangent dimension dim ker A=s at E(I), while the compressed measured linear map has rank at least dim S^(mr+1)-s. Two orthonormal bases on ambient order N give at most 2N-1 independent linear measurements, proving the bound. Hence N=Omega(m^4) for the generic L above.

**Caution.** This theorem does NOT imply a universal quartic lower bound outside the tensor-face architecture, nor does it obstruct positive companion embeddings of effective compressed order O(m). It identifies why reducing the ancilla of the prior tensor compiler alone cannot solve unrestricted near-quadratic universality.

## Numerical sanity check (optional)

For m=20, s=floor(m^2/4)=100. The rank-r projective dimension is v_r=20r-r(r-1)/2-1. For r=5, v_r=89<100; no rank<=5 symmetric matrix lies in a generic codimension-100 subspace through I. For r=6, v_r=104>=100, so this dimension obstruction no longer applies. This is a threshold for this elementary incidence argument, not proof of existence at r=6.

## Research consequence

The unrestricted O(m^2+p) program must escape the tensor-positive-rank-one-pullback architecture. The natural alternatives are (a) a non-tensor order-retract J:S_+^m -> S_+^{O(m)} admitting a rank-one-generated measurement operator system, or (b) a multi-stage non-face-embedded two-basis gadget whose auxiliary matrix variables are controlled without imposing Omega(d^2) independent measurements.
