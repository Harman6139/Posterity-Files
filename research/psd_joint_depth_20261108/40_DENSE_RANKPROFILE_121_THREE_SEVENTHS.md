# Milestone 40 — universal sharp 3/7 bound for dense facial rank profile (1,2,1)

**2026-11-08. PROVED independently of the dense weighted-flag extraction, arbitrary real measurement map, arbitrary positive target rank.** This is the last open rank profile at nullity four and singularity degree three.

## Theorem

Let X*≽0 be uniquely recoverable by L:S^n→R^m, with rank(X*)>=1, target nullity ν=4 and **canonical maximal-rank facial-reduction chain** of minimal degree 3 and rank drops (1,2,1). Then an actual positive-definite perturbation curve has
\[
\|X(t)-X_*\|_F=\Theta(t^3),\qquad
\|\mathcal L(X(t)-X_*)\|_2=\Theta(t^7).
\]
Therefore
\[
\boxed{\alpha(\mathcal L,X_*)\le3/7}.
\]
This is **sharp**: the source/root/core midpoint graph with weights (3/7,5/7,6/7,1) is a uniquely solvable PSD problem with exact rank-drop profile (1,2,1) and full-state exponent 3/7.

## Proof: two independent homogeneous semidefinite alternatives

Choose coordinates R^n=U⊕D⊕T⊕F, where U=range X*, D=span(e1) is the deepest null direction, T=span(e2,e3) is the two-dimensional second-exposed block, and F=span(e4) is the first-exposed block. Put K=ker L. The first exposing stress is a positive multiple of E44 in K⊥; therefore **H44=0 for every H∈K**. The canonical second compressed stress is PSD, positive definite on T, and zero on U⊕D. The final stress is positive on D after the first two exposures. Put W1=U⊕D⊕T and K1=K∩S(W1).

### Lemma 1: there exists A∈K1 with positive D diagonal and zero T null interactions

Let Q1={P_(D⊕T)H P_(D⊕T):H∈K1}. The second compressed stress, positive definite on T, belongs to Q1⊥. If Q1∩S(D⊕T)_+={0}, Gordan–Stiemke separation yields a **positive-definite** element of Q1⊥. By the compression-annihilator identity this lifts to a second exposing stress positive on D⊕T, reducing the facial degree to at most two, contradiction. Hence some A∈K1 has nonzero PSD bottom compression. Its pairing with the second stress is zero, so complementarity forces that compression to be supported on D. Because D is one-dimensional, A11=a>0 and A22=A33=A12=A13=A23=0. Support-to-T entries (from U to T) need NOT vanish; they are allowed below.

### Lemma 2: a second-order positive middle direction whose first-face rows are zero

Let R=T⊕F and Q={P_R H P_R:H∈K}. E44 belongs to Q⊥∩PSD and is positive on F. If Q∩S(R)_+={0}, Gordan–Stiemke gives a PD stress on all R; extending it by zero on U⊕D would expose T⊕F in one first step, after which the final D-compressed stress exposes D in one more step. This would give d<=2, contradiction. Therefore choose B∈K with C=P_R B P_R≽0 nonzero. Since H44=0 for all H∈K, C44=0 and PSD implies C_TF=0. Thus C is a nonzero PSD matrix on T. Let s=rank C∈{1,2}.

### Lemma 3 (only needed for s=1): a clean final middle direction

If s=1, choose an orthonormal basis e2,e3 for T in which C=b E22 with b>0. Since H44=0 for every H∈K, consider functionals f(H)=H33 and g(H)=H34 on K. If f=cg for some real c, then
    Z=E33-(c/2)F34+M E44
for M>c²/4 is globally PSD, lies in K⊥ and exposes at least e3,e4 in the *first* step. This contradicts maximal first stress rank s1=1. Hence f is not a multiple of g, so some Cmat∈K obeys
    (Cmat)33>0, (Cmat)34=0, (Cmat)44=0.
No other matrix blocks are assumed absent.

## Full PSD perturbations: exact support-order audit

Apply the elementary coefficient-rescaling lemma from the prior project, whose proof is independent of dense weighted-flag extraction. For weights assigned to orthogonal blocks, every coefficient t^e must have zero (i,j)-block whenever wi+wj>2e; if the first diagonal coefficient on every null block is strictly positive, multiplying each coefficient by fixed exp(σ e²) makes the entire generalized polynomial positive definite for small t>0.

**Case s=2.** Assign weights 0 to U, 3 to D, 5 to the entire T, 7 to F. Form
    X*+ t³A+t⁵B+t⁷ P_F.
The actual A is supported on U⊕D⊕T and has null compression only aE11: its possible U–T blocks have weight 5≤2·3=6; every other allowed block has sum≤6. The actual B has T compression PD, vanishing T–F and F–F blocks; its possible D–F blocks have sum 3+7=10=2·5, and all others have sum≤10. The terminal P_F supplies positive F diagonal. Thus after coefficient rescaling this is PD, with first displacement t³ and residual t⁷.

**Case s=1.** Assign weights 0 on U, 3 on D, 5 on e2, 6 on e3, and 7 on F. Form
    X*+t³ A+t⁵ B+t⁶ Cmat+t⁷ P_F.
A has only D diagonal among null blocks, with arbitrary U–T cross entries of weights at most 6=2·3; it has no F blocks. B has positive e2 diagonal, zero e3 diagonal and e2–e3 cross (because its PSD T compression has rank one), zero T–F cross, and zero F diagonal. Its other possible blocks have sum at most 10=2·5; crucially D–F has sum3+7=10. Cmat has positive e3 diagonal, zero e3–F cross and F diagonal; its other blocks have sum at most 12=2·6, with e2–F sum5+7=12. The terminal P_F has positive F diagonal. Hence rescaling gives a PD matrix curve.

In both cases, all coefficients below order seven lie in K, and P_F∉K since K∩PSD={0}. Thus residual is exactly Θ(t⁷), while A≠0 makes displacement Θ(t³). Hence α≤3/7. QED.

## Exact sharp sparse example

Take X*=E00 on S^5, and a sparse midpoint pencil with internal coordinates of weights 3/7,5/7,6/7, terminal 1, and parent relations
  2(3/7)=0+6/7,
  2(5/7)=3/7+1,
  2(6/7)=5/7+1.
Use small rational offdiagonal coefficient λ on each parent edge; measure trace, terminal diagonal and orthogonal projection off the pencil range. The full ambient recovery exponent is 3/7 by the exact harmonic inequality and normalized positive-definite sharp curve. The greedy facial-reduction layers are {terminal}, {two core vertices}, {root}, so rank profile (1,2,1). The upper bound 3/7 is therefore sharp.

## Audited limitations

This theorem is **directly universal for all dense kernels at this fixed rank profile**, and uses no midpoint necessity assumptions in the upper-bound proof. It does not claim that every target nullity/degree has such a simple bound. The two other nullity-four depth-three profiles (2,1,1) and (1,1,2) are covered by checkpoints 38 and 39. Together these prove the sharp universal upper endpoint α≤3/7 at ν=4,d=3, excluding the square-root endpoint unconditionally. The complete arithmetic spectrum ν=4,d=3 still uses the earlier full weighted-flag/midpoint theorem for exhaustiveness.

## Novelty discipline

The Gordan–Stiemke alternative and coefficient-rescaling trick are standard ingredients. Whether the particular universal rank-profile sharpness result is unpublished is not independently established.