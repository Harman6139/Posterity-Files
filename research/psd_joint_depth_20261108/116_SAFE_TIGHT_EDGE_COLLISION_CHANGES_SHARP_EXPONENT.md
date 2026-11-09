# Milestone 116 — EXACT counterexample to naïve collision-sharing at the UPPER peeling bound; and a universal collision-synchronization lemma

**2026-11-09. PROVED for explicit rational 7×7 PSD measurement data, with global competitor inequalities and a matching strictly PD curve.** The original Dikin/Bellman weights predict a desired exponent \(w_1=1/6\), but adding ONE purportedly Bellman-safe independent generator whose parent edge is already owned by a different child changes the true sharp exponent to **1/7**, despite retaining the intended four-step facial schedule. This demonstrates precisely why the global parent-edge uniqueness hypothesis in checkpoints 57/74 cannot simply be dropped. It does **not** disprove the all-nullity exponent/depth interval conjecture; it rules out one natural dimension-preserving construction.

## The explicit one-edge collision

Work on \(\mathbb S^7\), rows 0,...,6, with target \(X_*=E_{00}\), \(\lambda=1/100\), and \(E_{ii}=e_i e_i^\top,\ F_{ab}=e_ae_b^\top+e_be_a^\top\).

Start from the five tight parent pairs
\[
P_1=(0,3),\quad P_2=(0,5),\quad P_3=(1,4),\quad
P_4=(0,6),\quad P_5=(1,6).
\]
The corresponding strict harmonic weights are
\[
(w_0,w_1,\ldots,w_6)
=(0,\tfrac16,\tfrac7{24},\tfrac13,\tfrac12,\tfrac7{12},1).
\]
The canonical grade-only primal/dual peeling bounds are \(L(w)=3,\ U(w)=4\).
The **safe** nearest-parent edge at child 2 is
\[
e_2=(1,4),\qquad
(w_1+w_4)/2=\tfrac13>\tfrac7{24}=w_2.
\]
But \(e_2=P_3\), the tight parent edge of the DIFFERENT child 3. Rather than giving it a new clone, attach it as a separate mode at child 2, so the kernel becomes
\[
\begin{aligned}
H_1&=E_{11}-E_{00}+\lambda F_{03},\\
H_2&=E_{22}-E_{00}+\lambda F_{05},\\
H_3&=E_{33}-E_{00}+\lambda F_{14},\\
H_4&=E_{44}-E_{00}+\lambda F_{06},\\
H_5&=E_{55}-E_{00}+\lambda F_{16},\\
B_2&=E_{22}-E_{00}+\lambda F_{14}.
\end{aligned}
\tag{116.1}
\]
Let \(K=\mathrm{span}\{H_1,\ldots,H_5,B_2\}\) and \(L=P_{K^\perp}\) in Frobenius coordinates. All six generators are trace-free and have zero terminal diagonal, so trace and \(X_{66}\) are measured.

**THEOREM.** The target is uniquely PSD-recoverable, its exact optimal full-state Frobenius Hölder exponent and MINIMAL facial-reduction profile are
\[
\boxed{\alpha=\frac17,\qquad d=4,\qquad
(s_1,s_2,s_3,s_4)=(1,2,2,1).}
\tag{116.2}
\]
The original desired exponent \(w_1=1/6\) is NOT preserved by the added safe generator, even though its parent average is larger than \(w_2\).

## Complete proof of the sharp global exponent

Given arbitrary \(X\succeq0\) with \(\|L(X-E_{00})\|_F\le\delta\), write \(Y=E_{00}+P_K(X-E_{00})\), \(\|X-Y\|_F\le\delta\), so \(Y+\delta I\succeq0\), \(\mathrm{tr}Y=1\), \(Y_{66}=0\) and all diagonal coordinates are uniformly bounded. Write
\[
Y=E_{00}+aH_1+bH_2+cH_3+dH_4+eH_5+fB_2.
\]
Its nonzero structured offdiagonal entries are
\[
Y_{03}=\lambda a,\quad
Y_{05}=\lambda b,\quad
Y_{14}=\lambda(c+f),\quad
Y_{06}=\lambda d,\quad
Y_{16}=\lambda e.
\]
The internal diagonals are \(Y_{11}=a,\ Y_{22}=b+f,\ Y_{33}=c,\ Y_{44}=d,\ Y_{55}=e\).

Put \(U_i=|Y_{ii}|+\delta\), \(U_0=O(1)\), \(U_6=\delta\). Principal 2×2 PSD inequalities for \(Y+\delta I\) give
\[
\begin{aligned}
U_1&\le C\sqrt{U_3},\\
|b|&\le C\sqrt{U_5},\\
|c+f|&\le C\sqrt{U_1U_4},\\
U_4&\le C\delta^{1/2},\\
U_5&\le C\sqrt{U_1\delta}.
\end{aligned}
\tag{116.3}
\]
Here the harmless \(+\delta\) terms are absorbed using \(U_i\ge\delta\) and bounded diagonals. Positivity of the \(22\) and \(33\) diagonals of \(Y+\delta I\) means
\(b+f\ge-\delta\) and \(c\ge-\delta\). Hence
\[
c\le (c+f)+b+\delta
 \le C\bigl(\sqrt{U_1U_4}+\sqrt{U_5}+\delta\bigr)
\]
and therefore
\[
U_3\le C\left(\delta^{1/4}U_1^{1/2}
            +\delta^{1/4}U_1^{1/4}+\delta\right).
\]
Because \(U_1\) is uniformly bounded, the \(U_1^{1/2}\) term is dominated by a constant times \(U_1^{1/4}\). Combining with \(U_1\le C\sqrt{U_3}\) gives
\[
U_1^2\le C\delta^{1/4}U_1^{1/4}+C\delta.
\]
If the first term dominates, \(U_1^{7/4}\le C\delta^{1/4}\); otherwise \(U_1\le C\delta^{1/2}\). In both cases,
\[
\boxed{U_1=O(\delta^{1/7}).}
\]
Back-substitution gives
\[
U_3=O(\delta^{2/7}),\quad
|b|=O(\delta^{2/7}),\quad
U_5=O(\delta^{4/7}),\quad
U_4=O(\delta^{1/2}),
\]
and \(|f|\le|c+f|+|c|=O(\delta^{2/7})\), \(U_2=O(\delta^{2/7})\). Thus EVERY kernel coefficient, every structured matrix entry and the trace-controlled source diagonal are \(O(\delta^{1/7})\). Together with the projection error \(O(\delta)\),
\[
\boxed{\|X-X_*\|_F\le C\delta^{1/7}}
\]
for EVERY ambient PSD competitor. In particular \(X_*\) is the unique exact feasible PSD point.

For the matching PD curve set \(s>0\) small and
\[
X(s)=E_{00}+s^2H_1+2s^4H_2+s^4H_3
        +s^7H_4+s^8H_5-s^4B_2+s^{14}E_{66}.
\tag{116.4}
\]
The tied edge \(F_{14}\) cancels exactly, since its coefficient is \(\lambda(s^4-s^4)=0\). Diagonal entries are
\[
(1-s^2-2s^4-s^7-s^8,\ s^2,\ s^4,\ s^4,\ s^7,\ s^8,\ s^{14}).
\]
Every remaining offdiagonal, after diagonal congruence, has magnitude at most \(2\lambda\), with row sum <1. Thus the FULL matrix is strictly PD for small s. All generators belong to K, and E66 is measured with unit norm, so
\[
\|L(X(s)-X_*)\|_F=s^{14},\qquad
\|X(s)-X_*\|_F=\Theta(s^2).
\]
This proves the exact exponent \(2/14=1/7\).

## Exact minimal facial degree = 4

Put \(c_0=1/(2\lambda)=50\). The following four full matrices are in \(K^\perp\):
\[
\begin{aligned}
Z_1&=E_{66},\\
Z_2&=E_{44}+E_{55}-c_0(F_{06}+F_{16}),\\
Z_3&=E_{22}+E_{33}-c_0(F_{05}+F_{14}),\\
Z_4&=E_{11}-c_0F_{03}.
\end{aligned}
\tag{116.5}
\]
Their compressions to successive current coordinate faces are
\[
E_{66},\quad E_{44}+E_{55},\quad E_{22}+E_{33},\quad E_{11}.
\]
All 24 generator/stress Frobenius pairings vanish EXACTLY; each compression is PSD and positive on precisely the indicated exposed block.

For minimality, an arbitrary first globally PSD stress annihilating \(X_*=E_{00}\) has source row zero. Pairing with H1,H2,H4 forces rows 1,2,4 zero. Pairing B2 and H3 then forces row 3 zero; pairing H5 forces row5 zero. Therefore the FIRST stress can expose only 6. After removing 6, pairings with H1,H2,B2,H3 force rows1,2,3 zero, so the SECOND can expose only 4,5. After these are removed, H1 still forces row1 zero, so the THIRD can expose only 2,3. Z1,...,Z4 attain these maximal ranks, and the minimum degree is exactly FOUR, with profile (1,2,2,1).

## Universal collision-synchronization lemma

Let w be ANY strict scalar harmonic network, and for each child i define its minimal Bellman-safe edge
\[
e_i=(i-1,b_i^{\mathrm{safe}}),\quad
b_i^{\mathrm{safe}}
 =\min\{b>i:\ w_{i-1}+w_b\ge2w_i\}.
\]
Let the **universal dual upper peeling** U(w) of checkpoint99 partition the internal/terminal vertices into consecutive suffix layers. If \(e_i=P_j\) is the tight parent edge of a DIFFERENT child j, then
\[
\boxed{i<j\quad\text{and}\quad
        i,j\text{ lie in the SAME }U(w)\text{ exposing layer}.}
\tag{116.6}
\]

**Proof.** Harmonicity of P_j gives \(w_j=(w_{i-1}+w_b)/2\ge w_i\); strict weight order and i≠j imply j>i. Let C={p,...,J} be a maximal upper-peeling suffix at a remaining prefix {0,...,J}. If i∈C, then j∈C automatically because j>i. Conversely suppose j∈C but i∉C (i<p). Since i<p, the definition of p gives \(2w_i\le w_{i-1}+w_J\); thus the MINIMAL safe higher endpoint b_i^{safe}≤J. Therefore the tight edge P_j=e_i is ACTIVE at the current face and has lower parent i−1<p, outside C. But checkpoint99's upper suffix is exposable under ALL Bellman-safe parent actions: for any child j≥p and any active safe pair (a,b), a<p would imply \(w_a+w_b\le w_{p-1}+w_J<2w_p\le2w_j\), contradicting safety. Hence j could not be exposed without i in the same layer. This proves (116.6) for EVERY harmonic graph, at EVERY dimension.

This synchronization explains why edge-sharing can reproduce the DESIRED exposing schedule while silently changing the global stability exponent. The problem is not necessarily the dual peeling geometry: it is primal cancellation of a shared offdiagonal coefficient.

## Reproducibility and precise frontier

Checkpoint117 is a standalone exact SymPy/Fraction script validating all matrices, the monomial arc's block support and every stress pairing. It also enumerates ALL 2,286 strict harmonic graphs with h≤5, finding **321 safe-to-tight edge collisions**, and checks they ALL obey the synchronization lemma.

**Consequences:**
- Merely allowing arbitrary edge-sharing is NOT a legitimate replacement for clone-assisted Milestone110, because the required exponent can strictly worsen.
- Global parent-edge uniqueness in the earlier Shapley theorem is an essential analytic hypothesis, not just a convenience for enumeration.
- A dimension-preserving upper/intermediate-degree theorem must control the kernel's entire **weighted cancellation matroid**, not only whether each added edge is Bellman-safe in isolation. It could use a collision-free alternative harmonic graph, extra tied constraints, or an entirely different signed/determinantal mechanism.
- This milestone does NOT refute the conjectural existence of a distinct exact-nullity realization of each **exponent/depth pair** \(L(w)\le d\le U(w)\); the specific shared-edge augmentation fails but the pair might still be realized by a different kernel.

Publication originality/priority is unverified. The explicit proof and constraints are independent of all proposed dense-to-game equivalences.