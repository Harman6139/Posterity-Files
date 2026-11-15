# Milestone 22 — bounded dynamic range does not prevent exponential PSD rank

Date: 2026-11-13. This converts the robust smooth-body lower bound of 21 into a finite rational matrix theorem and a consequence for exact correlation generation. It also supplies a matching exponential upper bound for every bounded-entry matrix, by an elementary normed-space covering argument.

The lower family is existential with an inefficient computable selection, not an efficiently generated explicit standard combinatorial instance. The theorem concerns EXACT PSD factorizations. No constant entrywise-approximate PSD-rank bound is inferred. Bounded dynamic range means a bound on largest entry divided by smallest entry; it does NOT mean a bound on a spectral condition number, and the matrices have low ordinary rank.

Classical PSD-rank/slack-sandwich and correlation interpretations are acknowledged below. No named open conjecture is claimed solved and no historical priority for the combined bounded-entry statement is certified.

## 1. A sharp exponential-order separation

Put

    eta=2^(-24), K_star=3/eta=50,331,648.

For a finite nonnegative real matrix M, rank_psd,R(M) is the minimum d such that M_ij=tr(A_i B_j) for real d-by-d PSD factors. Define rank_+(M) by nonnegative vector factorizations. The elementary diagonal embedding gives rank_psd,R(M)<=rank_+(M).

**Theorem A.** For every integer r>=17 there is a finite rational matrix M_r satisfying

    rank(M_r)=r,
    1<= (M_r)_ij <=K_star,
    rank_psd,R(M_r)> floor(2^((r-1)/4)).                   (1)

Both row and column counts can be at most 2^(30(r-1)); every entry has rational numerator and denominator of O(log r) bits, with absolute implicit constants. Duplicating rows or columns makes the matrix square without changing any of these rank statements.

Conversely, for EVERY finite matrix M of ordinary rank r with entries in [1,K], K>=1,

    rank_psd,R(M)<=rank_+(M)
                 <= [5(1+8K)]^r <=(45K)^r.               (2)

Consequently, for the fixed absolute dynamic-range bound K_star,

    sup{rank_psd,R(M):rank(M)=r, 1<=M_ij<=K_star}
                   =2^(Theta(r)).                       (3)

The upper and lower exponential bases are not asserted sharp. Statement (3) identifies the exponential order, not an exact value of the supremum. Positive row/column scaling does not change PSD rank; no zero entries, divergent entry ratios, or real-number precision with growing per-entry bit length are needed for the separation.

## 2. The rational matrix lower bound

Fix n=r-1>=16 and take the body C_n from 21. We use only

    B_2 subset C_n subset 2 B_2,

and the fact that every body within epsilon_star=2^(-19) has single PSD order greater than floor(2^(n/4)).

### 2.1 Rational finite nets with bounded cardinality and bits

Choose finite rational eta-nets

    X={x_i} subset C_n,
    Y={y_j} subset C_n^polar.

Include 0 and +/-e_l/2 in X, and 0 and +/-e_l/4 in Y, for l=1,...,n. These points are valid because B_2 is contained in C_n and (1/2)B_2 is contained in its polar. The origin is interior to both finite convex hulls.

These nets can be chosen with all coordinates on the common grid

    qgrid^(-1) Z, qgrid=2^28 n,

and with each cardinality at most 2^(30n). Here is a proof rather than an assumption of boundary rationality.

Take a maximal eta/4-separated net in C_n. The disjoint radius-eta/8 balls about its points lie in the ball of radius 2+eta/8, giving at most (1+16/eta)^n points. The polar admits the analogous bound since it is in B_2. Shrink each point by the rational factor 1-eta/16. Convexity and the inner ball create a buffer eta/16 for C_n and eta/32 for its polar. Round to the nearest qgrid grid point. The Euclidean rounding error is at most

    sqrt(n)/(2qgrid)=eta/(32sqrt(n))<=eta/32.

The rounded points remain in the respective sets. The net error is at most eta/4+eta/8+eta/32<eta. Appending the stated spanning points preserves the bound 2^(30n) for n>=16. Every coordinate has O(log n) bits because absolute coordinate magnitude is at most two and the grid denominator is 2^28 n.

Shrink once more:

    x_i'=(1-eta)x_i, y_j'=(1-eta)y_j,
    S_ij=1-x_i'.y_j', M_r=S/eta.                         (4)

Since x_i.y_j<=1, and ||x_i||<=2, ||y_j||<=1,

    eta<=2eta-eta^2<=S_ij<=3.

Thus M_r has entries in [1,K_star]. All entries are rational with O(log n) bits: the dot products share denominator qgrid^2; the extra factors are fixed dyadic numbers, and the dot products are bounded by two in magnitude.

### 2.2 Exact ordinary rank

Formula (4) gives rank S<=n+1. Consider the submatrix on rows 0,e_1/2,...,e_n/2 and columns 0,e_1/4,...,e_n/4. Its first row and column are all ones, and its remaining block is

    1_(n x n) - [(1-eta)^2/8] I_n.

Subtracting the first row from each other row leaves a nonsingular diagonal n-by-n block. Hence rank S=n+1=r. Scaling by eta^{-1} does not change rank.

### 2.3 A small PSD factorization would approximate the hard body

Suppose S has an order-d PSD factorization. Define

    P=conv{x_i'},
    Q={z:y_j'.z<=1 for every j}.

The classical finite slack-sandwich theorem gives a convex body K with

    P subset K subset Q, sxc(K)<=d.                       (5)

For clarity, no closure assumption is hidden in this step. Write S_ij=tr(A_i B_j), and choose positive weights lambda_j summing to one with sum_j lambda_j y_j'=0. Such weights exist because 0 is interior to conv Y'. Compress all factors to the span of the ranges of the B_j. Then T=sum_j lambda_j B_j is positive definite. Set

    K={z:exists Z>=0, tr(B_j Z)=1-y_j'.z for all j}.

The row factors show P subset K; positivity shows K subset Q. Summing the equations gives tr(TZ)=1, so Z is bounded. Q is bounded because 0 is interior to conv Y'. Therefore K is compact and full-dimensional. This proves (5) at the SAME PSD order.

Now every point c in C_n is within 3eta of P: choose x_i within eta and use ||x_i-(1-eta)x_i||<=2eta. Also Y' is a 2eta-net of C_n^polar. For z in Q, support duality and the outer-net calculation give

    dist(z,C_n)<= 8eta/(1-4eta)<16eta.

Explicitly, choosing a net point near z/(2||z||) shows ||z||<=2/(1-4eta). For arbitrary y in C_n^polar, the net then gives y.z<=1+2eta||z||. Hence z/(1+2eta||z||) is in C_n, and the displayed bound follows by subtraction.

Thus every intermediate K in (5) obeys

    d_H(K,C_n)<=16eta=epsilon_star/2.

The hard-body theorem of 21 forces d>floor(2^(n/4)). This proves the lower bound in (1). Since global positive scaling preserves PSD rank, it also holds for M_r.

No explicit polynomial P_n or its factorization needs to be recovered from the matrix to prove this contradiction. The existence of the body and finite rational nets is enough. The efficient specification of the matrix family remains a separate issue; its full table may have exponentially many entries.

## 3. Universal exponential upper bound at fixed entry ratio

Let L be the r-dimensional row span of M in R^b, where b is its column count. Let

    B=L intersect [-1,1]^b.

This is the unit ball for the restricted infinity norm. Every row lies in K B and has every coordinate at least one.

Choose a maximal 1/4-separated subset of the rows, with centers z_1,...,z_N in this norm. It covers all rows by translates z_j+(1/4)B. The open translates z_j+(1/8)int B are disjoint and lie in (K+1/8)B. Comparing r-dimensional volumes gives

    N<=(1+8K)^r.                                        (6)

Choose a 1/2-net U in B of size at most 5^r, by the same volume argument using a maximal 1/2-separated set and disjoint radius-1/4 balls. It satisfies

    (1/2)B subset conv U.                                (7)

Indeed, for any linear functional f on L, select b in B maximizing f and u in the net within 1/2 in B norm. Then f(u)>=f(b)-(1/2)h_B(f)=(1/2)h_B(f). The support-function inequality proves (7).

Therefore

    z_j+(1/4)B subset z_j+(1/2)conv U.

Every row of M is a convex combination of the fixed vectors

    z_j+(1/2)u, j=1,...,N, u in U.

Each such vector has every coordinate at least 1-1/2=1/2, and is therefore nonnegative. Listing them as rows of a matrix and the convex-combination weights as a nonnegative matrix gives a nonnegative factorization of width at most N|U|. This proves (2), independently of the row and column counts. Diagonal PSD factors give the stated PSD upper bound.

This elementary upper bound also explains why some quantitative control of entry ratio matters: unbounded ordinary-versus-nonnegative rank separations at a fixed rank require losing this fixed positive entry window. It does not imply a useful polynomial bound in r for fixed K, and Theorem A shows exponential growth is necessary for one fixed K.

## 4. Exact correlation generation with bounded mutual information

Normalize the lower-bound matrix into a joint probability table

    p_ij=(M_r)_ij / sum_(a,b)(M_r)_ab.

If its row and column counts are a,b, then

    1/(K_star ab)<=p_ij<=K_star/(ab).                    (8)

Thus all events have positive probability, within a fixed factor of the uniform joint table. Its ordinary matrix rank is r. Using base-two entropy, its mutual information obeys

    I(I:J)<=log_2 K_star.                               (9)

Proof: D(p||Unif_a times Unif_b)<=log_2 K_star by the upper bound in (8), and the exact identity

    D(p||Unif_a times Unif_b)
       = I(I:J)+D(p_I||Unif_a)+D(p_J||Unif_b)

gives (9).

Suppose this distribution is produced exactly by local measurements on a shared quantum state rho on C^(D_A) tensor C^(D_B), without communication or additional uncounted shared randomness. The state may be mixed and the local measurements arbitrary POVMs. If E_i,F_j are their effects, define

    P_i=Tr_A[(sqrt(E_i) tensor I) rho (sqrt(E_i) tensor I)].

Then P_i>=0 of order D_B, and p_ij=tr(P_i F_j). Hence

    rank_psd,C(p)<=D_B,

and the symmetric argument gives the same bound with D_A. Here rank_psd,C uses complex Hermitian factors.

Realification of a complex order-D factorization gives a real order-2D factorization: for a Hermitian matrix H let

    R(H)=[[Re H,-Im H],[Im H,Re H]].

It is real PSD when H is Hermitian PSD, and tr(R(H)R(G))=2tr(HG). Scaling one factor by 1/2 preserves the desired pairing. Thus

    rank_psd,R(p)<=2 rank_psd,C(p).

Theorem A now forces

    D_A,D_B > (1/2) floor(2^((r-1)/4)).                  (10)

Each party therefore needs a local quantum memory of Omega(r) qubits for exact generation, even though mutual information is bounded by the absolute constant log_2 K_star and the ordinary rank is only r. A classical shared-randomness mixture similarly needs at least rank_+(p)>=rank_psd,R(p) values of its shared variable.

This is an exact-generation dimension lower bound, not a lower bound for approximate generation or arbitrary protocols with communication. Free extra shared randomness would change the counted resource and is explicitly excluded. Correlation/PSD-rank interpretations are classical; the argument is included to make the operational implication and its limitations precise.

## 5. What the theorem does and does not settle

- It proves exponentially large EXACT PSD rank with an absolute positive entry window and O(log r)-bit rational entries, and a matching exponential-order universal upper bound for such windows.
- The lower construction is existential through 21 and rational nets. No efficient explicit family, new communication-complexity conjecture resolution, or computational hardness class is claimed.
- Approximate body hardness in 21 is robust at a constant Hausdorff tolerance. It does not automatically imply constant entrywise approximate PSD-rank hardness of M_r; the theorem here is exact and makes no such inference.
- No spectral condition-number claim is made. Dynamic range is an entrywise quantity; an ordinary rank-r matrix with more than r rows is spectrally singular.
- The main antecedents are the slack/sandwich factorization theorem and classical counting lower bounds. The use of the smooth robust body family and the explicit finite-window quantitative synthesis is proved here; comprehensive historical priority has not been established.

Primary background: Gouveia–Parrilo–Thomas, arXiv:1111.3164; Fawzi–Gouveia–Parrilo–Robinson–Thomas, Positive Semidefinite Rank, arXiv:1407.4095; Briet–Dadush–Pokutta, arXiv:1305.3268; Averkov–Kaibel–Weltge, arXiv:1605.08538. Milestones 20–21 provide all new compact-shadow entropy and regular-body facts used in the lower proof.