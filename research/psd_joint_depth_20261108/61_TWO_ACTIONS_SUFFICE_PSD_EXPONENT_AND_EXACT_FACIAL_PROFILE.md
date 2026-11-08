# Milestone 61 — TWO ACTIONS PER VERTEX SUFFICE to preserve exact PSD recovery and all facial ranks

**2026-11-08. FULLY PROVED for the finite controlled midpoint PSD incidence class (checkpoint 57), including every ambient PSD competitor and the *entire canonical maximal-rank facial-reduction profile*.** This is a sharp simplification of the proposed richer combinatorial model. It does NOT claim every arbitrary dense kernel can be represented by such a model.

## Main theorem

Let A_i be nonempty sets of parent pairs (a,b), 0<=a<i<b<=T, on source O=0, internal vertices 1,...,h, terminal T=h+1; assume parent edges globally distinct and the controlled Bellman value vector w is strict:
    w_O=0, w_T=1, w_i=min_actions (w_a+w_b)/2,
    0<w_1<...<w_h<1.
Allow an optional leading independent source-to-vertex edge. Construct the real PSD incidence problem as in checkpoint 57. Let alpha be its exact full-state recovery exponent and s=(s_1,...,s_d) its canonical minimal exposing rank profile.

**Then there exists a subcollection B_i⊆A_i with**
\[
\boxed{1\le |B_i|\le2\quad\text{for every }i}
\]
such that the *smaller* real PSD inverse problem formed by retaining only those kernel generators has **exactly the same strict Bellman weights w, the same optimal Hölder exponent alpha, and exactly the same complete exposed-rank profile s**.

More sharply, B_i may be chosen as the union of:
- one *primal-optimal* action minimizing (w_a+w_b)/2;
- one *dual-exposing* action selected by the finite rooted-reachability construction below.

The sufficiency of 2 actions does not assert a matching lower bound: many instances require only 1, but the 6×6 counterexample in checkpoint 58 **provably needs 2 actions at one vertex** to match its exponent and depth at minimal nullity.

## Lemma 1 — maximal exposing sets are complements of SOURCE REACHABILITY

Fix any current remaining set R containing source O. Build a finite directed graph Γ_R with vertex set R. For each internal i∈R, and every action (a,b)∈A_i whose **both parents** a,b remain in R, place directed arcs
    a -> i,  b -> i.
(There are no arcs INTO terminal T because it has no generator.)

Let B_R be the set of vertices reachable from source O in Γ_R, including O itself. Then
\[
\boxed{C_{\max}(R)=R\setminus B_R}
\]
is the unique largest exposing-closed vertex set in the all-actions facial-peeling rule of checkpoint 57.

**Proof.** A removable set C⊆R\{O} is closed exactly when, for every active action whose child i lies in C, both parents also lie in C. Its complement B=R\C therefore contains O and is closed under the directed arcs parent->child: if p∈B and p->i is an active arc, then i∈B. The least arc-closed set containing O is its directed reachability set B_R. Therefore the largest removable C is R\B_R. The exact PSD exposing-stress theorem of checkpoint 57 guarantees this C is precisely the support removed by a single maximal-rank compressed PSD stress. QED.

At each stage k, the remaining set is
    R_k={O}∪{v: exposure_time(v)>=k}.
Let t_v be the **original** greedy exposure time; t_T=1, while every internal t_i>=2 because all lower-parent dependency chains originate at O. Then
    B_(R_k)={O}∪{v:t_v>k}.
The terminal is never source-reachable.

## Lemma 2 — ONE deterministic exposing action per vertex preserves EVERY peeling time

Construct a subpolicy π_i∈A_i with one action at each internal vertex as follows.

Process exposure-time levels in *descending* order, starting from the largest time D. When processing vertices with exposure time t=k+1, let
    H={O}∪{v:t_v>k+1}
be the source plus all vertices exposed strictly later, already assigned π actions. Let
    L={v:t_v=k+1}
be the current new time-level, and let R_k=H∪L∪{v:t_v=k}.
By Lemma 1 the original active dependency graph Γ_(R_k) reaches **every vertex in H∪L** from source; none of the vertices with t_v=k are reachable.

Construct a directed spanning forest from the already reachable seed set H into all vertices of L, using only active parent->child arcs of Γ_(R_k). For each newly reached vertex i∈L, select and store one action π_i=(a,b) that generated the incoming forest arc. Both its parents remain in R_k. A spanning forest exists: every vertex of L is reachable from H in the original Γ_Rk, and every intermediate vertex on such a path belongs to H∪L because the reachable set is exactly H∪L.

**Induction:** The selected π actions on higher-time vertices already make every vertex of H source-reachable in the smaller policy graph Γ_Rk^π: they were chosen on smaller remaining sets at later stages, and all their parent endpoints are still present on the larger R_k. Adding the forest actions makes every vertex of L reachable as well. Thus the smaller policy graph reaches precisely H∪L=B_(R_k), since its arcs are a subset of original arcs. Its maximal peeling stage removes exactly {v:t_v=k}. Descending induction preserves every exposing stage and hence the *entire minimal facial profile*.

For the time-one terminal there is no action; any internal vertex (if a pathological non-strict variant permitted it) that lacked a selected action could be assigned arbitrarily, which cannot create additional source reachability. Under strict ordered parents, all internal times are >=2 and all get one chosen action.

This produces π with the **same canonical greedy peeling times t** even though the full action system may have many actions per node. QED.

## Proof of main theorem — union of a primal and dual policy

For each i choose one action μ_i∈A_i satisfying
    2w_i=w_a+w_b.
It exists because A_i is finite. Define
    B_i={π_i, μ_i}
as a set, size at most two. All action edges remain distinct because B_i⊆A_i.

**Primal side:** Every retained action has parent average ≥w_i (because w is a solution of the original Bellman minimum), and the retained μ_i attains equality. Hence w is a fixed point of the reduced Bellman system. Uniqueness of the proper finite controlled harmonic system implies that the reduced system has EXACTLY the same w, so checkpoint 57 gives the same sharp exponent alpha.

**Dual side:** The one-action π subpolicy has exposing times exactly t by Lemma 2. Adding the μ actions can only increase exposing times (the tropical monotonicity theorem in checkpoint 59), whereas removing all other original actions can only decrease them. Since π⊆B⊆A,
    t(π) <= t(B) <= t(A),
and both endpoints equal t. Thus t(B)=t, including every exposed-rank layer and the exact minimal facial degree. QED.

## Efficient constructive algorithm

The primal policy uses Bellman-optimal action extraction. The dual policy takes O(d*(h+|A|)) graph-search work using the original exposure stages and BFS forests; one can calculate stages by reachability rather than a semidefinite solver. The full two-action construction retains at most 2h kernel generators, in addition to an optional leading edge. Thus this is a **linear-size normal form inside the multiaction family**.

The result is not obvious from choosing a final-time maximizer of the tropical recurrence: that recurrence can have extraneous nonminimal fixed points. The descending reachability forest avoids this trap by preserving *the least* exposing-time solution, not merely one fixed point.

## Exact exhaustive verification

A standalone Fraction/integer script constructs a deterministic reachability-forest π for every one of the 17,169 collision-free h=4 multiaction action systems and for all 24,821 strictly ordered h=5 single-action networks with one additional nonimproving action. The union of π with one Bellman-optimal action per vertex always reproduces **both** the original rational Bellman vector and the exact greedy exposing layers. At h=4, 10,267 of the audited graphs had at least one node with three or more actions, so the check substantially tests the reduction. All 41,990 cases passed.

## Significance and limitation

The two-action normal form is a concrete **bidirectional compression of the two competing invariants**: one action is enough to witness the recovery-rate minimum, another is enough to witness the slowest exposing schedule, and both can be retained simultaneously with no loss.

It makes finite combinatorial classification substantially smaller: to enumerate all exponent/profile pairs realized by multiaction PSD incidence systems with h internal nodes, it suffices to enumerate at most two actions per vertex, then use rational Bellman and the integer tropical peeling recurrence.

**Still unresolved:** Whether EVERY arbitrary dense uniquely solvable PSD inverse problem at fixed target nullity and exposing rank profile has a realization by this two-action normal form. The result gives complete reduction for the larger multiaction incidence class, NOT a universality theorem for all dense matrix kernels. A generic dense pencil may have coupled offdiagonal coefficients, cancellations, non-coordinate exposing flags, or other mechanisms that are not yet known to be simulable by independent parent actions.