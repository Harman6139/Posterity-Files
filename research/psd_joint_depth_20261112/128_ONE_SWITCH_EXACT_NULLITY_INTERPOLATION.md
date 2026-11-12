# Milestone 128 — One-switch interpolation at exact nullity

**Date:** 2026-11-12. **Status:** complete research proof, not independently refereed.

**Repository/branch:** `Harman6139/Posterity-Files`, `research/psd-joint-depth-universal-20261107`.
**Source checkpoint:** `48bcfb75063cb8674f3505384cbcd5e8ddc8af75`.

This proves the dimension-preserving intermediate-depth theorem left open in the Opus 5.5 handoff. It builds on the endpoint mechanisms of milestones 114 and 123, but does not assume that arbitrary admissible exposing schedules are realizable. Milestone 129 supplies the complete dense necessity argument and the resulting arithmetic classification.

## 1. Statement and notation

Fix a strictly increasing rational harmonic system
\[
0=w_0<w_1<\cdots<w_{k-1}<w_k=1,
\qquad 2w_i=w_{a_i}+w_{b_i},\quad 0\le a_i<i<b_i\le k.
\tag{1}
\]
There are no internal equations when \(k=1\). Write \(P_i=(a_i,b_i)\). For \(1\le j<k\), put
\[
\ell(j)=\#\{1\le i<j:2w_i<w_{j+1}\},\qquad
u(j)=\min\{1\le i\le j:2w_i>w_j+w_{i-1}\}-1.
\tag{2}
\]
Starting with \(k\to k-1\), repeatedly use \(j\to\ell(j)\) or \(j\to u(j)\) until zero. Their transition counts are \(L(w)\) and \(U(w)\), respectively.

**Theorem 128.** For every integer \(L(w)\le d\le U(w)\) and every half-weight
\[
\alpha=w_v/2\le w_1,\qquad 1\le v\le k,
\tag{3}
\]
there is a rational linear PSD inverse problem on \(\mathbb S^{k+1}\), with target \(X_*=E_{00}\), whose target nullity is exactly \(k\), whose **minimal** facial-reduction degree is exactly \(d\), and whose full ambient Frobenius recovery modulus is
\[
\sup_{X\succeq0,\ \|\mathcal L(X-X_*)\|_F\le\delta}
\|X-X_*\|_F=\Theta(\delta^\alpha).
\tag{4}
\]
In fact the constructed problem retains the entire monomial grade vector \(w\). Any prescribed positive target rank is obtained by fully measured positive-support padding. No extra null coordinates are used.

The construction uses at most \(2(k-1)+1\) kernel generators. Each generator has at most two positive null diagonal entries and at most two offdiagonal edges. The proof is uniform in \(k\).

## 2. The one-switch schedule lemma

Both \(\ell\) and \(u\) are nondecreasing and
\[
0\le\ell(j)\le u(j)<j.
\tag{5}
\]
For the middle inequality, if \(i\le\ell(j)\), harmonicity gives \(w_{b_i}\le2w_i<w_{j+1}\), hence \(b_i\le j\) and
\(2w_i=w_{a_i}+w_{b_i}\le w_{i-1}+w_j\). Thus none of the first \(\ell(j)\) indices meets the strict inequality defining \(u(j)+1\). Monotonicity follows directly as \(j\) increases. The index \(j\) itself always meets that strict inequality.

Define
\[
f(0)=0,\qquad f(j)=1+f(\ell(j)).
\]
Induction using monotonicity of \(\ell\) shows that \(f\) is nondecreasing. Let the upper chain be
\[
J_0=k,\quad J_1=k-1,\quad J_{t+1}=u(J_t),\quad J_U=0.
\]
For each \(1\le t\le U\), follow the first \(t\) upper transitions and then only lower transitions. Its total length is
\[
D_t=t+f(J_t).
\tag{6}
\]
For \(t<U\),
\[
f(J_t)-1=f(\ell(J_t))\le f(u(J_t))\le f(J_t),
\]
so
\[
D_{t+1}-D_t\in\{0,1\},\qquad D_1=L(w),\quad D_U=U(w).
\tag{7}
\]
Consequently these **one-switch schedules alone** realize every integer between \(L\) and \(U\). Choose any \(t\) with \(D_t=d\). This avoids the false assertion that every admissible prefix schedule is geometrically realizable.

Fix that cut and write
\[
q=J_t,\qquad b=J_{t-1}.
\]
The upper part removes all vertices larger than \(q\). The lower tail is
\[
q=s_0>s_1=\ell(s_0)>\cdots>s_m=0.
\tag{8}
\]
If \(q=0\), the lower tail is empty.

## 3. Main-edge ownership and synchronized children

Begin with one tight generator for each internal vertex:
\[
H_i=E_{ii}-E_{00}+\lambda F_{a_i b_i},
\quad F_{ab}=e_ae_b^\top+e_be_a^\top.
\tag{9}
\]
The positive rational constant \(\lambda\) will be chosen small. All tight edges are distinct: their midpoint determines their child's distinct weight.

Select additional blocking edges only as follows.

**Upper-prefix children.** For every \(i>q\), let
\[
c_i=\min\{c>i:w_{i-1}+w_c\ge2w_i\},\qquad Q_i=(i-1,c_i).
\tag{10}
\]
The set is nonempty because the tight parent \(b_i\) is eligible.

**Tail children whose tight edge has already escaped.** For \(i\le q\), select a blocker only when \(b_i>b\), and then put
\[
Q_i=(i-1,b).
\tag{11}
\]
For all other tail children, add no blocker.

The selected \(Q_i\) have different lower endpoints and therefore are distinct physical edges. Implement them by ownership, not independent duplication:

- If \(Q_i=P_i\), do nothing.
- If \(Q_i=P_j\), \(j\ne i\), add \(E_{ii}-E_{00}\) to the existing tight generator \(H_j\).
- If \(Q_i\) is not a tight edge, add one generator \(B_i=E_{ii}-E_{00}+\lambda F_{Q_i}\).

Every physical main edge now has exactly one owner. An owner has either one or two positive diagonal children. Write its child set as \(S_e\), so, before releases are added, its generator is
\[
A_e=\sum_{i\in S_e}(E_{ii}-E_{00})+\lambda F_e.
\tag{12}
\]
Every child satisfies
\[
a(e)<i<b(e),\qquad w_i\le\frac{w_{a(e)}+w_{b(e)}}2.
\tag{13}
\]
Each tight generator acquires at most one additional child.

### Lemma 3.1 — upper collisions remain in one upper layer

If an upper blocker \(Q_i=P_j\) with \(j\ne i\), then \(j>i\) and \(i,j\) belong to the same layer of the full upper chain.

The midpoint inequality implies \(j>i\). Suppose \(j\) is removed in an upper transition \(J\to Q=u(J)\) while \(i\) survives. Then \(i\le Q<j\le J\). The definition of \(u\) gives \(c_i\le J\), and hence
\[
2w_j=w_{i-1}+w_{c_i}\le w_Q+w_J
<2w_{Q+1}\le2w_j,
\]
a contradiction. Thus the children are exposed together. In particular, if \(i>q\), its owner \(j\) also exceeds \(q\). QED.

### Lemma 3.2 — all switch collisions occur in the first lower layer

Every selected tail blocker (11) is safe, is non-source, and has its child in
\[
C_*:=\{\ell(q)+1,\ldots,q\}.
\tag{14}
\]
If it equals a tight edge \(P_j\), then its owner \(j\) also belongs to \(C_*\). Its high endpoint \(b>q\) is off-face throughout the lower tail.

There are no selected tail blockers when \(t=1\), since then \(b=k\). Otherwise \(q=u(b)\), so for every \(i\le q\),
\[
2w_i\le w_{i-1}+w_b.
\tag{15}
\]
This proves safety. The condition \(b_i>b\) and harmonicity give
\[
2w_i=w_{a_i}+w_{b_i}>w_b\ge w_{q+1},
\tag{16}
\]
so \(i\in C_*\). Such an \(i\) cannot equal one: its tight lower parent would be zero, contradicting (15). Hence the blocker is non-source.

If \(Q_i=P_j\), it cannot equal \(P_i\) because \(b_i>b\), so \(j>i\). Ordered parents give \(j<b\). If \(j>q\), then
\[
2w_j=w_{i-1}+w_b\le w_q+w_b
<2w_{q+1}\le2w_j,
\]
a contradiction. Thus \(j\le q\), and (16) also puts \(j\) in \(C_*\). QED.

These lemmas are the dimension-preserving mechanism: every two-child generator has its children in one actual exposing layer. Independent coefficients never share a main edge.

## 4. Shared releases and the distinguished half-weight

For a tail tight owner \(i\le q\), let its lower layer be \(s_u<i\le s_{u-1}\), and define
\[
R_i=(0,s_{u-1}+1).
\tag{17}
\]
Add \(\lambda F_{R_i}\) to \(H_i\), unless \(R_i=P_i\), when it is already present. Upper owners and independent blocker generators receive no release.

These releases have midpoint at most \(w_i\). For \(i<s_{u-1}\), this follows from \(i>\ell(s_{u-1})\). For \(i=s_{u-1}\), harmonicity gives \(2w_i\ge w_{i+1}\), which proves the same inequality. If \(R_j=P_i\) for distinct owners, then
\[
w_i=w_{s_{u-1}+1}/2\le w_j,
\]
so \(i<j\). Thus release/main sharing is strictly upper triangular in the tight-generator coefficients.

If \(\alpha=w_1\), no extra leading mode is needed. If \(\alpha=w_v/2<w_1\), add
\[
G=\lambda F_{0v}.
\tag{18}
\]
It is not a tight main edge, because such an edge would have a child of weight \(\alpha<w_1\). It is not a new blocker edge: all independent blockers are non-source. (An upper blocker at child one is exactly \(P_1\); a tail blocker at child one is impossible.)

If \((0,v)\) is a release, it occurs only in the **last lower layer**. Indeed \(w_v<2w_1\) and that layer starts from \(J=v-1\), so \(\ell(J)=0\). In this case omit the release from every tight generator of that final layer. A different final PSD stress will be supplied in Section 7.3.

Let \(K\) be the span of the resulting generators, including \(G\) when present, and let \(\mathcal L=P_{K^\perp}\). All generators have trace zero and terminal diagonal zero. The main-edge coefficient system is triangular with unit diagonal, the new blocker edges are private, and the leading edge is unused; consequently these generators are linearly independent.

## 5. Global upper recovery estimate for every PSD competitor

Let \(X\succeq0\) and \(\|P_{K^\perp}(X-E_{00})\|_F\le\delta\), with \(0<\delta\le1\). Set
\[
Y=E_{00}+P_K(X-E_{00}).
\]
Then \(\|X-Y\|_F\le\delta\), \(Y+\delta I\succeq0\), \(\operatorname{tr}Y=1\), and \(Y_{kk}=0\). In particular all diagonal entries are uniformly bounded. Put
\[
U_i=|Y_{ii}|+\delta,\quad U_0=O(1),\quad U_k=\delta.
\]
PSD two-by-two minors give \(|Y_{ab}|\le\sqrt{U_aU_b}\).

Write \(x_i\) for the tight-generator coefficients. At the tight main edge \(P_i\),
\[
Y_{P_i}/\lambda=x_i+\sum_{j>i:R_j=P_i}x_j.
\tag{19}
\]
Backward substitution yields
\[
|x_i|\le C\sum_{j\ge i}\sqrt{U_{a_j}U_{b_j}}.
\tag{20}
\]
Every independent blocker coefficient satisfies \(|y_e|\le C\sqrt{U_{a(e)}U_{b(e)}}\), because its edge is private. Each internal diagonal is the sum of its positive-child coefficients. Therefore
\[
U_i\le\delta+C\sum_{(a,b)\in\mathcal A_i}\sqrt{U_aU_b},
\tag{21}
\]
where every pair in \(\mathcal A_i\) has
\[
b>i,\qquad (w_a+w_b)/2\ge w_i.
\tag{22}
\]
For the tight terms in (20), use \(j\ge i\); for blocker terms use safety. The lower endpoint of an induced pair need not be below \(i\), and the next lemma deliberately does not require that.

### Lemma 5.1 — an elementary weighted maximum principle

Inequalities (21)–(22), with bounded \(U_0\) and \(U_k=\delta\), imply \(U_i=O(\delta^{w_i})\).

Set \(h_0=h_k=0\), \(h_i=2^k-2^i\) for internal \(i\). Whenever \(b>i\),
\[
h_i-\frac{h_a+h_b}{2}\ge1.
\]
Indeed \(h_a\le2^k-2\) and \(h_b\le2^k-2^{i+1}\). Choose \(B\ge2\) also bounding \(U_0\), and set \(M_i=BR^{h_i}\). A sufficiently large fixed \(R\) gives
\[
C\sum_{\mathcal A_i}\sqrt{M_aM_b}\le M_i/2
\]
for every internal \(i\). The boundary ratios \(U_i/(M_i\delta^{w_i})\) are at most one. If their maximum were an internal value \(r>1\), (21), (22), and \(\delta\le1\) would give
\[
r\le\frac12+\frac r2,
\]
a contradiction. QED.

Thus \(x_i=O(\delta^{w_i})\), and all blocker coefficients are \(O(\delta^{w_1})\). When present, the coefficient of \(G\) is \(O(\delta^{w_v/2})\). The trace identity controls the source diagonal, while \(X-Y=O(\delta)\). Hence
\[
\|X-E_{00}\|_F=O(\delta^\alpha)
\tag{23}
\]
for every ambient PSD competitor. Letting \(\delta\downarrow0\) also proves uniqueness.

## 6. Matching positive-definite curve

Choose, for example, \(0<\lambda\le1/[8(k+1)^2]\), rational. Use the tight generators at coefficients \(\epsilon^{w_i}\), all independent blockers at coefficient zero, and put
\[
X(\epsilon)=E_{00}+\sum_{i=1}^{k-1}\epsilon^{w_i}H_i
+\epsilon E_{kk}
+\begin{cases}\epsilon^\alpha G,&G\text{ is present},\\0,&\text{otherwise}.\end{cases}
\tag{24}
\]
The internal diagonal at \(i\) is \(\epsilon^{w_i}\) plus nonnegative higher-order contributions from owners \(j>i\). The source diagonal tends to one. Congruence by
\(\operatorname{diag}(1,\epsilon^{-w_1/2},\ldots,\epsilon^{-w_k/2})\)
makes every tight edge bounded by \(\lambda\), every release contribution bounded by \(\lambda\), and the optional leading contribution equal to \(\lambda\). There are at most \(2(k-1)+1\) such contributions. For the stated \(\lambda\), strict diagonal dominance proves \(X(\epsilon)\succ0\) for all sufficiently small \(\epsilon\).

Because \(E_{kk}\in K^\perp\), its residual is exactly \(\epsilon\). Its displacement is \(\Theta(\epsilon^\alpha)\): use the lowest internal diagonal if \(\alpha=w_1\), or the unused leading edge otherwise. Together with (23), this proves (4). The same diagonal bounds and thick curve, via the maxdet envelope proved in milestone 129, show that the full canonical chart has these grades.

## 7. Exact maximal exposing layers

A measurement stress is an ambient \(Z\in K^\perp\) with \(\langle Z,E_{00}\rangle=0\) whose compression to the current face is PSD. Its compressed source row is zero. A PSD matrix with a zero diagonal entry has its entire corresponding row and column zero.

We prove at every scheduled prefix that **all** compressed PSD stresses are supported in the intended layer, and construct one positive definite on that entire layer. This establishes maximality, not just existence of one chain.

### 7.1 First and upper-prefix steps

The first maximal layer is \(\{k\}\). To exclude an internal exposed diagonal, take the least one. Its tight generator has only lower-grade extra diagonal children and only edges whose lower endpoints have smaller weight; a more formal equivalent argument pairs successively with the tight generators, whose support weights are at most \(w_i\). All earlier rows vanish, leaving its positive diagonal pairing. Thus every internal row must vanish. The stress \(E_{kk}\) exposes the terminal.

At an upper step with current prefix \(\{0,\ldots,J\}\), put \(Q=u(J)\) and \(C=\{Q+1,\ldots,J\}\). Suppose a PSD compressed stress has a positive diagonal at some survivor \(i\le Q\); choose the smallest such \(i\). Every smaller remaining row is zero.

If \(i>q\), use its minimal safe blocker (10). That edge is active because \(i\le u(J)\) implies \(c_i\le J\). Its owner has no release, and every child remains by Lemma 3.1. Its lower endpoint \(i-1\) has zero row. The generator equation therefore says that a positive sum of nonnegative diagonals is zero, a contradiction.

If \(i\le q\) and \(b_i\le b\), use its tight generator. Its main edge is active since \(b\le J\), and its lower parent has zero row. Its release, when present, is an active source edge, hence also pairs to zero. All its children remain. Again the diagonal sum is positive, a contradiction.

If \(i\le q\) and \(b_i>b\), use its switch blocker. The edge \((i-1,b)\) is active. Its owner has only tail children, and its possible release is an active source edge. The same contradiction applies. Thus every compressed stress vanishes on all survivors.

For existence, assign positive diagonal values \(z_i\) on \(C\), and zero on all other ambient diagonals. At every main edge set
\[
2\lambda Z_e=-\sum_{i\in S_e}z_i.
\tag{25}
\]
All tail releases have zero value: a nonzero upper source main edge has high endpoint at least \(q+2\), whereas a tail release has high endpoint at most \(q+1\). Hence every generator pairing vanishes exactly, including the optional leading mode.

If a main edge with a child in \(C\) is active, both endpoints belong to \(C\). Otherwise its lower endpoint would be at most \(Q\), and safety would contradict
\[
w_{a(e)}+w_{b(e)}\le w_Q+w_J<2w_{Q+1}\le2w_i.
\]
Choose a common denominator \(M\) for \(w\) and put \(z_i=T^{(Mw_i)^2}\), with \(T\) a sufficiently large positive integer. For every active edge and each of its children,
\[
\frac{w_a^2+w_b^2}{2}-w_i^2
\ge\frac{(w_b-w_a)^2}{4}>0.
\tag{26}
\]
Thus the diagonal-normalized offdiagonal entries in (25) tend to zero as \(T\to\infty\). The compression is PSD, positive definite exactly on \(C\). All stress entries can be rational.

### 7.2 Ordinary lower-tail steps

At a lower step from prefix \(J\) to \(Q=\ell(J)\), let \(C=\{Q+1,\ldots,J\}\). Assume first that its release is not the forbidden leading edge. Put diagonal one on \(C\), zero on all other ambient diagonals, and set
\[
2\lambda Z_{0,J+1}=-1.
\tag{27}
\]
Every ordinary tight generator belonging to \(C\) has exactly this release (or has this edge as its main edge). A tight generator outside \(C\) has neither a nonzero diagonal pairing nor this release. Its main edge also cannot equal \((0,J+1)\): that equality would imply \(2w_i=w_{J+1}\) and place its child in \(C\).

The only remaining nonzero pairings are those of independent switch blockers and tight owners with an extra switch child. By Lemma 3.2, their children all lie in the first lower layer, and their main edges are private non-source edges with high endpoint \(b>q\). Correct each remaining pairing by changing the value on its own main edge. Those entries are off-face throughout the lower tail, and are not releases or other main edges. This makes every pairing exactly zero while leaving the current compression equal to the diagonal identity on \(C\).

For maximality, suppose a survivor \(i\le\ell(J)\) has positive compressed diagonal, and choose the smallest. Its tight generator is single-child: all transferred tail children and owners belong to the first lower layer, never to a survivor of a lower step. Since \(2w_i<w_{J+1}\), the tight upper parent satisfies \(b_i\le J\). Its release, if present, belongs to a later lower layer and also is active. The lower-parent row and source row vanish. The generator equation forces its positive diagonal to be zero, a contradiction.

### 7.3 Final leading-edge collision

If the leading edge equals a release, its final prefix is \(J=v-1\) and its next index is zero. All releases on this final layer were omitted in Section 4.

Put \(z_i=T^{(Mw_i)^2}>0\) on every remaining null coordinate \(1\le i\le J\), zero on all other ambient diagonals, and use (25) on every main edge. No earlier release gets a nonzero value. Indeed a surviving final child \(i\) satisfied \(2w_i<w_{B}\) at any earlier lower release \((0,B)\), whereas equality would be needed for its tight main edge to equal that release. Private blocker edges are non-source. Synchronized children rule out a removed owner with a surviving extra child. Therefore every generator pairing is zero. The leading edge is not a main edge and has value zero.

An active tight edge in the final face cannot touch the source: otherwise its upper weight would be \(2w_i\ge2w_1>w_v>w_J\), contradicting activity. Switch-blocker main edges are off-face. Thus every active nonzero main edge lies wholly in the final null block. Inequality (26) proves that the compressed stress is positive definite on that block and zero on the source. This is a legitimate final exposing stress, including when the first and last lower layers coincide.

### 7.4 Why this is the minimum degree, including noncoordinate chains

At every scheduled face, the preceding arguments show that the intended stress kills the union of the ranges of **all** valid compressed PSD stresses. Its survivor face is therefore contained in the survivor of any single valid reduction from that face.

Inductively compare the greedy chain with any other chain. If the greedy face is contained in the other current face, restricting the other's next PSD stress to the greedy face is still a valid compressed stress. Its range is annihilated by the next greedy survivor. Because the larger compression is PSD, zero quadratic form on a vector forces that vector into its kernel. Hence the next greedy survivor is contained in the other's next survivor. This proves the inclusion at every step, even when the other chain uses rotated subspaces.

No other chain can reach the target face earlier. The constructed greedy chain has length \(t+f(q)=d\), so its **minimal** singularity degree is exactly \(d\). Theorem 128 is proved.

## 8. Regression examples and the old obstructions

For milestone 125's weights
\[
(0,1/4,3/7,1/2,17/28,5/7,1),
\]
the cut after two upper transitions gives
\[
6\to5\to4\to1\to0,
\]
with layers \(\{6\},\{5\},\{2,3,4\},\{1\}\), not the forbidden schedule \(\{6\},\{4,5\},\{2,3\},\{1\}\).

A simultaneous switch-merge and leading-release repair occurs for
\[
P=((0,4),(0,6),(1,5),(2,5),(4,6)),
\quad w=(0,1/3,1/2,7/12,2/3,5/6,1).
\]
Choose the same cut and \(\alpha=1/4\). The switch edge \(Q_2=(1,5)=P_3\) transfers child 2 into the tight owner 3; both are exposed in the first lower block. The optional edge \((0,2)\) forces omission of the final release, handled by Section 7.3. No additional null coordinate is introduced.

The adjacent exact-arithmetic program checks the deterministic construction on the handoff's obstruction examples and dyadic families. It verifies generator/stress pairings, support inequalities, synchronized ownership, no-gap cut lengths, and minimality certificates. These checks are supplementary; no finite enumeration is used in the proof above.

**Scope:** This closes the exponent-versus-minimal-degree existence problem at unchanged nullity. It does not assert that every individual flag, rank-drop profile, or given dense kernel has this normal form. The previous counterexamples to those stronger assertions remain valid.
