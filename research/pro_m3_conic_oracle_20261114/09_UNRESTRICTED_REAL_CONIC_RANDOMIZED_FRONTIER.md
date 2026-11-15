# Checkpoint 09 — unrestricted randomized conic minimax for REAL coefficients

## Scope

This proves the unrestricted exact-value/gradient frontier for genuine weakly infeasible PSD-distance objectives with REAL affine data. It has a fixed distribution, arbitrary finite queries and output, uniform escape constants, polynomial dimension, and a complete lower-bound proof. It does NOT satisfy the original handoff's rational-support condition. The rational version of this particular family is decoded in one exact query, so that qualification is mathematically substantive.

Fix any positive rational beta. The fixed conic tail from checkpoint 05 supplies that exponent; beta=1/2 uses just [[0,1],[1,z]]. All coefficient templates before the random orthogonal rotation can be rational.

## Theorem

There are constants c_beta,C_beta,s_beta,k_beta>0 and, for every T>=1, a fixed distribution of genuinely weakly infeasible isometric affine PSD pencils with

    f(0)<=1, inf f=0 unattained,
    c_beta s^-beta<=rho_f(s)<=C_beta s^-beta, 0<s<=s_beta,

such that EVERY measurable randomized adaptive algorithm using at most T exact natural value/coordinate-gradient queries and returning any finite unqueried output satisfies

    Pr{f(output)>=k_beta (T+1)^(-2/(2beta+1))}>=7/8.

The probability is over a single initial Haar rotation and the independent algorithm seed. The coordinate dimension and matrix order are O_beta(T^3). The matching universal upper bound is O_beta(T^(-2/(2beta+1))) by accelerated natural gradients. No query-radius restriction is imposed.

## 1. An elementary fixed-Haar matrix-vector lemma

Let A0 be a fixed positive definite D-by-D matrix and b0 a fixed vector. Draw U Haar uniformly from O(D), and give the algorithm b=Ub0 and the matrix-vector oracle A=UA0U^T. The algorithm is allowed arbitrary adaptive vectors, unrestricted computation, independent randomization, and any finite output.

LEMMA 1 (deferred rotation, including an unqueried output). There is a coupling under which the reference-coordinate output U^T x_hat belongs to

    span{A0^k b0:0<=k<=T}
       +span{A0^k zeta_j:0<=k<=T, 1<=j<=T+1},          (1)

where zeta_1,...,zeta_(T+1) are independent standard Gaussian vectors in R^D. This is an enlargement of the information available to the algorithm, not a restriction that it obey a linear-span rule.

Proof. Reveal U only on a reference subspace V and its image W. Initially V=span(b0), and Ub0 is revealed. Conditional on these mappings, the unassigned orthogonal map V^perp->W^perp is Haar. At a query v, decompose v into W and W^perp. If the latter component is nonzero, its reference preimage is uniform on the sphere in V^perp. Realize it by the normalized projection of a fresh independent standard Gaussian zeta_j onto V^perp, and assign that reference direction its required physical image. The reference query therefore lies in span(V,zeta_j). Next reveal the image of A0 times that reference query. Its component outside the enlarged reference subspace has a uniform physical direction in the remaining orthogonal complement; assign that image. The unrevealed map remains Haar, by invariance of Haar measure under the stabilizer of the already assigned vectors. Degenerate zero components require no new assignment.

After query j the reference subspace is contained in span of A0^k b0 for k<=j and A0^k zeta_i for i<=j and k<=j-i+1. This follows inductively because the new query is in V+span(zeta_j) and its answer is A0 times that vector. At the output, apply the same preimage construction once more, using zeta_(T+1), but no matrix-vector product. Enlarging all polynomial degrees to T gives (1).

This construction has exactly the joint law of an initially Haar U and the algorithm's transcript: it is deferred sampling of a fixed random orthogonal map, not a rotation selected to oppose a realized random seed. Independent algorithm randomness can be conditioned on throughout and then averaged. QED.

## 2. Repeated eigenspaces make exploratory directions harmless

Suppose A0 has N distinct eigenvalues lambda_1,...,lambda_N, each with multiplicity L. Let E_i be their orthogonal eigenspaces and write b0=sum_i b_i, b_i in E_i. Let

    W_i=span{Proj_E_i zeta_j:1<=j<=T+1}, W=direct_sum_i W_i.

Every Gaussian-start term in (1) belongs to W, and W is A0-invariant. If b_i is nonzero set u_i=b_i/||b_i||. The random W_i is a uniform (T+1)-dimensional subspace of E_i almost surely, provided L>T+1. Rotational symmetry gives

    E||Proj_W_i u_i||^2=(T+1)/L.

Markov's inequality and a union bound give

    Pr{some i has ||Proj_W_i u_i||^2>1/2}
       <=2N(T+1)/L.                                  (2)

Zero b_i can simply be omitted. Take L=16N(T+1), so the good event has probability at least 7/8.

Let x_star=A0^-1 b0 and q0(x)=||x-x_star||_(A0)^2/2. For any polynomial p of degree at most T, minimizing over w in W gives

    min_w q0(p(A0)b0+w)
      = (1/2)sum_i lambda_i(1/lambda_i-p(lambda_i))^2
                       ||(I-Proj_W_i)b_i||^2
      >= (1/2) min-free-expression sum_i
               [(1/2)lambda_i(1/lambda_i-p(lambda_i))^2||b_i||^2]
      = (1/2)q0(p(A0)b0).                              (3)

In the middle line, the outer factor 1/2 is the loss from retaining at least half the squared norm of each b_i; equivalently, and unambiguously,

    min_w q0(p(A0)b0+w) >= (1/2) q0(p(A0)b0).

Therefore on the same good event EVERY vector in the enlarged information space (1) has quadratic gap at least half the best ordinary Krylov gap:

    q0(U^T x_hat) >= (1/2) min_(deg p<=T) q0(p(A0)b0). (4)

This bound is simultaneous over all polynomials and coefficients, even those chosen from the full transcript. It controls arbitrary query magnitudes and arbitrary output magnitudes without a concentration argument for the queries themselves.

## 3. A weighted tridiagonal quadratic with a uniform profile

Set

    theta=2/(2beta+1), nu=2-theta,
    t=(1-theta)/2,
    sigma_i=2^floor(t log_2 i), q_i=sigma_i/sigma_(i+1),
    a=1/16, c0=a^2/2=1/512,
    N=2T+3, L=16N(T+1), D=NL.

Let B_N be the N-by-N bidiagonal difference map whose rows are e_1^T and e_i^T-q_i e_(i+1)^T, i=1,...,N-1. Invertibility follows by back substitution. Its Gram matrix is symmetric tridiagonal with nonzero offdiagonal entries, so its eigenvalues are simple: the first coordinate of an eigenvector determines all remaining coordinates by the three-term recurrence, making every eigenspace at most one-dimensional.

Set

    A0=a^2 diag(B_N^T B_N,...,B_N^T B_N)  [L copies],
    b0=a^2 e_1 in the first copy,
    q0(x)=x^T A0 x/2-b0^T x+c0.

Then q0 is nonnegative, with unique zero x_star=(sigma_1,...,sigma_N,0,...,0). It equals c0 times the anchored chain on the first copy, and homogeneous nonnegative chain energies on the others. Also 0<A0<=10a^2 I<I/2. Each eigenvalue has precisely multiplicity L.

Because b0 is the first coordinate of an irreducible tridiagonal chain,

    span{A0^k b0:0<=k<=T}

is exactly the first T+1 coordinate positions of the first copy. Induction gives one nonzero new coordinate at each multiplication and no coordinates beyond it. Weighted Cauchy--Schwarz therefore gives

    min_(deg p<=T) q0(p(A0)b0)=c0/D_(T+1),
    D_k=1+sum_(i=1)^k sigma_i^-2
       <=(1+4/theta)(k+1)^theta.                       (5)

Combining (4)--(5), any T-query matrix-vector algorithm, even with b=Ub0 given for free, satisfies with probability at least 7/8

    q_U(x_hat)>=c0/[2(1+4/theta)](T+2)^(-theta).         (6)

This proves the fixed-distribution randomized quadratic bound needed here without invoking an unspecified oracle lower-bound transfer. The multiplicity device enlarges dimension to O(T^3), but leaves the comparator geometry unchanged.

## 4. Actual conic realization and exact transcript simulation

Let C0=a diag(B_N,...,B_N), d0=a e_1 in its first row block, so C0^T C0=A0, C0^T d0=b0, and ||d0||^2/2=c0. Choose a rational Gram factor S0^T S0=I/2-A0, and put

    C_U=C0 U^T, S_U=S0 U^T,
    M=max(1,ceil(||x_star||)).

Use the exact pencil from checkpoint 07, replacing its 2x2 tail by the fixed rational conic tail g_beta:

    X_U(x,y)=diag( star(C_U x-d0),
                   [[M,(S_U x)^T],[S_U x,M I]],
                   tail_beta(y) ).

Its natural objective is

    f_U(x,y)=q_U(x)+(||S_U x||-M)_+^2/2+g_beta(y).      (7)

The x-directions have unit Gram matrix because 2C_U^T C_U+2S_U^T S_U=I; the tail directions are orthonormal and disjoint. The fixed tail forbids exact feasibility. At x=Ux_star the first block is zero and ||S_U x||<=||x_star||/sqrt(2)<=M, so the first two blocks are PSD. The tail tends to the cone. Hence every sampled affine space is genuinely weakly infeasible.

Give the conic algorithm the extra side information b=Ub0, M,c0 and the tail template. At an arbitrary finite query, one product Ax determines the exact value and gradient of (7), by checkpoint 07's displayed formula. Thus a T-query conic algorithm is simulated by a T-query matrix-vector algorithm, including every unbounded excursion and its unqueried output. Since f_U>=q_U, inequality (6) proves the conic lower bound. Not giving the optional side information cannot weaken that lower bound.

## 5. Uniform escape geometry

The fixed tail supplies rho_f(s)>=rho_g(s)>=c_beta s^-beta. For the upper bound, use the first-copy prefix comparators from the chain proof. Their quadratic gap is c0/D_k, their coordinates obey |x_i|<=sigma_i, and

    sum_(i=1)^k sigma_i^2 <= (k+1)^nu/nu.

Choosing k=O_beta(s^(-1/theta)), or the exact zero if that prefix exceeds N, gives q_U<=s/2 and ||x||<=K_beta s^-beta. Every such prefix has norm <=||x_star|| and hence zero padding cost. Add a tail comparator at s/2. This gives the upper profile with constants and onset independent of T,D,U. Also f_U(0)=c0+1/2<1.

A rational Gram factor S0 can have at most 4D rows by rational LDL elimination and four-square expansion. Consequently the matrix order is at most 5D+2+m_beta=O_beta(T^3). A real square root factor would reduce this constant, but is unnecessary. The Haar rotation is the only source of nonrational coefficients. No coefficient-height bound for it is asserted.

## 6. Upper bound, feasibility translation, and status

For any natural conic objective in the same normalized profile class, accelerated gradients with arbitrary finite comparators give

    f(x_T)<=s+2rho_f(s)^2/(T+1)^2.

Taking s=(T+1)^(-theta) proves the matching objective rate. Residual delta=sqrt(2f) therefore has minimax power T^(-1/(2beta+1)), and the optimal query order for residual tolerance delta is delta^(-(2beta+1)). At beta=1/2 this is objective Theta(1/T), residual Theta(T^-1/2), and query order Theta(delta^-2). Coordinate escape is Theta(delta^-2beta); the norm of the matrix displacement from X0 is exactly the coordinate norm. Absolute matrix norm differs by the fixed instance offset and is not asserted to have a uniform dimension-independent bound when X0 itself grows with the horizon.

This completes the real-data unrestricted conic theorem, with an explicit fixed distribution and query-level conic simulation. Checkpoint 08 instead completes a rational-data radius-charged theorem. Neither silently solves the original rational-data, unrestricted-exact-query conjecture. The latter remains a distinct open obligation in this project.
