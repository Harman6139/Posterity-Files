# Copositive quantitative pivots — Track II results

**Date:** 14 November 2026. **Status:** mathematical obstruction and replacement bounds proved in the accompanying manuscript; historical priority and the requested upper-quintile publication benchmark are **not certified**.

## Main outcome

The proposed polynomial-in-binary-precision bound for the specified adjacent shadow-pivot rule is false. An explicit input of length O(log N) forces N pivots; the target-aware grid modification still requires at least N−1. The example is indefinite, so a PSD pretest defeats it. It is not a lower bound for all separation algorithms.

The all-order positive results are a sharp effective Ryshkov interior/height theorem (also for finitely generated rational cones), explicit singly exponential adjacent-path complexity and polynomial object heights, and a fully specified rational nonlocal separation algorithm with fixed-dimensional polynomial precision complexity. The support-oracle and ellipsoid architecture are classical and are credited as such.

**Manuscript:** `manuscript.tex` (13-page compiled PDF supplied with the downloadable research bundle). The proof of every asserted new theorem is included; the standalone old milestone 34 is not required. This is a complete research manuscript, not a claim of cleared publication priority or submission readiness.

## Reproduce

Use Python 3.10 or later; no third-party packages are required. From this directory:

```sh
python test_exact.py
python run_five_cycle.py
python verify_certificates.py
pdflatex -halt-on-error manuscript.tex
pdflatex -halt-on-error manuscript.tex
```

The first command runs eight exact test groups. The second regenerates a strict separator for a positive-definite, doubly nonnegative five-dimensional nonmember. The third verifies the full certificate with a separately implemented determinant routine and rejects four deliberate corruptions. Do not run assertion-based tests with `-O` or `-OO`.

Resource caps in the algorithms raise `ResourceLimit`; they never turn exhausted searches into mathematical conclusions. Setting `max_pivots=None`, `max_vectors=None`, and `max_ray_subsets=None` removes the adjacent routine's caps. Setting `max_iterations=None` removes the nonlocal cap. The nonlocal routine is a promised-nonmember procedure, not a terminating CP-membership test. It requires Frobenius norm at most one; rescale rationally when needed.

The large-N test checks exact formulas at N=2^100. It does not claim to have simulated 2^100 pivots. Wall-clock times are metadata and vary across runs; all mathematical comparisons use integer or rational arithmetic.

## Files

The GitHub branch stores the manuscript source, executable programs, audit, and compact run record. The compiled PDF and full generated JSON outputs are in the downloadable research bundle; the commands above regenerate them from the committed sources.

- `manuscript.tex`, `manuscript.pdf`: complete proofs, algorithms, resource accounting, and limitations.
- `exact_algorithms.py`: exact support oracle, Ryshkov primitives, shadow procedure, rational nonlocal separator.
- `test_exact.py`, `verification_results.json`: executable eight-group tests and actual run results.
- `run_five_cycle.py`, `five_cycle_nonlocal_certificate.json`: deterministic rational certificate generator and its full output.
- `verify_certificates.py`, `independent_checker_results.json`: checker importing no producer modules, with corruption tests.
- `AUDIT_AND_BENCHMARK.md`: prior-work distinctions, fixed journal samples, access/review status, and unfulfilled requirements.
- `STATUS.md`: compact PROVED / NOT ESTABLISHED checklist.

## Repository provenance

Repository: `Harman6139/Posterity-Files`.
Source baseline: `22ed4becd320695b41f8a11f1223ea090ef89ecf`.
Results branch: `research/pro-m2-copositive-quantitative-20261114`.
Results directory: `research/pro_m2_quantitative_20261114/`.
The branch preserves source milestones. The initial proof milestone and preregistered benchmark protocol are also retained there.

No independent human peer review, proof-assistant verification, acceptance probability, eight-month editorial guarantee, or achieved 80th-percentile rating is asserted.
