# Milestone 114 — COMPLETE exact-nullity, RANK-ONE realization at the primal peeling LOWER endpoint for EVERY harmonic half-weight

**2026-11-09. PROVED for every strict rational harmonic midpoint system, at arbitrary finite nullity.** This closes the only previously unresolved *rank-one leading-edge collision* in checkpoint 112. All conclusions concern the **actual full PSD inverse problem and its minimal facial reduction**, not merely an abstract graph. The independent exact-rational audit in checkpoint 115 verifies **all 933 collision instances** among the 5,269 valid strict leading-halfweight inputs through five internal vertices.

## Theorem — no cloning or additional positive support required

Let h>=1, k=h+1 and let
\[
0=w_0<w_1<\cdots<w_h<w_k=1,\qquad
2w_i=w_{a_i}+w_{b_i},\quad0\le a_i<i<b_i\le k
\]
be ANY strict rational harmonic network (one genuine tight parent pair P_i=(a_i,b_i) per internal vertex). Choose ANY valid distinguished exact recovery exponent
\[
\alpha=w_v/2\le w_1,\qquad 1\le v\le k.
\]
Let \(L(w)\) be the original-kernel primal forced-peeling integer recurrence of milestone 99: start with k→k−1, then at prefix j remove the suffix after
\[
\ell(j)=\#\{1\le i<j:2w_i<w_{j+1}\}.
\]

**Then there exists an explicit rational linear PSD inverse problem on \(\mathbb S^{k+1}\)**, with target \(X_*=E_{00}\) of **rank exactly one, nullity exactly k**, such that its *sharp full ambient Frobenius recovery exponent* is **exactly α** and its **MINIMAL facial reduction degree is exactly L(w)**.

Fully measured positive support padding supplies every prescribed target rank r>=1 at EXACT SAME nullity k, without changing either invariant.

Thus the LOWER endpoint of the universal primal/dual weight-based peeling interval is **dimension-preservingly sufficient for EVERY valid halfweight and EVERY rank**, not merely α=w1 or r≥2 as in checkpoint 112.

## I. Recall the original shared-release construction (checkpoint 112)

Write the fastest prefix schedule
\[
k=j_0>j_1=k-1>\cdots>j_d=0,\qquad d=L(w),\quad
j_t=\ell(j_{t-1})\ (t\ge2),
\]
with layers \(C_t=\{j_t+1,\ldots,j_{t-1}\}\).
For t>=2, let
\[
b_t=j_{t-1}+1,\qquad f_t=(0,b_t).
\]
Each child i∈C_t has \(w_{b_t}\le2w_i\), so the release edge f_t is no larger than its harmonic coefficient order w_i.

With small rational λ, start from the kernel generators
\[
H_i=E_{ii}-E_{00}+
  \lambda F_{P_i}+
  \begin{cases}\lambda F_{f_{t(i)}}&f_{t(i)}\ne P_i,\\
                 0&f_{t(i)}=P_i,\end{cases}
\tag{114.1}
\]
where t(i) is the layer of vertex i. Several generators may share a release edge. The tight anchors P_i are pairwise distinct. Whenever an anchor P_i is also a different generator's release edge f_t, that other generator has strictly *higher* harmonic weight w_j>w_i. Thus the anchor inequalities are upper triangular in the generator coefficients and force \(x_i=O(\delta^{w_i})\) against every PSD residual-δ competitor, by the weighted maximum principle in checkpoint 112.

The monomial curve \(X_*=E_{00}+\sum_i z^{w_i}H_i+zE_{kk}\) is full-PD for small z after diagonal normalization (take λ small) and has residual Θ(z), displacement Θ(z^{w1}). The original explicit exposing stresses for t>=2 are
\[
Z_t=\sum_{i\in C_t}E_{ii}-\frac1{2\lambda}F_{0,b_t},
\tag{114.2}
\]
which are orthogonal to every H_i and have PSD face compression exposing exactly C_t. Along with Z1=Ekk this establishes exact degree L(w), by the direct original-kernel forced-peeling lower bound.

For α<w1 add the independent G=λF_(0,v), giving a matching leading displacement Θ(z^α) and global recovery exponent α. If its edge (0,v) does NOT equal any f_t, (114.2) is also orthogonal to G and the theorem follows immediately from checkpoint 112. The only remaining case is a collision.

## II. The collision can occur ONLY at the LAST exposing step

Assume α=w_v/2<w1 and (0,v)=f_t for some stage t>=2. Since α<w1, we have
\[
w_v<2w_1.
\tag{114.3}
\]
But v=b_t=j_(t-1)+1 and the next fastest transition satisfies
\[
j_t=\#\{1\le i<j_{t-1}:2w_i<w_{j_{t-1}+1}=w_v\}.
\]
Because \(2w_1>w_v\), this count equals ZERO. Consequently \(j_t=0\), so **t=d is the final step** and
\[
\boxed{v=b_d=j_{d-1}+1.}
\tag{114.4}
\]
No other release edge can equal G; the b_t indices strictly decrease with t.

Thus all earlier exposing layers and all their release edges are unaffected. Only the final layer \(C_d=\{1,\ldots,j\}\), j=v−1, must be handled differently.

## III. Modify ONLY the last-layer generators: omit the forbidden release edge

For every i∈C_d, use only its TIGHT harmonic anchor:
\[
\boxed{H_i=E_{ii}-E_{00}+\lambda F_{P_i},\quad i\le j.}
\tag{114.5}
\]
For i>j retain the shared-release generators (114.1) from checkpoint 112. Add G=λF_(0,v).

**A. Full recovery exponent remains exactly α.** Every H_i still has the same positive diagonal and all its offdiagonal entries satisfy the weight-order inequality \(w_a+w_b\le2w_i\); the new generators have FEWER terms than before. Anchor edges remain pairwise distinct and their possible interference from other generators' release edges remains strictly triangular from higher-grade variables. Thus the checkpoint-112 global PSD principal-minor/weighted maximum-principle proof applies unchanged, showing all internal diagonal variables are \(O(\delta^{w_i})\) and the independent leading variable is \(O(\delta^{w_v/2})\). The normalized monomial curve with x_i=z^{w_i} and leading G coefficient z^α is strictly PD for small λ, giving matching residual Θ(z) and displacement Θ(z^α).

**B. All EARLIER exposing stresses remain valid.** For every stage s<d the original stress (114.2) has its ONLY offdiagonal at f_s≠f_d=(0,v), so removing f_d from the generators H_i of the final layer does not change any of its pairings. It is also orthogonal to G, because f_s≠(0,v). The terminal stress Z1=Ekk is unchanged. Hence the first d−1 desired layers remain exposable in the same order.

## IV. New exact FINAL stress, with a PD non-diagonal compression

After d−1 stages the remaining coordinate face is
\[
W_j=\operatorname{span}\{e_0,e_1,\ldots,e_j\},\qquad j=v-1.
\]
Choose positive numbers z_1,...,z_j and define a full symmetric matrix Z by:
- Z_00=0, Z_ii=z_i>0 (1≤i≤j), Z_ll=0 (l>j);
- for EACH tight anchor P_i=(a_i,b_i), 1≤i≤j, set
  \[
  \boxed{Z_{a_i b_i}=Z_{b_i a_i}=-z_i/(2\lambda);}
  \tag{114.6}
  \]
- all other entries zero.

The tight P_i edges are pairwise DISTINCT, so (114.6) is well defined.

**Lemma 1: every active anchor is wholly inside the final exposed null block, never touching the source.** If \(b_i\le j=v-1\) and \(a_i=0\), harmonicity gives \(w_{b_i}=2w_i\ge2w_1>w_v\), contradicting b_i<v. Hence \(a_i\ge1\). Since 1≤a_i<i<b_i≤j, both active endpoints lie in \(\{1,\ldots,j\}=C_d\). Any anchor with b_i≥v is OFF-FACE and poses no PSD restriction.

**Lemma 2: Z is orthogonal to the ENTIRE original kernel, including G.**
- For final-layer generators \(H_i\), i≤j, the diagonal contributes z_i, and their single anchor contributes \(2\lambda Z_{a_i b_i}=-z_i\); their source diagonal pairs to Z00=0. Hence <Z,H_i>=0.
- Every earlier-exposed generator H_l, l>j, has zero diagonal pairing. Its tight anchor P_l cannot equal any P_i with i≤j (strict harmonic edge uniqueness). Its release edge f_s=(0,b_s) for some earlier stage s<d cannot equal any P_i with i≤j: because final i survives stage s, it satisfies \(i\le j_s=\ell(j_{s-1})\), implying \(2w_i<w_{j_{s-1}+1}=w_{b_s}\). But P_i=(0,b_s) would imply \(2w_i=w_{b_s}\). Therefore NO earlier release edge occurs in Z's support, and <Z,H_l>=0.
- The independent leading edge G=(0,v) is not a tight P_i at any i≤j, because a harmonic P_i=(0,v) would imply \(w_i=w_v/2=\alpha<w_1\), impossible. Thus \(Z_{0v}=0\), so <Z,G>=0.
Therefore \(Z\in K^\perp\) exactly, even though it contains numerous off-face entries.

**Lemma 3: the compression of Z to the final face W_j is PSD and PD on ALL remaining null coordinates.** Pick
\[
z_i=e^{\sigma w_i^2}
\]
for one sufficiently large fixed σ. The only nonzero offdiagonal entries INSIDE W_j are the active tight harmonic edges P_i=(a_i,b_i) from Lemma 1. After congruence by \(\operatorname{diag}(z_1^{-1/2},\ldots,z_j^{-1/2})\) on the null block, each active edge has normalized magnitude
\[
\frac{z_i}{2\lambda\sqrt{z_{a_i}z_{b_i}}}
=\frac1{2\lambda}
  \exp\left(-\frac\sigma4(w_{a_i}-w_{b_i})^2\right)
\longrightarrow0.
\tag{114.7}
\]
The limit is the identity on the null block. Strict diagonal dominance holds for sufficiently large σ. Since **no active anchor touches e0**, the source row and column of the compressed stress vanish. Thus
\[
P_{W_j}ZP_{W_j}\succeq0
\quad\text{and is PD on }\operatorname{span}\{e_1,\ldots,e_j\}.
\]
Choosing σ as a sufficiently large rational multiple of a common rational-square denominator (or taking integer powers of a sufficiently large rational base) makes every z_i and Z entry rational if desired.

Hence this SINGLE legitimate original measurement stress exposes the ENTIRE last remaining null face. Together with the d−1 earlier stresses, it gives a valid length-d facial-reduction chain.

## V. Minimality and exact nullity

All generators H_i, including the modified final ones, have:
1. \((H_i)_{ii}=1>0\);
2. no nonzero entry on a pair of harmonic weights whose sum exceeds 2w_i.
The independent leading G has **no** diagonal and does not affect stress annihilation of the forced internal rows. Therefore the original-kernel triangular stress-annihilation argument in checkpoint 112 (or the full blockwise forced peeling in checkpoint 97) applies to THIS K: every facial-reduction chain must survive at least L(w) steps.

We have already constructed d=L(w) valid steps, so **the MINIMAL singularity degree is exactly L(w)**. Matrix order is k+1 with rank-one target E00, hence target nullity is exactly k; no clone coordinates were added.

For α=w1 or noncolliding G, checkpoint112 applies. The colliding case was proved above, so the theorem holds for EVERY valid halfweight and EVERY h. Fully measured positive support padding raises target rank to arbitrary r≥1 without altering the nullity, sharp exponent or minimum facial degree. QED.

## Exhaustive exact-rational audit and scope

Checkpoint 115 independently enumerates all strict harmonic systems with h=1,...,5 internal vertices (counts 1,3,18,165,2099), and **every** admissible α=w_v/2<w1. There are 5,269 such strict leading-halfweight cases, of which **933 have a source-release collision**, all of them at the final layer. For every instance the audit checks exact original-generator/dual-stress Frobenius pairings at EVERY exposing step, the forbidden G edge, harmonic support inequalities and strict positivity conditions for final active-edge normalization. Every assertion passed.

**This closes the previously open rank-one lower-bound collision at EXACT original nullity.** It does NOT construct the UPPER extreme d=U(w) or every intermediate depth at original nullity; those are only known with bounded clone overhead (checkpoint110). The stronger all-nullity fixed-(ν,d,α) classification is thus NOT proved by this milestone, though its dimension-preserving lower-bound realization half is complete.

Standard PSD facial reduction, harmonic midpoint constructions and coefficient rescaling are prior tools; the new shared-release final-layer repair has a complete mathematical proof but bibliographic novelty has not been audited.