# Final theorem status — ordinary CP, canonical start, every descending adjacent rule

Date: 15 November 2026.
Results branch: research/pro-m2-ordinary-cp-canonical-all-rules-20261115.
Parent snapshot: f79e4d104575603a459718944dc748f4ba261161.
Repository directory: research/pro_m2_ordinary_canonical_20261115/release.

## Proved in the complete analytical manuscript

For each fixed n>=5 and every integer m>=1, the explicit rational center A_N is positive definite, strictly entrywise positive, norm at most one, and outside the ORDINARY completely positive cone CP_n. From the ACTUAL canonical tridiagonal vertex T_n, EVERY strictly objective-descending extreme-ray adjacent rule must make at least m pivots. This is simultaneous over all possible improving choices, including adaptive and randomized choices, and does not require uniqueness of the path. Center binary input-and-distance precision is Theta_n(log(m+1)); hence the lower bound is exponential in that parameter.

The statement holds throughout the explicit Frobenius ball of radius 1/(1600 n^4 N^2). One explicit rational separator works on the whole ball, has positive cone margin 1/(20 n N^2), norm at most 6, pairing at most -1/(6 n N^2), and yields distance at least 1/(36 n N^2). No scalar identity correction of ANY improving ray can separate during the forced prefix.

The new geometric mechanism is proved for every positive-definite leading block H: each bounded edge in its quadratic Ryshkov epigraph changes cross-column coordinate i by at most 1/2+2sqrt(H_ii). For H=T_(n-1), this is 5/2 in every dimension. Dirichlet approximation provides a uniform transverse gap and an active-denominator bound; vertex stationarity supplies residual-gradient bounds. An arithmetic exposure gap and cofactor height estimates then exclude all improving rays that could leave the fixed-block face. Nonmembership supplies an improving extreme ray at every stage, completing the all-choice induction.

The proof is self-contained for the construction and bounds. The classical perfect-form framework, Dirichlet approximation, Horn copositivity, determinant bounds, and positive diagonal congruence are acknowledged antecedents. No transfer from a constrained column cone or noncanonical shear initialization is used.

## Exact scope, not claimed

The lower bound is for the stated local adjacent-pivot model with current-vertex, selected-ray, and scalar-identity-corrected-ray separator exits. It is NOT a lower bound against arbitrary algorithms, unrelated separator searches, nonlocal preprocessing or jumps, non-descending moves, or input-dependent initialization. The explicit short global separator is a bypass, not a contradiction.

The robust ball preserves the m-pivot guarantee. Arbitrary rational perturbations in it can have longer encodings than the compact rational centers. No optimal numerical exponent or optimal dimension dependence is claimed. Eventual termination of every possible local rule is not asserted. The lower bound is compatible with the original suitable-pivot finite-termination conjecture.

## Reproducibility and preservation

The complete nine-page LaTeX manuscript and both complete standard-library Python programs are committed. Authenticated Git tree reads verified all three source Git hashes against local bytes. The verifier imports no generator code, uses Bareiss determinants and cofactors, and separately checks target arithmetic, interval reserves, full canonical tangent-ray sets, and every improving branch of a short prefix.

Fresh results: six parameter families, 36 canonical extreme rays (improving counts two and three in orders five and six), 18 short-prefix vertices, 26 edges, 7,869 exact finite lattice evaluations with analytical exclusion of omitted vectors/denominators, 119 common-active incidences, and seven deliberately corrupted data sets rejected. The largest analytical prefix is m=2^64; its n=5 parameter N has 4823 bits. No exponential trajectory is simulated.

Certificate SHA256: 048031057335bfb9fc7c86df3ecba5f3cc55fc32c484e6013d9f79efd577f95f.

A clean rebuild from the three source files reproduced exact certificate JSON, verification report, and complete Markdown proofs byte for byte. The PDF compiled twice without overfull or undefined-reference warnings; all nine pages were rendered and visually inspected. The conversation ZIP includes the compiled PDF and generated JSON/Markdown. These derived files are not all separately asserted to be GitHub binary uploads; they are reproducible from the committed source.

## Validation and publication limits

The universal theorem rests on the analytical proof, not on finite tests. No independent human review, proof-assistant verification, exhaustive historical first-priority certificate, journal-percentile designation, or editorial acceptance probability is claimed. The older article-level journal benchmark remains a separate unfinished task; no missing mathematical lemma in this theorem is being hidden as a publication task.
