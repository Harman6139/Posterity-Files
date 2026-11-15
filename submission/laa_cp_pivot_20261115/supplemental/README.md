# Exact completely positive separation verification

This is the content of the companion `CP_Pivot_Verification.zip` archive.
Python 3.9+ and its standard library are sufficient.

```sh
python code/generate_certificates.py
python code/verify_certificates.py
```

Do not use Python's `-O` option: the generator uses assertions. The independent
verifier does not import the generator and uses determinant/cofactor checks.

The generator writes `certificates/exact_certificates.json`. Its platform-independent
UTF-8/LF SHA-256 is
`048031057335bfb9fc7c86df3ecba5f3cc55fc32c484e6013d9f79efd577f95f`.
The verifier writes `certificates/verification_report.json`.

The six tested parameter families use orders 5, 6, 8, and 10. The finite geometric
checks cover all 36 canonical rays in two orders and a complete improving-branch
prefix of depth three in an order-five example: 18 vertices, 26 edges, 7,869 finite
lattice evaluations, and 119 shared-active incidences. Seven deliberately corrupted
data sets are rejected.

The largest family guarantees at least 2^64 pivots by the article's analytical
proof; it does not simulate that path. The associated order-five scale N has
4,823 bits. These finite checks are reproducibility evidence, not the universal
proof, a verification of every positive definite block, or formal certification.

Original mathematics and scripts: Posterity-Files commit
`11ffd7fe0e83b7eda47459d1d9b90b7358a4fcfc`, directory
`research/pro_m2_ordinary_canonical_20261115/release`.
The delivered scripts change only output serialization to UTF-8/LF bytes so that
Windows reproduces the original data hash.
