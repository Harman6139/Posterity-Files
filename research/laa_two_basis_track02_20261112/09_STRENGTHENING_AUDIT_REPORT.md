# Strengthening audit: verified results and reproducibility

Date: 2026-11-12. Branch: laa-track02-gptpro-analytic-frontier-20261112.

## What has been proved

Milestones 06–08 extend the original quadratic positive-quotient theorem to one uniform construction with N=11m^2+8m+14+2p. It has all-nonzero basis overlaps with an explicit inverse-polynomial separation, a basis transition not signed-permutation-equivalent to any symmetric matrix, positive observations even at zero source, a completely positive linear encoder part with a fixed rank-one affine offset, a one-Kraus contraction decoder, exact whole-fibre surjectivity, and polynomial global all-PSD residual bounds.

The same construction identifies the full minimum lifted face, gives maximum lifted/preimage rank r+m^2+m+3 at any nonzero source point of rank r, preserves singularity degree by k -> max(1,k), and preserves both SDP dual optimal values and finite dual attainment. Its exact whole-ambient recovery law is Omega_b(t) asymp sqrt(t+mu_b(t)), where mu_b is the ORIGINAL source mass outside its minimum face; the zero-source law is Lipschitz. Complete positivity and source residual soundness persist at every ancillary matrix level with no ancillary-dimension factor, with observations explicitly interpreted as matrix-valued blocks.

These conclusions have algebraic proofs in the following immutable commits:

- 06_FACIAL_DUAL_AND_SHARP_AMBIENT_STRENGTHENING.md: f152760f6e4f2cd47a50384206bf0115ac34e6c0.
- 07_COMPLETE_POSITIVITY_AND_ANCILLA_UNIFORM_UNIVERSALITY.md: 2b0f214d0dba60b4540bc529d5d3a8970fe41700.
- 08_DENSE_NONREFLECTION_FULL_STRENGTH_THEOREM.md: c69aefea9cd2b74dfff238287dd65e987356ad32.

## Adversarial distinctions

1. The encoder is AFFINE in the fully positive-data version: E(X)=E_lin(X)+Y_0, where E_lin is completely positive and Y_0 is fixed rank-one PSD. It is not mislabeled as a linear map.
2. The entire lifted fibre is generally larger than E(F_b). Thus the construction does not contradict the historical exact-bijection lower bounds.
3. Neither map is asserted trace preserving on its full ambient cone. Complete positivity does not imply that normalization.
4. Exact facial-depth preservation does not imply equal optimal recovery exponents. The explicit rational depth-k family in 06 has source exponent 2^{-(k-1)} and lifted exponent 2^{-k}. This is why the source-leakage law, not an unjustified omega_source+sqrt(t) identity, is used.
5. The all-PSD source residual constant is polynomial without source Slater or rank gaps. Whole-ambient distance constants additionally use the actual relative-interior eigenvalue and the restricted measurement singular value on the minimum face. Those margins are displayed, not presumed uniform.
6. At ancillary level n>1, the observations are two lists of n-by-n blocks. No claim is made that these are only two scalar rank-one ONB diagonal lists on the entire Nn-space. No ancillary-level facial-depth formula is silently inferred.
7. Exact construction is polynomial-bit given a rational positive trace certificate; without one, the explicitly conditioned certificate-search result of 03 applies. This is not an unconditional polynomial-time exact SDP solver.

## Reproducible diagnostics

The accompanying audit archive contains:

- strict_shield.py: strict-trace, shielded inner construction.
- dense_anchor.py: final anchored/nonreflection compiler and explicit source extraction.
- audit_strengthening.py: numerical construction, operator identities, global soundness, both dual directions, Choi positivity, entangled ancillary input and all-depth curves, plus exact symbolic checks.
- audit_exact_dense.py: independent Python Fraction verification of tightness, signed isotropy, all-nonzero overlaps and a nonreflection certificate.
- STRENGTHENING_RESULTS.json and EXACT_DENSE_RESULTS.json: observed outputs.
- README.md and SHA256.json: instructions and per-file hashes.

Run:

    OPENBLAS_NUM_THREADS=1 python audit_strengthening.py
    python audit_exact_dense.py

NumPy and SymPy are required for the first suite. The exact dense suite uses only Python's standard library.

Nine construction cases passed, including m=1,2,3, zero/rank-one/full-rank source points and the depth-two model. The largest forward-data error was 7.759285399353114e-12; the largest source-extraction operator error was 8.289582647566703e-16. The smallest observed basis overlap was 1.6536266588615584e-13; the smallest target observation, including zero data, was 8.268133652481166e-14.

Choi identities and positivity were checked at m=1,2,3,4. An entangled m=2, ancillary-order-3, source-rank-4 input passed the amplified tests: section error 7.576204545718236e-15 and forward-data error 1.6733824061449998e-12. The minimum inner eigenvalue -2.7194151499186866e-15 is numerical roundoff, reported explicitly. No analytic positivity conclusion is inferred from this floating-point value. The observed reverse-residual ratio was 0.0319482592811413, below the same proved scalar bound 14452659.270689338.

Nine source-leakage curves at depths one, two and three were checked against the exact predicted residual relation. The all-depth proof itself is analytic for every k. An exact SymPy sum-of-squares identity was checked for rational H=[[2,1],[1,3]], and the rational all-depth source family was symbolically checked for k=1,...,6.

The independent Fraction audit at m=p=1 (N=35) passed every exact test. The nonreflection power-sum discrepancy has nonzero positive numerator of 477 bits and denominator of 493 bits. Its certificate SHA-256 is 5523bb7d0aedd59796de17727ed312da46fb6c2908fe44fe65b6ded9ce8c01ce. The exact guaranteed overlap/anchor margin for that diagnostic instance is 1/76749924836206182400000. The all-dimensional nonreflection theorem is proved separately by the finite-grid polynomial argument in 08.

Audit archive SHA-256: f01b845dd17c794f1f94db4c134b6e14b358d4ff7b345ea79b9c04071f5c78e8.

## Scope of verification

The tests are diagnostics and exact finite-instance checks, not substitutes for the universal proofs. An initial test-run failure was a Python Boolean/SymPy coercion issue; replacing the Boolean coefficient by int(i==j) resolved it before the passing outputs were generated. No mathematical assertion was inferred from that failed run. The inherited historical audit scripts were not all rerun in this continuation.

The result has not been independently referee-certified, and no comprehensive literature-priority audit has been completed. Classical Choi/Kraus and facial-reduction background is attributed in 06–07. The new statements are supported by their explicit proofs, not by a claim of external certification.
