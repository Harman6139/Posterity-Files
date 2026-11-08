# Milestone 77 — exact dual tropical Shapley equation for tied-edge PSD facial-reduction times

**2026-11-08. PROVED for the full finite tied-edge generator family of checkpoint 74, with arbitrary finite sets of modes per internal vertex and all modes' edges globally distinct.** This is a dual counterpart to the exact primal min–max stochastic-game exponent theorem. It is not a universal dense-to-game reduction.

## Definition

Vertices O=0, internals 1,...,h and terminal T=h+1. Every internal i has a nonempty finite family A_i of modes; each mode a contains a nonempty finite set E_(i,a) of edges (u,v) with u<i<v. Each individual edge is globally unique.

For exposing times in N∪{∞}, set boundary times t_O=∞, t_T=1. Define a symmetric operation
\[
\tau(a,b)=\begin{cases}
a,&a=b,\\
\min(a,b)+1,&a\ne b,
\end{cases}
\qquad \tau(\infty,b)=b+1
\quad(b<\infty).
\]
Define a monotone map on internal integer times:
\[
\boxed{
(\mathscr D t)_i
=
\max_{a\in A_i}
 \min_{(u,v)\in E_{i,a}}\tau(t_u,t_v).
}
\tag{1}
\]

## Theorem

Initialize t_i^(0)=1 for all internal vertices, retaining t_O=∞,t_T=1. Then the iterates t^(m+1)=\mathscr D t^(m) are componentwise nondecreasing, bounded above by h+1, and stabilize at the *least* fixed point t*. The actual canonical greedy facial-reduction peeling times of checkpoint 74 are precisely t*. Consequently:
\[
\boxed{\operatorname{singdeg}=\max_{i\in\{1,\ldots,h,T\}}t_i^*}
\]
and its exact rank-drop profile is the numbers of vertices with each time j. This requires **only finite integer min/max operations**, no semidefinite optimization.

Combined with the primal equation
\[
w_i=\min_{a\in A_i}\max_{(u,v)\in E_{i,a}}\tfrac12(w_u+w_v),
\]
the family has a strict min–max versus max–min duality: primal value uses minimization across coefficient modes and maximization across edges tied within one coefficient; facial exposure uses maximization across modes and minimization across the same edge sets.

## Proof

1. The function \tau is nondecreasing in each argument on N∪{∞}; this follows by checking the cases a<b, a=b, a>b. Hence both finite minimum and maximum preserve monotonicity. From all internal ones, \mathscr D t^(0)≥t^(0), so all iterates increase.

2. A complete proposed exposure-time assignment t (with source ∞ and terminal1) defines at each time j the set C_j={v:t_v=j}, and R_j={v:t_v≥j}∪{O}. It gives valid exposing-closed layers in the AND-across-modes/OR-within-mode rule iff
\[
t_i\ge\max_a\min_{(u,v)\in E_{i,a}}\tau(t_u,t_v)
\tag{2}
\]
for every internal i. Verify (2) edgewise: for an edge with parent times p,q, it is an acceptable witness at stage t_i exactly when either some parent was removed earlier (t_i>min(p,q)), or both parents are removed at the same stage (t_i=p=q). This is *equivalent* to t_i≥\tau(p,q). A mode is satisfied when some edge is acceptable, i.e. t_i≥min_edge \tau; all modes must be satisfied, i.e. the maximum over modes. Thus (2) is exactly the facial closure condition.

3. Greedy exposing closure removes at least one non-source vertex each step: the highest-index remaining vertex has every higher-index parent already removed, so all its modes are automatically disabled and that vertex is individually removable. Therefore all vertices are removed by stage h+1. Let g be the exact greedy times. Its layers are exposing-closed, so g≥\mathscr D g. As t^(0)≤g, monotonicity gives t^(m)≤g for every m. The coordinates are increasing bounded integers, so they stabilize in finitely many steps at a fixed point t*≤g.

4. At that fixed point (2) holds, so C_j={v:t*_v=j} are exposing-closed layers. They constitute a valid facial reduction schedule, possibly allowing empty stages; removing the maximal exposing set greedily cannot occur later than such a schedule, so g≤t* componentwise. Together with t*≤g this gives t*=g. In particular no empty stages occur at the fixed point, and the exact minimal singularity degree and exposing rank profile follow from the earlier proved canonical maximal-rank facial peeling theorem.

Every load-bearing implication is now established. QED.

## Reproducibility

The exact standard-library test in checkpoint 78 independently computes:
- the greedy AND–OR exposing layers; and
- the least fixed point (1) by integer iteration.

For h=3 and h=4 with *one tied mode per internal vertex and at most two edges per mode*, it exhaustively checks **104 + 6,902 = 7,006 globally edge-disjoint systems**. Every instance agrees exactly. The theorem applies to arbitrary finite mode counts and edge sets, not only the tested cases.

## Scope and frontier

This is a **complete exact dual combinatorial invariant within the tied-edge incidence construction class**. The dense-kernel universality question remains whether every arbitrary PSD exponent/rank-profile triple can be realized in this tied-edge game family at the *same matrix size*. The previous independent-edge two-policy universality was disproved by checkpoint 75. This theorem does not assert that the tied-edge game model is universally sufficient.

Prior tropical Shapley games and facial reduction have substantial literature; bibliographic priority of this specific PSD exposing-time formula remains unaudited.