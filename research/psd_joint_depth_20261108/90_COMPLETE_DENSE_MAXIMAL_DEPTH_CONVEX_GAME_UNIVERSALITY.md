# Milestone 90 — COMPLETE dense-to-game universality at MAXIMAL PSD facial depth

**2026-11-08. New universal theorem with self-contained proof**, assuming only the already-proved general analytic-center Loewner envelope, the general fixed monomial maxdet chart (checkpoint 89), elementary conic separation and the already-proved global correctness of explicit harmonic incidence gadgets (checkpoints 57/70/72). The necessity holds for ALL arbitrary dense measurement maps, with no a priori sparsity, weighted-flag-to-midpoint extraction, genericity or selected recovery arc. This **fully resolves the maximal-depth slice** of the joint all-value exponent/depth/dimension classification. It does not claim the fixed-depth d<nullity classification.

## Universal theorem

Fix positive target rank r>=1, nullity nu=n−r>=2, and suppose X*>=0 is the unique PSD point with the measurements of L:S^n→R^m. If the **minimal** facial-reduction degree is MAXIMAL, d=nu, then there exists a STRICT scalar harmonic midpoint graph on one source 0, exactly h=nu−1 internal vertices and one terminal h+1, with:

1. rational weights 0=w0<w1<...<wh<w_(h+1)=1;
2. nondecreasing positive gaps
   w1−w0 <= w2−w1 <= ... <= w_(h+1)−wh;
3. one distinct-parent harmonic relation at every internal vertex
   2w_i=w_(a_i)+w_(b_i), 0<=a_i<i<b_i<=h+1;
4. the actual sharp recovery exponent alpha equals **one of its half weights**, alpha=w_v/2<=w1 for some v=1,...,h+1.

Conversely, EVERY such graph and every valid half weight are realized, at the SAME nullity nu and target rank r, by an explicit uniquely solvable rational PSD inverse problem with exact maximal minimal degree d=nu and sharp full-matrix exponent alpha, against arbitrary ambient PSD competitors.

Thus the arbitrary-dense universal maximal-depth spectrum EQUALS the earlier strict multi-action incidence spectrum, not merely contains it:
\[
\boxed{
\Sigma^{\rm ALL\ DENSE}_{r,\nu,d=\nu}
=
\mathcal C_\nu
=
\bigcup_{g\in\mathcal I_{\nu-1}}
 \left\{\frac{\sum_{j=0}^{v-1}g_j}
 {2\sum_{j=0}^{\nu-1}g_j}:
 1\le v\le\nu,\
 \sum_{j=0}^{v-1}g_j\le 2g_0\right\}.}
\tag{90.1}
\]
The FINITE purely integer set \(\mathcal I_h\) consists of primitive nondecreasing positive gaps g0<=...<=gh with total D<=2^h and, for each internal i, one pair a<i<b satisfying
    sum_(j=a)^(i-1)g_j = sum_(j=i)^(b-1)g_j.
This is the previously proved integer-gap theorem (checkpoint 72), now upgraded from an incidence-family classification to **UNIVERSAL DENSE NECESSITY** at d=nu.

In particular, the first nonreciprocal maximal-depth exponents occur at nullity six: 3/46, 3/23, 2/15. The earlier ν=4 reciprocal-only maximal-depth spectrum and the 7×7 nonreciprocal example are consistent with (90.1).

## Step 1 — the canonical center produces a valid EXPOSING CHAIN along its valuation flag

The shifted maxdet center C_epsilon and its fixed orthogonal monomial Loewner chart (checkpoint 89) give
\[
C_\epsilon=D_\epsilon M_\epsilon D_\epsilon,\quad
D_\epsilon=\bigoplus_{i=0}^k\epsilon^{w_i/2}I_{U_i},
\quad
cI\preceq M_\epsilon\preceq CI,
\]
where U0=range X*, 0=w0<w1<...<wk=1, and k<=nu. The normalized M_epsilon is semialgebraic and bounded above/below by fixed PD matrices, hence it has a finite positive-definite limit \(M_0=\lim_{\epsilon\downarrow0}M_\epsilon\succ0\).

Stationarity implies the positive dual central path
\[
Z_\epsilon=\epsilon C_\epsilon^{-1}
=\epsilon D_\epsilon^{-1}M_\epsilon^{-1}D_\epsilon^{-1}
\in K^\perp\cap S_+^n,\qquad K=\ker L.
\]

For j=k,k−1,...,1, let \(W_j=U_0\oplus\cdots\oplus U_j\). The PSD compression \(P_{W_j}Z_\epsilon P_{W_j}\) has a Puiseux expansion whose **first nonzero coefficient occurs at exponent \(1-w_j\)** and is exactly
\[
P_{U_j}M_0^{-1}P_{U_j}\succ0
\]
supported on U_j: all other entries within W_j have exponent \(1-(w_i+w_\ell)/2>1-w_j\), because i,l<=j and max(w_i,w_l)=w_j only when i=l=j. Every coefficient of Z_epsilon lies in the fixed linear space K^\perp. Therefore the coefficient at exponent \(1-w_j\), call it \(Z_j\in K^\perp\), has a PSD compression to W_j that is PD on U_j and zero on W_(j−1). It is a **valid facial-reduction exposing stress on W_j**.

The sequence W_k⊋W_(k−1)⊋...⊋W_0 is thus an actual exposing chain of length k ending at the minimal target face. Hence the MINIMAL singularity degree obeys d<=k<=nu.

If d=nu, necessarily k=nu and every null valuation block U_i is ONE-dimensional. Choose the unit basis e1,...,e_nu of these grades, in increasing order of weight. The maximal-depth exposing chain is necessarily
\[
U+\operatorname{span}(e_1,\ldots,e_\nu)
\supsetneq \cdots\supsetneq U+\operatorname{span}(e_1)
\supsetneq U.
\tag{90.2}
\]
We have rigorously aligned the *actual dense canonical-center valuation basis* with an exact maximal-depth facial flag **without assuming this alignment**.

## Step 2 — a universal downshift obstruction (the key tool)

Use the Puiseux expansion
\[
C_\epsilon=X_*+\sum_{e>0}A_e\epsilon^e,\qquad
A_e\in K\ (e<1),\quad A_1-I\in K.
\]
The coefficient rescaling lemma from checkpoint 89 says that a finite list of matrices whose blocks satisfy
\[
(H_e)_{ab}=0\quad\text{when }w_a+w_b>2e
\]
and whose earliest positive diagonal coefficients lie at specified weights can be multiplied by fixed factors exp(σe²) to make a **full positive-definite** polynomial curve. Its measurement residual is O(epsilon) as long as every coefficient below e=1 belongs to K.

**Downshift principle.** Suppose one of the internal weights w_i can be replaced by w'_i<w_i, preserving strict order, and there exists an actual H∈K with H_ii>0 such that the entire block support of H obeys
\[
w'_a+w'_b\le 2w'_i
\quad\text{for every nonzero H_(a,b),}
\tag{90.3}
\]
where all other weights stay fixed. Then the curve made from the actual center's truncation through exponent one PLUS H ε^{w'_i}, with coefficient rescaling, is PD for small ε and has residual O(epsilon). Its i-th diagonal is Θ(epsilon^{w'_i}), whereas the canonical center's i-th diagonal is Θ(epsilon^{w_i}). The universal analytic-center Loewner envelope \(Y_\epsilon\preceq C'C_\epsilon\) for all residual O(epsilon) contradicts w'_i<w_i. Therefore **NO such downshift H can exist**. This principle uses no genericity and works for arbitrary dense H.

## Step 3 — every internal weight is a genuine HARMONIC MIDPOINT

For each i<nu the first nonzero i-th diagonal Puiseux coefficient \(H_i=A_{w_i}\) lies in K and has (H_i)_ii>0. PSD Cauchy–Schwarz along the center gives the exact order restriction
\[
(H_i)_{ab}=0\quad\text{if }w_a+w_b>2w_i.
\tag{90.4}
\]
Within H_i, any offdiagonal entry whose weighted midpoint equals w_i necessarily joins a lower index a<i to a higher index b>i: pairs both at or below i have average <w_i unless diagonal (i,i), and pairs both at or above i have average >w_i unless diagonal.

Suppose H_i had NO such equality offdiagonal. Its finitely many other nonzero offdiagonal entries have weighted midpoints STRICTLY LESS than w_i; H_i has no positive-weight diagonal beyond i because of (90.4). Choose a small rational w'_i<w_i, still exceeding w_(i−1), so that all its nonzero entries satisfy the perturbed support inequalities (90.3): any pair involving i and a smaller index becomes easier after decreasing w_i, while entries not involving i have a positive strict margin. The downshift principle then contradicts the center's sharp Loewner upper envelope.

Therefore H_i MUST have at least one nonzero offdiagonal entry connecting a<i<b and satisfying
\[
\boxed{2w_i=w_a+w_b.}
\]
Select one such edge at each internal vertex. Distinct internal vertices cannot choose the same parent edge, since the weights are strictly increasing and its average determines the child's weight. Hence this gives a valid strict one-action harmonic midpoint network on exactly nu−1 internal vertices (and terminal nu), extracted from the ORIGINAL DENSE kernel.

## Step 4 — maximal facial depth forces DISCRETE CONVEXITY

Fix i=1,...,nu−1. Consider the actual face
\(W_{i+1}=U+\operatorname{span}(e_1,\ldots,e_{i+1})\).
Its canonical exposing rank in a length-nu minimal chain is exactly ONE, supported on e_(i+1), by Step 1. Put
\(K_{i+1}=K\cap S(W_{i+1})\), and project it to the two-dimensional space \(R=\operatorname{span}(e_i,e_{i+1})\).

Because the compressed exposing stress E_(i+1,i+1) is orthogonal to K_{i+1}, every projected kernel matrix has (i+1,i+1)=0. If the projected kernel subspace met the PSD cone ONLY at zero, the homogeneous strict Gordan–Stiemke alternative would give a PD 2×2 matrix orthogonal to it. By the exact compression-annihilator identity, this PD matrix (zero extended on the rest of W_(i+1)) would lift to an ambient K^\perp stress whose compressed PSD rank is TWO at W_(i+1). Prepending earlier steps would yield a facial-reduction sequence shorter than nu, CONTRADICTING maximal minimal depth.

Thus there exists an actual H∈K_{i+1} whose PSD compression to R is nonzero. Positive pairing with E_(i+1,i+1) is zero, so by PSD complementarity the compression is precisely \(aE_{ii}\) with a>0. Therefore
\[
H_{ii}>0,\quad H_{i,i+1}=H_{i+1,i+1}=0,
\quad H\text{ is supported on }W_{i+1}.
\tag{90.5}
\]

Suppose the consecutive gaps were NOT nondecreasing at i:
\[
2w_i>w_{i-1}+w_{i+1},
\quad w_0:=0 \text{ on target support}.
\]
Choose \(w'_i\) strictly between \(\max(w_{i-1},(w_{i-1}+w_{i+1})/2)\) and w_i. The possible nonzero entries of H can be:
- among U and the first i grades, with new pair weight <=2w'_i;
- between e_(i+1) and one of U,e1,...,e_(i−1), with pair weight <=w_(i−1)+w_(i+1)<2w'_i;
- NOT between e_(i+1) and e_i, or within e_(i+1), by (90.5);
- NOT to any grade beyond i+1, since H is supported on W_(i+1).

Thus (90.3) holds for H at the lower weight w'_i. The downshift principle again produces a forbidden competitor with larger i-th diagonal. Contradiction. Therefore
\[
\boxed{w_{i+1}-w_i\ge w_i-w_{i-1}
\qquad(1\le i\le\nu-1).}
\tag{90.6}
\]
The extracted harmonic weights are DISCRETELY CONVEX. This conclusion is valid for arbitrary dense kernels, not merely graph constructions.

## Step 5 — the exact leading exponent is a valid HALF WEIGHT

The intrinsic Dikin–Hessian weighted-support formula of checkpoint 89 gives
\[
\alpha=\tau(K,w)
 =\min_{H\in K\setminus0}\max_{H_{ab}\ne0}\frac{w_a+w_b}{2}
\le w_1,
\]
because the first diagonal center coefficient H1=A_(w1)∈K has maximal support weight exactly w1.

If alpha=w1, the harmonic parent relation for vertex1 must have lower parent 0 and higher parent v with w_v=2w1; hence alpha=w_v/2.

If alpha<w1, choose an attaining H∈K. Every positive null diagonal or null-null offdiagonal has weight >=w1, so H has no such entry. Since uniqueness forces K∩S(U)=0, some support-to-null entry H_(0,v) is nonzero, and alpha is the largest half-weight w_v/2 among such entries. Thus again
\[
\boxed{\alpha=w_v/2\le w_1}
\]
for some internal/terminal vertex v. This completes the DENSE NECESSITY of the entire strict convex harmonic certificate.

## Step 6 — the converse game realization and integer formula

Starting with the extracted harmonic parent pairs and convex weights, add at every internal i the nearest-neighbor slack action (i−1,i+1), unless already equal to its selected parent pair. Discrete convexity means its average is >=w_i, so the Bellman weights are unchanged. Parent edges remain globally distinct since an edge spanning exactly two consecutive indices can belong only to its midpoint child. If alpha<w1, add a source-to-v leading edge; no collision is possible, since an occupied harmonic edge (0,v) would force a child's value alpha<w1, while a nearest-neighbor edge (0,v) would require v=2 and convexity gives w2/2>=w1. If alpha=w1, no optional edge is needed.

The already-proved strict incidence theorem (checkpoints 57 and 70) then provides a finite rational rank-one PSD pencil whose **entire ambient competitor recovery exponent is alpha** and whose *exact greedy exposing rank profile* is (1,...,1), so its minimal degree is nu. Positive support padding realizes every prescribed rank r≥1. This proves the converse and the universal equality with the integer-gap formula of checkpoint 72. QED.

## Important mathematical scope

**FULLY RESOLVED** by this milestone: the ALL-DENSE, ALL-VALUE arithmetic/combinatorial sharp exponent spectrum at exact MAXIMAL minimal facial depth d=nu, for EVERY nullity nu and positive target rank r. In particular, nonreciprocal values at nu>=6 are included and no other values occur.

**NOT RESOLVED:** the entire ALL-DENSE joint spectrum at arbitrary *nonmaximal* degree d<nu and every rank profile. For those, the center valuation-flag chain may be longer than the minimal facial chain; the Gordan alignment argument above does not directly force the full profile to match any tied-edge graph. The same weighted-support/dual compression bridge may help, but further work is needed.

**No overclaim of novelty:** Maxdet analytic centers, Gordan–Stiemke facial reduction, Puiseux data and mediated sets are established theories. The specific dense maximal-depth convexity and universality theorem is newly proved in this packet; priority relative to outside literature remains unchecked.
