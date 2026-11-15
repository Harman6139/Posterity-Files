# Early quadratic-frontier audit: reproduction instructions

The exact normal form and its later strengthened version are in this directory, files 02–09. The early numerical diagnostics are separate from the proofs.

Bundled early audit originally produced at snapshot 005b1267599a2c18abe37879b4959061bf47729a; the source scripts `audit_quadratic_quotient.py`, `audit_adversarial.py`, and `audit_historical_corrections.py` are committed here. Run from this directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python audit_quadratic_quotient.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python audit_adversarial.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python audit_historical_corrections.py
```

Requires Python 3, NumPy, SymPy. The scripts use no network or optimization solver. Recordings: `AUDIT_RESULTS.json`, `ADVERSARIAL_RESULTS.json`, `HISTORICAL_CORRECTION_RESULTS.json`. Compare hashes with `EARLY_AUDIT_SHA256.json`. Slight floating-point differences between systems are expected; numerical rank and eigenvalue checks are not mathematical proofs. Exact symbolic/rational checks are identified in the results.

The later independent strengthening suite resides under `strengthening_audit/`. Its original ZIP is a packaging of text files in this repository and is not a separate proof.
