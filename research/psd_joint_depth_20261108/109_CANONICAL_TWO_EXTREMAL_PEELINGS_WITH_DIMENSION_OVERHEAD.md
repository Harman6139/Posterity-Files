# Milestone 109 — for EVERY harmonic valuation graph, BOTH universal peeling bounds are attainable with ≤2x nullity

**2026-11-08. PROVED, dimension-independent, exact-rational constructive theorem.** This is the first explicit uniform interpolation *endpoint* realization theorem that starts from any given strict harmonic weight vector and preserves its full weight data, its distinguished sharp exponent, and its exact two canonical primal/dual peeling extremes. It is NOT a fixed-nullity proof of ALL intermediate depths. The obstruction is edge collision; a controlled vertex-clone construction resolves it with a linear nullity overhead.

## Input

Let h≥1, vertices 0 (source), 1,...,h (internal), k=h+1 (terminal), with a strictly increasing rational harmonic vector
\[
0=w_0<w_1<\cdots<w_h<w_k=1.
\]
For every internal i fix a tight distinct-parent pair P_i=(a_i,b_i),
\[
0\le a_i<i<b_i\le k,\qquad 2w_i=w_{a_i}+w_{b_i}.
\]
The P_i parent edges are automatically distinct: one shared edge would give equal midpoint weights at two different children. Fix any valid sharp leading exponent \(\alpha=w_v/2\le w_1\), or \(\alpha=w_1\), which equals a half-weight by the parent equation of vertex1.

Define the universal ORIGINAL-DENSE grade-only peeling recurrences of milestone99:
- L(w): remove terminal k first, and at each remaining prefix 0,...,j remove the suffix after
  \(\ell(j)=\#\{1\le i<j:2w_i<w_{j+1}\}\);
- U(w): remove terminal k first, then at each remaining prefix 0,...,j remove suffix \(p(j),...,j\), where
  \(p(j)=\min\{1\le p\le j:2w_p>w_j+w_{p-1}\}\).

## Theorem

There exist TWO explicitly described rational PSD inverse problems (real symmetric matrices, rank-one target, global full-ambient exact Hölder exponent alpha) with:
- the SAME h internal scalar Bellman weight values w_i as the input, possibly with duplicate diagonal-coordinate clones;
- exactly the LOWER canonical minimal facial degree \(d=L(w)\) for the first system;
- exactly the UPPER canonical minimal facial degree \(d=U(w)\) for the second system;
- respectively nullities at most \(2h+1\) and \(2h\), versus the original scalar nullity \(h+1\).
For arbitrary prescribed positive target rank r, fully measuring additional positive support coordinates preserves every invariant.

The systems use at most ONE tight parent action and ONE additional parent action per internal vertex:
- for L(w), the additional edge is TIED to its tight generator and has lower midpoint weight;
- for U(w), the additional edge is a separately controlled Bellman-slack or tied generator.
All needed parent-edge uniqueness is restored by cloning at most one endpoint for each added edge.

In particular, **the two scalar grade-only primal/dual bounds are not merely obstructions**. Each is attained by a finite real PSD construction at explicitly bounded dimension for EVERY strict harmonic weight sequence, with exact same exponent alpha. This does not prove either endpoint can always be attained at the original minimum nullity h+1.

## I. Canonical release edges attaining L(w)

For each internal i define
\[
c_i=\max\{\,b\in\{i+1,\ldots,k\}:w_b\le2w_i\,\}.
\]
This set is nonempty, because the tight parent pair satisfies
\(w_{b_i}=2w_i-w_{a_i}\le2w_i\).
The release edge is \(f_i=(0,c_i)\), of midpoint average \(w_{c_i}/2\le w_i\).

Take at each child i ONE generator whose offdiagonal support consists of both the tight edge P_i and the release edge f_i (if identical, keep it only once):
\[
H_i=D_i-\kappa_iE_{00}
    +\lambda(F_{P_i}+F_{f_i}),
\]
where \(D_i\) is the sum of all diagonal clone projectors for vertex i and \(\kappa_i\) its multiplicity. Because the release edge's midpoint average is at most w_i, the Shapley MAX over this one tied mode remains EXACTLY w_i, and the independent leading edge or a diagonal leading coordinate gives sharp alpha.

**Abstract exposing proof, BEFORE cloning.** Suppose the remaining vertices are the prefix \(\{0,1,\ldots,j\}\) and vertex j+1 was exposed just previously. Let
\[
q=\#\{i<j:2w_i<w_{j+1}\}.
\]
For each i>q with i≤j we have \(2w_i\ge w_{j+1}\), hence \(c_i\ge j+1\); its tied release edge f_i touches an already removed coordinate, and the ENTIRE one mode is inactive. Therefore every vertex in the suffix \(\{q+1,\ldots,j\}\) is exposable in the same step. Conversely for i≤q we have \(2w_i<w_{j+1}\), so c_i≤j and the mode is active. Every edge in that mode has a lower parent strictly below i: the original P_i has a_i<i, and the release f_i has lower source0. If any exposing-closed set contained a vertex i≤q, choose its SMALLEST such index i; its active mode would need some edge entirely inside the exposed set, impossible because each edge has a lower endpoint below i and no smaller i≤q is exposed. The source is never exposed. Hence the suffix is MAXIMAL. Initially all modes are active and the same strictly decreasing-parent argument exposes only the terminal. Induction proves the **exact** peeling recurrence L(w).

**Collision resolution.** A release edge f_i may equal another child's tight edge or another release edge. For every i whose release edge differs from P_i, create ONE new clone of the upper endpoint vertex c_i (even if there is no collision), and place f_i on the source-to-new-clone edge. Distinct i have distinct new clones, so no extra release edge collides with any tight edge or another release edge. The resulting clone multiplicities satisfy
\[
\nu_L=(h+1)+\#\{i:f_i\ne P_i\}\le2h+1.
\]
All clones share their vertex's original weight and are exposed simultaneously at the group level, by the exact vertex-blow-up stress theorem (checkpoint52), extended verbatim to tied modes (checkpoint83). The optional leading source-to-v edge uses the ORIGINAL representative v, so it is distinct from release edges on new clones and from every tight parent edge when alpha<w1. If alpha=w1 no separate leading edge is necessary.

## II. Canonical nearest-safe edges attaining U(w)

For each internal i put
\[
b_i^{\rm safe}
=\min\{b\in\{i+1,\ldots,k\}:
 w_{i-1}+w_b\ge2w_i\}.
\]
This set is nonempty: since the chosen tight parent lower index satisfies a_i≤i−1,
\(w_{i-1}+w_{b_i}\ge w_{a_i}+w_{b_i}=2w_i\).
Define \(e_i=(i-1,b_i^{\rm safe})\). It is Bellman-safe, since its parent average is ≥w_i. The edges e_i are pairwise distinct, because their lower endpoints i−1 are distinct.

Give vertex i two independently controlled one-edge generators with the tight P_i and the safe e_i (if identical, retain one). The Bellman MIN of their parent averages remains w_i. Thus exact sharp exponent alpha is unchanged.

**Abstract exposing proof.** Suppose remaining vertices form prefix 0,...,j. Put
\[
p=p(j)=\min\{i≤j:2w_i>w_j+w_{i-1}\}.
\]
The suffix C={p,...,j} is exposing-closed for EVERY active tight/safe action at a child i≥p: if its lower parent a<p and higher b≤j, its midpoint average satisfies
\[
(w_a+w_b)/2\le(w_{p-1}+w_j)/2<w_p\le w_i,
\]
contradicting the tight equality or the safe inequality. Thus both active parents lie in C. Conversely if i<p then, by minimality of p,
\[
2w_i\le w_{i-1}+w_j,
\]
so the safe edge e_i has b_i^{safe}≤j, remains active, and its lower parent i−1 is still present. Any purported exposing set containing a lower-prefix vertex would, taking the least such i, violate the all-actions closure because i−1 cannot belong to that set. Therefore **no vertex below p is exposable** in that step. The suffix C is maximal, and the exact greedy recurrence is U(w). Initially terminal alone is exposed, as usual.

**Collision resolution.** If an added safe edge e_i is already used by another child's tight action, clone ONLY its lower parent vertex i−1 and put the safe edge on that clone instead of its original representative. The case i=1 never collides across children: its lower parent is source0 and the first tight harmonic parent edge is exactly e1=(0,b1^safe). For i≥2, i−1 is a positive null vertex and a clone is legitimate. All e_i distinct, so at most h−1 clones are necessary:
\[
\nu_U\le (h+1)+(h-1)=2h.
\]
The exact vertex-blow-up theorem proves that all clones of a vertex share the same exposing time and that the full harmonic/Bellman recovery estimates survive. An optional leading edge (0,v) with alpha<w1 does not collide with any added safe edge, because every added safe edge has lower endpoint ≥1, and it cannot be a tight parent edge or the chosen child would have harmonic value alpha<w1.

## III. Why the constructions are genuine PSD recovery systems

Take lambda a sufficiently small positive rational, e.g. less than 1/[100(ν+1)]. For every generator mode, the diagonal contribution is the sum of the clones of the child vertex minus their number times E00, and its offdiagonal contribution is lambda times its one or two globally unique parent edges. Let K be the span of these generators and optional independent leading source edge; L is orthogonal projection to K-perp. The matrix identity is in K-perp and each terminal-clone diagonal variable is measured. The full-PSD recovery upper bound follows from the exact two-by-two principal-minor Shapley estimate in checkpoint74/83, where tied edges give a min of parent geometric means, independent modes give their sum. The monomial curve that activates only the minimizing mode at each child is strictly PD after diagonal normalization, with nonzero offdiag entries bounded by lambda. The global competitor upper rate and matching lower curve yield sharp alpha, unique target recovery.

The exact greedy exposing rank/depth, including all clone multiplicities, follows from the AND-across-modes / OR-within-mode facial stress equivalence of checkpoint74/83, whose proof constructs a PSD stress positive on all clones of each eligible vertex in ONE facial step. No arbitrary PSD stress can expose an ineligible vertex's clone earlier, due to the positivity of the offdiagonal parent entries and sum-of-clone-diagonal dual equations.

## IV. Exact tests and honest scope

An independent exact Fraction program (checkpoint110) exhaustively checked the abstract constructions for EVERY strictly increasing harmonic parent policy with h=1,...,5 internal vertices: strict policy counts (1,3,18,165,2099), and in every case the constructed L- and U-schedules agree EXACTLY with the original-kernel recurrences (99.1)–(99.2). The explicit clone assignment and edge uniqueness can be checked symbolically from the rules above; no SDP numerical testing is used.

**This closes the whole gap for attaining BOTH profile-free depth bounds when a LINEAR nullity enlargement is allowed. It does NOT prove fixed-\(\nu\) interval sufficiency**, where edge collisions cannot necessarily be repaired by clones. Indeed milestone107 shows that intermediate degrees cannot simply be obtained by one-edge unit increments: a single Bellman-neutral action may jump two facial steps.

The original ALL-DENSE spectrum theorem at fixed \(\nu\) remains open beyond the previously verified small nullities, and complete exact rank-drop-profile spectra remain a separate stronger objective.