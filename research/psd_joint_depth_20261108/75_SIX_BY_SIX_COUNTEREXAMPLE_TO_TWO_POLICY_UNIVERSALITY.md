# Milestone 75 — decisive SIX-BY-SIX counterexample to the proposed TWO-POLICY universal PSD exponent/depth classification

**Date: 2026-11-08. PROVED directly from explicit matrices, arbitrary-competitor bounds, exactly verified dual stresses, and exhaustive 576-case rational exclusion.**

The earlier proposed universal inclusion
\[
\Sigma_{\nu,d}^{\rm arbitrary\ dense}\subseteq
\Sigma_{\nu,d}^{\rm strict\ independent\!-\!edge\ two\!-\!policy}
\]
is **FALSE**, already at positive target rank one, target nullity ν=5, degree d=3, and optimal Hölder exponent α=3/22. This is a counterexample to the numerical exponent–degree spectrum, not merely to a particular rank-drop profile. The proposed two-policy normal form must be enlarged, for example to the **tied-edge MIN–MAX stochastic-game model** of checkpoint 74. Whether the latter is universal for all dense kernels is still OPEN.

## 1. Explicit rational 6×6 measurement kernel

Index coordinates 0,1,2,3,4,5. Put E_ii=e_i e_i^T and F_ij=e_i e_j^T+e_j e_i^T. Take λ=1/100, target X*=E00, and let K=ker L be the span of these five rational matrices:
\[
\begin{aligned}
H_1&=E_{11}-E_{00}+\lambda F_{02},\\
H_2&=E_{22}-E_{00}+\lambda(F_{05}+F_{14}),\\
H_3&=E_{33}-E_{00}+\lambda F_{15},\\
H_4&=E_{44}-E_{00}+\lambda F_{35},\\
G&=\lambda F_{01}.
\end{aligned}
\tag{1}
\]
Take L to be orthogonal projection onto K^\perp in the Frobenius metric. Every generator is trace-zero and has terminal diagonal (5,5) zero; hence identity and E55 belong to the measured span. The two offdiagonals F05 and F14 are **tied to the same kernel coefficient H2**. This coupling cannot be modeled as two independently selectable generators without changing the stability/depth pair.

## 2. Direct sharp upper bound against EVERY ambient PSD competitor

Let X≽0 have residual ||L(X-X*)||_F≤δ. Put
    Y=X*+P_K(X-X*),   E=X−Y,
so ||E||_F≤δ, Y+δI≽0, tr(Y)=1 and Y55=0. Write
    Y=E00+aH1+bH2+cH3+dH4+zG.
The only action offdiagonals are
    Y02=λa, Y05=Y14=λb, Y15=λc, Y35=λd, Y01=λz.
Let U_i=|Y_ii|+δ, so U0=O(1), U5=δ and U_i≥δ. Each principal 2×2 minor of Y+δI yields, with a fixed C,
\[
\begin{split}
U_1&\le C\sqrt{U_2},\\
U_2&\le C\min(\sqrt\delta,\sqrt{U_1U_4}),\\
U_3&\le C\sqrt{\delta\,U_1},\\
U_4&\le C\sqrt{\delta\,U_3}.
\end{split}
\tag{2}
\]
The harmless additive δ is absorbed because every U_i≥δ and the square-root terms are at least δ after a suitable fixed enlargement of C. Substitute successively:
\[
U_4\le C\delta^{3/4}U_1^{1/4},\quad
U_2\le C\delta^{3/8}U_1^{5/8},\quad
U_1\le C\delta^{3/16}U_1^{5/16}.
\]
Hence \(U_1^{11/16}\le C\delta^{3/16}\), which yields
\[
U_1=O(\delta^{3/11}),\
U_2=O(\delta^{6/11}),\
U_3=O(\delta^{7/11}),\
U_4=O(\delta^{9/11}).
\]
The independent leading edge G satisfies
    |z|≤C sqrt(U0U1)=O(δ^{3/22}).
The diagonal variables a,b,c,d are controlled by the corresponding U_i; trace controls Y00−1, and ||E||≤δ controls every unstructured entry of X. Therefore
\[
\boxed{\|X-X_*\|_F\le C\delta^{3/22}}
\tag{3}
\]
for ALL X≽0. Sending δ→0 also establishes uniqueness of the PSD solution.

## 3. Matching STRICTLY positive-definite perturbation curve

Let s>0 be sufficiently small and set
\[
X(s)=E_{00}+s^6H_1+s^{12}H_2+s^{14}H_3+
                     s^{18}H_4+s^3G+s^{22}E_{55}.
\tag{4}
\]
Its diagonal entries are
    1−s^6−s^12−s^14−s^18,\quad s^6,\quad s^12,\quad s^14,\quad s^18,\quad s^22,
all strictly positive for small s. After scaling rows/columns by inverse square roots of their diagonal entries, all six nonzero offdiagonal entries are bounded in magnitude by 2λ=1/50 (the tied F05 edge is actually smaller by an extra factor s). Since every row has at most five nonzero offdiagonals, normalized strict diagonal dominance makes **the whole matrix positive definite**.

Every H_i and G lies in K, while E55∈K^\perp. Thus
\[
\|L(X(s)-X_*)\|_F=s^{22},\qquad
\|X(s)-X_*\|_F=\Theta(s^3).
\]
The sharp exponent is therefore
\[
\boxed{\alpha=3/22}.
\tag{5}
\]

## 4. EXACT minimal singularity degree 3 and rank profile (1,3,1)

Define
\[
\begin{aligned}
Z_1 &= E_{55},\\
Z_2 &= E_{22}+E_{33}+E_{44}
       -\frac1{2\lambda}(F_{05}+F_{15}+F_{35}),\\
Z_3 &= E_{11}-\frac1{2\lambda}F_{02}.
\end{aligned}
\tag{6}
\]
All three matrices belong to K^\perp: their Frobenius pairings with EACH generator in (1) vanish exactly. Their compressions to the successive current faces supported on indices
    {0,1,2,3,4,5}, {0,1,2,3,4}, and {0,1}
are, respectively, the PSD matrices
    E55, E22+E33+E44, E11.

To prove the **MINIMAL** degree and maximum rank drops, let Z be any PSD first exposing stress in K^\perp. Since Z pairs to zero with X*=E00, its entire source row/column vanishes. Pairing with H1 forces Z11=0 and its row; pairing H3 then forces Z33=0; pairing H4 forces Z44=0; pairing H2 forces Z22=0. Thus every first exposing stress is supported solely on e5, so the first maximal rank drop is EXACTLY one.

After removing e5, H1 still forces Z11=0 for every PSD compressed exposing stress. Therefore the second exposed rank is at most three; Z2 attains all three directions e2,e3,e4 simultaneously, so the second maximal rank drop is EXACTLY three. Z3 finally exposes e1. Hence
\[
\boxed{d=3,\qquad(s_1,s_2,s_3)=(1,3,1),\qquad\nu=5.}
\tag{7}
\]
No hidden sparsity assumption on exposing stresses is used.

## 5. NO independent-edge two-policy realization with the same (ν,d,α)

Assume an arbitrary STRICT independent-edge midpoint/Bellman incidence system of target nullity ν=5, possibly with vertex blow-ups, had α=3/22 and minimal degree d=3. Let h be its number of distinct internal weight levels. The integer reduced denominator of 2α=3/11 is 11. Picking one Bellman-optimal parent action per internal vertex gives an h×h midpoint matrix whose positive integer determinant is ≤2^h and is divisible by 11. Consequently h≥4. Since ν=h+1 plus any clone excess, ν=5 forces **h=4 with no clone multiplicities**.

For h=4, each internal i has i(5−i) possible lower/higher parent pairs. There are exactly
    (4·6·6·4)=(4!)²=576
single-action parent policies. Solve each 4×4 rational harmonic system and retain precisely those with
    0<w1<w2<w3<w4<1,
    3/11 in {w1,w2,w3,w4,1},
    α=3/22≤w1.
**Exactly TWO policies survive**:
\[
\begin{array}{c|c|c}
\text{weights }(w_1,w_2,w_3,w_4)&
\text{optimal parent pairs}&
\text{single-action peeling layers}\\
(3/11,6/11,7/11,9/11)&
(0,2),(1,4),(1,5),(3,5)&
\{5\},\{3,4\},\{2\},\{1\}\\
(3/11,5/11,6/11,7/11)&
(0,3),(1,4),(2,4),(1,5)&
\{5\},\{4\},\{2,3\},\{1\}.
\end{array}
\]
Both policies require EXACTLY four exposing steps; the first and second rows have different explicit peeling orders. The exact verifier computes these from the displayed parent pairs.

Adding independent additional actions can **only DELAY** facial exposure, never advance a vertex: the all-actions closure conditions are strengthened when actions are added, and the monotone tropical exposing-time theorem (checkpoint 59) makes this explicit. Thus every independent-edge multiaction system containing either optimal harmonic policy has minimal degree at least FOUR. A two-policy subfamily certainly cannot achieve degree three. This contradicts the proposed realization.

The finite two-policy exclusion is certified by the companion self-contained exact Fraction script (checkpoint 76), which enumerates all 576 policies, checks the rational solutions and their peeling stages, and independently checks the symbolic stress identities of (6). The finite enumeration is exact, not probabilistic or numerical.

Hence
\[
\boxed{
( \nu,d,\alpha )=(5,3,3/22)
\in\Sigma^{\rm all\ PSD}
\setminus\Sigma^{\rm strict\ independent\!-\!edge\ two\!-\!policy}.
}
\]
This is the sought rigorous **COUNTEREXAMPLE to the previously conjectured universal necessity** of the two-policy incidence model at the same nullity and degree.

## 6. Mathematical interpretation and current frontier

The mode H2 has two distinct offdiagonal edges **controlled by the same scalar coefficient b**. One edge (1,4) gives the sharp order \(w_2=(w_1+w_4)/2=6/11\), while the other (0,5) has smaller parent average \(1/2\) and is therefore irrelevant to the maximum controlling recovery. Yet the edge touching terminal 5 allows its dual orthogonality equation to be satisfied off-face after the first reduction, enabling e2 to be exposed together with e3,e4 at step two. Splitting H2 into independently controllable parent actions destroys this coupling; the resulting minimum-over-actions Bellman operator cannot reproduce both invariants.

The natural richer object is the **MIN over generator modes, MAX over tied edges** stochastic game of checkpoint 74, with a dual AND/OR facial-peeling rule. The example proves that an explicitly stronger combinatorial normal form is required at the level of the universal exponent–degree spectrum.

**Still open:** prove or disprove that EVERY arbitrary dense PSD inverse problem has an equivalent tied-edge min–max game certificate preserving target nullity, sharp exponent and minimal facial rank profile. No such universal dense reduction is asserted here. Classical Gordan–Stiemke facial reduction, stochastic Shapley games and nonarchimedean spectrahedra are established prior areas; the concrete counterexample and its full-matrix proof are self-contained, with bibliographic priority unverified.