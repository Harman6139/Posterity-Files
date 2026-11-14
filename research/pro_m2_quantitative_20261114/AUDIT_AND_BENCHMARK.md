# Source audit, originality limits, and publication benchmark

**Audit date:** 14 November 2026.
**Decision:** the proposed adjacent-pivot theorem is disproved. The manuscript's positive quantitative replacements are proved internally. **An upper-quintile journal rating is not certified.**

## 1. Exact scope of the original target

The source handoff is `02_MANUSCRIPT_II_COPOSITIVE_QUANTITATIVE_PIVOTS.md` on `research/three-flagship-pro-handoffs-20261114`. The inherited mathematical baseline is commit `22ed4becd320695b41f8a11f1223ea090ef89ecf`, particularly milestone 37 and `00_MANUSCRIPT2_SHARP_GRID_STATUS.md`. Both were retrieved through authenticated GitHub. The full handoff and both files were read.

The standalone milestone 34 was not retrieved. Its rule and finite-path argument were available in milestone 37, and the manuscript gives a self-contained proof. No claim is made to have read a missing original file.

Dutour Sikirić–Schürmann–Vallentin, *A simplex algorithm for rational cp-factorization*, Mathematical Programming 187 (2021), 25–45, DOI **10.1007/s10107-020-01467-4**, contains Procedure 3 and Conjecture 3.2. Its conjecture concerns finite termination for a suitable pivot rule, not polynomial precision complexity. The published full text and the relevant PDF pages were inspected. Our lower bound refutes the stronger proposed theorem in the handoff, not finite termination itself.

## 2. Closest mathematical controls

| Source | Prior mechanism/result inspected | Distinction in this manuscript | Novelty caution |
|---|---|---|---|
| Dutour Sikirić–Schürmann–Vallentin (2021), DOI 10.1007/s10107-020-01467-4 | Perfect copositive simplex geometry; Procedure 3; finite-termination conjecture; binary Farey/continued-fraction discussion | Exact forced finite nonmember family with N pivots from O(log N)-bit input; survival under the specified grid correction; effective all-order arithmetic bounds | Binary subtractive paths are already present in substance. The explicit precision lower bound is not a new discovery of Farey geometry. |
| Oertel–Schürmann, *Generalized Perfect Matrices*, arXiv **2602.05841v2**, revised 4 June 2026 | Interior-Ryshkov property for rationally generated cones, Diophantine argument, generalized cone certificates | Explicit M^{-(n−1)} margin, matching perfect-matrix examples in every n, active-height bounds, quantitative finitely generated cone specialization | The qualitative IR theorem and Diophantine mechanism are not new. Independent priority checking of the quantitative sharpening remains needed. |
| G.-Tóth–Hendrix–Casado, CEJOR 30 (2022), 1071–1092, DOI **10.1007/s10100-021-00737-6** | Face-based simplex quadratic optimization; KKT and monotonicity arguments, full relevant propositions/proofs | Exact bordered-system formulation with minimum-support proof for singular cases; complete rational certificate table | This is a classical oracle mechanism, not a claimed new algorithmic paradigm. |
| Oertel–Schürmann, *On Computing the Copositive Minimum and its Representatives*, arXiv **2509.23696** (2025) | Integer copositive minimum and representative computation; relevant method discussion | Effective cutoff and exact neighbor interfaces with global precision accounting | Our practical code is not claimed to outperform their method. |
| Grötschel–Lovász–Schrijver (1981), Combinatorica 1, 169–197, DOI **10.1007/BF02579273** | Classical separation/ellipsoid framework, primary bibliographic record | Fully rational rounding constants, exact support cuts, two strict margins, explicit resource ledger | The polynomial fixed-dimensional nonlocal separation conclusion is classical in substance. |
| Yıldırım (2012), DOI **10.1080/10556788.2010.540014**; de Klerk–Laurent–Sun–Vera (2017), DOI **10.1007/s11590-016-1023-7** | Primary metadata and established grid/polyhedral approximation antecedents | The inherited sharp coefficient is used only to show that the modified adjacent path stays exponentially long | A full line-by-line proof audit of these two older articles was not completed here. No claim of inventing the first grid hierarchy or quadratic rate. |

Primary sources:
- https://link.springer.com/article/10.1007/s10107-020-01467-4
- https://arxiv.org/abs/2602.05841
- https://link.springer.com/article/10.1007/s10100-021-00737-6
- https://arxiv.org/abs/2509.23696
- https://ir.cwi.nl/pub/10046

## 3. 2026 boundary-factorization reports

The primary repository README at `ajt60gaibb/OpenProblemsInNLA/references/holden-pf03-2026-09-13/README.md` was retrieved. It reports Holden's order-444, rank-seven counterexample to unrestricted rational nonnegative factorization and expressly distinguishes its AI-assisted audit from human peer review or formal verification. The complete submitted proof and all its certificates were **not independently revalidated in this attempt**.

The handoff also reports Shitov's order-308 construction and a November 2026 Zenodo deposit. Search located a corresponding ResearchGate title, but the cited Zenodo full record was not successfully retrieved. It would be unjustified to certify its proof or priority from that evidence. Our theorems neither use nor assert an unrestricted rational boundary factorization statement, so neither report is a logical premise.

## 4. Preregistered published-paper comparison

Protocol committed **before scoring** as `02_BENCHMARK_PROTOCOL.md`, commit `d547cb044395dc24b96f6e5a94d7fe6c2d8b03df`.

Selection: first five research articles by first printed page from each of LAA volumes 720 and 721 (2025), and Mathematical Programming volume 215 issue 1–2 and volume 219 issue 1–2 (2026). Errata/editorials/indexes are excluded and replaced by the next research article. Inaccessible articles remain in the denominator. No convenient substitutions are allowed. These are fixed recent strata, not a random sample of all journal output.

Required evidence for a score: complete main theorem and proof, hypotheses, mechanism, novelty against close antecedents, breadth, constructive usefulness, correctness limitations, exposition and fit. An abstract, table of contents, or DOI is not enough. Even an eventual 8/10 in a small selected sample would not statistically establish a population percentile or an acceptance probability.

### Mathematical Programming: ten identified sample articles

The publisher issue pages and individual DOI records were retrieved. **None of these ten has been assigned a substantive comparative score:** their full proofs have not all been audited. Open-access HTML availability is not the same as completed reading.

| Volume; pages | Title | DOI | Benchmark status |
|---|---|---|---|
| 215; 1–56 | A primal-dual extension of the Goemans–Williamson algorithm for the weighted fractional cut-covering problem | 10.1007/s10107-025-02209-0 | Unscored; subscription preview and metadata retrieved |
| 215; 57–93 | A prophet inequality based approach to the adaptive ProbeTopK problem | 10.1007/s10107-025-02211-6 | Unscored; full HTML available, proof audit incomplete |
| 215; 95–143 | The two-stripe symmetric circulant TSP is in P | 10.1007/s10107-025-02215-2 | Unscored; metadata retrieved |
| 215; 145–191 | Duality in convex stochastic optimization | 10.1007/s10107-025-02216-1 | Unscored; full HTML available, proof audit incomplete |
| 215; 193–236 | An accelerated distributed stochastic gradient method with momentum | 10.1007/s10107-025-02217-0 | Unscored; correction must also be considered |
| 219; 1–27 | Inexact subgradient methods for semialgebraic functions | 10.1007/s10107-025-02245-w | Unscored; metadata retrieved |
| 219; 29–59 | On covering Euclidean space with Q-arrangements of cones | 10.1007/s10107-025-02252-x | Unscored; metadata retrieved |
| 219; 61–111 | Logarithmic integral optimization via adaptive importance sampling based surrogation methods | 10.1007/s10107-025-02254-9 | Unscored; full HTML available, proof audit incomplete |
| 219; 113–156 | A hierarchy of eigencomputations for polynomial optimization on the sphere | 10.1007/s10107-025-02251-y | Unscored; full HTML available, proof audit incomplete |
| 219; 157–217 | Globally convergent derivative-free methods in nonconvex optimization with and without noise | 10.1007/s10107-025-02255-8 | Unscored; metadata retrieved |

The publisher lists a correction to the momentum article in volume 215, pages 859–861. That correction cannot be ignored in any completed assessment.

Primary issue lists:
- https://link.springer.com/journal/10107/volumes-and-issues/215-1
- https://link.springer.com/journal/10107/volumes-and-issues/219-1

### LAA: sample not fully recovered

The selected publisher table-of-contents endpoints returned access errors. The first research paper in volume 720 was identified as *Counting core sets in matrix rings over finite fields*, Rissner–Werner, pages 1–25, DOI **10.1016/j.laa.2025.04.006**. The complete fixed ten-paper sample and its full proofs were not recovered, so **the LAA benchmark is incomplete and no percentile score is assigned**.

Volume 721 is the ILAS 2023 special issue, a fact established after preregistration. Its preface is excluded under the fixed protocol. The stratum must not later be described as an ordinary random issue. The predefined sample is not silently changed to easier-to-access papers.

## 5. Editorial decision and timing

The mathematics provides a negative answer to a proposed complexity strengthening, plus sharp height estimates and exact algorithms. It does not provide a new general polynomial separation paradigm. Our assessment is therefore:

- **LAA:** plausible subject fit for a quantitatively focused obstruction/height paper, contingent on a serious independent priority and proof review. No upper-quintile certification is supported.
- **Mathematical Programming or higher:** no defensible upgrade recommendation from the evidence collected. The fact that the original simplex paper appeared there is not a quality score for this manuscript.
- **Eight-month decision target:** no guarantee. A reported median time to first editorial decision is not a bound on a refereed decision or acceptance.

The official Mathematical Programming homepage displayed 16 days median submission-to-first-decision during this audit. This number includes editorial decisions and must not be translated into a review or acceptance guarantee. A reliable current LAA handling-time figure was not obtained; a lookalike publisher domain surfaced in search and was deliberately not used.

Primary journal page: https://link.springer.com/journal/10107

## 6. Verification limitations and exact completion statement

The proofs are internally checked mathematical arguments. The separate certificate checker has different arithmetic code but was prepared in the same research session: it is not independent human review. No proof-assistant verification occurred. The all-order conclusions do not rest on finite tests.

**Completed:** a rigorous disproof of the specified polynomial adjacent-pivot theorem; sharp universal height results; explicit adjacent and nonlocal algorithms and complexity; complete research manuscript; executable exact certificates; separate results branch.

**Not completed:** independent priority clearance; full-proof ten-paper-per-venue comparison; a defensible 80th-percentile quality certification; external review or submission. Consequently the user's entire flagship success condition is not reported as achieved.
