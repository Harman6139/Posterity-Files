# Checkpoint 09 — a deliberately coarse explicit rational witness

2026-11-15. This makes the sufficiently-large-M statement in Checkpoints 07–08 explicit by analytic bounds, not by a finite numerical orbit. The resulting integer is intentionally enormous. No claim of a practical onset or a short binary encoding for the starting matrix is made.

## 1. The specified start

Use exactly the affine space and rational formula Z0(M) in Checkpoint 08, with

    M_bullet = 10^(10^12).

This is a particular integer specified by an integer power, not an unspecified sufficiently large number. The expression is not meant to be expanded into decimal digits. The operation isqrt(3M_bullet^8) in Z0(M_bullet) is the unique integer n satisfying n^2<=3M_bullet^8<(n+1)^2. Thus every entry of the initial matrix is an exactly specified rational number.

We prove below that it satisfies the all-time trapping inequalities. The same proof in fact permits every integer M>=10^50000000000. These bounds are only existence witnesses with generous slack.

## 2. Numerical envelopes used in the proof

Set

    K_aux=10^10000,
    B=10^100000,
    C=B^1000=10^100000000,
    tau_*=C^(-1000).

Use the thick chamber from Checkpoint 07 with each of the five unscaled error radii at most delta_0=10^(-100), E in [-3,0], xi^2+eta^2 in [Fstar/4,2Fstar], and |f-fs0|<=1. Allow |ad|,|bd|,|fa|<=K_aux. Every primitive parameter other than these three auxiliary coordinates has absolute value below 10.

The following fine bounds will be used:

    ||e_s||<=C^2 tau, |e_H|<=C^4 tau,
    |e_chi|<=C^6 tau, ||e_a||<=C^10 tau,
    |e_j|<=C^14 tau, |f-fs0|<=C^8 tau.                  (2.1)

Weighted norms are those in Checkpoint 07. If tau<=tau_*, all these radii are far smaller than delta_0.

## 3. A quantitative analytic chart

Treat b and the four first-block and two second-block graph coordinates as seven unknowns. The charge equation and six Riccati equations in Checkpoint 07 form seven polynomial equations in 23 variables, including the 16 parameters. Upon expansion they have 154 terms in total, total degree at most 8, and coefficient magnitude at most 4/3. The accompanying exact symbolic script verifies these finite combinatorial bounds. For the estimates below it is enough to use 500 terms and coefficient magnitude 1000.

At tau=0 the seven unknowns have magnitude below 10. The Jacobian in these unknowns has determinant, up to sign,

    2 b0^3 (1+b0)^2 delta,
    delta=2c-C_sym+H^2/b0-1/4,

where C_sym denotes the scaled symmetric diagonal coordinate, not the large envelope C. On the thick chamber delta is within 10^(-90) of 1/8. The determinant is larger than 1/100 in absolute value, and every Jacobian entry is below 100. The adjugate formula, using six-by-six determinants bounded by 6!*100^6, gives inverse maximum-row-sum norm below 10^20.

On the complex box where all coordinates have magnitude at most 10^10001, every partial derivative of these polynomials through order 8 is bounded by

    500*1000*8!*(10^10001)^8 < B.                    (3.1)

Let rho=B^(-4). Around any real base point in the thick chamber, perturb tau and each parameter by complex quantities of magnitude at most rho, and put the unknowns in the maximum-norm ball of radius B^(-2) around their tau=0 values. The Newton map with the fixed base Jacobian has derivative norm at most

    23*10^20*B*(B^(-2)+rho)<1/2,

and its displacement of the ball center is at most 23*10^20*B*rho<B^(-2)/2. It is therefore a uniform contraction of that ball. The successive analytic iterates converge uniformly on every smaller polydisc, giving the holomorphic implicit branch there. This is a quantitative implicit-function argument, including uniformity over the whole annulus.

## 4. Bounds for the exact update and its remainders

Here are factored formulas that control the apparent divisions by tau. For the first block put

 Dg=1+tau(y^2+omega^2)+tau^2(x^2+zeta^2)
                         +tau^3(x*omega-y*zeta)^2,
 J00=1+tau*omega^2+tau^2*zeta^2,
 J01=-tau*y*omega-tau^2*x*zeta,
 J11=1+tau*y^2+tau^2*x^2.

With the symbols a,B_ref,beta_f,d,h,K,q of Checkpoint 07, the negative spectral coefficient matrix has entries N00=n00/t, N01=t*n01, N11=t^3*n11, where

 n00=[(B_ref-tau*h*y-tau^2*K*x)*J00
              +tau*(eta-h*omega-tau*K*zeta)*J01]/Dg,
 n01=[(B_ref-tau*h*y-tau^2*K*x)*(-y*omega-tau*x*zeta)
              +(eta-h*omega-tau*K*zeta)*J11]/Dg,
 n11=[(eta+tau*(xi*x-chi*y))*(-y*omega-tau*x*zeta)
              +(-q+xi*zeta-chi*omega)*J11]/Dg.

The required physical entries are exactly

 s00=t^3[n00*x^2+2tau*n01*x*zeta+tau^2*n11*zeta^2],
 s01=t^2[n00*x*y+tau*n01*(x*omega+y*zeta)+tau^2*n11*zeta*omega],
 s11=t[n00*y^2+2tau*n01*y*omega+tau^2*n11*omega^2],
 s02=-t[n00*x+tau*n01*zeta],
 s12=-[n00*y+tau*n01*omega],
 s06=-t^3[n01*x+tau*n11*zeta],
 s16=-t^2[n01*y+tau*n11*omega],
 s22=n00/t, s26=t*n01, s66=t^3*n11.

The second block is obtained by suppressing the sixth-coordinate couplings and reversing the asymmetric signs. The positive part is R+s.

On the complex chart, |Dg-1|<1/2. The radial update factor h_rad=t/t_next=1+tau^2*(s00/t^3+s33/t^3)/2 is also within 1/2 of 1 on a smaller fixed polydisc. The factored numerators involve only bounded-degree products of the displayed parameters and unknowns. Before removing vanishing powers of tau they are bounded by B^10 on that polydisc.

All apparent singularities in the rescaled map are removable. In particular n00-B_ref and its first tau derivative vanish at zero, so v22/t^3=(n00-B_ref)/tau^2 is analytic. Differences between the two blocks vanish to the additional orders stated in Checkpoint 07; the largest required division is the total third divided derivative for bd_next. The other coordinates use at most a first divided derivative. Cauchy's formula on successively halved discs therefore bounds all scaled update coordinates by B^30, with substantial slack. The charge update follows from a finite sum of their physical squared increments and is bounded by B^70. Composing the five polynomial/rational moving targets and the quartic amplitude correction raises this loose bound to at most B^100.

Cauchy's inequalities through order 8, allowing these same removable divided derivatives and the finite dimension factors, bound every Taylor and Lipschitz constant used in the hierarchy of Checkpoint 07 by B^200<C. For example each lost power of radius costs at most 2/rho=2B^4, and eight such powers, factorials, and dimension factors are all smaller than B^40. The gap between B^200 and C=B^1000 absorbs all changes between the displayed weighted and maximum norms. This calculation concerns exact analytic functions, not floating-point estimates.

The leading auxiliary reset functions are independent of the input ad,bd,fa. To bound those leading functions themselves, set these inputs to zero and repeat the preceding calculation with B_small=10^30 and all primitive parameters below 10. Bound (3.1) then holds with B_small; the same Jacobian estimate applies. Their leading values are below B_small^200=10^6000<K_aux/2. Thus the auxiliary box is invariant once C*tau<K_aux/2. The coarse f interval is invariant because its leading update b0*x*y is within 10^(-80) of fs0 on the thick chamber, and the remainder is bounded by C*tau.

## 5. Explicit contraction and barrier margins

For the symmetric and asymmetric fast maps, the exact positive Gram-defect minors are those in Checkpoint 05. In the weighted norms the smallest defect eigenvalue is at least 1/1000: for the asymmetric map its determinant is (44sqrt(3)-64)/9800>1/1000 and all its eigenvalues are at most one; the symmetric bound is stronger. Therefore both fast norms contract by at most 1-10^(-4). The scalar H filter has contraction rate at least one times tau on the thick chamber; the j filter has rate kappa>1.

Using the common bound C from Section 4, the hierarchy of Checkpoint 07 now gives the following forcing envelopes at the boundaries of (2.1):

 e_s: C*tau, versus contraction margin 10^(-4)C^2*tau;
 e_H: 2C^3*tau^2, versus margin C^4*tau^2;
 e_chi: C*tau, versus allowed radius C^6*tau;
 e_a: 4C^7*tau, versus margin 10^(-4)C^10*tau;
 e_j: 5C^11*tau^2, versus margin C^14*tau^2;
 f-fs0: 3C^5*tau, versus allowed radius C^8*tau.

The changing barrier widths cost at most a constant bounded by C times K*tau^3. At tau<=C^(-1000) this is smaller than half every relevant margin. Thus all fine estimates are preserved in the stated order, without choosing one bound in terms of a later bound.

The physical step bound ||d||_F<=C^20*t^3 follows from these inequalities and the exact factorizations. Hence |Delta E|<=C^42*tau^3. Since tau-tau_next>=c0*tau^3 and c0>1/10, the total charge variation is below 10C^42*tau_initial<1/10.

The corrected-amplitude remainder is bounded by C^50*tau^3. This follows by the same Taylor/Lipschitz bound, substitution of (2.1), and the exact quadratic cut identity; the largest fine radius is C^14*tau. The inward leading amplitude drift on the two protective bands is at least 10^(-7)*tau^2. At tau<=C^(-1000), the error is smaller than half this inward drift. The one-step change is also too small to cross a protective band. Finally the small-eigenvalue Schur margin is at least 10^(-5) at the targets, and all fine perturbations and analytic remainders are smaller than half this margin.

These explicit inequalities verify every smallness choice in Checkpoint 07 for tau_initial<=tau_*.

## 6. Entry of the particular rational matrix

For Z0(M), the rational square-root approximation has error below M^(-4)=tau_initial^2. Direct substitution into the polynomial target formulas bounds each of the five initial errors, and |f-fs0|, by 10^6*tau_initial^2. The charge differs from -3/2 by at most 10^6*tau_initial; Ftilde differs from 1/2500 by at most 10^6*tau_initial. The latter lies strictly inside [Fstar/2,3Fstar/2], with distance to either endpoint greater than 10^(-4). The auxiliary coordinates start at zero.

If M>=C^500=10^50000000000, then tau_initial=M^(-2)<=tau_*. All entry and invariance inequalities above hold. In particular M_bullet=10^(10^12) is admissible. This provides an exact rational affine system and one exact rational starting point for the persistent transverse circle proved in Checkpoint 08.

## Qualification

The absurdly large bound is an analytic certificate of one explicit witness, not a claim about the true onset, numerical stability, bit complexity, or the earlier gamma=1 data. The exact symbolic script checks the polynomial sizes and coefficient identities; the infinite-time proof is the analytic argument in Checkpoints 07–09.
