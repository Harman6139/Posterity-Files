# Milestone 26 — EXPLICIT SHARP NON-LIPSCHITZ EXPONENT HALVING IN POSITIVE TWO-BASIS UNIVERSAL FRAME COMPOSITION

Date 2026-11-08. Proved exact algebraic counterexample to an overly strong sharpness claim for the generic double-zero compiler, and (by the signed-anchor second stage) even for strictly-positive, no-zero-overlap, rank-three two-basis lifts. The source exponent is 1/2; the lifted exponent is EXACTLY 1/4. This is an architectural no-go, NOT a theorem that every possible universal two-basis lift degrades exponents.

## Theorem 1

Define six column vectors in R^3 by
  g1=(sqrt(3)/2,0,0),
  g2=(0,sqrt(23)/6,0),
  g3=(1,1,0)/sqrt(8),
  g4=(1,-1,0)/sqrt(8),
  g5=(0,1/3,1)/sqrt(2),
  g6=(0,1/3,-1)/sqrt(2).
Let G=[g1 ... g6] (3 by 6), define the rank-one frame measurement map
  M_G(Z)=(g_j^T Z g_j)_{j=1}^6,
and take Z_*=diag(1,1,0).

Then:
(A) GG^T=I_3 and span{g_j g_j^T}={H in S^3:H_13=0}, a five-dimensional operator system. Every entry of M_G(Z_*) is positive. The PSD source fibre at M_G(Z_*) is the singleton {Z_*}, among all ranks. Its OPTIMAL ATTAINED local exponent is 1/2.

(B) Apply the exact two-zero Naimark dilation of Milestone 21. This produces two honest ONBs in ambient dimension n=2*6-3=9, and a unique rank-two PSD target Y_*=F_0^T Z_* F_0. The exterior rotation may be chosen so that ALL 81 entries of the transition matrix are nonzero. The optimal attained local recovery exponent of the ambient rank-unrestricted two-basis inverse problem is EXACTLY 1/4.

(C) Apply the positive signed-anchor second dilation of Milestone 24 to this n=9 intermediate problem. The final dimension is N=5n+4=49, its target is rank THREE, ALL 98 target diagonal observations are STRICTLY POSITIVE, and every transition matrix entry can be chosen nonzero (also with non-reflection basis transition). Its optimal attained local exponent is EXACTLY 1/4. After scaling by the fixed target trace 3, the target has trace one without changing these exponents. Both stages preserve exact feasible fibres, positive decoding, and objective values. The source-to-final map therefore halves a GENUINELY NON-LIPSCHITZ exponent even under the usual nondegeneracy requirements.

## Proof of A: source frame and optimal source exponent

Directly summing the six outer products gives GG^T=I:
  diag1:3/4+1/8+1/8=1,
  diag2:23/36+1/8+1/8+1/18+1/18=1,
  diag3:1/2+1/2=1,
and the off-diagonal terms cancel in the +/- pairs.
The outer products recover the three diagonal directions and the 12,23 off-diagonal directions, and contain no 13 entry. Thus their span is exactly the five-dimensional path graph measurement space.

Every Z>=0 with the same source data has Z33=0, so PSD positivity forces row3 and column3 zero. The other measured coordinates Z11,Z22,Z12 then force Z=Z_*. This proves exact uniqueness.

Let delta=||M_G(Z)-M_G(Z_*)||_2. The five-dimensional span identity and finite-dimensional norm equivalence give
  |Z11-1|+|Z22-1|+|Z33|+|Z12|+|Z23|<=C delta.
For Z>=0 and small delta, |Z13|<=sqrt(Z11 Z33)<=C sqrt(delta). Therefore ||Z-Z_*||_F<=C sqrt(delta).

For 0<t<1, put a(t)=sqrt(1-t²/2) and
  V_t=[[a(t),0],[0,a(t)],[t,0]] in R^{3 x 2},
  Z(t)=V_t V_t^T
      =[[1-t²/2,0,a(t)t],
        [0,1-t²/2,0],
        [a(t)t,0,t²]].
It is PSD rank two, tr Z(t)=2=tr Z_*, and
  Z(t)-Z_*=t a(t)(E13+E31)+t² H_2,
  H_2=diag(-1/2,-1/2,1).
The 13 cross term is unmeasured, so
  M_G(Z(t))-M_G(Z_*)=t² v,
where
  v=(-3/8,-23/72,-1/8,-1/8,17/36,17/36),
  1^T v=0, v!=0.
Meanwhile ||Z(t)-Z_*||_F~sqrt(2)t. Hence every exponent greater than 1/2 fails, and 1/2 is attained.

## Proof of B: explicit exact cancellation with a PSD Gram factorization

Complete the Parseval rows of G with K in R^{3 x 6} so [G;K] in O(6). Let
  F_0=[G, 0_{3 x 3}] in R^{3 x 9}.
The canonical two-zero transition is
  U_0=[[K^T,G^T G],
       [0_{3 x 3},K]] in O(9).
Set S1=[K^T;0] and S2=[0;I_3], both 9-by-3, and S=[S1,S2]. Then [F_0^T,S] is an orthogonal 9-by-9 matrix. The first six standard-basis vectors are
  e_j=F_0^T g_j+S1 K e_j;
the last six columns of U_0 are
  u_j=F_0^T g_j+S2 K e_j,
and the other columns in each basis are exterior-only and have zero target outcomes.

The following 2-by-6 matrix is the explicit cancellation certificate:
  W0=[
    [sqrt(3)/8,0,-3/(4sqrt(8)),-3/(4sqrt(8)),0,0],
    [0,sqrt(23)/24,5/(4sqrt(8)),-5/(4sqrt(8)),
      -17/(12sqrt(2)),-17/(12sqrt(2))]
  ].
A direct six-column computation gives the TWO key identities
  W0 G^T=0,                                         (1)
  2 sum_{a=1}^2 (g_j)_a (W0)_{aj}=-v_j
      for all j=1,...,6.                          (2)

Moreover the 1st row of W0 vanishes at j=5,6, exactly where the 3rd row of G can be nonzero. Consequently
  2 diag[G^T V_t (W0/a(t))]=-v
for EVERY 0<t<1, not merely asymptotically. The rows of W0/a(t) remain orthogonal to G.

First work with unrotated U_0. In coordinates (source R^3, exterior S1 R^3, exterior S2 R^3) define the 9-by-2 Gram factor
  L_t=[ V_t ; t²(W0 K^T/a(t))^T ; t²(W0 K^T/a(t))^T ].
Set Y(t)=[F_0^T,S] L_t L_t^T [F_0^T,S]^T >=0.
Its rank is two for t small and its compression is F_0Y(t)F_0^T=Z(t).

For each first-basis surviving vector e_j, the quadratic data expansion consists of:
  g_j^T Z(t)g_j
  +2t² g_j^T V_t (W0/a(t)) e_j
  +t^4 [quadratic exterior term].
The order-t² source residual t² v_j is canceled EXACTLY by (2). The same holds in the second basis, because the exterior factor is duplicated on S1 and S2. All exterior-only outcomes are O(t^4). Therefore
  ||A_(U0)(Y(t)-Y_*)||_2=Theta(t^4).
The lower Theta(t^4) is immediate from trace: trY(t)=2+2t^4||W0 K^T/a(t)||_F², whereas trY_*=2, and the coefficient is strictly positive. The distance is at least the isometric source compression:
  ||Y(t)-Y_*||_F >=||Z(t)-Z_*||_F~sqrt(2)t.

Now rotate the exterior to remove all basis overlap zeros as in Milestone 21. Let Omega in O(6) be sufficiently close to I_6 so that the 6-by-6 matrix
  C_Omega=[ [I_3;0_3], Omega [0_3;I_3] ]
is invertible. Let W_Omega be the orthogonal ambient operator acting as identity on source F_0^T and as Omega in the exterior basis S, and set U=W_Omega U_0. Choose generic Omega in this neighbourhood so ALL entries of U are nonzero, which Milestone 21 proves is possible.

Define the fixed 2-by-6 exterior coefficient
  B_Omega(t)
   =[W0 K^T,W0 K^T] C_Omega^(-1)/a(t).
Replace L_t by
  L_t^(Omega)=[ V_t ; t² B_Omega(t)^T ] in source/exterior coordinates.
Its first-basis cross block acts on S1 as W0K^T/a(t) and its second-basis cross block acts on Omega S2 as the same matrix. Hence the identical cancellation occurs in BOTH bases. The exterior quadratic terms remain O(t^4) because C_Omega^(-1) is bounded and a(t) stays away from zero. Positivity and constant rank follow from the Gram factorization, and the trace defect is t^4||B_Omega(t)||_F²>0. Therefore the sharp upper obstruction alpha_lift<=1/4 holds even with every basis overlap nonzero.

The independent all-ambient PSD estimate in Milestone 21 gives
  omega_lift(delta)<=C omega_source(C sqrt(delta))+C sqrt(delta)=O(delta^(1/4)),
since omega_source(t)=Theta(sqrt(t)).
Thus alpha_lift>=1/4. Combining proves the EXACT attained exponent 1/4.

## Proof of C: strictly positive final observations, rank 3 and unchanged exponent 1/4

Apply the second signed-anchor lift from Milestone 24 to the two-basis system of order n=9. Its rank-one Parseval compiler uses M'=2n+1=19 vectors (two ONBs scaled by 1/sqrt(2), with one duplicated column) and an admissible ONB already present. The signed construction yields an (n+1)-by-(5n+4)=10-by-49 Parseval frame F_1 and U_1 in O(49), with a measured certificate S_0>=2Q, strictly positive anchor coordinate in EVERY frame vector, and no zero entries in U_1. Generic equal-weight rotation makes U_1 nonreflection while leaving the certificate and exact compressed measurement span unchanged.

The final target is
  X_*=F_1^T (Y_* direct-sum [1])F_1.
It has rank 2+1=3 and trace 2+1=3, and all 98 two-basis outcomes are strictly positive. The complete PSD fibre is the singleton {X_*}, since the intermediate two-zero fibre was a singleton. The embedded curve
  X(t)=F_1^T (Y(t) direct-sum [1])F_1
is PSD of rank 3, has distance Theta(t) and final two-basis residual Theta(t^4): the reflection lift's compressed frame analysis is linearly equivalent to the intermediate two-basis map, including for the generic small equal-weight rotation. Thus alpha_final<=1/4.

Conversely the signed-reflection all-ambient upper theorem (earlier Track 02 and Milestone 22) gives
  omega_final(delta)<=C omega_lift(Cdelta)+C sqrt(delta)
                    =O(delta^(1/4)),
proving alpha_final>=1/4 and exact sharpness.

Divide target and curve by 3 to obtain a trace-one rank-three example without changing the exponent.

## Why the new result matters

This disproves the informal belief that a generic exact frame-to-two-basis compilation preserves every source non-Lipschitz rate automatically. The source is already unstable with exponent 1/2, but the all-rank two-basis lift has exponent 1/4, even with strictly positive final observations, all nonzero basis overlaps, and equal target/curve rank three.

Thus Milestone 24's exponent interval
  alpha_source/2 <=alpha_final<=min(alpha_source,1/2)
is attained at its LOWER endpoint for alpha_source=1/2. The square-root loss in the first stage is not a removable artifact of the norm inequalities. A universal sharpness-preserving compiler must use the cross-output transversality mechanism of Milestone 22 (or something genuinely different).

This is an architectural counterexample, not an impossibility for all two-basis representations of the given source problem. The earlier positive single-certificate graph lift (Track 02 original theorem) preserves the source exponent 1/2, so DIFFERENT embeddings of exactly the same source geometry can behave differently.

## Hostile audit

1. The source target is rank 2, source competitor curve rank 2; no high-rank-only pathology is invoked.
2. The source trace is exactly constant along Z(t), allowing exterior cross terms to cancel all order-t² source data. A changing source trace would not be cancelable at first order because cross terms have zero trace.
3. Every identity uses the explicit W0 matrix; no numerical pseudoinverse or generic solvability assumption hides a gap.
4. The exterior-rotation repair uses the explicit invertible matrix C_Omega and a Gram factor; it retains PSD rank and exact order-t² cancellation.
5. The target is uniquely recoverable among arbitrary PSD matrices, both at source and after each lift.
6. The final strictly positive target is rank 3 and can be normalized to trace one.
7. The upper bound alpha>=1/4 holds for ALL ambient PSD competitors and is proved independently from the special lower curve.
8. Numerical checks (optional) confirm residual/t^4 converges to a positive limit but do not replace the exact algebraic proof.
9. The statement does not assert any impossibility of sharp universal embeddings outside this two-zero-plus-signed-anchor architecture.
