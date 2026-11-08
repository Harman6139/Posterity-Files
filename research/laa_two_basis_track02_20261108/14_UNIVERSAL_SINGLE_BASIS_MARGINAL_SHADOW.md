# Milestone 14 — exact quadratic-size positive MARGINAL representation using one maximally entangled basis and arbitrary observables

Date 2026-11-08. This is a sharp universal hybrid normal form, but **NOT** a two-orthonormal-basis universality theorem: it uses one complete orthonormal-basis diagonal plus p-1 additional, generally noncommuting subsystem quadratic observables. Its purpose is to isolate exactly the final two-MASA obstruction.

## Theorem 1 — universal quadratic-size marginal shadow

Let A:S^m -> R^p be a real trace-controlled linear map, with nonempty PSD fibre F_b. Normalize so trace belongs to range(A*), and choose an independent basis of the measurement space consisting of I and H_1,...,H_h, h=rank(A)-1. Let tau>0 be the prescribed trace (tau=0 is trivial). Put r=2m and n=mr=2m^2.

There exists an explicit REAL orthonormal basis Psi={psi_j}_{j=1}^n of R^m tensor R^r such that every psi_j has the same partial trace:
  Tr_aux(psi_j psi_j^T)=I_m/m.

Define the hybrid PSD spectrahedron
 T_b={Y>=0 in S^n:
       psi_j^T Y psi_j=tau/n (all j=1,...,n),
       <H_a tensor I_r,Y>=b_a (a=1,...,h)}.
Define positive linear partial-trace decoder D(Y)=Tr_aux Y and positive linear encoder
  E(X)=(X tensor I_r)/r.
Then for EVERY feasible b, without restricting the rank of Y:
  D(T_b)=F_b,
  D(E(X))=X for all X>=0,
  E(F_b) subset T_b.
Moreover
  ||E(X)-E(Z)||_F=||X-Z||_F/sqrt(r),
  ||D(Y)-D(Z)||_F<=sqrt(r)||Y-Z||_F,
and every source objective is preserved EXACTLY for every symmetric Y:
  <C,D(Y)>=<C tensor I_r,Y>.
The original residual is exactly the norm of the additional subsystem expectation residuals:
  <H_a,D(Y)>-b_a = <H_a tensor I_r,Y>-b_a.
Thus there is no square-root deterioration in decoded residuals or objective errors; all feasible-set shadows are exact and decoding is globally PSD-positive.

If tau=0, the only source point is X=0, and the zero matrix Y=0 is the unique PSD matrix with all first-basis diagonal entries zero.

## Proof of the real maximally entangled basis

For each a,b in {0,...,m-1} let W_ab be the m-by-m complex Weyl matrix
 (W_ab)_{j,k}=1_{k=j+a (mod m)} exp(2*pi*i*b*j/m).
They satisfy W_ab W_ab*=I and tr(W_ab W_cd*)=m delta_ac delta_bd. In R^{m x 2m}, define real matrices
  Q_ab^R = [Re W_ab, Im W_ab]/sqrt(m),
  Q_ab^I = [-Im W_ab, Re W_ab]/sqrt(m).
Vectorizing these 2m^2 real matrices yields a real orthonormal basis. Indeed the real Hilbert-Schmidt inner product of Q_ab^R and Q_cd^R, or of Q_ab^I and Q_cd^I, is Re tr(W_ab W_cd*)/m; the real-inner-product cross term is Im tr(W_ab W_cd*)/m=0. Each Q has orthonormal rows up to factor 1/sqrt(m), since Re(W)Re(W)^T+Im(W)Im(W)^T=I_m and similarly for the (-Im,Re) pair. Therefore Tr_aux(psi psi^T)=Q Q^T=I_m/m.

For X>=0 of trace tau,
  psi^T E(X) psi = (1/r) tr[X Tr_aux(psi psi^T)] = tau/(mr)=tau/n.
The partial trace of every Y>=0 is PSD and its trace equals tr Y. Since the first-basis diagonal constraints fix trY=tau, D(Y) has trace tau. The additional constraints satisfy
 <H_a,D(Y)>=<H_a tensor I_r,Y>=b_a.
Hence D(T_b) subset F_b. Conversely E(X) belongs T_b for every X in F_b and D(E(X))=X, proving exact surjectivity.

The norm identities follow from elementary tensor Frobenius multiplication and the partial-trace operator norm sqrt(r). The objective identity is the definition of the adjoint of partial trace. QED.

## Theorem 2 — optimal dimension of a uniform maximally entangled basis architecture

Suppose Psi is an orthonormal basis of R^m tensor R^r such that every psi has reduced density I_m/m. Every psi then has Schmidt rank m, since the reduced matrix has rank m. But Schmidt rank is at most r, so r>=m. Consequently n=mr>=m^2. Our explicit real construction attains n=2m^2 and is within factor two of this architecture's minimal possible dimension. This is NOT a lower bound for arbitrary PSD shadows.

## Exact two-MASA compatibility criterion

Let D_1,D_2 be the subspaces of real symmetric matrices diagonal in two orthonormal bases on R^n. Let D be a positive linear decoder S^n -> S^m, and let F_b contain a positive definite source state X_0. Suppose the ambient two-basis fibre T={Y>=0:diag_{B1}Y=a,diag_{B2}Y=c} has a positive definite feasible Y_0 and D(T)=F_b. Then NECESSARILY
  D*(range A*) subset D_1+D_2.
Proof: at Y_0>0, the affine tangent space of T is (D_1+D_2)^perp. Any tangent H has both positive and negative small feasible variations, so A(D(H))=0, giving D*A*lambda in (ker measured map)^perp=D_1+D_2. Conversely, if this inclusion holds and the measured target data pair to b under the induced linear combination, then every Y in T decodes to F_b; completeness requires a separate lifting argument.

For the partial-trace decoder, D*(H)=H tensor I_r. Thus ANY attempt to replace all extra H_a tensor I_r expectations of the hybrid theorem by a SECOND FULL ORTHONORMAL BASIS, while preserving an exact positive-definite interior and the same decoder, must solve the noncommutative inclusion
  L tensor I_r subset D_1 + D_2.
This is the precise two-MASA bottleneck. It is not settled by the existence of the maximally entangled first basis, by Naimark alone, or by spanning rank-one POVMs.

## Hostile audit

- The hybrid is NOT advertised as a full two-basis construction; the extra H_a tensor I_r constraints may be noncommuting and not diagonals in any single basis.
- Surjectivity is exact for every PSD matrix rank, and source positivity is inherited from partial trace, not from an assumed fixed-rank Gram factor.
- The constant first-basis outcomes are strictly positive for tau>0.
- Choosing r=2m permits a REAL explicit basis for all m, avoiding unsupported claims about real orthogonal error bases of order m for arbitrary m.
- Objective and linear residual decoding are exact; ambient distance to the entire hybrid fibre may exhibit additional instability, so no ambient bi-Hölder exponent is asserted.
- The two-MASA condition is necessary under a positive-definite lifted feasible point; without strict feasibility one must compress to the minimal face first.
