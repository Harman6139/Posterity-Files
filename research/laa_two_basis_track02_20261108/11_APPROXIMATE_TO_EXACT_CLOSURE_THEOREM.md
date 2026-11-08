# Milestone 11 — all-tolerance approximate two-basis reductions force exact fibre surjectivity

Date 2026-11-08. This closes a subtle loophole in interpreting the surjective-projective lower bound: a FIXED two-basis design and FIXED decoder offering two-way approximation guarantees at every tolerance is automatically an exact surjective representation in the zero-noise limit. No explicit exact encoder is needed.

## Theorem (quantitative approximation closure)

Let B:S^N -> R^(2N) be the two-orthonormal-basis map B(Y)=(diag Y,diag(U^T Y U)), and let y in R^(2N). Let A:S^m -> R^p and b in R^p have a nonempty PSD feasible fibre F_b={X>=0:A(X)=b}. Let D:S^N -> S^m be a fixed positive linear decoder (in particular a CP decoder).

Assume there are functions eps -> rho(eps),eta(eps) with rho(eps),eta(eps) ->0 as eps downarrow0, such that for every sufficiently small eps>0:

(A) (soundness) if Y>=0 and ||B(Y)-y||<=eps then dist(D(Y),F_b)<=rho(eps);

(B) (completeness) for every X in F_b there is Y_eps(X)>=0 satisfying
  ||B(Y_eps(X))-y||<=eps,
  ||D(Y_eps(X))-X||<=eta(eps).

Then the exact two-basis fibre T={Y>=0:B(Y)=y} is nonempty and
  D(T)=F_b.

**Proof.** Take any X in F_b. By (B), Y_eps(X) has bounded trace because its first-basis diagonal has Euclidean error <=eps from the first N entries of y:
  tr Y_eps(X) <= sum_{j=1}^N y_j + sqrt(N) eps.
For PSD matrices, ||Y||_F<=trY. Therefore Y_eps is uniformly bounded; choose eps_n downarrow0 and a convergent subsequence Y_eps_n ->Y. By closedness, Y>=0. Continuity of B,D and the two vanishing errors give B(Y)=y and D(Y)=X. This proves F_b subset D(T), and T is nonempty.

For any Y in T and any eps>0 small, ||B(Y)-y||=0<=eps, so (A) gives dist(D(Y),F_b)<=rho(eps). Since F_b is closed and rho(eps)->0, D(Y) belongs to F_b. Hence D(T) subset F_b. QED.

## Corollary (tradeoff for fixed-design weak reductions)

Take the generic rational source family from Milestone 09, with source fibre containing I_m. Suppose a two-basis design of order N<=C m^2 and fixed CP decoder of Kraus rank t<=C m satisfies the above two-sided all-tolerance approximation guarantees, with ANY rates rho(eps),eta(eps)->0 (no polynomial or exponent assumption). Then its exact fibre T must have minimal PSD face order d>=c_C m^2 and auxiliary exact-fibre dimension a>=c'_C m^4. If a<=A m^2, then necessarily N=Omega(m^(8/3)).

This follows immediately from exact surjectivity and Milestone 09. No positive linear encoder is assumed, and the sharpness tradeoff does not depend on the particular modulus of decay of rho or eta.

## Important limitations

1. The design U, target y, and decoder D must remain FIXED as eps->0. A tolerance-dependent family U_eps,D_eps can evade this compactness argument, although then coefficient size and conditioning require independent analysis.
2. Completeness must cover every X in F_b. A reduction solving only a scalar optimum value, or one producing a single feasible source point, need not have a surjective exact fibre and is not covered.
3. The CP Kraus-rank/slack lower bounds come from Milestone 09 and retain their stated architectural hypotheses.
4. The theorem does not claim an unrestricted quadratic-size weak SDP feasibility reduction is impossible. It identifies exactly what an all-tolerance *recovery* reduction with fixed data would entail.
5. The proof uses trace control of the TWO-BASIS residual to obtain compactness of approximate lifts. Replacing it with an arbitrary unbounded PSD measurement map may invalidate the conclusion.
