# Milestone 94 — EXACT exponent/depth and Dikin normal form are coefficient-independent for arbitrary SIGNED tied-edge PSD pencils

**Date 2026-11-08. PROVED for the entire strict tied-edge MIN–MAX incidence class with arbitrary fixed NONZERO REAL edge coefficients, not merely common small positive lambda.** Both sharp recovery exponent and exact minimal exposing rank profile depend only on mode/edge incidence and strict Shapley values, not on edge magnitudes or signs. The proof uses a novel-to-this-packet application of the full PSD coefficient-rescaling lemma, not numerical small-coupling assumptions. This meaningfully extends the class of dense matrix pencils whose Dikin invariants and facial depth are provably encoded by the finite tied-edge game. It is not a universal theorem for all arbitrary dense kernels.

## General signed-coefficient system

As in checkpoint74, fix source vertex 0, internals 1,...,h, terminal T=h+1 and for each internal i a nonempty finite collection of modes a∈A_i. Each mode has a nonempty set E_(i,a) of unordered parent pairs (u,v) with u<i<v. Every individual edge is assigned to exactly one mode/child, so all edge supports are globally disjoint. Let **arbitrary real coefficients**
\[
d_{i,a}>0,\qquad
\lambda_{i,a,(u,v)}\in\mathbb R\setminus\{0\}
\]
be fixed (no upper/lower absolute-size bound and signs may vary). Define the measurement kernel K by generators
\[
\boxed{
H_{i,a}
=d_{i,a}(E_{ii}-E_{00})
+\sum_{(u,v)\in E_{i,a}}
\lambda_{i,a,(u,v)}F_{uv}.
}
\tag{1}
\]
An optional extra generator \(\lambda_G F_{0,t}\), \(\lambda_G\ne0\), on an unused edge (0,t) is permitted. Let X*=E00 and L=P_(K⊥) with Frobenius metric. Every generator has trace zero and terminal diagonal zero, so I and E_TT belong to K⊥.

Define the unique strict Shapley weights
\[
0=w_0<w_1<\cdots<w_h<w_T=1,\qquad
w_i=\min_{a\in A_i}\max_{(u,v)\in E_{i,a}}
              \frac{w_u+w_v}{2}.
\tag{2}
\]

## Theorem A — sharp full ambient PSD recovery exponent independent of coefficients

For EVERY choice of signs and magnitudes subject to (1), the target is uniquely PSD recoverable, and
\[
\boxed{\omega(\delta)=\Theta(\delta^\alpha),\quad
\alpha=\min\{w_1,\ w_t/2\text{ if optional leading edge exists}\}.}
\tag{3}
\]

**Global upper bound:** For arbitrary PSD competitor X with residual≤δ, set Y=X*+P_K(X−X*), so ||X−Y||≤δ and Y+δI≽0. Since trace is measured, Y and all its diagonal coordinates are bounded; the terminal diagonal of Y is zero. Each mode coefficient y_(i,a) appears on several globally UNIQUE offdiagonal entries, each equal to \(\lambda_e y_{i,a}\), and on the i-th diagonal as \(d_{i,a}y_{i,a}\). The 2×2 principal-minor bound gives
\[
|y_{i,a}|
\le C_{i,a}\min_{e=(u,v)\in E_{i,a}}\sqrt{U_uU_v},
\quad
U_i=|Y_{ii}|+\delta,\ U_T=\delta,\ U_0=O(1),
\]
where C_(i,a) depends only on the finite fixed inverse coefficient magnitudes 1/|\lambda_e|. Therefore
\[
U_i\le\delta+C_i\sum_{a\in A_i}
          \min_{e\in E_{i,a}}\sqrt{U_uU_v}.
\]
The exact same positive Shapley supersolution/weighted maximum-principle proof as checkpoint74 applies (only constants change), giving \(U_i=O(\delta^{w_i})\), all individual mode coefficients \(O(\delta^{w_i})\), and the optional generator coefficient \(O(\delta^{w_t/2})\). Tr(Y)=1 controls the source diagonal and ||X−Y||≤δ controls every other ambient entry. Hence ||X−X*||≤Cδ^α for ALL PSD competitors, proving uniqueness.

**Matching PD curve for ARBITRARILY LARGE and SIGNED coefficients:** Select at every i one minimizing mode a_i satisfying
\[
\max_{e=(u,v)\in E_{i,a_i}}\frac{w_u+w_v}2=w_i.
\]
The matrix coefficient H_(i,a_i) has a POSITIVE diagonal at i, and all its potentially nonzero blocks e=(u,v) satisfy \(w_u+w_v\le2w_i\). Add the terminal coefficient E_TT at exponent1. By the **full PSD coefficient-rescaling lemma** from checkpoint89, for sufficiently large fixed σ,
\[
\boxed{
X_\sigma(t)=E_{00}
+\sum_{i=1}^h e^{\sigma w_i^2} t^{w_i}H_{i,a_i}
+e^\sigma t E_{TT}
+[e^{\sigma(w_t/2)^2}t^{w_t/2}\lambda_G F_{0,t}]
}
\tag{4}
\]
is strictly POSITIVE DEFINITE for all sufficiently small t>0. Indeed, after diagonal congruence by \(e^{\sigma w_i^2/2}t^{w_i/2}\), all diagonal leading coefficients are \(d_{i,a_i}>0\), the terminal is1, and every surviving cross entry joins DIFFERENT weights w_u<w_v and acquires the exponentially decaying multiplier
\[
e^{-\sigma(w_u-w_v)^2/4}.
\]
Thus no matter how large the fixed signed edge coefficients are, all normalized cross-blocks can be made arbitrarily small by selecting σ sufficiently large. This handles the optional leading edge as well, because its parents have distinct weights 0<w_t.

All terms in (4) below order one lie in K, while E_TT∉K, so the measurement residual is Θ(t) and displacement is Θ(t^α). This proves exact (3).

## Theorem B — exact MINIMAL facial degree/profile are also coefficient-independent

On any current coordinate face, let C be a subset of remaining non-source vertices. It is exposable in ONE compressed PSD stress if and only if the same AND–OR condition as in checkpoint74 holds:

For each internal i∈C and each mode a at i whose ENTIRE edge set E_(i,a) has endpoints still present,
\[
\boxed{\exists e=(u,v)\in E_{i,a}\text{ with }u,v\in C.}
\tag{5}
\]
The maximal such C is unique; iterating it yields the exact minimal facial-reduction degree and rank-drop profile.

**Necessity:** The dual stress orthogonality equation for generator H_(i,a) is
\[
d_{i,a}Z_{ii}+2\sum_{e=(u,v)\in E_{i,a}}\lambda_{i,a,e}Z_{uv}=0.
\tag{6}
\]
For PSD compression, if Z_ii>0 and all edges of mode a are active within the face, the first term in (6) is nonzero; hence some active offdiagonal Z_uv must be nonzero. PSD positivity forces Z_uu,Z_vv>0, i.e. u,v∈C. This is exactly condition (5), regardless of coefficient signs.

**Sufficiency:** Let C satisfy (5). Give its vertices strictly positive stress diagonals
\[
Z_{ii}=\eta^{-10^i}\quad(i\in C)
\]
and zero remaining diagonals outside C, for sufficiently small positive η. For each active mode at a child i∈C, choose an edge e=(u,v) entirely inside C and solve (6) using that one entry:
\[
Z_{uv}=-\frac{d_{i,a}Z_{ii}}{2\lambda_{i,a,e}}.
\]
For modes with at least one edge touching a removed coordinate, choose a FREE off-face stress entry on such an edge to solve its own equation; for modes at i∉C choose zero relevant entries. Global edge-disjointness ensures that no dual variable is assigned inconsistent values. For each active within-face selected edge u<i<v, after diagonal normalization its absolute value is proportional to
\[
\eta^{(10^u+10^v)/2-10^i}\to0
\]
since \(10^v\ge10^{i+1}=10\cdot10^i\). The resulting face compression is strictly diagonally dominant and PD on C, zero on the other remaining vertices. Thus it is a valid PSD exposing stress with precisely the desired support. Greedy maximal-rank facial reduction proves the exact profile and minimal degree.

No sign, small-coupling or generic-coefficient hypothesis is used. QED.

## Corollary — exact Dikin–Bellman bridge for signed coefficient pencils

The monomial matching curve in Theorem A is uniformly Loewner-comparable to the diagonal Bellman power matrix
\[
D_t^2=\operatorname{diag}(1,t^{w_1},\ldots,t^{w_h},t).
\]
The global competitor diagonal bounds give the reverse Loewner upper estimate, so the universal canonical-center sandwich of checkpoints86/89 proves
\[
cD_\epsilon^2\preceq C_\epsilon\preceq CD_\epsilon^2.
\]
The weighted kernel rank threshold remains \(\tau=\min(w_1,w_t/2)\): every nonzero mode coefficient has at least one unique edge of weight ≥w_i, while a minimizing mode at vertex1 has all weights ≤w1; optional leading edge is unique. Hence the Dikin radius's exact rate and the complete minimum facial exposing profile depend only on the finite signed-SUPPORT game data, even though numerical constants may vary drastically with the arbitrary generator magnitudes.

## Broader dense perturbations and exact scope

- Applying ANY fixed orthogonal congruence to these kernels makes their matrices generally dense, while leaving Hölder exponents, exposing rank profiles and the intrinsic Dikin exponents unchanged up to fixed norm-equivalence constants. Thus this theorem covers a nontrivial continuously parametrized family of dense-looking PSD measurement maps.
- Arbitrary fixed traceless perturbations supported entirely inside the TARGET SUPPORT block can also be added to each kernel generator, provided the total generator trace remains zero; they vanish in every compressed PSD exposing stress (whose support rows are zero), and along matching arcs they are lower-weight than the null-block leading terms. Their presence changes only fixed recovery constants, not exponents or minimal exposing profiles. For target rank one there are no nonzero such traceless support perturbations.
- **NOT INCLUDED:** arbitrary overlapping offdiagonal edge coefficients or signed cancellations between modes on the same edge. These can destroy the individual mode bounds from 2×2 minors and alter facial rank. A fully general dense-to-game theorem would require control of these additional linear-algebraic dependencies, plausibly through the signed Plücker initial/jet data of checkpoints90–92.

This theorem strengthens the constructed candidate class; it is still not a proof that EVERY dense PSD exponent/profile pair can be matched by a finite incidence game with unchanged nullity.

## Prior-art disclaimer

The Jordan/PSD positivity tools, maxdet Hessian, weighted coefficient-rescaling and facial-reduction principles are established ingredients. This coefficient-robust exact Shapley game extension is proved here with full assumptions; independent priority audit is still needed.
