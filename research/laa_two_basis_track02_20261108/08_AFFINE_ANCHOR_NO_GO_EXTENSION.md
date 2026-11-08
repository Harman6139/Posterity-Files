# Milestone 08 — the superquadratic lower bound also covers globally positive AFFINE encoders with PSD anchors

Date: 2026-11-08. This closes the fixed-anchor loophole in Milestone 07.

## Theorem

Let m>=2, L<=S^m contain I_m and let b=A(I_m) with range(A*)=L. Consider any globally cone-positive AFFINE encoding
  E(X)=J(X)+A_0,   E(S^m_+) subset S^N_+,
and a globally positive LINEAR decoder D:S^N -> S^m satisfying
  D(E(X))=X for all X>=0.
Assume the exact entire two-basis fibre at E(I) is
  {Y>=0:A_U(Y)=A_U(E(I))}=E({X>=0:A(X)=b}).

Then the same generic lower bounds as Milestone 07 hold:
  rank E(I) >= Omega(m^(4/3)),
  N >= Omega(m^(8/3))
for a dense open full-measure collection of rational trace-controlled input measurement spaces L of codimension floor(m(m+1)/4). Hence the strong universally quadratic N=O(m^2+p) theorem is FALSE even when a fixed positive anchor is allowed.

### Proof

1. Evaluate at zero: A_0=E(0)>=0, and D(A_0)=0. For every X>=0 and t>0,
   E(tX)/t=J(X)+A_0/t>=0;
   sending t to infinity gives J(X)>=0. Since D(E(X))=X and D(A_0)=0, one has D J=id on all symmetric matrices. Thus the linear part J,D form an exact positive retract.

2. The positive-retract classification of Milestone 06 supplies, after an invertible congruence and support compression, a canonical decoder-positive subspace carrying X tensor I_t. Its defining support E is the support of D*(I) after normalization. Because A_0>=0 and D(A_0)=0,
   tr(D*(I) A_0)=0.
   A positive-semidefinite product with zero trace has orthogonal supports, so A_0 has zero block and cross block against E. Therefore the affine anchor lies wholly in the decoder-invisible auxiliary part.

3. The positive block-lift cross map has the form (X tensor I_t)B, eliminated by a fixed block-triangular congruence. Because A_0 has zero rows/columns on the tensor subsystem, this congruence leaves its location in the auxiliary block unchanged. Thus the affine encoding has the exact normal form
   E(X)=(X tensor I_t) direct-sum [T(X)+A]
with T a positive linear map and A>=0 independent of X. Restrict the output to the support of E(I), so E(I) is positive definite and the canonical decoder remains partial trace on the first summand.

4. Let W be the span of the compressed two-basis rank-one projectors after this congruence. The strict-feasible tangent calculation does not see the constant anchor:
   W^perp=J(ker A_source).
Applying the canonical decoder pi gives
   pi(W^perp)=ker A_source.
Therefore L={H:pi*(H) in W} with the same FIXED pi*(H)=(H tensor I_t)/t direct-sum 0.

5. The rank-one-generated parameter count in Milestone 07 is unchanged: the family of W at compressed order d has semialgebraic dimension at most D_d(d-1)<d^3/2, while the Grassmannian of measurement spaces containing I has dimension (ell-1)s=Theta(m^4) when ell,s=Theta(m^2). Thus generic d=Omega(m^(4/3)). The exact tangent dimension and two-basis rank bound give N=Omega(m^(8/3)). QED.

## Interpretation

The earlier reflection constructions use affine encoders X -> F^T(J(X) direct-sum [1])F. This theorem applies to ALL such globally positive affine encodings with positive linear decoders, not only to canonical reflections. It rules out using a fixed positive anchor as a way to bypass the generic superquadratic barrier.

The theorem is still conditional on exact full-fibre equality and global cone-positive affine encoding/positive linear decoding. It is NOT an obstruction to projections of larger two-basis fibres, nonlinear b-dependent encodings, or decoders that preserve positivity only on the given feasible fibre rather than on the whole PSD cone.
