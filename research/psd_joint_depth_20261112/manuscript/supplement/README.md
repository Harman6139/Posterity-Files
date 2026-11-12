# Exact computational supplement

Python 3 standard library only; no floating-point exponent fitting or numerical PSD acceptance tests.

From the manuscript directory:

```sh
python3 supplement/one_switch_audit.py --output supplement/one_switch_results.json
python3 supplement/profile_audit.py --max-h 4 --output supplement/profile_results.json
python3 supplement/field_audit.py --output supplement/field_results.json
python3 supplement/independent_audit.py --output supplement/independent_audit.json
```

The first three are preserved predecessor programs, rerun during consolidation. The fourth was independently written for this audit. Recorded outputs are included. Counts describe labelled certificates, not numbers of mathematically distinct problems, except the explicit coarse-spectrum counts in the field audit.

The one-switch and profile audits supplement analytic proofs. The minimum separating nullity assertion through nullity five is a finite computer-assisted statement and is isolated in the paper's appendix; none of Theorems A–C depends on it. `finite_minimality_witnesses.md` preserves the four additional exact real witnesses needed for this finite claim. The separate product discussion is not part of the manuscript package. The unrestricted weighted cut-rank statement in the historical Milestone 139 must be read with the internal-grade restriction in the consolidated manuscript. The terminal counterexample is encoded in the independent audit.
