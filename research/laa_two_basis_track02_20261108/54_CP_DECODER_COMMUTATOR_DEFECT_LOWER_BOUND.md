# Milestone 54 — quantitative non-Jordan obstruction for GENERAL completely positive two-basis SDP decoders

Track 02, 2026-11-09. This is an independent channel-level theorem. It extends the ordinary partial-trace no-go of Milestones 49–53 to ANY *-preserving linear channel adjoint, and in particular to arbitrary CPTP/CP decoders, at the price of a precisely quantified commutator defect. No partial trace, tensor form, reflection, first-basis entanglement condition, or positive linear source encoder is assumed. The result is necessary, not sufficient, for a quadratic-size many-to-one normal form.

## 1. Definitions

Let L⊂S^m be a real source measurement space. For skew T∈so(m), put
  omega_T(H,K)=<T,[H,K]>_F, H,K∈L,
and define its uniform fourth-singular-value commutator margin
  gamma_4(L)=min_{||T||_F=1,T∈so(m)}sigma_4(omega_T|L).
Milestone 53 proves gamma_4(L)>0 for a full-measure open dense family of real L containing I_m with dimL>=m+3 (m>=4).

Let Φ:M_m(R)→M_N(R) be a real-linear map satisfying Φ(X^T)=Φ(X)^T, so it sends symmetric matrices to symmetric matrices and skew to skew. A completely positive Kraus-adjoint map Φ(H)=sum_a B_a^T H B_a is of this form. Let
  sigma_skew(Φ)=inf{||Φ(T)||_F:T∈so(m),||T||_F=1}
be its minimum skew-sector singular value, possibly zero.

Define its SOURCE COMMUTATOR DEFECT on L by
  delta_comm(Φ;L)
   =sup_{H,K∈L, ||H||_F=||K||_F=1}
        ||Φ([H,K])−[Φ(H),Φ(K)]||_op.
This is finite and computable by compact optimization. It vanishes for true algebra homomorphisms and real Jordan tensor amplifications Φ(H)=O(H⊗I_r)O^T.

## Theorem 1 — skew survival forces a nonzero commutator defect

Suppose TWO arbitrary real orthonormal-basis diagonal operator spaces D1,D2 on R^N obey
  Φ(L)⊂D1+D2.                                           (1)
Then
  delta_comm(Φ;L)
    >=gamma_4(L)*sigma_skew(Φ)
        *sqrt[(m(m−1)/2)/(N(N−1))].                       (2)

Consequently, if gamma_4(L)>0 and sigma_skew(Φ)>0, NO exactly commutator-preserving (Jordan) map Φ can place L inside the span of only two ONB diagonal algebras. Conversely, a two-basis-readable channel adjoint must pay in EITHER commutator distortion delta_comm OR a small skew-sector singular value sigma_skew. This is a direct, quantitative NECESSARY CONDITION for near-reversible positive decoder proposals.

## 2. Proof

Choose the first ONB ψ_1,...,ψ_N and a LINEAR splitting
  Φ(H)=A_H+B_H, A_H∈D1, B_H∈D2
for all H∈L. Such a linear splitting exists because finite-dimensional addition D1⊕D2→D1+D2 is surjective onto Φ(L). Put
  ell_ij(H)=<ψ_i,Φ(H)ψ_j>,
  f_ij(H)=<ψ_i,A_Hψ_i>−<ψ_j,A_Hψ_j>.
Commutativity of each diagonal algebra yields, for i<j,
  <ψ_i,[Φ(H),Φ(K)]ψ_j>
    =f_ij(H)ell_ij(K)−f_ij(K)ell_ij(H).
As a bilinear alternating form on L this has rank at most TWO.

Define T_ij∈so(m) by the Riesz formula
  <T,T_ij>_F=<ψ_i,Φ(T)ψ_j>
for EVERY skew T. Since Φ is *-preserving, Φ(T) is skew. Then
  omega_(T_ij)(H,K)=<ψ_i,Φ([H,K])ψ_j>.
The commutator defect assumption makes this bilinear form differ from a decomposable rank-two alternating form by at most delta_comm(Φ;L) in operator norm, uniformly for unit Frobenius H,K. By the rank-two singular-value approximation inequality,
  sigma_4(omega_(T_ij)|L)<=delta_comm(Φ;L).
By the definition of gamma_4 and homogeneity,
  gamma_4(L)||T_ij||_F<=delta_comm(Φ;L)       for all i<j. (3)

Now exploit the exact reduced-skew frame identity, valid for EVERY *-preserving Φ and EVERY complete real ONB ψ_i:
  sum_(i<j) <T,T_ij>_F²
    =(1/2)||Φ(T)||_F²                            (4)
for all skew T, because a real skew matrix has zero diagonal in any real ONB and its Frobenius norm squared is twice the sum of squares of its upper triangular entries.

Polarization identifies the frame operator of {T_ij} with (1/2)(Φ|so)* (Φ|so). Let k=dim so(m)=m(m−1)/2. Taking traces gives
  sum_(i<j)||T_ij||_F²
      =(1/2)||Φ|so||_HS²
      >=(k/2) sigma_skew(Φ)².
Since there are N(N−1)/2 pairs,
  max_(i<j)||T_ij||_F
      >=sigma_skew(Φ) sqrt[k/(N(N−1))].        (5)
Choose a maximizing pair in (3) to obtain (2). QED.

## 3. Special cases, interpretation, and exact frontier relevance

- **Ordinary partial trace.** Φ(H)=H⊗I_r has sigma_skew=sqrt(r) and delta_comm=0, so (2) recovers the exact impossibility of Milestones 49–53 for gamma_4(L)>0. The change of basis is arbitrary.
- **Unitary/Jordan amplification.** Φ(H)=O(H⊗I_r)O^T is exactly multiplicative and has sigma_skew=sqrt(r), so cannot fit a generic rich L into two MASAs, regardless of O.
- **Depolarizing channels.** Φ(H)=tr(H)I_N/m has sigma_skew=0, so (2) is correctly vacuous. Such a channel destroys the source observables and is not by itself a faithful universal recovery map.
- **General CP decoder.** For D(Y)=sum_a B_a YB_a^T, its adjoint Φ(H)=sum_a B_a^T H B_a is *-preserving. If the full two-basis PSD fibre has an interior feasible point and is SOUND for source constraints L under D, tangent duality forces (1). Thus any such design with a non-negligible σ_skew must have a correspondingly non-negligible commutator defect. A decoder that is almost reversible as an algebraic representation cannot simultaneously be almost noiseless in the commutator sense and two-basis-readable on L.
- **Ordinary source objective decoding** is not enough to satisfy (1); the inclusion follows from soundness on the ENTIRE affine fibre at a positive-definite lifted point, not merely from some algorithm's selected output.
- **Dimension scaling.** The factor sqrt[k/(N(N−1))] is asymptotically m/N. For N=O(m²), it is order 1/m. The result is a condition-controlled channel distortion lower bound; it does NOT forbid N=O(m²) when Φ is strongly non-Jordan or has σ_skew≈0.
- **Singular lifted face.** If a sound fibre has no full-rank ambient feasible point, only the compressed adjoint P_EΦ(H)P_E must lie in the compressed two-basis projector span. Those compressed rank-one frames need not be MASAs, so Theorem 1 does not apply without additional structure.
- **Novelty qualification.** This proof combines decomposable commutator forms with the tight-frame identity of real skew matrix coefficients. Standard matrix-channel and MASA ideas are antecedents; external literature priority and independent refereeing have not been completed.

## 4. Audit

1. The Riesz representatives T_ij are skew because the functional is tested on so(m); no assumption on Φ's restriction to symmetric matrices outside L is needed except transpose preservation.
2. The commutator [H,K] is skew for real symmetric H,K, so Φ([H,K]) is defined and skew.
3. The two-MASA commutator form uses a LINEAR splitting; this is guaranteed by finite-dimensional linear algebra, not by nonlinear minimization over decompositions.
4. The approximation is measured in BILINEAR operator norm; an entrywise inequality uniform for all unit H,K IS that operator norm, so no hidden dimL factor appears.
5. The reduced-skew matrix coefficients form a tight frame only when Φ|so is a scalar isometry; the general identity (4) correctly uses the positive Gram operator Φ*Φ and its least singular value.
6. Complete positivity and trace preservation are NOT needed for the algebraic theorem, but are natural sufficient hypotheses for the adjoint of a positive SDP decoder.
7. The theorem does not claim a new construction or unrestricted complexity-class lower bound.
