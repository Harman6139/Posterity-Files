# Completely positive separation — LAA manuscript

Title: *Exponential paths for every improving pivot rule in completely positive matrix separation*.

This directory contains the complete 14-page article, matching editable source,
and exact verification supplement. It is a prepared manuscript, not a journal
submission. Read `LAA_EDITORIAL_CHECK.md` for remaining workflow and venue checks.

## Build

Requires Python 3.9+ and a TeX installation containing the standard packages listed
in `main.tex`. The bibliography is embedded in that file; there are no external
figures, bibliography databases, or nonstandard local class dependencies.

```sh
python build.py
python supplemental/code/generate_certificates.py
python supplemental/code/verify_certificates.py
```

`build.py` runs pdfLaTeX twice, rejects warnings and overfull/underfull boxes, and
records exact input and output hashes in `build/build_record.json`. PDF metadata
contains a compilation timestamp, so independent recompilations need not produce
the same PDF hash. The source and the shipped PDF are the matched reviewed pair.
The generator and verifier use only Python's standard library. Do not run with
`python -O`, since the original generator uses assertions.

For visual inspection, run `pdftoppm -r 110 -png main.pdf page` in an existing
inspection directory. Text extraction does not replace rendered-page inspection.

## Original input and editorial changes

The mathematical source of record is Posterity-Files commit
`11ffd7fe0e83b7eda47459d1d9b90b7358a4fcfc`, path
`research/pro_m2_ordinary_canonical_20261115/release/manuscript/MAIN.tex`.
This results branch starts from the editorial-brief commit
`ea7700fe645e238edf1d052cb29ab0de87a9dd0e`.
Original research files and branches have not been overwritten.

The rewritten article preserves the theorem, construction, constants, robustness
radius, all-choice quantifier, certificate tests, and fixed-order encoding claims.
It makes three substantive expository improvements:

1. A plain-language opening defines the factorization question and states the
   distinction between local search and short global certificates immediately.
2. The fixed-block movement estimate is presented as a separate geometric result,
   with uniform local finiteness, common-constraint cancellation, and finite
   adjacent-endpoint arguments made explicit.
3. The certificate construction precedes the all-choice confinement proof;
   arithmetic dominance, every allowed exit, and the binary estimate are explained
   in separate measured steps with precise credit to prior work.

The two supplemental scripts are the original exact scripts with only UTF-8/LF
output serialization made platform independent. No mathematical or test logic was
changed. This fixes Windows newline translation and reproduces the original
certificate SHA-256:
`048031057335bfb9fc7c86df3ecba5f3cc55fc32c484e6013d9f79efd577f95f`.

The article's proof is self-contained. The supplement is reproducibility evidence,
not a substitute for the universal proof or a simulation of the long prefix.
`highlights.txt` is a separate editable optional companion prepared to Elsevier's
general size guidance; the current LAA-specific obligation remains to be verified.

Private author records, internal reports, policy actions, and ordinary-web review
records are maintained separately in the authorized private workflow repository.
They are excluded from the clean submission source archive.
