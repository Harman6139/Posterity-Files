# Novelty and priority audit — 15 November 2026

## Decision

The release has a complete internal proof of the canonical arithmetic-carrier theorem and its stated consequences. **Historical priority is not certified.** The comparisons below identify the actual candidate contribution and the substantial antecedents. A negative search is not evidence that no equivalent theorem exists. The reported 2026 boundary counterexamples are not assumptions of any proof here; their full external certificates were not independently rerun.

## Closest primary sources

| Source | Verified antecedent and boundary of the present claim |
|---|---|
| Borwein–Wolkowicz, *Facial reduction for a cone-convex programming problem*, J. Austral. Math. Soc. A 30 (1981), 369–380, DOI 10.1017/S1446788700017250 | Successive conic exposure is classical. The proposed contribution is not facial reduction itself; it is the exact rational column-domain replacement and the resulting canonical carrier. |
| Safey El Din–Zhi, *Computing rational points in convex semi-algebraic sets and sum of squares decompositions*, SIAM J. Optim. 20 (2010), 2876–2889, DOI 10.1137/090772459 | Their rational-point and rational-SOS decision results are prior art. Section 2 supplies the sampling, field-factorization, and quantifier-elimination bounds used here. A rational matrix point in a generalized CP cone need not have rational permitted columns. The new claim concerns these column restrictions, not the first fixed-dimensional rational decision theorem. |
| Dutour Sikirić–Schürmann–Vallentin, LAA 523 (2017), 46–51, DOI 10.1016/j.laa.2017.02.017 | Rational interior CP factorization is prior art. The reserve lemma is a general polyhedral-domain version used as a prerequisite, not the flagship novelty. |
| Same authors, Mathematical Programming 187 (2021), 25–45, DOI 10.1007/s10107-020-01467-4 | Perfect-form simplex traversal and rational-factor discovery are antecedents. Conjecture 3.2 concerns finite nonmember termination with a suitable pivot, not a polynomial pivot guarantee. The present exact arithmetic-fiber obstruction and canonical domain are different statements. |
| Dannenberg–Schürmann, *Perfect copositive matrices*, Communications in Mathematics 31 (2023), 137–156, DOI 10.46298/cm.11141 | Shear vertices, perfectness, and adjacency/lifting are antecedents. The isolated new path statement fixes a nonsimplicial cone, uses interior factorable targets, proves exactly N−1 unique shadow moves, and holds the arithmetic carrier and observation condition fixed. |
| Oertel–Schürmann, *Generalized Perfect Matrices*, arXiv:2602.05841v2 (2026) | Rationally generated cones have the qualitative Interior Ryshkov property; generalized tessellations and certificate procedures already exist. The current work does not re-claim these. Its proposed contribution concerns exact rational affine fibers and finite canonical rational column domains, including arithmetic infeasibility. |
| Hillar, Proc. AMS 137 (2009), 921–930, DOI 10.1090/S0002-9939-08-09641-X; Scheiderer, JEMS 18 (2016), 1495–1513, DOI 10.4171/JEMS/620 | Totally real SOS descent, trace forms, rational obstructions, and characteristic subspaces are antecedents. The present descent retains polyhedral restrictions on each column even when conjugation leaves those cones. It is not a first trace-descent theorem. |
| Laplagne, *Facial reduction for exact polynomial sum of squares decomposition*, Mathematics of Computation 89 (2020), 859–877, DOI 10.1090/mcom/3476 | Sections 3.1–3.4 already use algebraic zero, kernel, trace, and coefficient restrictions. The paper warns that its general parametrization restrictions need not retain every rational solution. Here rational coordinates in a rational face basis make the coefficient restrictions necessary, and the proof establishes exact preservation and canonicity. |
| Nishijima–Lourenço, LAA 743 (2026), 211–249, DOI 10.1016/j.laa.2026.04.019 | A substantial non-orthant benchmark: real facial classification over the second-order cone, including exposedness and chain information. The present theorem is an arithmetic completion theorem for polyhedral column domains, not a replacement for that classification or a theorem covering arbitrary nonpolyhedral domains. |
| Yıldırım (2012), DOI 10.1080/10556788.2010.540014; de Klerk–Laurent–Sun–Vera (2017), DOI 10.1007/s11590-016-1023-7 | Polyhedral approximation and quadratic grid rates are old. The isolated claim is the exact angular constant for the specified moment-preserving map, optimal-grid rational nonattainment, and the explicit stereographic rational grids. |

Primary full texts used for the nearest mechanisms include:

- https://perso.lip6.fr/Mohab.Safey/Articles/convex_sas.pdf
- https://arxiv.org/pdf/1810.04215
- https://arxiv.org/html/2602.05841v2
- https://arxiv.org/html/2502.04006v2
- https://ems.press/content/serial-article-files/32129
- https://cm.episciences.org/11588/pdf

The specific proofs and sections above were inspected; this is not a claim of an exhaustive proof audit of every publication in the field.

## What must not be called new

Conic Carathéodory, four-square conversion of rational weights, rational interior reserves as a general mechanism, classical separation, real-algebraic sampling, qualitative generalized perfectness, the existence of non-exposed faces, unconstrained totally real SOS descent, and a second-order grid rate by themselves are not new contributions. The sharp lattice norm exponent was established in the preceding Manuscript II project and is reproduced with attribution.

## Candidate novelty that survives these comparisons

The precise candidate is a **canonical finite union of rational polyhedral vector cones**, equal to the closure of rational directions insertable into a feasible rational Gram completion, with a choice-independent construction in at most n(n+1)/2 strict matrix-span reductions. It preserves every rational factor column, characterizes exact and limiting rational fibers, decides each rational regularization direction, and supports the constrained totally-real descent argument. This is more than computing a rational point in a convex set or giving a sufficient regularization.

The accompanying local/global result is a corrected separation principle: genuine arithmetic faces can be fixed and trivial while an interior perfect-form subdivision forces exponentially many local crossings. It is not an assertion that no possible invariant can encode a path, nor a lower bound on every local algorithm.

## Unfinished verification

The full Shaked-Monderer–Dür–Berman 2018 article was not successfully retrieved in this continuation; known boundary sufficient conditions were checked against the authors' 2025 survey, but that does not replace a full-proof audit. The complete Holden and Shitov external counterexample packages were not independently verified. The literature search did not establish a historical first-priority certificate. Expert review of the universal theorem and its complexity accounting is still required before treating the result as a vetted publication claim.
