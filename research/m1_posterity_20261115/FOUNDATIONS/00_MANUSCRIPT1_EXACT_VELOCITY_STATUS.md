# Manuscript I — exact velocities and finite angular motion

Date: 2026-11-14.
Proof commit: `a1b1ad2d49fa643e53d78490b3d9266ee85a1954`.
Code commit: `9e3dbf100cba5ab7ad03e53e525d2958a9439b08`.
Full recorded results commit: `2917f5f0dada05390798667642f2c9623e51a664`.

## Complete new theorem

Read `40_EXACT_VELOCITIES_AND_FINITE_ANGULAR_MOTION.md`.

For every finite-dimensional proper closed convex semialgebraic objective F with finite unattained infimum F_*, the quadratic regularization path determines p in Q intersect (0,1/2) and V!=0. For ANY convex splitting F=g+h with globally L-smooth g and proper closed convex h, neither of which must be definable, fixed-step forward–backward iteration with 0<eta<2/L satisfies at physical time tau=eta*k:

    x_k=V tau^p+o(tau^p),
    tau^(1-p)(x_(k+1)-x_k)/eta -> p V,
    F(x_k)-F_* ~ [p^2||V||^2/(1-2p)] tau^(2p-1),
    [F(x_k)-F(x_(k+1))]/eta ~ p^2||V||^2 tau^(2p-2).

The SAME constants hold for every start and admissible splitting/step at equal physical time. A positive-power velocity remainder implies that the radially normalized STATE trajectory has finite total angular motion, with an O(K^-zeta) tail bound for some zeta>0. The iterate radius is asymptotically minimal among all points attaining its objective gap, and accumulated travel divided by net displacement tends to one.

All-order conic consequence: exact last velocity and exact feasibility-distance constants for alternating projections on every pair of closed convex semialgebraic sets disjoint at distance zero, including EVERY matrix order of weakly infeasible SDP. The canonical whitened equation residual has the same exact leading feasibility constant. Unwhitened residual vectors are not assigned an unproved directional limit.

## Mechanism and independent dependencies

The proof tracks a semialgebraic regularization path even when the split map itself is nondefinable. Cocoercivity and monotonicity control the split gradient along that path. A convex energy-tail identity identifies the actual speed via monotone secants, avoiding the invalid differentiation of a state remainder. Convexity across widely separated iterates fixes its direction. Quantitative Puiseux remainders then imply finite spherical length.

The proof is self-contained apart from classical proximal existence, gradient cocoercivity and one-variable semialgebraic asymptotics. Earlier project results on cosmic dynamics, dimension-dependent escape, and SDP universality are not required premises.

## Exact exclusions

The requested arbitrary-order PLAIN DOUGLAS–RACHFORD last-step statement remains unproved. The positive arbitrary-order result here is for ALTERNATING PROJECTIONS and convex forward–backward methods. Generic firm nonexpansiveness is insufficient, as the independent counterexample in 35 shows.

Other restrictions: finite dimension, exact updates, finite unattained objective infimum, a semialgebraic total objective, and strict eta<2/L when L>0. The endpoint has a simple oscillatory counterexample. Variable-step extensions are proved only for pure proximal point and pure gradient descent, not arbitrary composite variable steps. The finite spherical-length claim concerns states, not total variation of normalized velocities. No universal remainder exponent, uniform onset, finite-precision stopping certificate, changed-metric direction invariance, or randomized/inertial theorem is asserted.

## Current prior-work boundary

The primary preprint of Do–Jentzen–Kuckuck, arXiv:2610.29211v2 (revised 9 November 2026), reports finite spherical length for continuous gradient trajectories of arbitrary definable C1 potentials. This must be acknowledged: milestone 40 does NOT claim a new resolution of that continuous-flow conjecture. The distinction is convex nonsmooth DISCRETE splitting, exact velocity/energy constants, and potentially nondefinable pieces. Ji–Dudik–Schapire–Telgarsky's COLT2020 regularization-path result and classical Baillon–Haddad/forward–backward facts are also attributed. Historical priority and external refereeing of the full theorem have not been certified.

Suggested manuscript focus: **Finite Angular Motion and Exact Velocities of Convex Splittings at Infinity**. The theorem materially strengthens Manuscript I but does not establish an editorial outcome.

## Reproduction

Directory: `exact_velocities/`.

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python test_exact_velocities.py --steps 80000

Dependencies: Python 3, NumPy, SciPy, SymPy. No network. Five exact symbolic constant checks passed. The completed run records twelve scalar split/step cases, two coupled nonsmooth splits, a nondefinable trigonometric split, a two-tail angular example, order-two and order-three PSD alternating projections, and the excluded endpoint step.

Scalar scaled velocity ratios range from 0.99999793879076 to 1.0001726524047796. The last-half step-energy/objective-drop ratios in order-two and order-three AP are 1.000006918008531 and 1.0000057001874854. State and direction transients remain visible, particularly at order three. These numerical checks do NOT prove the universal asymptotic theorems. The recorded JSON preserves the full results rather than only favorable scalar cases.

The delivery ZIP includes an expanded prose proof, reproduction instructions and SHA-256 manifest. Its expanded proof and the compact repository manuscript are mathematically equivalent editorial versions, not byte-identical files. No new theorem is held only in the ZIP.
