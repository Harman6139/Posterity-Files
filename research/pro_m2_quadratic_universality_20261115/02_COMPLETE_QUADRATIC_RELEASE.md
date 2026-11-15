# Complete quadratic arithmetic release — 15 November 2026

## Main mathematical strengthening

The new standalone 18-page manuscript proves an exact arithmetic classification for every rational symmetric quadratic column inequality q(x)>=0. For a rational PSD target A, a nonnegative trace pairing gives real feasibility. Strictly positive trace always permits rational factors; at trace zero, rational factors exist exactly when the restricted form on range(A) vanishes identically or its nondegenerate quotient is isotropic over Q. This is an exact criterion, not a sufficient condition only.

The same mechanism yields a canonical arithmetic carrier for every rational affine completion fiber. The algorithm computes maximal rational support, uses at most 2n+3 rational convex-semialgebraic point queries and at most one rational isotropy decision, and returns the closure of every viable rational column direction. The carrier can be genuinely curved. It describes the closure of all rational completions and exact observation-preserving rationalization.

For standard Lorentz cones, every rational real-feasible target of rank at least five factors rationally. An explicit integer rank-four matrix of order five proves sharpness, by a modulo-eight obstruction on its range. Rank-two and rank-three examples are also supplied. Exact spherical and ellipsoidal moment problems inherit the arithmetic criterion. A rank-two Lorentz matrix with factors over Q(sqrt(2)) but no rational factors shows that the earlier polyhedral totally-real descent theorem cannot extend unchanged to curved columns.

For any relatively open positive-scaling-invariant domain in range(A), minimum rational permitted width is exactly the maximum of minimum real permitted width and unrestricted rational width. Signed Cayley approximation gives explicit bit heights and a column-clearance hypothesis gives a quantitative dual margin. Classical orthogonal density and the rank+3 unrestricted width consequence are credited, not claimed as new.

Two quadratic observations on products of PSD2 column cones, or on one larger PSD column cone, encode arbitrary rational polynomial feasibility. The proof preserves rational solutions in both directions and excludes escape through arbitrary Gram width. It makes no claim about the present decidability/undecidability status of that problem. A repeated-squaring family independently proves exponential necessary coordinate bit height in variable dimension.

## Resources and proof scope

The general theorems have complete internal analytical proofs. Rational convex-point decision and classical quadratic-form results are explicitly charged antecedents. Cassels' explicit bound gives a total fixed-dimensional 2^{O_n(L)} isotropy search; successful seeds and resulting factors have O_n(L) bit height. Post-seed weighted factor construction is polynomial for fixed n. A production implementation of the abstract rational-point and isotropy algorithms is not supplied.

No new local-pivot lower bound for Lorentz cones is asserted. The earlier all-descending-rule theorem is inherited without changing its domain or rule restrictions. The unifying conclusion is that arithmetic behavior is governed by the permitted quadratic zero domains: linear coefficient kernels in the polyhedral case, local-global isotropy for one quadratic boundary, and arithmetic-circuit universality for simultaneous curved boundaries.

## Preservation and verification

All eight editable LaTeX files, three complete Python programs, README, theorem-status document, source-priority audit, exact verification report, and clean-rebuild report are committed under release/. Authenticated GitHub tree reads verified that all fourteen manuscript/program/document Git blob hashes equal their local files. Earlier milestones and branches are unchanged.

A fresh clean rebuild from source reproduced the standalone LaTeX, complete Markdown proofs, exact data JSON, and verification report byte for byte. The PDF compiled twice without overfull or undefined-reference warnings; all eighteen pages were rendered and visually inspected. The PDF and full generated JSON/Markdown are derived outputs included in the conversation release archive, not separately asserted to be binary GitHub uploads.

The separate verifier imports no generator code. It passed three arithmetic obstruction cases with 4,889 modular evaluations; four exact rational-factor cases; two affine carriers; three rational Cayley cases; and three circuit cases. Seven deliberately corrupted data sets were rejected.

Certificate SHA256:
2f432846643e31e100935ba1a4f3c58adb19bbce89bee89f2e652efc055969f7

Standalone proof-source SHA256:
8fb64d8dbfbc3b1d0c50222304df721ec78cf7bb75303751b28651ff2780be62

## Historical and publication limits

Sturm–Zhang's real rank-one generation, Nishijima–Lourenco's real Lorentz-face classification, Safey El Din–Zhi's rational convex-point algorithm, classical Hasse–Minkowski/Meyer/Cassels arithmetic, rational orthogonal approximation, and Burer–Dong's real QCQP conic reformulations are explicit antecedents. Historical first priority of the precise combined arithmetic theorem is not certified. The registered LAA upper-quintile comparison remains incomplete and unscored. No external human review, formal proof-assistant checking, journal percentile, or editorial probability is claimed.
