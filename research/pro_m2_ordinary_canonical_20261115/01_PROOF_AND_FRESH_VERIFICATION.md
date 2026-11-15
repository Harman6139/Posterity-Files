# Ordinary CP, canonical initialization, every descending adjacent rule

Date: 2026-11-15. This supersedes the provisional scope in checkpoint 000. A self-contained nine-page analytical proof has been written and compiled locally; complete source/code upload is the next packaging step. Historical first priority, independent human review, and a journal-percentile designation are not claimed.

## The theorem

For every n>=5 and m>=1 define r=n-1, d=n(n+1)/2, q=2n, Y=2q^r, U=2Yn^2(m+1), E=(d-1)!(2U^2)^(d-1), and N=20000n^3 E^2. Let F=I+(3/5)Adj(C5), the cycle being on (1,2,3,4,n), let D=diag(1,8/5,8/5,1,...,1), and C_ij=min(i,j)(n+1-max(i,j)). Put epsilon=1/(100n^3), B=DFD+epsilon C, S_N=diag(N,...,N,1), and A_N=S_N B S_N/(4nN^2).

Every target in the Frobenius ball of radius rho=1/(1600n^4N^2) about A_N is norm<=1, positive definite, strictly entrywise positive, and OUTSIDE THE ORDINARY CP_n cone. Every strictly descending extreme-ray adjacent rule, starting from the actual canonical T_n, must perform at least m pivots. This is a simultaneous all-choice statement, not a statement about one shadow rule or one prescribed path. In fact the exact n=5 canonical center has two improving rays, and the n=6 center has three.

No current-vertex separator or copositive improving-ray separator can terminate the prefix. No scalar identity correction R+tau I of ANY improving ray can separate, for any real tau. Arbitrary unrelated separators or nonlocal preprocessing/jumps are not ruled out; those are outside the local rule model.

An explicit common separator is W_N=S_N^-1 W_0 S_N^-1+I/(20nN^2), where W_0 is the inverse-D-congruence Horn form on the same cycle. It has cone margin 1/(20nN^2), norm<=6, target pairing<=-1/(6nN^2) throughout the ball, and yields distance>=1/(36nN^2). Center input length and separator height are O_n(log(m+1)). The lower bound is therefore 2^{Omega_n(H)} in the binary input-and-distance parameter.

## Why all rules are covered

Retaining the top-coordinate interval constraints of T_n gives a face with fixed leading T_(n-1) block. For ANY fixed SPD leading block H, the associated quadratic epigraph has a uniform positive gap above its continuous nonnegative quadratic minimum. Dirichlet approximation gives a fixed upper bound on the last coordinate of all active lattice vectors. Complementarity at a vertex bounds each residual gradient coordinate by 1/2.

Any bounded edge has a common active lattice constraint at its endpoints. Quadratic Cauchy-Schwarz then bounds the difference of their i-th cross-column coordinates by 1/2+2 sqrt(H_ii). For the canonical top block this is 5/2, in EVERY dimension. This does not assume that active last coordinates are one, nor does it use a small-dimensional covering-radius shortcut.

After at most m such moves, all active vectors have coordinates<=U. Cofactors bound every primitive integral extreme tangent ray by E. The fixed leading objective B_0 exposes the face; outside it the objective gap is at least 1/(500n^3). The N^2 leading contribution dominates every O(NE) negative contribution and perturbation. Thus ALL improving rays stay in the face. Its recession directions have nonnegative entries and cannot improve a positive objective. Nonmembership always supplies an improving extreme ray, and current-vertex pairings stay positive. Induction proves the prefix. No enumeration of the exponentially many paths is used in the proof.

## Fresh exact verification

A new generator and separately written verifier (no generator imports) ran successfully. The verifier uses Bareiss determinants and cofactor ray enumeration rather than the generator's RREF route. Passed checks:

- Six explicit parameter families, in dimensions 5,6,8,10, including m=2^64.
- All 36 canonical extreme rays for the tested orders 5 and 6, with the improving counts 2 and 3.
- A COMPLETE branching prefix through depth three in order five: 18 distinct vertices, 26 edges, and all improving relative rays at every nonterminal tested node.
- 7,869 exact finite lattice evaluations, together with a continuous quadratic-gap certificate excluding every omitted denominator/vector in those short-prefix vertex tests.
- 119 shared-active-constraint incidences and the 5/2 edge-movement bound.
- All explicit robust positivity, Horn separation, interval reserve, confinement, vertex-exit and scalar-correction inequalities for the six families.
- Seven deliberately corrupted data sets rejected (scale, target entry, separator, interval weight, canonical ray, edge length, and deletion of an improving branch).

Certificate SHA256: 048031057335bfb9fc7c86df3ecba5f3cc55fc32c484e6013d9f79efd577f95f.

The largest analytically certified prefix is 18446744073709551616 pivots. Its n=5 parameter N has 4823 bits. It is NOT a 64-bit input, and no long trajectory was simulated. Finite checks do not replace the universal proof.

## Current deliverable state

Local directory /mnt/data/m2_ordinary_canonical contains the complete manuscript, exact generator/verifier, and generated data/report. Packaging, full editable source upload, visual PDF checks, and remote/local hash verification are underway in the same session. Earlier project branches remain unchanged.
