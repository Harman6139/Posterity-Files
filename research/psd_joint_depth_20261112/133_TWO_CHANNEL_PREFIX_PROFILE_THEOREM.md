# 133 — Two real offdiagonal coordinates suffice for every admissible grade-prefix facial schedule

**Date:** 2026-11-12.  
**Starting head:** `55aebb71fd8b1c1ebd4f047a645f83014a562c38`.  
**Branch:** `research/psd-joint-depth-universal-20261107`.  
**Status:** complete research proof, using the canonical-chart necessity established in 128/132; not independently refereed.  
**Scope:** a necessary-and-sufficient classification of prescribed **grade-prefix schedules** over complex and quaternionic Hermitian PSD cones, with arbitrary grade multiplicities, exact sharp exponent and exact minimum facial degree. This is NOT a classification of every real-PSD rank-drop profile with the central weights unspecified, nor a claim that all greedy flags are grade-prefix flags.

## 1. Result and significance

The real one-switch theorem selects particular schedules of each permissible length. Here one additional real coordinate in every offdiagonal entry removes the schedule-selection restriction: every arithmetically allowed prefix schedule is realizable at the original nullity. The proof uses real and imaginary components as two independent linear coordinates. It uses no clone coordinates and, after identifying one redundant source blocker, no multi-child diagonal generators.

Milestone 134 gives a rotation-free real obstruction and a complex witness. It proves that one real offdiagonal coordinate does not suffice uniformly. The change of scalar field is therefore consequential for the joint central-spectrum/facial-profile problem, although the coarser exponent–degree spectrum of 132 remains rank-universal.

### Conventions

Let H_n(F) be the real vector space of Hermitian matrices over F=C or H, with inner product Re tr(XY). Measurements are real-linear. In the quaternionic case fix one imaginary unit i and use its complex subfield for the construction. All unmentioned quaternionic components are measured. Let K be a real linear subspace and A=P_(K-perp). The target is X*=diag(I_r,0), r>=1.

The sharp full-ambient exponent alpha is defined by

    sup{||X-X*||_F : X>=0, ||A(X-X*)||_F<=delta} = Theta(delta^alpha).

At each facial-reduction step take a maximum-rank PSD compressed measurement stress. Its kernel in the current face is the unique next greedy face. The ranks removed by this canonical process form the greedy rank-drop profile. This process has minimum length; a proof is recalled below.

For a pair of different coordinate representatives a<b define Hermitian entry directions

    R_ab = e_a e_b^* + e_b e_a^*,
    I_ab = i e_a e_b^* - i e_b e_a^*.

Their squared Frobenius norms are two and their real inner product is zero. Thus R_ab and I_ab are two independent real coordinates on the same physical offdiagonal entry.

## 2. Exact theorem

Fix a strict harmonic certificate

    0=w_0<w_1<...<w_k=1,
    2w_i=w_(a_i)+w_(b_i),  0<=a_i<i<b_i<=k,  1<=i<k.

Fix positive grade multiplicities m_1,...,m_k, let nu=sum m_i, and let the positive target rank be r>=1. Write U_0 for the target support and U_i for an m_i-dimensional null grade. Let

    W_j = U_0 + U_1 + ... + U_j.

For 1<=j<k put

    ell(j) = #{1<=i<j : 2w_i<w_(j+1)},
    u(j) = min{1<=p<=j : 2w_p>w_j+w_(p-1)} - 1.

Consider a proposed prefix schedule

    k=j_0 > j_1=k-1 > j_2 > ... > j_d=0,
    C_t={j_t+1,...,j_(t-1)}.

Here C_t is a set of grade indices, not a set of individual coordinates.

### Theorem 133.1

For k>=2, the following data are simultaneously realizable in H_(r+nu)(C), and in H_(r+nu)(H):

* canonical central grades w_i with multiplicities m_i;
* greedy faces exactly W_(j_0), W_(j_1),...,W_(j_d);
* sharp full-ambient exponent alpha;

if and only if

    ell(j_(t-1)) <= j_t <= u(j_(t-1))  for t=2,...,d,
    alpha=w_v/2 <= w_1 for some v in {1,...,k}.

The target nullity is exactly nu, with no overhead. The exact rank drops are

    s_t = sum_(i in C_t) m_i,

and d is the minimum facial-reduction degree, not merely the length of the displayed chain. All real and imaginary coefficients of the constructed data are rational.

For k=1 the only schedule removes U_1 at the first step; alpha can be 1 or 1/2, with arbitrary m_1.

The theorem is not asserting that an arbitrary instance has prefix greedy faces. It is an iff for the specified aligned schedule. Non-prefix greedy instances exist, as recorded at the end of 134.

## 3. Necessity from the actual primal and dual central coefficients

Use the established canonical center

    C_t = argmax{log det X : X>0, X-X*-tI in K},
    c D_t^2 <= C_t <= C D_t^2,
    D_t = I_(U_0) direct-sum (direct-sum_i t^(w_i/2) I_(U_i)).

The entries of C_t and Z_t=t C_t^(-1) have convergent Puiseux expansions. For every internal grade i, the actual coefficient T_i of C_t at order w_i lies in K, is positive definite on U_i, and has no (U_a,U_b) block with w_a+w_b>2w_i. Each coefficient of Z_t lies in K-perp. Its U_i diagonal starts positive definite at order 1-w_i, and its (a,b) block has order at least 1-(w_a+w_b)/2.

At the initial face, a PSD stress annihilating X* has zero U_0 row. Pairing successively with T_1,...,T_(k-1) forces all internal rows to vanish. The constant coefficient of Z_t is positive definite on U_k and zero elsewhere. Thus the first maximal exposed range is exactly U_k, explaining j_1=k-1 and s_1=m_k.

Now let the current face be W_j.

**Lower restriction.** If i<=ell(j), then 2w_i<w_(j+1), so T_i is supported entirely in W_j. Pairing successively with these T_i forces U_1,...,U_ell(j) to survive any PSD exposure. A prefix survivor W_q therefore has q>=ell(j).

**Upper restriction.** Put p=u(j)+1 and E=1-w_p. Truncate the actual dual series on W_j through exponent E. Every row in U_0+...+U_(p-1) vanishes in that truncation, because

    1-(w_(p-1)+w_j)/2 > 1-w_p=E.

Every diagonal leading coefficient on U_p,...,U_j is included and positive definite. The finite coefficient-rescaling lemma turns this truncation into one actual PSD compressed measurement stress, positive definite on the entire suffix U_p+...+U_j. For clarity, that lemma multiplies the coefficient at exponent e by exp(sigma e^2). After normalization on diagonal grade b_i, a surviving cross block acquires exp(-sigma(b_i-b_j)^2/4); sufficiently large fixed sigma makes the limiting block matrix positive definite. All coefficients being combined belong to K-perp, so this is a genuine ambient measurement stress.

A maximum-rank stress cannot leave any of that suffix unexposed. Hence q<=u(j).

The half-weight restriction alpha=w_v/2<=w_1 follows from the established weighted Dikin support formula. Briefly, an internal positive kernel mode at weight w_1 gives alpha<=w_1. A lower-order invisible direction cannot have a null–null entry; it must have a support-to-null entry of weight w_v/2. If alpha=w_1, harmonicity of the lowest grade gives w_v=2w_1. This proves necessity.

## 4. Schedule edges and their arithmetic inequalities

It is enough first to describe rank one and simple grades. Prescribed multiplicities and target rank will be included directly in the same formulas.

For an internal child i, let t(i)>=2 be the unique stage with i in C_(t(i)). Retain the tight parent edge

    P_i=(a_i,b_i).

Give it a release edge and a blocker edge

    R_i=(0, j_(t(i)-1)+1),
    B_i=(i-1, j_(t(i)-2)).

The release midpoint is at most w_i. Indeed, at the assigned transition j->q, i>q>=ell(j). For i<j this gives 2w_i>=w_(j+1); for i=j the same inequality follows from its harmonic parents, since b_i>=j+1.

The blocker midpoint is at least w_i. For t(i)=2 this follows from harmonicity and a_i<=i-1, b_i<=k. For t(i)>2, child i survives the preceding transition J->j, and i<=j<=u(J), so

    2w_i <= w_(i-1)+w_J.

Thus

    (w_(R_i.lower)+w_(R_i.upper))/2 <= w_i
       <= (w_(B_i.lower)+w_(B_i.upper))/2.

The tight physical edges P_i are pairwise distinct. The blocker physical edges B_i are pairwise distinct, since their lower endpoints are i-1. Release physical edges are source edges, constant within one exposure layer and distinct between layers.

## 5. Two-coordinate ownership and the only three-way collision

Put each tight edge in its REAL coordinate, and every release in its IMAGINARY coordinate.

For each blocker B_i:

* if B_i is not a tight physical edge, put the blocker in its real coordinate;
* if B_i is a tight physical edge but not a release physical edge, put it in its imaginary coordinate;
* if B_i is both a tight and a release physical edge, OMIT this blocker.

The last instruction is legitimate because this case is necessarily the redundant blocker of child one. Here is the full proof.

A release edge has source endpoint zero. Thus B_i being a release implies i=1. Prefix ordering makes t(1)=d. Write b=j_(d-2), so B_1=(0,b). No earlier release R_t, t<d, equals this edge: its upper endpoint j_(t-1)+1 is at least b+1. Therefore a collision can occur only with the final release, and

    b=j_(d-1)+1.

The blocker inequality gives w_b>=2w_1, while the release inequality for child one gives w_b<=2w_1. Hence equality holds. If B_1=P_j, harmonicity and distinct weights imply j=1. Thus

    B_1=P_1=R_1=(0,b),

where R_1 here means the release assigned to child one. Before the final stage the source-to-b entry remains on-face. The tight generator of child one, which uses both its real and imaginary coordinates, already prevents that child from being exposed. The independent blocker is redundant.

This is a deletion of a redundant constraint, not an unsupported identification of two independent kernel coefficients. It avoids exactly the positive-circuit issue of earlier shared-edge constructions.

After this deletion, every tight-real coordinate and every surviving blocker coordinate is globally unique. No blocker coordinate is a release-imaginary coordinate. Different coordinates on one physical pair are orthogonal under Re tr(XY).

## 6. Actual rational matrices

Select one coordinate representative from every U_i and one source representative o in U_0. E_i denotes the identity on U_i, extended by zero; E_oo is the source rank-one projector. Interpret all parent, release and blocker pairs as edges between these representatives.

Choose a positive rational lambda sufficiently small, for example lambda=1/[100(r+nu)^2]. For every internal child set

    H_i = E_i - m_i E_oo + lambda R_(P_i) + lambda I_(R_i).

Both terms are kept if P_i and R_i are the same physical pair: they occupy different real coordinates.

For every nonomitted blocker set

    N_i = E_i - m_i E_oo + lambda F_(B_i),

where F is its assigned real or imaginary coordinate.

If alpha=w_v/2<w_1, also include

    G = lambda R_(0,v).

This real coordinate is unused. A tight edge there would force an internal grade alpha<w_1. A blocker there would have midpoint alpha although every blocker midpoint is at least its child's weight, hence at least w_1. Releases use imaginary coordinates.

Let K be the real span of these generators and A=P_(K-perp). They all have trace zero and zero terminal diagonal. The projection A has rational coefficients in real entry coordinates because the generators are rational and their Gram matrix has a rational inverse. The target is X*=I_(U_0).

## 7. Complete full-ambient recovery proof

### 7.1 A graded-separation lemma

Let the coordinate weights lie in [0,1], with weight zero on the support of X*. Suppose K has a constant basis H_j and positive degrees gamma_j such that

    t^(gamma_j) D_t^(-1) H_j D_t^(-1) -> B_j,

where the limits B_j are linearly independent and their span I contains no nonzero PSD matrix. Then every PSD residual-t competitor satisfies

    X <= C D_t^2,
    |coefficient of H_j in P_K(X-X*)| <= C_j t^(gamma_j).

**Proof.** Write X-X*=H+E with H in K and ||E||<=t. Since every entry weight is at most one, D_t^(-1)(X*+E)D_t^(-1) is bounded. The scaled kernel subspaces converge to I because the B_j are independent. If D_t^(-1)X D_t^(-1) were unbounded along residual-t competitors, divide by its norm and take a subsequence. Its nonzero PSD limit would belong to I, a contradiction. This proves the Loewner bound. Uniform linear independence of the normalized basis gives bounded coefficients c_j t^(-gamma_j), hence the second assertion. The argument also works with a fixed constant times t in the residual. QED.

### 7.2 Independent leading forms

Assign degree w_i to H_i, degree eta_i=(w_(B_i.lower)+w_(B_i.upper))/2 to N_i, and degree alpha to G. Every generator has no entry whose weight exceeds its assigned degree. The normalized limits have independent pivots: the tight-real entry for H_i, the unique assigned blocker coordinate for N_i, and the unused real leading coordinate for G. Releases never occur at a blocker pivot, and the tight-real pivots are distinct. Thus all normalized limits are linearly independent.

The H_i limit contains E_i, its real tight entry, and possibly its imaginary release if that release is tight. The N_i limit contains E_i only when eta_i=w_i; otherwise it is a pure offdiagonal direction.

### 7.3 Explicit positive definite separator

Put z_i=exp(sigma w_i^2), z_0=1, and put z_i I on each grade block of W. On each tight-real coordinate put

    W_(P_i,real) = -m_i z_i/(2 lambda).

For a blocker with eta_i=w_i put the same value on its own coordinate; for a strictly safe blocker put zero there. Put zero on every release-imaginary coordinate, the optional leading coordinate, and all other entries. There is no assignment conflict by Section 5.

The real inner product of W with each leading form is zero: its diagonal contribution m_i z_i is cancelled by its unique tight or tight-blocker coordinate. A strictly safe blocker and G pair to zero separately.

After diagonal congruence by z_i^(-1/2) on every grade, each nonzero offdiagonal contribution has magnitude

    [m_i/(2 lambda)] exp(-sigma (w_a-w_b)^2/4),

because its midpoint equals w_i. There are finitely many such terms, and a<b have distinct weights. For sufficiently large fixed sigma, the normalized Hermitian matrix is strictly diagonally dominant with positive diagonal, hence positive definite. This assertion over H follows directly from bounding each cross term by 2|W_ab||x_a||x_b|. Therefore W>0 and I cap PSD={0}.

The exponential notation is not required for rational data. Take a common denominator Q for the weights, put z_i=B^((Qw_i)^2), and choose a sufficiently large positive integer B. All entries of W are then rational and the same strict dominance holds.

### 7.4 Upper bound, uniqueness, and sharp curve

The graded-separation lemma yields the coefficient bounds. All generator degrees are at least w_1 except the optional G at degree alpha. Consequently

    ||X-X*||_F = O(t^alpha)

for EVERY ambient PSD competitor. In particular exact feasibility forces X=X* by applying the bound for every t>0.

For the matching arc activate only the tight generators:

    X(t)=X* + sum_(i=1)^(k-1) t^(w_i) H_i + t E_k
                   + [t^alpha G if G is present].

Every null-grade diagonal is exactly t^(w_i) I, and the chosen source diagonal tends to one. The normalized real tight edges are O(lambda), and every release is O(lambda) or smaller since its midpoint is at most its child's degree. Finitely many shared releases contribute at most (k-1)lambda on one entry. Our small lambda makes the entire normalized matrix positive definite for small t. Its residual is exactly t||E_k||, because E_k is orthogonal to K. Its displacement is Theta(t^alpha), detected by the optional real leading entry or by the first null diagonal. Thus the exponent is exactly alpha.

This arc is also uniformly bounded below by cD_t^2. The canonical maximum-determinant envelope compares every residual-O(t) PSD matrix with a constant multiple of C_t, giving C_t>=c'D_t^2. The all-competitor upper bound applies to C_t itself, giving C_t<=C'D_t^2. Hence the claimed central grades and their multiplicities are exactly realized, not merely postulated.

## 8. Actual ambient exposing stresses and exact minimum degree

Let c=1/(2lambda). At the first step take Z_1=E_k. At a later stage t, let R_t=(0,j_(t-1)+1), and define the ambient Hermitian matrix

    Z_t = sum_(i in C_t) (1/m_i) E_i
          - c I_(R_t)
          - c sum_(i in C_t with N_i present) F_(B_i).

Every generator pairing vanishes exactly. The diagonal trace of H_i is one precisely for children in C_t, and its release-imaginary pairing is then -1; different layers use different releases. The blocker coordinates are independent of all tight-real and release-imaginary coordinates. A present N_i similarly pairs as 1-1 or 0. G uses an unassigned coordinate. Source diagonal terms pair with zero.

All displayed offdiagonal entries are OFF the current face W_(j_(t-1)): the release endpoint is j_(t-1)+1, and every current child's blocker endpoint is j_(t-2)>j_(t-1). Thus the current compression is exactly

    sum_(i in C_t) (1/m_i) E_i,

positive definite on the entire intended exposed group and zero elsewhere. There is no illegal extension of a compressed stress; the ambient Z_t has just been checked against every original kernel generator.

**Maximality at the first step.** A globally PSD stress annihilating X* has zero source rows. The equation for H_1 forces trace(S_11)=0. Inductively, the lower endpoint of P_i lies in an already zero group row, and the release touches the source. The equation for H_i forces trace(S_ii)=0. PSD then makes each whole group row vanish. Only U_k can be exposed, and Z_1 attains all of it.

**Maximality at later steps.** Suppose a PSD compressed stress exposes any vector in a future group i<=j_t. Choose the smallest such i with positive group trace. If N_i is present, both endpoints of B_i are still in the current face; its lower group i-1 has zero trace (or is the source), hence zero whole row. Its blocker entry vanishes, and the N_i equation forces the supposedly positive group trace to be zero. If N_i is omitted, then i=1 and H_1 uses only the real and imaginary source-to-b entries of the redundant collision. Before the final stage both entries are on-face and vanish by the source row, so H_1 again forces zero trace. Contradiction.

Therefore every valid compressed stress is supported inside the specified current layer. Z_t attains that whole layer. These are exactly the greedy faces, with rank drops sum_(i in C_t)m_i.

For completeness, maximal-rank greedy reduction has minimum length. Inductively its survivor F_t is contained in the survivor G_t of any other chain after the same number of steps. Compress the other chain's next PSD stress to F_t. It is a valid stress there, so the maximal greedy stress exposes at least its range. Positivity identifies a zero compressed quadratic form with membership in the original stress kernel. Thus F_(t+1) is contained in G_(t+1). Any shorter chain reaching the target face would force the greedy chain to have reached it too. This proves minimum degree d against arbitrary rotated chains, not only the displayed coordinate chains.

The k=1 cases are a fully observed singular target (alpha=1), or the same observed null block with an invisible source-to-null real entry (alpha=1/2). This completes Theorem 133.1. QED.

## 9. What has and has not been resolved

**Resolved uniformly:** every prescribed grade-prefix schedule over C and H, with a rational iff, arbitrary target rank and grade multiplicities, full-ambient sharp recovery, and exact minimum facial degree at the original nullity. Two real entry coordinates suffice; 134 proves that one does not suffice in general.

**Not resolved by this theorem:** the full real-PSD existence spectrum for an arbitrary prescribed rank-drop composition and alpha when the canonical central spectrum is allowed to vary; arbitrary non-prefix flags even over C; or an assertion that rank-profile information is independent of cone type. The last assertion is disproved in 134.

This result is not obtained by enumerating profiles. The proof supplies the same formulas and the same single collision argument for every k. Program 135 checks finite exact certificates as a supplementary audit, not as the proof.

## 10. Provenance and relation to the single paper

The prior real one-switch result 128 and the canonical spectral analysis in 132 remain unchanged. The present proof exploits the two real components of a Hermitian entry, rather than asserting a new universal real-kernel normal form. The aligned real bottleneck in 125 was the starting obstruction; 134 removes its alignment hypothesis for the example and gives the matching complex construction.

Classical facial-reduction and central-path background includes Sturm, *Error Bounds for Linear Matrix Inequalities*, SIAM J. Optim. 10 (2000), 1228–1248, DOI 10.1137/S1052623498338606; Sremac–Woerdeman–Wolkowicz, *Error Bounds and Singularity Degree in Semidefinite Programming*, SIAM J. Optim. 31 (2021), 812–836, DOI 10.1137/19M1289327; and Hu–Sotirov–Wolkowicz, *Facial reduction for symmetry reduced semidefinite and doubly nonnegative programs*, DOI 10.1007/s10107-022-01890-9. No bibliographic-priority certification is claimed.
