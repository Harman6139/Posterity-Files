# Milestone 55 — complete finite combinatorial realization rule at each prescribed PSD facial rank profile

Date: 2026-11-08. **PROVED as a necessary-and-sufficient theorem for the vertex-blown-up sparse midpoint family and a universally valid SUFFICIENCY theorem for arbitrary PSD recovery.** A universal DENSE necessity theorem for this rule is **not claimed**. This is the precise remaining universality conjecture.

## Finite combinatorial data

Fix a positive rank-drop profile s=(s1,...,sd), d>=1 and ν=sum s_j. Enumerate all strictly ordered harmonic midpoint graphs G with source 0 of weight 0, h internal vertices of distinct rational weights 0<w1<...<wh<1 and one terminal of weight 1, where 0<=h<=ν-1. Every internal vertex i chooses distinct parents a(i)<i<b(i) in {0,...,h+1} and solves 2w_i=w_a+w_b.

The exact *greedy peeling layers* C_1,...,C_(d_G) are computed by the finite rule: among remaining non-source vertices, remove in one step the largest set C such that, whenever an internal i∈C has both parents still remaining, both parents lie in C. The sparse facial-peeling theorem proves that this is the minimum facial degree and each layer is the maximal exposed support of one PSD stress.

For each vertex v of positive weight (including terminal), put alpha=w_v/2 and retain it when alpha <= min_i w_i (or alpha=1/2 when h=0). Let
\[
\mathcal R_s=\{\alpha\in\mathbb Q\cap(0,1/2]:
  \exists G\text{ with }d_G=d,\
  |C_j|\le s_j\ (1\le j\le d),\
  \alpha=w_v/2\le\min_i w_i\text{ for some }v\}.
\]

## Theorem — exact realizability of every combinatorial certificate

For EVERY target rank r>=1, every alpha∈R_s is the exact full-matrix recovery exponent of an explicitly constructible uniquely solvable PSD inverse problem on S^(r+ν), with **canonical maximal exposing rank profile exactly s**. Conversely, every PSD inverse problem in the *blown-up strict harmonic incidence family* of checkpoint 52, with profile s, has exponent in R_s. Thus R_s is the **complete exact spectrum of that natural construction family** and a certified lower inclusion
\[
\boxed{\mathcal R_s\subseteq\Sigma_s^{\rm arbitrary\ dense}}.
\]

**Proof.** If a graph G has peeling layer cardinalities c_j≤s_j, choose positive vertex multiplicities κ_v with Σ_(v∈C_j)κ_v=s_j. This is possible by distributing the s_j-c_j extra units among vertices of C_j. The vertex blow-up theorem in checkpoint 52 proves that the resulting real PSD pencil has exactly the same exponent, exactly d greedy exposing stages and rank drops Σκ_v=s_j. Its upper bound controls all ambient PSD competitors, and its matching monomial arc is strictly PD after diagonal normalization; positive target padding gives any r.

Conversely, collapsing clone coordinates in any member of the defined blown-up family recovers its underlying strict harmonic graph. By the exact peeling theorem, its profile is the sums of clone multiplicities in the corresponding peeling layers, and its exponent is one of the above leading half-weights. Thus its exponent belongs to R_s. QED.

## Finiteness and exact implementation

At fixed h the parent choices are ∏_(i=1)^h i(h+1-i)=(h!)². For each parent assignment, solve the finite integer harmonic system by exact rational elimination, retain strictly ordered weights, calculate greedy peeling, and test the simple layer-size inequalities. Thus the entire R_s is computable using **only rational arithmetic and finite graph search**, with no SDP solver, continuous parameter search or real quantifier elimination. The companion script checkpoint 56 implements the enumeration.

The algorithm stops after h=ν-1. This bound is optimal for the family (there are h internal positive-weight directions and one terminal). Output graph and multiplicities are explicit correctness certificates, including the full measurement pencil.

## Tested comparison to arbitrary dense classifications

The independent exact catalogue through ν=4 yields:
- ν=3, d1: {1/2}; d2: {1/4,3/8,1/2}; d3: {1/8,1/6,1/4,1/3}.
- ν=4, d1: {1/2}; d2: {1/4,5/16,1/3,3/8,5/12,7/16,1/2}; d3: {1/8,1/6,3/16,1/5,3/14,1/4,3/10,1/3,5/14,3/8,2/5,3/7}; d4: {1/16,1/14,1/12,1/10,1/8,1/7,1/6,1/5,1/4}.
These agree, after adding the independently realizable Lipschitz exponent 1 at d1, with the **previously claimed** complete dense spectra in checkpoints 20 and 41. This agreement is evidence and a consistency check, not a proof at ν>=5.

The degree-two profile-specific theorem in checkpoint 47 likewise agrees with R_s for every checked s through ν=6. At ν=5 the union over profiles produces 23,49,32,20 possible non-Lipschitz exponents for degrees d2,d3,d4,d5 respectively. At ν=6 the corresponding counts are 81,190,161,80,43 for degrees d2,...,d6. Every listed value has a graph and exact PSD realization.

## Frontier question stated sharply

**Conjecture:** For all ν, all positive rank-drop profiles s and all rational α,
\[
\Sigma_s^{\rm arbitrary\ dense}=\{1\text{ when }d=1\}\cup\mathcal R_s.
\]
The inclusion R_s⊂Σ_s is PROVED. The reverse inclusion, involving arbitrary dense kernels and all higher degrees, is NOT proved. It is exactly the sought-after depth-preserving universality of sparse midpoint networks at the level of attainable (alpha,rank-profile) triples, *not* necessarily an equivalence of individual measurement systems.

A proof would give a complete finite combinatorial spectrum classification and exact optimal dimensions for prescribed exponent/depth via minimizing Σs_j over the finite graph witnesses; a counterexample would identify a genuinely new dense singularity mechanism beyond midpoint peeling.

## Audit

This certificate rule is non-tautological: all inputs are finite integer parent choices, exact rational weights and finite closure/peeling operations. The sufficiency proof is against all PSD competitors and has an explicit matching curve. No universality of arbitrary dense recovery is presumed, and no numerical experiments substitute for the proof. Previous standard mediated-set theory is acknowledged as prior art.