# Milestone 58 — SIX-BY-SIX COUNTEREXAMPLE to the proposed single-action universal depth spectrum

Date: 2026-11-08. **FULLY PROVED**: a real rational 6×6 uniquely solvable PSD inverse problem has sharp Frobenius exponent 7/32, target rank one/nullity five, and EXACT minimal facial-reduction degree four; no single-action harmonic midpoint network (nor any vertex blow-up of one) in that target nullity can realize this exponent at depth four. The stronger statement concerns *the insufficiency of the earlier proposed combinatorial normal form*, not the impossibility of a full universal classification with richer hypergraph data.

This is a genuine new mechanism: one **slack, non-optimal parent action** changes the exact facial-reduction timing without changing the sharp exponent.

## 1. An explicit rational measurement kernel

Index coordinates 0,1,2,3,4,5. Write E_ii=e_i e_i^T and F_ij=e_i e_j^T+e_j e_i^T. Fix lambda=1/100 and target X*=E_00∈S^6. Define K as the span of six explicit matrices:
\[
\begin{aligned}
H_1&=E_{11}-E_{00}+\lambda F_{03},\\
H_2&=E_{22}-E_{00}+\lambda F_{14},\\
H_3&=E_{33}-E_{00}+\lambda F_{05},\\
H_3'&=E_{33}-E_{00}+\lambda F_{24},\\
H_4&=E_{44}-E_{00}+\lambda F_{15},\\
G&=\lambda F_{02}.
\end{aligned}
\tag{1}
\]
Let L be Frobenius orthogonal projection onto K⊥ (identified with Euclidean measurement coordinates). Every kernel generator has trace zero, so I∈K⊥ and trace is measured. All generators have (5,5)-entry zero, so E_55∈K⊥ and the terminal diagonal is measured. The kernel is exactly K.

## 2. Exact sharp exponent 7/32: full PSD upper bound

Let X≽0 have measurement residual at most δ. Set Y=X*+P_K(X-X*) and E=X-Y, so ||E||_F<=δ and Y+δI≽0. Trace control bounds the diagonal entries and, in particular, Y_00. Write Y as
\[
Y=E_{00}+aH_1+bH_2+cH_3+eH_3'+fH_4+zG.
\]
The internal diagonal coordinates are x1=a, x2=b, x3=c+e, x4=f, while Y55=0 and Y00=1-a-b-c-e-f. Put U_i=|x_i|+δ for i=1,...,4, U_0=|Y00|+δ=O(1), and U_5=δ.

Distinct action edges allow the five principal 2×2 PSD inequalities:
\[
\begin{aligned}
U_1&\le C U_3^{1/2}, \qquad &(0,3)\text{ for }H_1,\\
U_2&\le C(U_1U_4)^{1/2}, &(1,4)\text{ for }H_2,\\
U_3&\le C(\delta^{1/2}+(U_2U_4)^{1/2}), &(0,5),(2,4)\text{ for }H_3,H_3',\\
U_4&\le C(\delta U_1)^{1/2}, &(1,5)\text{ for }H_4.
\end{aligned}
\tag{2}
\]
Here harmless +δ terms are absorbed because δ<=U_i and δ<=δ^(1/2); constants are independent of the competitor and small δ.

Successive substitution gives
\[
U_1\le C U_3^{1/2},\quad
U_4\le C\delta^{1/2}U_3^{1/4},\quad
U_2\le C\delta^{1/4}U_3^{3/8},
\]
and hence
\[
U_3\le C\left(\delta^{1/2}+\delta^{3/8}U_3^{5/16}\right).
\tag{3}
\]
The elementary inequality x<=a+b*x^p with p<1 implies x<=2a+(2b)^(1/(1-p)). Applying this to (3), since
    (3/8)/(1-5/16)=6/11>1/2,
gives U3=O(δ^(1/2)). It follows that
\[
U_1=O(\delta^{1/4}),\quad
U_2=O(\delta^{7/16}),\quad
U_3=O(\delta^{1/2}),\quad
U_4=O(\delta^{5/8}).
\tag{4}
\]
The independent leading edge G lies at (0,2), so its principal-minor inequality gives
\[
|z|\le C(U_0U_2)^{1/2}=O(\delta^{7/32}).
\]
Each other generator coefficient is controlled by its own edge principal minor, with order at least 1/4; trace controls Y00−1 and ||E||≤δ controls all off-pencil entries. Thus
\[
\boxed{\|X-X_*\|_F\le C\delta^{7/32}}
\tag{5}
\]
against **every** ambient PSD competitor. Sending δ→0 proves uniqueness.

## 3. Exact matching strictly positive-definite polynomial curve

Let t=s^32 and set
\[
\boxed{
X(s)=E_{00}+s^8H_1+s^{14}H_2+s^{16}H_3+s^{20}H_4
+s^7G+s^{32}E_{55}.
}
\tag{6}
\]
The coefficient of H3' is zero. Its six diagonal entries are
    1−s^8−s^14−s^16−s^20,\quad s^8,\quad s^14,\quad s^16,\quad s^20,\quad s^32.
For 0<s<=1/2 the source diagonal exceeds 1/2. Diagonal normalization sends the five nonzero offdiag edges to absolute entries lambda or lambda/sqrt(X00), bounded by 2lambda=1/50. The offdiagonal row sums are at most 5/50<1. By strict diagonal dominance the **entire matrix is positive definite**, not merely its two-by-two principal minors.

Since every H_i and G belongs to K and E55∈K⊥,
\[
\|\mathcal L(X(s)-X_*)\|_F=s^{32},\qquad
\|X(s)-X_*\|_F=\Theta(s^7).
\]
Equations (5)–(6) prove the exact sharp exponent
\[
\boxed{\alpha=7/32}.
\]

## 4. Exact minimal facial rank-drop profile (1,1,2,1)

We exhibit four exposing stresses in K⊥. Their full matrices need not be globally PSD after the first step; only their current-face compressions must be PSD:
\[
\begin{aligned}
Z_1 &= E_{55},\\
Z_2 &= E_{44}-\frac1{2\lambda}F_{15},\\
Z_3 &= E_{22}+E_{33}
       -\frac1{2\lambda}(F_{14}+F_{05}+F_{24}),\\
Z_4 &= E_{11}-\frac1{2\lambda}F_{03}.
\end{aligned}
\tag{7}
\]
Direct Frobenius pairings with all six generators in (1) are zero. The successive compressions to current faces supported on indices
  {0,1,2,3,4,5}, {0,1,2,3,4}, {0,1,2,3}, {0,1}
are, respectively,
    E55, E44, E22+E33, E11.
Thus degree at most four and the displayed rank profile is feasible.

To prove minimality and maximal exposing ranks, let Z∈K⊥ be an arbitrary exposing stress on any current face:
- First face: PSD and <Z,X*>=0 annihilate source row 0. H1 forces Z11=0 and hence row 1 zero; H3 forces Z33=0 and row 3 zero; H2 then forces Z22=0; H4 then forces Z44=0. Thus every first PSD stress has support only on e5. First exposed rank is EXACTLY 1.
- After removing e5: the compressed PSD stress still annihilates source. H1 kills row 1; H2 then kills row 2; H3' then kills row 3 (the entry Z24 is zero because row2 vanishes). Thus every second exposing stress is supported only on e4. Rank EXACTLY 1.
- After removing e4: H1 still kills row 1, while the explicitly given Z3 exposes both e2,e3. Third maximal rank is EXACTLY 2.
- The final face retains one null direction e1 and the explicit Z4 removes it. Fourth rank is 1.

Hence the **canonical maximal-rank facial reduction degree is exactly four**, and
\[
\boxed{(s_1,s_2,s_3,s_4)=(1,1,2,1).}
\tag{8}
\]

## 5. Why this disproves the proposed single-action universal depth spectrum

The formerly proposed universal combinatorial rule allowed only ONE parent pair per internal diagonal variable, optionally duplicating vertices without changing their peeling time (checkpoints 52 and 55). We show it cannot represent the pair (nullity ν=5, depth d=4, alpha=7/32).

For any single-action harmonic midpoint graph, the reduced denominator of 2alpha=7/16 divides the integer midpoint determinant, which is at most 2^h for h internal vertices. Thus h>=4. Target nullity ν=5 implies h<=4, hence h=4 and **there is no room for any vertex blow-up**.

There are exactly (4!)²=576 possible ordered choices of one lower and one higher parent for four internal vertices. Solving their rational midpoint equations and imposing strictly increasing weights, 2alpha as an internal/terminal weight and alpha<=min internal weight leaves EXACTLY four graphs:
1. weights (1/4,7/16,1/2,5/8), parent pairs (0,3),(1,4),(0,5),(1,5); peeling layers {5},{3,4},{1,2}.
2. weights (7/16,1/2,3/4,7/8), pairs (0,4),(0,5),(2,5),(3,5); peeling layers {5},{2,3,4},{1}.
3. weights (3/8,7/16,1/2,3/4), pairs (0,4),(1,3),(0,5),(3,5); peeling layers {5},{3,4},{1,2}.
4. weights (1/4,3/8,7/16,1/2), pairs (0,4),(1,4),(2,4),(0,5); peeling layers {5},{4},{1,2,3}.

Every one has peeling **degree three**, not four. The attached standalone Fraction script verifies this finite list exactly. Therefore the concrete valid PSD instance (1)–(8) is a rigorous counterexample to the conjecture that a *single-action harmonic midpoint graph*, even with vertex blow-ups, reproduces every attainable sharp exponent–minimal-degree pair.

**The extra action is H3'=E33−E00+λF24.** Its parent average (w2+w4)/2=(7/16+5/8)/2=17/32 is strictly larger than the Bellman-optimal w3=1/2. Thus adding it does not change the sharp exponent. But it prevents vertex 3 from being exposed together with vertex 4, postponing exposure and increasing the minimal degree from 3 to 4. This is the new independent instability/depth mechanism.

Two analogous counterexamples exist at the same (ν,d) with exponents 5/32 and 7/24 (checkpoint 59); 7/32 alone suffices for the decisive conclusion.

## Exact conclusion and nonconclusion

**DISPROVED:** the conjectural universal necessity Σ_(ν,d)=single-action harmonic-peeling catalogue (even after exact vertex blow-ups). The failure occurs at (ν,d)=(5,4), the first nullity beyond the completed dense ν≤4 cases.

**NOT DISPROVED:** existence of a richer finite purely combinatorial universal classification, for example by controlled multi-action midpoint networks. Checkpoint 57 proves that this richer family has exact computable exponents and facial degrees, but no theorem currently proves that EVERY dense PSD problem reduces to it. The global user goal of a full universal all-value (ν,d) classification is therefore still open.

**Literature:** standard facial reduction and stochastic Bellman methods are prior tools. The counterexample and its full PSD proofs are self-contained; priority relative to previous 2026 literature remains to be checked.