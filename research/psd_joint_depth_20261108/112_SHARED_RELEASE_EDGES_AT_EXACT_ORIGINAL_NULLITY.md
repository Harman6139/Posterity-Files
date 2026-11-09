# Milestone 112 — every harmonic valuation system attains the PRIMAL lower peeling bound at EXACT ORIGINAL NULLITY via shared release edges

**2026-11-08. PROVED for arbitrary numbers of ordered harmonic grades, with completely explicit rational finite-dimensional PSD generators and direct full-PSD upper/lower recovery bounds.** This is stronger than the clone-assisted theorem of milestone110: for the important leading-diagonal sharp exponent alpha=w1, **NO nullity enlargement** is needed. For leading alpha<w1, the same construction works when its source edge does not collide with a release edge; for any prescribed target rank >=2, an independent second support coordinate removes that collision completely. The general rank-one leading-edge collision remains an obstacle to the FULL fixed-nullity all-value theorem.

## Input and theorem

Fix any integer h>=1, k=h+1, strict rational harmonic weights and parent pairs
\[
0=w_0<w_1<\cdots<w_h<w_k=1,\quad
2w_i=w_{a_i}+w_{b_i},\qquad0\le a_i<i<b_i\le k.
\]
Let L(w) be the universal primal forced-depth integer recurrence from checkpoint99:
initial terminal k removal, and at a remaining prefix j remove the suffix after
\[
\ell(j)=\#\{1\le i<j:2w_i<w_{j+1}\}.
\]

**Main theorem.** There is a rational linear PSD inverse problem on **EXACTLY S^(k+1)** with rank-one target X*=E00, nullity exactly k, **sharp full ambient Hölder exponent alpha=w1**, and **exact MINIMAL facial-reduction degree d=L(w)**. The same original-nullity construction works for a chosen alpha=w_v/2<w1 when the independent source-to-v edge (0,v) is distinct from the finite list of release edges constructed below. For any target rank r>=2, ALL such qualifying halfweight exponents alpha can be realized at nullity k, using a second positive support coordinate to place the leading edge without any release collision.

Thus BOTH scalar harmonic and facial-depth data are preserved at the original nullity for the LOWER endpoint in these precise regimes, with no midpoint-edge uniqueness assumption.

## I. The canonical fastest prefix schedule and its SHARED release vertices

Compute the deterministic strict descending prefix sequence
\[
j_0=k,\qquad j_1=k-1,\qquad
j_{t}=\ell(j_{t-1})\quad(t=2,\ldots,d),\quad j_d=0.
\]
The t-th exposing layer is
\[
C_t=\{j_t+1,\ldots,j_{t-1}\}.
\]
The first layer is terminal {k}. For t>=2 define the EARLIEST vertex from the preceding removed layer
\[
b_t=j_{t-1}+1,\quad
f_t=(0,b_t).
\]
Every internal vertex i in C_t has \(2w_i\ge w_{b_t}\). This follows from i>ell(j_(t−1)), including the largest current index because harmonic weights obey the adjacent-spacing inequality \(w_{i+1}\le2w_i\). Thus the release edge f_t has midpoint order <=wi, and it is allowed to be tied into a mode whose harmonic anchor has exact midpoint wi.

## II. The explicit rank-one kernel (edges may be shared!)

Set λ>0 a sufficiently small rational, e.g. λ<1/[100(k+1)^2]. For each internal i in layer C_t form
\[
H_i=E_{ii}-E_{00}
       +\lambda F_{a_i,b_i}
       +\begin{cases}
         \lambda F_{0,b_t},&(a_i,b_i)\ne(0,b_t),\\
         0,&(a_i,b_i)=(0,b_t).
        \end{cases}
\tag{112.1}
\]
Let \(K=\operatorname{span}\{H_1,\ldots,H_h\}\), L=P_(K⊥), X*=E00. Here \(F_{uv}=E_{uv}+E_{vu}\).
All H_i have trace zero, terminal diagonal zero, and mutually independent unique diagonal entries Eii. Hence identity and Ekk are measured. Several H_i in the SAME exposing layer intentionally share the SAME offdiagonal edge F_(0,b_t); a release edge may also coincide with the harmonic anchor of the FIRST child of that layer. This is a new **shared-edge generator** construction, not the globally edge-disjoint tied-mode Shapley family.

## III. FULL AMBIENT sharp exponent = w1 despite shared coefficients

For PSD X with ||P_(K⊥)(X-X*)||<=delta, put Y=X*+P_K(X-X*), E=X-Y. Then ||E||_F<=delta, Y+delta I>=0, traceY=1, Ykk=0. Write
    Y=E00+sum_(i=1)^h x_i H_i,
so Yii=x_i (one generator per internal vertex), and y0=1−sum x_i. Positive semidefiniteness of Y+delta I gives x_i>=−delta; trace control makes all x_i and Y00 bounded.

The harmonically tight ANCHOR edge P_i=(a_i,b_i) has offdiagonal
\[
Y_{a_i b_i}
=\lambda\left(x_i+
\sum_{\substack{j>i:\ f_{t(j)}=P_i\\P_j\ne f_{t(j)}}}x_j\right).
\tag{112.2}
\]
The crucial **UPPER-TRIANGULAR property** follows from the release condition:
if a different child's release edge equals P_i then P_i=(0,b) has midpoint wi=w_b/2, whereas the releasing child j has wj>=w_b/2=wi, hence j>i. No *earlier* harmonic coefficient can enter a later child's unique tight anchor. If the anchor has positive lower endpoint a_i>0 it is never a release edge.

Write Ui=|x_i|+delta, U0=|Y00|+delta=O(1), Uk=delta. Principal PSD 2x2 minors of Y+delta I at each anchor, combined with (112.2), yield
\[
\boxed{
U_i\le C\sqrt{U_{a_i}U_{b_i}}
       +C\sum_{j>i}U_j+C\delta.
}
\tag{112.3}
\]
The sum over j>i is triangular and STRICTLY SUBLEADING because wj>wi.

To prove the sharp bound rigorously, let t_i be the finite expected absorption time of the fair parent walk on the TIGHT harmonic graph, with t0=tk=0 and \(t_i=1+(t_{a_i}+t_{b_i})/2\). Every internal state reaches terminal by repeatedly choosing its higher parent, so the expected times are finite. Choose positive constants M0,Mk and Mi=A exp(B t_i) for B sufficiently large that
    C sqrt(M_(a_i)M_(b_i))<=Mi/4
for every i, and select M0 large enough for U0, Mk>=1 for Uk. Because the finitely many strict inequalities wj>wi hold, for all sufficiently small delta
    C sum_(j>i) Mj delta^(wj)+Cdelta <=(Mi/4)delta^(wi).
Suppose R=max_i Ui/(Mi delta^(wi))>1. Its maximizer is internal, since boundary ratios<=1. Equation (112.3) then gives
    R Mi delta^(wi) <=(R/4+R/4+1/4)Mi delta^(wi),
a contradiction. Thus Ui=O(delta^(wi)) for every internal i; all release-edge offdiagonals are finite sums of x_j and therefore O(delta^w1). Source diagonal follows from trace; off-kernel entries differ by at most delta. Hence
\[
\boxed{\omega(\delta)=O(\delta^{w_1})}.
\]

For SHARPNESS, take \(X(t)=E00+\sum_i t^{w_i}H_i+tE_{kk}\), with fixed small lambda. Its source diagonal tends to one and all internal/terminal diagonals equal t^wi. Every tight anchor offdiagonal term has exponent wi=(w_a+w_b)/2, while every SHARED release term from child i has exponent wi>=w_(b_t)/2. After diagonal congruence all normalized offdiagonals are at most hλ times a harmless source factor, so for sufficiently small λ the entire matrix is STRICTLY DIAGONALLY DOMINANT and PD for small t>0. Its measurement residual equals t (Ekk is measured) and displacement Θ(t^w1). Therefore \(\omega(\delta)=\Theta(\delta^{w_1})\) and uniqueness holds.

**Consequently the canonical maxdet-center Loewner valuation grades of this system are EXACTLY w:** the preceding competitor bounds control every diagonal by O(delta^wi), while the matching monomial curve is uniformly PD after normalization and supplies a lower Loewner bound; the universal analytic-center envelope of checkpoint09 transfers it to C_delta. This observation is not needed for the next direct minimality proof.

## IV. EXPLICIT SINGLE-ENTRY dual exposing stress for EVERY layer

At the first stage, choose Z1=Ekk∈K⊥. It exposes only terminal.

At any stage t>=2, let C_t be the desired suffix layer, and let b_t=j_(t−1)+1 be its PREVIOUSLY removed release vertex. Define one full ambient dual matrix
\[
\boxed{
Z_t=\sum_{i\in C_t}E_{ii}
               -\frac1{2\lambda}F_{0,b_t}.}
\tag{112.4}
\]
Its compression to the current face W_(j_(t−1)) is precisely the positive diagonal sum on C_t; the only offdiagonal term touches the already removed vertex b_t, so it is OFF-FACE. Hence the compressed stress is PSD and PD on exactly C_t.

We verify **Z_t∈K⊥ for EVERY original generator**, despite the shared edge:
- If i∈C_t, the generator H_i includes f_t=(0,b_t) exactly ONCE (as harmonic anchor or as tied release); the positive diagonal pairing contributes +1 and the F_f pairing contributes −1.
- If i∉C_t, neither its release edge nor its harmonic anchor equals f_t. Other stage release vertices are distinct. If its harmonic anchor P_i=(0,b_t), then \(2w_i=w_{b_t}\), so i is exactly the FIRST index with \(2w_i\ge w_{b_t}\), namely i=ell(j_(t−1))+1=j_t+1, which BELONGS to C_t. Thus an outside i cannot have that anchor. Its diagonal also pairs to zero.
Therefore all <Z_t,H_i>=0, and (112.4) is a VALID full measurement stress. It exposes the exact suffix, giving a facial-reduction chain of length **L(w)**.

## V. MINIMALITY directly from the ORIGINAL kernel coefficients (NO graph theorem)

All H_i have positive (i,i) diagonal and obey the exact support bound
\[
(H_i)_{ab}=0\quad\text{whenever }w_a+w_b>2w_i,
\]
including all shared release edges. At the initial face any PSD exposing stress S annihilates the target source row. Choose the smallest internal index i with Sii>0. Every null-null block of H_i involving a higher-index vertex has its other endpoint STRICTLY below i by the support inequality; the corresponding row of S is zero by minimality of i. Every source cross pairs to zero. Thus
    0=<S,H_i>=Sii>0,
contradiction. Hence NO first stress can expose an internal coordinate; the terminal-only first step is unavoidable.

More generally, suppose after some stages the current (possibly rotated) feasible face contains
\(W_j=U_0+\operatorname{span}(e_1,\ldots,e_j)\).
For every internal index \(i\le\ell(j)\), the support inequality and \(2w_i<w_{j+1}\) force H_i∈K∩S(W_j). Pair the compressed PSD exposing stress S with H1,...,H_ell in order. If the earlier i−1 rows vanish, every possible nonzero null-null entry of H_i touching a higher index pairs with one of those zero rows, while the (i,i) entry is positive. PSD complementarity forces Sii=0 and the entire i-th row to vanish. Hence the next face still contains \(W_{\ell(j)}\).

Iterating the forced survivor recurrence from the unavoidable first terminal step shows that **EVERY** facial-reduction chain has length at least L(w). The explicit length-L(w) chain (112.4) proves the MINIMAL singularity degree equals L(w), without using the maxdet theorem or any depth-preserving sparse graph assumption. QED.

## VI. Leading exponent alpha < w1 and higher target rank

If an independent source-to-v leading kernel generator \(G=\lambda F_{0v}\) is added, with \(\alpha=w_v/2<w_1\), all global recovery estimates and the matching PD curve remain valid: the edge (0,v) is never a harmonic anchor (otherwise some wi=alpha<w1). If it is also distinct from EVERY release edge f_t, the exposing stresses (112.4) remain in the new K⊥, so the exact degree is still L(w), and the sharp exponent becomes alpha.

If (0,v) COINCIDES with one of the f_t, the specific stress (112.4) is no longer orthogonal to G, so **the rank-one proof above DOES NOT cover that case**. This is a genuine fixed-nullity/rank-one collision issue, not something silently ignored.

For target rank r>=2, add one fully measured positive support coordinate u beyond source0, take target E00+Euu and place the independent leading generator on \(F_{u,v}\) instead of \(F_{0,v}\). All release stresses use source0 rows and hence are automatically orthogonal to G; all full-PSD estimates and matching curves remain valid after the obvious block-diagonal positive padding. No extra NULL direction is introduced. Thus for EVERY harmonic leading half-weight alpha, the lower peeling bound L(w) is attained at original nullity k for any target rank r>=2.

## Audit and impact

The independent exact Fraction checker in checkpoint113 verifies, for all 1,3,18,165,2099 strict harmonic parent policies at h=1,...,5:
1. every release edge is Bellman-subleading;
2. every shared generator has the stated anchor upper-triangular interference;
3. EACH explicit stress (112.4) pairs to zero with every generator;
4. the complete exposed suffix chain has length exactly L(w);
5. the H_i weighted support inequalities needed by the direct global minimality proof hold.

This is a **DIMENSION-PRESERVING theorem** for one of the two universal peeling extremes, and a concrete new shared-edge PSD coupling beyond globally disjoint two-edge modes. It does NOT yet prove fixed-nullity realizability of the UPPER extreme or every intermediate d, and does not settle the rank-one optional-leading-edge collision. The all-nullity joint exponent/degree arithmetic spectrum remains open.

Standard facial reduction and PSD inequality methods are prior art; external specialist review and literature priority audit remain necessary.