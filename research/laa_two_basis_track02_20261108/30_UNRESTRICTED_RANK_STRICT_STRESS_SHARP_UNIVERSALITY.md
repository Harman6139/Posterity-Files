# Milestone 30 — SHARP target-adapted two-basis universality for EVERY strictly stressed uniquely recoverable PSD problem, of ANY rank

Date 2026-11-08. This is a complete, self-audited theorem in the real PSD setting. It resolves the sharp transfer problem for the entire strict-stress/singularity-degree-at-most-one class **without requiring an admissible ONB in the original rank-one measurement space**. It strengthens Milestones 27-29 (no rank-one assumption, no "safe support projector" test, no tangent-kernel dimension threshold). It also gives a sharp O_s(m²) representation for all FIXED-CODIMENSION strictly stressed general linear PSD problems. It does NOT solve the high-facial-depth or unrestricted O(m²+p) computational universality problem.

## 1. Sharp theorem for arbitrary rank-one Parseval measurements

Let G in R^{d x M} be Parseval (GG^T=I_d), let W=span{g_jg_j^T}, q=dim W, and let M_G(Z)=(g_j^T Zg_j)_j. Let Z_*>=0 be uniquely recovered from these data among ALL PSD competitors. Let P project onto ranZ_*, let Q=I-P, and suppose a strict measured PSD stress exists:
  S in W, S>=gamma Q, SP=0, gamma>0.
The full-rank case Q=0 is included (choose S=0). Assume Z_*!=0.

**Theorem A.** Given the support projector and this stress, one can construct a new rank-one Parseval frame G' containing the projectors of a complete orthonormal basis of R^d, such that the original and augmented PSD recovery moduli are EQUIVALENT:
  omega_G'(t)~omega_G(t)
as t downarrow0, even when the original space W has NO admissible ONB.

In fact G' can be chosen with at most 2q+d columns and is obtained by adding one adaptively chosen orthonormal basis at positive weight to a conically sparsified original frame. The source moduli both have EXACT optimal exponent either 1 or 1/2, and that exponent is preserved by the augmentation.

Consequently the ONE-STAGE signed-anchor two-basis lift (with optional nonreflection rotation) has dimension
  N <= (2q+d)+3d+4 = 2q+4d+4 <=6q+4,
and satisfies, for the COMPLETE ambient PSD cone and every rank of competing Y,
  {Y>=0:A_U(Y)=A_U(X_*)}={X_*},
  omega_final(t)~omega_G(t)+sqrt(t).
Every target observation is STRICTLY positive, every basis overlap is nonzero, the globally PSD-positive decoder recovers source matrices exactly on embedded points, and source linear objectives are represented EXACTLY on all symmetric ambient matrices. The target rank becomes rank(Z_*)+1, and source Frobenius distances are preserved on the embedding.

Thus every NON-LIPSCHITZ strict-stress source modulus is preserved, as a FUNCTION up to multiplicative constants, by a near-dimension-optimal O(q) two-basis construction. The only unavoidable loss is Lipschitz-to-square-root for nonzero targets.

## 2. Exact tangent-map Lipschitz/square-root dichotomy

Let E=ranZ_* have rank r. Consider the first-order tangent map
  T:S(E) direct-sum Hom(E^perp,E) -> R^M,
  T(A,C)=M_G(A+C+C^T).
The strict-stress tangent theorem of Milestone 29 proves:

- If ker T={0}, then omega_G(t)=Theta(t), i.e. sharp local exponent 1.
- If ker T is nonzero, then omega_G(t)=Theta(sqrt(t)), i.e. sharp local exponent 1/2.

The proof is direct. Strict stress gives tr(QZ)=O(delta), and block positivity gives ||PZQ||=O(sqrt(delta)). If T is injective, the original data modulo the O(delta) lower block invert T and yield a Lipschitz recovery estimate. If T has nonzero (A,C) in its kernel, then
  Z(t)=[D+tA, tC;tC^T,t² bI_Q],
with D=Z_*|E>0 and b sufficiently large, is PSD by its Schur complement; the data change only at order t² and the error is order t. The general strict-stress upper sqrt bound follows from source uniqueness and injectivity of compressed measurements on S(E).

This is a complete local classification, NOT an unproved generic dichotomy.

## 3. The new key: choose an adapted ONB hollowizing ONE unmeasured tangent

First conically sparsify the original tight frame to at most 2q rank-one Parseval columns without changing W (reserve q independent projectors at positive weight and apply conic Caratheodory to the residual identity). It retains the exact measurement kernel, source modulus up to fixed constants, and the strict stress. We may therefore assume M<=2q.

If ker T={0}, choose any real orthonormal basis u_1,...,u_d adapted to E direct-sum E^perp. Appending its rank-one projectors at positive Parseval weight cannot DESTROY a Lipschitz bound, because the original measurements remain: if G'=[sqrt(1-epsilon)G,sqrt(epsilon)U_basis], then
  ||M_G(Z-Z_*)|| <= (1-epsilon)^(-1)||M_G'(Z-Z_*)||.
A scaling perturbation Z_*+t uu^T supplies the linear lower bound. Thus omega_G'(t)=Theta(t)=omega_G(t).

If ker T is NONZERO, choose one nonzero pair (A,C) with
  M_G(A+C+C^T)=0.
Since G is Parseval, the sum of these measurements equals trace(A+C+C^T)=tr A, so
  tr A=0.                                             (3.1)
This is the crucial identity.

There ALWAYS exists a real orthonormal basis of E in which the diagonal of the traceless symmetric A is identically zero. This is the elementary real HOLLOWIZATION lemma: if A!=0 traceless, choose a unit vector u with u^T A u=0 by mixing eigenvectors for positive and negative eigenvalues; the compression to u^perp still has trace zero, so recurse. If A=0, choose any basis. This construction uses real eigenvectors and square roots, and produces an exact algebraic basis whenever A is algebraic.

Choose such a hollowizing basis u_1,...,u_r of E, and extend it arbitrarily to a full ONB of R^d using vectors in E^perp. For every support basis vector u_i,
  u_i^T(A+C+C^T)u_i=u_i^T A u_i=0.
For every kernel basis vector u_j in E^perp, the tangent matrix A+C+C^T has zero Q-Q block, hence u_j^T(A+C+C^T)u_j=0.
Thus the chosen NONZERO tangent direction is invisible both to the ORIGINAL frame and to EVERY newly appended ONB projector.

Let
  G'=[sqrt(1-epsilon) G, sqrt(epsilon) U_basis], 0<epsilon<1.
It is Parseval, has the same unique PSD target (old data retained), and retains the strict stress. Its tangent map therefore still has a NONZERO kernel. Milestone 29's sharp dichotomy yields
  omega_G'(t)=Theta(sqrt(t))=omega_G(t)
for all sufficiently small t. In particular, no O(delta) residual equivalence of each appended basis coordinate is required; preserving ONE bad tangent direction suffices to preserve the WORST-CASE modulus.

This proves the adaptive ONB theorem for ALL target ranks.

## 4. One signed reflection stage, not the unstable double-zero stage

The augmented frame G' is Parseval and has a complete ONB in its projector span. Use the explicit signed-anchored frame construction of Milestone 27:
 - at each adapted ONB vector, three weighted columns with weights -1,2,3, chosen to satisfy both tightness and zero signed compression;
 - columns h g'_j of weight 4, h=1/10;
 - nonzero small anchor coefficients and three pure-anchor columns of weights -1,2,4;
 - one duplicated weight-4 frame column, retained after a small equal-weight rotation to make the final bases genuinely different and nonreflection.

This gives order N<=M+4d+4<=2q+4d+4 and an isometric embedding
  E(Z)=F^T(Z direct-sum[1])F
with FF^T=I_(d+1), FDF^T=0 and exposing certificate
  S0=D+UDU^T>=2(I-F^TF).
Its compressed measurement span is the anchored extension of W'. Consequently every PSD exact ambient solution is E(Z) for an exact source solution Z, so uniqueness is global and rank unrestricted. All target observations are strictly positive by their anchor component; every transition entry is nonzero by finite algebraic avoidance. Linear source costs are represented by F^T(C direct-sum[0])F and equal <C,D_final(Y)> for every ambient symmetric Y, with D_final(Y)=(FYF^T)_(1:d,1:d)>=0 for PSD Y.

The even part of the two measured lists eliminates support-to-exterior cross terms exactly, giving omega_final(t)<=C omega_G'(Ct)+C sqrt(t) for arbitrary ambient PSD Y. Embedded competitors give omega_final(t)>=omega_G'(ct). Because rank E(Z_*)=rank Z_*+1>=2 and the exterior dimension is large, there is a nonzero invisible support-to-exterior cross block; its same-rank Gram-repaired PSD curve gives the matching omega_final(t)>=c sqrt(t). Thus
  omega_final(t)~omega_G'(t)+sqrt(t)~omega_G(t)+sqrt(t).
The sharp exponent and modulus statements follow.

## 5. Corollary — sharp quadratic universality for ALL fixed-codimension STRICT-STRESS linear PSD problems

Let A:S^m->R^p be a real trace-controlled linear measurement map with independent measurement-space codimension s=dim S^m-dim range(A*), and let X_*>=0 be uniquely recoverable and STRICTLY STRESSED: after trace normalization there is Omega=Omega^T>=0 in range(A*) with
  Omega X_*=0,  Omega>=gamma P_(ker X_*), gamma>0.

The codimension-adaptive rank-one purification compiler proved in CODIMENSION_TWO_UNIVERSAL_THEOREM.md, Part 3 (in the earlier dense_quadratic directory), takes
  r0=max{k>=1:k(k+1)/2<=s+1},  r_aux=2r0+1=O(sqrt(s+1)),
  d=m r_aux,
  J(X)=X tensor I_(r_aux),
and constructs a rank-one Parseval frame on R^d whose projector span is
  W_L={H in S^d:partial_trace_aux(H) in range(A*)}.
Its measurement kernel is J(ker A). The positive partial-trace decoder and Frobenius isometry imply that the compiled PSD recovery modulus is equivalent to the original omega_A(t), up to fixed scaling of argument and norm. Its target J(X_*) is unique because the original fibre was unique. Importantly
  Omega tensor I_(r_aux) in W_L,
is PSD, annihilates J(X_*), and has the SAME strict gap gamma on the kernel of J(X_*). Thus the rank-one compiled problem falls under Theorem A irrespective of whether W_L has an admissible ONB.

Apply the target-adapted hollowization+one-stage signed-anchor construction. Since q=dim W_L <=d(d+1)/2 and q>=d, its final order is
  N<=2q+4d+4=O(d²)=O(m²(s+1)).
For every fixed codimension s, this is **N=O_s(m²)**. The final target has rank
  r_aux rank(X_*)+1.
Every target observation is positive, every basis overlap nonzero, exact full-cone recovery holds, and its sharp modulus satisfies
  omega_final(t)~omega_A(t)+sqrt(t).
Thus **EVERY non-Lipschitz strict-stress finite-dimensional real PSD inverse problem of fixed codimension has a sharp quadratic-size two-basis normal form**, including arbitrary dense noncommuting measurement spaces with s>=3. The preceding double-zero construction guaranteed exact fibres but could halve the source exponent; the hollowized target-adapted construction eliminates that loss.

The construction is effective in algebraic arithmetic given the target support, source strict stress and a finite rank-one compiler. The positive singular gaps and certificate gaps enter constants explicitly. This is NOT a uniform polynomial-Turing-bit algorithm that finds unknown targets/certificates or handles unbounded codimension at order O(m²+p).

## 6. Sharp scope and adversarial audit

- The key hollowization is for ONE unmeasured tangent-support matrix A, not simultaneous hollowization of the entire annihilator operator system. Therefore it is always possible, independent of rank r and dimension of ker T.
- The new ONB is NOT necessarily residual-wise rate-neutral for every PSD competitor. It preserves the WORST-CASE MODULUS because it preserves one bad tangent direction, and strict stress restricts possible optimal exponents to exactly 1/2 or 1.
- The exact source tangent kernel is checked before choosing the adapted basis. No assumption about the tangent nullity h>=r from Milestone 29 is needed.
- The source rank-one frame's Parseval property is essential: it measures trace, forcing tr A=0 and enabling hollowization.
- At a full-rank unique target Q=0, ker T=0 by uniqueness, so the Lipschitz branch applies.
- The final target has rank at least two because the source is nonzero and the anchor adds one; the matching ambient square-root obstruction is therefore genuine.
- The tensor-purification corollary is CONDITIONAL on the independently established positive rank-one compiler and the supplied strict stress; it does not assert arbitrary linear measurement spaces are themselves rank-one generated.
- The O(m²(s+1)) dimension bound is sharp in order for fixed s compared with the generic algebraic measurement-dimension lower bound, but no unconditional constant-factor optimality claim for every m,s is made.
- This does NOT solve cases of facial-reduction depth >=2, where the source modulus can have exponent below 1/2 and preserving merely one first-order tangent direction is insufficient.
- All competitor rank restrictions are absent from the upper bound, and the square-root lower curves are PSD by exact factorization.
- No claim of newness for the classical real hollowization lemma, conic Caratheodory or basic semidefinite facial reduction is made.
