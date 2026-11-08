# Milestone 96 — an exact 6×6 tied-edge PSD witness: exponent 3/20 at minimal facial degree 3

**Date 2026-11-08. Fully proved directly from explicit rational matrices**, with an all-PSD-competitor Hölder upper bound, a matching full positive-definite monomial curve, and exact maximum-rank exposing stresses. This provides the final missing constructive value for the newly completed target-nullity-five / degree-three spectrum (checkpoint 97), alongside the separate 3/22 construction in checkpoint 75.

## Theorem

There exists a rational linear measurement map on S^6 with uniquely recoverable rank-one PSD target X*=E00, target nullity ν=5, **exact minimal singularity degree d=3**, canonical exposed-rank profile (1,3,1), and sharp full ambient recovery exponent
\[
\boxed{\alpha=\frac3{20}.}
\]
The critical construction feature is one generator tying two offdiagonal edges whose second edge is *subleading for recovery but releases a dual facial exposure*.

## Explicit kernel and measurements

Index coordinates 0,1,2,3,4,5. Write \(E_{ii}=e_ie_i^T\) and \(F_{ij}=e_ie_j^T+e_je_i^T\). Fix \(\lambda=1/100\). Let \(K=\ker L\) be the span of the five rational matrices
\[
\begin{aligned}
H_1&=E_{11}-E_{00}+\lambda F_{02},\\
H_2&=E_{22}-E_{00}+\lambda(F_{14}+F_{05}),\\
H_3&=E_{33}-E_{00}+\lambda F_{25},\\
H_4&=E_{44}-E_{00}+\lambda F_{35},\\
G&=\lambda F_{01}.
\end{aligned}
\tag{96.1}
\]
Take L to be orthogonal projection to K^\perp in Frobenius coordinates. Every generator has trace zero and no (5,5) diagonal, so identity and E55 are measured.

## Sharp recovery UPPER BOUND for EVERY PSD competitor

For X≥0 with ||L(X−X*)||≤δ put
  Y=X*+P_K(X−X*), E=X−Y.
Then ||E||≤δ, Y+δI≥0, trY=1, Y55=0 and Y00=O(1). Write Y=E00+aH1+bH2+cH3+dH4+zG. For δ≤1 define U_i=|Y_ii|+δ, so U5=δ and U0=O(1), with Ui≥δ. The unique offdiagonal support of each coefficient gives by principal 2×2 minors:
\[
\begin{split}
U_1&\le C U_2^{1/2},\\
U_2&\le C\min\{\sqrt{U_1U_4},\sqrt\delta\},\\
U_3&\le C\sqrt{U_2\delta},\\
U_4&\le C\sqrt{U_3\delta}.
\end{split}
\tag{96.2}
\]
(Each bound can absorb an additive δ because Ui≥δ and all quantities are bounded; enlarge C once.)

Using the first, third and fourth inequalities,
\[
U_4\le C\delta^{3/4}U_2^{1/4},
\quad
U_2\le C\sqrt{U_1U_4}\le C\delta^{3/8}U_2^{3/8}.
\]
Thus \(U_2^{5/8}\le C\delta^{3/8}\), giving
\[
U_2=O(\delta^{3/5}),\
U_1=O(\delta^{3/10}),\
U_3=O(\delta^{4/5}),\
U_4=O(\delta^{9/10}).
\]
The independent leading edge G at (0,1) yields \(|z|\le C\sqrt{U_0U_1}=O(\delta^{3/20})\). Every remaining kernel coefficient is controlled by its diagonal coordinate or a unique parent edge, and trY=1 controls Y00−1. Together with ||E||≤δ this gives
\[
\boxed{\|X-X_*\|_F\le C\delta^{3/20}}
\]
for ALL ambient PSD X; in particular X* is the UNIQUE exact PSD solution.

## MATCHING strictly positive-definite curve

Let \(s>0\) be sufficiently small and set
\[
X(s)=E_{00}+s^6H_1+s^{12}H_2+s^{16}H_3
                  +s^{18}H_4+s^3G+s^{20}E_{55}.
\]
Its diagonal entries are
  \(1-s^6-s^{12}-s^{16}-s^{18},s^6,s^{12},s^{16},s^{18},s^{20}\),
all positive, with source diagonal >1/2 for small s. After diagonal congruence, every nonzero offdiagonal has modulus ≤2λ; the tied F05 edge even has an extra factor s². Each row has ≤5 such entries, so normalized strict diagonal dominance makes the FULL 6×6 matrix positive definite. Since H1,H2,H3,H4,G∈K and E55∈K^\perp with unit Frobenius norm,
\[
\|L(X(s)-X_*)\|_F=s^{20},
\qquad \|X(s)-X_*\|_F=\Theta(s^3).
\]
Thus the upper bound is sharp and the exact exponent is α=3/20.

## EXACT minimal facial degree and rank drops

Define three full dual matrices:
\[
\begin{aligned}
Z_1&=E_{55},\\
Z_2&=E_{22}+E_{33}+E_{44}
     -\frac1{2\lambda}(F_{05}+F_{25}+F_{35}),\\
Z_3&=E_{11}-\frac1{2\lambda}F_{02}.
\end{aligned}
\tag{96.3}
\]
Each has EXACTLY ZERO Frobenius inner product with all five generators in (96.1). Their compressions to the successive faces indexed by
  {0,1,2,3,4,5}, {0,1,2,3,4}, {0,1}
are respectively the PSD matrices
  E55, E22+E33+E44, E11.
Thus there is a valid three-step reduction with ranks (1,3,1).

Minimality: For any globally PSD first exposing stress Z∈K^\perp annihilating E00, its source row is zero. Pair H1 forces Z11=0 and entire row1 zero; pair H2 then forces Z22=0 because Z14=Z05=0; pair H3 forces Z33=0 because row2 vanishes; and pair H4 forces Z44=0 because row3 vanishes. Hence EVERY first exposing stress is supported only on coordinate5, so the first maximal rank drop is exactly one. After removing coordinate5, H1 still forces row1 of any PSD compressed exposing stress to vanish, so the next maximal rank drop is at most three; Z2 achieves rank three. The last direction is removed by Z3. Consequently
\[
\boxed{d=3,\qquad(s_1,s_2,s_3)=(1,3,1).}
\]

## Harmonic interpretation and relevance

The exact optimal value vector is
\[
(w_1,w_2,w_3,w_4,w_5)=
(3/10,3/5,4/5,9/10,1).
\]
The harmonic tight edges are (0,2),(1,4),(2,5),(3,5). The tied additional edge (0,5) has midpoint order 1/2, STRICTLY LOWER than w2=3/5, so it does not alter the sharp exponent. It does, however, allow the second stress to satisfy H2's orthogonality equation using an off-face entry after removing terminal5, exposing coordinates2,3,4 together instead of requiring a fourth step.

The independent-edge one-policy realization with these values has depth four, while the tied kernel has depth three. This is an explicit signed dual-cancellation mechanism, not a numerical conjecture.

All proof steps are exact rational linear algebra plus PSD principal minors and diagonal dominance. No dense-to-game universality hypothesis is used.
