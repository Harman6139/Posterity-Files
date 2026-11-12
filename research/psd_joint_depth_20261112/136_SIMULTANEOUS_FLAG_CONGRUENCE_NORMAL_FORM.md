# 136 — Simultaneous central/facial flag normal form without changing sharp invariants

**Date:** 2026-11-12.  
**Branch:** `research/psd-joint-depth-universal-20261107`.  
**Status:** proved below for real, complex and quaternionic Hermitian PSD problems, using the canonical maxdet envelope and monomial chart established in 128/132. Not independently refereed.  
**Scope:** an exact reduction of arbitrary rotated greedy flags to coordinate flags for the *existence problem*. The resulting flags need not be prefixes of the weight order. This is not a complete arithmetic realizability criterion for every facial rank-drop profile.

## 1. The theorem

Let F be R, C or H. Let A:H_n(F)->R^m be real-linear and uniquely recover X*>=0 of positive rank r. Write K=ker A. In fixed coordinates let its established canonical central chart be

    C_t ~ D_t^2,
    D_t= I_(U_0) direct-sum (direct-sum_(i=1)^k t^(w_i/2) I_(U_i)),
    U_0=range X*, 0<w_1<...<w_k=1.

Here `~` denotes two-sided Loewner comparison by constants independent of t. Set

    F_i=U_0+...+U_i,  i=0,...,k.

Let

    V_0=F^n > V_1 > ... > V_d=U_0

be the canonical maximum-rank greedy facial survivor flag. Let s_t=dim_F(V_(t-1))-dim_F(V_t).

### Theorem 136.1

There exists an invertible constant F-linear matrix T preserving every F_i such that the congruently transformed problem

    X*'=T X* T*,
    K'=T K T*,
    A'(Y)=A(T^(-1)Y T^(-*))

has all of the following properties:

1. Its canonical central curve satisfies C_t' ~ D_t^2 in the same ordered grade coordinates, so its complete central orders and multiplicities are unchanged.
2. Its greedy survivor flag is T V_0 > ... > T V_d, and every T V_t is spanned by coordinate axes.
3. Its full-ambient sharp recovery exponent, minimum facial degree, and complete greedy rank-drop profile are unchanged.
4. After an additional invertible change restricted to U_0, the target can be normalized to diag(I_r,0), retaining all preceding conclusions.

Consequently, in classifying attainable joint central spectra and greedy profiles, arbitrary rotations do not introduce an additional continuous flag-position variable. One may use a finite nonnegative-integer incidence table describing how many coordinates of each grade are removed at each step. The unknown measurement kernel may still have essential signed/conic information; the theorem does not eliminate it.

## 2. Elementary simultaneous splitting of two flags

We give the linear-algebra proof, including partial flags and repeated central grades. Reverse the survivor flag and write

    G_j=V_(d-j),  j=0,...,d,

so G_0=F_0=U_0 and G_d=F^n. Work first in the quotient by U_0. Thus both flags begin at zero. For each pair i,j, choose a complement E_(i,j) of

    (F_(i-1) cap G_j) + (F_i cap G_(j-1))

inside F_i cap G_j. Such complements exist over each division ring R,C,H. Choose them successively in increasing i+j.

Induction shows

    F_i cap G_j = direct-sum_(a<=i,b<=j) E_(a,b).

Indeed the two previously decomposed subspaces intersect in F_(i-1) cap G_(j-1), whose decomposition is their common subset of summands; the newly chosen complement completes the sum. In particular the union of bases of all E_(i,j) is a basis adapted to both flags. Lift it to F^n and add a basis of U_0. The lifted vectors still give a simultaneous adapted basis because U_0 belongs to every nonzero flag member.

Let S be the matrix of these basis vectors, arranging columns first by their F-grade i. Then S preserves each F_i and is upper block triangular in the decomposition U_0,...,U_k. Its diagonal blocks are invertible. Every G_j, and therefore every V_t, is spanned by a subset of these columns. Set T=S^(-1). Then T preserves the F_i and maps every V_t onto the span of a subset of the original coordinate axes. This proves the purely linear statement.

The simultaneous splitting of two flags is standard linear algebra. Its use here requires the additional analytic and facial-invariance arguments below; a change of basis alone does not identify two different identity-shift central curves.

## 3. Central curves are comparable under every fixed congruence

We prove a slightly more general fact, without assuming that T preserves the grade flag. Let C_t be the original identity-shift maxdet center, and C_t' the identity-shift maxdet center for the transformed problem. Then

    c T C_t T* <= C_t' <= C T C_t T*                 (3.1)

for sufficiently small positive t and constants depending on the two fixed problems and T.

For the upper bound, Y_t=T^(-1) C_t' T^(-*) is PSD. Since

    C_t' - X*' - t I in K',

its original residual is

    A(Y_t-X*)=t A(T^(-1) T^(-*)).

This is O(t). The original maxdet envelope bounds Y_t above by a constant multiple of C_t. Congruence by T gives the desired upper inequality.

For the lower bound, T C_t T* is PSD and its transformed residual is

    A'(T C_t T* - X*')=A(C_t-X*)=t A(I).

The transformed maxdet envelope bounds T C_t T* above by a constant multiple of C_t'. Rearranging gives the lower inequality in (3.1).

Thus the identity shift is not incorrectly assumed to commute with congruence: it becomes a fixed positive shift, and the all-competitor envelope compares the resulting centers.

Now use the T constructed in Section 2. Because it is upper block triangular, the block (a,b) of D_t^(-1) T D_t is zero for a>b, and for a<=b is

    t^((w_b-w_a)/2) T_(a,b).

The diagonal blocks are constant and invertible; all strict cross-grade upper blocks tend to zero. Therefore D_t^(-1) T D_t and its inverse are uniformly bounded. It follows that

    T D_t^2 T* ~ D_t^2.

Combining this with C_t~D_t^2 and (3.1) proves C_t'~D_t^2. All central eigenvalue orders and their multiplicities are consequently unchanged.

## 4. Sharp recovery and exact greedy facial invariance

The transformation is a bijection of the PSD cone. Its measurement residual is unchanged by definition:

    A'(T X T* - X*')=A(X-X*).

The linear maps H->T H T* and its inverse are bounded on the finite-dimensional Hermitian space. Thus their Frobenius norms are comparable by positive constants, uniformly in H. Taking suprema over corresponding PSD competitors gives two-sided comparison of the complete recovery moduli. In particular their sharp exponents agree.

An ambient measurement stress transforms by

    Z'=T^(-*) Z T^(-1).

It lies in (K')-perp exactly when Z lies in K-perp; real-trace pairings are preserved. It annihilates X*' exactly when Z annihilates X*. On the face supported by TV, its quadratic form is the pullback of the quadratic form of Z on V:

    (T v)* Z' (T v)=v* Z v.

Hence the compressed form is PSD on TV exactly when the original compressed form is PSD on V. Its null subspace inside TV is precisely T times the old null subspace inside V, and its compressed rank is unchanged. This correspondence works for every valid exposing stress and every intermediate support V, not just for one selected chain.

Maximum exposing rank is therefore preserved at every step. The unique greedy survivor is the common kernel of the available PSD exposing forms; the bijection maps it to the new common kernel. Induction proves that the entire greedy flag is TV_t. All rank drops are identical. Every facial chain is transported bijectively, so minimum facial length is unchanged as well.

Finally, X*' is positive definite on U_0 and zero outside it, because T preserves U_0. Congruence by its inverse square root on U_0, extended as the identity on the null coordinates, normalizes the target. This further transformation preserves every grade and every coordinate survivor flag, since each survivor contains all of U_0. The preceding arguments apply again. This proves the theorem. QED.

## 5. The finite incidence table

Let m_i=dim_F U_i for i>=1. The simultaneous flag-position table is

    b_(i,t) = dim(F_i cap V_(t-1)) - dim(F_i cap V_t)
              - dim(F_(i-1) cap V_(t-1)) + dim(F_(i-1) cap V_t),
    1<=i<=k, 1<=t<=d.                                (5.1)

The simultaneous splitting proves b_(i,t)>=0. Its margins are

    sum_t b_(i,t)=m_i,
    sum_i b_(i,t)=s_t.                               (5.2)

After the normalization above, b_(i,t) is literally the number of coordinates of grade w_i removed at step t. The first maximum exposure is the terminal grade, so

    b_(k,1)=m_k,  b_(i,1)=0 for i<k,
    b_(k,t)=0 for t>1.                               (5.3)

For fixed multiplicities and profile only finitely many nonnegative integer tables have these margins. Equivalently, an arbitrary original instance is congruent, for all the invariants at issue, to one whose central and greedy flags commute as coordinate projections.

This last statement is about a changed, congruently equivalent instance. It does NOT assert that the original Euclidean-orthogonal central and facial projections commute, nor that there is an orthogonal transformation accomplishing the same normalization.

## 6. Why the prefix theorem is still not the full classification

Prefix schedules are a restricted family of tables: after every step all surviving weights form an initial interval, and each grade is removed all at once. General tables may have non-prefix patterns or split a repeated grade across stages. Even after coordinate normalization, the existence of a kernel with the required positive initial separation and all required maximal face exposures remains to be characterized.

The real non-prefix example in Section 11 of milestone 134 has

    w=(0,1/4,2/5,1/2,3/5,4/5,1),
    layers {6}, {3,5}, {1,2,4}.

Its table is already coordinate and cannot be replaced by the prefix schedule with the same ranks at those weights: the latter violates ell(3)=1. Thus no step in this proof reduces arbitrary profiles to the prefix schedules of 133. Nor does it contradict the real/complex separation of 134.

The unresolved part of the all-real arithmetic profile spectrum is consequently the **kernel realization of these discrete tables**, with the graded positivity and successive face-compression constraints. The present theorem removes rotations as a separate obstacle, but does not remove those positivity constraints or solve the remaining realizability problem.

## 7. Role in the research packet

This is a compact structural reduction supporting future work on the full profile question. The paper-level new result remains the two-channel prefix theorem and its sharp field-sensitive obstruction in 133–134. Simultaneous flag splitting and congruence of PSD cones are classical; this note supplies the needed exact preservation of identity-shift central orders and greedy geometry rather than asserting bibliographic novelty for the underlying linear algebra.
