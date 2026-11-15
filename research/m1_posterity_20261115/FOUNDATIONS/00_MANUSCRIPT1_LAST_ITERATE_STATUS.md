# Manuscript I: last-iterate continuation, 2026-11-14

## Requested target

Prove for plain DRS on EVERY weakly infeasible SDP that a state expansion Z_k=V k^p+o(k^p) entails k^(1-p)(Z_(k+1)-Z_k)->pV, including exact original-equation residual asymptotics.

**That arbitrary-order PSD target remains unproved in this continuation. No PSD counterexample has been established.** The results below must not be described as its universal resolution.

## Complete new results

### 35 — Analytic firm nonexpansiveness is insufficient

Proof commit: 2d838fb810d8e5f40d9b44c22ee4695e68df83f6.
File: 35_ANALYTIC_FIRM_COUNTEREXAMPLE_TO_LAST_STEP_ASYMPTOTICS.md.

The rational analytic monotone operator

    A(t,y)=(-(1+3||y||^4/4)/t^4,
             (||y||^2 y+J y)/t^3), t>0, y in R^2,
    J=[[0,-1],[1,0]], T=(I+A)^(-1),

has a full-domain real-analytic semialgebraic firmly nonexpansive resolvent. Every orbit has state term 5^(1/5) k^(1/5)e0. From any off-axis start the scaled steps have cluster set

    5^(-4/5){(1,w):||w||=1},

and their norm tends to sqrt(2)5^(-4/5). On-axis starts have a different residual-norm constant despite the same state term. The Schur complement proving monotonicity is exactly 7/(4t^5). No earlier project theorem is a premise.

This is NOT shown to be the DRS map of an affine space and a PSD cone. It rules out the general-map shortcut, not the narrower SDP statement.

### 36 — Complete single-Lorentz theorem, all dimensions and all starts

Proof commit: ae397ac3880ea2176f85d68ecf530a54bcbd1391.
File: 36_EXACT_LAST_STEPS_FOR_ALL_SINGLE_LORENTZ_WEAK_INFEASIBILITY.md.

Let K be the standard Lorentz cone, U any affine subspace disjoint from K at distance zero, c=dist(0,U)>0, and e its time-axis unit vector. For T=I+P_K(2P_U-I)-P_U, from EVERY initial point,

    z_k/sqrt(k)->sqrt(2)c e,
    sqrt(k)(Tz_k-z_k)->(c/sqrt(2))e,
    sqrt(k)||Tz_k-z_k||->c/sqrt(2).

The affine shadow's cone distance times sqrt(k) tends to c/2. Every original equality residual has an explicit nonzero leading vector. The proof classifies all such affine subspaces by an orthogonal light-cone normal form and derives exact recurrences; it does not differentiate a state remainder.

This includes EVERY weakly infeasible real 2-by-2 SDP. In the orthogonal canonical form U={[[0,b],[b,t]]}, b!=0,

    Z_k/sqrt(k)->sqrt(2)|b|I,
    sqrt(k)(Z_(k+1)-Z_k)->|b|I/sqrt(2).

The Hermitian order-two case is also a Lorentz instance. The theorem does not include coupled products of several Lorentz cones just because each factor separately is covered.

## Reproducibility

Directory: last_iterate_boundary/.

    OPENBLAS_NUM_THREADS=1 python last_iterate_examples.py

Dependencies: Python 3, NumPy, SciPy, SymPy. Default run: 150,000 steps of the analytic counterexample, 40,000 steps for Lorentz dimensions 3, 5 and 12, exact symbolic identities, and 100 numerical firm-nonexpansiveness spot checks. The script writes full sampled LAST_ITERATE_RESULTS.json; RESULTS_SUMMARY.json records the completed run. Numerical observations support implementation checking, not universal proof.

Observed last counterexample state coefficient: 1.3797368487 versus 5^(1/5)=1.3797296615. Its scaled transverse step is still nonzero and rotates; the exact theorem, not finite numerics, proves the entire circle of cluster points. The Lorentz scaled residuals at 40,000 steps were approximately 0.705869, 0.353190 and 1.413555, against limits 1/sqrt(2), 1/(2sqrt(2)) and sqrt(2).

## Correct manuscript use

The counterexample gives a sharp separation between state and velocity asymptotics. The Lorentz theorem supplies a complete cone-specific positive result. Neither justifies advertising a universal higher-order SDP last-iterate law, a resolved named conjecture, or a guaranteed editorial outcome. Historical priority and external refereeing are not certified. The preceding cosmic/state theorems are not contradicted by the counterexample.
