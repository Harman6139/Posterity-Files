# Milestone 38 — a universal cubic obstruction for dense facial rank profile (2,1,1)

**Date: 2026-11-08. PROVED without the weighted-flag universality theorem.** This is an independent theorem applying to every dense real PSD measurement kernel. It establishes the strict square-root exclusion and a sharper exponent bound for one of the three possible rank profiles at target nullity four and depth three.

## Theorem

Let L:S^n→R^m be a linear map, let X*≽0 be its unique PSD preimage, and assume target rank r>=1 and nullity ν=4. Suppose the **canonical maximal-rank facial reduction chain** has exactly three strict steps of rank drops (s1,s2,s3)=(2,1,1). Then there exists a real symmetric polynomial PSD curve
    X(t)=X*+t A + M t² B + C t³ P_F
for fixed M,C>0, such that A,B∈K=ker L, A≠0, F is the first exposed two-dimensional null subspace, and
    ||X(t)-X*||_F=Θ(t),  ||L(X(t)-X*)||_2=Θ(t³).
Consequently the optimal recovery exponent satisfies
    **α≤1/3**.
In particular α=1/2 is impossible for this rank profile.

## Fully rigorous proof

Fix coordinates R^n=U⊕span{e1,e2}⊕F, where U=range X*, dim F=2. The canonical first stress Z1∈K⊥ is PSD, supported on F, and **positive definite on F**. The reduced face after step 1 is W1=U⊕span{e1,e2}. The second stress compresses to a positive multiple of E22 on W1; the last step exposes e1. Put K1=K∩S(W1), the subspace of kernel matrices supported on W1.

**Lemma 1 — a deep first-order direction.** Every H∈K1 obeys H22=0, since it pairs to zero with the second stress. On K1 let f(H)=H11 and g(H)=H12. If f=c g for some real c (including f≡0), then
    T=E11-(c/2)F12+M E22
for M>c²/4 is positive definite on span(e1,e2), annihilates U, and pairs to zero with K1. The identity
    (K∩S(W1))^⊥ inside S(W1) = P_W1 K^⊥ P_W1
lifts T to a valid second exposing stress in K⊥. That would eliminate e1 and e2 simultaneously, yielding facial degree at most 2 — contradiction. Hence f is not a scalar multiple of g, so some A∈K1 has A12=0 and A11>0 (reverse sign if required). It also has A22=0. All first-order null blocks involving F vanish, since A is supported on W1.

**Lemma 2 — a second-order direction without forbidden first-face blocks.** Set R=span(e2)⊕F and Q={P_R H P_R:H∈K}, a linear subspace of S(R). The first stress Z1, restricted to R, lies in Q⊥∩PSD and is positive definite on F. If Q∩PSD={0}, the strict semidefinite Gordan–Stiemke alternative gives a positive-definite Z∈Q⊥ on all of R. Extend Z by zero on U⊕e1. It is then a globally PSD stress in K⊥, exposing R at the *first* step. The residual face is U⊕e1; uniqueness implies one further exposing step suffices, so the original facial degree would be ≤2, contradiction. Thus Q∩PSD contains a nonzero B_R. Because B_R pairs to zero with Z1>0 on F, PSD complementarity forces its entire F rows/columns to vanish. Hence B_R=b E22 for b>0. By the definition of Q, choose B∈K whose R-compression is b E22. In particular
    B22=b>0, P_F B P_F=0, and P_F B e2=0.
This is an *exact* kernel condition, not an approximate or numerical one.

**Full PSD curve.** Assign support weights 0,1,2,3 to U,e1,e2,F respectively. The coefficient A at exponent 1 is supported on U⊕e1⊕e2 and satisfies A22=A12=0; therefore its every nonzero block has sum of endpoint weights at most 2. The coefficient B at exponent 2 obeys P_F B P_F=0 and P_F B e2=0, and hence every nonzero block has sum of endpoint weights at most 4. The final coefficient P_F at exponent 3 has positive-definite F compression. The diagonal leading coefficients on e1,e2,F are respectively A11>0, B22>0, I_F>0.

Apply the elementary coefficient-rescaling lemma: given a finite matrix polynomial whose coefficient at exponent e has no (i,j)-block with wi+wj>2e and whose leading diagonals at weights 1,2,3 are positive definite, multiplying the coefficient at each exponent e by a sufficiently large fixed factor exp(σe²) makes the whole polynomial positive definite for all sufficiently small t>0. Its proof is direct: diagonal congruence by exp(σwi²/2)t^(wi/2) produces positive limiting diagonal blocks and offdiagonals of size exp(-σ(wi-wj)²/4), which vanish as σ→∞. Thus for fixed sufficiently large σ the curve
    X(t)=X*+e^σ t A+e^(4σ)t² B+e^(9σ)t³P_F
is PSD, indeed PD, for every sufficiently small t>0.

Both A and B belong to K, while P_F∉K because P_F≽0 and uniqueness implies K∩PSD={0}. So the residual is exactly e^(9σ)t³||L P_F||=Θ(t³). The first-order coefficient A≠0 gives displacement Θ(t). Hence α≤1/3. QED.

## Scope and limitations

This theorem does **not** require the sharp-arc weighted-flag extraction or sparse midpoint combinatorics. It is a direct universal dense-map construction from two facial reductions and a Gordan–Stiemke alternative. It eliminates the square-root endpoint at nullity 4, degree 3, **rank profile (2,1,1)** only.

The other possible rank-drop profiles at (ν,d)=(4,3) are (1,2,1) and (1,1,2). In particular, this theorem does not justify excluding α=1/2 for all depth-three PSD systems, and does not complete the universal closed combinatorial classification.

## Novelty note

Facial reduction, the homogeneous Gordan–Stiemke alternative, and simple block-coefficient scaling are existing mathematical methods; the particular cubic incompatibility statement is proved here, but its bibliographic priority has not been established.