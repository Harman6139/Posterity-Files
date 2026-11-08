# Milestone 18 — any real fixed-diagonal universal density-state shadow needs mixed pure-state lifts

2026-11-08. This is a model-independent necessary condition for ANY finite real two-basis or even one-basis PSD fibre projecting surjectively onto the full trace-one density-matrix body by an arbitrary linear decoder. It does not assume a positive encoder or a reflection.

## Theorem A (finite rank-one points on a real fixed-diagonal PSD fibre)

Let a=(a_1,...,a_N) with a_j>=0. The set
  T_a^(1)={Y in S^N_+:rankY=1, diag Y=a}
contains at most 2^(k-1) matrices, where k=# {j:a_j>0}. For k=0 it contains no nonzero rank-one matrices. For k>=1, the bound is attained.

**Proof.** A nonzero real rank-one PSD Y equals vv^T. Its diagonal equations give v_j^2=a_j. Thus for each positive coordinate v_j is one of two numbers +/-sqrt(a_j), and for zero coordinates v_j=0. Vectors v and -v determine the same matrix. There are exactly 2^(k-1) distinct matrices, proving the claim.

If an additional orthonormal-basis diagonal is fixed, the rank-one locus is a subset, so the same bound holds.

## Theorem B (mixed lifts are unavoidable for universal density-state quotients)

Let m>=2, tau>0 and let T subset S^N_+ be any family with a fixed first-basis diagonal (after an orthogonal coordinate change, diagY=a). Let D:S^N -> S^m be ANY map that is a single-valued function on T, in particular any positive linear or completely positive decoder. Assume
  D(T)={X in S^m_+:tr X=tau}.
Then for all but at most 2^(k-1) projective unit vectors [u] in RP^(m-1), every preimage Y in T of tau uu^T has rank at least two. Indeed the rank-one members of T form a finite set, so their images under D form a finite set, whereas the source pure-state manifold RP^(m-1) is infinite.

**Consequence.** The real two-basis fibre must have genuinely mixed extensions of almost every pure source state. No architecture with a rank-one preimage for every pure state can realize the full trace-one density-body shadow with fixed first diagonal.

## Corollary C (CP decoder nullspace condition)

Suppose D is completely positive with Kraus matrices B_a:R^N ->R^m, a=1,...,t. If Y>=0 satisfies
  D(Y)=tau uu^T,
then
  supp Y subset K_u := intersect_{a=1}^t {v in R^N:B_a v in span(u)}.
Proof. Put P_u=I-uu^T. Then tr(P_u D(Y))=sum_a tr((P_u B_a)Y(P_u B_a)^T)=0. Each summand is nonnegative, hence P_u B_a Y^(1/2)=0 for all a. Thus every vector in ran Y lies in K_u.

Therefore, under the hypotheses of Theorem B and for all but finitely many pure source states [u],
  dim K_u>=2.
Equivalently, the stacked t(m-1)-by-N matrix of constraints P_u B_a has rank at most N-2 for all but finitely many u.

This imposes exact correlated kernel identities on any high-Kraus CP decoder used for a universal real trace-only shadow. It is not satisfied by a generic independent family of Kraus matrices when t(m-1)>=N-1; such a generic family has dim K_u<=1 for generic u. The latter generic observation is a straightforward full-rank-minor fact, not a universal lower bound on N or t.

## Audit / limits

- Positivity of the decoder is NOT needed for Theorem B; only surjectivity and the fixed first-basis diagonal are used.
- The rank-one finiteness uses REAL vectors. Over complex Hilbert space the fixed magnitudes leave continuous phases, so this argument would require a different statement.
- The theorem is for the trace-only source fibre that contains all pure states, not generic intermediate affine fibres that may contain none.
- It explains why the symmetric-square marginal in Milestone 15 cannot be used directly with fixed basis data: that map has unique rank-one lifts for every pure source state.
- It does not rule out high-rank mixed extensions; the maximally entangled first-basis construction of Milestone 14 provides them.
