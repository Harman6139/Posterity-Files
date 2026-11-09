# Milestone 47 — generic QUARTIC lower bound for ALL bounded-block trace-complement positive lifts

Date 2026-11-08. Complete, elementary architecture-restricted no-go theorem. Extends the two-block failure in Milestone 46 to ANY finite number of positive trace-affine congruence blocks. Thus merely adding a constant or sublinear number of balanced companions (including the three-block construction of Milestone 34) cannot yield a universal quadratic-size representation of generic dense PSD inverse problems, regardless of how many rank-one POVM outcomes or external Naimark coordinates are used. It does NOT rule out general matrix-valued positive companions or many-to-one PSD shadows.

## Setup

Let m>=3 and D_m=m(m+1)/2. Let L<=S^m be a linear measurement subspace containing I_m and with dimension ell>=2, codimension s=D_m−ell. Fix a source measurement map A with range(A*)=L and strictly feasible datum b=A(I_m).

Fix k>=1 and real scalars alpha_j,beta_j and orthogonal m-by-m matrices U_j such that
  beta_j>=max{0,−alpha_j},  (alpha_j,beta_j)!=(0,0)
for j=1,...,k, and assume AT LEAST ONE alpha_j is nonzero. This is necessary for a faithful source encoding; if every alpha_j=0, the map depends only on trace and collapses all trace-preserving source perturbations. Define the globally cone-positive linear lift
  J(X)=direct_sum_(j=1)^k [beta_j tr(X) I_m+alpha_j U_j X U_j^T]
from S^m to S^(km). Each block is PSD whenever X>=0:
if alpha_j>=0 it is plainly PSD, while if alpha_j<0 then the eigenvalues of X are bounded by trX and beta_j>=−alpha_j.

The same argument applies to the AFFINE anchored lift J_a(X)=J(X) direct-sum [a] for any fixed a>0. The anchor does not enter the source-dependent pullbacks.

Assume an EXACT rank-one measurement representation on the compressed face:
each rank-one projector vv^T among the compressed measurements has its outcome constant on J_a(F_b), and the ENTIRE compressed PSD fibre of those outcomes is J_a(F_b). No reflection or two-basis restriction is imposed; arbitrary rank-one POVMs are allowed.

## Theorem 1 — low-rank avoidance makes every allowed measurement TRACE-ONLY

If
  L ∩ {H:0<rank H<=k}=empty,                       (1)
then for EVERY compressed rank-one measurement vector v=(v_1,...,v_k[,v_anchor]), the source-dependent pullback is a scalar multiple of the identity:
  J* (vv^T)=c(v) I_m,  c(v)>=0.                 (2)
Consequently no such rank-one measurement collection can faithfully realize the given original PSD fibre when ell>=2 and J is source-injective (which follows from the standing assumption that some alpha_j is nonzero), even if infinitely many measured rank-one projectors are permitted.

**Proof.** For v partitioned into m-vectors, the source pullback is
  J*(vv^T)=sum_j alpha_j U_j^T v_jv_j^T U_j
                    +(sum_j beta_j||v_j||²)I_m.
The non-scalar part H_v=sum_j alpha_j u_ju_j^T has real rank at most k. Constancy over J_a(I+epsilon K), K∈ker A, both signs epsilon small, forces J*(vv^T)∈L. Because I_m∈L, this implies H_v∈L; hypothesis (1) forces H_v=0. Hence (2) holds.

Since ell>=2 and I∈L, choose nonzero traceless H∈L. For sufficiently small epsilon, X_epsilon=I_m+epsilon H is positive definite and has the SAME trace as I_m, but A(X_epsilon) !=A(I_m): indeed H∈range A*, and <H,H>>0 implies some measured linear functional changes. By (2), EVERY allowed rank-one measurement has the same value on J_a(X_epsilon) and J_a(I_m). Since at least one alpha_j is nonzero, J is injective: if J(H)=0, taking trace of every output block forces trH=0 (every beta_j m+alpha_j>0), then the nonzero-alpha block forces H=0. Hence J_a(X_epsilon) differs from J_a(I) and does not equal J_a(X) for any feasible X. It is an extraneous positive semidefinite exact solution, contradicting full-fibre correspondence. QED.

No choice of how the source block projections are mixed, signed, replicated, rotated or anchored can repair this within the stated block-diagonal trace-affine architecture: the pullback rank cap k is invariant.

## Theorem 2 — generic lower bound k=Omega(m)

Let s=floor(m²/4). There is a nonempty real Zariski-open dense set of measurement spaces L of codimension s containing I, including rational examples, such that EVERY exact data-faithful representation by trace-complement block lifts above must use
  k >= (1−1/sqrt(2)−o(1))m.                  (3)

**Proof.** The projective complex variety of nonzero symmetric m-by-m matrices of rank at most r has dimension
  v_r=mr−r(r−1)/2−1.
For any integer r<m satisfying s>v_r, an incidence dimension count in the Grassmannian of subspaces containing I shows a generic L avoids ALL nonzero matrices rank<=r. (The point [I] lies outside the variety for r<m; a subspace through [I] containing a fixed second projective point imposes codimension s.) Choose r=floor(c m) for any c<1−1/sqrt2. Then
  v_r/m² = c−c²/2+o(1)<1/4=s/m²+o(1).
Thus generic L meets (1) for all k<=r, which Theorem 1 excludes. Since c can approach 1−1/sqrt2, (3) follows. Zariski-open real rational input spaces exist by density of rational points in Grassmannian charts. QED.

## Theorem 3 — generic N=Omega(m⁴) in full-face two-basis normal forms of this class

Assume further that the exact source fibre is represented inside a fixed compressed PSD face of order d=km+a with a=0 or1 anchor, through the above J or J_a, and that a two-orthonormal-basis PSD problem of ambient order N has EXACTLY that embedded full fibre. Then for generic L from Theorem 2,
  d=Omega(m²),  N=Omega(m⁴).                       (4)

**Proof.** Theorem 2 gives k=Omega(m), hence d=Omega(m²). At the strictly feasible source X=I_m, every nonzero trace-complement block in J(I) is positive definite:
  beta_j m+alpha_j>0
because m>=3, beta_j>=max(0,−alpha_j), and (alpha_j,beta_j)!=(0,0). A fixed positive anchor is also positive. Thus J_a(I)>0 on the entire compressed face. The source feasible affine tangent space has dimension dim ker A=s. If a compressed measured linear kernel contained ANY direction beyond J(ker A), then small positive/negative perturbations of J_a(I) in that extra direction would remain PSD, be measured identically, and lie outside the encoded source fibre. Therefore the compressed measurement rank is at least
  D_d−s=d(d+1)/2−s.
Two complete orthonormal basis diagonals on order N impose at most 2N−1 independent linear constraints, so
  N>=(D_d−s+1)/2=Omega(m⁴).
This proves (4). QED.

## Explicit toy obstruction without genericity

Take L=span{I_m,H} for any non-scalar H and m>k+1, provided no nonzero combination of I,H has rank <=k. For example choose H diagonal with all m distinct entries and k<=m−2: every nonzero aI+bH has at most one zero eigenvalue, so rank>=m−1>k. Theorem 1 applies. This is a diagonal measurement system and can be represented quadratically using the special commuting construction of earlier Track 02 work, showing that the block-family no-go is architectural, not intrinsic to the source SDP.

## Scope and hostile audit

- The pullback rank bound uses k FULL m-by-m trace-affine congruence blocks, not k arbitrary auxiliary matrix coordinates. A general positive matrix-valued companion T:S^m_+->S^k_+ need not have this bounded-rank pullback.
- The strong no-go for k<generic threshold applies to arbitrary rank-one POVMs and any external ONB dilation; it is not specific to reflections, symmetry or Naimark completions.
- The proof relies on the FULL source affine fibre around I_m: exact constancy on every I+epsilon K, K∈ker A, forces each rank-one pullback to belong to L.
- The source counterexample X_epsilon is positive definite and has unchanged trace, but is NOT feasible, because H∈L∩I^perp is nonzero. Source injectivity (some alpha_j≠0) is ESSENTIAL; if all alpha_j=0, J collapses each fixed-trace source set to a singleton and the former theorem statement would be false.
- Exact full-fibre identity rather than mere surjective quotient is essential. Many-to-one PSD shadows remain outside the theorem.
- The two-basis dimension lower bound uses full-rank positivity of J(I), so it is unaffected by zero-rank source targets or facial reduction subtleties.
- The genericity theorem only supplies an asymptotic threshold; it does not claim every codimension-s operator space avoids low rank.
- The construction may include a fixed anchor; its source-independent contribution cancels when comparing two original matrices.
- No statement about complexity-class completeness, exact SDP feasibility algorithms, or unrestricted quadratic-size universal quotient representations is made.

## Correction of an omitted hypothesis (adversarial audit)

The original version did not explicitly require source injectivity and would have been false for the trace-only map with all alpha_j=0. The corrected standing assumption is that at least one alpha_j is nonzero. It makes J a globally injective positive linear encoding and is required for the extraneous-feasible-point contradiction. The lower bounds are unchanged for the intended positive-left-inverse universality model. This correction is preserved in Git history.
