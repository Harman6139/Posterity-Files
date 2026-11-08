# Milestone 17 — exact two-MASA inclusion criterion and product-basis path obstruction

2026-11-08. This is a complete algebraic characterization of ONE load-bearing linear compatibility condition in a fixed first basis. It does not prove that arbitrary SDP fibres admit a quadratic two-basis shadow: exact surjectivity of the PSD fibres is a separate requirement.

## Theorem 1 — two-MASA inclusion iff diagonal commuting completion

Fix a real orthonormal basis B1 of R^n, and let D1 be its diagonal symmetric subspace. Let S<=S^n be a linear subspace with basis H_1,...,H_p. Then the following are equivalent:

(i) There exists a second real orthonormal basis B2 with diagonal subspace D2 such that S subset D1+D2.

(ii) There exist diagonal real symmetric matrices Delta_1,...,Delta_p in D1 such that the corrected matrices
   H_a-Delta_a,  a=1,...,p,
pairwise commute.

Proof. (i)=>(ii): for each a choose a decomposition H_a=Delta_a+B_a with Delta_a in D1 and B_a in D2. Since D2 consists of matrices diagonal in one basis, all B_a commute. (ii)=>(i): pairwise commuting real symmetric matrices admit a common orthonormal eigenbasis B2. Its diagonal subspace D2 contains every B_a=H_a-Delta_a, proving inclusion. QED.

Thus two-MASA compatibility with a prescribed first basis is an exact finite collection of quadratic polynomial equations in at most pn real diagonal variables. It can be checked by real algebraic elimination in principle, although no polynomial-time algorithm for arbitrary p,n is asserted.

## Theorem 2 — a three-vertex path obstructs a product first basis

Let m>=3, r>=1, n=mr. Let D1 be the standard product-basis diagonal on R^m tensor R^r, or any orthonormal basis obtained by rotations WITHIN the coordinate groups e_i tensor R^r, so every D1-diagonal matrix is block diagonal for the group decomposition.

Let S be a source observable space containing
  H_12=(e_1e_2^T+e_2e_1^T) tensor I_r,
  H_23=(e_2e_3^T+e_3e_2^T) tensor I_r.
Then no second orthonormal basis satisfies
  S subset D1+D2.

Proof. Suppose H_12-Delta_12 and H_23-Delta_23 commute for some Delta_12,Delta_23 in D1. Each Delta is block diagonal for the three source groups. Take the (group 1,group 3) block of their commutator. Since H_12 connects only groups 1 and 2, and H_23 connects only groups 2 and 3, the (1,3) block of [H_12,H_23] equals I_r. The commutators [H_12,Delta_23], [Delta_12,H_23] have support only on group edges (1,2) or (2,3), while [Delta_12,Delta_23] may be nonzero inside groups but has zero (1,3) block. Therefore the (1,3) block remains I_r and cannot vanish, contradicting commuting completion. QED.

This applies to the partial-trace decoder D(Y)=Tr_aux(Y), for which the adjoint source observables are H tensor I_r. It shows that taking the first basis to be an ordinary product basis and hoping the second basis can supply all source off-diagonal constraints is impossible already for a length-two path.

## Quantitative bottleneck

In the maximally-entangled first basis of Milestone 14, every trace-zero H tensor I_r has ZERO first-basis diagonal, so the product-basis obstruction no longer directly applies. However Theorem 1 still requires diagonal corrections Delta_a in the ENTANGLED basis making all corrected operators commute. That system is nonlinear and is not solved by merely having rank-one reduced POVM elements span L. Both conditions are required for exact marginal detection from two basis data.

## Relationship to exact PSD surjectivity

Let D:S^n -> S^m be a fixed positive linear decoder, let L=range A* and let T={Y>=0:A_U(Y)=y} have a positive-definite feasible point on its minimal support. If D(T) subset {X:A(X)=b}, then tangent duality necessarily gives
 D*(L) subset D1+D2
on that minimal support. Theorem 1 characterizes this NECESSARY linear inclusion. It does not by itself establish D(T)=F_b, because a separate lifting argument must show that every source PSD feasible point has an ambient PSD preimage with the prescribed two-basis data.

## Hostile audit

- We require a common diagonal correction for each basis vector H_a, not merely that the reduced POVM statistics span the source measurement space. Those are different conditions.
- The product-basis obstruction is unchanged under arbitrary per-group auxiliary orthogonal changes, because the diagonal correction remains group block-diagonal.
- The commutator [Delta_12,Delta_23] need not vanish if group-local rotations differ; only its (1,3) group block is used.
- The lemma is valid for REAL symmetric matrices; common orthogonal eigenvectors exist by the real spectral theorem.
- The theorem is not an impossibility for ALL possible first bases, nor for other positive/nonlinear decoders.
