# Milestone 37 — Sharp finite-lattice certificates and exact rational CP regularization

Date: 2026-11-14. Working branch: `laa-track02-gptpro-analytic-frontier-20261112`.
Parent repository snapshot: `316878c732ee1495caa3d73d6e89a08b4f2291d3`.

## Status and prior-work correction

This is a self-contained strengthening of Manuscript II. It proves an EXACT best constant for a finite-lattice approximation of the completely positive/copositive dual pair, a rational regularization theorem preserving every off-diagonal entry, a finite LP certificate alternative, and a target-dependent replacement for the shadow algorithm's copositivity test. The proofs below do not depend on the other project theorems, except that the stated shadow-pivot application restates the earlier rule and uses published Ryshkov geometry.

The earlier suggestion to solve the universal rational CP-factorization conjecture positively was outdated. Current primary manuscripts report counterexamples: Sidney Holden, *A rational completely positive matrix with no rational nonnegative factor* (13 September 2026), supplies an integer example of order 444 and rank seven; Yaroslav Shitov, *Constructing a rational cp-matrix whose every cp-factorization is irrational, with GPT-6 Astra*, reports an order-308 example, dated 9 September 2026 and deposited on Zenodo on 11 November. Those are external works, not our contributions. This continuation does not purport to revalidate their full computational/formal certificates. Claiming a new positive resolution of that problem would therefore be unjustified. Nothing below assumes the correctness of either counterexample.

Polyhedral CP/COP approximation, rational interior factorizations, and second-order grid convergence have established antecedents: Yildirim (2012), de Klerk–Laurent–Sun (2015), de Klerk–Laurent–Sun–Vera (2017), and Dutour Sikiric–Schuermann–Vallentin (2017, 2021). We do NOT claim the first polyhedral hierarchy, the first rational approximation, or the first O(q^-2) grid rate. The assertions proved here are the sharp dimension-independent constant for this specific cubical-shell model and the stated exact arithmetic consequences. Historical novelty for their combination remains to be established; no conjecture-resolution or editorial guarantee is claimed.

## 1. Finite cones and the exact optimum

Use the trace pairing on real symmetric matrices. Write

    CP_n = cone{xx^T:x>=0},       COP_n = CP_n*.

For an integer q>=1 define the OUTER LAYER of the nonnegative integer cube,

    V_(n,q) = {v in {0,1,...,q}^n : max_i v_i=q}.

Its cardinality is exactly (q+1)^n-q^n, at most n(q+1)^(n-1). Define

    K_(n,q) = cone{vv^T:v in V_(n,q)},
    D_(n,q) = {Q:v^T Q v>=0 for all v in V_(n,q)}.

K_(n,q) is a closed rational polyhedral inner approximation of CP; D_(n,q) is its dual outer approximation of COP. All diagonal rays are present. Consecutive q need not give nested cones, but q=2^k does give nested inner cones and decreasing outer cones.

Set

    eta_q=(sqrt(1+q^(-2))-1)/2,       nu_q=1/(4q^2).

Then

    eta_q(1+eta_q)=nu_q,
    1/(4q^2+1)<=eta_q<1/(4q^2).

### Theorem 1: sharp cubical-shell correction

For EVERY n>=2 and q>=1, eta_q is the smallest nonnegative constant c for which either, equivalently both, of the following hold:

    A+c tr(A)I belongs K_(n,q) for every A in CP_n;       (1)
    Q+c tr(Q)I belongs COP_n for every Q in D_(n,q).     (2)

The same optimal constant applies if all nonzero cube points with coordinates at most q are tested, instead of just the outer layer. The constant has no dependence on n, rank, zero pattern, or distance to a cone boundary. The trace normalization is material; a Frobenius bound on the whole perturbation still includes sqrt(n).

For n=1 the least constant is zero; the displayed positive correction remains sufficient but is not optimal.

## 2. Proof by independent rounding

It suffices to treat A=xx^T with x>=0 and x!=0. Put m=max_i x_i and y=x/m, so max_i y_i=1. Independently round each y_i to its two adjacent multiples of h=1/q, preserving its mean; fix coordinates already on the grid. Let Z be the resulting random vector. A maximal coordinate stays one, so qZ always belongs V_(n,q).

Writing s_i in [0,h] for the offset above the lower grid endpoint (zero for an exactly represented coordinate), independence gives

    E[ZZ^T] = yy^T + Diag(s_i(h-s_i)).                  (3)

Every off-diagonal product is preserved EXACTLY. The scalar identity

    eta_q(1+s^2)-s(h-s)
      =(1+eta_q)(s-h/[2(1+eta_q)])^2 >=0              (4)

uses eta_q(1+eta_q)=h^2/4. A maximal coordinate has zero variance. For any nonmaximal coordinate a DIFFERENT coordinate is one, so ||y||^2>=1+y_i^2>=1+s_i^2. Hence every variance in (3) is at most eta_q||y||^2.

The nonnegative diagonal matrix eta_q||y||^2 I-Diag(s_i(h-s_i)) belongs to K_(n,q), as do all diagonal nonnegative matrices. The expectation in (3) also belongs to that finite cone. Consequently

    yy^T+eta_q||y||^2 I belongs K_(n,q).

Scale by m^2 and add over any CP decomposition of A to prove (1). The unknown decomposition is used only to prove cone inclusion, not as input to the finite LP algorithm below.

The map Phi_c(A)=A+c tr(A)I is self-adjoint for the trace pairing. Dualizing (1) proves (2). Conversely dualizing (2) proves (1), since the finite cone is closed. This proves equivalence. QED.

## 3. Sharpness in order two

Set

    Q_q=[[0,-1/(2q)],[-1/(2q),1]].

For integers 0<=a,b<=q,

    (a,b)Q_q(a,b)^T=b(b-a/q)>=0.

For b=0 it vanishes; for b>=1 one has b-a/q>=0. Thus Q_q passes even the FULL cube test. Its trace is one, and its negative eigenvalue is -eta_q, with a positive eigenvector proportional to (1,sqrt(q^2+1)-q). Therefore Q_q+cI is not copositive for any c<eta_q. This proves sharpness of (2), and hence of (1). Padding by zero rows/columns proves sharpness in every n>2.

Sharpness persists with rational primal inputs: a strict negative inequality at c<eta_q survives sufficiently close positive rational approximation of that eigenvector, giving a rational rank-one CP witness.

An explicit rational near-extremizer is

    A_q=[[4q^2,2q],[2q,1]]/(4q^2+1),   tr A_q=1.

It satisfies <Q_q,A_q>=-1/(4q^2+1). Thus A_q+delta I is outside K_(2,q) for every delta<1/(4q^2+1). This proves the sharp asymptotic constant 1/4 with rational data and rules out a uniformly smaller asymptotic order than q^-2 for this hierarchy.

## 4. Exact rational factors after arbitrarily small diagonal noise

### Theorem 2

For every rational completely positive A and rational epsilon>0, BOTH

    A+epsilon I,       A+epsilon Diag(A)

have nonnegative RATIONAL Gram factors. The latter retains every zero entry of A, including zero rows. Both preserve every off-diagonal entry exactly.

More generally A+D has a rational nonnegative Gram factor whenever D is rational nonnegative diagonal and D_ii>0 on every index with A_ii>0. Zero rows may remain zero.

For the two epsilon-perturbations the factor can have at most 4d=2n(n+1) columns, d=n(n+1)/2, with total bit length polynomial in n, the input encoding length, and log(1/epsilon) for 0<epsilon<=1. This is a certificate-length guarantee, not polynomial-time factor discovery.

### Scalar correction

If tr A=0 then A=0 and four squares handle the positive rational diagonal. Otherwise choose integer q with tr A/(4q^2)<=epsilon. Theorem 1, eta_q<=nu_q, and the diagonal rays imply

    A+nu_q tr A I belongs K_(n,q),
    A+epsilon I belongs K_(n,q).

A rational point in this finite integer-generated cone has rational nonnegative coefficients, obtainable at a basic feasible solution. Conic Caratheodory uses at most d independent generators.

### Relative diagonal correction

Delete the zero diagonal rows/columns; PSD makes the entire corresponding rows zero. Let s be the remaining order. Choose rational powers of two d_i such that A_ii<=d_i^2<4A_ii, using integer comparisons. For D0=Diag(d_i), the rational CP matrix B=D0^-1 A D0^-1 has diagonal in (1/4,1] and tr B<=s. Set q=ceil(sqrt(s/epsilon)). Then

    tr B/(4q^2)<=epsilon/4<=epsilon B_ii.

Hence B+epsilon Diag(B) belongs K_(s,q), by Theorem 1 and nonnegative diagonal completion. Congruence by rational D0 gives rational factor directions for A+epsilon Diag(A). Reinsert zero rows. Taking a sufficiently small scalar correction on the active rows proves the general D assertion.

### Weighted factors, four squares, and height

For a positive rational weight lambda=a/b, write the integer ab as s_1^2+...+s_4^2. Then

    lambda vv^T = sum_(l=1)^4 [(s_l/b)v][(s_l/b)v]^T.

Thus d weighted rational generators become at most 4d rational Gram columns. This classical equivalence is not claimed new.

For the height bound, list the upper triangles of the independent integer generators as columns. Their entries are at most q^2. Select a nonsingular square submatrix of order at most d, clear the target's rational denominator, and apply Cramer's rule and Hadamard's bound. Each weight has numerator/denominator bit length

    O(L+d log(dq)),

where L bounds the total target encoding length. Rational dyadic scaling adds only polynomial input length. Four-square integers satisfy s_l<=sqrt(ab). For the scalar correction, log q is polynomial in input length plus log(1/epsilon); for the relative correction, log q=O(log n+log(1/epsilon)). The total factor encoding bound follows. QED.

No unperturbed rational factor is asserted. If A_ij=0, every positive-weight generator used in the perturbed factor must have v_i v_j=0, since nonnegative terms cannot cancel. Thus the construction does not spread perturbations into absent off-diagonal edges.

## 5. A finite rational LP with an exact alternative for every input

For ANY rational symmetric A and integer q>=1 set

    B_q=A+nu_q tr(A)I.

Solve the finite LP feasibility system

    B_q=sum_(v in V_(n,q)) lambda_v vv^T, lambda_v>=0. (5)

Exactly one of the following occurs.

* Feasible: a basic solution gives at most d rational weighted generators for B_q and hence an exact rational Gram certificate by four squares. The Frobenius perturbation from A is nu_q sqrt(n)|tr A|.
* Infeasible: rational polyhedral separation gives rational Q with Q[v]>=0 on V_(n,q) and <Q,B_q><0. Return

      W=Q+nu_q tr(Q)I.

  Theorem 1 proves W in COP, and self-adjointness gives

      <W,A>=<Q,B_q><0.                               (6)

This requires neither a CP factor of A, a COP oracle, a Slater point, nor a promised gap.

For A in CP, the LP is feasible at every level. If A is outside CP, delta=dist_F(A,CP)>0. Eventually

    nu_q sqrt(n)|tr A|<delta,                         (7)

so B_q cannot be CP and the LP is infeasible. Thus doubling q terminates with a certificate for every rational nonmember. If tr A=0 and A!=0, infeasibility occurs at every q, since the only trace-zero CP matrix is zero.

This is NOT a finite exact boundary-membership algorithm: a factor of B_q does not prove A itself is CP. The grid contains (q+1)^n-q^n generators, so no dimension-uniform polynomial runtime is claimed. At a fixed trace scale, q=O(sqrt(1/accuracy)) is sufficient; Theorem 1 makes that order sharp for this grid model.

## 6. Objective-aware descent-or-certificate test

The shadow pivot supplies a rational candidate ray R with <A,R><0. A total decision whether R is COP is unnecessary. Put

    g=-<A,R>>0,      h=tr(A)tr(R),
    alpha=g/(2h) if h>0, and alpha=1/4 otherwise.

Choose integer q>=1 satisfying

    4q^2 alpha(1+alpha)>=1.                            (8)

This is exactly eta_q<=alpha, tested with rational arithmetic. Evaluate R[v] on V_(n,q).

* A negative value supplies an explicit nonnegative integer witness that R is not COP, suitable for the original adjacent-vertex step.
* If all values are nonnegative, return

      W=R+alpha tr(R)I.

  Then W is COP and

      <A,W>=-g/2 if h>0;
      <A,W>=-g+alpha h<=-g if h<=0.                   (9)

The result need not classify R itself: even a noncopositive R may correctly yield a corrected copositive separator of A. The cutoff has order sqrt(h/g) when h/g is large. The number of grid tests may still be exponential.

### Strict margins

When tr R>0, rational alpha satisfying (8) is strictly greater than eta_q: eta_q is irrational for every integer q>=1. Hence W has the positive rational copositivity margin

    mu=tr(R) [alpha(1+alpha)-1/(4q^2)]/(1+2alpha)>0,   (10)

meaning W[x]>=mu||x||^2 for every x>=0. Indeed alpha-eta_q equals the numerator in brackets divided by 1+alpha+eta_q, which is at most 1+2alpha.

If tr R=0 and the grid tests pass, diagonal tests force all diagonals zero and pair tests force all off-diagonal entries nonnegative. Add beta I, beta=g/[2(1+|tr A|)], to R. This gives a strictly copositive separator with margin beta and at least half the original negative pairing gap.

Thus the final witnesses can be strictly copositive rational matrices with explicit positive cone margins and negative target margins. Exact arithmetic, not floating-point sampling, certifies them.

## 7. Strict-copositivity certification for neighbor computations

For rational Q define

    b_q=min_(v in V_(n,q)) Q[v]/||v||^2,
    l_q=(1+n nu_q)b_q-nu_q tr Q.                      (11)

Apply Theorem 1 to Q-b_q I to obtain

    l_q<=min_(x>=0,||x||=1) Q[x]<=b_q.                (12)

The normalized grids become dense in nonnegative directions, so b_q converges to the true minimum along doubling q. If Q is strictly copositive, eventually l_q>0. This supplies an exact rational strict margin. A negative tested value supplies a noncopositivity witness. There is no termination claim on every COP boundary point.

For a known strictly copositive rational P, find such mu>0. Then its minimal integer vectors can be determined by enumerating ||v||^2<=1/mu, since only these can satisfy P[v]=1.

## 8. Consequence for the shadow-pivot procedure

Use the minimum-ratio rule from earlier manuscript 34, replacing the ray COP decision by Section 6. The negative-vector outcome permits the same adjacent edge; the separator outcome terminates correctly, possibly sooner than the unmodified procedure.

The adjacent-vertex computation also needs no total COP oracle. Suppose P is a Ryshkov vertex and R is a tangent ray, with integer w satisfying R[w]<0. Such w is not active at P, so

    s0=(P[w]-1)/(-R[w])>0.

The true edge length ell lies in (0,s0], and its endpoint is strictly copositive. There is therefore an open interval of rational s just above ell and below 2s0 on which Q=P+sR is strictly copositive but violates some integer constraint Q[v]>=1.

Dovetail rational s in (0,2s0), strict-margin certificates (11), and integer violating vectors. The open interval ensures eventual success. Given strict margin mu for such Q, enumerate the finite set with ||v||^2<1/mu and Q[v]<1. Then

    ell=min_(Q[v]<1) (1-P[v])/R[v]

is the exact edge length. Each displayed denominator is negative. Constraints not violated at s cannot fail earlier, by linearity and feasibility at zero. This returns the exact rational neighbor.

For clarity, the finite-path proof can be restated. At the initial vertex P0 choose C0 as the sum of the active rank-one normals. Their span is the full symmetric space, making C0 interior to CP and coercive on COP: <C0,Q>>=kappa||Q||. The minimum ratio <C0,R>/(-<A,R>) maintains C0+lambda A in the minimizing normal cone of the current vertex, with lambda nondecreasing. Each nonterminal edge strictly decreases <A,P>. Existence of a copositive separator Z for a nonmember A gives lambda<=<C0,Z>/(-<A,Z>). Before stopping <A,P>>=0, so comparison with P0 bounds <C0,P>, hence ||P||. A compact portion of the locally polyhedral Ryshkov set has only finitely many vertices, and strict descent prevents repetition. Every nonterminal pivot of our modified procedure is such a pivot. Thus every rational non-CP input terminates with a strictly copositive rational separator using finite integer checks and rational operations.

This uses the published geometry of the Ryshkov set. It does not invent the first exact nonmembership algorithm: earlier grid separation schemes and exact local methods already exist. The new correction theorem gives a sharp objective-dependent certificate interface, avoiding the need to classify the candidate on the COP boundary.

## 9. An exact order-five illustration beyond PSD tests

Let G be the five-cycle adjacency matrix, A=I+(3/5)G, and R=J-2G. Then tr A=tr R=5 and <A,R>=-1. The input A is positive definite and entrywise nonnegative; its smallest eigenvalue is (7-3sqrt(5))/10>0.

Section 6 chooses alpha=1/50 and q=4. Exact enumeration verifies all 5^5-4^5=2101 outer-layer quadratic tests. Consequently

    W=R+(1/10)I belongs COP_5,
    <A,W>=-1/2,
    W[x]>=(191/8320)||x||^2 for x>=0.

The last rational constant is (10). The implementation does not assume R's known copositivity to certify W. It does not claim to have run the full five-dimensional shadow path.

## 10. Reproducibility and scope

The `sharp_grid_certificates/` directory contains a pure-standard-library rational implementation and tests. It implements exact phase-I simplex with Bland pivot rules for the finite cone, the objective-aware descent alternative, and strict copositivity margins. The completed run verifies five rational sharpness cases, nine LP alternatives, seven descent/certificate cases, and three strict-margin cases. All identities and successful certificates use Fraction arithmetic. Resource caps raise errors, not false infeasibility conclusions.

The code returns weighted rational factors; the four-square conversion and its bit bound are proved above, not performed by a floating-point square root. The general neighbor subroutine is proved but not implemented in this module. The universal results rest on the proof, not the finite tests.

The optimal constant is specific to the cubical-shell model, not optimality across all approximation architectures. Polynomial certificate length does not imply polynomial discovery time. No rational factor of every UNPERTURBED boundary matrix, polynomial pivot bound, complexity-class collapse, or new resolution of the rational-factorization conjecture is claimed. The theorem and its objective-specific application still require literature-priority comparison before a novelty claim is finalized.

## Primary references

1. E. A. Yildirim, *On the accuracy of uniform polyhedral approximations of the copositive cone*, Optimization Methods and Software 27 (2012), 155–173. DOI 10.1080/10556788.2010.540014.
2. E. de Klerk, M. Laurent, Z. Sun, *An error analysis for polynomial optimization over the simplex based on the multivariate hypergeometric distribution*, SIAM J. Optim. 25 (2015), 1498–1514. DOI 10.1137/140976650.
3. E. de Klerk, M. Laurent, Z. Sun, J. C. Vera, *On the convergence rate of grid search for polynomial optimization over the simplex*, Optim. Lett. 11 (2017), 597–608. DOI 10.1007/s11590-016-1023-7; arXiv:1510.01163.
4. M. Dutour Sikiric, A. Schuermann, F. Vallentin, *Rational factorizations of completely positive matrices*, LAA 523 (2017), 46–51; arXiv:1701.03148.
5. Same authors, *A simplex algorithm for rational cp-factorization*, Math. Program. 187 (2021), 25–45. DOI 10.1007/s10107-020-01467-4; arXiv:1807.01382.
6. N. Shaked-Monderer, M. Duer, A. Berman, *Complete positivity over the rationals*, Pure Appl. Funct. Anal. 3 (2018), 681–691.
7. S. Holden, *A rational completely positive matrix with no rational nonnegative factor*, 13 September 2026. Primary source: https://github.com/ajt60gaibb/OpenProblemsInNLA/blob/main/references/holden-pf03-2026-09-13/proof/PF03_counterexample.tex . External reported counterexample, not our result.
8. Y. Shitov, *Constructing a rational cp-matrix whose every cp-factorization is irrational, with GPT-6 Astra*, ResearchGate posting 9 September 2026, DOI 10.13140/RG.2.2.14795.14889; Zenodo deposit https://zenodo.org/records/24126592 (11 November 2026). External reported counterexample, not independently reverified here.
