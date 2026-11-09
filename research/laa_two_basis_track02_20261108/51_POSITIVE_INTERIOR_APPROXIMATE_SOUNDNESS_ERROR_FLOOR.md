# Milestone 51 — a certified NUMERICAL ERROR FLOOR for approximately sound two-basis partial-trace SDP reductions

Track 02, 2026-11-09. This turns the exact and robust two-MASA commutator results of Milestones 49–50 into a condition-controlled lower bound on an ACTUAL SDP recovery soundness error. It is independent of the basis design and tensor ancilla dimension. It does NOT rule out quotients with a singular lifted feasible face, nonpartial-trace positive decoders, or arbitrarily ill-conditioned basis decompositions.

## Theorem (interiority/conditioning/error tradeoff)

Let m>=4, r>=1, N=mr, and let L⊂S^m be a real measurement space with gamma_4(L)>0 as in Milestone 50. For example generic L containing I_m with dim L>=2m+1 satisfies this hypothesis by Milestone 49.

Let B:S^N→R^(2N) be the two-real-orthonormal-basis diagonal map for arbitrary bases, and let D:S^N→S^m be the ORDINARY partial trace over R^r. Let Y_0 be an ambient PSD matrix with
  Y_0 >=rho I_N,  rho>0.
Define the exact two-basis data fibre
  T={Y>=0:B(Y)=B(Y_0)}.
Assume a soundness error guarantee
  ||P_L(D(Y)-D(Y_0))||_F <=eta_s
for EVERY Y∈T. Here P_L is Frobenius-orthogonal projection to the original measurement subspace L, so this is precisely the normalized ORIGINAL source-data residual error. The number eta_s may be any nonnegative real.

Define the two-MASA decomposition condition number
  kappa_B = sup_{X∈D1+D2, ||X||_F=1}
        min_{A∈D1,B∈D2,A+B=X}
           (||A||_op+||B||_op),
where D1,D2 are the two diagonal matrix spaces. This is a finite positive number for each fixed pair; it may diverge along degenerating pairs of nearly parallel MASAs. No dimension-only uniform bound is presumed.

Put
  x=eta_s/rho,
  c_mr=sqrt[(m-1)/(2(mr-1))].

**Theorem.** Necessarily
  8 kappa_B sqrt(r) x +2x² >=gamma_4(L)c_mr.     (1)
In particular, whenever x<=1,
  eta_s >=rho * gamma_4(L)c_mr/
                   (8 kappa_B sqrt(r)+2).       (2)

Equivalently a proposed uniformly accurate positive-interior ordinary-marginal two-basis SDP recovery scheme MUST have at least one of: (a) positive measured-source error, (b) vanishing positive-definite interior margin rho, (c) diverging two-MASA coefficient condition number kappa_B, or (d) increasing ancilla r at the quantitative rate encoded in (1). This tradeoff holds even when the approximate decoder is nonlinear at the algorithmic level, as long as the represented source output is the ordinary partial trace.

## Proof

1. Let K_B=ker B=(D1+D2)^perp (Frobenius orthogonal complement). For any H∈K_B with ||H||_F<=1, both Y_0+rho H and Y_0−rho H are PSD, because ||H||_op<=||H||_F<=1 and Y_0>=rho I. They have EXACTLY the same two-basis data as Y_0. Soundness applied to the two signs gives
   ||P_L D(H)||_F<=eta_s/rho=x.

2. Therefore the linear map P_L D restricted to K_B has Frobenius operator norm <=x. Taking its adjoint and using D*(Z)=Z tensor I_r gives
   ||P_(K_B)(H tensor I_r)||_F<=x||H||_F
for every H∈L. Since K_B is orthogonal to D1+D2, the left side is exactly the distance of H tensor I_r to D1+D2 in Frobenius norm.

3. Define the linear orthogonal projection
   R(H)=P_(D1+D2)(H tensor I_r).
It obeys
   ||H tensor I_r−R(H)||_op<=x||H||_F,
   ||R(H)||_F<=sqrt(r)||H||_F.

4. By the definition of kappa_B, each R(H) admits a decomposition R(H)=A_H+B_H with A_H∈D1, B_H∈D2 and coefficient norm <=kappa_B||R(H)||_F. A LINEAR decomposition with the same bound up to a fixed harmless factor can be selected by taking the Moore–Penrose least-Frobenius-norm right inverse of the sum map D1⊕D2→D1+D2. To keep the stated constant exact, interpret kappa_B as the operator norm of this FIXED linear splitting in the ||A||op+||B||op norm (or take the infimum over linear right inverses; the infimum is attained in finite dimension). Then
   ||A_H||op+||B_H||op<=kappa_B sqrt(r)||H||_F.

5. Apply the quantitative two-MASA theorem from Milestone 50 with approximation error epsilon=x and splitting coefficient K=kappa_B sqrt(r). It gives
   8Kx+2x²>=gamma_4(L)c_mr,
which is (1). If x<=1, use 2x²<=2x to obtain (2). QED.

## Norm-definition correction / precise implementation

For an exact numerical implementation, define kappa_B using the following LINEAR-splitting convention, rather than the pointwise minimum over decompositions:
  kappa_B :=
   inf_{S linear right inverse of (A,B)->A+B}
       sup_{X in D1+D2,||X||_F=1}
             (||S_1(X)||op+||S_2(X)||op).
This infimum is attained after eliminating the scalar intersection kernel by choosing its orthogonal complement; the Moore–Penrose solution is an explicit feasible splitter. In the statement and formulae, kappa_B ALWAYS means this linear-splitting quantity. The pointwise-minimum expression in the introductory line would be <=kappa_B and is NOT substituted into (1) without proof of a simultaneous linear selection.

## What this does and does not show

- The hypothesis is a strictly positive definite feasible lifted matrix Y_0 on the WHOLE ordinary tensor space. If the actual two-basis fibre lives in a proper PSD face, the margin rho=0 and this inequality does not apply.
- Soundness is required for ALL PSD matrices sharing exactly the same two-basis data as Y_0. This is the natural fixed-data weak recovery condition, not merely accuracy of a chosen optimization algorithm's one output.
- Normalized residuals use P_L, avoiding hidden scaling through an arbitrarily ill-conditioned original A. A general A is recovered using its nonzero singular values.
- kappa_B measures how the two diagonal bases ALMOST coincide and require large, mutually cancelling coefficients to represent source observables. It is an explicit condition number of an ordinary finite linear map.
- gamma_4(L)>0 is guaranteed generically for p>=2m+1; no uniform polynomial lower bound for arbitrary rational L is asserted.
- For any fixed design with rho>0 and finite kappa_B, the source recovery error eta_s has a STRICT positive lower bound, quantifying the exact impossibility of Milestone 49.
- This is a necessary error floor for partial-trace designs, not a universal SDP complexity lower bound nor an obstruction to other positive decoders.
