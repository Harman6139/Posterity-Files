# Milestone 64 — a strictly positive fixed-order numerical approximation gap for ALL positive spectraplex decoders

Track 02, 2026-11-09. This strengthens the exact 4×4 counterexample in Milestone 62: for ANY FIXED input PSD matrix order d, the bounded rational SDP fibre F from that milestone has a strictly positive Hausdorff distance from EVERY positive linear image of the full trace-normalized PSD spectraplex, even when the decoder and its coefficients vary arbitrarily. No positive right inverse, fixed decoded rank or complete positivity assumption is made. The bound is non-explicit and depends on d; it does not exclude a family with growing d and tolerance-dependent coefficients, nor general two-basis fibres with genuine auxiliary constraints.

## Theorem A — fixed-order positive gap

Let F⊂S^m_+ be any nonempty compact convex set. Fix tau>0 and d>=1. Write
  Δ_d(tau)={Y⪰0 in S^d:trY=tau}.
Define the family of positive linear images
  Q_d={D(Δ_d(tau)):D:S^d→S^m real linear, D(S^d_+)⊂S^m_+}.
Suppose F is NOT in Q_d. Then
  ε_d(F):=inf_{C∈Q_d} d_H(C,F)>0,                 (1)
where d_H is Hausdorff distance in Frobenius norm.
In particular if cone(F) has nonspectrahedral dual, the assumption F∉Q_d holds for EVERY d by Milestone 62, so ε_d(F)>0 for all fixed d.

### Proof (compactness with no decoder-norm hypothesis)

Assume instead ε_d(F)=0. Choose positive linear D_n with
  d_H(D_n(Δ_d(tau)),F)→0.
Let M=max_{X∈F}||X||_F <infinity. For any unit vector v∈R^d, τ vv^T belongs to Δ_d(tau). Therefore
  ||D_n(vv^T)||_F <=(M+1)/tau
for all sufficiently large n, uniformly over all unit v.

These bounds imply a UNIFORM operator norm bound on the full linear maps D_n:S^d→S^m. Indeed D_n(e_i e_i^T) are uniformly bounded, and with q_ij=(e_i+e_j)/sqrt2,
  e_i e_j^T+e_j e_i^T
    =2 q_ijq_ij^T−e_ie_i^T−e_je_j^T.
Thus the images of a fixed basis of S^d are bounded. Finite dimensionality gives a convergent subsequence D_n→D in operator norm.

The cone-positive property is closed: for any Y⪰0, D_n(Y)⪰0 and D_n(Y)→D(Y), so D(Y)⪰0. Because Δ_d(tau) is compact, uniform convergence of D_n on Δ_d(tau) gives
  d_H(D_n(Δ_d(tau)),D(Δ_d(tau)))→0.
Combining with d_H(D_n(Δ_d(tau)),F)→0 yields
  D(Δ_d(tau))=F,
contradicting F∉Q_d. Hence ε_d(F)>0. QED.

## Theorem B — explicit rational 4×4 SDP cannot be approximated arbitrarily at fixed input order

Take the source F from Milestone 62:
  F={X⪰0 :
      X13=X14=X23=X24=X34=0,
      X11−X22−2X33=0,
      X12−X44=0,
      trX=6}.
It is compact, strictly feasible and has rational measurement coefficients.
Its conic hull is linearly isomorphic to
  { (t,x,y):t>=sqrt(x²+y²), x>=0, y>=0 }.
Its dual has a nonexposed extreme point in a disk-plus-positive-quadrant affine section, hence is not spectrahedral. Milestone 62 therefore proves no positive linear decoder of ANY order maps Δ_d(6) EXACTLY onto F.

By Theorem A, for EVERY fixed integer d>=1 there exists ε_d>0 such that
  d_H(D(Δ_d(6)),F) >=ε_d
for every positive linear D:S^d→S⁴, irrespective of its coefficient magnitudes or its Kraus rank if CP.

Consequently a fixed-order/tolerance-varying version of the Milestone 61 spectraplex-only strategy cannot achieve arbitrarily accurate two-sided recovery/optimization over this source fibre. A growing-order strategy could still approximate F and is not addressed by this statement.

## Theorem C — uniform closedness and trace-normalization refinement

If the positive decoders are additionally assumed to be TRACE PRESERVING, the family of maps is itself compact at fixed d,m: each D(e_ie_i^T) is PSD with trace one, hence bounded; rank-one projector bounds extend to all of S^d as above. The same positive approximation gap follows immediately and may be expressed as a compact minimization over a semialgebraic set of decoder coefficients. For rational F and fixed d, ε_d is positive and in principle can be bounded using quantifier elimination over real closed fields, though no polynomial-in-d lower bound or efficient algorithm is claimed.

## Exact limitation relevant to the frontier

The theorem rules out only decoders applied to the ENTIRE PSD spectraplex. A genuine two-basis PSD fibre
  T={Y⪰0:diag_B1 Y=a,diag_B2Y=c}
is a proper constrained spectrahedron, not the whole spectraplex. Its positive decoder image may have nonspectrahedral dual; the 4×4 example is not proved impossible in that wider model. This is why the full \(N=O(m²+p)\) many-to-one frontier remains unresolved.

The proof is self-contained finite-dimensional compactness and does not claim novelty of general Hausdorff/semialgebraic closure theory.
