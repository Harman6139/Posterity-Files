# Complete corrected proof release — 15 November 2026

## Main result

The complete modular manuscript is saved under `research/pro_m2_grand_20261115/release/manuscript`. Its entry point is `MASTER_THEOREM.tex`, with all six included sections committed. The proof is centered on the canonical arithmetic carrier of a rational affine Gram fiber. It contains the exact factor-or-arithmetic-obstruction construction, prescribed-direction criterion, constrained totally-real descent, explicit fixed-dimensional bit accounting, corrected observation alternatives, sharp angular grid theorem, and nonsimplicial depth-zero local/global separation.

The strongest new local theorem has a unique shadow trajectory of exactly N-1 pivots on O_n(log N)-bit interior targets with explicit constant-width rational factors, fixed full carrier, fixed observation condition, and polynomially bounded inverse interior radius. It applies in every n>=4 to a fixed nonsimplicial cone and, after fixed integral congruence, to strictly entrywise-positive positive-definite targets. It is not an every-local-rule result.

## Preservation and reproducibility

All complete editable manuscript sections, the exact certificate generator, the separately written verifier, and `code/prepare_release.py` are saved remotely. The latter expands the full standalone source, regenerates the exact JSON, verifies it and its fixed SHA256, and optionally builds the PDF and full Markdown proof companion.

A fresh run passed five angular-grid cases, eleven compressed facet certificates, and one arithmetic obstruction; three deliberately corrupted data sets were rejected. The saved verification report gives the exact hash `ed0b5405a54353b35eaaa65312e77d08d5f1ead1ae41f5a3207ef914fe103117`.

The compiled 21-page PDF and full generated JSON/Markdown are included in the conversation release archive. They are derived from the committed source; this checkpoint does not claim that each derived binary/expanded file has separately been uploaded to GitHub. The PDF compiled twice without overfull or undefined-reference warnings and was rendered for visual checks.

Earlier milestones and baseline source branches are unchanged. This release supersedes the earlier uncertainty about the canonicity of the entire terminal vector domain: the proof now establishes that stronger uniqueness.

## Correctness and priority qualifications

The general proof is analytical; finite tests are supplementary. No independent human review, formal proof-assistant verification, or production implementation of general real-algebraic elimination has been performed.

Laplagne's algebraic SOS facial-reduction antecedents and the classical rational-point, totally-real trace, generalized-perfectness and grid literature are explicitly credited. The exact decision transcript need not be a full cylindrical cell decomposition. The weighted descent theorem requires total positivity.

The registered twelve-paper LAA full-proof benchmark remains incomplete and unscored. Historical first priority and an upper-20% mathematical-quality designation are not certified. Therefore the corrected mathematical theorem is delivered with complete internal proofs, but the broader assignment's historical/publication gate is NOT declared solved.
