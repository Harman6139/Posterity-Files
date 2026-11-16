# Proved / not proved — reusable local-search hardness theory

## Proved with complete analytical proofs

1. **Finite local models.** For every fixed real positive-definite leading block H, integer shear normalization bounds all active numerator and denominator coordinates and leaves only finitely many vertex and tangent-cone types. With rational H, all face vertices have a common denominator. With H perfect, full primitive tangent rays have bounded leading block, linearly growing cross entries, and quadratically growing last entry. Each complete local step is polynomial bit complexity for fixed H and dimension.
2. **General normal-cone lifting.** A rational positive-definite, strictly positive non-CP seed B qualifies whenever its leading block lies in the interior of the finite normal cone of a rational positive-definite perfect H. An explicit scaling N=C(m+1) forces at least m adjacent pivots for every strictly improving extreme-ray rule. Robustness, separator margins, bit heights, and all constants are specified. This removes the five-cycle from the theorem's hypotheses.
3. **Larger certificate model.** Arbitrary nonnegative diagonal and arbitrary PSD corrections of local rays cannot separate. Neither can any copositive history certificate with a PSD leading block. The underlying PSD-principal-block-to-SPN lemma is classical and credited, not a new result.
4. **Multiple starts.** Every initial vertex in any prescribed bounded region of the same fixed-H face is covered simultaneously. Fixed finite menus, parallel runs and restarts in this region do not evade a completed m-step run. The theorem does not cover arbitrary menus with different leading blocks.
5. **Genuinely higher-order seeds.** Every odd order n>=5 admits strictly positive positive-definite nonmembers satisfying the criterion and having all proper principal submatrices interior CP. A neighborhood retains that property. The same result applies to a class of nonuniform weighted cycles. Thus no smaller principal copositive certificate, even of order n-1, can detect these targets. Larger odd-order examples are not padded order-five obstructions.
6. **Independent graph geometry.** For every real H>0, the bounded-edge graph of the corresponding quadratic integer epigraph is connected, has bounded degree, graph-ball volume Theta(R^r), and a quasi-isometrically embedded Z_+^r. For rational H, logarithmic-height vertices can have exponential intrinsic graph distance. This is intrinsic to the fixed-block graph, not a claim about paths allowed to leave it.

## Counterexamples and limitations

Strict exposure is sufficient, not characterized as necessary for all hardness. Outside the normal cone, improving escaping rays exist for large scale; boundary exposure can also allow escape (an explicit canonical order-three example is provided). Distinct perfect forms have disjoint normal-cone interiors, so one strict seed exposure cannot establish the same confinement for arbitrary distinct-H starts. This is a limitation of this mechanism, not a universal impossibility theorem.

Arbitrary nonextreme descent directions and unrelated global separator searches are not covered. A small mixture with an escaping tangent direction already defeats exact confinement. Positive definiteness of H is necessary for the stated graph theorem: H=0 has only one graph vertex. No optimal dimension constants, optimal lower-bound exponent, or variable-dimensional polynomial runtime is claimed. No new diagonal-correction decomposition lemma is claimed.

## Verification actually performed

New exact suite: five seed families; 39 maximal-proper-principal factorizations using 2,092 weighted atoms; 15 scale cases; six sheared vertices with 129 full extreme rays; 25 explicit geometric vertices with 300 adjacency comparisons; two SPN decompositions; seven deliberately corrupted certificates rejected.

The inherited original suite was rerun unchanged: six families, 36 canonical rays, 18 branching-prefix vertices, 26 edges, 7,869 exact lattice evaluations, and seven deliberate corruptions rejected. These finite checks support implementation correctness and do not prove the universal theorems by themselves.

For the analytically certified m=2^64 example in order five, the new parameter N has 575 bits (the previous conservative construction used 4,823). No such long trajectory was simulated.

## Publication status

The proof package is an internally checked research manuscript, not externally refereed or proof-assistant certified. Primary-source comparison distinguishes the claimed new statements from qualitative perfect-matrix theory, inhomogeneous quadratic geometry, classical odd-cycle obstructions, and the known SPN lemma. Exhaustive historical first priority is not certified.

The user reports an old randomized benchmark of ten published papers, with ranks 4/11 and 7/11. The actual cohort and full rubric were not available in the retrieved files. The revised theorem materially improves reusable scope and algorithmic strength, but a top-three position in both axes is NOT certified and should be independently reranked using the unchanged sample.
