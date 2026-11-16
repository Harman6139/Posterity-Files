# Completely positive matrix separation — LAA revision

Title: *Pivot lower bounds and lattice geometry in completely positive matrix separation*.

This directory contains the complete 25-page Codex-authored revision, modular
editable LaTeX source and exact verification supplement. It continues Codex
commit 78a3ff709e14e49e95138f516fca85faec8eae72; it does not replace that manuscript
with the additional research release's MAIN.tex. The original versions remain in
Git history. This is a prepared revision, not a journal submission.

## Build and sources

Run python build.py with Python 3.9+ and a current TeX installation. The script
runs at least two pdfLaTeX passes, up to four when references need to settle,
rejects warnings and overfull/underfull boxes, and writes a
build record with the PDF hash and the hashes of every project source. main.tex
inputs sections/*.tex; the bibliography is sections/references.tex. Both figures
are editable TikZ in the source. No external class, image or BibTeX file is needed.
The source archive contains all these dependencies, highlights and the complete
computational companion. Build timestamps may change a recompiled PDF's hash.

The shipped main.pdf has 25 pages, at 11pt with A4 paper and 27mm margins.
Every final page was rendered at 110dpi and inspected; the figures and technical
proof passages were also checked in the earlier comprehensive editorial pass.
No typography was reduced to force a shorter page count.

## Mathematical sources and changes

The additional research source is Posterity-Files commit
8e551996c8462cfe78c20e5edf18d18c0707f2c5,
research/pro_m2_reusable_hardness_20261115/release/. Its 34 files are preserved
unchanged in a separate checkout and named Git history. Its results were
analytically audited before import, with exact checks rerun. The manuscript
preserves Codex's measured continuous-minimum/movement proof and the entire
canonical n>=5 result, including its original normalization and numerical bounds.

The first theorem is now certified-seed amplification. The fixed-block geometry
is a separate result for arbitrary real positive-definite blocks; rationality
enters denominator/encoding statements, and perfectness is needed for full
Ryshkov tangent-ray bounds. Graph distance is intrinsic to the fixed-block set.
The graphical constructions, all-proper-principal barrier and stored-direction
diagonal-correction barrier are developed with complete proofs.

See EDITORIAL_CHANGELOG.md for the section map, preserved results, imported
results and qualifications. PROOF_AND_SCOPE_AUDIT.md records the proof scope and
finite-check limits; NOVELTY_VS_2021_2023_2026.md records the historical comparison.

## Exact verification

The original canonical suite is in supplemental/code; the added suite is in
supplemental/reusable_seed/code. Each has a generator, an independent verifier
and exact data. Read supplemental/README.md and the extension's README.txt before
running them in a writable extracted copy. Both use only Python's standard
library. Do not use python -O. CP_Pivot_Verification.zip contains both suites.
Finite checks do not replace the universal analytic proofs or simulate the
exponentially long prefix.

## Status

Internal analytic audits and complete-source editorial reading were performed.
The recorded ordinary-web Extra High R1 reviewed the earlier 14-page input,
not this substantially expanded revision; no new ordinary-web round was claimed
or initiated. This revision is not labeled Final Submission Ready. The current
LAA-specific author guide returned HTTP403, so complete venue compliance remains
unverified. The author should review the final text and disclosure before use.
Private author records, referee reports and administrative evidence are excluded
from the clean submission source package.
