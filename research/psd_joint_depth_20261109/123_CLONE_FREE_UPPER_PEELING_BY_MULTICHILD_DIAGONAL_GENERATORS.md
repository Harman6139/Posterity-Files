# Milestone 123 — CLONE-FREE exact-nullity realization of the universal UPPER facial peeling bound for EVERY harmonic weight and half-exponent

**2026-11-09. NEW all-dimensional constructive theorem with complete PSD proof.** This removes the nullity overhead of the *upper* end in checkpoints 109–110. Unlike the false naive shared-edge implementation (checkpoint 116), **EVERY physical offdiagonal edge belongs to exactly ONE kernel generator**. An edge whose safe action would collide with another vertex's tight harmonic anchor is instead assigned to that existing tight generator, which carries *two positive child diagonal coefficients*. The shared edge then has no independent kernel coefficient to cancel, preventing the graded PSD initial-cone obstruction of checkpoint 121.

## Main theorem

Let \(h\ge1\), \(k=h+1\), with strictly increasing rational harmonic weights
\[
0=w_0<w_1<\cdots<w_h<w_k=1,\qquad
2w_i=w_{a_i}+w_{b_i},\quad0\le a_i<i<b_i\le k.
\]
Let \(U(w)\) be the universal original-dual maxdet truncation upper bound on minimal facial degree from checkpoint 99: first remove terminal \(k\), and from each remaining prefix \(\{0,\ldots,j\}\) remove the maximal suffix \(p(j),\ldots,j\), where
\[
p(j)=\min\{1\le p\le j:2w_p>w_j+w_{p-1}\}.
\]

For ANY valid distinguished full-matrix sharp exponent \(\alpha=w_v/2\le w_1\), there is an explicit RATIONAL PSD inverse problem on \(\mathbb S^{k+1}\), with target \(X_*=E_{00}\), **target nullity EXACTLY k**, uniquely PSD recoverable and with
\[
\boxed{\text{sharp full ambient Hölder exponent }=\alpha,\qquad
       \text{MINIMAL facial-reduction degree }=U(w).}
\]
Its exact canonical exposing layers are the successive upper suffixes just described. Fully measuring additional positive support coordinates realizes any prescribed target rank \(r\ge1\) without changing nullity, exponent or facial depth.

The kernel uses **at most \(2h\) generators**, each with one globally unique parent offdiagonal edge and one or two positive diagonal entries. It adds NO null coordinate clone and does NOT assume arbitrary dense-to-game equivalence.

## I. Canonical minimal-safe edges and collision transfer

For every internal vertex \(i=1,\ldots,h\), define its **minimal safe edge**
\[
e_i=(i-1,c_i),\qquad
c_i=\min\{b:i<b\le k,\quad w_{i-1}+w_b\ge2w_i\}.
\tag{123.1}
\]
This edge always exists because the original tight parent pair \((a_i,b_i)\), with \(a_i\le i-1\), implies \(w_{i-1}+w_{b_i}\ge2w_i\). Its average is Bellman-safe:
\[
\eta(e_i)=\tfrac12(w_{i-1}+w_{c_i})\ge w_i.
\]
Distinct \(e_i\)'s have distinct LOWER endpoints \(i-1\), so their physical edges are pairwise distinct. Also, \(e_1=P_1\): the minimum internal weight's tight lower parent is the source0, and its harmonic upper parent is exactly the first safe index.

The tight parent edges \(P_i=(a_i,b_i)\) are pairwise distinct because distinct child weights cannot equal the same parent midpoint.

If \(e_i=P_j\) for a different child j, then \(w_j=\eta(e_i)\ge w_i\); strict weights imply \(j>i\). Thus we can put an additional POSITIVE diagonal at coordinate i into the already existing tight generator at coordinate j without introducing any higher-order diagonal term that would change i's leading recovery order.

### Lemma (collision synchronization)

If \(e_i=P_j\) with \(i\ne j\), then \(i\) and \(j\) belong to the SAME universal U(w) exposing layer.

**Proof.** In the universal all-safe abstract parent-action closure, the exact exposing layers are consecutive descending suffixes \(C_1,\ldots,C_{U(w)}\). Because \(j>i\), j cannot be exposed later than i. Suppose j is exposed strictly earlier, at a stage whose remaining prefix is \(R=\{0,\ldots,J\}\), with i,j still present but i not in the maximal exposing set \(C\).

If \(c_i\le J\), the tight parent edge \(P_j=e_i=(i-1,c_i)\) is ACTIVE, and its lower endpoint \(i-1\) is not in C because i and all smaller indices are in a later layer. That violates the closure rule for the exposed child j.

If \(c_i>J\), NO safe parent pair at i is active: any active pair \((a,b)\) has \(a\le i-1\), \(b\le J<c_i\), and hence
\(w_a+w_b\le w_{i-1}+w_b<2w_i\)
by the minimality of \(c_i\). Adding i to C then cannot violate any closure equation of child i, and can only HELP the closure equations of other exposed children. Therefore the supposedly maximal exposed set C would already include i. Contradiction. Hence the two children have the same U-layer. QED.

This same-layer fact is vital: after completing any U-peeling layer, neither child in a two-diagonal generator can remain while the other was already exposed.

## II. The physical generator construction

For every TIGHT parent edge \(P_j\), create exactly one generator initially
\[
H_{P_j}=E_{jj}-E_{00}+\lambda F_{P_j}.
\]
For each safe edge \(e_i\):
- if \(e_i=P_i\), do nothing;
- if \(e_i=P_j\) for j>i, replace the existing generator \(H_{P_j}\) by
\[
H_{P_j}=E_{jj}+E_{ii}-2E_{00}+\lambda F_{P_j};
\]
- if \(e_i\) is not any tight parent edge, create one NEW generator
\[
J_{e_i}=E_{ii}-E_{00}+\lambda F_{e_i}.
\]
Each physical edge appears in only one generator; no two e_i coincide. A tight generator can acquire at most ONE extra diagonal child because the e_i have distinct lower endpoints.

More conceptually, index all physical generators by their DISTINCT offdiagonal edges e, and let \(S_e\subseteq\{1,\ldots,h\}\) be its set of positive diagonal child coordinates: either {j}, {i,j} with i<j, or {i} for a new safe edge. Then
\[
\boxed{H_e=\sum_{i\in S_e}E_{ii}-|S_e|E_{00}+\lambda F_e}
\tag{123.2}
\]
and, for EVERY \(i\in S_e\),
\[
a(e)<i<b(e),\qquad
w_i\le\eta(e)=\frac{w_{a(e)}+w_{b(e)}}2.
\tag{123.3}
\]
Every child i is a member of the tight generator for P_i and the generator for e_i. Add optional \(G=\lambda F_{0v}\) ONLY when \(\alpha=w_v/2<w_1\); it never collides with any physical H_e edge: no tight P_j can equal (0,v) (that would make w_j=alpha<w1), and the sole source-lower safe edge is e_1=P_1.

Take \(K=\operatorname{span}\{H_e\}\) (and G when used), \(L=P_{K^\perp}\) in Frobenius coordinates, \(X_*=E_{00}\). Every generator has trace zero and terminal diagonal zero, so the trace and terminal coordinate are observed. All data are rational for sufficiently small rational \(\lambda>0\).

## III. Global full-ambient recovery exponent is EXACTLY alpha

For any PSD competitor X with \(\|L(X-X_*)\|_F\le\delta\), put
\(Y=X_*+P_K(X-X_*)\) and \(E=X-Y\). Then \(\|E\|_F\le\delta\), \(Y+\delta I\succeq0\), \(\operatorname{tr}Y=1\), \(Y_{kk}=0\), and all diagonal entries of Y are bounded by measured trace. Let \(y_e\) be the coefficient of the generator H_e and put
\(U_i=|Y_{ii}|+\delta\), \(U_0=O(1)\), \(U_k=\delta\).
Because EVERY physical offdiagonal edge is unique,
\[
Y_{a(e),b(e)}=\lambda y_e
\quad\Longrightarrow\quad
|y_e|\le C\sqrt{U_{a(e)}U_{b(e)}}.
\]
Every internal diagonal satisfies \(Y_{ii}=\sum_{e:i\in S_e}y_e\), so
\[
\boxed{U_i\le\delta+
 C\sum_{e:i\in S_e}\sqrt{U_{a(e)}U_{b(e)}}.}
\tag{123.4}
\]
Each edge in this sum has parent-average at least w_i by (123.3), and each child has a higher parent \(b(e)>i\). Therefore the finite stochastic hitting-time supersolution/maximum-ratio argument of checkpoints 57/74 applies to (123.4) *verbatim*: choosing constants M_i with
\[
M_i\ge2+C'\sum_{e:i\in S_e}\sqrt{M_{a(e)}M_{b(e)}}
\]
and boundaries M0,Mk fixed, gives
\[
U_i=O(\delta^{w_i})
\quad\text{for EVERY ambient PSD competitor}.
\]
Consequently every coefficient y_e=O(\delta^{\eta(e)}) and each diagonal and offdiagonal part of Y−X* is O(\delta^{w1}). The optional independent leading coefficient is O(\delta^{w_v/2}), and all off-pattern entries of X are O(delta); hence
\[
\|X-X_*\|_F=O(\delta^\alpha).
\]
Taking delta→0 proves uniqueness.

For a MATCHING sharp arc, activate ONLY the h tight generators P_i at coefficients \(z^{w_i}\), set all new safe-edge generator coefficients to zero, set the terminal diagonal to z, and if used set the independent G coefficient to \(z^\alpha\). Because extra diagonal couplings go strictly from larger-weight j to smaller-weight i, the internal diagonal i is
\[
z^{w_i}+\sum_{j>i:\;e_\ell=P_j,\ i=\ell}z^{w_j}
\ \ge z^{w_i}>0.
\]
Every active tight offdiagonal edge has order \(w_i\) with parent midpoint \(w_i\). Diagonal normalization therefore makes its magnitude at most a constant multiple of lambda (the larger diagonal only helps). Taking lambda small ensures the FULL matrix is strictly diagonally dominant and PD for small z. Its measurement residual equals \(z\|L E_{kk}\|=z\) since \(E_{kk}\in K^\perp\), and its displacement is Theta(z^alpha). Thus the exponent is EXACTLY alpha.

## IV. Exact DUAL exposing geometry: edge-indexed positive diagonal sums

Let R be a coordinate remaining face that is a PREFIX \(\{0,1,\ldots,j\}\) of the universal U(w) exposing schedule. By collision synchronization, every two-child diagonal set S_e lies ENTIRELY inside a single U-layer. Thus, at such a prefix, either all children of S_e remain or all are already removed. In the latter case the edge e is OFF-FACE (its higher endpoint exceeds its child, hence the current prefix index), so it places no constraint on the current stress compression.

For a PSD compressed exposing stress S annihilating source e0, the dual generator equation reads
\[
\sum_{i\in S_e}Z_{ii}+2\lambda Z_{a(e),b(e)}=0
\tag{123.5}
\]
for EVERY physical edge e, with source Z00=0. If e is active (both parents still in R), all its child diagonal entries are nonnegative because its children remain in R. Therefore, if any i∈S_e has positive exposed diagonal, the sum is positive and \(Z_{a(e),b(e)}\ne0\). PSD positivity forces BOTH parent endpoints to have positive diagonal too.

It follows that ANY exposed-support set C at that prefix obeys the independent-action closure for BOTH the tight pair P_i and the minimal safe pair e_i of EVERY child i:
\[
i\in C,\quad (a,b)\in\{P_i,e_i\},\
 a,b\in R \quad\Longrightarrow\quad a,b\in C.
\tag{123.6}
\]

**Conversely**, given ANY C obeying (123.6), put positive stress diagonals \(Z_{ii}=z_i=\eta^{-w_i^2}\) on i∈C and zero on all other remaining vertices, set Z00=0, and for EVERY generator edge e define
\[
Z_{a(e),b(e)}
=-\frac{1}{2\lambda}\sum_{i\in S_e\cap C}z_i.
\tag{123.7}
\]
When an endpoint of e was already removed, this is an unrestricted off-face entry; if both endpoints remain, the closure rule (123.6) ensures both belong to C whenever the numerator is nonzero. All edges are physically distinct and optional G uses an unused edge, so these assignments satisfy ALL \(K^\perp\) equations exactly.

Within the remaining face, normalize by the positive stress diagonal. For every active edge e and i∈S_e, (123.3) and the strict inequality w_a<w_b give
\[
\frac{w_a^2+w_b^2}{2}-w_i^2
\ \ge\ \frac{(w_b-w_a)^2}{4}>0.
\]
Hence each nonzero normalized offdiagonal in (123.7) tends to zero as \(\eta\downarrow0\); finitely many edges allow strict diagonal dominance. Thus the current compressed stress is PSD, PD on precisely C, and zero elsewhere. This proves (123.6) is both necessary and sufficient on the U-prefix faces.

## V. Compute the U(w) greedy layers and MINIMAL degree

At the initial full coordinate face, no internal vertex is exposable: its tight parent edge has BOTH parents present and a strictly smaller lower parent, forcing a descending chain to source 0 in any putative exposing-closed set. Terminal k is individually exposable, so the first maximal exposing layer is exactly {k}.

At a later current prefix R={0,...,j}, let
\[
p=p(j)=\min\{1\le p\le j:\ 2w_p>w_j+w_{p-1}\}.
\]
**Sufficiency of the suffix:** C={p,...,j} is closed under ANY safe parent edge for children i≥p. If an active edge (a,b) at i≥p had a<p, then
\[
w_a+w_b\le w_{p-1}+w_j<2w_p\le2w_i,
\]
contradicting its harmonic or safe inequality. Hence both active parents lie in C.

**Maximality of the suffix:** for every i<p, minimality of p gives
\(2w_i\le w_{i-1}+w_j\), so the minimal safe edge \(e_i=(i-1,c_i)\) has c_i≤j and is ACTIVE. A proposed exposing set containing any i<p has a smallest such i; its safe edge requires the smaller index i−1 also to be exposed, impossible. Thus NO internal coordinate below p can be exposed in this stage.

By Section IV, these are exactly the PSD exposed sets of the actual edge-indexed kernel, not only abstract edges. Therefore the canonical maximal exposing chain removes the suffix C, leaving prefix 0,...,p−1. Iterating proves the exact greedy schedule and degree \(U(w)\). The general greedy-minimality principle follows by comparing an arbitrary exposing chain with the maximal-rank coordinate chain: at each step its surviving face contains the canonical greedy survivor face, because any compressed PSD exposing stress on a larger face restricts to a valid stress on the smaller canonical face, and the greedy stress kills the union of all exposable ranges. Hence no shorter arbitrary (possibly noncoordinate) facial chain exists.

This proves the theorem. QED.

## Explicit 8×8 nontrivial collision example

Take h=6, terminal7 and
\[
w=(0,3/32,3/16,3/8,1/2,9/16,3/4,1)
\]
with tight pairs
\[
P=((0,2),(0,3),(0,6),(0,7),(3,6),(4,7)).
\]
The canonical minimal safe edge for child4 is (3,6), which is ALREADY the tight edge of child5. Instead of introducing an independent generator that shares (3,6), replace the tight fifth generator by
\[
H_5=E_{55}+E_{44}-2E_{00}+\lambda F_{36}.
\]
Also add the safe independent generator \(J_3=E_{33}-E_{00}+\lambda F_{25}\) (and any other optional safe generators prescribed by the universal construction). The resulting full harmonic recovery exponent is \(w_1=3/32\), while the U-peeling schedule is
\[
\{7\},\{6\},\{4,5\},\{3\},\{2\},\{1\}.
\]
The edge (3,6) occurs in precisely ONE generator, and the two same-layer diagonal coefficients in H5 transfer its blocking constraint without creating a cancelling kernel circuit. All exposing stresses arise explicitly from (123.7), including a stress at stage three with compression E44+E55 and off-face entries -F07/(2lambda)-F36/lambda.

## Exact exhaustive checks

A self-contained exact-rational checker is in checkpoint 124. It exhausts all (h!)² harmonic parent assignments with h≤6 internal vertices, retaining respectively
  1,3,18,165,2099,34570
strictly ordered harmonic solutions. For EVERY solution it constructs the physical edge-indexed multi-child generators, verifies all edges are unique and all involved children satisfy their safe weighted inequality, and independently performs the full positive-exposure closure. The resulting layers agree EXACTLY with the universal U(w) recurrence in every case. At h=6 there are **34,570** valid systems, of which **6,276** use a genuine two-diagonal collision repair. No counterexample was found; the symbolic proof above applies for EVERY h.

## Scope and significance

**SOLVED:** The UPPER universal peeling endpoint \(d=U(w)\) is attained, with EVERY valid leading half-exponent, at EXACT original nullity and target rank one, in ALL dimensions. Combined with checkpoint 114, BOTH L(w) and U(w) are now achieved at original nullity without clone coordinates. The missing full fixed-(n,r,d,alpha) theorem has therefore been reduced specifically to **INTERMEDIATE** depths \(L(w)<d<U(w)\), and the still stronger exact arbitrary exposing rank-profile spectra.

This is a more expressive but still rational *one-edge-per-generator / multiple-child-diagonal* linear PSD model. It is neither the original independent-action midpoint family nor a claim of universal equivalence of all dense kernels to it. It avoids the cancellation pathology of checkpoints 116/118 by never sharing a physical offdiagonal coefficient between distinct kernel generators.

Mathematical priority and the load-bearing earlier universal dense necessity results need independent specialist verification before publication claims.