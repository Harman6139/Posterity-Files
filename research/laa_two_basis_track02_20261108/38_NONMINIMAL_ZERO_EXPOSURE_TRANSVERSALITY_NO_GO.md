# Milestone 38 — the 2d−1 stability ceiling holds for ALL zero-only two-basis exposure, even with arbitrary redundant ambient dimensions

Date: 2026-11-08. This closes a loophole in Milestone 25. Its sharp cross-image formula assumed a minimal two-zero Naimark dilation of order N=M_1+M_2−d. The SAME exact first-order information ceiling remains valid for ANY two-basis design of arbitrary order N, as long as the target face is exposed solely by zero observations in the two lists. Adding redundant zero coordinates cannot restore first-order stability.

## Theorem (arbitrary-dimensional zero-only exposure)

Let V be a d-dimensional subspace of R^N. Let B_1,B_2 be any two real orthonormal bases. For i=1,2, let Z_i⊂V^perp be the span of the basis vectors whose target observations are zero, and assume
  Z_1+Z_2=V^perp.
This is the exact condition that those zero outcomes alone expose the desired PSD face V: a positive semidefinite matrix with every such zero expectation has support inside (Z_1+Z_2)^perp=V. No minimality of N, no transversality of the two zero subspaces, and no signed exposing certificate are assumed.

Write M_i=N-dim Z_i. Project the remaining M_i basis vectors onto V; they form rank-one Parseval frames G_i of R^d (after an orthonormal identification V≅R^d). Let P_i=G_i^T G_i, and let c_i be the number of connected components in the graph on these M_i frame indices with edges whenever (P_i)_{jk}!=0. Assume all projected columns are nonzero (if any are zero, move that vector into Z_i first).

Let L_src:S^d→R^(M_1+M_2) be the concatenated two-frame rank-one analysis map, with rank q. Then the full output image of *first-order source-to-exterior cross blocks* in the two nonzero data lists is exactly
  (1_{M_1}^perp componentwise within each Gram graph) direct sum
  (1_{M_2}^perp componentwise within each Gram graph),
of dimension
  (M_1−c_1)+(M_2−c_2).
The quotient image of the source-data map modulo this exterior-cross image has dimension at most
  c_1+c_2−1 <=2d−1.                           (1)

In particular, if q>2d−1, there is a source perturbation H with nonzero measured source data and an exterior cross block K such that
  B(H_embedded+K+K^T)=0
to FIRST order in both complete basis diagonals, including every measured zero slot.

If the compressed target Z_*>0, this cancellation admits an actual PSD curve Y(t), with
  ||B(Y(t)-Y_*)||=Theta(t²),
  ||L_src(D(Y(t))-Z_*)||=Theta(t),
where D is orthogonal PSD-positive compression onto V. Thus an O(delta) decoded source residual estimate is impossible in this entire zero-only exposing architecture, irrespective of N. The construction need not be a reflection and may have no zero overlap between the two bases.

The theorem is architecture-restricted: a signed positive stress with nonzero target outcomes (as in Milestone 35), or a many-to-one PSD quotient with noncanonical decoder, is outside it.

## Proof

1. Each Z_i is spanned by a subset of an orthonormal basis, hence E_i:=Z_i^perp contains V. Its orthogonal complement to V is
  R_i:=E_i∩V^perp
and has dimension M_i−d. The first M_i surviving basis vectors form an ONB of E_i, and their projections onto V give Parseval G_i with complementary Naimark frame living in R_i.

2. The zero-only exposure condition implies R_1∩R_2={0}: indeed
  R_1∩R_2=(Z_1+Z_2)^perp∩V^perp=V∩V^perp={0}.
This identity holds EVEN if Z_1∩Z_2 is nonzero (which occurs when N>M_1+M_2−d). The subspaces R_1,R_2 are linearly independent, although they need not be orthogonal.

3. A source-to-exterior first-order cross perturbation is a linear map K:V^perp→V. Its output in basis i depends only on K|_{R_i}. Because R_1∩R_2={0}, the two restrictions K|_{R_1} and K|_{R_2} can be prescribed INDEPENDENTLY and extended linearly to V^perp (choose a basis of R_1+R_2 and extend it).

4. For either frame G_i, complete it with its Naimark complement K_i in R_i. The output cross map is
  T_i(X)=diag(G_i^T X K_i), X∈R^{d×(M_i−d)}.
The adjoint satisfies
  T_i*(lambda)=G_i diag(lambda) K_i^T.
As in Milestone 23, this vanishes exactly when the diagonal matrix diag(lambda) commutes with P_i=G_i^T G_i. Entrywise the condition is (lambda_j−lambda_k)(P_i)_{jk}=0. Thus lambda is constant on each Gram-support graph component, giving rank T_i=M_i−c_i. Step 3 proves the TOTAL cross image is their independent direct sum.

5. Both frames are Parseval, so the sum of measurements in either frame equals tr H for every symmetric H. Modulo the cross image, each frame contributes c_i component-sum coordinates; their two total sums have the SAME value. Therefore the joint source image in this quotient has dimension at most c_1+c_2−1. Every graph component spans a nonzero orthogonal subspace of R^d, so c_i<=d. This proves (1).

6. If q>c_1+c_2−1, choose a source H with L_src(H)!=0 but with both source lists in the exterior-cross images. By steps 3-4 choose K making all first-order data zero. All zero-observation slots receive no first-order cross or source data, because their basis vectors lie entirely in V^perp.

7. For a strictly positive compressed source Z_*, let Y_*=embedding(Z_*) on V. Choose any fixed positive definite A_Q on V^perp large enough that
  A_Q>=2 K^T Z_*^{-1} K.
Then
  Y(t)=[ Z_*+tH, tK;
         tK^T,      t² A_Q ]
is PSD for all sufficiently small t>0, by its Schur complement. The first-order measured change cancels exactly, leaving
  B(Y(t)-Y_*)=t² B(A_Q).
Since trace is measured, B(A_Q)!=0. Orthogonal compression decodes Z_*+tH, whose source measurement error is t||L_src(H)||>0. Thus there is no uniform O(delta) source-data decoder through the two complete basis lists. QED.

## Quantitative and conceptual consequences

- Merely enlarging N while preserving a zero-only exposure mechanism CANNOT restore the sharp even/odd cancellation of the signed positive-stress method.
- The number 2d−1 is an exact information ceiling for separating source measurements from off-face cross terms in every two-zero exposing design; for connected Gram graphs (c_1=c_2=1), only source TRACE survives first-order quotient.
- The theorem does NOT imply every such system worsens a singular source's optimal exponent. It proves cancellation of source data at a positive-definite source point, and Milestone 26 gives an explicit singular-source family where this leads to optimal exponent halving.
- The zero-support subspaces may have nontrivial intersection and the bases may be arbitrarily entangled. No minimal Naimark-completion coordinate form is assumed, closing the principal scope loophole in Milestone 25.
