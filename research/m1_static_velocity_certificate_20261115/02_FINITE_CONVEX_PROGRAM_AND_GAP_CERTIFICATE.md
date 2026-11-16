# Checkpoint 02 — a finite convex program for the regular escape coefficient

Date: 2026-11-15. This checkpoint proves the finite-dimensional optimization and certificate statements. Checkpoint 03 connects them to ACTUAL plain DRS trajectories. No order-seven resonance proof is a dependency.

## 1. Data extracted from an affine–PSD pair

Let U=a+L in S^m, with a perpendicular to L, be weakly infeasible for S_+^m. All inner products are Frobenius. Define two positive semidefinite cones

    R=L intersect S_+^m,
    N={Y in L^perp intersect S_+^m : <a,Y>=0}.

Let E be the span of the ranges of matrices in R, and F the corresponding span for N. Positive semidefinite orthogonality gives E perpendicular to F. Each span is attained as the range of one matrix in its cone: take a finite collection whose ranges span the desired subspace and add it. Thus there are H0 in R positive definite on E, and G0 in N positive definite on F.

For the program below assume E direct-sum F=R^m. Failure of this condition will later be shown to exclude an interior leading state, not to prove oscillation. In the E,F block coordinates put

    A={H in S(E): H extended by zero belongs to L},
    B={G in S(F): G extended by zero belongs to L^perp},
    C={C: some [[A_E,C],[C*,0]] belongs to U}.

The symbol A here is a matrix subspace, NOT the original measurement operator. Write C=C0+Cdir, where Cdir is its direction space.

### Lemma 1

A and B contain positive definite matrices on their respective coordinate spaces; a is orthogonal to B; C is a nonempty closed affine space and does not contain zero.

Proof. H0 and G0 give the first assertion. For every Y in L^perp intersect S_+^m, weak feasibility implies <a,Y>>=0: pair Y with PSD approximants to U. For any G in B, G0+epsilon G and G0-epsilon G are PSD for sufficiently small epsilon. Their pairings with a are nonnegative and <a,G0>=0, hence <a,G>=0.

Choose u_j in U and v_j PSD with u_j-v_j->0. Then <G0,v_j>->0. Positivity of G0 on F forces (v_j)_FF->0, and hence (u_j)_FF->0. The image of U under F-F compression is a finite-dimensional affine space, therefore closed; it contains zero. The indicated affine slice is nonempty, and its cross-block image C is again closed affine. If 0 belonged to C, an element of U supported on E could be made PSD by adding a sufficiently large multiple of H0, contradicting infeasibility. QED.

All objects above depend only on the affine data. Computing maximal supports may itself require facial analysis; no polynomial bit-complexity assertion is made.

## 2. The convex quadratic semidefinite program

Variables are H in A, C in C0+Cdir, S,Q,R,Z in S(F), with Z in B^perp. Solve

    minimize J(H,R) = ||H||_F^2/4 + ||R||_F^2          (P)
    subject to
        [[H,C],[C*,S]] >= 0,
        Q >= 0,
        R=S+Q-Z,
        H in A, C in C0+Cdir, Z in B^perp.

All constraints are linear or positive-semidefinite constraints. The two quadratic terms can equivalently be represented by rotated second-order-cone epigraphs. No limit, unknown orbit, Puiseux exponent or infinite-time excess occurs in this program.

### Theorem 2: attainment and uniqueness of the relevant coefficient

(P) has a finite positive attained minimum kappa_*. Its pair (H_*,R_*) is unique. Every minimizer has R_* in B intersect S_+(F). Define G_*=2R_*.

Proof. Strict feasibility is obtained with H=H0, any C in C0+Cdir, sufficiently large positive S, Q=I, Z=0 and R=S+Q. For bounded objective, H and R are bounded. Since G0 is positive definite on F and Z is orthogonal to it,

    <G0,R>=<G0,S+Q>.

Both S and Q are PSD, so the bound on R bounds tr(S)+tr(Q). Thus S,Q,Z are bounded. The block PSD constraint gives ||C||_F^2<=tr(H)tr(S), bounding C. Closedness yields compact objective sublevels and attainment. A zero objective would force H=R=0, hence S=Q=0 by the displayed identity and C=0 by block positivity, contradicting 0 not in C.

Strict convexity of J in (H,R), and convexity of the feasible set, imply uniqueness of that pair. For fixed S, minimization over Q,Z gives: variations of Z imply R in B; nonnegative variations of Q imply R PSD; scaling Q towards zero gives <R,Q>=0. Consequently, for every Y in B intersect PSD,

    <S-R,Y-R>=<Z-Q,Y-R>=-<Q,Y><=0.

This is precisely the Euclidean projection characterization, so

    R_*=P_(B intersect PSD)(S_*) .                   (2.1)

QED.

## 3. An explicit dual and exact gap identity

Dual variables are Y11 in S(E), Y12 rectangular, and G in B, with

    Y=[[Y11,Y12],[Y12*,G]] >= 0,
    Y12 perpendicular to Cdir.

Their dual value is

    ell(Y)=-||P_A Y11||_F^2-||G||_F^2/4
                         -2 Re tr(Y12* C0).          (D)

The dual maximizes ell. For EVERY primal feasible point and EVERY dual feasible point, the following identity is exact:

 J-ell = ||H-2P_A Y11||_F^2/4 + ||R-G/2||_F^2
          + <Y,[[H,C],[C*,S]]> + <G,Q> >= 0.         (3.1)

Proof: expand both squares; use R=S+Q-Z, G in B, Z in B^perp, and <Y12,C-C0>=0. Positivity of the last two terms follows from the PSD constraints. This proves weak duality without an external duality theorem. The strictly feasible primal program also satisfies the usual Slater hypothesis, so its standard conic quadratic dual has zero gap and an attained optimum.

Thus a rigorous primal–dual gap is directly available: epsilon=Jhat-ellhat>=0. This is not an estimated numerical error from a floating-point solver log. Feasibility of both certificates must actually be verified to use the bound.

## 4. Interior optimizer and finite algebraic balancing equations

Suppose H_* is positive definite on E and G_*=2R_* is positive definite on F. Then Q_*=0 by <R_*,Q_*>=0. Also

    S_*=C_*^* H_*^(-1) C_* .                        (4.1)

Indeed a nonzero positive Schur slack could be decreased, with first-order objective decrease 2<R_*,slack>>0, contradicting optimality.

Put W=H_*^(-1)C_*. The optimizer then satisfies the FINITE equations

    H in A, G in B, H>0, G>0, C in C0+Cdir,
    HW=C,
    P_Cdir(WG)=0,
    P_A(WGW*)=H/2,
    P_B(C*W)=G/2.                                  (4.2)

To verify the derivatives without assuming differentiability of a matrix eigenbasis, note that the function

    g(S)=||P_(B intersect PSD) S||^2

is continuously differentiable with gradient 2P_(B intersect PSD)S. This follows directly by completing the square in

    g(S)=max_(G in B intersect PSD){<G,S>-||G||^2/4}.

The maximizer is unique, equal to 2P_(B intersect PSD)S. Differentiating the matrix fractional expression C*H^(-1)C gives the three stationarity equations in (4.2). Equivalently they follow from the explicit dual below.

Conversely, ANY solution of (4.2) is a global primal optimizer and determines the unique pair (H_*,G_*). Indeed choose

    S=C*H^(-1)C, Q=0, R=G/2, Z=S-R,
    Y=[[WGW*,-WG],[-GW*,G]]
      =[-W;I] G [-W* I].

This Y is PSD, its off-diagonal block is orthogonal to Cdir, and all primal constraints hold. Every term in the exact gap (3.1) vanishes. The conditions are therefore a checkable algebraic certificate, not a stationarity guess.

Taking the inner products of the final two equations in (4.2) with H,G gives

    ||H||^2/2 = tr(H^(-1) C G C*) = ||G||^2/2.

Consequently, if V=H+G in the original orthogonal blocks,

    ||H||^2=||G||^2,
    kappa_*=(||H||^2+||G||^2)/4=||V||^2/4.          (4.3)

## 5. A finite numerical regularity certificate

Strong convexity supplies, for every primal feasible point,

    Jhat-kappa_* >= ||Hhat-H_*||^2/4
                         +||Rhat-R_*||^2.           (5.1)

For completeness, restrict J to the feasible segment from a minimizer to the point. Its one-sided derivative at the minimizing endpoint is nonnegative; the quadratic expansion leaves exactly the two squared terms in (5.1).

For a primal–dual feasible pair with gap epsilon=Jhat-ellhat, set Vhat=Hhat+2Rhat on the two orthogonal blocks. Then

    ||Vhat-(H_*+G_*)||_F <= 2 sqrt(epsilon).          (5.2)

In particular the finite inequalities

    lambda_min(Hhat)>2sqrt(epsilon),
    lambda_min(2Rhat)>2sqrt(epsilon)                 (5.3)

prove that H_* and G_* are positive definite. Checkpoint 03 will prove that this CERTIFIES the exact unanchored DRS velocity for every starting point. The same gap yields ellhat<=kappa_*<=Jhat and hence certified intervals for its speed constant sqrt(kappa_*).

An exact rational or interval-verified certificate satisfying (5.3) is sufficient. No claim is made that ordinary finite-precision eigenvalues and an unverified solver gap automatically constitute such a certificate.

## 6. Product cones and scope

For a finite product of real symmetric or complex Hermitian PSD cones, use a separate E_i,F_i split and block Schur constraint for each original cone block; use the real trace inner product and SUM the objectives. The subspaces A,B and affine cross-space C may couple all original blocks. Every proof above uses sums of the same trace identities and remains valid. This is not a coordinatewise reduction of a coupled problem to independent instances.

The program is guaranteed to be attained and strictly feasible on the extracted supports. Its interior test is still substantive: a boundary optimizer does not certify resonance or failure of exact velocity. It only fails to certify a fully regular leading spectrum. The exact equivalence and dynamic consequences are proved next.
