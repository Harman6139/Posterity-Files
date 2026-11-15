# Checkpoint 06 — independent nonlinear audit ledger

2026-11-15. Continuation branch: research/pro-m1-spectral-frontier-audit-20261115. Parent: 637d4417c63751d1bfaef51d4ecd23549081ae15.

The full frontier is NOT yet certified in this checkpoint. The objective is to audit the entire forward-invariant spectral region, not just a finite trajectory or the initial phase.

## Sources recovered

Both portions of Checkpoint 05 were fetched from the immutable parent. The attached DRS_progress_checkpoint_20261115.zip was extracted; its original balanced gamma=1 matrix data and diagnostic are available. The gamma=2 family is the distinct construction in Checkpoints 04–05. No new gamma=1 asymptotic claim is made.

## Independent leading-order derivation

Write beta=1/2, Caff=2(C-G)/3 and D=2Caff-C. The leading graph coefficients of the positive spectral space, before imposing symmetric fast equilibrium, obey

    y=-H/b,
    x=(beta*y-Caff-G)/(1+b),
    zeta=xi+beta*omega,
    (D+H^2/b-beta^2)*omega=beta*xi-(chi-H*eta/b).

The last denominator is 1/8 at the proposed reference point. At symmetric fast equilibrium C=Caff+H^2/b, G=H^2/b-Caff/2, Caff=2H^2/b^2-H/b, these become x=-H^2/b^2 and y=-H/b. The leading update of chi is exactly chi_next=H*eta/b. At H/b=3/4, chi=3eta/4, the remaining graph coefficients are zeta=3xi, omega=4xi.

These equations follow by dividing the four exact spectral Riccati equations by t,1,t,t^2, respectively. They identify the fast error chi-H*eta/b as the natural variable; using chi-3eta/4 too early conceals a dependency on the slow H error.

On the fast equilibrium, the asymmetric cone-complementarity equation (vplus*s)12 gives

    Delta ha/t^4=(3j/8-H0*Cafa)/b0+O(t^2)
       =-9sqrt(3)j/8-9xi^2-3sqrt(3)xi*eta/4+O(t^2).

The cut equations (vplus*s)06 and (s*vplus)26 give the leading rotational increments N eta t^3 and -N xi t^3, N=9/16. The large negative spectral direction gives mean top-diagonal increment b0*N^2*t^3. These are algebraic leading coefficients, not yet an orbit-asymptotic conclusion.

## Diagnostic scope

A newly written independent 90-decimal mpmath implementation of the exact Frobenius affine projection and PSD projection tests phases 0, pi/5, pi/2, pi at t=1/100,1/1000,1/10000. It checks the phase increments, radius coefficient, asymmetric filter, diagonal complementarity, and corrected amplitude equation. In these tests the residuals after subtraction of the stated coefficients are consistent with the claimed additional factor t^2. This is corroboration only and is not a proof of uniformity or trapping.

## Next proof obligation

Use a fixed compact spectral chamber, retain the correct moving fast targets, and separate (i) strictly contracting fast recurrences, (ii) t^2-scale stable filters, and (iii) t^4-scale amplitude and radius evolution. The bound for a later scaled error must not silently enter the leading forcing constant of an earlier one. A full analytic first-exit argument, or an equally rigorous normally-attracting-manifold argument, is still required before certifying persistent transverse steps.
