# Milestone 10 — generic linear Kraus-rank lower bound for completely positive encoders

Date 2026-11-08. This is a rigorous architecture-sensitive result. It is independent of whether the decoder is positive or whether the encoder is injective.

## 1. Theorem

Let m>=2, let L<=S^m contain I and have codimension s=floor(m^2/4), and choose a generic L in the Zariski-open set from Milestone 01. For every integer r with
  mr-r(r-1)/2-1 < s
there is no nonzero PSD matrix in L of rank <=r.

Suppose J:S^m -> S^d is a completely positive real linear map with Kraus decomposition
  J(X)=sum_{a=1}^R A_a X A_a^T,
where A_a are real d-by-m matrices. Suppose there is a family of nonzero rank-one measurement vectors v_j in R^d such that:
(a) the outcome v_j^T J(X)v_j is constant as X ranges over the relatively open source fibre {X>0:A(X)=A(I)} for each j; and
(b) their projectors span the support of J(I) (for example the vectors form a Parseval frame of that support).

Then necessarily
  R > r.
In particular R>=floor(m/4) for all sufficiently large m, so bounded or sublinear Kraus-rank completely positive encoders cannot provide universal exact data-faithful rank-one compilers on generic dense inputs.

**Proof.** Condition (a) implies that the pullback
  B_j=J*(v_j v_j^T)
lies in L, because every H in ker A is an admissible first-order perturbation of I of both signs. Complete positivity gives
  B_j=sum_{a=1}^R (A_a^T v_j)(A_a^T v_j)^T>=0,
hence rank B_j<=R. Since J(I) is nonzero on its support and the projectors span that support, at least one B_j is nonzero (indeed sum of its trace is positive). By the generic rank-avoidance theorem, rank B_j>r. Thus R>r. QED.

The sharp asymptotic obstruction from the incidence inequality is
  R/m >= 1-1/sqrt(2)-o(1) ~ 0.292893...
because mr-r(r-1)/2 < m^2/4 is equivalent asymptotically to r/m-(r/m)^2/2<1/4.
This is an obstruction threshold, not a claim that Kraus rank immediately above the threshold suffices.

## 2. Corollary for CP matrix-valued companions

Consider an exact affine positive retract encoding
  E(X)=F^T[(X direct-sum T(X)) direct-sum [a]]F
with positive companion T:S_+^m -> S_+^k. If T is completely positive with Kraus rank R_T, then the source-dependent linear part has a CP Kraus decomposition with at most R_T+1 terms. If every embedded two-basis measurement factors through A for all source matrices near I in the affine fibre, its nonzero rank-one pullbacks require
  R_T+1 >= (1-1/sqrt(2)-o(1))m.
In particular a CP companion with o(m) Kraus operators cannot evade the earlier tensor/diagonal lower bounds for generic dense L. The more general positive but not completely positive companion remains a viable direction.

## 3. Important scope

This theorem does not obstruct a CP encoder with R=Theta(m), a general positive non-CP encoder, a linear decoder with auxiliary nonunique feasibility, or a nonlinear b-dependent encoding. It is a quantitative condition on the common special case in which EACH embedded basis outcome is a function only of the original measurement data along the whole strictly feasible source fibre.

The result is valid for arbitrary real (not only algebraic) coefficients; the generic set includes rational L by density. No assumption on basis reflection or distinctness is used.

## 4. Adversarial audit

- J*(vv^T) is PSD because J is CP; the rank bound is exactly the Kraus count. This need not hold for merely positive maps.
- The source fibre uses b=A(I) and contains I+/-epsilon H for every H in ker A, making factorization into membership in L rigorous.
- At least one pullback is nonzero because the measurement vectors span the support of J(I). This avoids the vacuous case where all measurement outcomes are anchor-only.
- The numerical threshold uses s=floor(m^2/4), and only claims the asymptotic ratio 1-1/sqrt 2.
- Even with a fixed positive affine anchor E(X)=J(X)+A0, subtracting two points in the same source fibre removes A0 and gives the same condition on J*.
