# Reusable hardness amplification and lattice-epigraph geometry

Revised research manuscript: **Long pivot paths and short certificates for completely positive matrices — Fixed-block amplification and lattice epigraph geometry**.

Base repository: `Harman6139/Posterity-Files`.
Immutable baseline: `11ffd7fe0e83b7eda47459d1d9b90b7358a4fcfc`.
Intended new branch: `research/pro-m2-reusable-hardness-20261115`.
New repository directory: `research/pro_m2_reusable_hardness_20261115/release/`.

## Main files

- `manuscript/MAIN.tex`: integrated editable manuscript, with four included sections.
- `manuscript/MAIN.pdf`: regenerated research manuscript.
- `manuscript/MAIN_standalone.tex`: generated single-file source.
- `COMPLETE_PROOFS.md`: generated full proof companion.
- `code/generate_certificates.py`, `code/verify_certificates.py`: separate exact code paths.
- `certificates/`: reproducible instances, independent checks, rebuild records.
- `audit/NOVELTY_AND_PRIORITY.md`: closest-source distinctions, including the 2018 SPN corrigendum and 1998 bordered-matrix threshold antecedent.
- `audit/PL_UPDATE.md`: substantive changes, scope, and benchmark limitations.
- `STATUS_PROVED_NOT_PROVED.md`: exact theorem and delivery status.
- `original_baseline/`: original proof and verification infrastructure, preserved unchanged from the supplied baseline archive.

## Reproduce

From this directory:

```bash
python code/build_release.py --pdf --markdown --baseline
```

Certificate generation and verification use Python's standard library. `--pdf` requires pdflatex and the common packages declared in the source. `--markdown` requires pandoc. The verification is exact rational arithmetic, not floating-point evidence and not an exponentially long trajectory simulation. The general theorems are proved analytically.

## What changed mathematically

The main result now amplifies any certified seed with a positive principal-block normal reserve, instead of requiring the original five-cycle formula. Integral shear-normal forms yield location-independent local alphabets and linear scale N=Gamma(m+1). The proof covers any bounded starting portfolio in the same face and arbitrary diagonal corrections of all stored ray combinations. Graphical seed construction covers weighted path-forest-plus-hub families and branched D-type leading blocks. Collective seeds have every proper principal submatrix CP, defeating every proper-principal separator test, including conic combinations, on a certified perturbation ball. Independently, the fixed-block epigraph has intrinsic graph-ball growth of exact degree r, and its full-lattice version is quasi-isometric to Z^r.

## Remote delivery limitation

The connected GitHub actions available in this session are read-only. No push has been performed. The distribution includes a locally generated commit based on the verified baseline, an object pack/import utility, and a replayable patch. The existing remote branch is untouched. Read the accompanying `GIT_DELIVERY.md` for the exact commit and import instructions; do not confuse the local commit with a published GitHub head.
