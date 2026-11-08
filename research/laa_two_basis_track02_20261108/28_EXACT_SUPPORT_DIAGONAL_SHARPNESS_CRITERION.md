# Milestone 28 — a NECESSARY-AND-SUFFICIENT linear-algebra criterion for sharp stability of target-support diagonal measurements

Date 2026-11-08. This is a complete pointwise sharpness classification for individual rank-one quadratic observables on the support of a strictly stressed, uniquely recoverable real PSD target. It strengthens Milestone 27 from a sufficient support-basis assumption to an EXACT obstruction criterion, with explicit witnessing PSD curves. It does not solve the unrestricted near-quadratic universality problem.

## Theorem 1 — rank-one supported observable exponent dichotomy

Let G in R^{d x M} be Parseval, GG^T=I_d, with W=span{g_jg_j^T} and measurement map M_G(Z)=(g_j^T Zg_j). Let Z_*>=0 be a uniquely recovered target and let P project onto its range, Q=I-P. Assume a measured STRICT PSD exposing stress
  S=sum_j a_jg_jg_j^T >=gamma Q, SP=0, gamma>0.
Take any unit u in ran P, and define the local recovery modulus for one scalar functional:
  omega_u(t)=sup{|u^T(Z-Z_*)u|: Z>=0, ||M_G(Z-Z_*)||<=t}.

Then the following are equivalent:

(A) omega_u(t)=O(t), i.e. the supported quadratic observable is locally LIPSCHITZ-stable against all PSD competitors.

(B) There exists H_u in W with
  P H_u P = uu^T,
  P H_u Q=0.                                            (*)
The lower Q H_u Q block may be arbitrary and need not be PSD.

(C) The linear functional (A,C) ->u^T A u annihilates the kernel of the map
  T:S(P) direct-sum Hom(Q,P)->R^M,
  T(A,C)=M_G(A+C+C^T),
where A is supported on P and C=P C Q.

If these equivalent conditions fail, then
  omega_u(t)=Theta(sqrt(t)).
If they hold, then
  omega_u(t)=Theta(t).
In particular the optimal exponent is ATTAINED and is EXACTLY 1 or 1/2; no other exponent occurs for a target-support rank-one observable under the hypotheses.

The criterion (*) is a finite linear feasibility problem in the coefficients of H_u in W. It requires no genericity, no semialgebraic elimination, and no search over ambient PSD competitors.

## Proof of equivalence (B) <-> (C)

Write T*(lambda) in block form through H_lambda=sum_j lambda_j g_jg_j^T:
  <lambda,T(A,C)>=<P H_lambda P,A>+2<P H_lambda Q,C>.
Thus the functional (A,C)-><uu^T,A> is in ran T* if and only if there exists lambda with P H_lambda P=uu^T and P H_lambda Q=0. By finite-dimensional orthogonal duality, membership in ran T* is equivalent to annihilating ker T. Hence (B) and (C) are equivalent.

## Proof (B) => Lipschitz with explicit constants

Set delta=||M_G(Z-Z_*)|| for Z>=0. Let H_u=sum_j lambda_jg_jg_j^T satisfy (*). The strict stress and Parseval trace give
  0<=tr(QZ)<=kappa delta, kappa=||a||/gamma.
Since Z_* is supported on P and H_u has zero P-Q cross block,
  u^T(Z-Z_*)u
   =<H_u,Z-Z_*>-<Q H_u Q,QZQ>.
Consequently
  |u^T(Z-Z_*)u|
   <=[||lambda||+kappa||Q H_u Q||_op] delta.
Thus omega_u(t)=O(t).

To obtain the reverse omega_u(t)>=c t, test
  Z(t)=Z_*+t uu^T>=0.
Then u^T(Z(t)-Z_*)u=t, and ||M_G(Z(t)-Z_*)||=t||M_G(uu^T)|| with positive coefficient because trace is measured. This shows the optimal Lipschitz exponent is exactly one and attained.

## Proof of necessity via an explicit PSD quadratic curve

Suppose (*) fails. By the duality equivalence, choose A in S(P), C=P C Q such that
  T(A,C)=0,   f:=u^T A u !=0.
Write Z_*=D direct-sum 0 on P direct-sum Q with D positive definite on P. Fix
  b>||C||_op² / lambda_min(D)+1.
For sufficiently small t>0, define
  Z(t)=[ D+tA, tC; tC^T, t² b I_Q ].
Its upper block is positive definite, and its Schur complement is
  t²[bI_Q-C^T(D+tA)^(-1)C]>=0,
so Z(t)>=0 among unrestricted-rank competitors.

Its source data residual is EXACTLY
  M_G(Z(t)-Z_*)=t T(A,C)+t² b M_G(Q)
             =t² b M_G(Q).
Because Q!=0 and the frame is Parseval, ||M_G(Q)||>0 (the data sum equals tr Q). Yet
  u^T(Z(t)-Z_*)u=t f.
Thus no scalar recovery exponent larger than 1/2 is possible. In particular a local Lipschitz estimate is impossible, proving necessity (A)=>(B).

## Proof of the universal sqrt upper bound

Strict stress and Parseval give tr(QZ)<=kappa delta and trZ<=trZ_*+sqrt(M)delta. Thus ||PZQ||_F<=C sqrt(delta) and ||QZQ||_F<=C delta.

The restriction of M_G to symmetric matrices supported on P is injective: otherwise a nonzero unmeasured supported H would yield two exact PSD perturbations Z_*+/-tH, contradicting uniqueness. Let sigma_P>0 denote its least singular value. Then
  sigma_P||PZP-Z_*||_F
   <= ||M_G(PZP-Z_*)||
   <=delta+C(||PZQ||_F+||QZQ||_F)
   <=C' sqrt(delta).
Hence omega_u(t)<=C''sqrt(t), and the witnessing quadratic curve gives the matching lower bound when (*) fails.

This proves every assertion.

## Corollary 2 — exact criterion for RATE-NEUTRAL full ONB augmentation

Define the computable block-diagonal restricted measurement space
  H_P={P H P : H in W, P H Q=0} <= S(ran P).
There exists an ONB of R^d whose individual projector measurements can be appended to G with O(delta) residual cost for all PSD competitors if and only if H_P contains the projectors of an orthonormal basis of ran P.

Proof. Any ONB of the full space adapted to ran P splits into support and kernel vectors. Kernel-vector quadratic measurements are O(delta) by the strict stress. Each support-vector measurement is O(delta) exactly when it satisfies Theorem 1. Therefore an adapted full ONB is safe if and only if a support ONB satisfying (*) exists. QED.

Whenever this holds, Milestone 27 applies to give a ONE-STAGE positive-data two-ONB lift with
  N<=M+4d+4,
  omega_final(t) ~ omega_source(t)+sqrt(t),
and exact objective/PSD fibre correspondence.

For rank(Z_*)=1, the criterion is ALWAYS satisfied: H=I_d belongs to W by Parseval, PIP=uu^T and PIQ=0. Thus the rank-one strict-stress sharp transfer in Milestone 27 is a special case with NO additional assumptions.

## Example/consistency checks

1. The chordal missing-(1,3) frame of Milestone 26 has Z_*=diag(1,1,0,0) and W={H:H_13=0}. Its support basis e1,e2 has projectors in W and satisfies (*), so the ONE-STAGE signed reflection lift preserves its original 1/2 exponent. The DOUBLE-ZERO construction from Milestone 26 instead creates an avoidable 1/4 exponent. This clarifies precisely why the two architectures differ.

2. For the tetrahedral W={H in S^3:H_11=H_22=H_33} with rank-one target u1u1^T and strict stress I-u1u1^T, the actual projector u1u1^T happens to be in W, but the theorem does not need that: H=I suffices. The W-space has no admissible whole-space ONB; a RATE-NEUTRAL augmented ONB exists.

3. If (*) fails for a chosen support vector u, the Schur curve above is a CERTIFICATE of unavoidable square-root sensitivity for that new observable, so adding it as an independent measurement can improve the original inverse problem's recovery exponent. The theorem makes no claim that a full ONB is impossible unless it tests all support bases.

## Hostile audit

- The strict stress is a GLOBALLY PSD measured matrix with a fixed gap on the target kernel. A facial reduction certificate positive only after earlier restrictions cannot be substituted.
- Necessity uses a genuine full-PSD Schur-complement curve, not just a formal kernel tangent.
- The curve's bottom t² b I is PSD, makes the measured residual exactly order t², and its trace is detected, so the coefficient cannot vanish.
- A supported observable may have H_u with indefinite QH_uQ; this is harmless because that term is controlled by exterior PSD mass.
- The source uniqueness is needed only for the sqrt upper bound and optimal-exponent classification, not for the necessity/sufficiency of Lipschitz control.
- The basis-augmentation criterion concerns ONBs ADAPTED to target support. It does not classify all non-adapted ONBs, where support and kernel contributions can interact differently.
- Linear-algebra feasibility is finite and effective given P and W, but a supplied exact target support and strict stress are still required.
