# Milestone 103 — COMPLETE arbitrary-dense sharp PSD exponent/depth classification at target nullity SIX

**Research result, 2026-11-08.** For every real linear PSD inverse problem with positive target rank and target nullity \(\nu=6\), the **entire attainable sharp Hölder exponent set at each exact minimal facial-reduction degree \(d\)** is classified by an explicit finite rational certificate, with a complete constructive realization for every retained fraction. The enumeration program in checkpoint 104 is fully self-contained, uses only standard-library Fraction arithmetic, and reports a reproducible SHA256 digest. It is a finite exhaustive computer-assisted proof (not a closed elementary fraction formula), based on previously proved universal dense necessity and explicit PSD sufficiency theorems. Independent specialist review of those prerequisites remains needed.

## Theorem and exact sizes

For any prescribed target rank r>=1 and nullity exactly \(\nu=6\), let \(\Sigma_{6,d}\) denote the sharp full-PSD Frobenius recovery exponents among arbitrary dense linear measurements with a UNIQUE rank-r feasible PSD target and **minimal singularity degree exactly \(d\)**. Then:
\[
\boxed{\Sigma_{6,1}=\{1,1/2\},}
\]
and for d=2,...,6 the finite sets \(\Sigma_{6,d}\) are precisely those computed by the rational certificate predicate below, with cardinalities:
\[
\boxed{
\begin{array}{c|ccccc}
d&2&3&4&5&6\\\hline
|\Sigma_{6,d}|&81&206&174&107&46 .
\end{array}}
\]
The Python certificate checkpoint104 prints every set and supplies a concrete rational harmonic policy with at most three additional globally distinct parent edges for EACH attained fraction. The sorted (degree,exponent) concatenation has SHA256
\[
\texttt{cfbdc113e81b88a59d5bf31eff111802eeea23ad82d467d2ca7176b194468151}.
\]

## Universal DENSE necessity: no graph representation hypothesis

By the genuine canonical maxdet monomial chart (checkpoint89) and the universal dense-to-harmonic exponent theorem (checkpoint91), every arbitrary dense uniquely recoverable PSD inverse problem admits **strict rational harmonic positive-grade weights**:
\[
0=w_0<w_1<\cdots<w_h<w_{h+1}=1,\quad 0\le h\le\nu-1=5,
\]
where each internal grade satisfies \(2w_i=w_{a_i}+w_{b_i}\) for some ordered distinct parents \(0\le a_i<i<b_i\le h+1\). Its sharp non-Lipschitz exponent is one of the half-weights \(\alpha=w_v/2\le w_1\). The actual minimal facial degree \(d\) is bounded by the independently proven **primal and dual original-kernel peeling recurrences** L(w) and U(w) (checkpoint99), and Sturm gives \(\alpha\ge2^{-d}\). Thus the following finite criterion is NECESSARY for every dense measurement map:
\[
\exists\,h\in\{1,\ldots,5\},\quad \exists\,\text{ordered rational midpoint parents},\quad
L(w)\le d\le U(w),\quad
2^{-d}\le\alpha=w_v/2\le w_1.
\tag{103.1}
\]
No assertion about the dense kernel being sparse or graph-representable is used to obtain (103.1).

There are exactly \((h!)^2\) ordered midpoint policies for h internal vertices. Checking each rational solution and the integer conditions in (103.1) is therefore exhaustive. Through h=5 the numbers of strictly increasing harmonic policies are exactly:
\[
h=1,2,3,4,5:\quad 1,\ 3,\ 18,\ 165,\ 2099.
\]
All candidate sets produced by h<=4 are included in those produced by h=5 (verified by exact enumeration). The h=5 candidate counts at each d are the five numbers in the theorem.

## Constructive SUFFICIENCY: exhaustive finite rational witnesses

For every strictly ordered harmonic policy P from (103.1), take the known weak-offdiagonal rank-one PSD incidence pencil, with a generator for each internal vertex i:
\[
H_i=E_{ii}-E_{00}+\lambda F_{a_i b_i}
\]
and (if \(\alpha<w_1\)) an independent \(G=\lambda F_{0v}\) for \(\alpha=w_v/2\). Each selected parent edge is globally distinct. These coefficients provide a sharp full-PSD recovery rate by the exact harmonic/Bellman inequality and matching diagonally dominant positive definite monomial curve (checkpoints57/74).

For every ordered policy, the exhaustive certificate also considers **every admissible choice of zero, one or two additional distinct parent edges**, each placed either:
- into a NEW independently controllable generator \(J_i=E_{ii}-E_{00}+\lambda F_{ab}\), provided its weighted parent average is at least w_i (Bellman-slack or tied); or
- as a SECOND edge tied into the existing generator \(H_i\), provided its weighted parent average is at most w_i (min–max-slack or tied).

Each augmentation preserves the original strictly increasing Bellman/Shapley value vector w; its exact minimal facial degree is computed by the **AND across modes / OR within a tied mode** PSD exposing closure theorem (checkpoint74). Every extra edge must be globally distinct from the existing edges and from the optional leading edge (0,v) whenever \(\alpha<w_1\); this latter collision test is essential and is included explicitly in the verifier.

The program examines EVERY pair of added edges, so this is an exact finite constructive exhaustion, not sampled search. It realizes **all** candidates of degrees 2,3,4 and 6. At degree 5, it realizes 106 of the 107 candidates, with the **sole remaining fraction \(13/64\)**.

The explicit rational \(\nu=6,d=5,\alpha=13/64\) construction in checkpoint102 has five base harmonic generators, THREE globally distinct additional Bellman-slack generators and the independent leading edge. Its exact strict weights are
\[
(w_1,\ldots,w_5)=(1/4,13/32,1/2,5/8,13/16)
\]
and its five maximal exposing layers are \(\{6\},\{5\},\{4\},\{2,3\},\{1\}\). Checkpoint102 proves full ambient recovery bounds, a matching PD curve and five explicit dual stresses. Adding this ONE certificate fills the last degree-five gap.

Thus EVERY candidate satisfying (103.1) is actually realized at the prescribed exponent and exact degree. If a certificate uses fewer than five internal vertices, fully measuring independent added null coordinates brings the target nullity up to exactly six, preserving exponent and minimal degree: the new coordinates expose with the first stress and all cross coordinates are measured. Fully measured positive target padding yields any prescribed r>=1.

Therefore the finite dense necessity and constructive sufficiency lists COINCIDE for every \(d=1,\ldots,6\), proving the theorem.

## Why this matters for the full universality problem

This completes ALL sharp exponent-by-degree spectra for arbitrary dense maps through **target nullity six**, extending the previous complete nullity-five result of checkpoint100. It also demonstrates that a **third independent Bellman-slack edge** can be necessary for an efficient realization of a *particular harmonic grade system and exposing schedule*, even though the general 2-mode compression theorem only bounds the number of retained modes **per vertex**, not the total number of vertices receiving secondary actions.

The important all-nullity conjecture remains:
> Every strict harmonic weight vector w produced by a dense canonical maxdet center permits a finite tied-edge or richer PSD incidence realization with every integer degree \(L(w)\le d\le U(w)\), without increasing the target nullity.

Our computer-assisted result verifies the relevant exponent-level claim through \(\nu=6\). It does NOT prove the general interval-sufficiency theorem at arbitrary \(\nu\), nor the stronger exact facial rank-profile classification. The rank-profile endpoint theorem and the universal Dikin–Hessian classifier remain valid independent results.

## Proof integrity

The enumeration uses exact rational Gaussian elimination, finite ordered parent sets, integer peeling calculations and finite subset enumeration; there is no numerical tolerance, random search or unsupported SDP feasibility assumption. Each graph certificate has an independent proven global PSD recovery and exposing-stress realization. The standalone checker at checkpoint104 independently reconstructs every certificate and validates the final catalogue sizes and SHA256 digest.

This is a finite computer-assisted theorem requiring the reader to inspect/run the companion script and independently audit the analytic prerequisites (especially checkpoints89/91/99). Bibliographic priority and publication novelty have not been externally verified.
