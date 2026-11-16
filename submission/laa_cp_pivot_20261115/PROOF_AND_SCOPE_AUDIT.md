# Proof and scope audit — current restructured revision

This record supersedes the 16-page version's numbering. That record is preserved
at commit 78a3ff709e14e49e95138f516fca85faec8eae72.

| Result | Proof and exact scope |
|---|---|
| Theorem 2.2 | Section 4; fixed rational certified seed, fixed bounded starting region in one face, integer m>=1, N=Gamma(m+1), all improving extreme choices, real symmetric perturbation ball, rational centers/separators of logarithmic length |
| Corollary 2.3 | Classical copositive arrow decomposition plus confinement; arbitrary real combinations of stored selected improving extreme rays and arbitrary signed diagonal corrections, conditional on copositivity of the candidate |
| Theorem 2.4 | Section 3; real PD H for finite containing lists, rational H for common denominators, PD perfect H for full Ryshkov primitive-ray bounds |
| Theorem 2.5 | Section 3.4; intrinsic bounded-edge connectivity, bounded degree and Theta(R^r) growth; full-lattice quasi-isometry separately |
| Corollary 2.6 | Original canonical family and constants; Section 5.1 and Appendix A preserve construction, all-choice quantifier, finite endpoints, robustness and encodings |
| Theorem 3.1 and Lemma 3.2 | Retained Codex continuous-minimum, uniform positive gap, active-denominator bound, local finiteness and common-constraint cancellation |
| Theorems 5.2–5.3 | Classical comparison/Schur ingredients, exact hub intervals and positive spanning reserve; all proper principal blocks CP throughout the stated ball |
| Section 5.4 | PD tree/branched blocks, spanning path squares, explicit atom-basis perturbation reserve and correctly oriented canonical starts |

Internal analytical audits reconstructed the nontrivial proofs, including
singular/zero-diagonal arrow cases, active denominators, finite attained
endpoints, degeneracy, sheared full tangent rays, all-choice induction,
same-face multiple starts, normalized distance bounds, all-proper-block radii
and branched-block positivity. Two final scope defects were corrected explicitly:
integer m and selected improving extreme stored directions. A targeted recheck
found no remaining defect in those changes. These are internal analytical checks,
not formal certification or independent human refereeing.

The canonical finite suite passed six families of orders 5,6,8,10; 36 canonical
rays; a complete depth-three improving prefix in order five with 18 vertices,
26 edges, 7,869 lattice evaluations and 119 shared-active incidences; and seven
corruption tests. A 2^64 parameter tests exact inequalities, not a simulated path.
The original portable scripts retain only an output-serialization change.

The additional suite passed eight seed cases, 65 maximal proper principal
blocks, 18 scales, 20 geometric records, seven one-dimensional templates,
three arrow decompositions, four restriction groups and nine corruption tests.
Supplied and freshly generated instances passed the independent verifier.
Fresh parsed data equal the pinned data; all 34 original release files remain
byte-identical to their Git blobs. The supplement contains the unchanged added
programs, data and required inherited input.

The added geometric checks establish stored identities, residual/shear relations,
normal rank and listed-ray feasibility. They do not establish global lattice
feasibility, active-list completeness or every listed ray's extremality, and do
not implement an exhaustive movement loop. Analytic proofs establish those
universal conclusions. Finite seed certification is not claimed polynomial-time
in variable order; a general copositivity oracle is not supplied.

The lower bound concerns adjacent-pivot count, not elapsed time or all separation
algorithms. Input/vertex/ray encoding bounds are fixed-seed statements; arbitrary
real coefficients and arbitrary real/rational perturbed inputs need not have
short finite encodings. Intrinsic graph growth does not exclude external
shortcuts. Positive definiteness is essential, as the singular example shows.
Neither eventual termination nor its failure is proved. No optimal exponent,
all-seed classification or exhaustive historical priority is claimed.
