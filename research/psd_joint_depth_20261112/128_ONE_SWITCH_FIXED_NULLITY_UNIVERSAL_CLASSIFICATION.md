# 128 — One-switch interpolation at exact nullity and the universal PSD exponent–depth spectrum

**Date:** 2026-11-12.
**Research branch:** `research/psd-joint-depth-universal-20261107`.
**Source repository:** `Harman6139/Posterity-Files`.
**Reviewed source head:** `48bcfb75063cb8674f3505384cbcd5e8ddc8af75`.
**Status:** A complete research proof is supplied below. It has not been independently refereed. This file is a new continuation, not a file already committed to GitHub.

## Abstract and precise scope

For every strict harmonic weight vector, every admissible leading half-weight, and **every integer between its universal lower and upper facial-peeling depths**, we construct a rational uniquely solvable PSD inverse problem at **exactly the original scalar nullity**, with that sharp full-ambient recovery exponent and that **minimal** singularity degree. The construction uses no cloned null coordinates.

The key is to select a special schedule rather than realize every admissible-looking schedule: follow the upper recurrence for an initial segment, then switch exactly once to the lower recurrence. These schedules already cover every intermediate depth. A common non-source blocking endpoint keeps the delayed coordinates unexposable until the switch. Collisions with tight edges are resolved by adding a positive child diagonal to the edge's existing generator, not by giving the edge a second independent coefficient. After the switch, every such cross-layer collision is off-face. Shared source-release edges have a separate, triangular synchronization property.

Combining this construction with the dense necessity argument gives a finite, purely arithmetic necessary-and-sufficient formula for every attainable tuple `(n,r,d,alpha)`, for positive target rank. An explicit finite minimum over the same certificates gives the exact smallest nullity for each prescribed `(d,alpha)`.

This is **not** a classification of every prescribed facial rank-drop profile, nor a claim that every grade-aligned schedule is realizable. The obstruction in checkpoint 125 remains valid.

---

## 1. Definitions and the classification theorem

Let `S^n` have the Frobenius inner product. For a real linear map `A:S^n -> R^m`, suppose

\[
\{X\succeq0:A(X)=A(X_*)\}=\{X_*\},\qquad \operatorname{rank}X_*=r\ge1.
\]

Write `nu=n-r`. The full-ambient recovery modulus is

\[
\omega(\delta)=\sup\{\|X-X_*\|_F:X\succeq0,\ \|A(X-X_*)\|\le\delta\}.
\]

Its sharp exponent is the number `alpha` for which `omega(delta)=Theta(delta^alpha)` as `delta` decreases to zero. Equivalent finite-dimensional norms do not change it. The integer `d` is the **minimum** number of valid semidefinite facial-reduction steps needed to reach the face supported on `range(X_*)`.

A valid exposing matrix on a current support subspace `F` is an ambient matrix `Z` satisfying

\[
Z\in (\ker A)^\perp,\quad \langle Z,X_*\rangle=0,\quad P_F ZP_F\succeq0.
\]

The next support is `F cap ker(P_F ZP_F)`.

### Harmonic certificates

For an integer `k>=1`, a certificate consists of parents

\[
0\le a_i<i<b_i\le k\qquad(1\le i<k)
\]

and their solution

\[
0=w_0<w_1<\cdots<w_k=1,\qquad
2w_i=w_{a_i}+w_{b_i}\quad(1\le i<k).                 \tag{1.1}
\]

For fixed parents the boundary-value linear system is nonsingular: a nonzero solution with zero boundary values would have a positive maximum or negative minimum, and harmonicity propagates that extremum along increasing parents to the zero terminal boundary. Consequently its solution is rational. Parent choices whose solution is not strictly increasing are discarded. There are at most `((k-1)!)^2` choices; **no real-algebraic feasibility oracle is involved**. More explicitly, with internal indices `1,...,k-1`, set

\[
Q_{ij}=2\delta_{ij}-\mathbf1_{\{a_i=j\}}-\mathbf1_{\{b_i=j\}},
\qquad c_i=\mathbf1_{\{b_i=k\}}.
\]

Then `w_internal=Q^{-1}c`, or, by Cramer's rule, `w_i=det(Q with column i replaced by c)/det(Q)`. Thus the formula can be written using only integer determinants, rational comparisons, and finite integer recurrences.

For `1<=j<k`, define

\[
\ell(j)=\#\{1\le i<j:2w_i<w_{j+1}\},                 \tag{1.2}
\]
\[
p(j)=\min\{1\le i\le j:2w_i>w_j+w_{i-1}\},\qquad
u(j)=p(j)-1.                                      \tag{1.3}
\]

Let `L(w)` be the length of the path starting `k -> k-1` and then taking `j -> ell(j)` until zero. Let `U(w)` be the analogous length using `j -> u(j)`. For `k=1`, both equal one.

### Theorem 1 — complete attainable-tuple spectrum

Fix `r>=1` and `nu>=1`. A tuple `(r+nu,r,d,alpha)` is attainable if and only if one of the following holds:

* `d=1` and `alpha=1`;
* there are a harmonic certificate (1.1) with `1<=k<=nu` and an index `1<=v<=k` such that

\[
\boxed{\alpha=\frac{w_v}{2}\le w_1,\qquad L(w)\le d\le U(w).}       \tag{1.4}
\]

Every attainable tuple has a rational realizing measurement map and a rational target. The rank `r` affects only the total order `n=r+nu`, not the permitted `(nu,d,alpha)` combinations.

For `nu=0`, the only possibility is `d=0, alpha=1`.

Equivalently, if `H_k` denotes the finite set of strict harmonic certificates,

\[
\boxed{
\Sigma_{\nu,d}
=(\{1\}\ \text{if }d=1\text{, otherwise }\varnothing)
\ \cup\!
\bigcup_{k=d}^{\nu}\ \bigcup_{w\in H_k\,:\,L(w)\le d\le U(w)}
\left\{\frac{w_v}{2}:1\le v\le k,\ w_v\le2w_1\right\}.
}                                                               \tag{1.5}
\]

Empty unions have their usual meaning. In particular `d>nu` is impossible.

The necessity is proved in Section 2. The new fixed-nullity sufficiency occupies Sections 3–8. Section 9 gives an exact finite formula for minimum nullity, including a finite upper cutoff.

---

## 2. Dense necessity: why arbitrary kernels satisfy the certificate

This section restates and supplies the essential arguments of checkpoints 10, 89, 91 and 99. It does not assume that a dense kernel is an incidence kernel.

### 2.1 The canonical center and its envelope

Put `K=ker A`. Uniqueness implies `K cap S_+^n={0}`. Separating `K` from the compact trace-one PSD section gives `W>0` in `K^perp`. Hence the shifted PSD slices are bounded, and

\[
C_t=\arg\max\{\log\det X:X\succ0,\ X-X_*-tI\in K\}
\]

exists uniquely for `t>0`. Stationarity gives `C_t^{-1} in K^perp`. The central equations, after multiplication by the determinant, are polynomial. Thus the entries of the unique center are semialgebraic and admit convergent real Puiseux expansions near zero. Boundedness and uniqueness imply `C_t -> X_*`.

The identity

\[
n=\langle C_t^{-1},X_*\rangle+t\operatorname{tr}C_t^{-1}
\]

implies `C_t >= (t/n)I`. Write `Z_t=tC_t^{-1}`. Then `Z_t in K^perp`, `Z_t>=0`, `tr Z_t<=n`, and `<Z_t,X_*><=nt`.

Choose a fixed bounded right inverse of `A^*` on `K^perp`. For every PSD `Y` with residual at most `delta`, these identities give

\[
\boxed{0\preceq Y\preceq n(1+c\delta/t)C_t.}                      \tag{2.1}
\]

Indeed `<Z_t,Y><=nt+cn delta`; after congruence by `C_t^{-1/2}`, a PSD matrix is bounded above by its trace times the identity. This envelope applies to **every ambient PSD competitor**, not merely to the shifted central slice.

### 2.2 Fixed valuation grades and the rescaling lemma

Starting from `U_0=range(X_*)`, repeatedly take the range of the leading positive coefficient of the center compressed to the orthogonal complement of earlier grades. This gives a fixed orthogonal decomposition

\[
\mathbb R^n=U_0\oplus\cdots\oplus U_k,
\qquad 0=w_0<w_1<\cdots<w_k\le1,
\]

with each positive grade nonzero. On `U_i` the first diagonal coefficient is positive definite at exponent `w_i`. PSD Cauchy–Schwarz implies that a coefficient `A_e` of the center has block `(U_a,U_b)` equal to zero whenever

\[
w_a+w_b>2e.                                                     \tag{2.2}
\]

We use the following elementary finite-coefficient lemma. If a finite generalized polynomial has a positive-definite first diagonal coefficient at exponent `b_i` on each of finitely many distinct-weight blocks, and has no coefficient at `(i,j)` with `2e<b_i+b_j`, multiply its coefficient at exponent `e` by `exp(sigma e^2)`. For sufficiently large fixed `sigma`, the resulting polynomial is positive definite for small positive `t`.

To prove this, normalize block `i` by `exp(-sigma b_i^2/2)t^{-b_i/2}`. Only a cross term at `e=(b_i+b_j)/2` can survive in the limit, and its multiplier is

\[
\exp\{-\sigma(b_i-b_j)^2/4\}.
\]

The limiting diagonal blocks remain positive definite, while all cross blocks can be made arbitrarily small.

If `w_k<1`, apply this lemma to the center truncated through exponent `w_k`. All its nonconstant coefficients lie in `K`, because `C_t-X_*-tI in K`. It would give a positive-definite exact feasible curve, contradicting uniqueness. Therefore `w_k=1`.

Apply the same lemma through exponent one. The resulting thick positive curve has residual `O(t)`, so (2.1) bounds it by a constant multiple of `C_t`. Conversely, the center's graded diagonal orders bound its normalized trace. Thus

\[
\boxed{cD_t^2\preceq C_t\preceq CD_t^2,\qquad
D_t=\bigoplus_{i=0}^k t^{w_i/2}I_{U_i}.}                         \tag{2.3}
\]

In particular `k<=nu`.

### 2.3 Harmonicity of every internal grade

For `i<k`, the actual coefficient `H_i=A_{w_i}` lies in `K`, is positive definite on `U_i`, and satisfies (2.2). Suppose it has no nonzero cross-grade block with

\[
a<i<b,\qquad w_a+w_b=2w_i.
\]

Every cross-grade block of `H_i` then has midpoint strictly below `w_i`. Lower the entire weight of `U_i` slightly, to `w_i'` with `w_{i-1}<w_i'<w_i`, preserving the support inequalities for `H_i`. Add `t^{w_i'}H_i` to the finite center expansion and apply the coefficient-rescaling lemma with the modified weights. The result is a PSD curve of residual `O(t)` whose `U_i` diagonal is bounded below by a positive multiple of `t^{w_i'}`. Equation (2.1) contradicts the original center's `O(t^{w_i})` diagonal on that block.

Thus at least one genuine midpoint pair exists for each internal grade. Choosing one per grade gives (1.1), including rationality by its nonsingular rational linear system.

### 2.4 The exponent is an admissible half-weight

On `K`, define the Dikin radius

\[
\rho_t=\max\{\|H\|_F:H\in K,\ \|C_t^{-1/2}HC_t^{-1/2}\|_F\le1\}.
\]

For `K={0}`, put `rho_t=0`. With `q=||A(I)||>0`,

\[
\omega(qt)\asymp t+\rho_t.                                      \tag{2.4}
\]

For the lower bound, `C_t +/- H` are PSD for every admissible `H`, have residual `qt`, and differ by `2H`; also `X_*+tI` gives a linear displacement. For the upper bound, write any competitor as `C_t+H+E`, with `H in K` and `||E||=O(t)`. The envelope (2.1) and `C_t>=(t/n)I` bound the normalized Frobenius norm of `H`. The same argument applies to `C_t-X_*-tI in K`. This bounds the complete displacement by `O(t+rho_t)`.

In any fixed orthonormal grade coordinates, let

\[
\tau=\min_{0\ne H\in K}\ \max_{H_{ab}\ne0}\frac{w_{i(a)}+w_{i(b)}}2.
\]

The finite weighted-coordinate norm induced by (2.3) gives `rho_t=Theta(t^tau)`. For completeness, a fixed matrix attaining the finite support threshold gives the upper bound on its weighted norm. Projection from `K` onto entries of weight at least `tau` is injective, giving the converse bound uniformly over `K`. Thus `alpha=min(1,tau)`.

If `k>=2`, the nonzero coefficient `H_1` gives `alpha<=w_1`. When equality holds, harmonicity at vertex one gives `w_b=2w_1`, hence `alpha=w_b/2`. When `alpha<w_1`, a minimizing kernel matrix can have no null–null entry, since every such entry has weight at least `w_1`. It cannot be supported entirely on `U_0`, because a small perturbation of `X_*` within that support would remain PSD and contradict uniqueness. Its largest nonzero support-to-null block therefore gives `alpha=w_v/2`.

When `k=1`, the only possible support weights outside `U_0` are `1/2` and `1`, so `alpha` is `1/2` or `1`.

### 2.5 The lower peeling bound

Every ambient PSD exposing matrix annihilates `U_0`. Pairing successively with `H_i=A_{w_i}`, `i=1,...,k-1`, forces its compression to each internal grade to vanish: after all lower rows vanish, only the positive-definite `U_i` diagonal of `H_i` can contribute. Thus the first exposed range is contained in `U_k`. The leading constant coefficient of `tC_t^{-1}` is positive definite on `U_k` and zero elsewhere, so the first maximal exposed range is exactly `U_k`.

At any later stage whose surviving support contains `W_j=U_0+...+U_j`, the matrices `H_i` with `i<=ell(j)` are supported inside `W_j`, since `2w_i<w_{j+1}`. The same successive pairing argument forces all of `U_1,...,U_{ell(j)}` to survive the next step. Induction, even for non-coordinate or rotated intermediate faces, proves

\[
d\ge L(w).                                                       \tag{2.5}
\]

### 2.6 The upper peeling bound

The dual central curve `Z_t=tC_t^{-1} in K^perp` has positive-definite diagonal leading coefficients at exponents `1-w_i`, and its `(i,a)` block has order at least `1-(w_i+w_a)/2`.

On `W_j`, choose `p=p(j)`. Truncate the dual Puiseux series through exponent `E=1-w_p`. All rows of `U_0+...+U_{p-1}` vanish in this truncation: for a lower–upper cross block,

\[
1-\frac{w_{p-1}+w_j}{2}>1-w_p=E.
\]

Every leading diagonal coefficient on `U_p+...+U_j` is included. The finite coefficient-rescaling lemma gives one positive-definite compression on precisely this suffix. It is a fixed linear combination of **actual ambient coefficients in `K^perp`**, and its target-support diagonal is zero, so it is a legitimate exposing matrix. Repetition gives

\[
d\le U(w)\le k.                                                  \tag{2.6}
\]

If `alpha=1`, there cannot be an internal grade, so `k=1` and `d=1`. These arguments prove all necessity assertions in Theorem 1.

---

## 3. The one-switch lemma

For a fixed strict harmonic vector, both `ell` and `u` are nondecreasing and

\[
0\le\ell(j)\le u(j)<j.                                          \tag{3.1}
\]

Indeed, if `i<=ell(j)`, a tight upper parent of `i` has weight at most `2w_i<w_{j+1}`, hence index at most `j`. Therefore `2w_i<=w_{i-1}+w_j`; no such `i` can satisfy the inequality defining `p(j)`. Monotonicity follows as the relevant thresholds increase with `j`.

Let

\[
a(0)=0,\qquad a(j)=1+a(\ell(j))\quad(1\le j<k).                  \tag{3.2}
\]

Then `a` is nondecreasing. Write the complete upper path as

\[
j_0=k,\quad j_1=k-1,\quad j_{t+1}=u(j_t),\quad j_D=0,
\qquad D=U(w).
\]

For every `1<=s<=D-1`, follow the upper path for `s` steps, then follow the lower recurrence from `j_s`. Its length is

\[
d_s=s+a(j_s).                                                    \tag{3.3}
\]

We have `d_1=L(w)` and `d_{D-1}=U(w)`. Moreover,

\[
\begin{aligned}
d_{s+1}-d_s
 &=1+a(u(j_s))-a(j_s),\\
a(j_s)-1=a(\ell(j_s))
 &\le a(u(j_s))\le a(j_s).
\end{aligned}
\]

Therefore

\[
\boxed{d_{s+1}-d_s\in\{0,1\}.}                                 \tag{3.4}
\]

**Every integer in `[L(w),U(w)]` is the length of a one-switch schedule.** This statement does not interpolate individual edges or generators; the old two-step jump counterexample is irrelevant to it.

For the rest of the construction assume `k>=2`, choose such an `s`, and put

\[
q=j_s>0,\qquad J=j_{s-1}>q.                                     \tag{3.5}
\]

Coordinates `i>q` are called early, and coordinates `i<=q` are called delayed. Extend the chosen upper prefix by the lower recurrence to obtain a complete schedule ending at zero.

---

## 4. The fixed-nullity kernel

Work in `S^{k+1}` with coordinates `0,...,k`, target `X_*=E_{00}`, and

\[
F_{ab}=e_ae_b^T+e_be_a^T\quad(a<b),\qquad
\lambda=\frac1{100(k+1)^2}.                                    \tag{4.1}
\]

Fix any tight parents `P_i=(a_i,b_i)` in (1.1). Tight edges are pairwise distinct: an edge's midpoint determines its child's strict weight.

### 4.1 Releases for the lower phase

For each lower transition `j -> ell(j)`, assign every child in the layer `(ell(j),j]` the release edge

\[
R_i=(0,j+1).                                                     \tag{4.2}
\]

It satisfies `w_{j+1}<=2w_i`: this follows from the definition of `ell(j)` for `i<j`, and from the tight upper parent of `j` for `i=j`. Thus it has midpoint at most the child's weight. Early children receive no release.

### 4.2 Safe blockers, deliberately excluding child one

For **early** children `i>q`, let

\[
B_i=(i-1,c_i),\qquad
c_i=\min\{b>i:w_{i-1}+w_b\ge2w_i\}.                            \tag{4.3}
\]

For **delayed** children `2<=i<=q`, use the common upper endpoint

\[
\boxed{B_i=(i-1,J).}                                            \tag{4.4}
\]

There is **no additional blocker for child 1**. Its source-tight anchor already blocks it throughout the upper prefix. Excluding this redundant blocker is essential: it keeps every blocker non-source and separate from shared source releases.

Each blocker is safe. For (4.3), existence follows from any tight parents. For (4.4), if `s=1` then `J=k` and harmonicity implies `2w_i<=w_{i-1}+1`. If `s>=2`, then `q=u(J)`, so every `i<=q` satisfies `2w_i<=w_{i-1}+w_J`.

Blockers are pairwise distinct because their lower endpoints are distinct.

### 4.3 Unique edge ownership and positive extra children

Start one tight generator at each child:

\[
H_i=E_{ii}-E_{00}+\lambda F_{P_i}
       +\lambda F_{R_i}\quad\text{when a distinct release exists}. \tag{4.5}
\]

A release equal to `P_i` is counted only once.

For every blocker `B_i`:

* if `B_i=P_i`, no change is needed;
* if `B_i=P_j` for `j!=i`, add `E_{ii}-E_{00}` to the **existing generator `H_j`**;
* if it is no tight edge, add the new generator

\[
N_i=E_{ii}-E_{00}+\lambda F_{B_i}.                               \tag{4.6}
\]

In the middle case, safety and strict weights imply `j>i`. A tight generator acquires at most one extra child because blockers are distinct. Denote its extra child by `c(j)` when present, and let `S_j={j}` or `{j,c(j)}`. The tight generator is therefore

\[
H_j=\sum_{i\in S_j}E_{ii}-|S_j|E_{00}
 +\lambda F_{P_j}+\lambda F_{R_j},                               \tag{4.7}
\]

with the same conventions concerning absent or duplicate releases.

Every blocker/tight edge has one owner. Releases may be shared, but only in the synchronized way proved below.

### 4.4 The optional leading variable

If `alpha=w_1`, no additional generator is needed. If `alpha=w_v/2<w_1`, add

\[
G=\lambda F_{0v}.                                                \tag{4.8}
\]

This cannot be a tight edge: that would require a child of weight `alpha<w_1`. It cannot be a blocker, since blockers are non-source.

If `(0,v)` equals a lower-phase release, that lower step is necessarily the **last** one: `w_v<2w_1` implies `ell(v-1)=0`. In this one situation remove the release from **all generators of that final layer**, retaining their tight anchors. Section 7.3 supplies the exact replacement stress.

Finally let `K` be the span of these generators and take `A=P_{K^perp}` in Frobenius coordinates. Every generator has trace zero and zero terminal diagonal. In particular `I,E_{kk} in K^perp`.

The matrix order is exactly `k+1`, and the target nullity is exactly `k`.

---

## 5. The collision structure

These lemmas are the reason one switch suffices whereas arbitrary schedules can fail.

### Lemma 5.1 — early collisions stay within one upper layer

If an early blocker `B_i=(i-1,c_i)` equals `P_j` with `j>i`, then `i` and `j` belong to the same layer of the complete upper recurrence.

**Proof.** Suppose `j` is removed earlier, from a prefix `T`, while `i` survives. Then `i<p(T)`, so the defining inequality fails at `i` and hence `c_i<=T`. Since `j>=p(T)` and `i-1<=p(T)-1`,

\[
2w_j=w_{i-1}+w_{c_i}
\le w_{p(T)-1}+w_T<2w_{p(T)}\le2w_j,
\]

a contradiction. Since `j>i`, it cannot be removed later than `i` in a suffix schedule. ∎

### Lemma 5.2 — delayed collisions are released immediately at the switch

Suppose a delayed blocker `B_i=(i-1,J)` equals `P_j`, with `j>i`. Then

\[
\boxed{\ell(q)<j\le q,\qquad b_j=J>q.}                          \tag{5.1}
\]

Thus its owning child lies in the first lower layer, and its physical edge is off-face for the entire lower phase, even when the extra child is removed later.

**Proof.** If `s=1`, then `q=k-1` and `j<=q` is automatic. Otherwise `q=u(J)`. Were `j>q`, then

\[
2w_j=w_{i-1}+w_J\le w_q+w_J<2w_{q+1}\le2w_j,
\]

a contradiction. Also `2w_j=w_{i-1}+w_J>=w_{q+1}`, so `j>ell(q)`. The edge's upper endpoint is `J>q`. ∎

### Lemma 5.3 — source-release collisions synchronize exactly

If a tight edge `P_i=(0,b)` equals a release used at a lower transition from `j=b-1`, then `i` is in that same lower layer and its own release is `P_i`.

**Proof.** Harmonicity gives `2w_i=w_b`; the strict parent ordering gives `i<b`, hence `i<=j`, while the definition of `ell(j)` gives `i>ell(j)`. ∎

No source-tight generator has an extra child, since every blocker is non-source. Any other generator sharing that release has strictly greater weight. Thus sharing cannot cancel a tight leading coefficient in the associated-graded kernel.

### Lemma 5.4 — child one remains blocked during the upper prefix

Write `P_1=(0,b_1)`, so `w_{b_1}=2w_1`. At every upper-phase prefix this edge is active.

For `s=1` there are no noninitial upper steps to check. For `s>=2`, `q=u(J)>=1`, so `2w_1<=w_J`, hence `b_1<=J`. Earlier prefixes are at least `J`. Any release belonging to a delayed generator has upper endpoint at most `q+1<=J` and is also active during these steps. ∎

---

## 6. Exact exponent against all ambient PSD competitors

We prove a uniform upper bound, not merely exhibit one bad recovery arc.

### 6.1 Independent leading forms

Give `H_i` degree `w_i`. Give a new blocker generator `N_i` degree

\[
\eta_i=\frac{w_{i-1}+w_{b(B_i)}}2\ge w_i.
\]

Give `G` degree `alpha`. With `D_t=diag(t^{w_i/2})`, the normalized generator of degree `m` is

\[
\widehat H(t)=t^mD_t^{-1}HD_t^{-1}.
\]

It has a finite limit. For a tight generator the leading form is

\[
E_{ii}+\lambda F_{P_i},
\]

possibly with one additional release of midpoint exactly `w_i`. An extra child diagonal disappears because its weight is strictly smaller. For a new blocker the leading form is `E_{ii}+lambda F_{B_i}` when `eta_i=w_i`, and `lambda F_{B_i}` otherwise. The leading form of `G` is `lambda F_{0v}`.

These limiting forms are linearly independent. The tight edge `P_i` occurs in no other leading form: another generator can share it only as a release with strictly larger degree, by Lemma 5.3. New blocker edges and the leading edge are unique. Consequently the scaled subspaces

\[
K_t=D_t^{-1}KD_t^{-1}
\]

converge to the span `I` of these independent leading forms, with the same dimension.

### 6.2 An explicit rational positive-definite separator

Let `M` be a positive common denominator of all weights and put `m_i=Mw_i`. Choose the integer

\[
T=1+\left(\frac{4(k+1)}\lambda\right)^2,
\qquad z_i=T^{m_i^2}.                                           \tag{6.1}
\]

The expression inside the square is an integer for our choice of `lambda`. Define `W` by `W_{ii}=z_i` and

\[
W_{P_i}=-\frac{z_i}{2\lambda}.                                  \tag{6.2}
\]

For a new blocker with `eta_i=w_i`, also set `W_{B_i}=-z_i/(2lambda)`; for one with `eta_i>w_i`, set it to zero. Set all other offdiagonal entries to zero, including additional tight releases and `G`.

There is no conflict between these assignments. In particular an additional release of degree `w_i` cannot be another child's tight edge, since strict weights would force that child to be `i`, in which case it was already counted only once.

Every leading form is orthogonal to `W`. Moreover, for every nonzero assigned edge `(a,b)` associated to child `i`, harmonicity gives

\[
\frac{m_a^2+m_b^2}{2}-m_i^2
=\frac{(m_b-m_a)^2}{4}>0.
\]

Since the weights have been cleared to integers, this positive difference is at least `1/2`. Thus each normalized offdiagonal has magnitude at most `1/(2lambda sqrt(T))<1/(8(k+1))`. Strict diagonal dominance after diagonal congruence gives

\[
\boxed{W\succ0,\qquad W\perp I,\qquad I\cap S_+^{k+1}=\{0\}.}    \tag{6.3}
\]

No conic feasibility problem remains to be solved.

### 6.3 The uniform PSD bound

Let `X>=0` satisfy `||P_{K^perp}(X-E_{00})||_F<=t`. Write

\[
X-E_{00}=H+E,\qquad H\in K,\quad \|E\|_F\le t.
\]

Since all weights lie in `[0,1]`, `D_t^{-1}(E_{00}+E)D_t^{-1}` is uniformly bounded. If `D_t^{-1}XD_t^{-1}` were unbounded along a sequence `t -> 0`, divide by its norm and pass to a subsequence. The limit would be a nonzero PSD matrix in the limiting subspace `I`, contradicting (6.3). Therefore, uniformly over **all** such competitors,

\[
\boxed{0\preceq X\preceq C D_t^2.}                             \tag{6.4}
\]

The normalized generator basis has an independent limit, so its smallest singular value is bounded away from zero. If `H=sum_g a_g H_g` and generator `g` has degree `m_g`, boundedness of `D_t^{-1}HD_t^{-1}` implies

\[
a_g=O(t^{m_g})\quad\text{for every }g.
\]

All degrees are at least `w_1`, except for the optional degree `alpha` of `G`. Hence

\[
\boxed{\|X-E_{00}\|_F=O(t^\alpha).}                             \tag{6.5}
\]

Taking `t -> 0` for any exact feasible matrix proves uniqueness as well.

### 6.4 A matching full-positive-definite arc

Activate the tight generators only, together with the optional leading generator:

\[
X(t)=E_{00}+\sum_{i=1}^{k-1}t^{w_i}H_i+tE_{kk}
       +\begin{cases}t^\alpha G,&\alpha<w_1,\\0,&\alpha=w_1.\end{cases}  \tag{6.6}
\]

Each internal diagonal is `t^{w_i}` plus nonnegative strictly higher-order terms from extra children. The source diagonal tends to one. Every offdiagonal has order at least its midpoint weight. After normalization by `D_t`, the limiting diagonal is the identity and every nonzero limiting offdiagonal is at most `lambda` in magnitude. Our fixed choice of `lambda` gives strict diagonal dominance for all sufficiently small `t`, so `X(t)>0`.

Because `E_{kk} in K^perp` and has Frobenius norm one, the measurement residual is **exactly `t`**. The displacement is `Theta(t^alpha)`: use the first diagonal if `alpha=w_1`, or the unique leading edge otherwise. Together with (6.5), this proves the exact sharp full-ambient exponent.

The arc can be made an ordinary rational polynomial arc by substituting `t=s^{2M}`. The same thick arc, after adding `t(I-E_{kk})`, lies in the shifted central slice; the center envelope then also proves that its canonical scalar grades are exactly the prescribed `w`.

---

## 7. Exact facial geometry of the constructed kernel

All stresses below are ambient matrices in `K^perp`, not zero extensions incorrectly assumed to be measurements.

### 7.1 The first `s` maximal steps follow the upper recurrence

At the full face, an exposing matrix has `Z_{00}=0`. If an internal diagonal were positive, choose its smallest index `i`. Pairing with `H_i` leaves only its own positive diagonal: the anchor has a lower parent, the optional release touches the source, and any extra diagonal has lower index. This is impossible. Thus every first stress is supported on the terminal coordinate, and `E_{kk}` exposes precisely that coordinate.

Consider a later upper-phase prefix `W_T=span(e_0,...,e_T)`, and put `p=p(T)`. No coordinate below `p` can have positive diagonal in a compressed PSD stress. Otherwise choose the smallest such index `i`.

For `i=1`, Lemma 5.4 makes its tight source edge active, and its release, if any, is active too. Pairing with `H_1` is impossible.

For `i>=2`, its blocker is active. For a delayed child this follows from the common endpoint `J<=T`. For an early child below `p`, the inequality defining `p` fails at `i`, hence `c_i<=T`. If the blocker has a separate generator, its equation forces `Z_{ii}=0`, since its lower endpoint is `i-1` and that row vanishes. If it belongs to a tight generator, all that generator's children still lie in the face: early collisions are same-layer by Lemma 5.1, and delayed collisions have owner at most `q` by Lemma 5.2. Its release, if present, is an active source edge and contributes zero. A strictly positive sum of nonnegative child diagonals would have to vanish, again impossible.

Thus every exposed range lies in `C=span(e_p,...,e_T)`.

To expose all of `C`, put diagonal `z_i` from (6.1) on `C` and zero on every other ambient coordinate, including the source. On each tight edge assign

\[
Z_{P_j}=-\frac1{2\lambda}\sum_{i\in S_j\cap C}z_i,               \tag{7.1}
\]

and on each new blocker assign `-z_i/(2lambda)` if its child is in `C`, zero otherwise. Set all release entries to zero, and set the optional leading entry to zero.

These assignments are consistent. A release has upper endpoint at most `q+1`, so it cannot coincide with a tight edge whose own early child is exposed; an early owner cannot carry a delayed extra child by Lemma 5.2. All generator equations therefore vanish exactly.

If an assigned edge is active and has a child in `C`, both its endpoints must lie in `C`. Otherwise its lower endpoint is below `p`, and safety gives the contradiction

\[
2w_i\le w_a+w_b\le w_{p-1}+w_T<2w_p\le2w_i.
\]

For each active edge and contributing child, safety also gives

\[
\frac{m_a^2+m_b^2}{2}-m_i^2
\ge\frac{(m_b-m_a)^2}{4}>0.                                    \tag{7.2}
\]

At most two child diagonals contribute to any edge. The explicit `T` in (6.1) makes the normalized offdiagonal row sums less than `1/4`. Hence the compression is positive definite on precisely `C` and zero elsewhere. This proves that the first `s` greedy maximal steps are exactly the prescribed upper prefix, reaching `W_q`.

### 7.2 Ordinary lower-phase steps have diagonal compressed stresses

At a lower transition `j -> ell(j)`, let `C=(ell(j),j]` and `f=(0,j+1)`. In this subsection the step is not the final leading-edge collision repair.

Use ambient diagonal one on `C` and zero elsewhere. Set the current release entry `Z_f=-1/(2lambda)` and every other release entry to zero. For a tight edge not equal to any retained release, set

\[
Z_{P_i}=-\frac{\mathbf 1_{\{c(i)\in C\}}}{2\lambda},             \tag{7.3}
\]

where the numerator is zero when no extra child exists. Set each new blocker's entry to `-1/(2lambda)` if its child lies in `C`, and zero otherwise. Set the leading entry to zero.

The own diagonal of every current tight generator is canceled by its current release, or by its identical source-tight anchor. Lemma 5.3 proves exact consistency at every shared release/anchor. Extra child diagonals are canceled by (7.3); separate blocker generators are canceled by their own assignments. Earlier and later generators have zero own diagonal and satisfy the same equations. If a final-layer release was omitted for the future leading-edge repair, its child and any extra child are still outside the current exposed layer, so its pairing is also zero.

All nonzero offdiagonals just assigned are off-face. The current release endpoint is `j+1`. A new delayed blocker has upper endpoint `J>q>=j`. An extra child in an early owner has already been removed together with that owner, so contributes zero. An extra child in a delayed owner has the off-face edge described in Lemma 5.2.

Thus the current compression is **exactly the diagonal identity on `C`**. It is a legitimate ambient exposing stress.

### 7.3 Repair of a final release/leading-edge collision

Suppose `G=lambda F_{0v}` collided with the final release. Then the last prefix is `j=v-1` and `w_v<2w_1`; its final-layer releases were omitted in Section 4.4.

Put diagonal `z_i` from (6.1) on all remaining null coordinates `1,...,j`, and zero elsewhere. Assign on **every** tight edge

\[
Z_{P_i}=-\frac{z_i+z_{c(i)}}{2\lambda},                         \tag{7.4}
\]

where `z_i=0` outside the remaining block and absent extra children contribute zero. Assign `Z_{B_i}=-z_i/(2lambda)` on new blocker edges. Set all retained releases and the leading edge to zero.

There are no conflicting assignments. A retained source release can equal a tight edge only of its own earlier layer; that owner's diagonal is now zero, and a source-tight generator has no extra child. The edge of `G` is no tight edge. The generator pairings are therefore exactly zero, including pairings with earlier owners carrying a still-surviving extra child.

Every active tight edge with nonzero assignment has its own child in the remaining block; edges carrying any nonzero extra child are off-face by Lemma 5.2. An active tight edge cannot touch the source, since that would give

\[
2w_i=w_{b_i}\le w_j<w_v<2w_1\le2w_i.
\]

Thus active assigned edges are wholly inside the remaining null block. The same finite diagonal-dominance estimate (7.2) proves positive definiteness on that block, with source row zero. One valid step finishes the reduction.

---

## 8. Minimality, not just existence of a chain

### 8.1 Forced survivors after the switch

Every tight generator `H_i` has coefficient one on its own diagonal and has no entry with midpoint weight greater than `w_i`. This remains true after all ownership transfers and release omissions.

Let a current support `F` contain `W_j`. For `i<=ell(j)`, `2w_i<w_{j+1}`, so the entire matrix `H_i` is supported in `W_j`. Pair any valid ambient stress with `H_1,H_2,...,H_{ell(j)}` in order. The source row vanishes. Once rows below `i` vanish, all entries of `H_i` except its own diagonal pair to zero: its extra child is lower, every anchor has a lower parent, and every release touches the source. Orthogonality gives `Z_{ii}=0`, and PSD forces the corresponding entire compressed row to vanish.

Therefore the next support contains `W_{ell(j)}`. This holds even if `F` is not a coordinate subspace. Starting at `W_q`, every facial-reduction chain needs at least `a(q)` further steps. Sections 7.2–7.3 construct exactly that many.

### 8.2 Why the greedy prefix gives the global minimum

At a face `F`, the common kernel of all valid PSD compressed stresses is attained by a finite positive sum of them, so it is the survivor of a maximal-rank stress. Denote that survivor by `G(F)`.

If `F subset F'`, every valid stress on `F'` restricts to a valid stress on `F`. Positivity implies that its kernel on `F` is the intersection of `F` with its kernel on `F'`. It follows that `G(F) subset G(F')`. Inductively, the canonical maximal-stress survivor after any number of steps is contained in the survivor of every other chain after that many steps. Thus the greedy chain has minimum length.

Section 7.1 identifies its first `s` steps exactly, leaving `W_q`. Section 8.1 proves that the remaining minimum is `a(q)`. Consequently

\[
\boxed{d_{\min}=s+a(q)=d_s.}                                    \tag{8.1}
\]

Together with the one-switch lemma and Section 6, this proves:

### Theorem 2 — fixed-nullity interpolation

For every strict harmonic vector `w`, every `alpha=w_v/2<=w_1`, and every integer `L(w)<=d<=U(w)`, there is a rational PSD inverse problem on `S^{k+1}` with target `E_{00}`, exact nullity `k`, sharp full-ambient exponent `alpha`, and **minimal** singularity degree `d`.

### 8.3 Padding and boundary cases

For `k=1`, `alpha=1/2,d=1` is realized by retaining the invisible source-to-null offdiagonal and measuring the diagonal. Fully observing a singular target gives `alpha=1,d=1`.

To increase nullity from `k` to `nu`, append a zero target block, measure its entire matrix block and every added cross entry, and keep the old kernel embedded by zero. The added null directions are all exposable in the first step. Restricting a PSD stress to the old coordinates cannot expose any additional old direction, so the old minimal depth is unchanged. Every added entry of an approximate competitor is `O(delta)`, so the old exponent is unchanged too.

To increase rank from one to any prescribed `r`, append a fully observed positive-definite block of size `r-1` and fully observe every added cross entry. All exposing stresses annihilate this added target support. Again neither invariant changes.

For a full-rank uniquely feasible target, any nonzero kernel direction would remain PSD under a sufficiently small signed perturbation. Hence the map is injective, giving `d=0, alpha=1`.

This completes both directions of Theorem 1.

---

## 9. Exact minimum nullity and an explicit finite cutoff

The classification is a finite rational certificate formula, not an assertion that the answer reduces to one elementary expression in a numerator and denominator.

For admissible non-Lipschitz `(d,alpha)`, define

\[
\boxed{
\nu_{\min}(d,\alpha)=
\min\left\{k:\exists w\in H_k,\exists v,
\ \alpha=w_v/2\le w_1,\ L(w)\le d\le U(w)\right\}.
}                                                               \tag{9.1}
\]

Necessity proves that no smaller nullity can work; Theorem 2 constructs a realization at the minimum. For prescribed positive target rank,

\[
n_{\min}(r,d,\alpha)=r+\nu_{\min}(d,\alpha).                     \tag{9.2}
\]

We now make the range in (9.1) explicitly finite and classify when it is empty.

### 9.1 Dimension-free admissibility

Along the lower path, the smallest newly removed weight decreases by at most a factor two per step. It starts at one and ends at `w_1`. Therefore

\[
w_1\ge2^{-(L(w)-1)},\qquad
\alpha=w_v/2\ge w_1/2\ge2^{-L(w)}\ge2^{-d}.                     \tag{9.3}
\]

If `alpha=1/2`, then `w_1>=1/2`. With internal grades, harmonicity at vertex one also gives `w_1<=1/2`, so `w_1=1/2`. At the first reduced prefix, `2w_1=1>w_{k-1}`, and `p(k-1)=1`; consequently `U(w)=2`. Thus the complete dimension-unrestricted sets are

\[
\begin{array}{c|c}
d&\text{attainable sharp exponents}\hline
1&\{1,1/2\},\\
2&\mathbb Q\cap[1/4,1/2],\\
d\ge3&\mathbb Q\cap[2^{-d},1/2).
\end{array}                                                     \tag{9.4}
\]

Sufficiency and a finite dimension bound follow from the next construction. The bound (9.3) also recovers the exponent restriction associated with the classical singularity-degree error bound, without using that theorem as an extra assumption here.

### 9.2 A base certificate of natural depth

Take rational `0<alpha<1/2`, and let

\[
e=\left\lceil\log_2(1/\alpha)\right\rceil,\qquad
c=2^{-(e-1)}.
\]

Write

\[
\frac{2\alpha-c}{1-c}=\frac ab
\]

in lowest terms, with `0<=a<b`; take `b=1` when the numerator is zero.

Use the source zero, terminal one, all dyadic spine values `1/2,1/4,...,c`, and all affine-grid values

\[
c+\frac{j(1-c)}b\quad(1\le j<b),
\]

discarding duplicates. A spine point has parents zero and twice itself; a new grid point has its two neighboring grid points as parents. Strict harmonicity holds, and `2alpha` is a vertex. The lower recurrence successively uses the exact spine thresholds `1/2,1/4,...,c`, so its length is exactly `e`. Theorem 2 realizes the exponent `alpha` and degree `e` with

\[
\nu\le e+b-1.                                                   \tag{9.5}
\]

### 9.3 A depth-`d` helper with exponent approaching one half

For `d>=3` and integer `M>=1`, set

\[
A_M=2^M-1,\qquad
\beta=\frac{A_M}{2A_M+d-2},\qquad
\Delta=\frac1{2A_M+d-2},\qquad T_0=2\beta+\Delta.
\]

Use `k=M+d-1` positive vertices, with

\[
w_1=\beta,
\quad w_i=T_0-\frac{T_0-\beta}{2^{i-1}}\ (2\le i\le M+1),
\]
\[
w_i=2\beta+(i-M-1)\Delta\quad(M+2\le i\le k).
\]

Then `w_{M+1}=2beta` and `w_k=1`. Choose parents `(0,M+1)` at vertex one, `(i-1,M+2)` for `2<=i<=M+1`, and `(i-1,i+1)` on the arithmetic tail.

The upper recurrence removes the arithmetic tail one vertex at a time, then removes the whole block `2,...,M+1`, then vertex one. Its depth is exactly `d`. To check this directly, note that `2w_i-w_{i-1}=T_0` throughout the dyadic block, while on the arithmetic tail it equals `w_i+Delta`. Theorem 2 therefore realizes exponent `beta` and degree `d` at nullity `M+d-1`.

Choose `M` so that

\[
(2^M-1)(1-2\alpha)>\alpha(d-2).                                 \tag{9.6}
\]

Then `beta>alpha`.

### 9.4 Source gluing and the finite cap

Two constructed kernels can share only their source coordinate, with all positive null coordinates disjoint and every cross-component null entry measured. The same independent-leading-form proof and positive diagonal separator give exponent equal to the minimum of the component exponents. Their maximal compressed PSD exposing sets are unions of the component maximal exposing sets: restriction gives necessity, and block-diagonal sums of the component compressions give sufficiency. Thus their minimal degree is the maximum of the component degrees. Source terms do not interfere, because every exposing stress has source diagonal zero and all source terms vanish in the positive-weight initial forms.

For an admissible `0<alpha<1/2`, `e<=d`. If `e=d`, use the base certificate. If `e<d`, glue it to the helper chosen by (9.6). This gives the explicit finite cap

\[
B(d,\alpha)=
\begin{cases}
e+b-1,&e=d,\\
e+b+M+d-2,&e<d,
\end{cases}                                                     \tag{9.7}
\]

where `M` is any positive integer satisfying (9.6), for example the least one.

Accordingly the exact minimum in (9.1) is the **finite arithmetic minimum over `d<=k<=B(d,alpha)`**. Every parent system is a nonsingular integer linear system with fixed zero/one boundaries. There are no quantified real kernel variables or conic tests.

The exceptional minima are

\[
\nu_{\min}(1,1)=1,\qquad
\nu_{\min}(1,1/2)=1,\qquad
\nu_{\min}(2,1/2)=2.
\]

For combinations outside (9.4), the minimum is infinity. The full-rank case has `nu_min(0,1)=0`.

---

## 10. Relation to the previous routes and validation

The proof does not assert that every interval-allowed schedule is realizable. For the checkpoint-125 weights

\[
(0,1/4,3/7,1/2,17/28,5/7,1),
\]

the upper path is `6 -> 5 -> 4 -> 3 -> 1 -> 0`. Switching after two upper steps gives

\[
6\to5\to4\to1\to0,
\]

with layers `{6},{5},{2,3,4},{1}`. It avoids the forbidden layers `{6},{4,5},{2,3},{1}`. The scalar degree remains four.

The earlier obstructions are respected:

* A one-edge modification can still jump two depths. Here the **schedule-length sequence**, not an edge sequence, has increments zero or one.
* Shared safe/tight edges still cannot receive independent coefficients. Here a collision transfers a **positive child diagonal** into the edge's sole owner.
* Shared releases are permitted only with the exact source/anchor synchronization of Lemma 5.3. Their leading-form independence is proved, not inferred from individual Bellman inequalities.
* Canonical scalar weights still do not determine the depth of an individual kernel. The theorem describes which tuples are **attainable**, and constructs an appropriate kernel for every allowed tuple.
* Prescribed rank-drop profiles and arbitrary signed compression towers are not classified by this theorem.

The companion Python file `129_ONE_SWITCH_EXACT_CERTIFICATE_AUDIT.py` performs exact rational checks of the uniform formulas on targeted regression systems and closed-form families. It verifies generator support orders, independent initial pivots, exact orthogonality of every proposed ambient stress to every generator, the strict diagonal-dominance exponent inequalities, and the active blockers/forced survivors. The regression systems include the actual checkpoint-123 early-edge collision, the checkpoint-125 forbidden-schedule example, cross-layer merged-child systems, and final leading-edge repairs. These checks are reproducibility aids; **the all-dimensional proof is Sections 3–8, not a finite enumeration**.

### Source audit trail

The following branch files supplied the prior mathematical context and load-bearing antecedents; all references below are relative to the repository root at the reviewed source head:

- `research/psd_joint_depth_20261109/OPUS_5_5_SUCCESSOR_RESEARCH_HANDOFF.md`.
- `research/psd_joint_depth_20261107/10_UNIVERSAL_DIKIN_HESSIAN_CLASSIFIER.md`.
- `research/psd_joint_depth_20261108/89_UNIVERSAL_FIXED_MONOMIAL_DIKIN_CHART_DENSE.md`.
- `research/psd_joint_depth_20261108/91_UNIVERSAL_DENSE_TO_HARMONIC_EXPONENT_NORMAL_FORM.md`.
- `research/psd_joint_depth_20261108/99_UNIVERSAL_PRIMAL_DUAL_INTEGER_PEELING_SANDWICH.md`.
- `research/psd_joint_depth_20261108/110_UNIFORM_INTERVAL_REALIZATION_WITH_LINEAR_NULLITY_OVERHEAD.md`.
- `research/psd_joint_depth_20261108/114_ALL_HALFWEIGHTS_LOWER_PEELING_EXACT_NULLITY_RANK_ONE.md`.
- `research/psd_joint_depth_20261109/119_INITIAL_CONIC_GRADED_KERNEL_LOEWNER_IFF.md`.
- `research/psd_joint_depth_20261109/123_CLONE_FREE_UPPER_PEELING_BY_MULTICHILD_DIAGONAL_GENERATORS.md`.
- `research/psd_joint_depth_20261109/125_DENSE_DUAL_BOTTLENECK_FORBIDS_ONE_INTERMEDIATE_FLAG.md`.
- `research/psd_joint_depth_20261109/127_POSITIVE_CIRCUIT_ELIMINATION_AND_FACE_GORDAN_CRITERION.md`.
- `research/psd_joint_depth_20261108/85_COMPLETE_DIMENSION_FREE_EXPONENT_VS_FACIAL_DEGREE_SPECTRUM.md` (the finite-cap discussion is rederived here).

The classical literature includes J. F. Sturm, “Error Bounds for Linear Matrix Inequalities,” *SIAM Journal on Optimization* 10(4), 1228–1248 (2000), DOI `10.1137/S1052623498338606`, and S. Sremac, H. J. Woerdeman and H. Wolkowicz, “Error Bounds and Singularity Degree in Semidefinite Programming,” *SIAM Journal on Optimization* 31(1), 812–836 (2021), DOI `10.1137/19M1289327`. No claim of independent bibliographic priority is made here for the classical tools or the branch's antecedent results.

**Conclusion.** The fixed-nullity interval-filling frontier is resolved by the one-switch construction. The resulting finite harmonic/peeling criterion is necessary and sufficient for all positive-rank attainable `(n,r,d,alpha)` tuples, with the exact minimum-nullity formula (9.1), bounded finitely by (9.7).
