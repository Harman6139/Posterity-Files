# Manuscript III — randomized and parallel strengthening completed

Date: 2026-11-14.
Branch: `laa-track02-gptpro-analytic-frontier-20261112`.
Primary proof commit: `8af05d2ace504a76d9f890deb96edc500a60ff14`.

## New complete mathematical result

For the same normalized escape-profile classes used in milestone 27, with rho_f(s) between fixed multiples of s^(-beta), the optimal expected error after T unrestricted randomized exact value/gradient queries is

    Theta_beta(T^(-2/(2beta+1))).

The corresponding expected-error and fixed-confidence query complexity is Theta_beta(epsilon^(-beta-1/2)). The proof gives a fixed distribution chosen before every algorithm seed, high-probability failure bounds, and an expected stopping-time corollary. All constants and the profile onset are independent of horizon and dimension.

A parallel version holds with T rounds and B simultaneous queries per round, at sufficient dimension O(T^3 log(BT/zeta)). No fixed-dimension no-parallel-speedup statement is made. For rational beta all hard functions are semialgebraic; they are globally convex C2 on the full space with globally Lipschitz gradients and finite unattained infimum zero.

## What closes the earlier gap

The deterministic resisting rotation in 27 could not establish a randomized lower bound. The new proof samples one Haar orthonormal frame in advance. A known sparse 3/2-power regularizer gives C2 smoothness and EXACT inactive-coordinate locality. A C2 radial exterior term makes arbitrarily large queries independent of the hidden frame. At most one additional frame vector is needed to simulate a whole batch on the high-probability coupling event. One unexposed output direction remains and forces the objective gap.

A scalar nonattained tail plus a small-gap finite core realizes the SAME radius profile uniformly at every scale. The lower-bound instance is not reselected after the seed, and no finite-precision argument hides a small nonzero gradient component.

## Recommended manuscript focus

Working title: **Randomized and Parallel Complexity of Convex Optimization Without Minimizers**.

Use 26 for fixed-instance radius/progress laws and the comparator idea; use 38 as the central matching randomized minimax theorem. The upper proof is reproduced in 38. Keep cosmic directions, copositive separation, smooth-body extension complexity, and two-basis compilation in their separate manuscripts rather than append them here.

The headline is an optimal normalized oracle-complexity law, not a new lower bound for ordinary attained smooth-convex optimization, which has classical antecedents. The 3/2-power sparse smoothing is also established. Novelty of the complete nonattainment/parallel synthesis and external correctness review remain publication questions, not consequences of a successful numerical run.

Not proved: a lower bound for explicitly supplied SDP data, a cone-projection oracle, stochastic/noisy gradients, a single fixed-dimensional function hard at all horizons, or polynomial-bit descriptions of the Haar-rotated instances. No named-conjecture or editorial-acceptance claim is made.

The proof and all diagnostic code/results are committed. Their local delivery package contains the same files and a checksum manifest.
