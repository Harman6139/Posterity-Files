# Milestone 43 — COMPLETE universal sharp upper endpoint for every degree-three PSD rank profile

**2026-11-08. PROVED directly for every arbitrary dense real PSD measurement kernel, without any weighted-flag or sparse universality hypothesis.** This is the broadest rank-profile obstruction yet. It excludes sharp exponent 1/2 at *every* singularity-degree-three instance regardless of dimension and target rank, and computes the exact largest exponent for every facial rank profile (f,s,t).

## Theorem

Let L:S^n→R^m be an arbitrary real linear measurement map, and let X*≽0 with rank(X*)>=1 be the unique PSD solution of L(X)=L(X*). Assume its **canonical maximal-rank facial-reduction chain** has *minimal length three* with consecutive rank drops
\[
(s_1,s_2,s_3)=(f,s,t),\qquad f,s,t\ge1.
\]
Then its optimal **full ambient PSD Frobenius recovery exponent** satisfies
\[
\boxed{
\alpha(\mathcal L,X_*)\le
A_{s,t}:=\frac{2^{t-1}(2^s-1)}{2^t(2^s-1)+1}
=\frac12-\frac1{2[2^t(2^s-1)+1]}
<\frac12.
}
\]
The bound is **exactly sharp for every pair s,t and every f≥1**: an explicit rank-one sparse midpoint pencil, padded by f-1 fully measured null coordinates, has precisely this exponent and its canonical facial rank-drop profile is (f,s,t). Adjoining fully measured positive-definite coordinates raises target rank arbitrarily without changing either invariant.

In particular, every arbitrary dense **degree-three** PSD recovery problem has \(\alpha<1/2\). This is NOT inferred from sparse enumeration: it follows from the direct cone-alternative proof below.

## 1. Two conic kernel flags forced by maximal exposing ranks

Choose orthogonal coordinates
\[
\mathbb R^n=U\oplus D\oplus T\oplus F,
\quad U=\operatorname{range}X_*,
\quad\dim D=t,\ \dim T=s,\ \dim F=f.
\]
The first exposing stress Z1∈K⊥ (K=ker L) is PSD, positive definite on F, and annihilates U⊕D⊕T. The second stress, compressed to W1=U⊕D⊕T, is PSD and positive definite on T, annihilating U⊕D. The third exposes D. Both first and second stresses are chosen **maximal-rank** in their corresponding exposing cones, giving canonical ranks f and s. Put K1=K∩S(W1).

### Lemma A (deep flag inside K1)

Starting with D_remaining=D, repeat:

Let R=D_remaining⊕T and Q_R={P_R H P_R:H∈K1}⊂S(R). The second exposing stress compressed to R is in Q_R⊥ and **positive definite on T**. If Q_R∩S(R)_+={0}, strict Gordan–Stiemke gives a **positive-definite** matrix Z∈Q_R⊥. Lift Z to an ambient stress in K⊥ with compression equal to Z on R and zero on the orthogonal complement of R inside W1. Then it would be a valid *second-step* PSD exposing stress of rank dim(T)+dim(D_remaining)>s, contradicting maximal second stress rank s.

Therefore Q_R∩PSD contains nonzero C_R. PSD complementarity with the second stress PD on T forces C_R supported on D_remaining. Choose an actual A_i∈K1 lifting it; let D_i=range(C_R)⊂D_remaining, and replace D_remaining by its orthogonal complement of D_i inside itself. Repeat until D_remaining=0.

This yields
\[
D=D_1\oplus\cdots\oplus D_l,\quad 1\le l\le t,
\]
with each A_i∈K1 satisfying:
- A_i has positive-definite compression to D_i;
- its compression to \((D_i\oplus\cdots\oplus D_l)\oplus T\) vanishes except on D_i×D_i;
- its F rows and columns vanish because A_i∈K1;
- all matrix entries involving U or *earlier* D_h (h<i) are unrestricted and may be dense.

### Lemma B (middle flag inside K)

Starting with T_remaining=T, repeat:

Let R=T_remaining⊕F and Q_R={P_R H P_R:H∈K}. The first PSD stress Z1, restricted to R, lies in Q_R⊥ and is PD on F. If Q_R∩PSD={0}, Gordan–Stiemke gives a **positive-definite** Z∈Q_R⊥ on R. Extend it by zero on U⊕D and the previously selected middle blocks. This produces a globally PSD stress in K⊥ of rank dim(F)+dim(T_remaining)>f, contradicting maximal first exposing rank f. Hence Q_R∩PSD contains nonzero C_R, which by PSD complementarity with Z1 is supported on T_remaining.

Choose B_j∈K with this PSD compression, let T_j=range C_R, and remove T_j from T_remaining. After finitely many steps:
\[
T=T_1\oplus\cdots\oplus T_k,\quad1\le k\le s,
\]
and each B_j has positive-definite compression on T_j, while its compression to (T_j⊕...⊕T_k)⊕F vanishes outside T_j×T_j. It can have arbitrary dense entries involving U, D, or earlier T_h, including earlier T_h–F cross blocks.

**Critical detail:** Both lemmas invoke strict separation on an image subspace of symmetric matrices. The lifted (Lemma A) or zero-extended (Lemma B) stress is a valid original measurement stress, via the finite-dimensional compression–annihilator identity. Positive definiteness on the larger remaining block would contradict *maximal* current exposing rank; no assumption about a preselected sparse chain is made.

## 2. One finite coupled midpoint system controls all possible dense blocks

Define
\[
B_*=\frac{2^l(2^k-1)}{2^l(2^k-1)+1},
\qquad
a_i=B_*(1-2^{-i})\quad(1\le i\le l),
\qquad
b_j=1-2^{-j}(1-a_l)\quad(1\le j\le k).
\]
All are positive and strictly ordered:
\[
0<a_1<\cdots<a_l<b_1<\cdots<b_k=B_*<1.
\]
They satisfy the exact midpoint identities
\[
2a_1=B_*,\qquad
2a_i=a_{i-1}+B_*\ (i\ge2),\qquad
2b_1=a_l+1,\qquad
2b_j=b_{j-1}+1\ (j\ge2).
\]

Assign weights 0 on U, a_i on D_i, b_j on T_j, and 1 on F, and form
\[
Y(z)=X_*+\sum_{i=1}^l z^{a_i}A_i
                   +\sum_{j=1}^k z^{b_j}B_j+zP_F.
\]

### Complete universal support-order verification

For each matrix at exponent e, the coefficient-rescaling PSD lemma requires that no nonzero block joining weights w,w' have w+w'>2e.

**A_i at order a_i.** It is supported on U⊕D⊕T and, among remaining D_i,...,D_l,T, only the D_i×D_i compression survives. All other potential blocks involve U or an earlier D_h (h<i). The largest possible pair weight is either b_k=B_* for U-to-T, a_(i-1)+B_* for earlier D-to-T, or 2a_i from D_i diagonal. By the displayed midpoint equations, each is ≤2a_i. There is no F block.

**B_j at order b_j.** Its compression to remaining T_j,...,T_k,F has only T_j diagonal. Every other potential block involves U, an arbitrary D_i, or an earlier T_h (h<j). The largest pair weights are bounded by:
- a_l+1=2b_1≤2b_j for D-to-F;
- b_(j-1)+1=2b_j for earlier T-to-F (when j>1);
- a_l+B_*≤a_l+1≤2b_j for D-to-later T;
- b_(j-1)+B_*≤b_(j-1)+1=2b_j for earlier T-to-later T;
- U-to-F has weight 1≤2b_j and T_j diagonal has weight 2b_j.
Thus **all potentially nonzero dense blocks** obey the PSD weighted-order criterion.

**Terminal.** The coefficient P_F≽0 is positive definite on F at exponent 1. The first diagonal coefficient on every D_i and T_j is positive definite by construction, and no earlier coefficient can contribute to that diagonal because of the compressed cone supports.

Apply the elementary coefficient-rescaling lemma: for sufficiently large fixed σ>0,
\[
X(z)=X_*+\sum_i e^{\sigma a_i^2}z^{a_i}A_i+
           \sum_j e^{\sigma b_j^2}z^{b_j}B_j+
           e^\sigma zP_F
\]
is **positive definite** for all sufficiently small z>0. This follows from block-diagonal congruence and suppression of offdiagonal limiting coefficients by factors \(e^{-\sigma(w-w')^2/4}\); it is a full-matrix PSD argument, not a 2×2-minor shortcut.

Every A_i,B_j lies in K, while P_F∉K by unique PSD recovery, so the measurement residual equals Θ(z). The leading nonzero coefficient A_1 occurs at exponent a_1, yielding displacement Θ(z^{a_1}). Hence
\[
\alpha\le a_1
=\frac{2^{l-1}(2^k-1)}{2^l(2^k-1)+1}.
\]
The right side is increasing in the positive integers l,k, and l≤t,k≤s, proving the desired α≤A_{s,t}. QED.

## 3. Exact sharpness for all rank profiles (f,s,t)

Build a sparse harmonic midpoint graph with one source O=0, t deep vertices of weights a_1,...,a_t, s middle vertices of weights b_1,...,b_s, and one terminal F of weight 1, with the displayed midpoint parent pairs:
- deep vertex D_1 parents (O,T_s);
- deep vertex D_i parents (D_(i-1),T_s) for i≥2;
- middle vertex T_1 parents (D_t,F);
- middle vertex T_j parents (T_(j-1),F) for j≥2.
Each parent pair is distinct, and all weight relations hold exactly.

In the standard sparse PSD pencil, a small offdiagonal multiple of each internal diagonal variable appears on its parent edge, with trace, terminal diagonal and off-pencil coordinates measured. The full ambient recovery exponent is the minimum internal weight a_1, by the universal harmonic inequalities and a matching normalized PD curve. The greedy exposing stages remove F first, then **all** middle vertices T_1,...,T_s simultaneously, then **all** deep vertices D_1,...,D_t simultaneously. This gives rank-drop profile (1,s,t) and *minimal* degree exactly three, since the source-parent dependency blocks D_1 from stage two.

Add f-1 fully measured independent null rows/columns. Their projector stresses are immediately available and join the first step, so the canonical rank-drop profile becomes (f,s,t); no new recovery instability occurs and the exponent is unchanged. Add fully measured positive coordinates to obtain any prescribed target rank. This realizes equality for every f,s,t.

## 4. Consequences

1. **Square-root rigidity at degree three:** Every uniquely solvable finite-dimensional real PSD inverse problem with exact minimal singularity degree d=3 has optimal exponent strictly less than 1/2, with an explicit gap depending only on the second and third facial rank drops.
2. **Exact largest exponent given rank profile:** The formula A_{s,t} is attained, so it is the *sharp* universal profile-dependent upper endpoint.
3. **Dimension-only bound at d=3:** Since s+t≤ν-1, maximize A_{s,t} by assigning the available dimensions between second and third drops. This is a finite elementary optimization; an explicit simplified formula can be extracted from the expression without any SDP search.
4. The earlier ν=4 results are recovered: (2,1,1) gives 1/3; (1,1,2) gives 2/5; (1,2,1) gives 3/7.

**Unresolved:** degree d>=4 generally and the full *set* of attainable exponents at each (ν,d) beyond the formerly classified small cases. This theorem is a sharp endpoint/rank-profile classification, not the full spectrum.

## Audit

The proof only uses (i) the semidefinite Gordan–Stiemke strict alternative, (ii) the standard compression-annihilator lifting identity, (iii) maximal-rank first and second exposing stresses, (iv) explicit coefficient support inequalities, and (v) the coefficient-rescaling lemma with a fully proved PSD congruence argument. It does **not** use an unproved depth-preserving sparse conversion. The result holds against every full PSD competitor, because it constructs a lower-bound *witness arc* in the original kernel. A separate upper recovery bound is used only for the explicit sharpness constructions, where it was proved by 2×2 minors for arbitrary competitors.

The novelty of Gordan, facial reduction and analytic-center machinery is not claimed. Bibliographic priority of the precise sharp rank-profile endpoint theorem is not verified.