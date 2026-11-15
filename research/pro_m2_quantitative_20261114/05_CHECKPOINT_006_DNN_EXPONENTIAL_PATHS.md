# Checkpoint 006 — exponential shadow paths survive PSD preprocessing

Date: 2026-11-14 project date. This strengthens checkpoint 002 substantially: the inputs below are positive definite, entrywise nonnegative, and outside CP in EVERY order n>=5. Thus the earlier limitation that a PSD pretest immediately rejects the lower-bound family no longer applies to this new family. Historical novelty and the venue-quality benchmark are still separate questions.

## Theorem

Fix n>=5, put r=n-1, h=r+2, c0=r(r+3)/2, b0=r(r+2), and

    gamma=2h/c0=4(r+2)/[r(r+3)],    t=3/5.

Let N be any integer with N>=256(r+2)^2. On coordinates 1,2,3,4,n take the five-cycle matrix F=I_5+t Adj(C_5), and scale its coordinates by (N,gamma,gamma,N,1). On the remaining coordinates 5,...,r put the diagonal block N^2 I_(n-5), with zero entries connecting it to the five-cycle block. Call the resulting rational matrix B_N, and set

    A_N=B_N/(n N^2),
    m_N=floor(sqrt(N)/[4(r+2)]).

Use the fixed initial Ryshkov vertex and its prescribed full-minimal-vector anchor

    P_1=[[J_r,-(3/2)1],[-(3/2)1^T,3]],
    C0_top=(r+4)I_r+J_r,
    C0_cross=(r+2)1,
    C0_last=c0.

For the specified minimum-ratio shadow rule, the first m_N-1 pivots are uniquely forced:

    P_1 -> P_2 -> ... -> P_(m_N),
    P_k=[[J_r,-(k+1/2)1],[-(k+1/2)1^T,k^2+k+1]].

None of the vertex tests, exact ray-copositivity tests, or the prescribed objective-dependent corrected-grid tests can terminate before those pivots. All A_N are positive definite and entrywise nonnegative, but A_N is not completely positive. They satisfy

    ||A_N||_F<=1,
    dist_F(A_N,CP_n)>=gamma^2/(5nN^2).

For every fixed n, H=O_n(log N), whereas the pivot count is Omega_n(sqrt(N))=2^[Omega_n(H)]. Therefore the proposed polynomial-in-H theorem remains false even after ordinary PSD and entrywise-nonnegativity preprocessing, in every dimension where DNN and CP differ.

The underlying vertices and their adjacency are the known Dannenberg–Schürmann construction, credited in checkpoint 004. The contribution proved here is the DNN objective family and its exact, unique shadow trajectory, not the invention of those vertices.

## 1. Positive definiteness, nonmembership, normalization and distance

The leading principal minors of F=I+(3/5)Adj(C_5), in cycle order, are

    1, 16/25, 7/25, 31/625, 11/3125.

Thus F is positive definite. Positive diagonal congruence and the additional positive diagonal block prove B_N positive definite. Entrywise nonnegativity is immediate.

Let H_5=J_5-2 Adj(C_5), the Horn matrix. It is copositive: on the simplex, the maximum of sum_(ij in E(C5)) x_i x_j is at most 1/4. To see this directly, choose a maximizing vector with minimal support. If two nonadjacent coordinates are positive, transferring their combined mass to the one with the larger neighbor sum does not decrease the objective and reduces the support. Hence the support is a clique, of size at most two, where the bound is elementary. Therefore H_5[x]=(sum x_i)^2-4 sum_edges x_i x_j>=0.

Moreover <F,H_5>=5-10(3/5)=-1. Inverse diagonal congruence of H_5, padded by zeros on the extra coordinates, gives W_N in COP_n with

    <B_N,W_N>=-1,
    ||W_N||_F<=5/gamma^2.

Here 0<gamma<1 for r>=4. Every entry of B_N has magnitude at most N^2, so ||B_N||_F<=nN^2. Duality and Cauchy–Schwarz give the stated distance bound after normalization. The input uses O(n^2(log N+log n)) bits.

## 2. The known shear vertices and their retained face

Checkpoint 002 gives the self-contained verification of the following facts. For k>=1,

    Min(P_k)={e_i:i<=r} union {(u,1):u>=0 integral, sum u in {k,k+1}}.

The extreme tangent ray toward P_(k+1) is

    R_k=[[0,-1],[-1^T,2k+2]],

with exact edge length one. Its retained active normals are e_i e_i^T and (u,1)(u,1)^T for sum u=k+1.

A useful strengthening of the normal-face argument is the following. Fix s>=2. Suppose a symmetric matrix C has a positive rational representation using all e_i e_i^T, all (s e_i,1)(s e_i,1)^T, and at least one positive two-coordinate composition u for every unordered pair i,j (with sum u=s). All these normals are retained by R_(s-1). Their common annihilator is one-dimensional: the e_i fix the top diagonal of a tangent direction to zero; the s e_i compositions make all cross entries equal and determine the last diagonal; the two-coordinate compositions then make every top off-diagonal zero. Thus C annihilates exactly the ray R_(s-1) among feasible tangent directions, and lies in the relative interior of its normal face.

This observation avoids enumerating all weak compositions and supplies a polynomial-size certificate for each forced transition.

## 3. Exact shadow parameter and target normal

Write I={1,4}, J={2,3}, and L={1,...,r}\J. The coordinates in L are the large-diagonal coordinates; the two coordinates in J remain bounded. Define

    a=t gamma,    b=t gamma^2.

For every integer 2<=s<=m_N set

    lambda_s=(s c0-b0)/(2tN-s)>0,
    C_s=C0+lambda_s B_N.

The normalization A_N multiplies the corresponding shadow parameter by nN^2 but changes no pivot choice. The top-to-last entries of C_s are

    h_i=h+lambda_s tN  for i in I,
    h_i=h              for i not in I,

and their sum is s(c0+lambda_s). The top off-diagonal entries D_ij are one, except

    D_12=D_34=1+lambda_s aN,
    D_23=1+lambda_s b.

The top diagonal is r+5+lambda_s N^2 on L and r+5+lambda_s gamma^2 on J.

The identity that makes the construction work is

    lambda_s aN = h s - gamma b0/2 + (gamma/2)lambda_s s.

It follows from gamma c0/2=h and the defining equation for lambda_s.

## 4. A positive rational decomposition of C_s

All vectors in this construction are (u,1) with integer u>=0 and sum u=s, except for the final coordinate axes. We specify weights that reproduce every off-diagonal top entry, then fill the means and diagonal slacks.

### Pair atoms

For each i in L and j in J, use

    u=(s-1)e_i+e_j,    weight D_ij/(s-1).

For each unordered pair i,j in L, use both orientations

    u=(s-1)e_i+e_j and u=e_i+(s-1)e_j,

with weight D_ij/[2(s-1)] each. Here D_ij=1.

For the pair J={2,3}, put p=floor(s/2), q=s-p, and use

    u=p e_2+q e_3,    weight D_23/(pq).

Every weight is positive. At s=2 some atoms coincide; duplicate positive weights may simply be added.

### Positive remaining means

Let L_i be the contribution of the pair atoms to the i-th top-to-last entry. On a large coordinate i in L,

    L_i=2+1_(i in I)lambda_s aN
          +(r-3)/2 [1+1/(s-1)].

Since gamma<1,

    h_i-L_i>=3+1_(i in I)lambda_s t(1-gamma)N>0.

On either small coordinate j in J, since min(p,q)>= (s-1)/2,

    L_j <= [r+lambda_s aN+2lambda_s b]/(s-1).

Using the identity in Section 3 gives

    (s-1)(h-L_j)
      >= 2/(r+3)-lambda_s[(gamma/2)s+2b].

This is strictly positive in the stated range. Indeed s<=sqrt(N)/(4h)<=N/5, so 2tN-s>=N and lambda_s<=c0 s/N. Therefore

    lambda_s[(gamma/2)s+2b]
      <= h s^2/N+2t c0 gamma^2 s/N
      <= 1/(16h)+2t h/(c0 sqrt(N))
      <= 1/(16h)+t/(8c0)
      <= 1/(8h)
      < 2/(r+3).

The penultimate inequality uses 2t h<=c0, valid for r>=4, and sqrt(N)>=16h.

For every i now add the concentrated atom u=s e_i with weight (h_i-L_i)/s. These weights are strictly positive. Every atom has top-coordinate sum s, and sum_i h_i=s(c0+lambda_s), so the resulting last diagonal is automatically c0+lambda_s, exactly as required.

### Positive diagonal completion

For any such distribution of compositions, its i-th top diagonal is forced to be

    s h_i - sum_(j!=i) D_ij.

Thus add the axis e_i e_i^T with coefficient

    chi_i=(C_s)_ii-s h_i+sum_(j!=i)D_ij.

For j in J, direct substitution yields

    chi_j=2h/(r+3)+lambda_s[(gamma/2)s+gamma^2(1+t)]>0.

For i in I,

    chi_i=2h-hs+lambda_s[N^2-tNs+aN].

For i in L\I,

    chi_i=2h-hs+lambda_s N^2.

Since s<=N/5, the first bracket is at least N^2/2. Also c0s-b0>=rs/2 for s>=2, so lambda_s>=5rs/(12N). Consequently both kinds of large-coordinate slack are positive under N>=256h^2.

We have now reproduced every entry of C_s by a strictly positive rational combination of retained normals. It includes the axes, all concentrated compositions, and a two-coordinate composition for every pair. Section 2 therefore proves that R_(s-1) is the unique zero-cost feasible ray for C_s.

## 5. Unique shadow choices and no early stopping

For every feasible tangent ray T at P_(s-1), <C_s,T>>=0, with equality only on R_(s-1). Because

    <B_N,R_(s-1)>=-2(2tN-s)<0,

the minimum ratio <C0,T>/(-<B_N,T>) among B_N-descending extreme rays is uniquely lambda_s and is attained at R_(s-1). Induction forces all stated pivots.

Every P_k is positive semidefinite and nonzero, whereas B_N is positive definite. Hence <B_N,P_k>>0, so the vertex separator test cannot terminate this prefix. Also R_(s-1) is not copositive, since its value at ((s+1)e_i,1) is -2.

For the corrected-grid ray test let T0=tr(B_N), and put

    beta=(2tN-s)/T0,
    alpha=beta/(2s).

These are exactly the test's correction parameters: R+alpha tr(R)I=R+beta I. Since T0>=2N^2, beta<=3/(5N), and s<=N/5,

    beta(2s+beta)<=6/25+9/(25N^2)<1.

Thus 4s^2 alpha(1+alpha)<1. Every allowed grid q with 4q^2 alpha(1+alpha)>=1 satisfies q>s, and the shell vector (q e_i,1) has ray value 2(s-q)<0. The grid procedure must descend. No assumption about its enumeration order is needed.

## 6. Reproducibility and implications

The local file code/dnn_shadow_obstruction.py constructs the normalized input and padded inverse-congruence Horn separator, and builds each normal-cone certificate with O(n^2) rational atoms. It has checked 48 exact certificates in dimensions 5 through 10, including N=2^32, without simulating the long path. These checks verify the formulas; the all-n proof above is independent of those finite tests.

The lower bound is not a special finite-dimensional example: it is an explicit asymptotic family in every n>=5, with a fixed start, unique choices, rational distance estimates and polynomial-size compressed proofs. Together with the single-exponential upper bound in checkpoint 005, it establishes the same exponential-in-binary-precision growth class even on doubly nonnegative nonmembers.

The original n=2 rule-independent family remains useful: it shows that changing a local A-descending extreme-ray tie-breaker cannot fix the unrestricted algorithm. The present family addresses the separate objection that PSD preprocessing might remove all difficult lower-bound inputs.

Still NOT claimed here: the higher-order canonical tridiagonal-start path; historical priority for this algorithmic lower bound without further audit; or a completed upper-quintile journal comparison.
