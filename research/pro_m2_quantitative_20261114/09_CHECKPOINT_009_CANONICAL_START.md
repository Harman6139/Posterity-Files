# Checkpoint 009 — canonical initialization also has exponential paths

Project date: 2026-11-14. This strengthens the lower-bound theorem: in every n>=5 the UNMODIFIED minimum-ratio shadow algorithm, started at the canonical tridiagonal T_n, has exponential paths on positive definite, strictly entrywise-positive nonmembers. The proof certifies an interval of normal cones and does not enumerate the preceding trajectory. The corrected-grid interface is forced to descend throughout the certified interval; this checkpoint does NOT prove that an additional corrected-grid test cannot stop during the earlier, uncertified prefix. Checkpoints 006–007 already give full grid-robust lower bounds from the fixed shear initialization.

## 1. Data and theorem

Let n>=5, r=n-1, t=3/5, and choose an integer K>=2^20 n^6. Put

    N=2^20 n^6 K^2,
    a1=r(5n+4)/10,
    a2=r^2+5r/8-1,
    gamma1=(2/n)(1-a1/K),
    gamma2=(2/n)(2-a2/K).

Both gamma parameters are in (0,1), and min(gamma1,gamma2)>=1/n. On the cycle of coordinates (3,1,2,4,n), take F=I_5+t Adj(C_5), scaled respectively by (N,gamma1,gamma2,N,1). Put N^2 on every remaining diagonal and zero in the other entries. Call the resulting matrix B. The normalized input is A=B/(nN^2).

The starting matrix T_n has diagonal one, adjacent off-diagonal entries -1/2 and other entries zero. Its prescribed anchor is

    (C0)_ij=min(i,j)(n+1-max(i,j)),  1<=i,j<=n.

Set m=K+floor(K/(100n^2)). The unmodified minimum-ratio algorithm must traverse the consecutive edges

    P_(K-1) -> P_K -> ... -> P_m,

where P_k is the known shear vertex from checkpoint 002. Every choice in this window is unique. There are m-K+1>=K/(100n^2) pivots in the window, regardless of the preceding path or degeneracies there.

The input is positive definite and entrywise nonnegative, has Frobenius norm at most one, and satisfies

    dist_F(A,CP_n)>=1/(5n^3 N^2).

Moreover, with epsilon=1/(2^20 n^6 N^4), the input

    A'=(B+epsilon J_n)/(2nN^2)

is strictly entrywise positive, positive definite, has the same forced window, and satisfies dist_F(A',CP_n)>=1/(20n^3 N^2). For fixed n, H=O_n(log K), while the window has Omega_n(K) pivots. Thus the canonical initialization itself has exponential binary-precision complexity in every n>=5.

## 2. Target normal matrices

Write E for the upper-left r by r block of C0. Its cross-column entries are h_i=i, its last diagonal is n, and its cross-column sum is b0=nr/2. For every integer K<=s<=m put

    lambda_s=(ns-b0)/(2tN-s),
    C_s=C0+lambda_s B.

The parameters are strictly increasing in s. The retained active normals of R_(s-1) are the axes e_i and all (u,1) with nonnegative integer u summing to s. We construct a strictly positive representation using axes, all concentrated compositions, and a two-coordinate composition for every pair. Their common annihilator is exactly the line of R_(s-1), as proved in checkpoint 006.

Let the small coordinates be J={1,2}, the large coordinates L={3,...,r}, and the cycle pairs be (3,1),(4,2). Put T=16n^2. All pair vectors below have last coordinate one.

## 3. Pair atoms and positive means

For every i in L and j in J, include

    u=(s-T)e_i+T e_j, weight E_ij/[T(s-T)].

For the two cycle pairs, also include

    u=(s-1)e_i+e_j, weight lambda_s tN gamma_j/(s-1).

For every pair i,j in L, put p=floor(s/2), q=s-p and use both p e_i+q e_j and q e_i+p e_j, each with weight E_ij/(2pq).

For the small pair put p=floor(4s/9), q=s-p and use p e_1+q e_2 with weight (E_12+lambda_s t gamma1 gamma2)/(pq).

These atoms reproduce every upper off-diagonal entry of C_s. Denote their i-th mean contribution by L_i, and write h'_i=(C_s)_in. We prove h'_i-L_i>0, then add s e_i with weight (h'_i-L_i)/s. Since sum_i h'_i=s(C_s)_nn, the bottom diagonal is then correct automatically.

For large i, the baseline large-small mean is at most 2n^2/T=1/8. The large-large mean is at most 3n^3/s. The only additional mean is lambda_s tN gamma_j on a cycle coordinate, whose available extra mean is lambda_s tN. Hence

    h'_i-L_i >= i-1/8-3n^3/s
                 +1_(i is a cycle coordinate)lambda_s tN(1-gamma_j)>2.

For small j, put d_j=a_j/K, so gamma_j=2(h_j-d_j)/n, and note the exact identity

    lambda_s tN gamma_j=(h_j-d_j)(s-r/2)+(gamma_j/2)lambda_s s.

The top off-diagonal row sums of the canonical anchor are

    Q1=nr/2-1,    Q2=r^2-2,    E12=r.

For the small-pair means use 1/q<=9/(5s) and 1/p<=9/(4s)+7/s^2. The baseline large-small means obey

    sum_(i in L) E_ij/(s-T)
       <= (sum_(i in L) E_ij)/s + 32n^4/s^2.

Consequently, with

    M1=r(5n+3)/10,
    M2=r(4n-3)/4,

we have

    (s-1)(h_j-L_j)
      >= d_j(s-r/2)-M_j
           -(gamma_j/2)lambda_s s
           -3lambda_s-52n^4/s.

The inequalities lambda_s<=ns/N, s<=2K, a_j<=n^2 and K>=2^20 n^6 bound all error terms, including a_j r/(2K), by less than 1/16. Define

    D1=r(n+1)/2,
    D2=r^2+r-2.

Then a_j=(M_j+D_j)/2 and

    D1-M1=r/5>=4/5,
    D2-M2=3r/4-2>=1.

It follows that (s-1)(h_j-L_j)>=1/4 and hence every small mean residual is at least 1/(8K).

## 4. Positive diagonal completion

Add the axis e_i with coefficient

    chi_i=(C_s)_ii-s(C_s)_in+sum_(j!=i) (C_s)_ij.

For a small coordinate j, substitution gives

    chi_j=D_j-d_j(s-r/2)
            +lambda_s[(gamma_j/2)s+gamma_j^2+t gamma1 gamma2].

Since s/K<=1+1/(100n^2), this is at least

    (D_j-M_j)/2-a_j/(100n^2)>1/4.

For a large coordinate, the lambda coefficient is either N^2 or
N^2-tNs+tN gamma_j, and is at least N^2/2. Also lambda_s>=5ns/(12N). Thus chi_i is positive (indeed greater than one), since its only negative anchor term is -si and i<=n.

Every required normal now has a positive coefficient. Therefore C_s lies in the relative interior of the normal cone of the single edge [P_(s-1),P_s]. In particular, P_(s-1) and P_s are exactly its minimizing vertices and R_(s-1) is the unique zero-cost feasible ray at P_(s-1).

## 5. Why the canonical shadow path must enter and cross the window

The preceding positive representation also proves C_s is in the interior of CP_n. Indeed, if Q in COP_n has <C_s,Q>=0, the positive top-axis terms force Q_ii=0 for all i<=r. Copositivity then makes every entry in those rows nonnegative. The concentrated (s e_i,1) terms force Q_in=Q_nn=0, and the pair terms force every Q_ij=0. Thus Q=0, proving strict positivity on the nonzero dual cone.

For lambda between consecutive lambda_s and lambda_(s+1), the matrix C0+lambda B is a strict convex combination of C_s and C_(s+1). Its optimal face is the intersection of the two adjacent optimal edges, namely the single vertex P_s. Thus these are genuine consecutive intervals of the parametric minimization problem, not merely isolated feasible normal certificates.

The entire segment from C0 to C_m lies in int CP_n. A copositive-ray termination before lambda_m is impossible, because its selected ray has zero pairing with the current normal matrix. A vertex termination is also impossible there: objective values of minimizers are nonincreasing with the parameter, while a future minimizing shear vertex is positive semidefinite and B is positive definite, so its B-pairing is positive. Every earlier minimizing vertex has at least that positive pairing.

The shadow invariant and finite-termination theorem therefore force the path past this window. It cannot jump across an open parameter interval whose unique optimizer is P_s. At lambda_s the only edge in the optimal face is [P_(s-1),P_s], and its B-pairing is -2(2tN-s)<0. The selected ratio is uniquely lambda_s. This proves every claimed transition without knowing the preceding path.

## 6. Strict positivity and distance

Positive definiteness and the Horn separator are the same diagonal-congruence argument as in checkpoint 006. Since gamma_j>=1/n, the inverse-congruence Horn separator W has norm at most 5n^2 and <B,W>=-1. This gives the stated distance bound.

For B'=B+epsilon J, replace lambda_s by

    lambda'_s=(ns-b0)/[2tN-s+epsilon(r-s)].

Writing C'_s=C0+lambda'_s B', elementary denominator estimates give

    max_ij |(C'_s-C_s)_ij|
       <=32nK^2 epsilon
       <=Delta:=1/(2^15 n^5 K^6).

Use the same atom decomposition, keeping the fixed baseline E_ij on the two cycle pairs and assigning their remaining positive off-diagonal value to the extra cycle atom. On other pairs use the perturbed off-diagonal value. Each remaining-mean functional has coefficient sum at most 2n+1, so its perturbation is at most (2n+1)Delta<1/(16K). Each diagonal-completion coefficient changes by at most (s+n)Delta<=3KDelta<1/8. The positive margins proved above therefore persist. The normal-window argument is unchanged.

Finally |<epsilon J,W>|<=5n^3 epsilon<1/2, and ||B'||_F<=2nN^2. This proves strict positivity, normalization, nonmembership and the distance bound for A'.

## 7. Grid-interface qualification

On every certified window edge, beta=[sum_i B_in-s B_nn]/tr(B) is at most 1/N, and s<=N/5. Thus beta(2s+beta)<1. The same shell witness as in checkpoint 006 proves that the prescribed corrected-grid test must descend throughout the window, if it reaches it. An earlier corrected-grid separator has NOT been ruled out for the unknown prefix from T_n. This distinction is deliberate: the canonical lower bound here concerns the unmodified shadow algorithm, whereas the complete grid-robust lower bounds from the fixed shear start are already proved.

## Reproducibility

The local file code/canonical_shadow_obstruction.py implements all rational data and O(n^2)-atom normal certificates. It has verified 72 cases, at the two ends and midpoint of the window, in dimensions 5,6,7,10,15,20, for both the minimum permitted K and K=2^64, and for both unperturbed and strictly positive inputs. The proof above establishes every intermediate transition; the tests do not simulate or replace that proof.
