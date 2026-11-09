# Milestone 63 — COMPLETE dual-LMI criterion and exact positive two-basis quotient for every bounded PSD cone with a spectrahedral dual

Track 02, 2026-11-09. Theorems are proved below and valid over REAL symmetric PSD matrices. This is the exact positive counterpart to the explicit 4×4 impossibility in Milestone 62. It generalizes the special coherent-CP arrow SDP of Milestone 61 to ANY bounded trace-controlled spectrahedral cone with an explicit LMI representation of its dual. The resulting two-ONB ambient order is N=2d², where d is the DUAL LMI order, and its decoder is positive, trace-preserving and uniformly Lipschitz on all ambient PSD competitors. It is **not** a universal O(m²+p) result for arbitrary bounded rational SDPs: some source PSD cones have nonspectrahedral duals (Milestone 62), and d may be much larger than m.

## Theorem A — quadratic two-basis shadow for every dual-spectrahedral cone

Let E⊂S^m be a finite-dimensional real linear subspace and let K⊂E∩S^m_+ be a closed pointed cone spanning E, with nonempty interior relative to E. Assume the matrix-trace functional e(X)=tr X lies in int_E*(K*). Fix tau>0 and the compact PSD base
  F_tau={X∈K:tr X=tau}.
Suppose its dual cone has a homogeneous LMI representation of order d:
  K*={H∈E : B(H)⪰0},
where B:E→S^d is real linear. After deleting a common kernel, suppose B(e)>0.

There exist TWO complete REAL orthonormal bases in R^N, N=2d², with transition matrix U∈O(N) having NO zero entries, strictly positive uniform target observations y=(tau/N)1_(2N), and a globally positive trace-preserving LINEAR decoder
  D:S^N→S^m
such that
  D({W⪰0:diag_B1(W)=diag_B2(W)=tau/N})=F_tau.          (1)
No positive right-inverse encoder, unique lifted fibre, rank bound or prescribed target support is required.

Every original cost C∈S^m has an explicit lifted cost \tilde C∈S^N satisfying
  <\tilde C,W>=<C,D(W)>
for EVERY symmetric W, and hence all exact linear optimization objectives and optimal values coincide across the two feasible sets.

For EVERY ambient PSD competitor W and full two-basis measurement residual
  delta=||(diag_B1 W,diag_B2 W)-y||_2,
its decoded source satisfies the GLOBAL, unrestricted-rank estimates
  dist_F(D(W),F_tau)<=d delta,                           (2)
  |tr D(W)-tau|<=d delta.                               (3)
For any source measurement operator A satisfying F_tau={X⪰0:A(X)=b}, and for which the cone over F_tau is exactly K,
  A(D(W))=(trW/tau)b,
  ||A(D(W))-b||=(||b||/tau)|trW-tau|
              <=(||b||d/tau)delta.                    (4)
The zero-input case is included by interpreting the coefficient as zero.

The construction is finite algebraic once B is supplied, with weak numerical complexity controlled by lambda_min(B(e)), the size of B, and the chosen orthogonal matrix precision. No claim of uniform bit-polynomial construction of an LMI B for an arbitrary input cone is made.

## Proof: normalize an arbitrary dual LMI to a trace-preserving PSD quotient

Milestone 62 proves (and here we summarize) that any homogeneous dual LMI for K* can be compressed to the common support so that B(e)>0. Its adjoint L=B*:S^d→E has closed PSD image K:
  L(S^d_+)=K.
The key closedness estimate is
  <e,L(Z)>=<B(e),Z>>=lambda_min(B(e))trZ
for Z⪰0, which bounds the PSD preimages of a convergent output sequence. The dual image is K* by self-duality, so the image equals K by the bipolar theorem.

Put P=B(e)^(1/2) and
  Phi(Z)=B*(P^(-1) Z P^(-1))∈E⊂S^m.
Then Phi(S^d_+)=K and
  tr Phi(Z)=<e,Phi(Z)>=trZ
for EVERY symmetric Z. It follows that
  Phi({Z⪰0:trZ=tau})=F_tau.

## Proof: two maximal-entanglement real bases with exact partial-trace shadow

Let r=2d,N=dr=2d². A complete REAL maximally entangled ONB of R^d⊗R^r exists for every d: realify all d² complex Weyl matrices W_ab, using the 2d² real matrices
  A_ab^R=[Re W_ab, Im W_ab]/sqrt(d),
  A_ab^I=[-Im W_ab,Re W_ab]/sqrt(d).
Their real vectorizations form a complete real ONB and all have row Gram
  A A^T=I_d/d.
The orthogonality follows from the complex Weyl Hilbert–Schmidt identity tr(W_ab W_cd*)=d δ_acδ_bd; the real and imaginary copies are also mutually orthogonal.

For a generic auxiliary rotation Q∈SO(2d), the vectors vec(A_j Q) give a SECOND real maximally entangled ONB. Each cross overlap is
  tr(A_i^T A_j Q),
a nonzero linear polynomial on SO(2d). Finite avoidance chooses Q with ALL overlaps nonzero and with second basis genuinely different. The dependence of these bases on B is NONE.

Write rho(W)=Tr_aux W. Define the two-basis PSD fibre
  T_tau={W⪰0:diag_B1(W)=diag_B2(W)=(tau/N)1_N}.
For any Z⪰0 of trace tau, the positive tensor state
  E0(Z)=(Z⊗I_r)/r
has both diagonal lists equal tau/N, because each basis vector has first marginal I_d/d. Also rho(E0(Z))=Z.
Conversely any W∈T_tau has trW=tau from its first diagonal, so rho(W)⪰0,trrho(W)=tau. Therefore
  rho(T_tau)={Z⪰0:trZ=tau}.
Define
  D(W)=Phi(rho(W)).
It is positive and trace preserving as a composition, and
  D(T_tau)=Phi(rho(T_tau))=F_tau,
proving exact surjectivity (1). For each source X∈F_tau, any PSD Z with Phi(Z)=X gives a concrete feasible lift W=E0(Z), proving completeness without invoking a positive affine section.

## Proof: objective and all-ambient quantitative estimates

The adjoint decoder is
  D*(C)=Phi*(C)⊗I_r,
so the ambient source cost is
  \tilde C=Phi*(C)⊗I_r.
This proves objective equality for all symmetric W.

For W⪰0 let s=trW=trD(W). By the two full diagonals, each with N entries summing to s, and both target lists summing to tau,
  delta²>=2(s-tau)²/N,
hence
  |s-tau|<=sqrt(N/2)delta=d delta.
Since D(W)∈K and trD(W)=s, if s>0 then X'=(tau/s)D(W)∈F_tau and
  ||D(W)-X'||_F
   =|s-tau| ||D(W)||_F/s
   <=|s-tau|,
since D(W)⪰0 implies ||D(W)||_F<=trD(W)=s.
If s=0 then D(W)=0, and any X'∈F_tau satisfies ||X'||_F<=tau. This proves (2)-(3) for every PSD W, independent of its rank.

For a source linear measurement A with exact fibre F_tau, every nonzero X∈K is a positive multiple of a member of F_tau. Thus linearity gives A(X)=(trX/tau)b on all of K, including X=0. Substitute X=D(W) and apply the trace inequality to obtain (4).

## Converse and exact architectural boundary

Suppose for some n there is ANY linear map Phi:S^n→E satisfying
  Phi({Z⪰0:trZ=tau})=F_tau.
Scaling shows Phi(S^n_+)=K; duality gives
  K*={H:Phi*(H)⪰0},
so K* MUST be spectrahedral. Conversely the preceding construction gives such a quotient whenever K* is spectrahedral. Therefore:

> A bounded PSD cone section can be reduced to two uniform maximally entangled real basis diagonals by composing ordinary partial trace with a source-positive linear quotient of an unconstrained spectraplex **if and only if the source cone has a spectrahedral dual**.

This is a precise necessary-and-sufficient CLASSIFICATION of the Milestone 61 architecture. The dual LMI order d controls the achieved two-basis ambient order 2d². It is not a converse for an arbitrary two-basis PSD fibre with additional genuine linear constraints or an arbitrary decoder that is not positive on the full input PSD cone.

The explicit rational 4×4 trace-controlled example in Milestone 62, whose cone is Lorentz_3∩{x≥0,y≥0}, has dual Lorentz_3+R_+e_x+R_+e_y with a nonexposed extreme point in its s=1 section. Hence its dual is NOT spectrahedral and it cannot be represented by THIS method at ANY n. Such sources force genuinely active two-basis auxiliary constraints or a different decoder architecture.

## Scope and adversarial audit

- Dual-LMI size d may be greater than m; the bound N=2d² is near-quadratic in the LMI size of the DUAL cone, not automatically in the original matrix order m.
- The two basis lists are both UNIFORM on all feasible tensors; the bases are genuinely distinct with no zero overlaps, but the second list does not encode independent source-observable values. This is deliberate: all source constraints are encoded in the positive quotient itself.
- Decoder positivity is global, trace is globally preserved, and the objective adjoint identity holds on ALL symmetric W, not only feasible ones.
- Source decoded soundness and distance are Lipschitz for EVERY PSD ambient W, while no isometric/bijective feasible-fibre model is claimed.
- The 4×4 counterexample shows the architecture cannot be universal at ANY order, so no blanket claim of N=O(m²+p) for arbitrary rational SDPs is made.
- All arguments work over REAL PSD cones. The complex Weyl matrices are merely a source of an explicitly REAL orthonormal basis via realification, not a change of the SDP field.
- Exact source lifting Z for a given feasible X may require a nontrivial PSD inversion of Phi; the theorem proves existence and gives explicit construction in the cone-image sense. Computing a particular lift with polynomial bit cost requires the normal conditioning/feasibility promises for that auxiliary SDP.
- The theorem's elementary conic-polarity classification has classical antecedents in spectrahedral duality and is not claimed to be historically original without literature audit.
