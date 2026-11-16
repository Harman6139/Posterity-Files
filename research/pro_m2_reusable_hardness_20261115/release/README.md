# Long pivot paths and short certificates: reusable hardness revision

Date: 15 November 2026. Repository: Harman6139/Posterity-Files.
Results branch: `research/pro-m2-reusable-hardness-theory-20261115`.
Baseline: `11ffd7fe0e83b7eda47459d1d9b90b7358a4fcfc`.

## Read

- `manuscript/MAIN.pdf`: revised complete paper.
- `manuscript/MAIN.tex` and `01_geometry.tex`–`05_scope.tex`: all editable sources.
- `COMPLETE_PROOFS.md`: expanded proof companion, generated from the sources.
- `STATUS_PROVED_NOT_PROVED.md`: exact claims, limitations, and progress against the mandate.
- `NOVELTY_AND_PRIORITY_AUDIT.md`: primary-source comparisons, including the classical SPN lemma.
- `PL_RESEARCH_UPDATE.md`: concise decision-facing summary.

## Rebuild

From this directory run:

```sh
python3 code/build_release.py --pdf --markdown --baseline
```

Python certificates use only the standard library. PDF compilation requires pdflatex with amsmath, mathrsfs, lmodern, microtype, geometry, booktabs, and hyperref. Markdown requires pandoc. The baseline programs run in a temporary directory; their original repository files are not modified. The standalone archive includes copies of those programs. The GitHub tree inherits them at `research/pro_m2_ordinary_canonical_20261115/release/code`.

The independent verifier does not import the generator. The exact data are regenerated, then checked, including seven deliberate corruptions. The universal proofs do not depend on finite tests, and no exponential trajectory is simulated. The explicit constants are conservative; fixed-dimension polynomial arithmetic is not a claim of uniformly practical high-dimensional enumeration.

## Main changes

A fixed positive-definite leading block admits finitely many normalized local vertex and tangent-cone models. This yields a seed-based hardness lifting theorem with a scale **linear** in the desired number of pivots, rather than the previous high power. The theorem covers all strictly improving extreme-ray adjacent rules, multiple starts sharing the leading block, arbitrary PSD local-ray corrections, and certain history certificates. Odd-order examples have every proper principal submatrix in the interior of the CP cone. Independently, fixed-block epigraph graphs have bounded degree, polynomial ball growth, and an embedded orthant lattice.

Original manuscripts and previous theorem statements remain intact on their original branches. The new theorem strengthens rather than replaces their correctness.
