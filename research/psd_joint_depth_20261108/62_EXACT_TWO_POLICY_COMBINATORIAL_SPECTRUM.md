# Milestone 62 — exact finite TWO-POLICY combinatorial spectrum for the multiaction PSD family

**Date 2026-11-08. PROVED for the explicitly defined two-action/multiaction sparse PSD incidence family, with arbitrary ambient PSD competitors and exact minimal exposing rank profiles.** This is a compact integer-rational certificate rule that avoids continuous feasibility optimization. It is **not claimed universally necessary** for every arbitrary dense kernel.

## Complete certificate data for target nullity nu and facial rank profile s

Let s=(s1,...,sd) be a positive integer composition of nu, and fix positive target rank r. For h=0,...,nu-1, consider vertices 0,1,...,h,T=h+1. An **ordered parent policy** P assigns to each internal i a pair (a_i,b_i) with 0<=a_i<i<b_i<=T. There are exactly (h!)² possible P.

1. Solve the rational harmonic system
      w0=0, wT=1, 2w_i=w_(a_i)+w_(b_i).
   Require 0<w1<...<wh<1. This is a finite rational linear system.

2. Choose a SECOND policy D assigning one parent pair (c_i,d_i) with 0<=c_i<i<d_i<=T. Require the **slack inequalities**
      w_(c_i)+w_(d_i)>=2w_i.
   The union of the P and D action edges must be globally distinct across different child vertices (the two actions at one child may coincide). Each node consequently has at most two independent actions.

3. For every candidate vertex v with weight w_v (including terminal T), set alpha=w_v/2; require alpha<=w1 when h>0. If alpha<w1, the independent leading edge (0,v) must be distinct from all parent-policy action edges. If alpha=w1, the leading displacement can instead use the already-existing diagonal coordinate of weight w1, so a separate source edge is unnecessary. For h=0, alpha=1/2 (terminal).

4. Compute exact **greedy peeling** for the union of the two policies: from current remaining vertices R, put directed edges a->i and b->i for each active action at child i with both parents a,b still in R. Remove all vertices *unreachable* from source 0, repeat until only 0 remains. Let C1,...,CdG be the successive nonempty removed layers. Require dG=d and |C_j|<=s_j for every j.

Call the set of retained rational alpha from all these finite cases \(\mathcal B_s\).

## THEOREM — exact construction family spectrum, universal sufficiency

For every profile s, every r>=1, and every alpha∈B_s, there is an explicit real PSD linear inverse problem on matrices of size n=r+nu with rank-r target, uniquely solvable among PSD matrices, and with:
  * sharp full-matrix recovery exponent **exactly alpha**, including upper bounds for every ambient PSD competitor;
  * minimal canonical facial-reduction degree exactly d, with exact rank-drop profile s.

Conversely **every** problem in the class of strict, globally distinct-edge **multi-action midpoint PSD incidence pencils**, including their vertex-blown-up variants, produces an alpha in B_s. Therefore B_s is exactly that whole family's full exponent/profile spectrum. The conjectural equality B_s=Sigma_s^(all dense kernels) is a separate unproved universality statement.

### Proof of necessity *within the incidence family*

Checkpoint 57 establishes that any multiaction incidence problem's exact exponent is the Bellman value min(w1,w_v/2) and its exact exposing layers are the all-actions greedy closure sets, equivalently complements of source reachability (checkpoint 61). The two-action compression theorem (checkpoint 61) retains, at each internal vertex, one Bellman-minimizing action P and one dual action D selected by descending reachability forests. The reduced action family has exactly the same w and **all** exposing times. The Bellman equations and slack inequalities in (1)-(2) therefore hold. The exponent comes from one of the distinguished half-weights, with the lower-barrier condition alpha<=w1; if alpha=w1, an independent leading edge is unnecessary. Greedy peeling gives precisely the original vertex-level layers.

If the original system is blown up, collapsing identical clone coordinates recovers that vertex graph and its per-layer vertex counts c_j<=s_j. Thus alpha∈B_s.

### Proof of sufficiency and global recovery stability

Given certificate P,D, form the union action set A_i={P_i,D_i}. Define a rank-one PSD pencil with one variable per action,
   H_(i,a,b)=E_ii-E_00+lambda F_ab,
an optional leading generator G=lambda F_(0,v), and target E_00. Choose fixed sufficiently small rational lambda>0. Measure orthogonal projection to the kernel complement. Identity and terminal diagonal are in the measurement span because all generators have trace zero and no terminal diagonal entries.

The harmonic P equations give w_i=(w_a+w_b)/2 for the P action; all D averages >=w_i, so w solves the Bellman minimum, and the proper finite Bellman system has a unique value. The exact all-competitor recovery theorem (checkpoint 57) gives omega(delta)=Theta(delta^alpha), with a matching positive-definite monomial curve and a log-ratio upper bound against every PSD competitor. The all-actions peeling theorem gives exact layers C_j and minimal facial degree.

To reach prescribed s_j>=c_j, choose a positive integer multiplicity kappa_v for every non-source vertex with sum_(v∈C_j)kappa_v=s_j. Replace v by kappa_v identical-diagonal coordinate clones, placing every parent edge on a distinguished representative of its parent. Each generator becomes
   H_(i,a,b)=sum_(q=1)^kappa_i E_(i,q),(i,q)
             -kappa_i E_00+lambda F_(a,1),(b,1).
The optional leading edge still uses the distinguished representative. The full ambient PSD competitor estimate from checkpoint 57 is unchanged up to fixed constants, because the clone diagonals share the same variable and all action inequalities remain valid on distinguished principal 2x2 blocks. The matching curve gives each clone diagonal t^w_v, so after diagonal congruence all offdiagonal entries are bounded by lambda; strict diagonal dominance gives full positive definiteness. Trace normalization controls source coordinate. The exposing-stress equations become
   sum_(q=1)^kappa_i Z_(i,q),(i,q)+2lambda Z_(a,1),(b,1)=0.
Exactly the original all-actions closure rule results from PSD positivity, and a stress positive on all clones in C_j is constructed by assigning their diagonals eta^(-w_i²), with active offdiagonals -kappa_i eta^(-w_i²)/(2lambda). Diagonal-normalized offdiagonals vanish as eta->0 by strict Bellman midpoint **slack** inequalities, and all action edges are distinct; hence the stress is PSD on precisely those clone subspaces. Thus the minimal facial profile is exactly s.

Finally add a fully observed (r-1)-dimensional positive definite support block and all cross coordinates, preserving all invariants. This proves sufficiency.

## Complexity

For h internal vertices, there are exactly (h!)² possible single parent policies. Enumerating ordered pairs (P,D) requires at most (h!)^4 rational cases, prior to collision and slack pruning. Each case uses a rational h-by-h linear solve, O(h²) arithmetic size checks, and O(h) source-reachability/peeling iterations. Clone multiplicities are chosen by integer compositions after the vertex-level peeling profile is computed. No real semidefinite solver, real quantifier elimination, or optimization over PSD recovery curves is involved.

This is an **exact finite two-colored directed graph classification** for an explicit nontrivial family, not an implicit restatement of a continuous recovery optimization.

## Significance, limitations and novelty

1. Single-action networks were refuted as universally sufficient by checkpoint 58 (first counterexample at target nullity 5). The two-policy model contains that example and all arbitrary finite multiaction incidence systems, by the proved compression of checkpoint 61.
2. The additional action can be Bellman-slack and hence irrelevant to the recovery exponent while essential to the exposing rank profile. The *two distinct policies* are therefore not redundant.
3. The missing direction for the user's full universal dense classification remains:
   \[
   \Sigma_s^{\rm arbitrary\ dense}\subseteq\mathcal B_s.
   \]
   Neither the weighted-flag extraction theorem (which preserves exponent but not degree) nor the rank-profile endpoint theorem proves this inclusion. No claim of full universality is made.
4. There is no assumption of rank-one source for an arbitrary dense instance: rank-one is a **realization** supplied by this certificate, not a reduction of a general kernel. 
5. Stochastic Bellman equations, min/max graph algorithms, PSD facial reduction and mediated sets are established methods; literature priority of this two-policy PSD construction/classification is not audited.