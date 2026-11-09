# Milestone 55 — surjectivity onto PURE PSD RAYS forces skew-injectivity for every real CP decoder

Track 02, 2026-11-09. Complete finite-dimensional theorem and compactness corollary. This resolves one of the two escape alternatives left by the general CP-channel two-MASA commutator-distortion bound in Milestone 54: a completely positive decoder that covers all pure PSD source rays CANNOT annihilate any nonzero skew-symmetric source direction. Thus a well-conditioned true PSD-cone quotient must pay nonzero commutator distortion when its source measurement space is generically rich. The result is independent of any basis design, positive encoder, linear right inverse, fixed fibre or trace-preservation assumption.

**Quantitative strengthening (Milestone 56):** The compactness-based positive skew singular-value margin in Corollary 2 is now explicitly bounded below by sin(pi/(t+2))/(t sqrt(m)) for every CPTP cone quotient of Kraus rank t, with an inverse Kraus-stack singular-value factor for nonTP CP maps. See 56_EXPLICIT_POLYNOMIAL_SKEW_MARGIN_CP_QUOTIENTS.md.

## Theorem 1 — exact skew-injectivity of every pure-ray-surjective CP decoder

Let m>=2,N>=1 and let D:S^N→S^m be REAL completely positive:
  D(Y)=sum_(a=1)^t B_a Y B_a^T
for arbitrary real m-by-N Kraus matrices B_a. Trace preservation is NOT assumed. Suppose for EVERY nonzero u∈R^m the positive rank-one ray R_+ uu^T is hit by the cone map D, meaning there exists Y_u>=0 with
  D(Y_u)=uu^T.
Then the Kraus adjoint extension
  Phi(T)=sum_a B_a^T T B_a
has TRIVIAL KERNEL on the real skew matrix space so(m):
  Phi(T)=0 and T^T=−T  ==> T=0.                     (1)
Equivalently,
  sigma_skew(Phi)>0.
The statement holds for EVERY specified Kraus representation of D, even if different real CP extensions agree on symmetric inputs.

### Proof

Define the real linear Kraus stacking map
  V:R^N→R^m⊗R^t,
  Vx=sum_a B_a x⊗e_a.
It need not be an isometry when D is not trace preserving, but it satisfies
  D(Y)=Tr_anc(VYV^T),
  Phi(T)=V^T(T⊗I_t)V.

Fix a nonzero source u. Since D(Y_u)=uu^T and Y_u>=0, the PSD matrix W_u=VY_uV^T has first partial trace uu^T. Every vector perpendicular to u has zero first marginal expectation; positivity forces W_u to be supported on span(u)⊗R^t. Since W_u!=0, its range contains a nonzero vector u⊗w, with w!=0, which lies in ran V. Hence the 'pure product fibre'
  K_u={w∈R^t:u⊗w∈ran V}
is NONZERO for every source projective direction [u].

Suppose, for contradiction, that Phi(T)=0 for a nonzero real skew T. Every nonzero real skew matrix has a two-dimensional real orthonormal invariant rotation plane with a basis e1,e2 satisfying
  e1^T T e2=λ!=0.
Choose t+1 pairwise distinct unit vectors
  u_j=cos θ_j e1+sin θ_j e2,
with θ_j all distinct in (0,π). Then for every i!=j,
  u_i^T T u_j=λ sin(θ_j−θ_i)!=0.

For each j choose nonzero w_j∈K_(u_j). There exist input vectors x_j with
  Vx_j=u_j⊗w_j.
Because Phi(T)=V^T(T⊗I)V=0, for all i!=j,
  0=x_i^T Phi(T)x_j
   =(u_i^T T u_j)(w_i^T w_j).
The first factor is nonzero, so w_i^T w_j=0 for all i!=j. Thus w_1,...,w_(t+1) are t+1 nonzero pairwise orthogonal vectors in R^t, impossible. The contradiction proves T=0. QED.

## Corollary 2 — uniform positive skew margin at FIXED source/input orders for CPTP cone quotients

Fix integers m>=2,N>=1. Consider all real completely positive TRACE-PRESERVING maps D:S^N→S^m satisfying
  D({Y>=0:trY=1})={X>=0:trX=1}.
The family is compact: in a real Choi representation, the CP condition is a PSD cone constraint, trace preservation is affine, and the Choi trace equals N; exact surjectivity onto the compact state space is CLOSED under limits by compactness of the input density-matrix body.

By Theorem 1, for every such D and every real CP Kraus extension its adjoint has sigma_skew>0. The singular value depends continuously on the real Choi/Kraus-extension coefficients, and the compact set of CP extensions is bounded by the trace-preserving condition. Therefore a (possibly very small) dimension-dependent constant
  c_skew(m,N)>0
exists such that
  sigma_skew(D*)>=c_skew(m,N)                    (2)
for all such CPTP cone-quotient designs and their Kraus extensions.

No explicit polynomial-in-m,N lower bound for c_skew is claimed. The quantity is a compact semialgebraic optimization minimum and could be computationally expensive to certify.

## Corollary 3 — non-Jordan distortion is UNAVOIDABLE for generic rich SDP measurement spaces

Let m>=4 and let L⊂S^m be a measurement space in the generic open class of Milestone 53, so gamma_4(L)>0 already when dim L>=m+3. Let D:S^N→S^m be ANY real completely positive decoder whose cone image contains every source PSD pure ray, and let Phi=D* be its chosen real Kraus adjoint on all matrices.

If two real ONB diagonal spaces D1,D2 on R^N satisfy
  Phi(L)⊂D1+D2,
then Milestone 54's exact channel commutator-distortion lower bound becomes STRICT:
  delta_comm(Phi;L)
    >=gamma_4(L) sigma_skew(Phi)
       sqrt[(m(m−1)/2)/(N(N−1))]
    >0.                                                  (3)
Thus a true CP cone quotient cannot evade the two-MASA obstruction by suppressing all skew commutators. Its adjoint MUST distort matrix multiplication/commutation by a nonzero amount whenever it attempts to make rich noncommuting source observables readable in exactly two bases.

For a CPTP density-body quotient at fixed m,N, (2) makes this quantitative even uniformly over all such decoders:
  delta_comm(Phi;L)
    >=gamma_4(L)c_skew(m,N)
       sqrt[(m(m−1)/2)/(N(N−1))].              (4)
This is a necessary nonreversibility/conditioning cost, not an impossibility theorem for arbitrary CP quotients: strongly non-Jordan channels can satisfy (3).

## Scope and adversarial audit

1. The exact skew-injectivity proof does NOT use trace preservation, a unital adjoint, or the existence of any positive linear encoder. Cone-surjectivity onto pure rays is the sole substantial hypothesis.
2. The supports of the pure-output PSD lifts are forced into u⊗R^t by POSITIVITY. No rank-one input lift or uniqueness assumption is made.
3. The two-dimensional rotation plane exists for every nonzero real skew T; the chosen t+1 projective source vectors have pairwise nonzero skew pairings.
4. The Kraus stacking V may have nontrivial kernel. Only product vectors in ran V are needed, so injectivity of V is NOT assumed.
5. The theorem applies to each real Kraus extension individually. It does not falsely claim that the action of a real CP map on S^m uniquely determines its action on skew matrices.
6. Compactness in Corollary 2 is over trace-preserving CP extensions/Choi matrices of FIXED input/output dimensions; this hypothesis prevents rescaling the channel so its skew singular values vanish while retaining cone-surjectivity.
7. A decoder whose PSD range only covers a PROPER source feasible fibre with no full pure-ray family may annihilate skew directions, so the theorem is not a blanket statement for all SDP recovery tasks.
8. The two-MASA obstruction remains conditional on full-rank lifted feasible data for ordinary soundness; a singular minimal face can evade full-space operator inclusion even when the decoder is cone-surjective.
9. External literature priority on CP cone-quotient maps is not certified; the proof is elementary and self-contained.
