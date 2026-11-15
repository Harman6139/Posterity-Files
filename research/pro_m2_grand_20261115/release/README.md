# Arithmetic carriers of constrained Gram representations

Manuscript II research release, 15 November 2026.

The main proof is `manuscript/MASTER_THEOREM.pdf`. The complete editable source is `manuscript/MASTER_THEOREM.tex` and the six numbered `.tex` sections. `COMPLETE_PROOFS.md` is a generated, full-text companion; the typeset manuscript is authoritative for numbering and mathematical typography.

## What is delivered

The canonical arithmetic-carrier theorem, exact completion/regularization criteria, constrained totally-real descent, complete fixed-dimensional bit accounting, corrected partial-observation alternatives, sharp angular moment grids, sharp lattice conditioning, and a precise nonsimplicial interior local/global separation are proved in the manuscript.

`STATUS_PROVED_NOT_PROVED.md` separates mathematical proof claims from unfinished historical-priority and venue requirements. `NOVELTY_AND_PRIORITY_AUDIT.md`, `ARTICLE_LEVEL_VENUE_BENCHMARK.md`, and `ADVERSARIAL_PROOF_AUDIT.md` record the comparisons and limitations. No journal percentile, acceptance probability, external human verification or proof-assistant certification is claimed.

## Reproduce the exact certificates

Python 3.10 or newer and its standard library suffice:

```sh
python code/generate_new_certificates.py
python code/verify_new_certificates.py
```

The generated `certificates/new_exact_certificates.json` must have SHA256

`ed0b5405a54353b35eaaa65312e77d08d5f1ead1ae41f5a3207ef914fe103117`.

The verifier reports five angular-grid cases, eleven facet cases, one arithmetic obstruction and three rejected deliberate corruptions. Long-path certificates are compressed identities, not simulations of exponentially many pivots. These programs do not implement general real quantifier elimination.

## Build the paper and expanded proof text

A standard TeX installation with `pdflatex` and the listed document packages is required for the PDF. Pandoc is optional for the Markdown companion.

```sh
python code/prepare_release.py --pdf --markdown
```

Without those flags the script expands the standalone TeX source and regenerates/verifies certificates using only Python. With `--pdf`, it runs LaTeX twice and rejects compilation failures. The PDF output is deterministic in content, but PDF metadata and TeX-engine versions may change its byte hash. Mathematical data have the fixed hash above.

## Remote preservation

Repository: `Harman6139/Posterity-Files`.
Branch: `research/pro-m2-grand-arithmetic-matrix-cones-20261115`.
Remote directory: `research/pro_m2_grand_20261115/release`.

Complete modular LaTeX and executable source are preserved remotely. The archive supplied with the response additionally contains the compiled PDF, expanded proof text, and full generated certificate JSON. These derived files can be regenerated from the remote source; their inclusion in this archive is not a claim that every binary or expanded file has separately been uploaded to GitHub.

Earlier checkpoints and their source branches have not been overwritten. The new release clarifies that the terminal vector domain itself is canonical, whereas an earlier checkpoint only established canonicity of its matrix slice.
