# Milestone 35 — universal dense nullity-four: alpha=1/7 forces exact depth 4

2026-11-08. **PROVED** for every arbitrary dense PSD measurement kernel, without sparsity assumptions, using the previously established dense sharp weighted-flag extraction. This resolves one of the two potential extra exponents at the nullity-four depth-three frontier. The other, alpha=1/2 at d>=3, remains unresolved by this argument.

## Theorem

Let L:S^n→R^m be an arbitrary real linear map, X*>=0 uniquely recovered by its PSD measurements, rank r>=1 and nullity ν=n-r=4. If the sharp full-matrix Hölder recovery exponent is alpha=1/7, then the **minimal** facial-reduction degree is exactly
\[
\boxed{d=4.}
\]
Thus alpha=1/7 cannot occur at d=1,2,3, for any dense K=ker L. The rank-one sparse constructions at nu4,d4 (checkpoint 17) prove attainability at d4, so the conclusion is sharp.

## Complete proof

**The unique harmonic valuation flag.** From the dense weighted-flag/midpoint extraction and the exact complete rational enumeration of all h<=3 internal midpoint networks (checkpoint 27 and earlier exact catalogue), the exponent alpha=1/7 has exactly one sharp harmonic weight pattern at nullity four:
\[
(0,w_1,w_2,w_3,w_4)=(0,1/7,2/7,4/7,1),
\]
with parents (0,2),(0,3),(1,4) for internal vertices 1,2,3. The four positive null-weight blocks are each one-dimensional. Choose an orthonormal null-space basis e1,e2,e3,e4 according to those weights and write U=range X*.

The *actual kernel coefficients of the sharp PSD arc* at weights 1/7 and 2/7 are H1,H2∈K satisfying
\[
(H_1)_{11}>0,\quad (H_2)_{22}>0.
\]
The PSD order inequalities imply for every block pair (i,j) of H_\ell:
\[
(H_\ell)_{ij}=0\quad\text{if }w_i+w_j>2w_\ell.
\]
Consequently:
- \(H_1\) is supported on \(U+\operatorname{span}\{e_1,e_2\}\), and its *null-null* block has only the entry (1,1) possibly nonzero. It may also have an arbitrary support-to-e2 block, which does NOT affect its stress pairing.
- \(H_2\) is supported on \(U+\operatorname{span}\{e_1,e_2,e_3\}\), and its null-null block has a strictly positive (2,2) entry and possibly entries among e1,e2. In particular \((H_2)_{33}=(H_2)_{23}=0\); its support-to-e3 block is allowed.

**First stress.** Let Z1 be any nonzero first PSD exposing stress, so Z1>=0, Z1∈K⊥ and <Z1,X*>=0. The universal first-stress/valuation alignment theorem (checkpoint 23) implies range(Z1)⊆span(e4). Therefore the first exposing step removes exactly e4. A nonzero first stress exists by facial reduction for a uniquely feasible PSD target. Let
\[
W_3=U+\operatorname{span}(e_1,e_2,e_3),
\quad
K_3=K\cap S(W_3).
\]

**Second stress must remove only e3.** Let Z be any valid second stress, i.e. Z∈K⊥, with compressed S=P_W3 Z P_W3>=0 annihilating U. Since H1,H2∈K3, one has
\[
\langle S,H_1\rangle=\langle S,H_2\rangle=0.
\]
Because S>=0 and S annihilates U, its support-to-null blocks are all zero. By the exact support restrictions on H1,
\[
0=\langle S,H_1\rangle=(H_1)_{11}S_{11},
\]
so S11=0. Positivity then forces **the entire e1 row/column of S to vanish**. Pairing next with H2, and using (H2)33=(H2)23=0, now gives
\[
0=\langle S,H_2\rangle=(H_2)_{22}S_{22},
\]
so S22=0 and the entire e2 row/column vanishes. Thus range(S)⊆span(e3), and every nonzero second stress removes exactly one null direction e3. Such a stress exists: the feasible face W3 is larger than the unique minimal face U, so facial reduction supplies a nonzero compressed exposing stress there.

**Third stress must remove only e2.** After removing e3, the face is
\[
W_2=U+\operatorname{span}(e_1,e_2).
\]
Any PSD compressed stress S on W2 annihilating U satisfies <S,H1>=0 because H1∈K∩S(W2). As before, S11=0 by (H1)11>0, so S is supported on e2. Thus the third step removes exactly e2.

**Fourth step is unavoidable.** After three steps the remaining null direction e1 is still present. A final fourth stress is required to reach the minimal face U. Since nullity is four and every valid facial-reduction chain removes at least one direction per step, the degree is at most four. Therefore the **minimal** degree is exactly four, proving the theorem. QED.

## General structural lemma: triangular kernel support forces maximal facial depth

Let ν>=2. Suppose there exists a one-dimensional null valuation flag e1,...,eν with:
1. every first PSD exposing stress is supported on eν;
2. for each i=1,...,ν-1 there is a kernel matrix H_i∈K∩S(U+span(e1,...,e_(i+1))) whose (i,i) null diagonal is positive and whose null-null entries (a,b) vanish whenever max(a,b)>i;
3. the prior H_1,...,H_(i-1) have positive leading diagonal entries and null-null support restricted to their first i-1 coordinates.

Then every successive valid exposing stress, after compressing away the previously removed largest-index null directions, is supported on its **last remaining** null coordinate. Hence the minimal singularity degree is ν.

**Proof:** Descending induction on the current coordinate face. At U+span(e1,...,ej), each H_i with i<j is supported there and its null-null entries involve only indices ≤i. For any compressed PSD stress S annihilating U, pair with H1 to get S11=0 and hence kill its first row. Then pair H2 to get S22=0, and continue i=3,...,j-1. Each previously killed row makes lower-index null-null entries of H_i irrelevant, while its own positive diagonal forces Sii=0. Therefore S can be supported only on ej; nonzero stress removes exactly that coordinate. Continue until U. QED.

The 1/7 sharp pattern meets these hypotheses automatically from its dense PSD coefficient-support inequalities.

## Audit

- H1 is a **single actual first Puiseux coefficient** with a positive e1 diagonal (and may contain simultaneous support-to-e2 entries); it is NOT wrongly split into unrelated kernel matrices at the same exponent.
- No support-to-target entries of H1,H2 are assumed absent; they are irrelevant because valid PSD stresses annihilate the target support.
- All stresses may have arbitrary off-face entries; the proof uses only their compressed PSD blocks, so it covers arbitrary dense measurement maps.
- The rank-one first-stress alignment is a prior independently proved lemma of this research packet; without it, the conclusion would not follow from the displayed H_i alone.
- The conclusion classifies the prescribed alpha=1/7 at nu4, not every possible alpha or higher-depth triple. The alpha=1/2 high-depth endpoint is separate and remains unresolved.