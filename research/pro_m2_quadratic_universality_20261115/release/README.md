# Manuscript II — single-quadratic arithmetic classification

Research date: 15 November 2026.

This is a new, standalone 18-page mathematical continuation of the earlier
polyhedral arithmetic-carrier and all-descending-rule work. The corrected
scope is one rational quadratic column inequality, all rational affine
measurements, and an explicit universality obstruction for products of
second-order cones. It is not a claim to solve every rational matrix-cone
factorization problem.

## Main deliverables

`manuscript/MASTER_THEOREM.tex` is the entry point; all seven included section
files are supplied. The PDF and `COMPLETE_PROOFS.md` are derived outputs.
`STATUS_PROVED_NOT_PROVED.md` states the exact theorem scope and limitations.
`NOVELTY_AND_PRIORITY_AUDIT.md` distinguishes the contributions from primary
antecedents. Source and program hashes are in `SOURCE_MANIFEST.json`.

## Rebuild and verify

Python 3 with the standard library is sufficient for all certificate checks:

```sh
python code/build_release.py
```

To additionally build the PDF and the full Markdown proof companion:

```sh
python code/build_release.py --pdf --markdown
```

The latter command requires `pdflatex` and `pandoc`. The exact verifier imports
no generator code. It tests the saved instances and rejects seven deliberate
corruptions; it is not a production implementation of the general algorithms
or a substitute for their analytical proofs.

Expected certificate SHA256:
`2f432846643e31e100935ba1a4f3c58adb19bbce89bee89f2e652efc055969f7`.

## Preservation

Repository: `Harman6139/Posterity-Files`.
New branch: `research/pro-m2-quadratic-universality-20261115`.
New directory: `research/pro_m2_quadratic_universality_20261115`.
Parent: `ea809bed847d103a4c586428972d0aeda1b4d9d1`.
The new manuscript and programs are under `release/` in that directory.
Earlier checkpoints and source branches are unchanged.

## Evidence limits

The manuscript has complete internal mathematical proofs and supplementary
exact arithmetic checks. No independent human review, proof-assistant
validation, first-priority certification, completed LAA percentile benchmark,
or editorial acceptance probability is claimed. The general rational-point
and isotropy algorithms are specified and charged mathematical primitives,
not represented as having been implemented by the example scripts.
