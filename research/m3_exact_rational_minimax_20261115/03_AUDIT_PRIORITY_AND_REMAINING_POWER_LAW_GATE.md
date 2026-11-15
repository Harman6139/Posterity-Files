# Checkpoint 03 — proof audit, priority, and the remaining power-law gate

Date: 2026-11-15. This continuation preserves the full history through f843934bd5c83280b732bface3967737207e93da and the original conic-oracle checkpoints. The new results branch is research/pro-m3-exact-rational-minimax-20261115.

## 1. The actual proved advance

Checkpoints 01 and 02 give a new explicit optimization-hard family in the ORIGINAL rational, free-radius, exact natural value-and-gradient model. The information-bearing blocks are scalar PSD inequalities; a fixed 2-by-2 PSD block supplies genuine weak infeasibility. This is not being claimed as a lower bound driven by noncommuting spectral eigenvectors.

For the depth-n family, at every 0<epsilon<=(5/384)4096^(-n), the exact minimax success probability after T calls and an arbitrary unqueried output is

    S(n,T)=2^(-n) sum_(j=0)^min(n,T) binom(n,j).

The same value is optimal under the uniform prior sampled before the algorithm's random seed. Exact expected objective infima are also computed. There is a matching Theta(log(1/epsilon)) fixed-confidence theorem for ALL normalized rational conic objectives with TWO affine coordinates and arbitrary PSD order. Two coordinates does not mean 2-by-2 matrices.

Consequently a universal accuracy-independent constant-query optimizer over the whole rational class with unbounded PSD order is impossible. A universal logarithmic bound independent of the number of affine coordinates is NOT proved, and the original polynomial minimax lower bound is NOT proved.

## 2. Model audit

- Natural squared PSD distance: every scalar squared hinge is produced by actual rational diagonal matrix entries, not an unspecified SDP epigraph. Appending W(z) preserves the exact objective identity.
- Rational chart: the coefficient matrices themselves are rational; no hidden real rotation or chart is used.
- Isometry: the x direction's squared norm is the total atom mass one; the z direction is unit and has disjoint support.
- Uniform origin: <X0,Hx>=<X0,Hz>=0 and ||X0||_F^2=125/48. The growing matrix order does not hide growing offsets.
- Genuine weak infeasibility: det W(z)=-1 for every finite z. All scalar inequalities are satisfied at the true core center, and the tail approaches the PSD cone.
- Common profile: (1/2)s^(-1/2)<=rho_f(s)<=s^(-1/2) for EVERY 0<s<=1/8, independently of depth, word, order and encoding height.
- Polynomial encoding: order 24(n+1)+2, O(n) nonzero entries with O(n) bits each, total explicit encoding O(n^2).
- Free-radius queries: exact moment identities make all exterior value/gradient replies agree. The stronger word oracle simulates each query at any finite real point, including arbitrarily large or algebraically complicated points.
- Arbitrary output: success requires membership in a unique leaf interval, so the output itself determines the hidden word; it need not have been queried.
- Randomized quantifiers: one fixed uniform word is sampled first. Conditioning on an algorithm seed does not change the distribution, and the lower bound holds for each deterministic strategy.
- Matching actual conic queries: first-mismatch probes use x=c_guess+(h^n/16)sqrt(2). Distinct mismatch positions have distinct rational gradient slopes at this irrational point. The decoder compares finitely many exact candidate answers.
- Expected risk: statements are infima, not attained objectives, because the known tail is positive at every finite output.
- Universal two-coordinate upper bound: central-cut ellipses retain a comparison disk in a small sublevel. The proof does not assume an attained minimizer or impose a restriction on the queries allowed to competitors.

## 3. Exact verification

The standard-library script verify_minimax.py completed 9,964 checks at --max-depth 6. It uses fractions and an explicit implementation of Q(sqrt(2)); no floating-point tolerance is used. Tests include moments, positive weights, true scalar PSD distances, rational square factors, coordinate isometry, bounded origin norm, leaf barriers, exact exterior identities at queries as large as 2^1000, prefix locality, all guessed-word probes through depth five, and the binomial/expected-risk recurrences.

The script and VERIFICATION_RESULTS.json are committed. These are finite exact diagnostics supporting the analytical induction and transcript proofs. They are NOT independent external mathematical refereeing. No assertion that finite testing proves the theorem is made.

## 4. Serious prior-art qualification

The first-mismatch / correct-prefix information process is the classical FIXED-COORDINATE-ORDER LeadingOnes black-box problem, not a new search mechanism.

Stefan Droste, Thomas Jansen, Ingo Wegener, 'Upper and Lower Bounds for Randomized Search Heuristics in Black-Box Optimization', Theory of Computing Systems 39(4), 525-544 (2006), DOI 10.1007/s00224-004-1177-z.

Primary publisher record: https://link.springer.com/article/10.1007/s00224-004-1177-z
Accessible original preprint: ECCC TR03-048, posted 24 June 2003, https://eccc.weizmann.ac.il/report/2003/048/download

Theorem 6 and its complete proof on printed page 17 were read, including a rendered screenshot. It gives expected complexity n/2+/-o(n), explicitly using the uniform hidden-word prior, uniform conditional suffix, and geometric revelation process. Our exact fixed-budget binomial formula permits an unqueried final output, unlike their first-queried-optimum convention; it is proved here but is not represented as a new underlying combinatorial idea.

The actual additional claims are the positive rational moment-matching realization, global natural-conic transcript simulation both ways, polynomial rational isometric pencils with common escape constants, and the resulting conic minimax law. The central-cut ellipsoid upper argument is likewise classical, not an algorithm invention.

The 2026 real matrix-vector work is a separate antecedent, not a rational endpoint proof: M. Derezinski, E. N. Epperly, R. A. Meyer, 'The matrix-vector complexity of Ax=b', arXiv:2602.04842v4, July 2026, https://arxiv.org/html/2602.04842v4 . Its real-matrix information model and the already-known arbitrary-query/Krylov methodology must not be conflated with the moment-matched rational family.

A targeted search and these proof-level comparisons do not certify historical priority of the entire new conic formulation. The preregistered SIOPT/MOR published-paper benchmark from the earlier branch has not been completed. No upper-quintile rating, publication-readiness claim, or acceptance probability is earned here.

## 5. Exactly what the original target still needs

At beta=1/2 the requested original objective threshold is c/(T+1), equivalent to Omega(1/epsilon) queries in the dimension-uniform minimax problem. Our explicit high-probability horizon construction instead uses

    epsilon_T=(5/384)4096^(-4(T+1)).

That exponential-versus-polynomial distinction is essential. The present family therefore cannot be relabeled as the requested hard prior. Its exact optimal success law also shows that no stronger polynomial-depth interpretation is hidden in its analysis.

For the normalized rational class with varying affine-coordinate dimension, the proved query-complexity bracket is now

    c log(1/epsilon) <= N(epsilon) <= C/epsilon

at beta=1/2, using the present lower bound and the earlier accelerated conic upper bound. For the fixed-two-coordinate class, both sides are Theta(log(1/epsilon)). Constants for the higher-dimensional ellipsoid upper bound depend on that coordinate dimension and cannot be dropped.

A positive full resolution requires a rational information-hiding construction whose optimization barrier remains polynomial rather than exponentially small in the number of sequential revelations, with the same normalization, free query radii and arbitrary outputs. A negative resolution requires a stronger universal optimizer over growing-coordinate-dimension rational PSD pencils. Neither has been supplied. The earlier real-coefficient, positive-error rational, and charged-radius frontiers remain separate results and do not fill this gap.
