# Milestone 79 — TWO GENERATOR MODES × TWO TIED EDGES suffice for exact PSD recovery exponents and ALL exposing ranks

**2026-11-08. PROVED WITHIN THE FULL FINITE TIED-EDGE MIN–MAX PSD INCIDENCE FAMILY of checkpoints 74 and 77, for all strict rational game value vectors.** There is no claim that arbitrary dense kernels reduce to this construction. This substantially strengthens the earlier two-mode theorem restricted to single-edge modes, and gives a bounded-support normal form for the more expressive tied-edge game family.

## Theorem

Let vertices be source 0, internals i=1,...,h, terminal T=h+1. Each internal vertex i has a nonempty finite set A_i of generator modes. A mode a has a nonempty finite set E_(i,a) of parent edges (u,v) with 0<=u<i<v<=T; all action edges are globally distinct. Its exact PSD recovery rate and facial degree are determined by:

- a unique strict stochastic-game value vector 0=w0<w1<...<wh<wT=1 satisfying
\[
 w_i=\min_{a\in A_i}\max_{e=(u,v)\in E_{i,a}}(w_u+w_v)/2;
\]
- the canonical greedy exposure times t_i from the all-modes AND / within-mode OR peeling rule (checkpoints 74 and 77).

An optional independent source-to-vertex leading edge may be present.

**There exists a subfamily obtained ONLY BY DELETING WHOLE MODES AND DELETING INDIVIDUAL EDGES FROM RETAINED MODES such that**
\[
\boxed{\text{at most TWO modes at each internal vertex and at most TWO edges in each retained mode}}
\]
and **its entire game value vector w, optimal full ambient PSD Hölder exponent, all canonical exposure times and thus the entire minimal facial-rank profile remain EXACTLY unchanged.**

The two modes per internal vertex can be chosen as one primal minimizing mode and one dual blocking mode. Within each retained mode, the two edges can be chosen as one primal maximizing edge and one dual release edge. Either pair may coincide, so many vertices need fewer.

In particular the set of exponent/profile pairs realized by ALL finite tied-edge incidence PSD systems with at most h internal vertices is completely represented by a finite list of generators with at most 2h modes and 4h distinct parent edges, plus at most one optional independent leading edge. Their full-matrix competitors are governed by the already-proved min–max theorem.

## Lemma 1: monotone hypergraph reachability describes every greedy exposing step

Fix a currently remaining vertex set R containing 0. A mode a at child i∈R is *active* if every endpoint of every edge of E_(i,a) remains in R. For a candidate nonremovable set B⊆R containing 0 define the reachability closure
\[
\Phi_R(B)=B\cup\{i\in R\cap\{1,\ldots,h\}:
 \exists a\in A_i \text{ active in }R,\
 \forall e\in E_{i,a},\ e\cap B\ne\emptyset\}.
\]
Start with B={0} and iterate the monotone operator to its least fixed point B_R.

Then the unique maximal one-step exposing set from checkpoint 74 is
\[
\boxed{C_{\max}(R)=R\setminus B_R.}
\]
Proof: An exposing set C⊆R\{0} is closed iff every active mode of each i∈C contains at least one edge e⊆C. Its complement B=R\C contains 0 and satisfies: whenever some active mode at i has every edge intersecting B, then i∈B. These are precisely the fixed-point supersets of Φ_R. Taking the least such B maximizes C. The PSD stress construction of checkpoint 74 realizes this maximal set, so the abstract closure is an EXACT facial step. QED.

## Lemma 2: ONE exposing mode per child preserves the full greedy exposing schedule

Let d be the original minimal facial degree, t_i the original exposing time (with t0=∞ and tT=1), and C_j={i:t_i=j}. Every internal i has t_i≥2: if an internal i were in the first exposing set, at the full initial face every mode is active, and for each i in that set one must choose an internal parent edge whose lower parent is also in the set. Repeatedly descending the lower-parent index would eventually require source0 in the exposed set, contradiction.

We construct selected exposing modes π_i one per internal vertex, processing time levels **in descending order**. For each j=d-1,d-2,...,1, set
\[
R_j=\{0\}\cup\{v:t_v\ge j\},\quad
H_j=\{0\}\cup\{v:t_v>j+1\},\quad
L_j=\{v:t_v=j+1\}.
\]
(The terminal has tT=1 and is absent from H_j,L_j for j>=1.)

Inductively, already selected π modes on H_j\{0} make that set reachable from source under Φ_Rj, because their earlier witness derivations on smaller remaining sets remain active and valid on the larger R_j. By Lemma 1, the original closure from source on R_j yields exactly
\[
 B_{R_j}=H_j\cup L_j.
\]
Starting the original operator Φ_Rj from H_j, monotonically add vertices of L_j until all are reached. At the moment a new i∈L_j enters, select one **active** mode π_i whose EVERY edge intersects the previously reached set. Such a mode exists by the operator definition. The selected mode alone witnesses that same addition; hence after processing L_j, the π-only system reaches H_j∪L_j from source on R_j. Descending induction gives this reachability certificate simultaneously at all stages.

Since π uses a subset of original modes, it cannot make vertices expose *later*: its greedy exposure times are ≤ original times. Since the π reachability certificate keeps every original unexposed vertex unexposed at every earlier stage, its times are ≥ original times. Thus the entire schedule is unchanged. QED.

## Lemma 3: TWO EDGES per selected mode preserve BOTH the game value and all exposing times

Fix selected modes π_i of Lemma 2, and choose at each vertex a primal minimizing mode μ_i with
\[
\max_{e\in E_{i,\mu_i}}\frac{w_u+w_v}{2}=w_i.
\]
Keep only the union of π_i and μ_i.

For EACH retained mode a at vertex i, choose:

1. **A maximizing edge** e_max in E_(i,a), maximizing its average \((w_u+w_v)/2\); this preserves that mode's exact value when evaluated at w.
2. **A releasing edge** e_rel in E_(i,a) certifying that this mode permits the *original* exposing stage t_i: let R_(t_i) be the vertices still present at that stage and C_(t_i) its exposed set. If some edge e of the original mode has an endpoint outside R_(t_i), take one such edge (making the reduced mode inactive at that stage). Otherwise the original exposing-closure condition supplies an edge fully contained in C_(t_i); take such an edge.

Keep the set {e_max,e_rel}, deleting other edges. All retained modes stay nonempty, with at most two edges, and global edge distinctness is preserved.

**Primal w is unchanged:** For each retained mode, its maximum parent average at w is unchanged by keeping e_max. Every original mode's maximum was ≥w_i, while μ_i attains equality. The reduced Shapley operator therefore fixes w. The proper finite stochastic game has a unique fixed point, so the entire rational value vector is exactly the original w. The optional leading edge is unchanged, so the recovery exponent is identical.

**Dual schedule is unchanged:** At each vertex's original stage t_i, every retained mode is either disabled by its releasing edge touching an already removed vertex, or has its releasing edge entirely in C_(t_i). Hence the original simultaneous layers remain an exposing-closed schedule for the reduced system, giving reduced greedy exposure times ≤t. Conversely, for each π_i the mode was chosen at the earlier stage t_i-1 when ALL original edges remained active and intersected a previously reachable set B. Its two retained edges form a subset, are still active then and each still intersects that same prior reachable set. Thus all reachability certificates in Lemma 2 survive the edge pruning. They force the reduced greedy exposure times ≥t. Equality follows, including every rank-drop count. QED.

Combining the lemmas proves the theorem.

## Exact tests

A self-contained standard-library Fraction checker was run on 1,923 strict rational finite Shapley games (internal node counts 3,4,5) generated from exact harmonic policies and additional slack/tied modes. It independently solves each game's rational fixed-point equations, computes its original exposing schedule, compresses to the two-mode/two-edge form, recomputes the exact game value and exposing layers, and checks their equality. All assertions passed. These tests corroborate but do not substitute for the proof.

## Implications

This sharpens the earlier hierarchy:
1. Single-action/independent-edge networks were refuted as universal at nullity5, checkpoint58.
2. Two independent-edge modes per vertex were refuted as universal at nullity5, checkpoint75.
3. The tied-edge min–max family (checkpoint74) strictly extends both. **Within that ENTIRE family, two modes and two edges per mode are sufficient to encode both exact invariants.**
4. The resulting finite combinatorial candidate spectrum at nullity ν can be enumerated over O(ν) finite mode and edge choices, rather than all mode subsets. The enumeration remains factorial/exponential, not claimed polynomial time.

**The genuinely missing universal step is still:** prove or refute that every arbitrary dense PSD exponent/minimal facial-rank-profile triple admits such a tied-edge game realization at equal nullity. This checkpoint is a powerful reduction WITHIN the game model, not that dense reduction. Signed cancellation and high-order determinant degeneracies remain potential obstructions.