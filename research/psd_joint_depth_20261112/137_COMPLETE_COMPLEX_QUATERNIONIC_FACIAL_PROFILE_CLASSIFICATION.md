# 137 — Complete arithmetic classification of facial profiles over complex and quaternionic PSD cones

**Date:** 2026-11-12.  
**Branch:** `research/psd-joint-depth-universal-20261107`.  
**Dependencies:** the canonical monomial chart and half-weight theorem in 128/132, and the simultaneous-flag congruence reduction proved in 136.  
**Status:** complete research proof below; not independently refereed.  
**Scope:** every greedy rank-drop profile, including non-prefix flags and repeated grades split across several steps, for complex and quaternionic Hermitian PSD. The same arithmetic conditions are necessary for real PSD; their converse for fixed real central data is false. Whether changing the central data always permits a real realization of the same coarse exponent/profile tuple is NOT settled here.

## 1. The insight beyond the prefix construction

For an arbitrary facial schedule, the smallest previously removed weight need not change at every step. Reusing a source-release edge at several steps would couple their stress equations and invalidate the simple prefix argument.

There is a uniform repair. Let r be an already removed coordinate of minimum weight. A child i of smaller weight uses the source edge (0,r). A child of at least that weight instead uses the **self-release edge (r,i)**. The latter is off-face at the child's exposure and has midpoint at most the child's weight. Self-release edges are globally distinct. A source-release edge is shared only within one stage: as soon as it is used, that stage removes a smaller weight and the minimum strictly decreases.

Tight edges use real entry coordinates; releases use imaginary coordinates. Blockers use the unused coordinate. A blocker can never be a self-release edge, because their endpoint removal orders are opposite. The only possible three-way collision with a tight edge is a redundant source blocker, which can be deleted exactly as in 133.

These observations remove the prefix restriction and also handle repeated grades. The result is an exact finite integer-table classification, not a quantifier-elimination test.

## 2. Arithmetic data and theorem

Let F=C or H, and let H_n(F) have real inner product Re tr(XY). Measurements are real-linear. Fix target rank r>=1, nullity nu=n-r>=1, and a proposed greedy rank-drop profile

    s=(s_1,...,s_d),  s_t>=1,  sum_t s_t=nu.

The greedy procedure chooses a maximum-rank PSD compressed measurement stress at every step; its survivor face is unique. Its length is the minimum facial-reduction degree. The sharp exponent alpha is defined using the full-ambient Frobenius recovery modulus.

Choose k<=nu and a strict harmonic certificate

    0=w_0<w_1<...<w_k=1,
    2w_i=w_(a_i)+w_(b_i), 0<=a_i<i<b_i<=k, 1<=i<k.    (2.1)

Choose positive grade multiplicities m_1,...,m_k, with sum_i m_i=nu. A **survivor table** consists of integers x_i^t, i=1,...,k and t=0,...,d, such that

    x_i^0=m_i,  x_i^d=0,  0<=x_i^t<=x_i^(t-1),
    sum_i [x_i^(t-1)-x_i^t]=s_t.                       (2.2)

It specifies how many coordinates of grade i remain after each greedy step. Require the exact first exposure

    x_k^1=0,  x_i^1=m_i for i<k.                       (2.3)

For every t>=2 define

    b_t=max{i:x_i^(t-1)>0},
    a_t=min{i:x_i^(t-1)<m_i}.

Thus w_(b_t) is the greatest remaining weight before step t, and w_(a_t) the smallest weight removed before it. For each grade i with x_i^t>0, put

    p_t(i)=max({0} union {j<i:x_j^t>0}).

The two local arithmetic conditions are

    x_i^(t-1)>x_i^t  =>  2w_i >= w_(a_t),             (L)
    x_i^t>0         =>  2w_i <= w_(p_t(i))+w_(b_t).    (U)

Condition (U) implies that the entire greatest remaining grade is removed at each step. In particular d<=k. The analogous (U) inequality at the first step follows automatically from harmonicity and (2.3).

### Theorem 137.1 — full profile spectrum

For k>=2, the central weights w_i with multiplicities m_i, survivor table x, and sharp exponent alpha are simultaneously attainable in H_(r+nu)(C), and in H_(r+nu)(H), if and only if (2.1)–(2.3), (L), (U), and

    alpha=w_v/2<=w_1 for some v in {1,...,k}            (2.4)

hold. The greedy rank drops are exactly s, the minimum facial degree is d, and there is no rank or nullity overhead. All coefficients can be chosen rational in real and imaginary entry coordinates.

For k=1, the only profile is (nu), with d=1 and alpha in {1,1/2}. Consequently the complete fixed-(n,r,s) exponent spectrum over C and H is the finite union of the values in (2.4) over harmonic certificates, multiplicities and survivor tables satisfying the displayed arithmetic conditions, together with alpha=1 for the one-step profile.

The formula uses only integer tables and rational arithmetic. For fixed harmonic parents the weights solve a nonsingular integer linear system and are ratios of integer determinants. All searches in the formula are finite because k<=nu and each x_i^t lies between zero and m_i. No unknown real kernel or conic-feasibility predicate remains.

In particular, the full exponent/profile spectrum over C and H is independent of positive source rank r. This theorem is not a claim of the corresponding real-field converse.

## 3. Necessity for arbitrary dense kernels and arbitrary flags

Use 136 to make the central grade flag and the greedy survivor flag coordinate flags by one fixed congruence. This preserves central orders and multiplicities, sharp exponent, and the entire greedy profile. A grade may now have different coordinates removed at different times; the survivor table records their counts. There is no prefix assumption.

We recall the established central facts. The identity-shift maxdet center satisfies

    C_t ~ D_t^2,  D_t=diag(t^(theta_a/2)),

where theta_a is zero on the target support and w_i on grade i. For every internal grade i, the actual coefficient H_i of C_t at exponent w_i belongs to K=ker A, is positive definite on its whole grade, and has no entry between weights whose sum exceeds 2w_i. The dual curve Z_t=t C_t^(-1) belongs to K-perp, has a positive-definite first diagonal coefficient on grade i at order 1-w_i, and cross order at least 1-(w_i+w_j)/2. Every Puiseux coefficient of Z_t is an ambient measurement stress. The first maximum exposure is the entire grade k. Harmonicity and the half-weight formula were proved in 128/132.

### Proof of (L)

At a current coordinate face V, let mu be the smallest weight of any removed coordinate. If 2w_i<mu, every entry of H_i touching a removed coordinate is zero; thus H_i is supported inside V. All coordinates in grade i and all lower grades are still present, because their weights are below mu. Pairing successively with the positive leading coefficients on these grades forces their entire rows to vanish in any PSD exposing stress on V. Therefore no coordinate of a grade with 2w_i<mu can be removed. This is exactly (L).

### Proof of (U), including partially surviving grades

Let V be the current face, W its greedy survivor, and C=V cap W-perp the actual maximal exposed subspace. The coordinates are aligned with the grades, but C may contain only part of a grade. Let M be the largest weight in V. Suppose a surviving grade i violates (U), so

    2w_i > M+w_p,

where p is the largest strictly smaller grade still represented in W, or p=0. Take the actual dual Puiseux series, compress to V, and truncate through E=1-w_i. Every row in the lower surviving part of W is zero in this truncation: its possible cross order with any coordinate of V is at least

    1-(w_p+M)/2 > E.

On the part W_high of W with weights at least w_i, the leading diagonal coefficients are positive definite and all are included. The finite coefficient-rescaling lemma makes this compression positive definite on W_high. The lemma multiplies the coefficient at exponent e by exp(sigma e^2); after block normalization, a surviving cross term between different diagonal orders c_a,c_b gains exp(-sigma(c_a-c_b)^2/4). Within an equal-weight block the leading coefficient is already positive definite, so its principal compression to the surviving subspace is positive definite as well.

Call the resulting ambient stress T. Its compression is zero on the lower surviving rows and positive definite on W_high; its entries on C and between C and W_high can be arbitrary. Let S be an actual PSD stress positive definite on C, available by maximality. For sufficiently large fixed lambda, the compression of T+lambda S is positive definite on C+W_high and zero on the lower survivor. This follows from the block Schur complement, since the W_high block is already positive definite and the C block can be made arbitrarily positive. It is a valid stress exposing more than C, a contradiction.

Thus (U) is necessary. Taking i to be the greatest remaining grade shows that it cannot survive even partially, proving the useful top-grade assertion. Necessity is complete over R, C and H.

## 4. Choose coordinates for a permitted survivor table

For sufficiency, realize the table by an ordered partition C_1,...,C_d of the null coordinates. There are m_i coordinates of grade i, assigned weight theta_a=w_i. At stage t remove exactly m_i-x_i^t minus the number previously removed in that grade; the particular labels do not matter. Fix a total order on null coordinates by increasing weight and then by their labels. Let S_t be the surviving coordinate set after step t, including the source representative o=0. Let t(a) be the removal time of coordinate a. All terminal-grade coordinates form C_1.

Choose one representative coordinate from every grade, and a source representative 0. The harmonic pair for grade i gives a tight physical edge P_i between the representatives of grades a_i and b_i. All coordinates in the same grade use that same tight edge. Tight physical edges belonging to distinct grades are distinct, because their midpoint weights differ.

For every internal coordinate a (not in grade k), put t=t(a)>=2. Let q_t be a previously removed coordinate of smallest weight, breaking ties by earliest removal time and then by label. In particular the same q_t is retained while the smallest removed weight does not decrease. Define its release edge by

    R_a=(0,q_t)            if theta_a<theta_(q_t),
    R_a={q_t,a}            if theta_a>=theta_(q_t).    (4.1)

The braces denote an unordered physical pair. The second case is the self-release edge. In the first case, (L) gives theta_(q_t)/2<=theta_a. In the second, the edge midpoint is at most theta_a directly. Every release is off-face at the child's exposure.

Let p_a be the immediate predecessor of a in the fixed total order restricted to S_(t-1), with predecessor 0 allowed. Let b_a be one fixed representative of the greatest-weight grade in S_(t-2). Define

    B_a={p_a,b_a}.                                    (4.2)

The greatest grade is removed at step t-1, so

    theta_(p_a)<=theta_a<theta_(b_a).

If p_a has the same weight as a, the blocker is strictly safe. Otherwise (U) at step t-1 gives

    theta_(p_a)+theta_(b_a)>=2theta_a.                 (4.3)

At the first transition the same inequality follows from harmonicity. The blocker is on-face at every earlier step and becomes off-face precisely at the child's prescribed step.

Blocker physical edges are globally distinct. At a common removal time the predecessor map is injective. At different removal times their larger-weight endpoints belong to different successively removed maximum grades. No ambiguity is introduced by equal weights inside a grade.

## 5. Release ownership and the only exceptional collision

### Lemma 5.1 — a release coordinate belongs to one stage

A self-release pair {q_t,a} is unique: its first endpoint has already been removed when its child a is exposed. Reversing their roles in another release would require both t(q_t)<t(a) and t(a)<t(q_t). It is never a source-release pair, since both endpoints are null coordinates.

A source-release pair (0,q_t) can be shared by several children of the same stage. When it is used, at least one child has weight strictly below theta_(q_t). The minimum removed weight therefore strictly decreases after that stage, so the same source-release pair is never used at a later stage. Before that stage, if the minimum had already been q_t, only self-releases were used. Thus every release pair is assigned to exactly one stage. QED.

Put each tight edge in its REAL coordinate, and every release in its IMAGINARY coordinate. For a blocker B_a use the real coordinate if B_a is not a tight physical edge; otherwise use the imaginary coordinate, unless it is also a release pair.

### Lemma 5.2 — a triple collision is a redundant source blocker

A blocker cannot equal a self-release pair. The larger-weight endpoint of a blocker is removed before its child, while its lower endpoint survives to the child's stage. For a self-release pair the lower-or-equal-weight endpoint was removed before the higher-or-equal-weight child endpoint. These orders are incompatible. If both self-release endpoint weights are equal, they cannot be a blocker because its upper weight is strictly larger than its child's weight and its lower weight is at most that weight.

Suppose B_a is both a tight physical edge and a source-release pair (0,q). Then p_a=0 and q=b_a is removed at step t(a)-1. The source-release stage u satisfies u>=t(a). If u>t(a), coordinate a, which is removed at step t(a) and has theta_a<theta_q, would lower the minimum removed weight before u, contradicting the use of q there. Hence u=t(a). The blocker inequality and (L) at this stage give

    theta_a <= theta_q/2 <= theta_a.

Thus theta_a=theta_q/2. Since the tight owner of B_a has that midpoint, it belongs to the same grade as a, and all coordinates of this grade use the same physical tight edge. Therefore

    P_(grade(a))=B_a=R_a=(0,q).

The generator for a already uses both real and imaginary coordinates of this source pair. Before its intended step, q remains on-face, so a PSD stress annihilating the source must have both entries zero and hence forces the child's diagonal to vanish. Its separate blocker is redundant and is omitted. QED.

Every surviving blocker coordinate is now globally unique and is not any tight-real or release-imaginary coordinate. The only deleted blockers are certified by Lemma 5.2. No unsupported identification of independent coefficients is made.

## 6. Rational matrices realizing the table

For a physical pair u<v write

    R_uv=e_u e_v*+e_v e_u*,
    I_uv=i e_u e_v*-i e_v e_u*.

These are orthogonal real coordinates of squared norm two. Over H use one fixed imaginary unit i, and measure all other components. Choose a rational lambda>0 sufficiently small, for example lambda=1/[100(r+nu)^2]. Let X*=diag(I_r,0).

For every internal null coordinate a use

    H_a=E_aa-E_00+lambda R_(P_grade(a))+lambda I_(R_a). (6.1)

For every nonomitted blocker use

    N_a=E_aa-E_00+lambda F_(B_a),                      (6.2)

where F is its assigned real or imaginary entry coordinate. If alpha=w_v/2<w_1, also use

    G=lambda R_(0,rep(v)).                            (6.3)

The latter real coordinate is unused by tight and blocker entries: its weight is alpha<w_1, while all tight and blocker weights are at least w_1. A release on the same physical pair is imaginary and is therefore independent.

Let K be the real span of these matrices and A=P_(K-perp). All generators have trace zero and zero terminal diagonal. Multiple children of one grade may share the same tight real pivot; their distinct diagonal coordinates will give linear independence. No coordinate cloning is used: the order is exactly r+nu.

## 7. Full-ambient exponent and exact central multiplicities

Assign degree theta_a to H_a, midpoint eta(B_a)>=theta_a to N_a, and alpha to G. Normalize a generator of degree gamma as t^gamma D_t^(-1) H D_t^(-1).

The limiting generators are linearly independent. Each N_a has a unique blocker coordinate absent from all H-generators and all other blockers. G has its own unique real coordinate. After eliminating these, each remaining H_a has a unique null diagonal E_aa, even when its tight edge is shared with other children of the same grade.

Their limiting span has an explicit positive definite separator. Set the diagonal at every coordinate of grade i to

    z_i=exp(sigma w_i^2),

and the source diagonals to one. At the tight real edge of grade i put -z_i/(2lambda). All children sharing that edge have the same weight, so the assignment is consistent. At a blocker coordinate whose midpoint equals its child's weight put -z_i/(2lambda); at a strictly safe blocker put zero. Put every release-imaginary coordinate and the optional G coordinate equal to zero. Lemma 5.2 guarantees that none of these assignments conflict.

Each leading generator pairs to zero with this separator. An equal-weight self-release may survive in a leading form, but its separator entry is zero and so causes no problem. Every NONZERO offdiagonal separator entry joins two distinct weights with midpoint w_i. After diagonal congruence its magnitude is a fixed constant times

    exp(-sigma(w_u-w_v)^2/4).

For sufficiently large fixed sigma, strict diagonal dominance gives a positive definite Hermitian separator W. The argument also proves quaternionic positivity by bounding each cross term with its quaternionic norm. Rational powers of a sufficiently large integer can replace the exponential notation. Thus the limiting scaled kernel contains no nonzero PSD element.

We spell out the all-competitor consequence. For any PSD X with residual at most t, write X-X*=H+E, H in K and ||E||<=t. The normalized X*+E is bounded, because all coordinate weights lie in [0,1]. If D_t^(-1) X D_t^(-1) were unbounded, division by its norm and passage to a subsequence would give a nonzero PSD matrix in the limiting scaled kernel. The separator excludes this. Hence X<=C D_t^2. Uniform independence of the normalized generator basis bounds each generator coefficient by its assigned power of t. Therefore

    ||X-X*||_F=O(t^alpha)                              (7.1)

for EVERY ambient complex or quaternionic PSD competitor. Taking t to zero establishes uniqueness.

For sharpness activate only the H-generators:

    X(t)=X*+sum_(a internal) t^(theta_a)H_a
             +t I_terminal+[t^alpha G if present].    (7.2)

Each null diagonal is exactly its prescribed t^theta_a, while the selected source diagonal tends to one. Every normalized offdiagonal is bounded by a constant multiple of (r+nu)lambda; shared tight or source-release entries contribute only finitely many such terms. Our small lambda gives positive definiteness and a uniform lower bound cD_t^2 for small t. The residual is exactly t||I_terminal||, and displacement is Theta(t^alpha).

The maxdet envelope transfers this thick lower bound to the actual center. The all-competitor bound applies to the center itself and gives its upper bound. Thus C_t~D_t^2, with exactly the required grade multiplicities and full primal/dual eigenvalue orders. This proves the claimed sharp exponent and spectrum.

## 8. Exact ambient stresses and greedy maximality

Let c=1/(2lambda). Take Z_1=I_terminal. At step t>=2 put

    Z_t=sum_(a in C_t) E_aa
        -c sum_(distinct release pairs e assigned to C_t) I_e
        -c sum_(a in C_t with blocker present) F_(B_a). (8.1)

All generator pairings are zero. A tight-real entry is never assigned by a release or a blocker. Each release-imaginary coordinate belongs to precisely the current stage, where it cancels the unit diagonal pairing of each child using it. Each blocker coordinate is unique and cancels its own unit diagonal pairing. G is on an unused real coordinate. Thus Z_t belongs to the orthogonal complement of the ORIGINAL kernel.

Every displayed offdiagonal of Z_t is off the current face. A release has an already removed endpoint; the blocker's upper endpoint was removed at the previous stage. The compressed stress is therefore exactly the identity on C_t, extended by zero to the other current coordinates. It exposes the whole prescribed layer.

For maximality, consider any PSD compressed stress and choose the first future null coordinate a in the fixed total order with positive diagonal. If N_a is present, its lower blocker endpoint p_a is an earlier future coordinate or the source, and therefore has zero entire row. Its upper endpoint is still on the current face, because it is removed only at step t(a)-1. The N_a equation forces the positive diagonal at a to vanish, a contradiction. If N_a is omitted, Lemma 5.2 gives a source pair which is still on-face at every earlier stage; both its real and imaginary entries vanish, and H_a again forces zero diagonal.

The same argument at the initial face kills every internal coordinate, leaving exactly the whole terminal grade. Thus at every stage all valid stresses are supported on the prescribed layer, and (8.1) attains it. The displayed flag is the actual greedy flag, not merely one permissible chain.

Maximum-rank greedy reduction has minimum length. To recall the argument, compare it with any chain. After each equal number of steps, the greedy survivor is contained in the other survivor. Compress the other chain's next stress to the greedy survivor; it is valid there, and the maximum greedy stress exposes at least its range. For PSD forms a zero quadratic form means membership in the kernel, completing the induction. A shorter competing chain reaching the target face would imply the greedy chain had also reached it. Hence the degree is exactly d.

This completes the constructive sufficiency and Theorem 137.1. QED.

## 9. What this solves and what remains real

This theorem classifies **every** joint central-order/multiplicity/greedy-profile/exponent datum over C and H, including non-prefix flags and grades split across several stages. Via the finite union in Section 2 it also classifies every coarse `(n,r,s_1,...,s_d,alpha)` tuple over those fields. The proof is the same for every dimension.

It supplies universal arithmetic necessity over R. The fixed-central-data real converse is false: 134 proves a real rank-one obstruction for the weight vector `(1/4,3/7,1/2,17/28,5/7,1)` and profile `(1,2,2,1)`, while the construction above realizes those data over C. That obstruction does not automatically rule out a real realization of the same coarse exponent/profile tuple using DIFFERENT weights. No such coarse real equivalence or non-equivalence is asserted here.

The remaining real classification must resolve precisely that real realization problem. Milestone 136 shows that rotations can be eliminated by congruence; they are not an extra continuous flag parameter. What remains is the signed/positive kernel realization of the admissible discrete tables, or a proof that replacing their weights preserves the desired coarse real tuple. This manuscript is not presented as a full real-profile solution.

The bounded-set gauge reduction in 132 preserves every facial chain and the sharp error exponent. It consequently transports the complex/quaternionic classification to nonempty affine sections in the corresponding bounded-set error-bound sense. It does not change the field limitation just stated.

## 10. Audit and relation to the paper

The finite exact audit in 138 checks the construction, original-generator/stress pairings, independent leading forms, symbolic positive separation, every collision exception, and the maximality premises. It includes repeated grades split across steps. These finite checks supplement the proof and are not its basis.

The elementary simultaneous splitting of flags and standard facial-reduction facts are classical. The novel-content claim requiring external priority review is the complete arithmetic realization criterion and this uniform self-release/two-channel construction. The background comparison remains the maxdet/singularity-degree literature listed in 132. This is one structural continuation of the same paper, not a separate application program.
