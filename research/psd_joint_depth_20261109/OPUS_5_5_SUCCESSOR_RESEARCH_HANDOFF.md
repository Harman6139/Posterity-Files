# HANDOFF TO OPUS 5.5 — PSD Hölder exponent / facial-depth UNIVERSAL CLASSIFICATION

**Prepared:** 2026-11-09
**Repository:** Harman6139/Posterity-Files
**Research branch (all work, numbered milestones 01–127):** `research/psd-joint-depth-universal-20261107`
**Research index:** `research/psd_joint_depth_20261107/README.md`
**Project-lead index:** `research/psd_joint_depth_20261107/PROJECT_LEAD_START_HERE.md`
**First-day checkpoint directory:** `research/psd_joint_depth_20261107/`
**Second-day checkpoint directory:** `research/psd_joint_depth_20261108/`
**Latest directory:** `research/psd_joint_depth_20261109/`
**Original stand-alone conversation attachments:** `research/psd_joint_depth_20261107/ORIGINAL_CHAT_ATTACHMENTS/` (see manifest for included exact snapshots).
**Visibility at handoff:** GitHub reported the repository PRIVATE. The connector in this conversation can commit files, but has NO repository-visibility mutation endpoint. Do NOT tell the project lead it is public. The owner must change visibility via GitHub Settings or make a scoped public copy, after inspecting other repository material.

## I. The EXACT user research question

For every real linear map L:S^n→R^m, uniquely recovered PSD target X*≽0 with rank r≥1, nullity ν=n-r, define the sharp full ambient recovery modulus

\[
\omega(\delta)=\sup\{\|X-X_*\|_F:X\succeq0,\;\|L(X-X_*)\|\le\delta\}=\Theta(\delta^\alpha)
\]

for small δ. Let d be the **minimal** singularity degree of semidefinite facial reduction to the face supported on range(X*), not an arbitrarily selected exposing-chain length.

**Strong target:** a compact, explicit, NECESSARY-AND-SUFFICIENT purely combinatorial/arithmetic formula for ALL feasible tuples (n,r,d,α), including exact smallest possible nullity/dimension for prescribed d and α, for **arbitrary dense** kernels K=ker L. Alternatively rigorously refute a proposed simple formula and derive the smallest richer correct model. A terminating quantifier-elimination test counts only as an effective analytic classifier, NOT the requested closed combinatorial spectrum.

No theorem should be announced as proved unless every direction and full ambient PSD competitor bound are valid. A numerical exhaustive check for ν≤7 is evidence for an all-ν statement, not a proof for all ν.

## II. Most promising conjectural CLOSED all-nullity formula

Every actual dense instance has canonical maxdet valuation grades 0=w0<w1<...<wk=1, k≤ν, with each internal grade harmonic:

\[
2w_i=w_{a_i}+w_{b_i},\qquad 0\le a_i<i<b_i\le k.
\]

Sharp non-Lipschitz α is an admissible half-weight \(\alpha=w_v/2\le w_1\). Let \(L(w)\) and \(U(w)\) be the following **two canonical grade-peeling recurrences** (proven necessary for actual dense kernels in Milestone 99):

Start with j=k, first move k→k-1. At any later j≥1 set
\[
\ell(j)=\#\{1\le i<j:2w_i<w_{j+1}\},\qquad
p(j)=\min\{1\le p\le j:2w_p>w_j+w_{p-1}\}.
\]
For L choose j→\(\ell(j)\); for U choose j→\(p(j)-1\). Stop at j=0 and count transitions.

For exact degree d, the universal NECESSARY conditions include
\[
\boxed{\;2^{-d}\le\alpha=w_v/2\le w_1,\qquad L(w)\le d\le U(w)\le k\le\nu.\;}
\]

**Frontier conjecture (degree-only):** Those finite rational harmonic conditions, plus α=1 at d=1 and standard boundary cases, are SUFFICIENT at the original target nullity ν for arbitrary prescribed positive target rank r. If true, the all-n candidate spectrum is obtained by enumerating harmonic graphs with h=k-1≤ν-1 internal vertices, allowing grade multiplicities/padding up to ν, and checking only the displayed rational integer inequalities.

**IMPORTANT:** This sufficiency has NOT been proved. At the stronger **rank-profile/individual schedule** level it is false that every feasible-looking prefix schedule can be realized with the same grade weights (Milestone 125).

## III. Established research claims: what to READ first

1. **Core analytic method:** 09/10/12 (Loewner center, universal Dikin–Hessian modulus, determinant ratio), 37 (exterior-minor valuations), 89 (fixed monomial maxdet chart for dense K), 91 (dense-to-harmonic *exponent-only* construction), 93/94 (full Dikin spectral orders via matroid rank).
2. **Universal necessity:** 99 (the ORIGINAL dense-kernel dual/primal integer peeling bounds), 95 (dual two-step threshold), 122 (graded initial PSD cones split by valuation grade; rank criterion for simple grades).
3. **FULL maximal-depth:** 90 and 72 (dense d=ν claimed complete; bounded primitive nondecreasing integer-gap harmonic formula; nonreciprocal ν≥6 examples in 68/70).
4. **Dimension-preserving proven ENDPOINT constructions:** **114** (every harmonic halfweight α realizes d=L(w) at rank-one EXACT nullity, including the last leading-edge collision); **123** (every harmonic halfweight α realizes d=U(w) at rank-one EXACT nullity, via one globally unique edge per generator and two-child positive diagonal couplings).
5. **Whole interval with DIMENSION OVERHEAD:** **110** (for every w and every integer d in [L(w),U(w)], a tied + safe-action construction realizes the exact exponent/depth at nullity ≤3(k-1)+1; 111 exact checks). **This does not prove fixed-nullity sufficiency.**
6. **Small exact strata:** 41 (ν≤4), 100 (ν=5), 103 (ν=6), 105 (ν=7; 106 exact C++ audit). These are self-described computer-assisted classifications and need fresh independent reruns. Counts at ν=7, for d=1..7: 2,325,857,817,596,321,117.
7. **Dimension-free projection:** 85 claims exact degree-only spectrum with unbounded dimension: d1 {1,1/2}, d2 Q∩[1/4,1/2], d≥3 Q∩[2^{-d},1/2).
8. **Analytic all-n fallback:** **119** (graded-conic initial dual separation + thick near-feasible primal ⇔ center monomial Loewner chart), **120** (finite harmonic/matroid/conic-stress semialgebraic all-n iff membership certificate; Q.E. remains), **127** (exact projected-positive-circuit iff for a proposed facial exposing block).

**CRITICAL audit disclaimer:** The branch contains ~127 numbered mathematical checkpoints written rapidly in research sessions. They have **NOT** been independently referee-verified. The checkpoint titles 'PROVED' describe internal claims, not external certification. Review load-bearing arguments before building a journal proof.

## IV. Counterexamples / false shortcuts — DO NOT REPEAT

- **58:** one-action midpoint-graph degree universality FALSE: explicit ν5,d4,α=7/32 requires extra Bellman-slack action; 66 extends infinitely.
- **75:** independent-edge TWO-policy degree universality FALSE: ν5,d3,α=3/22 tied-edge generator with two physical edges; check 76. A second tied example ν5,d3,α=3/20 in 96.
- **116/118/121:** naïvely SHARING a physical offdiagonal edge between distinct generators can introduce a positive *graded initial kernel circuit*, MERGE Dikin valuation grades and WORSEN the sharp exponent (example changes intended 1/6 to actual 1/7). In 121 the exact difference of two generators yields a rank-one PSD graded initial direction. Merely checking each added edge's Bellman safety is INSUFFICIENT. **Erratum:** the displayed weights in 116 have L=U=4, NOT L=3,U=4; the corrected file says so.
- **107/108:** one permissible action may jump minimum facial depth by TWO steps. Induction by "one edge -> one new degree" is FALSE.
- **125/126 and 127:** at ν=6, w=(0,1/4,3/7,1/2,17/28,5/7,1), the specific schedule {6},{4,5},{2,3},{1} is impossible for ANY dense kernel with that canonical grade-aligned flag, by a two-coefficient/single-offface-entry dual bottleneck. A DIFFERENT schedule {6},{5},{2,3,4},{1} realizes the SAME weights, α=1/4 and d=4. Thus proving that *every schedule* is realizable is stronger than needed and FALSE.
- **87/88:** a pair of ν5 PSD kernels have identical leading canonical center AND full restricted Dikin–Hessian valuation spectra, but d=3 vs d=4. Hence scalar weights and the valuation matroid alone do NOT encode exact degree. The signed face-compression tower is essential.
- **63/65:** entrywise signs and all principal-minor signs through any fixed bounded order cannot classify arbitrary dense stability/depth.

## V. The TWO requested research routes — current honest assessment

### ROUTE A — Dimension-preserving POSITIVE-CIRCUIT elimination / intermediate schedule construction

**What succeeded:** endpoints L(w) and U(w) at exact nullity (114,123); all intermediate depths with ≤linear nullity overhead (110); finite examples ν≤7. The innovative 123 mechanism transfers a duplicate safe edge to its tight generator as a **second positive child diagonal**, so the physical edge appears in only one generator and cannot cancel.

**What failed:** every arbitrary proposed prefix exposure schedule is NOT geometrically feasible (125/127); a blind identification of cloned edges can change the Dikin exponent (116/118/121); one-edge monotone interpolation is false (107). Any proof must select **one compatible** schedule for each target depth, not preserve every schedule.

**Next explicit target:** Construct, for every harmonic w and integer L(w)<d<U(w), a fixed-nullity kernel whose physical parent edges are distinct and whose generator diagonal-child sets encode a compatible prefix schedule, possibly moving children between layers. The L/U endpoint construction uses singleton/two-child diagonal supports; investigate whether *controlled multi-child diagonal generators* plus tied release edges can realize a suitable intermediate schedule while passing both (1) graded conic separation (119/122), and (2) every intended compressed face positive circuit test (127).

Try a general combinatorial "schedule selection + edge/circuit ownership" lemma. Test it first against the ν6 schedule obstruction of 125 and find the alternate schedule automatically. If the lemma fails, generate an explicit (ν,d,α) candidate that satisfies harmonic L≤d≤U but cannot be realized by ANY dense kernel, using the full signed-conic test 120.

### ROUTE B — Signed conic-matroid tower ELIMINATION

119 gives the correct *primal chart* iff:
\[
\mathcal I_\theta(K)\cap\mathbb S_+^n=\{0\}
\quad\text{and a thick grade-positive near-feasible primal arc exists.}
\]
120 gives a finite real-algebraic necessary/sufficient kernel+stress certificate for exact d; 122 reduces the graded PSD positivity test to ordinary rank conditions for **simple one-dimensional grades**; 127 localizes facial step feasibility as
\[
Q_{F,C}:=P_C(K\cap\mathbb S(F))P_C,\qquad
C\text{ exposable}\iff Q_{F,C}\cap\mathbb S_+(C)=\{0\}.
\]

**Next explicit target:** remove real-conic feasibility and characterize the *entire nested face-compression positive circuit tower* by finitely many discrete oriented-matroid/gammoid-style axioms, with realization at original nullity. If rank/flag arithmetic alone is insufficient, find a minimal signed/determinantal counterexample and define the smallest richer model that actually distinguishes it. If real-conic feasibility is genuinely indispensable, state that as a rigorous limitation (do not claim a graph-only formula).

### Why a full proof remains OPEN

Both routes require one missing uniform constructive/structural theorem. An EFFECTIVE all-n semi-algebraic membership decision criterion in 120 is NOT equivalent to the desired explicit graph-only arithmetic spectrum or exact optimal nullity function. Numerical verification through ν7 does not close this.

## VI. Mandatory successor research / validation workflow

1. Read milestone 123, 114, 99, 110, 125, 127, 119/120, then review essential 89/91 Dikin claims. Work from actual generator matrices, not informal graph cartoons.
2. Independently RUN the committed audit programs (if possible): 104 (Python exact ν6), 106 (C++ Boost ν7), 111 (all schedule path checks), 115 (rank-one collisions), 117 (shared-edge lock), 124 (clone-free upper), 126 (forbidden aligned schedule).
3. Check potential proof flaws and update with explicit ERRATA. In particular, check all cases where a compression-annihilator stress is lifted and where a generator's off-face entries influence other stages. Check the P1/P2 prime assumptions of the original harmonic/center lemmas. A finite test or broad "positive rebalancing" invocation is not a substitute for the exact PSD inequalities.
4. Pursue Route A and Route B fully. Either produce a complete self-contained all-ν proof and exact optimal-dimension formula; OR produce a rigorous counterexample and the next correct richer complete model; OR, if both approaches genuinely stall, document the failed lemmas and explicit surviving gap. Do NOT make unsupported claims of solvability or impossibility.
5. SAVE EVERY VERIFIED MILESTONE on the SAME branch `research/psd-joint-depth-universal-20261107` under `research/psd_joint_depth_20261109/` as next numbered `NN_TOPIC.md` with scripts nearby. Append verified status and **counterexamples/errata** to `research/psd_joint_depth_20261107/README.md` and the project-lead handoff.
6. When reporting to the user and PL, distinguish PROVED (subject to audit), CONDITIONAL, COMPUTATION, COUNTEREXAMPLE, and OPEN. Cite commit hashes for immutable review.

## VII. Compact ready-to-paste prompt for Opus 5.5

> You are assigned the final frontier of the LAA PSD sharp stability project. Connected GitHub repo Harman6139/Posterity-Files, branch research/psd-joint-depth-universal-20261107, file research/psd_joint_depth_20261109/OPUS_5_5_SUCCESSOR_RESEARCH_HANDOFF.md (READ ALL). The goal is a complete compact purely combinatorial/arithmetic classification of attainable (n,r,d,alpha) with exact minimum dimension for uniquely solvable arbitrary DENSE PSD inverse problems. A uniform effective QE/matroid/conic membership certificate already exists (120); this does NOT solve the stronger goal. The universal finite harmonic necessary condition is alpha=w_v/2<=w1, 2^{-d}<=alpha, L(w)<=d<=U(w). BOTH endpoint depths L(w) and U(w) are constructively realized at EXACT original nullity for every harmonic w/alpha (114,123). EVERY intermediate depth is realized with linear nullity overhead (110). The missing problem is dimension-preserving INTERMEDIATE depths or a counterexample/additional criterion. Crucially some SPECIFIC intermediate face schedules are impossible even for dense kernels (125,127), though alternate schedules at same exponent/degree exist. Shared physical parent edges can merge canonical Dikin grades and alter alpha (116,118,121). Route A: positivity-preserving signed circuit/edge-ownership construction selecting at least one compatible schedule per permitted depth. Route B: eliminate graded cone and nested face positivity from 119/120/122/127 into a finite discrete signed-conic matroid tower. Pursue BOTH seriously, independently audit load-bearing proofs, and COMMIT EVERY verified milestone to the SAME branch and master README. If full theorem cannot be proved, provide rigorous obstruction and final researcher/project-lead handoff without pretending to have solved it.

## VIII. Privacy/visibility and transfer

The current source repository is PRIVATE and contains other work, not solely this research lane. **Making the entire repository public would expose ALL files, branches and reachable commit history**. The linked GitHub app connector does not offer a visibility-changing action. A safe alternative is to make a NEW public repository containing only the three research folders above and the original chat attachment archive, after inspecting for confidential data. Or grant the successor researcher collaborator access to the private repo.

### Archival caveat

Older one-off generated chat attachments may not all be represented verbatim in the original numbered checkpoints. The archive under ORIGINAL_CHAT_ATTACHMENTS is intended to preserve these historical originals separately, so the next researcher can compare the first formulations and later corrected checkpoint proofs. The old files are research data, NOT proof that every claim in them is valid.
