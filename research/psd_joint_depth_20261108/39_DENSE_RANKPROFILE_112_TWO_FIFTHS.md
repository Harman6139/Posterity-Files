# Milestone 39 — a universal 2/5 obstruction for dense rank profile (1,1,2)

**2026-11-08. PROVED WITHOUT the weighted-flag theorem or sparse reduction.** Rank-one or rank-two tangent alternatives and canonical maximal-rank dual stresses yield a complete, explicit, full PSD perturbation with displacement t² and residual t⁵.

## Theorem

Let a real linear PSD inverse problem have a uniquely recoverable positive-rank target X*, nullity ν=4, and canonical maximal-rank facial-reduction chain of exact degree 3 with rank drops (s1,s2,s3)=(1,1,2). Then
\[
\boxed{\alpha(\mathcal L,X_*)\le2/5.}
\]
In particular α=1/2 is impossible for this rank profile. The bound is attained by an explicit sparse incidence pencil: coordinates 0 (source), 1,2 (deep), 3 (second exposed), 4 (first exposed), with kernel generators
 A=E11+F03, H=E22+F13, B=E33+F24,
and a measured terminal X44. Its midpoint weights are (2/5,3/5,4/5,1); its full-state exponent is 2/5 and greedy exposing rank profile is (1,1,2).

## Proof

Let U=range X*. Choose coordinates U⊕D⊕T⊕F with D=span(e1,e2), T=span(e3), F=span(e4), so that the first exposing stress Z1 is a positive multiple of E44, the second compressed stress on W1=U⊕D⊕T is E33, and the last stress compressed to W2=U⊕D is strictly positive on D. Write K=ker L and K1=K∩S(W1).

### Step 1: a positive semidefinite deep null-compression in K1

Let Q1={P_(D⊕T) H P_(D⊕T): H∈K1}⊂S(D⊕T). Since the canonical second stress is PSD and supported on T, E33∈Q1^⊥. If Q1∩S(D⊕T)_+={0}, Gordan–Stiemke gives a strictly positive definite dual in Q1^⊥. Its lift to an ambient stress in K^⊥ would expose all D⊕T after the first face reduction, giving minimal degree ≤2, contradiction. Thus there exists A∈K1 with C=P_(D⊕T)A P_(D⊕T) PSD and nonzero.

As E33∈Q1^⊥, PSD complementarity forces the T row and column of C to vanish. Thus C is nonzero PSD on D. Let s=rank C∈{1,2}. If s=1, choose orthonormal basis e1,e2 of D such that C=aE11 with a>0; if s=2, C is positive definite on D. In either case A is supported on W1, has no null–null interaction involving T, and may have arbitrary support-to-D or support-to-T blocks.

### Step 2: a clean middle/first-face kernel mode

Put R=T⊕F and Q={P_R H P_R:H∈K}. The first exposing stress Z1 is PSD, lies in Q^⊥ and is positive on F. If Q∩S(R)_+={0}, Gordan–Stiemke gives a positive definite Z in Q^⊥, extended by zero on U⊕D. This would be a globally PSD first exposing stress removing T and F simultaneously, after which the original last compressed stress exposes all of D, reducing the degree to at most two. Contradiction. Therefore Q∩PSD contains nonzero B_R; complementarity with Z1 forces B_R=bE33 (b>0). Choose B∈K lifting it. Thus
    B33=b>0, B34=0, B44=0.
No condition is imposed on its other dense entries.

### Step 3 (only when s=1): a clean additional deep mode

In the chosen basis A_D=aE11 and A_D,T=0. Every H∈K1 has H33=0 because it pairs with the compressed second stress. Consider f(H)=H22 and g(H)=H23. If f=cg on K1, then the matrix
    Z=E22-(c/2)F23+M E33, M>c²/4,
is PSD on W1, positive definite on T⊕e2, annihilates U and pairs with every H∈K1. It therefore lifts to a valid second exposing stress of rank at least two. This contradicts the stipulated **canonical maximal** second rank drop s2=1. Hence f is not a multiple of g, so there is H∈K1 with H22>0 and H23=0, after reversing its sign. Its H33=0 and all its F rows vanish because H is supported on W1. H may have arbitrary entries in U⊕D and between e1 and T.

### Step 4: a full positive-definite polynomial perturbation

Use the PSD coefficient-rescaling lemma, independently proved by diagonal congruence: if every coefficient at exponent e has zero blocks with wi+wj>2e, and the first coefficient on each positive diagonal block Ui occurs at its assigned weight wi and is positive definite, multiplying the coefficient at exponent e by exp(σe²) for sufficiently large σ makes the polynomial PD for small t>0.

If s=1, assign weights 0 on U, 2 on e1, 3 on e2, 4 on T, 5 on F. Use coefficients
    t²A +t³H+t⁴ B+t⁵P_F.
Check *every possible dense block*:
- A is supported on U⊕D⊕T; its D⊕T compression has only aE11, hence the null–null blocks involving e2 or T vanish. Its possible support-to-T block has weight 4=2·2, and all its other possible blocks have weight sum ≤4.
- H lies in K1, so has no F blocks. H33=H23=0; its largest potentially nonzero null block is e1–T of weight 2+4=6=2·3. All other blocks have sum ≤6.
- B has B33=b>0, B34=B44=0. Its remaining possible blocks have weight sum ≤8=2·4: e2–F has sum 3+5=8, e1–F has sum 7, and e2–T sum 7.
- P_F at order 5 supplies positive F diagonal.
Leading diagonals at weights (2,3,4,5) are respectively a,b_H,b,I_F, all strictly positive.

If s=2, assign weight 2 to the entire two-dimensional D, weight 4 to T, weight 5 to F. Use
    t² A +t⁴ B+t⁵P_F.
A has PD D compression and vanishing D–T,T–T null blocks; its support-to-T blocks have weight 4=2·2. B has positive T diagonal and vanishing T–F,F–F blocks; its D–F blocks have weight 2+5=7≤8=2·4. The same rescaling lemma gives PD.

In both cases all coefficients before exponent five lie in K, while P_F≽0 is not in K by uniqueness. Thus the perturbed PSD matrix has measurement residual Θ(t⁵). The first nonzero coefficient A occurs at t² and is nonzero, so displacement Θ(t²). Hence \(\alpha\le2/5\), proving the theorem. QED.

## Exact sharp example and verification

For the rank-one example n=5:
    X*=E00,
    A=E11+F03,
    H=E22+F13,
    B=E33+F24,
    K=span{A,H,B}.
The trace-controlled measurement can be taken as Frobenius orthogonal projection to K^⊥ (positive definite trace control follows from uniqueness). The sparse harmonic equations
    2w1=w0+w3, 2w2=w1+w3, 2w3=w2+w4
give (w1,w2,w3,w4)=(2/5,3/5,4/5,1), so the full-state exponent is 2/5. The maximal greedy first stress is E44, second compressed stress E33, third compressed stress PD on e1,e2. Thus facial rank profile (1,1,2), attaining the bound.

## Scope

This is a standalone **arbitrary dense** theorem for one prescribed rank profile. With checkpoint 38 for (2,1,1), only the rank profile (1,2,1) remains to resolve the square-root endpoint at nullity ν=4, degree d=3. These rank profiles exhaust all partitions of four into three positive rank drops. No conclusion for arbitrary ν,d is claimed here.

## Prior art

The standard Gordan–Stiemke cone alternative and facial reduction are classical. The explicit exponent–rank-profile obstruction is established by the proof here, but its literature priority is not verified.