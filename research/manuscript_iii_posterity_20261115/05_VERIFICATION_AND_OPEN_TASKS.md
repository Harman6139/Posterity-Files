# Reproducibility and explicit unresolved proof gates

**Audit executed 2026-11-15.** This file distinguishes exact computational diagnostics, mathematically proved conditional/subclass theorems as asserted in saved manuscripts, and the open all-pencil target. No program run verifies a quantified theorem for ALL possible adversarial real queries.

## Independent reruns of saved programs

1. **Exact-rational minimax construction.** Script in [complete proof archive](PROOF_ARCHIVE/04_EXACT_RATIONAL_MINIMAX_CHECKPOINTS_01_TO_13/verify_minimax.py), result [VERIFICATION_RESULTS.json](PROOF_ARCHIVE/04_EXACT_RATIONAL_MINIMAX_CHECKPOINTS_01_TO_13/VERIFICATION_RESULTS.json). The script (from the user's earlier artifact packet, identical source to committed script) was rerun in an isolated working directory using:

       python verify_minimax.py --max-depth 6 --output rerun_minimax_results.json

   Runtime result: `{"status":"PASS","exact_checks":9964}`. The rerun JSON and the committed original report have identical SHA-256 hash `8fcd82902a74509e70319c5c93298918771924cdf4bc0b9bb7bc27647a9a6b6b`. Script SHA-256 `fa966f7abb445c16c65dd19ff4afde99c7b41af766fe10b14d2e73fb49850b60`.

   Tested: rational three-moment equations, positivity and support, four-squares encoding, Frobenius isometry, normalization, actual scalar negative-spectrum distances, exact exterior values and gradients up to huge evaluation magnitudes, prefix locality, irrational quadratic-field mismatch decoding, exact binomial minimax recursion, explicit confidence constants, and weak-infeasibility tail algebra.

2. **Arithmetic spectral observability construction.** Script [verify_results.py](PROOF_ARCHIVE/03_ARITHMETIC_SPECTRAL_CHECKPOINTS_01_TO_08/verify_results.py) and corresponding [report](PROOF_ARCHIVE/03_ARITHMETIC_SPECTRAL_CHECKPOINTS_01_TO_08/VERIFICATION_RESULTS.json) were independently rerun with installed SymPy 1.14:

       python verify_results.py

   Result: `{"checks":286,"all_passed":true,"sympy_version":"1.14.0"}`. Local script SHA-256 `33ea835eef352ae5cbd44a8cbecc13f5ea8516f596df98b2251d5f5033d17aee`; generated JSON SHA-256 `c2d7c1c80d16d3d845019429b8228d592d414c7facdf5959682f3ec571da1299`.

   Tested: exact small rational isometry and identity examples, discriminants/characteristic polynomials, nontrivial irrational scalar fingerprints, subset-sum generating identities and exceptional pairs, rational response-code separations. The test suite explicitly states that finite checking is not proof of the universal claims.

3. **Later spectral PLQ and stronger-PSD-projection theorems:** full analytical proofs are saved as checkpoints 09–13 in exact-rational subtree, but **NO new comprehensive independent finite or symbolic test suite was run for those theorems in this archive operation.** Their proof-level correctness must be assessed separately by another mathematician; prior targeted checks/notes are described in each checkpoint and do not count as fresh external certification.

**Local manuscript drafts outside GitHub archive.** Earlier attached draft artifacts in the chat's model container include `m3_grand_arithmetic_20261115/main.tex`, `main.pdf`, `m3_exact_rational_minimax_20261115/minimax_proof.tex` and `minimax_proof.pdf`. The content-addressed GitHub PROOF_ARCHIVE trees store every numbered source checkpoint and its FULL MATHEMATICAL PROOFS as Markdown, alongside committed verification scripts/results. These particular earlier compiled PDFs/TeX builds were **not committed** in this operation. The archive must not falsely claim to contain those binary builds. They may remain available as conversation artifacts, and can be uploaded as an additional optional publishing-source commit if desired. Their local original SHA256 checks were:

- Grand arithmetic `main.tex`: `b523315d039a375a5d595b24fc761938e27bdf0efb527f7df4dbf28d977c2506`;
- Grand arithmetic `main.pdf`: `1f02acfa5f3b9821ee66c9efe574678c209d212d3d797a5c73ddb8fb75d71c27`;
- Exact minimax prior companion ZIP packet: `9b6900728fbd585e0c50c5b5f8fc22f1be79c897b5d9a1dbdd9875b19c229f6e`.

The original initial handoff and subsequent grand arithmetic handoff **are** verbatim committed, and all current source proof Markdown is committed.

## Definitive mathematical gates

### A — primary unresolved target, do not represent as solved

In the rational isometric PSD-distance model with unknown rational coefficient matrices, exact scalar value and full coordinate-gradient calls at arbitrary finite real vectors, and arbitrary unqueried output, prove either:

- for beta=1/2 a single fixed polynomial-bit rational hard prior per horizon T with Pr[f(output)>=c/T]>=2/3 after T exact calls, matrix order/dimension polynomial in T, common all-accuracy escape profile, or
- a universal identification/optimization method that refutes that lower rate and a sharp corrected dimension-uniform law.

*Neither statement currently follows* from the archived results. Only Omega(log(1/epsilon)) lower and O(1/epsilon) upper in the all-coordinate-dimension beta=1/2 class. Fixed two coordinates give Theta(log(1/epsilon)).

### B — model separation that cannot be relaxed

- REAL Haar hidden chart in the real-conic result is not rational: cannot change names of coordinates to pretend it is.
- Positive gradient error `zeta>0` is not the exact zero-noise case; the hard rational support can vary with `zeta`.
- Radius-charged rational lower bound is a separate cost.
- Full PSD-projection oracle reveals a whole matrix; the original returns only scalar loss and compressed tangent gradient. Exact simulation can require Theta(n) original calls on known examples.
- Knowing explicit SDP coefficients permits an entirely different algebraic offline algorithm with zero identification calls. This does not refute hidden-input lower bounds.

### C — independent verification and manuscript tasks

- Obtain external theorem-by-theorem referee checks of the spectral hyperplane-propagation proof, especially the kernel projector rational extension and rank bound; check the all-rational irreducible-squared-spectrum field-trace proof and common probe hypotheses.
- Verify the exact-rational binomial strategy's arbitrary-real-query simulation including boundary cases; countable independent fixed-prior success quantifiers; finite precision vs strong exact computation.
- Audit priority against 2024–2026 matrix-vector, conic-oracle, spectral calculus and radial basis function literature. Check no theorem has a known equivalent under a different oracle name.
- Extract one 20–30 page self-contained complete-scope manuscript. Integrate only compatible hypotheses. Short abstract and introduction must acknowledge the original all-pencil question OPEN. No “grand frontier fully solved” title.
- For SIOPT aim ~25 journal-formatted pages and no reliance on extensive appendices that must be published as supplementary material; consult current SIAM policy. JCA has separate author instructions at new Banach Press site.
- Expand 32-paper benchmark by reading *all* actual full results/proofs under authorized subscriptions or author manuscripts. Currently full-proof pairwise proof-depth superiority for 8/10 or 10/12 **NOT certified**.
- If a future all-pencil positive hard distribution exists, it must preserve a polynomial-in-T objective barrier under exact arbitrary-distance queries. Existing nested scalar/radial masks provably lose energy exponentially. More independent copies or rotated equal-scale copies do not repair them.

## GitHub reproducibility and provenance

The exact four original source trees are embedded in this archive with their original Git blob hashes; [full inventory](01_FULL_PROOF_MAP_AND_PROVENANCE.md) lists each file and source SHA. All results appear on a NEW independent branch. The original proofs, failed routes, historical initial statuses, and revisions remain in the underlying Git history.

Do not infer formal journal referee endorsement, originality certification or an “80% acceptance chance” from the archived checkpoints, test counts, or preliminary rubric.
