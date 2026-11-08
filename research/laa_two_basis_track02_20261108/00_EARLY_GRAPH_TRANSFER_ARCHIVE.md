# Archival Track 02 result — sharp graph-completion-to-two-basis recovery transfer

Provenance: reconstructed 2026-11-08 from the earliest Track 02 assistant research response, which originally appeared in the ChatGPT conversation rather than as a separate GitHub document. This file supplies the load-bearing mathematics in a self-contained format. The original submitted manuscript's explicit graph frame is the input; the new result concerns full-ambient NOISY moduli.

## Definitions

Let G be a graph with m vertices, e edges, and pi_G(B) the vector of diagonal and graph-edge entries of B in S^m. Let C_*>0 or >=0 be uniquely completable from pi_G(C_*). Define omega_G(delta)=sup{||B-C_*||_F:B>=0,||pi_G(B-C_*)||_2<=delta}.

The manuscript's frame F in R^{(m+1) x N}, N=3m+2e+2, has
 FF^T=I, FDF^T=0,
with D containing exactly m+1 negative entries -1 and all remaining entries >=2. The frame rank-one projectors span the anchored graph space L_H (old graph plus one anchor connected to every old vertex). Every frame column has a nonzero anchor coordinate; every pair of distinct columns has nonzero inner product; no squared column norm equals 1/2.

Let P=F^TF,Q=I-P,U=P-Q, and X_*=F^T((C_* direct-sum [1]))F. Then U is real orthogonal with all entries nonzero, both observed diagonals at X_* are strictly positive, and the measured exposing certificate
 S_0=D+UDU=2QDQ >=2Q
has kernel ran(F^T).

Define omega_U(delta)=sup{||Y-X_*||_F:Y>=0,||A_U(Y)-A_U(X_*)||_2<=delta}.

## Theorem (exact sharp graph-transfer law)

For every fixed uniquely completable graph instance, including all target ranks,
 omega_U(delta) ~ omega_G(delta)+sqrt(delta)   if C_*!=0,
 omega_U(delta) ~ delta                       if C_*=0.
Both are comparisons of actual worst-case moduli, not merely of selected curves or singularity-degree exponents. In particular every non-Lipschitz graph modulus is preserved up to positive multiplicative constants, while every nonzero Lipschitz target becomes exactly square-root. The optimal local exponents are attained and satisfy
 alpha_U=min(alpha_G,1/2) if C_*!=0, and alpha_U=1 if C_*=0.
Facial-reduction depth changes as max(1,k), rank as rank(C_*)+1, and trace as tr(C_*)+1.

### Proof: all-ambient upper bound

For arbitrary Y>=0, write A=PYP,B=QYQ,K=PYQ, let residuals r_1=diag(Y-X_*), r_2=diag(UYU-X_*), and delta=sqrt(||r_1||²+||r_2||²).

The certificate gives tr B<=kappa delta, kappa=||diag D||/sqrt 2, and ||B||_F<=kappa delta. Since trace is measured, tr Y<=M=trX_*+sqrt N on residual <=1. PSD block Cauchy-Schwarz gives ||K||_F²<=tr A tr B<=M kappa delta.

The essential exact even-odd identity is
  (r_1+r_2)/2=diag(A-X_*+B),
  (r_1-r_2)/2=diag(K+K^T).
The cross block contributes NO error to the averaged compressed measurement list. Thus if Z=FYF^T>=0, the compressed frame residual of Z relative to C_* direct-sum1 is at most (1/sqrt2+kappa)delta.

Because the frame projectors span exactly the anchored graph measurement space, a fixed linear decoder recovers pi_G(Z_old-C_*), the old-anchor cross vector and the anchor scalar error from that residual with a finite operator norm l_G. Let Z=[Z_old,z;z^T,s]. Then
  ||pi_G(Z_old-C_*)|| <= l_G(1/sqrt2+kappa)delta,
  ||z||+|s-1| <= c_G delta.
The principal old block Z_old is PSD for every Y>=0. Therefore the explicit nonlinear PSD retraction
  R(Y)=F^T((Z_old direct-sum [1]))F
is well defined, and
  ||Y-R(Y)||_F <= C_1 sqrt(delta)+C_2 delta.
Also ||R(Y)-X_*||_F=||Z_old-C_*||_F <= omega_G(C_3 delta).
This proves
  omega_U(delta) <= omega_G(C_3 delta)+C_1 sqrt(delta)+C_2 delta.

### Proof: lower bounds and zero exception

For every old PSD competitor B>=0, the lifted Y=F^T((B direct-sum[1]))F is PSD, ||Y-X_*||_F=||B-C_*||_F, and its two-basis residual equals sqrt2 times the compressed frame residual. The latter is comparable above and below to ||pi_G(B-C_*)|| because the anchored projectors span exactly the graph measurement space. Thus omega_U(delta)>=c omega_G(c' delta).

If C_*!=0, then rank X_*=rank C_*+1 >=2. Let R_* project onto ran X_* and set q=N-(m+1)=2m+2e+1. The support-to-exterior cross-block space {K=R_* K Q} has dimension rank(X_*)q>=2q. The diagonal map K->diag(K+K^T) takes values in the (N-1)-dimensional zero-sum hyperplane. Since 2q-(N-1)=m+2e+1>0, a nonzero K exists with diag(K+K^T)=0. Put G=K^T X_*^dagger K>=0. Then
  Y(t)=X_*+t(K+K^T)+t²G
       =(I+t K^T X_*^dagger) X_* (I+t X_*^dagger K)>=0,
has the same rank as X_*, residual Theta(t²), and Frobenius distance Theta(t). This proves omega_U(delta)>=c sqrt(delta).

If C_*=0, X_*=aa^T with a=F^T e_anchor and ALL coordinates a_j nonzero. Any support-to-exterior cross block has form a z^T, with z perpendicular to a. The first diagonal of a z^T+z a^T is 2a.*z, which vanishes only if z=0. The compressed old PSD block and exterior mass are O(delta), and positivity bounds all other cross blocks by O(delta). The remaining anchor-to-exterior cross block is recovered linearly by its diagonal because a has no zero coordinates. Hence omega_U(delta)=O(delta). Scaling the target gives the matching Omega(delta) lower bound.

### PSD moduli dichotomy and attainment

For a compact PSD linear feasibility fibre, either a Lipschitz error bound holds or there is a tangent-kernel vector with nonzero exterior PSD component. Adding a quadratic Schur-complement correction produces PSD competitors at distance Theta(t) and residual O(t²), so any non-Lipschitz modulus satisfies omega(delta)>=c sqrt(delta). Combining with the sharp transfer law gives preservation of every non-Lipschitz source modulus. One-variable semialgebraic growth of the compact worst-case modulus implies a rational exponent is attained for each fixed system.

## Extension to nonsingleton graph fibres

For the entire graph fibre F_G={B>=0:pi_G(B)=g}, replace distance to C_* by distance to F_G in the graph modulus, and distance to F^T((F_G direct-sum[1]))F in the two-basis modulus. The same upper bound uses the PSD retraction and a nearest graph completion; embedded curves give the graph lower bound. If g!=0, choose any nonzero completion to obtain an invisible exterior cross-block curve, whose distance from every exact embedded completion is at least its cross-block norm. The zero-data case is Lipschitz. Thus the same full-fibre modulus law holds without uniqueness.

## Scope and provenance caveats

This result does not require an algebraic/conditioning promise on the target C_*. Constants depend on the fixed graph and frame; the dimension is N=3m+2e+2. A nonzero graph target rank and all ambient competitor ranks are handled. The facial-depth calculation and the explicit graph frame construction are in the original pinned LAA manuscript and the research brief; they are not re-proved line by line in this archival file.

The universal tensor and deterministic diagonal-width extensions developed later in the same conversation appear in the branch's dense_quadratic memoranda. The numerical scripts for the earliest response were provided as conversation artifacts; they were not automatically committed to this GitHub branch.
