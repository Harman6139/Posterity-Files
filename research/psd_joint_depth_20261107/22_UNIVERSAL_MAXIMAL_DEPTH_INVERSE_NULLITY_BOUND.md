# Universal dense-kernel sharp instability at maximal facial depth: alpha <= 1/nullity

2026-11-07. NEW universal structural theorem for **all arbitrary dense PSD kernels**, all n and all positive target ranks. No sparse representation or combinatorial stress preservation is assumed.

## Theorem
Let L:S^n→R^m be arbitrary linear, with X*≥0 the unique PSD matrix having its measurements, rank r≥1, nullity nu=n-r≥2. If its minimal facial-reduction degree equals the largest possible value d=nu, then its sharp full-matrix Hölder exponent satisfies
\[
\boxed{\alpha(L,X_*)\le 1/\nu.}
\]
The inequality is sharp for EVERY nu≥2, witnessed by the rank-one sparse midpoint chain with nu-1 internal vertices and minimum weight 1/nu, giving alpha=1/nu and exact depth nu. This proves the exact **largest** attainable exponent at prescribed (nu,d=nu) for arbitrary dense maps:
\[
\max\Sigma_{\nu,\nu}=1/\nu.
\]
It does **not** prove that the rest of that spectrum consists only of reciprocal exponents.

## Proof: build one kernel mode at every consecutive null-space level

Since d=nu, every step of every minimal reduction chain removes exactly one null direction. Choose one such chain and an orthonormal basis e1,...,e_nu of ker(X*) in reverse order, so that after nu-m steps the remaining face is
   W_m=U⊕span(e1,...,e_m),
where U=range(X*), and its exposing stress compressed to W_m in the next step is a positive multiple of E_mm. Put
   K_m = ker(L) ∩ S(W_m).
The subproblem restricted to the face S_+(W_m) has the same unique feasible target and **minimal** singularity degree exactly m. Proof: it has the inherited m-step remainder of the original chain; if a shorter chain existed, prepend the original nu-m exposing steps to obtain a chain shorter than nu in the full space, contradicting minimality.

For each m=2,...,nu we will find a nonzero H_m in K_m satisfying
\[
(H_m)_{mm}=0,\quad (H_m)_{m-1,m}=0,\quad (H_m)_{m-1,m-1}>0. \tag{1}
\]
The first equality holds automatically for every H∈K_m, since the first exposing stress on W_m is E_mm in K_m^perp.

For the others consider linear functionals phi(H)=H_(m-1,m-1) and psi(H)=H_(m-1,m) on K_m. If phi=c psi on K_m for any c∈R, the matrix
   Z=E_(m-1,m-1) -(c/2)F_(m-1,m)+M E_mm
lies in K_m^perp for every M, and is PSD of rank two on span(e_(m-1),e_m) for M>c²/4. It is an admissible *first* exposing stress of the reduced problem that removes two null directions simultaneously. Since only m-2 null directions then remain, its entire facial reduction would take at most (m-1) steps, contradicting that the reduced degree equals m. Hence phi is not a scalar multiple of psi, so some H_m∈K_m∩ker psi has phi(H_m)≠0. Change sign to obtain (1).

No linear algebra of the original kernel outside these restrictions is used.

## Proof: one PSD perturbation with residual order nu

Let U_0=U and U_j=span(e_j) for 1<=j<=nu. Give U_0 weight zero and U_j weight j. For the kernel coefficient H_m at exponent e=m-1:
- it is supported on U_0+...+U_m;
- its (m,m) and (m-1,m) blocks vanish by (1);
- consequently any nonzero (i,j) block (including support index i or j=0) satisfies
  i+j <= 2(m-1)=2e.
For the final positive coefficient E_(nu,nu) at exponent e=nu the same inequality holds.

Form the generalized polynomial
\[
Y(t)=X_*+\sum_{m=2}^{\nu} t^{m-1}H_m+t^\nu E_{\nu\nu}.
\]
The diagonal leading coefficient at U_j is:
- X*|U>0 for j=0,
- H_(j+1)[jj]>0 at order t^j for each 1<=j<=nu-1, since all earlier coefficients are either supported in fewer null directions or have zero (j,j) entry by (1),
- E_(nu,nu)>0 at order t^nu for j=nu.
The coefficient-rescaling lemma (proved independently in the parent weighted-flag memorandum) now applies: for some sufficiently large fixed sigma>0,
\[
X(t)=X_*+\sum_{m=2}^{\nu}e^{\sigma(m-1)^2}t^{m-1}H_m
           + e^{\sigma\nu^2}t^\nu E_{\nu\nu}
\]
is **positive definite** for all sufficiently small t>0. The lemma follows by congruence with diagonal block scalings e^{sigma j²/2}t^{j/2}; all offdiagonal surviving normalized coefficients have factor e^{-sigma(i-j)²/4}, tending to zero as sigma→infinity while normalized diagonals stay positive. Thus this is a genuine *full PSD matrix*, not a collection of 2×2 PSD constraints.

Every H_m lies in ker L, whereas E_(nu,nu) does not (indeed the original first exposing stress is a nonzero multiple of E_(nu,nu) in (ker L)^perp). Therefore
\[
\|L(X(t)-X_*)\|=\Theta(t^\nu),\qquad
\|X(t)-X_*\|_F=\Theta(t).
\]
Hence no recovery estimate with exponent greater than 1/nu holds. This proves the universal theorem. QED.

## Sharpness, examples and scope
The maximal-depth sparse harmonic chains in 17_MAXIMAL_DEPTH_RECIPROCAL_SPECTRUM.md realize alpha=1/q for q=nu,...,2^(nu-1) and exact d=nu. Choosing q=nu yields alpha=1/nu, proving optimality of the **upper endpoint** universally. In particular:
   nu=2,d=2 => alpha<=1/2 (sharp)
   nu=3,d=3 => alpha<=1/3 (sharp)
   nu=4,d=4 => alpha<=1/4 (sharp)
   nu=5,d=5 => alpha<=1/5 (sharp)
   nu=6,d=6 => alpha<=1/6 (sharp).

This bound is independent of whether the dense-to-sparse depth-preservation conjecture holds. It is stronger than the generic square-root gap and, for large nu, proves severe instability from maximal depth alone.

**Not claimed:** that every dense maximal-depth exponent belongs to the reciprocal sparse list. The full fixed-(nu,d) arithmetic spectrum for nu>=4 is not yet established. The construction enforces only the upper endpoint, not an exhaustive enumeration of possible exponents.

## Novelty discipline
The use of minimal facial-reduction chains and general coefficient-rescaling to construct feasible arcs is self-contained; whether this precise degree-versus-exponent upper bound has appeared previously requires literature review. Do not claim novelty for classical facial-reduction definitions or semialgebraic selection.