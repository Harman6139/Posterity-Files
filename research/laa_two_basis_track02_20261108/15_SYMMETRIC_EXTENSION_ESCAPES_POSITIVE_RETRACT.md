# Milestone 15 — a quadratic-size PSD shadow with NO positive linear section

2026-11-08. This is a rigorous new architectural escape from the exact-positive-retract lower bounds. It is NOT yet a two-orthonormal-basis normal form: the arbitrary source measurement constraints still need to be realized by two basis diagonals.

## Theorem 1: symmetric-square surjective quantum marginal

Let m>=2, V=Sym^2(R^m) regarded as the symmetric subspace of R^m tensor R^m, with real dimension d=m(m+1)/2. Let P be the orthogonal projector onto V. For Y in S(V), view PYP as a real symmetric operator on R^m tensor R^m and let
  D(Y)=Tr_2(PYP)
denote its partial trace over the second tensor factor.

Then:
(a) D is linear, completely positive, trace preserving, and PSD-positive;
(b) D({Y>=0 on V:trY=tau})={X>=0 on R^m:trX=tau} for every tau>=0;
(c) for ANY real linear map A:S^m ->R^p and any b with a nonempty PSD source fibre F_b,
    T_b={Y>=0 in S(V):A(D(Y))=b}
    obeys D(T_b)=F_b, including nonsingleton fibres and all ranks;
(d) every source objective is represented exactly on EVERY ambient symmetric Y by
    <C,D(Y)>=<P(C tensor I_m)P,Y>,
    and for all Y,Z, ||D(Y)-D(Z)||_F<=sqrt(m)||Y-Z||_F;
(e) there is NO linear positive right inverse J:S^m -> S(V) to D when m>=2.

This shows that a quadratic-order semidefinite extension can have exact surjective PSD recovery and objective preservation without lying in the globally positive linear retraction class. The obstruction to two bases is now genuinely a measurement-geometry problem, not lack of a positive SDP lift.

## Proof

(a) Let V:R^d ->R^{m^2} be the isometric inclusion of the symmetric subspace. Then
 D(Y)=sum_{j=1}^m B_j Y B_j^T,
 with B_j=(I_m tensor e_j^T) V,
 a real Kraus decomposition. Since sum_j B_j^T B_j=V^T V=I_d, D is trace preserving. CP and PSD positivity follow.

(b) For any unit u in R^m, the symmetric product z=u tensor u belongs to V and
 D(zz^T)=uu^T.
For X>=0 of trace tau, choose a spectral decomposition X=sum_i lambda_i u_i u_i^T, lambda_i>=0, and define Y=sum_i lambda_i (u_i tensor u_i)(u_i tensor u_i)^T. Then Y>=0 on V, trY=tau, D(Y)=X. The reverse inclusion follows from positivity and trace preservation. For tau=0 both sides are {0}.

(c) The forward containment D(T_b) subset F_b is immediate. For every X in F_b, construction (b) supplies Y>=0 with D(Y)=X, hence A(D(Y))=b, giving reverse containment.

(d) The adjoint of partial trace is D*(C)=V^T(C tensor I_m)V. This yields the cost identity. The Frobenius operator norm bound follows from ||Tr_2 W||_F<=sqrt(m)||W||_F for arbitrary W and isometric inclusion.

(e) Suppose a positive linear J with D J=id existed. For any unit u, J(uu^T)>=0 and has trace one because D is trace preserving and D(J(uu^T))=uu^T. A PSD bipartite matrix whose first partial trace is rank one has its range contained in span(u) tensor R^m: for w perpendicular to u, its nonnegative expectation against |w><w| tensor I is zero, hence the corresponding PSD block vanishes and so do its cross blocks. Since J(uu^T) is supported inside Sym^2(R^m), its range lies in
  (span(u) tensor R^m) intersect Sym^2(R^m)=span(u tensor u).
Therefore
  J(uu^T)=(u tensor u)(u tensor u)^T
for EVERY unit u.

This is impossible for a linear map J. With orthonormal u=e1,v=e2 and z_+=(u+v)/sqrt(2), z_-=(u-v)/sqrt(2), one has
  z_+ z_+^T+z_- z_-^T=uu^T+vv^T
on the SOURCE. But their forced symmetric-product lifts have nonzero sum of matrix coefficients on (u tensor v+v tensor u)/sqrt(2), whereas the sum of lifts of uu^T and vv^T vanishes there. Explicitly
  <s, J(z_+z_+^T+z_-z_-^T) s>=1/2,
  <s, J(uu^T+vv^T) s>=0,
where s=(u tensor v+v tensor u)/sqrt2. Contradiction. QED.

## Exact gap to two orthonormal bases

Let A_U:S^N ->R^{2N} be the pair of basis diagonals and let D_new be a CP decoder from S^N into S^m. For a full-rank (on its minimal support) two-basis fibre T with D_new(T)=F_b, tangent-space duality requires
  D_new*(range A*) subset span{first basis projectors,second basis projectors}
after support compression. This is necessary; a separate positive lifting argument is required to show surjectivity.

For the symmetric extension the source adjoint operators are
  D*(H)=P(H tensor I_m)P on V,
i.e. the one-body observables acting on the symmetric square. A quadratic-size TWO-BASIS theorem via this architecture would need to represent the necessary L of these operators in the sum of two orthogonal MASAs, or construct a more flexible first/second-basis PSD fibre with a compatible decoder. This is an explicit finite-dimensional simultaneous-diagonal-correction problem, not solved in this milestone.

## Comparison with the earlier hybrid marginal result

Milestone 14 used order 2m^2 and a first real maximally entangled basis plus arbitrary extra subsystem measurements; it even possessed a globally positive linear right inverse X ->X tensor I/(2m). The symmetric-square extension here has smaller order m(m+1)/2 and NO positive linear section. Therefore it genuinely escapes Milestones 05--08 rather than trivially reparameterizing them.

## Hostile audit

- Pure-state lifting Y=(u tensor u)(u tensor u)^T is NONLINEAR in X=uu^T. This is the mechanism behind the no-section theorem.
- The lifted fibre is a PSD spectrahedron, with exact surjective decoder, but constraints are arbitrary one-body observables, not two-basis diagonal constraints. No false universal two-MASA claim is made.
- Real symmetry is used throughout; partial trace and the symmetric tensor subspace are real.
- The no-section argument uses positivity for ALL rank-one PSD source inputs. A b-specific affine section only on a restricted feasible set is not excluded.
- This is not a proof that all positive quotient maps lack positive sections: some do, some do not. The symmetric-square quotient gives a concrete universally surjective example with no section.
