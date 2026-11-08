# Milestone 13 — unconditional quadratic-order lower bound for exact AFFINE-ISOMORPHIC two-basis SDP fibres

Date 2026-11-08. Unlike the positive-retract lower bounds, this theorem does not require a positive encoder or decoder or a fixed congruence normal form. It assumes only an exact affine bijection between the entire source and target feasible sets. It gives Omega(m^2), not a superquadratic lower bound.

## Theorem

Fix m>=4, D=m(m+1)/2, and integers 2<=s<=D-2. Let L <= S^m be a generic codimension-(D-s) measurement space containing I and put b=A(I), with ker A of dimension s (equivalently, choose a generic s-dimensional subspace V<=S_0^m of traceless symmetric matrices and set the source fibre F={I+H:H in V,I+H>=0}). Suppose a two-orthonormal-basis PSD fibre
  T={Y>=0:A_U(Y)=y}, Y in S^N
is affinely isomorphic to F as a convex set (no positive or globally linear cone encoder/decoder assumption). Let d be the order of the minimal PSD face containing T. Then
  d>=m,
  N >= [m(m+1)/2-s+1]/2.
For s=floor(D/2), this is N=Omega(m^2).

The theorem applies equally when the affine isomorphism is implemented by an arbitrary nonlinear algorithm whose restriction to F happens to be affine. It is not a statement about general semidefinite SHADOW/projection representations or nonlinear homeomorphisms.

## Proof

1. Determinant boundary of the source. Identify F with the spectrahedron
  S={x in R^s: M(x)=I+sum_{j=1}^s x_j H_j>=0},
where H_j are a basis of a generic s-plane V<=S_0^m. Its polynomial boundary candidate is
  p(x)=det M(x)
of degree exactly m. The leading homogeneous term det(sum x_j H_j) is not identically zero for generic V: the traceless invertible matrices form an open dense subset of S_0^m for m>=2. Hence deg p=m.

2. Generic irreducibility. Over C the projective determinantal hypersurface
  Z={X in P(S^m_C):det X=0}
is irreducible because rank-(m-1) matrices form a dense irreducible orbit-family (equivalently det of a generic symmetric matrix is irreducible). Consider projective linear s-planes in P(S^m_C) through the point [I], which lies OUTSIDE Z. Bertini's irreducibility theorem for successive general hyperplane sections through a basepoint outside Z implies that, for generic such s-planes with s>=2, the intersection with Z is irreducible of dimension s-1. Restricting to s-planes whose affine tangent directions are traceless amounts to taking general projective planes in the projective hyperplane corresponding to the affine trace normalization; the determinant hypersurface restricted to that ambient hyperplane remains irreducible, because its projective variety is the graph of the linear trace coordinate over Z. The linear system of hyperplanes through [I] has no basepoints on Z, so Bertini applies. Therefore p(x) is irreducible over C for generic V.

3. A real smooth boundary patch. Since V consists of traceless matrices and s>=2, a generic H in V has a simple negative smallest eigenvalue. On the line I+tH the first boundary point for t>0 is at t_0=-1/lambda_min(H), and M(t_0) is PSD of rank m-1. The gradient of p in the H-direction is nonzero there (the zero eigenvalue crosses linearly while the others remain positive). Therefore F has a nonempty relatively open patch of real smooth points of the irreducible hypersurface {p=0}. Such a patch is Zariski dense in the complex irreducible hypersurface: any complex polynomial vanishing on it vanishes identically on the hypersurface by the identity principle on a smooth real-analytic local parametrization.

4. Affine isomorphism preserves the algebraic boundary degree lower bound. Compress the target fibre to its unique minimal PSD support E of dimension d. It has a relative-interior matrix positive definite on E. The affine isomorphism identifies the s-dimensional source affine hull with the s-dimensional target affine hull. Thus in the source coordinates the target is described by a symmetric affine pencil
  B(x)=B_0+sum_j x_j B_j in S^d,
with B(x)>=0 iff M(x)>=0. At the interior x=0, B(0)>0, so the polynomial q(x)=det B(x) is nonzero and has degree <=d. Every source boundary point maps to a target boundary point, at which B(x) is singular, hence q vanishes on the real smooth boundary patch of p. By step 3, p divides q in C[x_1,...,x_s]. Thus deg q>=deg p=m, proving d>=m.

5. Dimension/rank count. At the target's relative interior point B(0)>0, its affine tangent space is the kernel of the compressed two-basis measurement map M_E:S^d->R^(2N). Because the fibre is exactly s-dimensional, this kernel has dimension s. Thus rank(M_E)=d(d+1)/2-s. The two diagonal lists have equal sum, so rank(M_E)<=2N-1. Hence
  2N-1>=d(d+1)/2-s>=m(m+1)/2-s,
which rearranges to the stated lower bound.

6. Rational source examples. Reducibility, repeated-eigenvalue degeneracy, and the exceptional parameter loci lie in proper algebraic/semialgebraic subsets of the Grassmannian of traceless s-planes. Their complement contains a nonempty real Euclidean open set and hence rational s-planes. Thus generic rational trace-normalized examples exist.

## Scope and adversarial audit

- The result covers ANY exact affine isomorphism, not only positive-linear retractions.
- It is not an obstruction to merely surjective spectrahedral shadows or nonlinear equivalences, where algebraic boundary degrees can increase under elimination.
- The determinant irreducibility uses the standard Bertini irreducibility theorem with a basepoint outside the hypersurface, and explicitly checks the needed basepoint and dimension hypotheses.
- An LMI representation of order d can have determinant with extra factors; the irreducible degree-m source factor still forces d>=m.
- The relative-interior target need not be full rank N, but is positive definite on the minimal support E by definition.
- For s=1, the determinant of an affine line pencil splits into linear factors over C; hence the theorem intentionally assumes s>=2.
- The quadratic bound N=Omega(m^2) is weaker than the Omega(m^(8/3)) bound under globally positive exact retracts, but it applies to a much wider class of affine correspondences.
- The generic source constraints are trace-controlled because I belongs to their measurement space.
