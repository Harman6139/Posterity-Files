# Checkpoint 06 — exact ADMM transfer and the averaging scale of a resonance

Date: 2026-11-15. Sections 1–3 are independent consequences of the new certificate and averaging theorems. Section 4 is explicitly conditional on the earlier gamma=2 resonance theorem; it is not a new verification of that theorem. Classical DRS–ADMM equivalence is not claimed as new.

## 1. The precise ADMM algorithm and conjugacy

Consider the feasibility splitting

    minimize indicator_U(x)+indicator_K(v)
    subject to x-v=0,

with a fixed penalty rho>0 and scaled multiplier lambda. Its standard exact ADMM iteration is

    x_(k+1)=P_U(v_k-lambda_k),
    v_(k+1)=P_K(x_(k+1)+lambda_k),
    lambda_(k+1)=lambda_k+x_(k+1)-v_(k+1).          (1.1)

For indicator functions the scaled projection updates do not depend on rho. The conventional dual residual is rho(v_(k+1)-v_k).

Let T be the ORIGINAL affine-first DRS map from the other checkpoints and R_U=2P_U-I, an affine isometry. Define the reversed map

    T_rev(r)=r+P_U(2P_Kr-r)-P_Kr.

The exact affine identity is

    T_rev R_U=R_U T.                                (1.2)

Indeed T=(I+R_KR_U)/2, T_rev=(I+R_UR_K)/2, and affine R_U commutes with taking the midpoint of two points.

Given a DRS state Z_k, set

    r_k=R_U Z_k,
    v_k=P_K r_k,
    lambda_k=r_k-v_k.

Then (1.1) yields r_(k+1)=x_(k+1)+lambda_k=T_rev r_k and preserves these identities. Conversely, from arbitrary ADMM initial v_0,lambda_0, the identities hold from its first completed step, with r_1=x_1+lambda_0. Thus every ADMM start is covered after one irrelevant initial step.

The ADMM cone point v_k is exactly the cone shadow of the affine-first DRS orbit, not merely a comparable or transformed residual. For a general cone, lambda_k=-s_k, where s_k=P_(K*)(-R_UZ_k) is the positive dual shadow. If u_k=P_UZ_k and d_k=Z_(k+1)-Z_k, exact identities give

    x_(k+1)=2u_(k+1)-u_k,
    rAD_(k+1):=x_(k+1)-v_(k+1)=P_L d_k-d_(k+1),
    tAD_(k+1):=rho(v_(k+1)-v_k).                   (1.3)

To check the first identity, 2v_k-R_UZ_k=Z_k+2d_k and P_U is affine. The second follows by v_(k+1)=u_(k+1)+d_(k+1). Equivalently rAD_(k+1)=lambda_(k+1)-lambda_k=-[s_(k+1)-s_k].

## 2. Finite static certificates determine both ADMM residuals

Under the finite regularity certificate of Checkpoints 02–03, every ADMM start satisfies

    v_k=H_*sqrt(k)+O(log k),
    lambda_k=-G_*sqrt(k)+O(log k),
    sqrt(k) rAD_(k+1) -> -G_*/2,
    sqrt(k) tAD_(k+1) -> rho H_*/2.                 (2.1)

Proof. Insert the ACTUAL DRS last-step estimate from Checkpoint 03 into (1.3), and use v_k=u_k+d_k. The difference d_(k+1)-d_k is o(k^-1/2) directly from that estimate; no unspecified remainder is differentiated.

In the weakly infeasible feasibility problem both residuals therefore tend to zero even though no feasible point exists. The theorem identifies their precise natural-scale coefficients rather than interpreting vanishing residuals as a finite infeasibility certificate. Their norm coefficients are ||G_*||/2 and rho||H_*||/2, computable from the static program. Arbitrary redundant equality descriptions remain covered by the separate equation-residual formulas in Checkpoint 03.

## 3. Universal local residual recovery, even outside the regular class

For any closed convex semialgebraic cone and weakly infeasible affine space, use the centered windows of Checkpoint 01. Define

    rbarAD=(1/(2h))sum_(j=n-h)^(n+h-1) rAD_(j+1),
    tbarAD=(1/(2h))sum_(j=n-h)^(n+h-1) tAD_(j+1).

Then for h/n~1/log n,

    n^(1-p)rbarAD -> -pG,
    n^(1-p)tbarAD -> rho pH.                        (3.1)

Both are computed by telescoping endpoints, and the positive average of the cone iterates is a cone point with the exact equation-residual and sharp efficiency properties of Checkpoint 01.

Proof. The common-state remainder and boundedness of individual DRS steps give

    v_k=Hk^p+O(k^(p-eta')),
    lambda_k=-Gk^p+O(k^(p-eta'))

for a possibly smaller eta'>0, chosen below p. Here v=a+PZ+d and lambda=-(QZ-a+d), so the assertion follows without a raw natural-scale step bound. The two ADMM residual sums are the corresponding endpoint differences. The centered-secant proof of Checkpoint 01 applies verbatim. QED.

Thus this is an implementable residual recovery rule for the actual ADMM feasibility algorithm, not an assertion that every ADMM objective or variable-penalty scheme is covered.

## 4. Sharp window response for the previously constructed circular mode

This section assumes the exact gamma=2 spectral theorem saved in the earlier branch. Its scaled steps have the representation

    k^(3/4)d_k=V/4+R[cos(theta_k)F06+sin(theta_k)F26]+o(1),
    theta_(k+1)-theta_k=-omega k^(-1/2)+O(k^-1),
    R>0, omega=(9/16)/(4c0)^(1/2), c0=27sqrt(3)/256.

For centered means dbar_n and h=o(n):

(a) If h/sqrt(n)->ell in [0,infinity), then

 n^(3/4)dbar_n=V/4+R sinc(omega ell)
                     [cos(theta_n)F06+sin(theta_n)F26]+o(1),

where sinc(t)=sin(t)/t and sinc(0)=1. The scaled cluster circle therefore has radius R|sinc(omega ell)| in the displayed two-coordinate representation.

(b) If h/sqrt(n)->infinity, then n^(3/4)dbar_n->V/4.

In particular a window h=o(sqrt(n)) does NOT remove the obstruction. At comparable windows, exact phase-period resonances can cancel the leading circle; therefore h much larger than sqrt(n) is a robust sufficient condition, not a logically necessary condition for every finely tuned width.

Proof of (a). Summing the phase increments over |j-n|<=h gives, uniformly when h=O(sqrt(n)),

    theta_j=theta_n-omega(j-n)/sqrt(n)+o(1).

A Riemann sum of the complex exponential on [-ell,ell] is sinc(omega ell). The leading radial scale and amplitude vary by o(1) on the window. This proves the formula. The original phase has the whole circle as its cluster set, so the stated cluster circle follows.

For (b), uniformly over the window,

    theta_j=theta_(n-h)-2omega(sqrt(j)-sqrt(n-h))+O(h/n+n^-1/2).

The accumulated O(k^-1) term is O(h/n)=o(1). The integral of exp(-2i omega sqrt(t)) over [n-h,n+h] has magnitude O(sqrt(n)), by substituting u=sqrt(t) and integrating u exp(-2i omega u). Its normalized Riemann sum differs from its normalized integral by o(1). After division by 2h the magnitude is O(sqrt(n)/h)+o(1), which tends to zero. This proves (b).

This calculation explains the scale at which the local postprocessor removes the specific transverse resonance. It does not certify the source construction independently.

## 5. Diagnostic evidence

A separate script checked (1.2) and the ADMM cone-shadow identity through 200 steps of a seeded affine/PSD example. The largest floating-point discrepancy was 1.09e-13.

For the order-two affine slice [[t,1],[1,0]], the exact static profile at radius r is obtained by the unique c>0 solving c+c^3/r^2=1, with

    D(r)^2=2(c-1)^2+c^4/r^2.

For centered windows h=floor(n/log n), the computed quantity

    (log n)^2[||Qvbar-a||/D(||Pvbar||)-1]

was 0.10755017 at n=1000, 0.08800034 at n=10000, 0.08430011 at n=100000, and 0.08364746 at n=1000000. The proved limit in Checkpoint 01 is (1-p)/6=1/12=0.08333333. These are floating-point corroborations only; the proof is the finite-difference and profile argument.
