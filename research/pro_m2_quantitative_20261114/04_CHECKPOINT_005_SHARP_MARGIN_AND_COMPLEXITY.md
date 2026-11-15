# Checkpoint 005 — sharp quantitative Ryshkov geometry and a complete exponential complexity class

Date: 2026-11-14. This is an additional proved mathematical result. It is NOT a claim that the requested upper-quintile comparison or priority audit has been completed.

## 1. Sharp norm-to-margin invariant

For P in the copositive Ryshkov set R_n, write

    mu(P)=min{P[x]: x>=0, ||x||_2=1}.

For n>=2 and M>=max(1,||P||_F), define

    U_n(M)=8n(16nM)^(n-1).

Then

    mu(P) >= 1/U_n(M).

The exponent n-1 of M is optimal in every fixed dimension, even if P is required to be a positive definite perfect Ryshkov vertex. Thus this is a uniform quantitative version of the Interior Ryshkov property, not just compactness. Its proof develops the same simultaneous-approximation mechanism used qualitatively in the earlier orthant and generalized-perfect-matrix literature; historical novelty of the explicit sharp exponent must not be assumed without further comparison.

### Proof of the lower bound

First P is copositive: a negative value at a real nonnegative vector would persist at a rational one, and clearing denominators would contradict the defining integer inequalities.

Choose a unit nonnegative minimizer x and let S be its positive support, of size s. On this support, first-order stationarity for the sphere gives P_SS x_S=mu x_S. If s=1, the conclusion follows from P_ii>=1. Otherwise choose j with x_j=max_i x_i and put y=x/x_j, so y_j=1 and ||y||<=sqrt(n).

Let Q=ceil(sqrt(8nM)). The pigeonhole proof of simultaneous Dirichlet approximation gives an integer m with 1<=m<=Q^(s-1) and integers v_i, i in S\{j}, such that |v_i-m y_i|<=1/Q. Set v_j=m and set the other coordinates to zero. Because each m y_i>=0 and the error is strictly less than one, all v_i are nonnegative. Thus v is a nonzero permitted lattice vector. For e=v-my,

    ||e||<=sqrt(n)/Q,
    P[v] = mu m^2||y||^2 + 2mu m<y,e> + P[e]
          <= mu(m||y||+||e||)^2 + M||e||^2
          <= 4n mu Q^(2(n-1)) + 1/8.

Since P[v]>=1, mu>=7/[32n Q^(2(n-1))]. Also Q<=4sqrt(nM), so in particular mu>=1/[8n(16nM)^(n-1)]. This proves strict copositivity and the quantitative bound simultaneously. No rationality assumption on P is needed.

### Sharpness of the exponent

Let T_n be the canonical tridiagonal perfect matrix with diagonal one and adjacent entries -1/2. Let S be the upper shift matrix, and for any integer q>=2 put

    V_q=I-qS,
    P(q)=V_q^T T_n V_q.

The matrix V_q is integral unimodular, and V_q^(-1)=I+qS+...+q^(n-1)S^(n-1) is entrywise nonnegative. For every nonzero integer z, T_n[z]>=1; indeed

    T_n[z]=(z_1^2+z_n^2+sum_(i=1)^(n-1)(z_i-z_(i+1))^2)/2.

Its integer minimum is attained exactly by the positive and negative consecutive-interval indicators. Their positive rank-one matrices span Sym_n. Hence P(q) belongs R_n and is a perfect copositive vertex: the inverse images of the positive interval vectors remain nonnegative and their rank-one matrices still span.

Let w_q=V_q^(-1)e_n=(q^(n-1),q^(n-2),...,1). Then P(q)[w_q]=1, so

    mu(P(q))<=1/||w_q||^2<=q^(-2(n-1)).

On the other hand,

    ||P(q)||_F <= ||V_q||_2^2 ||T_n||_F
               <= (q+1)^2 sqrt((3n-1)/2)
               <= (9/4) sqrt((3n-1)/2) q^2.

Thus mu(P(q)) ||P(q)||_F^a tends to zero for every a<n-1. No smaller norm exponent can hold uniformly. The same example shows that the maximal norm of a minimal lattice vector can grow like M^((n-1)/2).

## 2. Uniform vertex and ray heights

Every v in Min(P) satisfies ||v||^2<=U_n(M). Consequently there are at most

    K_n(M)=(floor(sqrt(U_n(M)))+1)^n-1

possible active vectors for all vertices in the norm-M region.

In upper-triangular matrix coordinates the integer normal of v has entries v_i^2 on the diagonal and 2v_i v_j off the diagonal, all bounded by 2U_n(M). A vertex is determined by d=n(n+1)/2 independent active equations with right-hand side one. Cramer's rule therefore bounds all numerator and denominator magnitudes by

    E_n(M)=d! [2 ceil(U_n(M))]^d.

An extreme tangent ray has an integer primitive generator given by cofactors of d-1 independent active equations, and every entry is bounded by E_n(M) as well. These statements include arbitrary vertex degeneracy. In bit terms the bound is O(n^3(log n+log M)).

There are at most binom(K_n(M),d) vertices in this region. This count uses bounded active normals supplied by the quantitative margin; norm compactness alone does not give such an arithmetic bound.

## 3. Global shadow-path bound with explicit constants

Consider either the canonical tridiagonal initialization, or the fixed P_1 and its anchor from checkpoint 002. Let ||A||_F<=1 and delta=dist_F(A,CP_n)>0. Every nonterminal vertex visited by the specified minimum-ratio rule has

    ||P||_F <= M = 48 n^5/delta.

Here is the complete estimate. In both initializations, ||C0||_F<=2n^3, ||P_start||_F<=3n, and <C0,P_start>=|Min(P_start)|<=2n^2. Moreover

    ||Q||_F <= 6n <C0,Q>   for every Q in COP_n.

For the canonical anchor this follows by recovering each matrix entry from the consecutive-interval quadratic values via the four-term second-difference formula. For P_1, put a_i=Q[e_i], s_i=Q[(e_i,1)], t_i=Q[(2e_i,1)]. Then

    Q_in=(t_i-s_i-3a_i)/2,
    Q_nn=2s_i-t_i+2a_i,

and the values at (e_i+e_j,1) recover Q_ij. All these quadratic values are nonnegative and their sum is at most <C0,Q>; the displayed factor 6n is a valid common bound.

The shadow invariant is C0+lambda A in the minimizing normal cone of the current vertex. Starting at lambda=0, the minimum ratio preserves this invariant and makes lambda nondecreasing: at the old lambda every feasible ray has nonnegative cost, and increasing lambda first makes an A-descending ray cost zero precisely at the minimum ratio. The adjacent endpoint then minimizes the same functional. This argument allows ties and degenerate vertices.

Take Z in COP_n with ||Z||_F=1 and <A,Z>=-delta, supplied by conic projection. Since C0+lambda A is in CP_n,

    lambda<=<C0,Z>/delta<=2n^3/delta.

At a nonterminal vertex, <A,P>>=0. Comparing the minimizing cost with the initial vertex gives

    <C0,P><=2n^2+lambda*3n<=8n^4/delta.

The anchor inequality now gives the norm bound M.

Every bounded pivot strictly decreases <A,P>, so no departure vertex is repeated. Hence the number of adjacent pivots is bounded by

    binom(K_n(48n^5/delta), d)
    <= [2 sqrt(8n) (768n^6)^((n-1)/2)]^(nd)
       delta^[-n(n-1)d/2].

This is 2^[O(n^4(log n+log(1/delta)))], and therefore 2^[O(n^4(H+log n))]. Checkpoint 002 gives 2^[Omega_n(H)] lower bounds. Thus, in every fixed dimension for the specified fixed-start rule, single-exponential dependence on binary precision is a sharp worst-case growth class. The numerical constant and dimension exponent in the upper bound are not claimed optimal.

This does NOT prove the proposed polynomial theorem; it classifies its failure. Nor does it imply exponential intrinsic complexity of CP separation: checkpoint 003 gives a polynomial-precision replacement.

## 4. Terminal endpoints and a finite, bounded neighbor routine

The preceding norm bound covers nonterminal vertices. To avoid silently assuming it also covers the last endpoint, proceed separately.

Let E=E_n(M), and normalize a selected noncopositive ray R to its primitive integer generator, with entries bounded by E. The exact support-stationarity oracle of checkpoint 003 supplies a nonnegative rational x with R[x]<0. Cramer's rule on a bordered system of order at most n+1 gives a nonnegative integer witness w with

    0<=w_i<=F=(n+1)! E^(n+1),
    R[w]<=-1.

Set s0=(P[w]-1)/(-R[w])>0. The edge length ell is at most s0<=MnF^2. Consequently its endpoint P' has

    ||P'||_F <= M'=M(1+n^2 E F^2).

Applying Section 2 at M' bounds the terminal vertex's rational heights by E_n(M'). In particular every visited vertex, primitive ray, negative-vector witness, and terminal certificate has polynomial-in-H bit length; a conservative uniform bound is O(n^7(H+log n)). This is fully compatible with exponentially many pivots.

There is also a direct finite rational neighbor algorithm. Compute the negative integer witness w and s0. Obtain any rational Mbar>=||P||_F+s0||R||_F, for example from entrywise absolute sums. Enumerate all nonzero v>=0 integral with ||v||^2<=U_n(Mbar). Among those with R[v]<0, minimize

    (P[v]-1)/(-R[v]).

The true endpoint is in R_n and has norm at most Mbar, so an active endpoint vector belongs to this finite enumeration. Every tested ratio is at least the true edge length, and at least one equals it. Thus the minimum is exactly ell. This supplies an explicit cutoff, unlike an unquantified dovetail. The enumeration can still be exponential in binary precision, as it must be for an implementation that explicitly lists all active vectors on the family in checkpoint 002.

## 5. Resource interpretation and priority

The lower-bound family keeps vertex/ray heights logarithmic while crossing exponentially many faces. The optimal margin invariant explains why all objects nevertheless have polynomial encoding length, and supplies a matching single-exponential upper complexity class. A valid precision-polynomial repair must bypass the number of adjacent face transitions, not merely control coefficient growth.

The simultaneous-approximation proof is closely related to the qualitative Interior Ryshkov arguments in Dutour Sikirić–Schürmann–Vallentin and Oertel–Schürmann, Generalized Perfect Matrices, arXiv:2602.05841v2, Theorem 4.1. The latter explicitly cites Dirichlet's theorem. The sharp norm exponent and the quantitative shadow-path consequences are the specific assertions being isolated here; priority remains subject to a full literature comparison.

A new September 2026 preprint, Linchuan Wei, *Integer quadratic programming in fixed dimension is polynomial-time solvable*, was also located on Optimization Online. Its full proof has not yet been audited and none of the theorems above depend on it. No fixed-dimensional integer-quadratic hardness claim should be made without confronting this development.
