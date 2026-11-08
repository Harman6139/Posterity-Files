# Milestone 102 — explicit rational 7×7 PSD example: sharp exponent 13/64, exact facial degree 5

**2026-11-08. Directly proved for the displayed rational inverse problem.** This new witness completes the one residual gap in the strict five-internal-vertex *two-extra-action* construction search. A finite enumeration theorem at nullity six is in the next checkpoint. This is an explicit full-ambient PSD example, not a formal network-only calculation.

## Statement and generators

Index coordinates 0,...,6. Let E_ii=e_i e_i^T, F_ij=e_i e_j^T+e_j e_i^T. Put λ=1/100, X*=E00, and define K=ker L as the span of **nine** rational symmetric matrices:

\[
\begin{array}{ll}
H_1=E_{11}-E_{00}+\lambda F_{03},
 &H_2=E_{22}-E_{00}+\lambda F_{05},\\
H_3=E_{33}-E_{00}+\lambda F_{06},
 &H_4=E_{44}-E_{00}+\lambda F_{16},\\
H_5=E_{55}-E_{00}+\lambda F_{46},&\\
J_2=E_{22}-E_{00}+\lambda F_{14},
 &J_3=E_{33}-E_{00}+\lambda F_{24},\\
J_4=E_{44}-E_{00}+\lambda F_{35},
 &G=\lambda F_{02}.
\end{array}
\]
Let L be Frobenius orthogonal projection onto K⊥, identified with Euclidean coordinates. The nine offdiagonal edges are globally unique, so the generators are independent. All are trace-zero and have terminal (6,6)-entry zero; identity and E66 are in K⊥.

**Claim.** X* is the unique PSD feasible point, the sharp full-matrix Hölder exponent is
\[
\boxed{\alpha=13/64}
\]
and the minimum facial-reduction degree and canonical rank drops are
\[
\boxed{d=5,\qquad(s_1,\ldots,s_5)=(1,1,1,2,1).}
\]

## 1. Exact Bellman values, including three strict slack inequalities

The five diagonal values solve the tight harmonic system
\[
2w_1=w_3,\quad 2w_2=w_5,\quad 2w_3=1,\quad
2w_4=w_1+1,\quad 2w_5=w_4+1.
\]
The unique solution is
\[
(0,w_1,w_2,w_3,w_4,w_5,w_6)
=(0,1/4,13/32,1/2,5/8,13/16,1).
\]
The three extra independent actions are all strictly Bellman slack:
\[
\begin{aligned}
(w_1+w_4)/2&=7/16>13/32=w_2,\\
(w_2+w_4)/2&=33/64>1/2=w_3,\\
(w_3+w_5)/2&=21/32>5/8=w_4.
\end{aligned}
\]
The optional independent edge G=(0,2) has exponent w2/2=13/64, strictly smaller than w1=1/4. Hence the exact *global* exponent follows from the multi-action theorem of checkpoint57. The next two sections give independent direct checks.

## 2. Upper bound against arbitrary PSD competitors

Given X≽0 with ||L(X−X*)||_F≤δ, put Y=X*+P_K(X−X*) and E=X−Y. Then ||E||_F≤δ, Y+δI≽0, trY=1, Y66=0 and its diagonal variables are bounded by trace control. Set Ui=|Yii|+δ, so U0=O(1), U6=δ.

Because each generator has its own globally unique parent edge, its scalar coefficient is bounded by the 2×2 principal minor of Y+δI on that edge. Summing coefficients that contribute to one internal diagonal gives fixed C with
\[
\begin{aligned}
U_1&\le C(\delta+\sqrt{U_0U_3}),\\
U_2&\le C(\delta+\sqrt{U_0U_5}+\sqrt{U_1U_4}),\\
U_3&\le C(\delta+\sqrt{U_0U_6}+\sqrt{U_2U_4}),\\
U_4&\le C(\delta+\sqrt{U_1U_6}+\sqrt{U_3U_5}),\\
U_5&\le C(\delta+\sqrt{U_4U_6}).
\end{aligned}
\]
All edge averages are at least the displayed Bellman weights wi and each vertex has one tight action. The finite weighted maximum principle (proved in checkpoint57) yields, with constants independent of X and δ,
\[
U_i=O(\delta^{w_i})\quad(i=1,\ldots,5).
\]
The leading coefficient z of G satisfies |z|≤C√(U0U2)=O(δ^{13/64}). All other kernel coefficients are O(δ^{wi}) by their unique edges; the source diagonal is controlled by the measured trace, and the projection error E is O(δ). Thus
\[
\|X-X_*\|_F=O(\delta^{13/64})
\]
for **all** ambient PSD competitors. In particular uniqueness follows as δ→0.

## 3. Matching strictly PD perturbation

For s>0 small define
\[
X(s)=E_{00}
+s^{16}H_1+s^{26}H_2+s^{32}H_3+s^{40}H_4+s^{52}H_5
+s^{13}G+s^{64}E_{66}.
\]
All three slack J generators have coefficient zero. The seven diagonal entries are
\[
1-s^{16}-s^{26}-s^{32}-s^{40}-s^{52},
s^{16},s^{26},s^{32},s^{40},s^{52},s^{64}.
\]
They are positive with source diagonal greater than 1/2 for sufficiently small s. Diagonal congruence makes every selected offdiagonal edge at most 2λ=1/50 in modulus; each row has at most six such entries, hence strict diagonal dominance gives **positive definiteness of the full 7×7 matrix**. Since the five H_i and G are in K and E66 is in K⊥,
\[
\|L(X(s)-X_*)\|_F=s^{64},\qquad
\|X(s)-X_*\|_F=\Theta(s^{13}).
\]
So α=13/64 is exactly sharp.

## 4. Five exact exposing stresses and minimality

Let c=1/(2λ)=50 and set
\[
\begin{array}{ll}
Z_1=E_{66},&
Z_2=E_{55}-cF_{46},\\
Z_3=E_{44}-c(F_{16}+F_{35}),&
Z_4=E_{22}+E_{33}-c(F_{05}+F_{14}+F_{06}+F_{24}),\\
Z_5=E_{11}-cF_{03}.&
\end{array}
\]
Every listed Z_j has ZERO Frobenius pairing with every one of the nine kernel generators: for each H_i/J_i the positive diagonal contributes 1 and the corresponding \(-cF_{ab}\) contributes \(-2cλ=-1\); the remaining pairings vanish by distinct edge supports. Each Z_j also pairs to zero with G=λF02.

Their compressions to successive current coordinate faces are PSD and equal to
\[
E_{66},\quad E_{55},\quad E_{44},\quad E_{22}+E_{33},
\quad E_{11},
\]
with the previously exposed rows removed in that order. This yields a valid degree-five chain.

**Minimality for every arbitrary compressed PSD stress.** At the first face, source row0 is zero. H1 forces row1 zero; H2 forces row2 zero; H3 forces row3 zero; H4 forces row4 zero (its parent edge touches already-zero row1); H5 forces row5 zero (its edge touches row4). Thus every first PSD stress is supported on coordinate6; Z1 achieves rank one.

After removing6, source row0 is still zero. H1 forces row1 zero, H2 forces row2 zero, J3 forces row3 zero using zero row2, and J4 forces row4 zero using zero row3. Only coordinate5 can be exposed; Z2 achieves it.

After removing5 and6, H1 forces row1 zero, J2 forces row2 zero via row1, J3 forces row3 zero via row2. Only coordinate4 is eligible; Z3 achieves it.

After removing4, H1 forces row1 zero, while Z4 exposes both coordinates2 and3. Finally Z5 removes coordinate1. Hence each step has the stated MAXIMAL exposing rank and the **minimum singularity degree is exactly five**.

## Significance

This witness shows that the grade-only necessary interval can require *three* independent Bellman-slack actions for realization at a prescribed nonmaximal degree. The earlier two-extra-action search missed exactly 13/64 for (five internal vertices,d=5); the additional edge fills that gap without needing any tied coefficient.

The construction preserves nullity six and exact degree five, and positive support padding gives any positive target rank r. It is a nontrivial new sharp exponent/profile realization, not a generic double-counting or dimension-padding shortcut. The complete finite all-degree nullity-six classification that uses this witness is checkpoint103.
