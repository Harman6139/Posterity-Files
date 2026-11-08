# Milestone 91 — canonical PSD recovery weights are ISOLATED vertices of a Plücker matroid fan; explicit integer denominator bound

**2026-11-08. PROVED for arbitrary dense real uniquely solvable PSD inverse problems, without harmonic-midpoint extraction, sparse representations, or real quantifier elimination.** This is a nontrivial arithmetic consequence of the universal strict primal–dual initial Grassmannian iff criterion in checkpoint 90. It supplies a finite explicit uniform denominator bound on every sharp Hölder exponent at fixed target nullity and kernel dimension, derived entirely from integer Plücker-weight tie equations.

## Main theorem

Let X*≽0 be uniquely recoverable by a real linear map L:S^n→R^m, with positive target rank r, nullity \(\nu=n-r\ge1\), and measurement kernel \(K=\ker L\) of dimension \(k\ge1\). Fix the **constant orthogonal basis Q** of the canonical monomial center normal form (checkpoint 89), so its null-space diagonal valuation weights are
\[
\theta=(\theta_1,\ldots,\theta_\nu)\in(0,1]^\nu.
\]
Let \(A\) be the N×k real coordinate matrix of \(Q^\top KQ\), N=n(n+1)/2, and let \(\eta_e(\theta)=(\theta_i+\theta_j)/2\) be the weight of symmetric coordinate e=(i,j), with support indices carrying weight zero.

For every nonzero k×k row minor \(p_I=\det A_I\), define its Plücker weight
\[
m_I(\theta)=\sum_{e\in I}\eta_e(\theta)
           =\tfrac12\sum_{a=1}^{\nu}c_{I,a}\theta_a,
\quad c_{I,a}\in\{0,\ldots,2k\}.
\]
Let \(\mathcal M\) be the set of bases I whose m_I(\theta) is maximum, and let \(F=\{a:\theta_a=1\}\).

### Theorem A — ISOLATED matroid normal-fan cell

The polyhedron of candidate weights \(\widetilde\theta\in(0,1]^\nu\) with:
1. the *same* set F of boundary coordinates equal to one;
2. the *same* maximizing Plücker bases \(\mathcal M\), i.e.
   \[
   m_I(\widetilde\theta)=m_J(\widetilde\theta)\ (I,J\in\mathcal M),
   \quad m_I(\widetilde\theta)>m_{I'}(\widetilde\theta)
   \ (I\in\mathcal M,I'\notin\mathcal M,\ p_{I'}\ne0);
   \]

consists of **exactly the single point \(\theta\)**. In other words, the canonical central weight vector lies at an **isolated vertex of the weighted Plücker-matroid normal fan intersected with the box (0,1]^\nu**.

This result is stronger than rational Puiseux existence: the numbers are forced by finitely many *integral tie equations between maximal-matroid-basis weights* plus weight-one boundary equations.

### Proof of Theorem A

The initial Grassmannian limit K0 is determined (checkpoint 90) by the **numerical** Plücker coefficients p_I for those indices in \(\mathcal M\), and by zeros for all other indices. Therefore changing \theta while preserving \mathcal M leaves K0 **exactly unchanged**, not just its dimension or signs. Likewise the affine base B0 from checkpoint 90 depends on \theta only through which null coordinates have θ_a=1, hence it is unchanged while F stays fixed.

For the actual canonical weight \theta, the universal positive-definite monomial normalization (checkpoint 89) and the initial Slater theorem (checkpoint 90) give two STRICT conic conditions:
\[
\exists H\in K_0:B_0+H\succ0,
\qquad
K_0^\perp\cap S_{++}^n\ne\varnothing.
\]
Because K0 and B0 do not change throughout the candidate cell, the SAME two conditions hold for every other point \widetilde\theta of that cell.

The if-and-only-if theorem in checkpoint 90 then implies that the FIXED unique central curve Cε would satisfy, simultaneously for two different weight vectors \theta and \widetilde\theta in the SAME constant orthogonal basis Q,
\[
D_\epsilon(\theta)^{-1}Q^\top C_\epsilon QD_\epsilon(\theta)^{-1}\to M\succ0,
\]
and
\[
D_\epsilon(\widetilde\theta)^{-1}Q^\top C_\epsilon Q
D_\epsilon(\widetilde\theta)^{-1}\to\widetilde M\succ0.
\]
Looking at each null-coordinate diagonal gives
\[
(C_\epsilon)_{aa}\sim M_{aa}\epsilon^{\theta_a}
           \sim\widetilde M_{aa}\epsilon^{\widetilde\theta_a}
\]
with both leading coefficients STRICTLY positive. Hence necessarily \theta_a=\widetilde\theta_a for every a. Thus the candidate cell contains no other point. It contains \theta itself, so is exactly {\theta}. QED.

### Theorem B — explicit elementary denominator bound

Every central null valuation weight is rational with a COMMON positive integer denominator \(D_\theta\) satisfying
\[
\boxed{D_\theta\le(2k\nu)^{\nu-1}.}
\tag{1}
\]
Consequently the sharp full-state PSD recovery exponent \alpha has reduced denominator at most
\[
\boxed{
\operatorname{den}(\alpha)\le2(2k\nu)^{\nu-1}.}
\tag{2}
\]
The bound is uniform over ALL arbitrary dense kernels of dimension k and target rank r, without any genericity assumption.

### Proof of Theorem B

Fix the exact maximizing-basis set \(\mathcal M\) and boundary set F at \theta. Every equality \(m_I=m_J\) is an INTEGER homogeneous linear equation in the ν null weights:
\[
\sum_{a=1}^\nu (c_{I,a}-c_{J,a})\theta_a=0,
\qquad |c_{I,a}-c_{J,a}|\le2k.
\tag{3}
\]
Every a∈F gives a boundary equation \theta_a=1, with unit coefficient row and integer right-hand side.

We claim these tie and boundary equations have full rank ν. Otherwise their homogeneous solution space has nonzero tangent v with v_a=0 on F and preserving all maximal-basis ties. Since all other basis inequalities are STRICT at \theta, and all unpinned null weights lie strictly between 0 and1, the vectors \theta±t v remain in the SAME maximizing Plücker-basis cell with the SAME set F for all sufficiently small t>0. This contradicts Theorem A. Therefore the integer equations contain a nonsingular ν×ν subsystem \(M\theta=b\), where each RHS entry of b is either 0 or1. There must be at least one boundary equation \theta_a=1: otherwise all tie equations are homogeneous and the positive vector \theta could be scaled slightly in both directions while remaining within (0,1), contradicting uniqueness.

Choose a nonsingular ν×ν subsystem containing a boundary unit row (possible because tie-only homogeneous equations cannot have full rank when they annihilate the nonzero vector \theta). Each remaining row has Euclidean norm at most 2k sqrt(ν) ≤2kν. By Hadamard's determinant bound,
\[
1\le|\det M|\le (2k\nu)^{\nu-1}.
\]
Cramer's rule gives \theta_a∈(1/\det M)\mathbb Z for every a, so all null weights have a COMMON integer denominator \(|\det M|\) satisfying (1).

By the universal weighted-support Dikin rank formula (checkpoints 86 and 89),
\[
\alpha=\min\{1,\;(\theta_i+\theta_j)/2
        \text{ for some symmetric coordinate }(i,j)\}.
\]
Every such half-sum has denominator dividing \(2|\det M|\). This proves (2). QED.

## Consequences

1. **Finite rational candidate set without QE.** At fixed positive nullity ν and kernel dimension k, one can enumerate ALL possible sharp exponents from rationals with denominator at most \(2(2k\nu)^{\nu-1}\) in the universal range (0,1], then test realizability at any prescribed degree by the finite semialgebraic compatibility predicate of checkpoint 14. This gives a simple explicit bound replacing the much less transparent QE-degree bound of checkpoint 16. It does not claim practical efficiency.
2. **A stronger finite MATROID-flag algorithm for a fixed orthogonal Q.** Enumerate maximizing-basis patterns \mathcal M and boundary sets F; solve their rational tie equations, retain isolated candidates satisfying 0<θ_a≤1; construct the initial Plücker space K0 by (3) of checkpoint 90; and perform the two strict primal/dual PD feasibility tests. Exactly ONE weight vector succeeds, namely the canonical central weights in that Q basis, whenever Q is adapted to the central monomial flag. No Puiseux series need be explicitly solved.
3. **A universal rank/basis geometry behind midpoint equations.** In the special tied-edge incidence family the maximal-weight Plücker ties reduce to ordinary midpoint equations \(2w_i=w_a+w_b\). For arbitrary dense kernels they can involve **sums of up to k pair-weights** and signed/numerical Plücker coefficients. Thus tied-edge games are a particular combinatorially simple face of a more general *oriented weighted linear-matroid* phenomenon.
4. **What remains open:** Q itself varies over continuous orthogonal flags, and the minimal exposing rank profile still requires its separate PSD face-compression tower. Neither of these difficulties is resolved by the fixed-Q arithmetic bound. This theorem does NOT prove arbitrary dense-to-tied-game equality at the same nullity/profile, nor the full closed arithmetic spectrum for all \nu,d.

## Example: the 3×3 quarter-power kernel

Take K=span(−E00+E11+F02, F01) and θ=(1/2,1) on null coordinates 1,2. The maximum Plücker bases involve one F01 coordinate of weight θ1/2, and one of E11 or F02, whose weights are θ1 and θ2/2. Their required tie equality
\[
\theta_1=\theta_2/2
\]
combined with the terminal boundary pin \theta_2=1 gives the unique vertex θ=(1/2,1). The associated initial Plücker space passes both strict conic Slater tests (checkpoint 90). The Dikin weighted-support rank threshold is θ1/2=1/4.

## Novelty, interpretation and audit

Grassmannian weight degenerations, Plücker bases, rational polyhedral normal fans and Hadamard bounds are classical. The new observation is the PSD center's **strict primal–dual feasibility forces complete isolation of its actual monomial weight in the Plücker fan**, yielding an explicit universal exponent denominator bound without QE. The proof is self-contained modulo the immediately preceding universal center/initial-Grassmannian theorems, whose full proofs are committed in checkpoints 89–90. Bibliographic priority of the combined stability statement has not been checked.
