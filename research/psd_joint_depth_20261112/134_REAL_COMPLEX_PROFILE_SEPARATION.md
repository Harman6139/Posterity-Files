# 134 — Full central spectra and greedy facial profiles detect the scalar field

**Date:** 2026-11-12.  
**Branch:** `research/psd-joint-depth-universal-20261107`.  
**Predecessors:** 125 (aligned real bottleneck), 128 (real tuple spectrum), 132 (rank universality and central multiplicities), 133 (two-channel prefix-schedule theorem).  
**Status:** complete research arguments, subject to independent mathematical review.  
**Not claimed:** a complete arithmetic classification of all real tuples (n,r,s_1,...,s_d,alpha) with the central weights left free.

## 1. Main conclusions

The rank universality of the exponent–degree spectrum does NOT persist after simultaneously prescribing the complete central spectrum and the greedy facial rank-drop profile. This failure already occurs between real and complex Hermitian PSD cones of the same Jordan rank seven, with rank-one target and nullity six.

The earlier real obstruction in 125 only ruled out one grade-aligned flag. The proof below removes that hypothesis: no rotated real exposing subspaces can produce the forbidden greedy profile. An explicit seven-generator complex pencil realizes it. More precisely, for the displayed spectrum the missing profile is attainable over F=R,C,H at target rank r exactly when

    r * dim_R(F) >= 2.

Thus both the scalar field and the number of positive support directions can matter for this refined problem. There is no contradiction with 128 or 132: those classify coarser data.

The companion uniform theorem 133 shows that two real coordinates per offdiagonal entry suffice for every arithmetically permitted grade-prefix schedule, at unchanged nullity and arbitrary multiplicities. The present example proves that this uniform two-coordinate requirement is sharp.

## 2. The spectral vector and the exact profile theorem

Take six simple null grades

    (w_1,w_2,w_3,w_4,w_5,w_6)
      = (1/4, 3/7, 1/2, 17/28, 5/7, 1),                 (2.1)

and source weight w_0=0. They have harmonic parents

    P_1=(0,3), P_2=(1,4), P_3=(0,6),
    P_4=(3,5), P_5=(2,6).                              (2.2)

The canonical primal central eigenvalues have orders Theta(1), of multiplicity r, and Theta(t^(w_i)), i=1,...,6, each of multiplicity one. The dual orders are automatically 1-w_i. The only possible sharp recovery exponents are

    alpha in {1/8, 3/14, 1/4}.                         (2.3)

### Theorem 134.1 — rotation-free separation and exact capacity threshold

For these central orders, in H_(r+6)(F), F=R,C,H, the possible greedy rank-drop profiles are exactly

    A=(1,3,2),
    B=(1,1,3,1),
    C=(1,1,2,2),
    D=(1,1,1,2,1),                                    (2.4)

together with

    E=(1,2,2,1)                                       (2.5)

if and only if r dim_R(F)>=2. Every listed profile is attainable with each exponent in (2.3).

In particular, E is impossible in real S^7 with rank-one target, even allowing arbitrary dense kernels and arbitrarily rotated intermediate exposing subspaces. It is attainable in complex H_7(C), and in real S^8 with rank-two target. In both constructions the nullity is six and the null central orders are exactly (2.1).

We first prove the real obstruction; the full list and attainability are then established.

## 3. Canonical facts used in the obstruction

We use the fixed monomial chart proved in 128/132, not any sparse-normal-form hypothesis. In fixed orthogonal coordinates adapted to (2.1), the actual center has coefficients

    C_t = X* + sum_(e>0) t^e H_e,

with H_e in K whenever e<1. For each internal grade i, write H_i for H_(w_i). Then

    (H_i)_(ii)>0,
    (H_i)_(ab)=0 whenever w_a+w_b>2w_i.                (3.1)

For a source block of dimension r, the same condition holds blockwise. In the real rank-one case source coordinate 0 is one dimensional.

The dual path Z(t)=t C_t^(-1) lies in K-perp. Its i-th diagonal first has a strictly positive coefficient at order 1-w_i, and its (a,b) entry has order at least

    1-(w_a+w_b)/2.                                    (3.2)

All its Puiseux coefficients are actual ambient measurement stresses. Coefficients at order less than one annihilate the source target.

Every internal positive coefficient has at least one nonzero tight cross-grade block whose endpoint weights average to its grade. This follows either from harmonic downshift or from positive separation of the graded initial kernel. In particular, the only tight parent pair for w_3=1/2 in (2.1) is (0,6), so in the real rank-one case

    (H_3)_(06) != 0.                                  (3.3)

The first maximum-rank exposure is exactly the terminal grade e_6. This follows by successively pairing a global PSD stress with H_1,...,H_5 and using the leading constant coefficient of Z(t) for attainability.

## 4. Why a rank-two second exposure cannot evade the obstruction by rotation

After removing e_6, the current face is supported on

    W=span(e_0,...,e_5).

The matrices H_1 and H_2 are supported inside W, because 2w_2=6/7<1. Pairing successively with them forces rows 1 and 2 of every PSD compressed exposing stress to vanish. Thus every second exposed range is contained in

    V=span(e_3,e_4,e_5).                               (4.1)

The leading dual coefficient on W has positive compression on e_5 alone. Therefore a maximum-rank second stress always exposes e_5. If the maximum rank were two, its support would have the form

    C=span(e_5,v),  v in span(e_3,e_4), v!=0.           (4.2)

This statement is valid over R, C or H, with the corresponding one-dimensional module interpretation.

Take the ACTUAL dual coefficient at

    E=1-w_4=11/28,

and compress it to W, calling the result T. It is the compression of an ambient element of K-perp. Every row 0,1,2 vanishes in T, since

    (w_2+w_5)/2 = 4/7 < 17/28 = w_4.

Its restriction to span(e_3,e_4) is

    T|_(3,4) = diag(0,a),  a>0.                       (4.3)

Indeed 1-w_3=1/2>E and 1-(w_3+w_4)/2>E, whereas the e_4 diagonal begins positive at E. Entries involving e_5 can be arbitrary; that does not impair the argument.

Suppose v has a nonzero e_3 component. The complement of C in V is a line whose e_4 component is nonzero. By (4.3), T is strictly positive on that line. If S is the hypothesized positive rank-two stress on C, then T+M S is positive definite on V for sufficiently large fixed M. This is the elementary block Schur-complement fact: the block on C becomes arbitrarily positive, while the positive block on C-perp stays fixed and the cross correction tends to zero. All rows outside V still vanish. Thus T+M S is a legitimate compressed measurement stress of rank three, contradicting maximality of rank two.

Consequently v has zero e_3 component. Any rank-two maximum second exposure, even one initially allowed to rotate freely, MUST have

    C=span(e_4,e_5).                                  (4.4)

This is the additional argument absent from the aligned obstruction in milestone 125.

## 5. The real one-coordinate bottleneck

Now specialize to F=R and r=1. Suppose a PSD compressed second stress S has range (4.4), and let Z in K-perp be an ambient lift.

For H_3, all entries on C vanish. Among its possible off-face entries involving the removed coordinate 6, only (0,6) is allowed by (3.1). It is nonzero by (3.3). Therefore

    0=<Z,H_3>=2 (H_3)_(06) Z_(06),

so Z_(06)=0.

For H_4, the only possible off-face entry is again (0,6), because

    (w_1+1)/2=5/8>17/28=w_4.

On C its only nonzero entry is the strictly positive (4,4) entry: both the (4,5) and (5,5) weights exceed w_4. Hence

    0=<Z,H_4>=(H_4)_(44) S_(44)+2(H_4)_(06) Z_(06)
              =(H_4)_(44) S_(44)>0,

a contradiction.

Together with Section 4 this excludes EVERY rank-two maximal second exposure, not merely the coordinate flag in (4.4). Thus the profile (1,2,2,1) is impossible for every real rank-one kernel with central spectrum (2.1).

The obstruction consumes one real off-face scalar to satisfy the surviving half-weight coefficient and leaves no independent scalar to expose the next grade. It is not an assertion that arbitrary real profile problems are impossible to classify.

## 6. An explicit complex witness

In H_7(C), put lambda=1/100, X*=E_00 and c=1/(2lambda)=50. Use R_ab and I_ab as defined in 133. Let K be the real span of the following seven Hermitian matrices:

    H_1=E_11-E_00+lambda(R_03+I_02),
    H_2=E_22-E_00+lambda(R_14+I_04),
    H_3=E_33-E_00+lambda(R_06+I_04),
    H_4=E_44-E_00+lambda(R_35+I_06),
    H_5=E_55-E_00+lambda(R_26+I_06),
    J_2=E_22-E_00+lambda R_15,
    J_3=E_33-E_00+lambda R_25.                         (6.1)

Take A=P_(K-perp). These are real-linear measurements with rational real and imaginary coefficients.

### 6.1 Genuine ambient stresses

The following four ambient matrices belong to K-perp:

    Z_1=E_66,
    Z_2=E_44+E_55-c I_06,
    Z_3=E_22+E_33-c(I_04+R_15+R_25),
    Z_4=E_11-c I_02.                                  (6.2)

Every one of the 28 generator/stress pairings is exactly zero. On the successive faces supported on {0,...,6}, {0,...,5}, {0,...,3}, {0,1}, their compressions are respectively

    E_66,  E_44+E_55,  E_22+E_33,  E_11.

Thus they form a valid chain with profile (1,2,2,1).

### 6.2 Exact maximality, not just an exhibited chain

Initially, a PSD stress annihilating E_00 has zero source row. The H_1 equation forces diagonal 1 to vanish, H_2 then forces 2, H_3 forces 3, H_4 forces 4, and H_5 forces 5. Only 6 can be exposed, and Z_1 attains it.

At the second face H_1 forces row 1 to vanish; J_2 then forces row 2 to vanish; J_3 then forces row 3 to vanish. Only 4 and 5 are exposable, and Z_2 attains both.

At the third face H_1 still forces row 1 to vanish. Z_3 attains both remaining directions 2 and 3. Z_4 finally exposes 1. Thus these are the actual greedy faces, and their length four is minimum against all possible chains.

The real bottleneck is avoided because the real (0,6) coordinate cancels the H_3 equation while the imaginary (0,6) coordinate cancels the H_4 and H_5 equations. They are independent real coordinates on one Hermitian entry.

### 6.3 Full-ambient sharp exponent and exact central spectrum

Use weights (2.1), D_t=diag(t^(w_i/2)), and assign degrees

    (1/4,3/7,1/2,17/28,5/7,27/56,4/7)

to (H_1,...,H_5,J_2,J_3). The normalized limits have independent pivots on the five real tight edges in (2.2), and on R_15,R_25. All imaginary release terms have strictly smaller entry weights than their generator degree and disappear in the limit. The two J limits are pure real offdiagonal directions.

An explicit positive separator is available. Put

    a=(0,7,12,14,17,20,28),
    W_ii=2^(a_i^2),
    W_(P_i,real)=-50*2^(a_i^2), i=1,...,5,

and all other offdiagonals zero. It annihilates every normalized limiting generator. For every tight edge, its normalized absolute value is

    50 * 2^(-(a_b-a_a)^2/4).

The smallest square-gap exponent is nine, and each row has at most two nonzero offdiagonal entries. Thus every normalized row sum is at most

    100/512 = 25/128 < 1.

So W is strictly positive definite. The graded-separation lemma of 133 gives, for ALL ambient Hermitian PSD competitors,

    X <= C D_t^2,
    ||X-X*||_F=O(t^(1/4)).

The matching arc

    X(t)=E_00+sum_(i=1)^5 t^(w_i) H_i+tE_66            (6.3)

has positive null diagonal t^(w_i), source diagonal tending to one, and uniformly small normalized offdiagonals. It is strictly positive definite for small t. Its residual is exactly t and its displacement is Theta(t^(1/4)). Therefore the sharp exponent is 1/4. The arc is thick in the D_t chart; the maxdet envelope and the upper bound give cD_t^2<=C_t<=CD_t^2. Hence the full central eigenvalue-order vector is exactly (2.1).

To realize alpha=1/8 or 3/14, add G=lambda R_(0,v), v=1 or 2 respectively, and add t^(w_v/2)G to (6.3). These real coordinates are unused; even R_02 is distinct from the imaginary release I_02. All stresses in (6.2) remain orthogonal to G. The positive separator already has zero at G's coordinate, and its normalized limit is an additional independent pure offdiagonal pivot. Thus the same full spectral vector and profile realize every alpha in (2.3).

## 7. Exact threshold in source rank and scalar field

The complex construction works over H by using one fixed complex subfield and measuring all other components. Its full-ambient proof and maximality proof remain valid: a zero PSD diagonal annihilates the entire quaternionic row, and the same positive separator works in the full quaternionic space.

For a REAL realization with target rank two, add a positive source coordinate s, set X*=E_00+E_ss, and replace every imaginary source edge I_(0,b) in (6.1) and (6.2) by the real edge R_(s,b). Keep all real tight edges and blocker edges unchanged. All pairings, off-face supports and row-zero arguments are identical. The releases still have the same weights because the new source weight is zero. The leading separator gains only one positive source diagonal, and the matching arc gains a constant E_ss. Optional leading edges R_01 or R_02 use the original source and do not collide with releases from s.

Fully measured positive padding then supplies every r>=2 over R and every r>=1 over C or H. Conversely, the only case with r dim_R(F)<2 is real r=1, which Sections 4–5 exclude. This proves the exact threshold for E.

The threshold is stated in terms of this particular refined spectral/profile datum. It is not a general formula for every prescribed profile.

## 8. Why the profile list (2.4)–(2.5) is complete

This part holds for arbitrary dense kernels and arbitrary rotated greedy faces over R, C or H, at any positive source rank r.

After the first step, Section 4 shows that the second maximal rank is one, two or three. If it is two, the range must be span(e_4,e_5). If it is one, it must be span(e_5); if it is three, it is all of span(e_3,e_4,e_5).

If the second rank is three, the remaining face is W_2. The dual upper recurrence exposes both remaining null grades at once. This gives A=(1,3,2).

If the second rank is two, the remaining face is W_3. At j=3 both bounds equal one: ell(3)=u(3)=1. Consequently the next exposure is exactly {2,3}, then {1}. This gives E=(1,2,2,1).

Suppose the second rank is one, leaving W_4. H_1 is supported in W_4, so every next PSD stress has zero row 1. The top remaining grade e_4 is exposable and belongs to every maximal exposed range. The third maximal rank is one, two or three.

A rank-two third exposure must be span(e_3,e_4), even if rotations are allowed. The proof repeats Section 4 with the actual dual coefficient at E=1-w_3=1/2: on W_4 it has zero rows 0,1, and its restriction to span(e_2,e_3) is diag(0,b), b>0. The required zero orders follow from

    1-(w_1+w_4)/2=4/7>1/2,
    1-w_2=4/7>1/2,
    1-(w_2+w_3)/2=15/28>1/2.

If a rank-two exposing range containing e_4 mixed e_2 into its other direction, addition of a large multiple of that PSD stress to this coefficient would expose all three grades 2,3,4, contradicting maximality. Therefore the third survivor is W_2, whose remaining two grades expose together. This gives C=(1,1,2,2).

A rank-three third exposure leaves W_1 and gives B=(1,1,3,1). A rank-one third exposure removes e_4 alone, leaving W_3. Again ell(3)=u(3)=1, so the next exposure has rank two and the last rank one, giving D=(1,1,1,2,1). There are no other possibilities.

The half-weight theorem restricts alpha to exactly (2.3). It remains to establish attainability of A–D over R, including all those exponents.

## 9. Explicit real realizing families for A–D

Use lambda=1/100, c=50, the weights and parents (2.1)–(2.2), and tight generators

    T_i=E_ii-E_00+lambda R_(P_i),  i=1,...,5.

The following real kernels realize the four profiles. Each additional displayed edge is a strictly lower-weight release or a strictly higher-weight blocker. Consequently their normalized leading forms consist of the same five tight forms, together with independent pure blocker pivots. The positive separator from Section 6 annihilates these forms (and has zero on the additional blocker coordinates). Shared releases at (0,6) in A occur only in higher-degree generators, so disappear in those normalized limits. The all-competitor proof and the matching thick monomial curve therefore apply to all four kernels. Optional G=lambda R_01 or lambda R_02 is unused in every kernel and preserves the listed stresses; it realizes the two smaller exponents.

### A=(1,3,2)

Use T_1,T_2,T_3, T_4+lambda R_06, T_5+lambda R_06. Stresses are

    E_66,
    E_33+E_44+E_55-c R_06,
    E_11+E_22-c(R_03+R_14).

At the second face H_1 forces row 1 to vanish and H_2 then forces row 2. The displayed second stress attains all three other directions. Thus the profile is exact.

### B=(1,1,3,1)

Use T_1, T_2+lambda R_05, T_3,T_4,T_5 and

    J_3=E_33-E_00+lambda R_24.

The first two stresses are E_66 and E_55-cR_26. Choose positive z_2,z_3,z_4 satisfying z_2 z_4>c^2 z_3^2. A specific exact choice is

    z_i=2^(2(28w_i)^2), i=2,3,4.

The third stress is

    z_2 E_22+z_3 E_33+z_4 E_44
       -c(z_2 R_05+z_3 R_06+z_3 R_24+z_4 R_35).

Its only on-face offdiagonal is -c z_3 at (2,4); the displayed inequality proves its compression is positive definite on {2,3,4}. The final stress is E_11-cR_03.

At the second face the equations of T_1, the modified T_2, J_3 and T_4 successively kill rows 1,2,3,4. At the third face T_1 still kills row 1. The stresses attain every other direction at the stated stage, proving exact maximality.

### C=(1,1,2,2)

Use T_1,...,T_5 and J_3=E_33-E_00+lambda R_25. Stresses are

    E_66,
    E_55-cR_26,
    E_33+E_44-c(R_06+R_25+R_35),
    E_11+E_22-c(R_03+R_14).

At the second face T_1,T_2,J_3,T_4 successively kill rows 1,2,3,4. At the third face T_1,T_2 still kill rows 1,2. The displayed stresses attain the remaining permitted rows, so the profile is exact.

### D=(1,1,1,2,1)

Use T_1,...,T_5 and J_3=E_33-E_00+lambda R_24. Stresses are

    E_66,
    E_55-cR_26,
    E_44-cR_35,
    E_22+E_33-c(R_14+R_06+R_24),
    E_11-cR_03.

At the second and third faces T_1,T_2,J_3 kill rows 1,2,3; T_4 also kills row 4 at the second face. At the fourth face T_1 still kills row 1. The stresses attain each intended group, proving exact maximality.

All listed ambient pairings are zero. All compressed stresses are diagonal PSD except the explicitly positive 2-by-2 block in B. The common initial-separation and arc arguments establish uniqueness, the exact full-ambient exponent, and the exact entire central spectrum. Positive support padding and extension to C or H preserve these direct row-zero arguments. This completes Theorem 134.1. QED.

## 10. A separate warning: the scalar spectrum plus the profile endpoint is not enough

One might try to classify a prescribed real profile by taking the already-known scalar (nu,d) spectrum and imposing only the sharp upper endpoint beta(s) of milestone 45. That proposed simplification is false even at nullity four.

Both alpha=3/14 and alpha=5/14 occur at nu=4,d=3, but neither can have profile (1,1,2), although both satisfy

    2^(-3)<=alpha<=beta(1,1,2)=2/5.

Here is an arithmetic exclusion, not a numerical enumeration.

The denominator of 2alpha is seven. A harmonic certificate with h internal vertices has denominator dividing det(2I-A), where A is its internal parent adjacency matrix and 1<=det(2I-A)<=2^h. At nu=4 this forces h=3, determinant seven, and all positive grades simple. For three vertices, direct determinant expansion gives

    det(2I-A)=8-2*(number of directed 2-cycles)
                  -(number of directed 3-cycles).

Thus there are no 2-cycles and exactly one 3-cycle. Any extra internal edge would reverse one of its edges and create a 2-cycle, so the internal graph is exactly the directed 3-cycle. Each other parent is a boundary 0 or 1. Solving cyclic equations 2w_i=w_next+epsilon_i shows that the three weights are either {1,2,4}/7 or {3,5,6}/7; the all-zero and all-one bit patterns are excluded by strict interior weights. Containing 3/7 or 5/7 forces

    w=(0,3/7,5/7,6/7,1).

At the face W_3, the dual upper rule has p(3)=2 and therefore forces a second exposure of rank at least two. Profile (1,1,2) is impossible, over any matrix field covered by the canonical theorem. The profile (1,2,1) is realized by the one-switch construction with either exponent. This proves the failure of the endpoint-only rule.

The determinant bound is the elementary directed-forest expansion of the transient binary midpoint matrix; equivalently it counts cycle-free parent selections out of 2^h choices. At h=1,2 the bound excludes denominator seven directly; at h=3 the displayed determinant identity supplies the complete argument.

This warning is about the stronger profile problem, not an error in the scalar classification.

## 11. Non-prefix flags really exist

A prefix-schedule theorem must not be relabeled as a classification of all flags. For example the real tight-parent system with

    w=(0,1/4,2/5,1/2,3/5,4/5,1),
    P=((0,3),(0,5),(0,6),(2,5),(4,6))

has greedy layers

    {6}, {3,5}, {1,2,4}.

Take generators T_i=E_ii-E_00+lambda R_(P_i). Ambient stresses are

    E_66,
    E_33+E_55-c(R_06+R_46),
    E_11+E_22+E_44-c(R_03+R_05+R_25).

At the second face T_1,T_2,T_4 force rows 1,2,4 to vanish, and the second stress attains rows 3,5. The third stress attains all remaining null rows. The same tight-pivot separator and thick curve prove the stated canonical weights and exponent 1/4.

Its rank profile is (1,2,3), but the sorted-prefix schedule 6->5->3->0 is impossible at these weights, because ell(3)=1. This makes the distinction between a prescribed rank composition and a prescribed aligned prefix schedule concrete.

## 12. Research status and single-paper recommendation

**New, fully proved here:** a rotation-free field-sensitive profile obstruction; an explicit complex witness; an exact source/field threshold; the complete refined profile list for the one separating spectral vector; and a rigorous failure of the naive endpoint-only replacement. The uniform all-dimensional positive result is the two-channel prefix theorem in 133.

**Still not proved:** a compact arithmetic iff for every real tuple (n,r,s_1,...,s_d,alpha) with arbitrary central spectra and arbitrary greedy flags. Neither the examples nor the prefix theorem are represented as such a solution. No claim is made that this remaining classification is impossible.

For the single paper, the field-sensitive obstruction is a concise sharp boundary to the rank-universality theorem of 132. The uniform two-channel construction can be included as a related structural theorem if the proof-length budget permits. Do not replace the main exponent–degree classification with a long catalogue of profile cases or claim that every profile has now been classified.

The background is standard facial reduction and maximum-determinant regularization; the exact new claims have not been independently referee-verified or globally novelty-certified. The relevant primary comparison is Sremac–Woerdeman–Wolkowicz, SIAM J. Optim. 31 (2021), 812–836, DOI 10.1137/19M1289327, which studies the external maxdet family and links spectral rates to singularity degree, not the field-sensitive complete profile datum proved here.
