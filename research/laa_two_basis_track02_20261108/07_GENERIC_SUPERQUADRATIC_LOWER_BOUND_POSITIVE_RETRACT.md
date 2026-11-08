# Milestone 07 — generic superquadratic lower bound for EVERY globally positive exact face-retract two-basis representation

Date 2026-11-08. THIS IS A RIGOROUS NEGATIVE ANSWER TO UNRESTRICTED N=O(m^2+p) UNIVERSALITY **WITHIN THE NATURAL GLOBAL POSITIVE-LINEAR RETRACT / EXACT-FULL-FIBRE MODEL**. It is substantially broader than the tensor, diagonal-companion and faithful-decoder no-go results. It does NOT rule out b-specific nonlinear encoders, non-positive decoders, auxiliary-variable extensions that are merely surjective rather than one-to-one, or encodings not realized as one fixed PSD face.

## 1. Precise representation model

Let m>=2, D_m=m(m+1)/2, s=floor(D_m/2), ell=D_m-s. Let L range over ell-dimensional real linear subspaces of S^m containing I_m, so every L defines a rational-trace-normalized PSD measurement operator A with range(A*)=L and a strictly feasible datum b=A(I_m). The original fibre F_b has affine tangent space ker A=L^perp of dimension s.

A GLOBAL POSITIVE EXACT FACE RETRACT consists of:
 (a) an ambient two-basis measurement map A_U on S^N;
 (b) an isometric compressed PSD face F^T S^d_+ F with FF^T=I_d;
 (c) positive linear maps J:S^m -> S^d and Delta:S^d -> S^m with Delta J=id;
 (d) a target datum y such that the ENTIRE ambient exact PSD fibre is
   {Y>=0:A_U(Y)=y}={F^T J(X) F:X in F_b}.
No orthogonal-reflection, same-list, rank amplification or conditioning hypotheses are imposed. The encoding need not be tensor, diagonal companion, nor commuting, and U may be any orthogonal matrix.

Since J(I) dominates J(X) for all X>=0 bounded by cI, J(S^m) lies in the support face of J(I). Replace d by this support order so J(I)>0. The positive decoder restricts to this support, preserving the hypotheses.

## 2. Theorem — generic lower bounds d=Omega(m^(4/3)), N=Omega(m^(8/3))

There is a semialgebraic generic (dense open, full measure) set of L containing I such that EVERY global positive exact face retract of its strictly feasible fibre satisfies
  d >= c m^(4/3),    N >= c' m^(8/3)
for universal positive c,c' and all sufficiently large m. Such L can be chosen rational. Consequently no universal construction of the above kind can have ambient dimension N=O(m^2+p) for p=ell=Theta(m^2), even with arbitrarily ill-conditioned algebraic coefficients.

### Proof

Step A: normalize EVERY positive encoder/decoder pair. By Milestone 06 (proved independently there), up to an invertible positive congruence on the compressed face, every positive linear retract has the exact form
  J(X)=(X tensor I_t) direct-sum T(X)
for some t>=1 and some positive linear companion T:S^m -> S^k, with mt+k=d. The canonical positive decoder
  pi(Z)=(1/t) partial_trace_ancilla(Z_first mt-by-mt)
satisfies pi J=id. The transformation is a fixed congruence, so it takes every compressed rank-one PSD measurement projector to another rank-one PSD matrix. It has no effect on the dimension of the compressed measurement space.

Step B: derive the tangent identity at the strictly feasible source. Let W<=S^d be the span of the compressed rank-one projectors from both bases (after the normalizing congruence). Let M be their analysis map. The exact source fibre contains I+epsilon K for all K in ker A and all sufficiently small positive/negative epsilon. Hence J(ker A) subset ker M=W^perp.

Conversely, since J(I)>0 on the compressed face, any H in ker M yields J(I)+epsilon H>0 for all sufficiently small positive/negative epsilon. By exact full-fibre equality this matrix equals J(X_epsilon) for some source X_epsilon in F_b. Applying pi gives X_epsilon=I+epsilon pi(H), so H=J(pi(H)) and pi(H) in ker A. Therefore
  W^perp=J(ker A).
In particular dim W = D_d-s. Applying the canonical decoder gives
  pi(W^perp)=ker A.

Step C: determine the source measurement space using ONLY the rank-one measurement span. By finite-dimensional duality,
  L=(pi(W^perp))^perp={H in S^m: pi*(H) in W}.
The dual pi* is the FIXED tensor injection
  pi*(H)=(H tensor I_t)/t direct-sum 0_k.
Thus, after the normal-form congruence, the entire original L is determined by the finite-dimensional rank-one-generated subspace W, together with the DISCRETE integers d,t. All continuously variable positive companions T, original decoders, face orientations and ambient orthogonal matrices have disappeared from this formula. This is the crucial reduction behind the lower bound.

Step D: dimension count. For a given d and rank q<=D_d, every q-dimensional subspace W spanned by rank-one PSD projectors admits a basis of q projectors v_jv_j^T, j=1,...,q. It is consequently parameterized by q nonzero vectors in R^d, modulo independent rescaling, and its semialgebraic family has dimension at most q(d-1)<=D_d(d-1)<d^3/2 for d>=2. For fixed d,t,q, the map
  W -> {H in S^m:pi*(H) in W}
is semialgebraic on the locus where the image has fixed dimension ell (it is computed by solving a linear system). Therefore the family of L representable at compressed order d and any t, any q, has dimension at most D_d(d-1). A finite union over d<=d0 and t<=d/m does not increase this dimension bound beyond max_{d<=d0} D_d(d-1).

In contrast the Grassmannian of ell-dimensional subspaces L containing I_m has dimension
  g=(ell-1)(D_m-ell)=(ell-1)s.
For s=floor(D_m/2), g=Theta(m^4); more precisely g=m^4/16+O(m^3).

Fix any d0 with D_{d0}(d0-1)<g. The representable L with d<=d0 lie in a semialgebraic subset of dimension <g, hence have dense-open full-measure complement in the Grassmannian. The threshold is
  d0=Theta(g^(1/3))=Theta(m^(4/3)).
It follows that for generic L, d=Omega(m^(4/3)).

Step E: convert compressed order into ambient two-basis order. The span W of compressed first- and second-basis rank-one projectors has rank at most 2N-1 (the sum of the first list equals the sum of the second list). On the other hand dim W=D_d-s, so
  2N-1 >= d(d+1)/2 - s,
  N >= [d(d+1)/2-s+1]/2.
Since d=Omega(m^(4/3)) while s=O(m^2), the lower bound yields
  N=Omega(m^(8/3)).
This proves the theorem.

Step F: rational examples. The exceptional representable family is contained in a proper semialgebraic subset of the real Grassmannian, whose closure still has dimension <g. The complement contains a nonempty Euclidean open set. Rational subspaces containing the rational vector I_m are dense in that Grassmannian (use local rational graph charts), hence it contains rational L. Choosing a rational basis of L produces a rational trace-controlled input operator A. The theorem is therefore a genuine obstruction for rational SDPs, not merely a transcendental genericity statement.

## 3. Scope and interpretation

The theorem solves a *precisely stated* version of the near-quadratic universality challenge **negatively**: for globally positive linear encoders, globally positive linear decoders and an exact bijective full-fibre face representation, a quadratic ambient dimension bound is false on a generic open set of rational trace-controlled SDPs. The lower exponent 8/3 is not claimed optimal; the previous general O(m^4) upper bound remains valid, and the optimal asymptotic growth between these bounds is unresolved.

It is essential NOT to claim a no-go for all conceivable computational reductions. A two-basis PSD fibre with a positive decoder merely SURJECTING onto the original feasible set may have additional auxiliary feasible points and need not be a positive linear retract; a nonlinear b-dependent encoding might also escape. Such weaker models are outside the theorem and may still admit near-quadratic reductions.

## 4. Hostile proof audit

- This is a Grassmannian dimension statement with g=Theta(m^4), not a count of numerical degrees of freedom of the input bit string.
- The initial source datum b=A(I) is strictly feasible, so PSD positivity gives a full affine tangent neighbourhood and makes the kernel equality exact.
- The full ambient fibre correspondence, not only an injection of encoded feasible matrices, is indispensable for W^perp=J(ker A).
- The positive decoder is globally positive, permitting Milestone 06's tensor-plus-positive-companion normal form. Without this hypothesis the canonical decoder pi* is unavailable and a generic arbitrary decoder contributes O(m^4) parameters.
- The normalizing congruence transforms rank-one PSD projectors to rank-one PSD matrices; no orthonormality is assumed after congruence.
- The rank-one span W may be smaller than D_d and the family dimension estimate maximizes over all q.
- The parameterization uses q projective vectors; even the weaker q*d bound suffices for the m^(4/3) threshold.
- There is no hidden dependence on the positive companion T: the exact kernel identity and canonical decoder eliminate it from the source measurement space formula.
- The ambient measurement rank is <=2N-1 regardless of whether the two lists coincide on targets.
- A lower bound under this strong notion does not contradict the known exact O(m^2) constructions for codimension one, two, commuting annihilators or select open low-codimension families, because those L occupy lower-dimensional subsets of the full Grassmannian.
- Novelty and priority have not been externally certified. The proof uses elementary semialgebraic dimension and the fully proved positive retract classification in Milestone 06, rather than an imported conjecture.
