# Milestone 29 — exact tangent-kernel criterion for depth-one PSD sharpness and a stronger basis-augmentation theorem

Date 2026-11-08. This complements Milestones 27-28: residual-wise O(delta) safe ONB augmentation is sufficient for preserving a recovery modulus, but it is NOT necessary. If sufficiently many independent unstable tangent directions survive, the worst-case sqrt modulus is preserved even when no support-basis projector is individually O(delta)-stable. A complete three-dimensional example is given.

## 1. Complete tangent rank classification under a strict measured stress

Let G in R^{d x M} be Parseval (GG^T=I), M_G(Z)=(g_j^T Zg_j), and Z_*>0 on its support E=ran Z_* with rank r and projection P. Let Q=I-P. Assume Z_* is uniquely recovered from M_G and there is a strict PSD exposing stress S in W=span{g_jg_j^T} with
  SP=0, S>=gamma Q, gamma>0.

Define the measured first-order target-tangent map
  T:S(E) direct-sum Hom(E^perp,E) ->R^M,
  T(A,C)=M_G(A+C+C^T),
where A=PAP and C=PCQ. Put h=dim ker T.

**Theorem 1.**
  h=0 if and only if the full target recovery is locally LIPSCHITZ.
  h>0 if and only if its sharp attained exponent is exactly 1/2.
In particular under a strict stress no intermediate exponent between 1/2 and one occurs, and the distinction is a simple rank test of T.

Proof: For any PSD Z with residual delta, strict stress gives tr(QZ)<=kappa delta and hence ||QZQ||<=kappa delta. Decompose
 Z-Z_*=A+C+C^T+B with B=QZQ>=0.
The measured data give
  T(A,C)=M_G(Z-Z_*)-M_G(B),
whose norm is <=(1+||M_G||kappa)delta.
If ker T=0, its least singular value is positive and ||A+C+C^T||<=C delta. Adding B proves Lipschitz recovery. Conversely, if (A,C) is a nonzero kernel element, set D=Z_*|_E>0 and choose b>||C||²/lambda_min(D)+1. Then
  Z(t)=[D+tA, tC;tC^T,t²bI_Q]
is PSD for all sufficiently small t>0 by Schur complement. Its measured residual is exactly t² b M_G(Q), nonzero because the frame measures trace and Q!=0, while its Frobenius distance from Z_* is Theta(t). Therefore no exponent >1/2 holds. The universal O(sqrt(delta)) bound follows from the strict stress, PSD cross-block estimate, and injectivity of M_G on supported S(E) (uniqueness). This proves Theorem 1, including attainment.

## 2. Augmentation does not kill high-dimensional tangent instability

Fix any ONB adapted to E direct-sum E^perp. Append its rank-one projectors at small positive Parseval weight to G, as in Milestone 27, forming a new rank-one Parseval frame G'. No requirement is made that the added measurement residuals be O(delta) in the original data metric.

On tangent directions (A,C), every added kernel-basis projector has ZERO value because Q(A+C+C^T)Q=0. The r added support-basis measurements have values u_i^T A u_i, whose sum is tr A. But the ORIGINAL Parseval frame already measures trace, and every (A,C) in ker T satisfies tr A=0. Therefore the new ONB introduces AT MOST r-1 independent linear constraints on ker T, so
  dim ker T_aug >= h-(r-1).                              (2.1)

**Theorem 2 (rank-surplus sharpness preservation).** If h>=r, then for EVERY adapted support/kernel ONB, the augmented source problem remains uniquely recoverable with attained sharp exponent 1/2. Its worst-case local modulus is Theta(sqrt(t)), hence equivalent up to constants to the original modulus, even though its INDIVIDUAL new residual coordinates may be order sqrt(t) rather than order t.

Applying the ONE-STAGE signed positive two-basis dilation to the augmented frame gives
  N<=M+4d+4
(or after exact conic sparsification, <=2q+4d+4, q=dim W),
with strict positive target observations, nonzero basis overlaps, exact full-PSD fibre, positive decoder and objective preservation, rank increase one, and sharp exponent 1/2, PRESERVED from the original source.

Proof: h>=r makes (2.1) positive, so Theorem 1 applied to the augmented frame yields sharp exponent 1/2. The old exact data remain among the augmented measurements, so the feasible target is still unique; the old stress belongs to the augmented frame span, so the same strict gap persists. The signed reflection transfer then gives omega_final~omega_aug+sqrt(t)=Theta(sqrt(t))=omega_source up to constants. QED.

This is a strictly broader SHARPNESS (not residual-wise) preservation principle than Milestone 27's rate-neutral projector test.

## 3. An explicit three-dimensional example: NO admissible ONB, NO safe support ONB, yet sharp preservation

Let d=3 and let
  v1=(1,0), v2=(-1/2,sqrt(3)/2), v3=(-1/2,-sqrt(3)/2)
be unit vectors in R², with sum v_j=0, pairwise dot -1/2, and sum v_jv_j^T=(3/2)I_2. Fix c=1/2 and let
  g_j=sqrt(2/3)*(v_j,c) in R³ (j=1,2,3),
  g4=sqrt(1-2c²)*e3=e3/sqrt2.
Then
  sum_{j=1}^4 g_jg_j^T=I_3,
so G is a real four-column Parseval frame. The three top projectors v_jv_j^T are independent and span S².

Take
  Z_*=diag(1,1,0)
of rank r=2. Since g4g4^T=(1/2)e3e3^T, the stress S=e3e3^T is measured, PSD and has kernel span(e1,e2). All exact PSD competitors are thus supported on this 2-plane; the three remaining measurements span S² on the plane, proving exact PSD target uniqueness among unrestricted-rank competitors.

The compressed first-order tangent map has dimension 5 (three A coordinates plus two cross coordinates). The g4 measurement is identically zero on tangent directions, and the other three have independent linear restrictions, so rank T=3 and h=5-3=2. In particular h=r=2; Theorem 1 gives sharp original exponent 1/2, and Theorem 2 guarantees that appending ANY adapted ONB preserves the sharp 1/2 exponent.

An explicit witnessing tangent kernel vector is
  A=diag(1,-1) on E,  C=-e1 e3^T.
For j=1,2,3 the relation
  v_j^T A v_j+2c v_j^T(-e1)=0
is checked directly: it is 1-1=0 at v1 and -1/2+1/2=0 at v2,v3. The g4 tangent measurement vanishes too. One can take the rank-two PSD curve
  Z(t)=[ I_2+t diag(1,-1), -t e1;
         -t e1^T, t²/(1+t) ], 0<t<1/2.
Its Schur complement is identically zero, its source data residual is Theta(t²), and its Frobenius distance is Theta(t). Hence the 1/2 sharpness is witnessed by rank-two competitors at constant rank.

**No original admissible ONB.** The rank-one allowable lines of W=span{g_jg_j^T} are EXACTLY the four lines spanned by g1,g2,g3,e3. To verify this, a block matrix H in W has its cross-to-e3 vector equal to c(a-d,-2b), where [[a,b],[b,d]] is its top 2-by-2 block; the independent e3e3 coefficient is free. For a rank-one H=xx^T with x=(u1,u2,z), its top block is uu^T and the cross condition becomes
  z(u1,u2)=c(u1²-u2²,-2u1u2).
If u!=0, collinearity forces
  u2(u2²-3u1²)=0,
i.e. precisely the three directions v1,v2,v3. If u=0, x is along e3. The four allowed lines are pairwise NONORTHOGONAL, because g_i^T g_j=(2/3)(-1/2+c²)=-1/6 for i!=j<=3 and g_i^T e3=sqrt(2/3)c!=0. Thus W has no admissible orthonormal basis.

**No residual-wise safe support ONB.** If H in W has zero E-to-E^perp cross block, its top 2-by-2 block must be a scalar multiple of I_2: with H=sum_j alpha_j g_jg_j^T+beta e3e3^T, the cross condition is sum_j alpha_j v_j=0, which implies alpha_1=alpha_2=alpha_3. Therefore the block-diagonal image H_P from Milestone 28 is just R I_2, containing no rank-one support projector. By Milestone 28, EVERY supported unit-direction quadratic observable is only square-root stable, not Lipschitz; no adapted ONB can be appended with O(delta) residual equivalence.

Nonetheless, because the tangent kernel has dimension h=2>r-1=1, every adapted basis addition leaves at least one bad tangent direction and preserves the WORST-CASE square-root modulus. The one-stage signed dilation gives an all-positive, no-zero-overlap, rank-three two-basis target with order
  N<=M+4d+4=4+12+4=20,
exact full-ambient uniqueness and optimal exponent 1/2. This is sharper and smaller than the universal two-zero+anchor construction, and its success is not explained by individual residual-wise safe augmentation.

## 4. Audit and limitations

1. The source target is strictly stressed and unique; both claims are proved explicitly, not inferred from floating-point evidence.
2. The tangent kernel calculation is on the full real PSD tangent model S(E)+cross(E,E^perp); the lower repair includes t² on the kernel block and is genuinely PSD.
3. The number of new constraints on ker T is at most r-1, not r, because the trace was already measured by Parseval tightness. Kernel-basis measurements vanish to first order.
4. Theorem 2 concerns equivalence of WORST-CASE MODULI at a fixed target, not pointwise equivalence of EVERY candidate's measured residual vector. Example 3 proves this distinction is real.
5. The source W has no allowable ONB even though it has a Parseval frame; the allowable line classification is exact.
6. The bounded-size lifted N<=M+4d+4 construction is target-adapted and assumes a strict stress certificate. The unrestricted dense SDP universality problem remains open outside this certified class.
