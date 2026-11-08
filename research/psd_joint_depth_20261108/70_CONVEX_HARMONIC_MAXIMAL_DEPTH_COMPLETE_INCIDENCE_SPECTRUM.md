# Milestone 70 — discrete convexity COMPLETELY classifies the maximal-depth spectrum of every strict multi-action PSD incidence system

**2026-11-08. PROVED for the entire strict multi-action midpoint-incidence PSD family**, including arbitrary finite action sets and independent optional leading edges. This gives a necessary-and-sufficient finite *one-policy* combinatorial certificate for **all attainable exponents at maximal degree** within that family, even though a genuine second slack action may be required for the facial rank profile. It does NOT assert necessity for arbitrary dense PSD kernels.

## Theorem — maximal-depth exposure iff an adjacent-upper action exists at every vertex

Consider the strict controlled Bellman/harmonic system of checkpoint 57 with h internal vertices, source 0, terminal T=h+1, and 0=w0<w1<...<wh<1=wT. Each internal i has a nonempty set A_i of pairs (a,b) with a<i<b; action edges globally distinct. Its canonical minimal facial degree is d.

Then
\[
\boxed{d=h+1\ \Longleftrightarrow\
\forall\,i=1,\ldots,h,\ 
\exists (a_i,i+1)\in A_i\text{ with }a_i<i.}
\tag{1}
\]
If these conditions hold, the greedy exposing schedule is *forced* to be
    {T},{h},{h-1},...,{1}
(one null coordinate per exposing step).

**Necessity.** There are h+1 non-source vertices, so d=h+1 means every step exposes exactly one. The terminal is always individually exposable, hence is first. After removing all indices greater than i, every parent pair at vertex i has higher parent b>i already removed, so i is individually exposable. Induction forces the singleton schedule in descending index order. At the step before removing i+1, all vertices {0,1,...,i+1} remain. To prevent i from also being exposed then, some action of i must have *both* parents still remaining. Its higher parent b>i must equal i+1. This gives the required adjacent-upper action.

**Sufficiency.** If all adjacent-upper actions exist, first terminal is exposable. Before vertex i+1 is removed, every still unexposed lower vertex j<=i has an active action (a_j,j+1), with both parents still remaining. If a nonempty exposing-closed set included any lower vertex, it would have to include its lower-parent a_j, and repeating the strictly decreasing lower-parent relation would force the source 0 into the exposing set, impossible. Thus only the highest remaining non-source vertex can be exposed. After that vertex is removed, the next-highest vertex has all higher parents already removed and is individually exposable. By induction the exact schedule is {T},{h},...,{1}. Checkpoint 57 proves exposing-closed sets correspond exactly to compressed PSD exposing stresses, giving minimal degree d=h+1. QED.

## Corollary — NECESSARY DISCRETE CONVEXITY of Bellman weights

Since the Bellman weights satisfy w_i<= (w_a+w_b)/2 for EVERY action, the adjacent-upper action at i gives
\[
2w_i\le w_{a_i}+w_{i+1}\le w_{i-1}+w_{i+1}.
\]
Therefore
\[
\boxed{0<w_1-w_0\le w_2-w_1\le\cdots\le w_T-w_h}.
\tag{2}
\]
Maximal minimal facial degree forces the entire harmonic weight sequence to be **discretely convex**. This is not a statement about arbitrary dense kernels' sharp valuation flags; it is proved for strict incidence systems.

## Converse — EVERY convex harmonic policy has a collision-free two-action maximal-depth realization

Let P select a *single harmonic parent pair* (a_i,b_i), with
    2w_i=w_(a_i)+w_(b_i),
producing strictly increasing weights 0=w0<...<wh<1=wT. Suppose these weights satisfy (2).

For each i add the nearest-neighbor action
\[
\boxed{D_i=(i-1,i+1)}
\]
if it is not already P_i. By convexity, its parent average is >=w_i, so it is Bellman-slack or Bellman-tied and DOES NOT alter the optimal harmonic weights. The new edges are **automatically collision-free**:
- D_i has two endpoints whose indices differ by exactly two. The *only internal child* strictly between them is i, so it cannot equal P_j or D_j for j≠i.
- If P_i=D_i, retain one copy.
- The original P edges are distinct, because if two child vertices shared an identical parent edge, their strict harmonic values would be equal, violating the strict weight order.

Every vertex now has an adjacent-upper action, so the theorem above gives the **exact maximal facial degree h+1**.

Let the intended recovery exponent be a valid leading half-weight α=w_v/2<=w1 for v∈{1,...,h,T}. If α=w1, no optional leading edge is needed: the smallest internal diagonal variable gives exponent w1. If α<w1, add the independent edge (0,v). It cannot collide with any P_i, because such a harmonic parent pair (0,v) would force w_i=w_v/2=α<w1. It cannot collide with any D_i except when i=1,v=2, but convexity gives w2/2>=w1, contradicting α<w1. Thus the leading edge is always available when needed.

The multiaction recovery theorem of checkpoint 57 then supplies
\[
\omega(\delta)=\Theta(\delta^\alpha)
\]
for ALL ambient PSD competitors and the exact exposing profile (1,...,1).

## EXACT finite full spectrum in the maximal-degree incidence family

For target nullity ν=h+1, define
\[
\mathcal C_\nu=
\left\{\,\alpha:
\begin{array}{l}
\text{there exists a strict harmonic one-policy network}\\
0=w_0<w_1<\cdots<w_h<w_{h+1}=1,\\
2w_i=w_{a(i)}+w_{b(i)},\ a(i)<i<b(i),\\
w_{i+1}-w_i\ge w_i-w_{i-1}\ \text{for every }i,\\
\alpha=w_v/2\le w_1\ \text{for some }v=1,\ldots,h+1
\end{array}
\right\}.
\tag{3}
\]

Then
\[
\boxed{\mathcal C_\nu=
\Sigma_{\nu,d=\nu}^{\rm strict\ multiaction\ incidence}.}
\tag{4}
\]

**Necessity:** pick one Bellman-optimal action at every vertex from an arbitrary maximal-depth multiaction system; the resulting one-policy harmonic network has the SAME strict Bellman weights. Convexity is forced by (1). The full recovery exponent is a valid leading half-weight (every minimum internal weight w1 is also a half-weight: the parent pair of vertex 1 has lower parent source and higher parent weight 2w1, so w1= w_b/2). Thus α appears in (3).

**Sufficiency:** the explicit collision-free nearest-neighbor completion above realizes every α from (3), exactly at maximal depth. This is a complete arithmetic/combinatorial iff theorem for this large explicit PSD class.

The enumeration requires at most (h!)² rational harmonic systems rather than the earlier (h!)^4 two-policy combinations. The distinction is substantial: one policy determines the **value**, and deterministic convex completion supplies the **depth**.

## First nonreciprocal values and exact audit

Exact Fraction enumeration gives the following:
- h=1,2,3,4 (nullity ν≤5): every convex harmonic network has ONLY reciprocal valid sharp exponents at maximal degree;
- h=5 (ν=6): exactly 208 strict convex harmonic one-policy networks; the maximal-depth multiaction spectrum contains **46 distinct exponents**, of which three are nonreciprocal:
\[
\boxed{3/46,\quad 3/23,\quad 2/15}.
\]
All other 43 are reciprocal. This agrees with the formerly known 43-element *single-action* maximal-depth catalogue. The explicit 3/46 system and its full PSD proof are in checkpoint 68. A 2/15 example uses harmonic weights (2/15,4/15,2/5,3/5,4/5,1) and one additional nearest-neighbor slack action, with the smallest internal diagonal supplying the sharp exponent.

These numbers are certified by a self-contained standard-library Fraction enumerator (checkpoint 71). The theorem is symbolic for every ν, not based on finite testing.

## Limits and significance

This proves **a complete convex-harmonic combinatorial classification at maximal singularity degree inside the strict multiaction incidence family**, and gives a universally valid constructive *lower inclusion* for arbitrary dense PSD spectra. It explains precisely how maximal-depth nonreciprocal instability can occur.

It does NOT establish the missing universal reverse inclusion for arbitrary dense kernels at any ν≥5. In particular, do not replace the full universal dense classification by (3) without proving that every arbitrary dense pair has some convex harmonic witness with the same exponent/nullity/depth. That is still an open research problem.

Stochastic Bellman equations, finite harmonic networks, and greedy facial reduction are prior mathematical mechanisms; bibliographic novelty of the combined convexity iff characterization has not been audited.