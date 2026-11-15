# Reproducible strengthening audits

The complete universal proofs are in the parent directory, milestones 06–08; the audit interpretation and limits are in 09_STRENGTHENING_AUDIT_REPORT.md.

Run from this directory:

```sh
OPENBLAS_NUM_THREADS=1 python audit_strengthening.py
python audit_exact_dense.py
```

Python 3, NumPy and SymPy are required for the first suite. The second uses only standard-library Fraction arithmetic.

- strict_shield.py constructs the strict-trace, shielded inner normal form.
- dense_anchor.py constructs the final dense, anchored, nonreflection basis pair and explicit source extraction.
- audit_strengthening.py checks operator/data identities, all-PSD source residuals, rank formulas, zero data, dual certificates, Choi positivity, an entangled ancillary input, and all-depth model curves. It also contains exact rational/symbolic identities.
- audit_exact_dense.py independently verifies tightness, signed isotropy, nonzero overlaps, and a nonreflection invariant using entirely rational factored-column arithmetic.
- STRENGTHENING_RESULTS.json and EXACT_DENSE_RESULTS.json record the passing outputs. Running the scripts regenerates these files. The first stored JSON is compacted, without changing its values.

All four Python source blobs match the locally executed files, apart from removal of one final blank line in strict_shield.py. The corresponding standalone conversation audit ZIP has SHA-256 f01b845dd17c794f1f94db4c134b6e14b358d4ff7b345ea79b9c04071f5c78e8; it includes pretty-printed JSON and its own per-file hash manifest. This ZIP hash is not a hash of the Git tree.

Floating-point checks are diagnostics, not universal proofs. Roundoff-level negative eigenvalues are reported explicitly. The exact Fraction audit is one independently verified instance, not a replacement for the all-dimensional finite-grid argument. No external refereeing or priority certification is asserted.
