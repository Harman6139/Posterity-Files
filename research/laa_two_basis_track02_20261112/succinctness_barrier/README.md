# Robust membership hardness and the succinctness barrier

Parent theorem: `../25_ROBUST_MEMBERSHIP_HARDNESS_AND_SUCCINCTNESS_BARRIER.md`.
Proof commit: `5be4e709f849a6c91d377435ca61b69e58a9330d`.

## Proven conclusions

For the Boolean-moment body from manuscript 24, polynomial-bit rational graph queries distinguish P_n(x)<=1/2 from P_n(x)>=2 and have an inverse-polynomial interior/exterior geometric margin. Simple Max Cut reduces to this promised membership problem. The same queries remain valid for EVERY convex body within Hausdorff distance 1/(32 n^3), not merely the original defining polynomial.

A uniformly polynomial-time evaluable nearby family would therefore imply P=NP. Uniform polynomial-size rational division-free circuits, with polynomial final degree/coefficient heights, are covered by the proved modular-evaluation lemma. Nonuniform short descriptions imply NP subset P/poly instead. These are conditional conclusions, not proofs separating those complexity classes.

One exact integer homogeneous-moment evaluation recovers the full cut-size histogram. Together with the classical hardness of T_G(3,2), this proves #P-completeness of integer moment evaluation under polynomial-time oracle reductions. The original polynomial has at least binom(p+D-1,D-1) nonzero monomials, independently of complexity assumptions.

## What remains unproved

The proposed full target is a uniformly constructible polynomial-total-description family with dimension-independent near-sphericity/positive-curvature bounds and superpolynomial SDP approximation order at one fixed positive accuracy. Manuscript 25 does not establish that target, and does not rule it out for other families. The obstruction applies to compression or sufficiently close replacement of the particular moment body. It must not be cited as a general impossibility theorem for smooth-body SDP hardness.

## Reproduce the finite exact checks

Python 3.10 or later; no third-party libraries or network required:

```sh
python succinctness_barrier.py
```

`EXACT_RESULTS.json` records the output: 74 simple graphs, 121 nontrivial threshold queries, 74 recovered cut histograms, and one modular-cancellation demonstration with 200 repeated squarings. The query tests use the analytically sufficient smaller half-degree 4*n^2*(n+1), not the unnecessarily huge production degree. The radix identity is checked at smaller admissible even exponents because its proof applies to every even exponent at least the edge count. The modular example computes 49/25 without expanding intermediate denominators of exponential bit length.

These exact finite examples illustrate the displayed algebra. They are not premises of the all-dimensional proof and do not provide evidence for the separate, still-unproved full target.
