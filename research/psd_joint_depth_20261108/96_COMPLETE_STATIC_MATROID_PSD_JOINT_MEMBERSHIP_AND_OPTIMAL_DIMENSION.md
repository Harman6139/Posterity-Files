# Milestone 96 — universal all-depth PSD exponent/profile spectra have exact STATIC matroid–conic certificates and terminating optimal-dimension algorithm

**2026-11-08. PROVED for arbitrary real dense PSD measurement maps, any target rank, nullity and minimal facial-reduction profile.** This removes all analytic-center-path quantification and all moving orthogonal flags from the *existential spectrum-membership* problem. It combines the canonical monomial center theorem (89), initial weighted Plücker/strict Slater iff (90), isolated matroid fan denominator bound (91), and canonical maximal-stress facial reduction (01) into one finite **STATIC** necessary-and-sufficient certificate. The result is a complete exact **algebraic/combinatorial decision classification**, not the stronger hoped-for small pure integer parent-edge formula. The strict tied-edge game conjecture remains unproved for all dense kernels.

## Exact setup and finite candidate weights

Fix positive target rank r>=1 and target nullity ν>=1, n=r+ν, N=n(n+1)/2. Let k∈{0,...,N} be a potential measurement kernel dimension. We may assume without loss of attainability generality that
\[
X_*=\mathrm{diag}(I_r,0_\nu),\qquad
\mathcal L=P_{K^\perp}
\]
for some k-dimensional linear subspace K⊂S^n: an invertible constant congruence normalizes the support of any PSD target to identity, and equivalent norms and injective changes of measurement coordinates preserve the sharp exponent and minimal facial-reduction chain. Likewise, since K itself is existentially chosen, one may **absorb the constant orthogonal Q of the canonical center flag into K** using a block-diagonal support-preserving rotation. Therefore **Q=I** suffices in the universal *attainability* search.

For k>=1, the bound in checkpoint91 gives a fully explicit integer
\[
\boxed{D_{n,r,k}=(2k\nu)^{\nu-1}}
\]
such that every canonical null-weight vector admits a common denominator ≤D. Enumerate all weakly increasing rational ν-tuples
\[
0<\theta_1\le\cdots\le\theta_\nu\le1,
\qquad \theta_i\in\{p/q:1\le p\le q\le D\}.
\tag{1}
\]
(If k=0, only the injective Lipschitz case occurs.) These are FINITELY many candidate weight vectors, and every truly attainable uniquely solvable PSD instance has at least one candidate after a constant nullspace rotation.

## Static certificate for a fixed proposed sharp exponent α and exact profile s

Fix a proposed rational 0<α≤1 and a positive rank-drop composition
\[
s=(s_1,\ldots,s_d),\qquad\sum_js_j=\nu.
\]
An exact certificate consists of:

1. An N×k real matrix A of full column rank, interpreted as a basis of K in the fixed symmetric-coordinate basis. Each entry is a finite real unknown, not a Puiseux series.

2. A choice of rational weight tuple θ from (1), with zero support weights on indices 1,...,r. Give symmetric coordinate e=(i,j) the rational weight η_e=(θ_i+θ_j)/2.

3. The finite weighted **initial Plücker subspace** K0: compute every k-minor p_I=det A_I, let M=max_{p_I≠0}Σ_(e∈I)η_e, and define the initial Plücker coordinates p_I^(0)=p_I on maximizing bases and zero on others. These determine an exact k-plane K0 by checkpoint90. All choices of which minors vanish and which maximize are FINITELY disjunctive cases with polynomial equalities/inequalities in A.

4. Two STRICT conic Slater witnesses:
\[
\exists H_0\in K_0:\quad B_0+H_0\succ0,\qquad
\exists W_0\succ0:\quad W_0\perp K_0,
\tag{2}
\]
where \(B_0=P_U+\sum_{\theta_i=1}E_{r+i,r+i}\). These are finite semidefinite feasibility tests with polynomial principal-minor strict inequalities. By the universal iff theorem (checkpoint90), they say **exactly** that θ is the central maxdet monomial weight vector for K.

5. The exact **weighted kernel rank threshold**:
\[
\boxed{
\min\{u:\operatorname{rank}A_{\{e:\eta_e>u\},:}<k\}=\alpha
}
\tag{3}
\]
for k>=1. The minimum ranges over at most N rational half-sums and can be tested by finitely many polynomial minors; checkpoint89 proves it equals the sharp full Frobenius exponent against ALL ambient PSD competitors. For k=0, α=1.

6. The canonical maximal PSD **facial-reduction rank profile** s. Introduce symmetric orthogonal face projectors \(P_0=I,P_1,\ldots,P_d=P_U\) and full ambient exposing stresses \(Z_j\in K^\perp\). Require
\[
P_j^2=P_j=P_j^\top,\quad P_jP_{j-1}=P_j,\quad
\operatorname{tr}(P_{j-1}-P_j)=s_j,
\]
\[
S_j=P_{j-1}Z_jP_{j-1}\succeq0,\quad
S_jP_j=0,\quad S_j+P_j+(I-P_{j-1})\succ0,
\quad\langle Z_j,X_*\rangle=0.
\tag{4}
\]
These guarantee that each step exposes *exactly* the prescribed coordinate face drop. Enforce CANONICAL MAXIMALITY by the finite universal quantified implication: for every symmetric Z∈K⊥ with \(P_{j-1}ZP_{j-1}\succeq0\) and \(\langle Z,X_*\rangle=0\), its face compression annihilates P_j:
\[
P_jP_{j-1}ZP_{j-1}P_j=0.
\tag{5}
\]
Since the compressed matrices are PSD, this means no alternative stress can expose any additional direction at that stage. The standard maximal-rank greedy facial reduction theorem (checkpoint01) proves that this yields the MINIMAL singularity degree and exact canonical rank-drop profile s.

7. Support-space injectivity \(\ker L\cap S(U)=\{0\}\), expressed by full rank of the coordinate restriction of the kernel projector onto S(U), or the equivalent polynomial linear-independence condition. Along with the actual exposing chain to U, this proves X* is the UNIQUE PSD solution.

### THEOREM — complete static necessity and sufficiency

For every fixed (n,r,s,α), α is the sharp PSD recovery exponent of some uniquely solvable real linear inverse problem with rank-r target, nullity ν, and **exact minimal facial rank-drop profile s**, **IF AND ONLY IF** one of the finitely many weight choices (1) admits a real solution of the static polynomial/rank/PSD conditions (2)–(7).

**Proof of necessity:** Normalize X* by congruence and choose the orthogonal canonical weight basis from checkpoint89; absorb its rotation into K since the existence search ranges over all kernels. The observed weight vector lies in (1) by checkpoint91, its initial K0 and B0 satisfy strict Slater (checkpoint90), its sharp exponent equals rank threshold (checkpoint89), and the canonical maximum-rank facial chain yields the exact rank-drop projectors/stresses (checkpoint01). Uniqueness implies support-injectivity. Thus the static certificate exists.

**Proof of sufficiency:** Given A and θ satisfying (2), checkpoint90 gives a positive-definite canonical center normalized by the stipulated Dε; checkpoint89/86 gives exact sharp exponent equal to the rank threshold (3). The facial chain (4) and maximality (5) enforce minimal degree/profile s, while support-injectivity (7) makes the PSD fibre unique. Choosing L=P_(K⊥) realizes the desired problem. There are no missing limits, quantified recovery curves or conjectural graph reductions. QED.

## Fully terminating optimal-dimension computation for EVERY (r,d,α) in the dimension-free spectrum

The previously proved unrestricted-dimension theorem (checkpoint85) gives a **complete list** of rational exponents achievable at each degree:
- d=1: {1,1/2};
- d=2: Q∩[1/4,1/2];
- d>=3: Q∩[2^(−d),1/2).

For any such rational α and target rank r, checkpoint85 also gives an **explicit finite dimension upper bound** ν0(r,d,α), by a dyadic-spine-plus-grid base gadget, an optional high-depth helper and source gluing. The upper bound may be large and is NOT claimed optimal.

To compute the **EXACT optimal nullity and matrix order** for the given (r,d,α):
1. Set ν=d,d+1,...,ν0 successively.
2. For each ν, enumerate every positive composition s of ν of length d and the finitely many candidate rational weights (1), with k ranging from zero to N.
3. Decide the static real-algebraic certificate (2)–(7) using standard exact real-closed-field quantifier elimination (strict positive definiteness by principal minors).
4. The FIRST ν with a true sentence is the exact optimal nullity; the optimal matrix order is \(n_{\min}=r+\nu\).

This procedure **always terminates** because the source-glued construction at ν0 is feasible. A true certificate is an explicit realizing PSD measurement kernel; a false certificate at each smaller ν is a rigorous impossibility result. This computes exact optimal dimension for every rational α and prescribed minimal degree d, albeit not as a short closed arithmetic formula.

The same finite process at fixed ν enumerates the COMPLETE all-degree joint spectrum \(\Sigma_{n,r,d}\), via candidate rational α with reduced denominator ≤2(2Nν)^(ν−1) and profiles s of length d. Its completeness follows from the strict central monomial and matroid fan theorems, independently of any dense-to-tied-game conjecture.

## Interpretation: what is and is not "combinatorial"

This is a **completely finite signed matroid + SDP face-tower classification** for arbitrary dense PSD recovery. Its finite indices are rational weight vertices, maximal Plücker bases, coordinate rank patterns and exposing-rank profiles. The continuous part consists of real coefficients of a realizable signed Plücker matrix and strict PSD feasibility tests, decided by real quantifier elimination. It is therefore **algorithmic and algebraic**, not a compact purely integer parent-graph formula.

Checkpoints75 and87–88 show that earlier independent-edge two-policy models fail and that *leading Dikin/tropical data alone* cannot recover depth. The full finite signed Plücker jet of checkpoint92 exactly retains the additional subleading data needed. Whether all numerical (α,s) pairs can be realized by the smaller tied-edge Shapley-game class remains an OPEN *compression theorem*; the present static certificate is a proved universal fallback without conjectural reductions.

## Boundary audit

- If ν=0 (positive definite target), uniqueness forces K=0, exponent1 and facial degree0. This case is outside the stated ν>=1 certificate.
- If k=0 and ν>=1, the exact exponent is1 and a full null-support stress exposes all ν directions in one step, so d=1 with profile (ν).
- If target rank zero, unique zero target plus K∩PSD={0} gives exponent1 and first full exposing stress; treat separately.
- Strict versus nonstrict inequalities must be preserved: the primal/dual initial tests require PD, not merely PSD, as shown in checkpoint90.
- This certificate's reliability depends on the universal monomial-center, Plücker fan and Dikin modulus theorems (checkpoints09–12 and 86–91), all of which have self-contained mathematical proofs in the branch but have not been independently refereed for publication.

## Priority/novelty discipline

Real-closed-field QE, Grassmannian initial degenerations, PSD Slater, Dikin analytic centers and facial reduction are established prior methods. No novelty claim is made for those ingredients. The claimed mathematical combination is an explicit static *necessary and sufficient* structural theorem and exact optimal-dimension algorithm; an external expert should audit its load-bearing proofs before publishing it as new theory.
