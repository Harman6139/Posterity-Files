# Milestone 72 — a bounded INTEGER-GAP Diophantine classification of every maximal-depth multiaction PSD exponent

**2026-11-08. Fully proved, exact iff within strict multiaction incidence PSD systems.** This removes even the rational linear-system step from the convex-harmonic graph classification (checkpoint 70). It is a compact arithmetic description using at most ν positive integers, a total bound \(2^{\nu-1}\), and finitely many interval-sum equalities. It is a universally valid sufficiency theorem for arbitrary PSD recovery. The reverse implication for arbitrary dense kernels is NOT proved.

## Precise theorem

Let target nullity ν≥2 and set h=ν−1. Let \(\mathcal S^{\mathrm{multi}}_{\nu,\nu}\) be the set of sharp full-state Hölder exponents realized by strict finite multiaction incidence PSD systems whose minimal facial degree equals their target nullity ν (i.e. every exposing rank drop is one).

Define \(\mathcal I_h\) to be the finite set of vectors
\[
g=(g_0,\ldots,g_h)\in\mathbb Z_{>0}^{h+1}
\]
satisfying ALL conditions:

1. \(g_0\le g_1\le\cdots\le g_h\) (discrete convexity);
2. \(\gcd(g_0,\ldots,g_h)=1\);
3. \(D:=\sum_{j=0}^{h}g_j\le2^h\);
4. For every \(i=1,\ldots,h\), there exist integers \(0\le a<i<b\le h+1\) with the **balanced-interval equation**
\[
\boxed{\sum_{j=a}^{i-1}g_j=\sum_{j=i}^{b-1}g_j.}
\tag{1}
\]

Let \(S_v=\sum_{j=0}^{v-1}g_j\) for \(v=1,\ldots,h+1\), with \(S_{h+1}=D\). Then
\[
\boxed{
\mathcal S^{\mathrm{multi}}_{\nu,\nu}
=
\bigcup_{g\in\mathcal I_h}
\left\{
\frac{S_v}{2D}:
 1\le v\le h+1,\quad S_v\le 2g_0
\right\}.
}
\tag{2}
\]
All listed exponents occur at target rank one (and at any higher prescribed target rank by fully measured positive padding), with target nullity ν and **exact maximal facial degree ν**. No SDP search, coefficient optimization or rational harmonic solve appears in formula (2).

## Necessity

From checkpoint 70, maximal exposing depth within the strict multiaction family forces its Bellman values
    0=w_0<w_1<...<w_h<w_(h+1)=1
to be discretely convex:
    w_(j+1)-w_j nondecreasing.
Select one Bellman-optimal action (a_i,b_i) at each internal i, so that 2w_i=w_(a_i)+w_(b_i). The reduced h×h integer midpoint matrix M has rows 2e_i-e_(a_i)-e_(b_i), with boundary columns 0,h+1 suppressed. Expand each row as
    (e_i-e_(a_i))+(e_i-e_(b_i)).
Each of the 2^h terms is the determinant of a rooted functional-graph incidence matrix: zero if its selected directed arcs contain an internal cycle, and +1 otherwise (topological elimination gives determinant +1). At least one cycle-free selection exists by choosing the higher parent at every internal vertex, which reaches terminal in at most h steps. Thus
    1<=det M<=2^h.
Cramer's rule shows that each w_i has denominator dividing det M. Let D be the least common denominator of all w_i; then D<=det M<=2^h. Set
    g_j=D(w_(j+1)-w_j)>0.
Convexity gives nondecreasing integer gaps. Since D is the minimal common denominator, gcd(g_0,...,g_h)=1. Their sum equals D.

The harmonic equality for each selected action (a_i,b_i) is exactly
    w_i-w_(a_i)=w_(b_i)-w_i,
and after multiplying by D this becomes the balanced-interval equation (1). Finally the exact sharp full-state exponent in the incidence model is either the minimum internal weight w1=g0/D, or half of an available distinguished internal/terminal weight w_v. Both are covered by the half-weight form: the optimal parent pair of minimum vertex 1 has lower parent source0 and higher parent v, giving 2w1=w_v. Necessarily alpha<=w1, so S_v<=2g0. This proves inclusion of every actual exponent in the right side of (2).

## Sufficiency

Fix primitive nondecreasing positive integer gaps g satisfying (1)–(4). Define rational strictly increasing weights
    w_0=0,\quad w_v=S_v/D\quad(1<=v<=h+1).
For each internal i choose ANY pair (a_i,b_i) witnessing (1). The equality means 2w_i=w_(a_i)+w_(b_i), so these pairs form a single-action strict harmonic network. Its parent edges are globally distinct: if two different children shared the same unordered endpoints, the harmonic equality would give identical child weights, contradicting strict increase.

Discrete convexity implies
    2w_i<=w_(i−1)+w_(i+1).
Adjoin, for every internal i, the nearest-neighbor action (i−1,i+1) if not already present. These actions are Bellman-slack or tied and automatically collision-free (the only integer child between i−1 and i+1 is i). The exact Bellman weights remain w, while the adjacent-upper action condition from checkpoint 70 forces singleton greedy peeling
    {T},{h},{h−1},...,{1}.
Thus the canonical minimal facial degree is ν=h+1.

For every candidate alpha=S_v/(2D)<=g0/D=w1, use the independent source-to-v leading edge if alpha<w1, and no extra edge if alpha=w1. An edge (0,v) with alpha<w1 cannot collide with a harmonic parent edge (that would force a child weight alpha<w1) or any nearest-neighbor action (its only possible such edge is (0,2), for which convexity would give w2/2>=w1). The full PSD incidence recovery theorem of checkpoint 57 then supplies a rank-one uniquely recoverable PSD problem of sharp full-matrix exponent exactly alpha, with matching positive-definite monomial curve and exact maximal facial degree ν. Positive support padding realizes any rank r≥1. QED.

## Exact small spectra and novelty

The accompanying self-contained Fraction/integer program (checkpoint 73) enumerated every primitive nondecreasing gap vector with total D<=2^h through h=5, and cross-checked against independent harmonic parent-network enumeration. Numbers of valid primitive gap vectors for h=1,2,3,4,5 are respectively
    1, 2, 6, 25, 132.
The corresponding numbers of distinct maximal-depth exponents are
    2, 4, 9, 20, 46.
For h<=4 all are reciprocal; at h=5, exactly three are nonreciprocal:
    3/46, 3/23, 2/15.
In particular the concrete primitive gap vector (3,3,3,4,5,5) has D=23 and yields α=3/46, while (2,2,2,3,3,3) has D=15 and yields α=2/15.

**This is an exact bounded Diophantine theorem for a broad explicit class**, not a proof that arbitrary dense SDP spectra are covered by the same integer-gap conditions. The dense-to-two-policy necessity remains the user's unresolved full universal classification question. Ordinary graph determinants and combinatorial mediated-set techniques are prior art; bibliographic priority of this exact gap characterization is unverified.