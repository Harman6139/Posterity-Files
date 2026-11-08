# Milestone 42 — universal SHARP dense bound for any three-step profile (f,s,1)

**2026-11-08. PROVED with no weighted-flag extraction or sparse-representation assumption.** This is a dimension-uniform structural theorem, superseding the specific (2,1,1) and (1,2,1) results in checkpoints 38 and 40. It uses a constructive sequence of finitely many homogeneous Gordan–Stiemke alternatives and the elementary full-PSD coefficient-rescaling lemma.

## Theorem

Let L:S^n→R^m be any real linear measurement map with a uniquely recoverable PSD target X* of rank r>=1. Suppose the **canonical maximal-rank facial-reduction chain** has minimal length d=3 and consecutive rank drops
    (s1,s2,s3)=(f,s,1),  f>=1,s>=1.
Then the exact optimal full-state recovery exponent satisfies
\[
\boxed{
\alpha(L,X_*)\le\frac{2^s-1}{2^{s+1}-1}<\frac12.}
\]
This upper bound is **sharp for every pair (f,s)**, attained by a finite rank-one sparse PSD pencil with s core vertices, one root, one terminal, and (f-1) additionally fully observed zero directions; its exposing rank profile is (f,s,1). Thus no square-root-stable dense PSD inverse problem can have a three-step chain with one-dimensional final exposed block.

The proof does not depend on target rank, the number of measurements, or a prior sharp exponent catalogue.

## Proof

Choose orthogonal coordinates
    R^n=U ⊕ D ⊕ T ⊕ F,
where U=range X*, dim D=1, dim T=s, dim F=f. The first exposing stress Z1∈K⊥ is PSD, **positive definite on F**, and zero on U⊕D⊕T. The second exposing stress compressed to W1=U⊕D⊕T is PSD and **positive definite on T**, annihilating U⊕D. The third exposes D. Let K=ker L, K1=K∩S(W1).

### A. Force a deep kernel mode supported in W1

Let Q1={P_(D⊕T) H P_(D⊕T):H∈K1}. The second stress's compression lies in Q1⊥ and is PD on T. If Q1∩PSD={0}, the strict semidefinite Gordan–Stiemke alternative yields a PD element of Q1⊥ on D⊕T, lifting to a second exposing stress that removes D and T together. Then facial degree ≤2, contradiction. Hence some A∈K1 has nonzero PSD compression C on D⊕T. PSD complementarity with a second stress PD on T forces C supported entirely on D, whose dimension is one. Thus A_DD=a>0 and A_DT=A_TT=0. A may have arbitrary U-to-D, U-to-T and U-to-U blocks, but has no F entries because it lies in K1.

### B. Force a complete *flag* of positive middle kernel modes

Initialize T_remaining=T. Repeat:
- Define R_j=T_remaining⊕F and Q_j={P_Rj H P_Rj:H∈K}.
- The first stress Z1, compressed to R_j, is in Q_j⊥∩PSD and is PD on F.
- If Q_j∩PSD={0}, strict Gordan–Stiemke supplies a positive definite element of Q_j⊥ on R_j. Extend it by zero on U⊕D⊕(T⊖T_remaining). It is a globally PSD measurement stress in K⊥, with rank dim R_j>f, contradicting the **maximal first exposing rank f**.
- Therefore choose B_j∈K with nonzero PSD R_j-compression C_j. Complementarity with Z1 PD on F forces C_j supported on T_remaining. Let V_j=range C_j, a nonzero subspace of T_remaining; C_j is PD on V_j and identically zero on the complement V_{j+1}⊕... of V_j within T_remaining.

Set T_remaining=T_remaining⊖V_j and continue until it vanishes. This yields an orthogonal decomposition
    T=V_1⊕...⊕V_k,   1<=k<=s,
with strictly positive leading diagonal blocks B_j|V_j, and the exact support restrictions:
- B_j has zero F×F block;
- B_j has zero (V_l,F) blocks for l>=j;
- B_j has zero (V_l,V_m) blocks whenever l,m>=j and at least one index >j;
- B_j may have arbitrary entries involving U, D, or earlier V_i, including earlier V_i to F and earlier-to-later V_i couplings.
These restrictions hold without any coordinate sparsity of the original kernel.

### C. Assign a feasible rational weight system

For a fixed k, put
\[
a=\frac{2^k-1}{2^{k+1}-1},\qquad
b_j=1-2^{-j}(1-a)\quad(j=1,\ldots,k).
\]
Then
    0<a<b1<...<bk<1,
    2b1=a+1,
    2b_j=b_(j-1)+1 for j>=2,
    bk=2a.
Assign weights 0 on U, a on D, b_j on V_j, and 1 on F.

Consider the generalized polynomial
\[
Y(t)=X_*+t^a A+\sum_{j=1}^k t^{b_j}B_j+t P_F.
\]

Check every possible dense block:

**A at order a.** It is supported on U⊕D⊕T, has null compression supported on D, and hence any nonzero offdiagonal block is U-to-D or U-to-V_j. The largest weight of such a block is bk=2a. No A block exceeds pair-weight 2a.

**B_j at order b_j.** Its F×F block is zero. Within T_remaining=V_j⊕...⊕V_k, its only nonzero block is V_j×V_j. All other potentially nonzero entries involve U,D, or an **earlier** V_i with i<j. The worst possible pair-weight among these is
    max{a+1, b_(j-1)+1, a+bk, b_(j-1)+bk}
(with the terms indexed j-1 omitted when j=1), or 2b_j from V_j×V_j. The recurrence and bk<=1 give
    a+1=2b1<=2b_j,
    b_(j-1)+1=2b_j for j>=2,
    a+bk<=a+1<=2b_j,
    b_(j-1)+bk<=b_(j-1)+1=2b_j.
Thus every potentially nonzero B_j block satisfies its pair-weight bound 2b_j, including arbitrary dense support-to-null couplings and interactions with previously peeled T directions.

**Terminal coefficient.** P_F is PSD, strictly positive on F at order one. Since all preceding null diagonals are positive definite at their assigned orders, the coefficient-rescaling lemma applies: multiplying the coefficient of each exponent e by exp(σe²), for sufficiently large fixed σ, makes the entire Y_sigma(t) positive definite for small t>0. This is a full PSD assertion (all minors) proved by diagonal congruence, not an inference from 2×2 conditions.

Every A,B_j lies in K, while P_F≽0 is not in K because uniqueness implies K∩PSD={0}. Therefore
\[
\|L(Y_\sigma(t)-X_*)\|_2=\Theta(t),
\qquad
\|Y_\sigma(t)-X_*\|_F=\Theta(t^a).
\]
Hence α≤a.

Finally a_k=(2^k-1)/(2^(k+1)-1) increases with k, and k≤s. Consequently α≤a_s=(2^s-1)/(2^(s+1)-1), proving the theorem.

### D. Sharpness

Use the sparse harmonic ladder with source weight 0, root weight a_s, s core weights
    b_j=1-2^{-j}(1-a_s), j=1,...,s,
and terminal weight 1. Root parents are (source,b_s), and core j has parents (root or previous core,terminal). Every midpoint identity holds, with b_s=2a_s. The exact full ambient PSD exponent is a_s, by the harmonic 2×2 minor upper estimates and diagonally-dominant positive definite matching curve. Its greedy exposing layers are terminal (one null direction), all s core vertices, then root, so its rank profile is (1,s,1). Add f-1 fully measured zero null directions: they are exposed together with the terminal at the first step, yielding (f,s,1), preserving exponent. Pad positive target rank with a fully observed positive block. This realizes equality for all f,s.

## Audit and significance

- Every dual stress in the B_j iteration is **globally PSD**, because the positive definite stress from the Gordan alternative is extended by zero on omitted coordinates. It is in K⊥ via compression annihilation. Hence its rank >f contradicts maximal first rank.
- Every selected B_j is an **actual original kernel matrix**, not an abstract quotient; it need not be PSD globally. Only its compression to R_j is PSD, and the displayed support restrictions suffice for a genuine full PSD curve.
- F may have arbitrary dimension f, and all within-F offdiagonal entries of B_j vanish because its R_j-compression is PSD and pairs to zero with Z1 positive definite on F.
- The final obstruction is strict: a_s<1/2 for every finite s. This directly excludes α=1/2 for the entire family of rank profiles (f,s,1), at arbitrary nullity f+s+1.
- This does not settle all length-three facial profiles whose **final** exposed block has dimension >=2, nor all longer chains. It is a sharp, dimension-uniform, dense-kernel structural theorem.
- Gordan–Stiemke and facial reduction are established tools; the specific optimal exponent bound is proved here, with bibliographic novelty unverified.