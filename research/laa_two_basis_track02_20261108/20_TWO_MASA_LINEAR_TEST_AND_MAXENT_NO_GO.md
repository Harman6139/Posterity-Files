# Milestone 20 — polynomial-time TWO-MASA test and dimension-independent maximally-entangled no-go

Date 2026-11-08. This supersedes the mistaken "quadratic equations" description in Milestone 17: for a FIXED first basis, the diagonal commuting-completion equations are LINEAR because any two diagonal corrections commute.

## Theorem 1 (complete linear compatibility test for two MASAs)

Let S=span{H_1,...,H_p} <= S^n be a real symmetric operator space, and fix the first orthonormal basis B1, with diagonal algebra D1. Then a second real orthonormal basis B2 exists with
  S subset D1+D2
if and only if the following FINITE LINEAR SYSTEM in variables delta_(a,i), a=1,...,p, i=1,...,n, is consistent:
  [H_a,H_b]_(i,j)
   +(delta_(a,i)-delta_(a,j)) (H_b)_(i,j)
   -(delta_(b,i)-delta_(b,j)) (H_a)_(i,j)=0
for every pair a<b and every i<j, in coordinates of B1.

Proof. Write Delta_a=diag(delta_(a,1),...,delta_(a,n)). The symmetric matrices H_a-Delta_a commute pairwise exactly when
  [H_a-Delta_a,H_b-Delta_b]=
    [H_a,H_b]-[Delta_a,H_b]-[H_a,Delta_b]=0.
The displayed equation uses the equivalent plus/minus sign convention obtained by replacing delta with -delta; either convention is valid. Because [Delta_a,Delta_b]=0, the system is LINEAR in all delta variables. A common real orthonormal eigenbasis for these pairwise commuting corrected matrices defines D2. Conversely every inclusion into D1+D2 produces such corrections. Gaussian elimination therefore decides compatibility and constructs the corrected commuting family in polynomial arithmetic time for rational/algebraic inputs; common orthogonal eigenvectors can be found algebraically.

**Sign convention.** With corrected matrices B_a=H_a+diag(delta_a), the displayed formula is exactly
 [B_a,B_b]_(i,j)=[H_a,H_b]_(i,j)
 +(delta_(a,i)-delta_(a,j)) (H_b)_(i,j)
 -(delta_(b,i)-delta_(b,j)) (H_a)_(i,j).
For corrections H_a-Delta_a, replace all delta by their negatives. The linear system has p*n variables and binom(p,2)*binom(n,2) scalar equations.

## Theorem 2 (maximally entangled first-basis noncommutativity obstruction)

Let m>=2, r>=m, n=mr, and fix a real ONB B1={psi_j}_{j=1}^n of R^m tensor R^r satisfying
  Tr_aux(psi_j psi_j^T)=I_m/m
for EVERY j. Define source one-body operators
  A=H tensor I_r, B=K tensor I_r
for H,K in S^m. If H and K DO NOT COMMUTE, then
  span{A,B} is NOT contained in D1+D2
for ANY real orthonormal second basis B2, irrespective of r.

More strongly, for ANY diagonal corrections Delta_A,Delta_B in D1,
  ||[A+Delta_A,B+Delta_B]||_F >= ||[A,B]||_F
    =sqrt(r) ||[H,K]||_F >0.                                (1)
Thus there is a positive explicit commutator gap that cannot be removed by corrections.

### Proof

Let C=[A,B]=[H,K] tensor I_r. It is real skew symmetric, and
  ||C||_F=sqrt(r)||[H,K]||_F.
Let E_1 be the orthogonal conditional expectation onto D1, i.e. take the diagonal in B1. Because every psi_j is maximally entangled, for any real symmetric trace-zero Z,
  <psi_j,(Z tensor I_r)psi_j> = <Z,I_m/m> =0.
Hence E_1(Z tensor I_r)=0 for every traceless symmetric Z.

For any diagonal symmetric Delta, cyclicity of trace gives
  <C,[Delta,B]>_F
   =tr(Delta [C,B]).
The double commutator [C,B]=[[H,K],K] tensor I_r is SYMMETRIC and has trace zero, being a commutator. Therefore E_1([C,B])=0 and <C,[Delta,B]>=0. Similarly
  <C,[A,Delta]>_F
   = -tr(Delta[C,A])=0
because [C,A]=[[H,K],H] tensor I_r is symmetric traceless.

Since Delta_A and Delta_B commute,
 [A+Delta_A,B+Delta_B]
   = C+[Delta_A,B]+[A,Delta_B].
The last two terms are Frobenius-orthogonal to C, so
 ||[A+Delta_A,B+Delta_B]||_F^2
 =||C||_F^2+||[Delta_A,B]+[A,Delta_B]||_F^2
 >=||C||_F^2.
It follows that no diagonal corrections can make the two source observables commute. By Theorem 1, no second MASA can contain both A and B modulo D1. QED.

## Corollary (a universal obstruction for the quadratic hybrid normal form)

In Milestone 14 the first real orthonormal basis on R^m tensor R^(2m) is maximally entangled, while the positive decoder is ordinary partial trace D(Y)=Tr_auxY. If the original measurement space L contains any pair H,K with [H,K]!=0, then there is NO second orthonormal basis B2 such that
  D*(L)=L tensor I_(2m) subset D1+D2.
Consequently NO exact two-basis fibre with a positive-definite feasible lift and the SAME partial-trace decoder can enforce all original source constraints solely through the two measured diagonal lists. This remains true even if the ancilla dimension is enlarged arbitrarily and one insists that the first ONB remain uniformly maximally entangled.

This is a dimension-INDEPENDENT no-go for the natural "take a maximally entangled first basis and use a second arbitrary basis to encode general noncommuting measurements" strategy. It does not rule out a non-maximally-entangled first basis, a different decoder, singular lifted fibres, or a nonlinear/tolerance-dependent normal form.

## Corollary (generic noncommutation)

For m>=3 and a generic source measurement space L of dimension >=2, L contains two noncommuting matrices. The commuting-subspace case is exceptional: if a pair H,K in L is chosen generically, [H,K] !=0 unless the entire L is simultaneously diagonalizable. Therefore the maximally-entangled-first-basis construction cannot serve as the universal missing two-basis compiler on generic dense instances.

## Reproducible computational sanity checks

For m=2,3,4, take the realified Weyl maximally entangled basis and sample H=E12, K=E23 (for m=2 replace E23 by diag(1,-1)). Form the linear system of Theorem 1 for diagonal corrections. Direct least-squares gives residual exactly equal to ||[H tensor I,K tensor I]||_F up to numerical precision: m=2 gives 4, m=3 gives sqrt(6), m=4 gives sqrt(8). This confirms the analytical orthogonality identity; numerical checks are not part of its proof.

## Hostile audit

- The prior claim that the equations are quadratic was incorrect; it ignored that all diagonal corrections commute. This file explicitly repairs it.
- The Hilbert-Schmidt inner-product identity is applied to REAL symmetric trace-zero double commutators; the original single commutator is skew, but its double commutators with symmetric H,K are symmetric, so the maximally entangled diagonal property applies correctly.
- The commutator-gap conclusion holds for any choice of correction magnitudes; there is no hidden bounded-coefficient assumption.
- One-body source operators H tensor I_r may have scalar trace; subtracting scalar components does not change their commutator, so the theorem applies to arbitrary symmetric H,K.
- The exact-fibre corollary requires a positive-definite (on minimal support) feasible lift, because source soundness then forces D*(L) into the two measured MASAs by tangent duality. The theorem itself does not require PSD fibres, only operator subspaces.
- Noncommuting is necessary for this particular obstruction; commuting L can evade it by using a suitable product or mixed first basis.
