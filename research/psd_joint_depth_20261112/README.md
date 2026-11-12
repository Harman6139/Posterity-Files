# PSD joint-depth frontier — 2026-11-12 theorem package

The all-nullity tuple-existence frontier is addressed by a uniform exact-nullity construction and a finite arithmetic classification.

Read [128: one-switch interpolation](128_ONE_SWITCH_EXACT_NULLITY_INTERPOLATION.md), then [129: complete spectrum and minimum nullity](129_COMPLETE_ALL_NULLITY_ARITHMETIC_SPECTRUM.md). [131: audit and handoff](131_FRONTIER_CLOSURE_AUDIT_AND_HANDOFF.md) explains scope, predecessor dependencies, and the counterexamples that remain valid.

[130: exact certificate program](130_EXACT_ONE_SWITCH_CERTIFICATE.py) and [its recorded output](130_AUDIT_OUTPUT.txt) provide supplementary regression checks.

Status: complete research proof, not independently refereed. The classification concerns existence of `(n,r,d,alpha)`, not every exact exposing rank profile or every dense kernel's normal form.

## Parallel proof packet — additional exact certificates

The companion [fixed-nullity classification proof](128_ONE_SWITCH_FIXED_NULLITY_UNIVERSAL_CLASSIFICATION.md), [standard-library constructor/auditor](129_ONE_SWITCH_EXACT_CERTIFICATE_AUDIT.py), [225 exact audit records](130_ONE_SWITCH_EXACT_AUDIT_RESULTS.json), [example input](EXAMPLE_125_DEGREE_FOUR_INPUT.json) and [example certificate](EXAMPLE_125_DEGREE_FOUR_INPUT.json) were prepared independently in another research continuation. The original [pre-push README](README_PARALLEL_ONE_SWITCH_PROOF.md), [index text](INDEX_APPEND.md), and [source checksum manifest](SOURCE_AND_CHECKSUM_MANIFEST.json) are preserved as produced; their historical 'not committed' statements refer to the packet before this GitHub push. Both sets of numbered milestone files coexist without overwriting each other. Status: unrefereed research proof and exact-rational regression checks.

## One-paper geometric strengthening — Milestone 132

[132: rank universality, complete central spectra, and single-paper architecture](132_RANK_UNIVERSALITY_CENTRAL_SPECTRA_AND_SINGLE_PAPER.md) contains the proofs of the irreducible-symmetric-cone rank-universality theorem and the prescribed-multiplicity central-spectrum theorem, followed by an adversarial literature audit, title, abstract, draft introduction, proof architecture, and journal recommendation. The [primary-source bibliography](132_PRIMARY_SOURCES.bib) accompanies it.

The recommendation is one consolidated paper, **Sharp error exponents and facial depth in irreducible symmetric cones**, targeting Transactions AMS first. The new scope is exact affine-section error exponents and minimum facial depth at fixed Jordan rank, plus eigenvalue orders for external maximum-determinant regularization. It is not a claim about all reducible cones, arbitrary central paths, all facial rank profiles, or algorithmic rates. The arguments use established Milestone 128 and standard Jordan algebra facts and remain unrefereed research proofs.

## Profile continuation — Milestones 133–136

[133: two-channel prefix-profile theorem](133_TWO_CHANNEL_PREFIX_PROFILE_THEOREM.md) proves a uniform iff for every arithmetically admissible sorted-grade-prefix greedy schedule over complex and quaternionic Hermitian PSD, with arbitrary grade multiplicities, every admissible sharp exponent, and no nullity overhead. The construction has explicit ambient stresses, a positive initial-kernel separator, a matching thick arc, and a minimum-degree proof. One redundant child-one blocker resolves the only three-way physical-edge collision.

[134: real/complex profile separation](134_REAL_COMPLEX_PROFILE_SEPARATION.md) shows that fixing the full central spectrum together with the greedy profile can distinguish cone types. For the null weights `(1/4,3/7,1/2,17/28,5/7,1)`, profile `(1,2,2,1)` is impossible over real PSD with rank-one target, even allowing rotated faces, and is attained over complex order-seven PSD. The exact source/field threshold for this datum is `r dim_R(F)>=2`. The file includes the full profile list for that spectrum and counterexamples to the endpoint-only and prefix-only shortcuts. This does not contradict the coarser universality theorem of 132.

[135: exact audit](135_PROFILE_CHANNEL_EXACT_AUDIT.py) and [recorded results](135_PROFILE_CHANNEL_EXACT_AUDIT_RESULTS.json) verify 999 rational exponent–schedule certificates, 454 redundant-collision cases, and explicit real/complex witness pairings. Run `python 135_PROFILE_CHANNEL_EXACT_AUDIT.py --max-h 4 --output audit.json`. The finite audit supplements the proofs rather than establishing the all-dimensional theorem.

[136: simultaneous-flag congruence normal form](136_SIMULTANEOUS_FLAG_CONGRUENCE_NORMAL_FORM.md) proves that any real, complex or quaternionic instance can be transformed so its central and greedy facial flags are both coordinate flags, preserving the entire central order vector, sharp exponent, minimum degree and greedy rank profile. It handles the change of identity shift by two-sided central-envelope comparison. The relative flag position becomes a finite integer incidence table; the flags need not be prefixes.

## Complete arbitrary-profile classification over C and H — Milestones 137–138

[137: complete complex/quaternionic facial-profile classification](137_COMPLETE_COMPLEX_QUATERNIONIC_FACIAL_PROFILE_CLASSIFICATION.md) removes the prefix restriction from 133. It gives a necessary-and-sufficient finite arithmetic criterion for **every** joint central-weight, multiplicity, greedy-survivor-table, sharp-exponent and rank-drop-profile datum over complex and quaternionic Hermitian PSD. Repeated grades may split across multiple steps. The order is exactly the prescribed `r+nu`, with no added null coordinates.

The new construction uses an already removed minimum-weight coordinate q. A lower-weight child uses the source edge `(0,q)`; a child of at least that weight uses its own off-face edge `(q,child)`. Source releases belong to one stage and self-releases are unique. Real tight coordinates, imaginary release coordinates, and a precise redundant-source-blocker deletion give a uniform construction. The proof establishes full-ambient sharp bounds, a thick positive arc, exact central orders, ambient measurement stresses and maximum-rank greedy minimality.

[138: self-contained exact audit](138_GENERAL_PROFILE_TABLE_EXACT_AUDIT.py) and [results](138_GENERAL_PROFILE_TABLE_EXACT_AUDIT_RESULTS.json) verify **7,572** labelled exponent–schedule cases, including **1,590 split-grade cases**, **404 non-prefix cases**, **2,707 redundant-source-blocker cases**, and **247,749 exact generator/stress pairings**. These are supplementary rational checks, not a finite-case proof. Run `python 138_GENERAL_PROFILE_TABLE_EXACT_AUDIT.py --max-h 4 --output audit.json`.

**Real-field boundary:** the arithmetic conditions of 137 are necessary over R. Their converse with fixed central data is false by 134. The full coarse real spectrum `(n,r,s_1,...,s_d,alpha)`, where different central weights may be chosen, is still NOT classified here: the fixed-weight counterexample does not settle that weaker real existence question. All new results are research proofs pending independent review; no worldwide priority certification is claimed.
