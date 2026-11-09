# Milestone 61 — explicit coherent CP quadratic-size TWO-BASIS quotient of a bounded noncommuting arrow SDP

Research Track 02, 2026-11-09. This is a genuine **POSITIVE CONSTRUCTIVE** step toward the still-open general \(N=O(m^2+p)\) many-to-one frontier. We explicitly realize a bounded rational trace-controlled SDP with a curved rank-\((m-1)\) boundary and an open family of kernel directions as the exact positive-decoder image of TWO real orthonormal-basis PSD diagonals of order \(N=2m^2\). The decoder is a coherent, non-entanglement-breaking CP map with no positive affine right inverse, so it demonstrably evades the strong-positive-retract, entanglement-breaking, and ordinary-partial-trace two-MASA obstructions. The construction has exact objective preservation and a LIPSCHITZ decoded source residual against all ambient PSD matrices. It is **NOT** an unrestricted theorem for all dense SDPs: the source arrow cone is rotated-second-order-cone representable.

## 1. The rational source SDP

Fix \(m\ge3\) and let \(V\subset S^m\) be the \(m\)-dimensional trace-zero arrow subspace
  V={ [[t,v^T],[v, -t/(m-1) I_(m-1)]] : t in R, v in R^(m-1) }.
Choose any rational linear measurement A:S^m ->R^p with ker A=V, where p=D_m-m and D_m=m(m+1)/2, and let b=A(I_m). This is trace-controlled since every V element is traceless; I_m lies in range A*. The exact source fibre is
  F={X(t,v)=[[1+t,v^T],[v,(1-t/(m-1))I_(m-1)]] >=0}.
It is compact, nonempty, and contains I_m>0. Write the generic arrow matrix as
  X(a,v,beta)=[[a,v^T],[v,beta I_(m-1)]].
It belongs to the arrow PSD cone K_arrow iff a>=0,beta>=0 and a beta>=||v||² (with the usual v=0 convention when beta=0). In F, a+(m-1)beta=m. Hence F is an affine trace-m section of a rotated second-order cone, despite the large number p=Theta(m²) of source measurements.

The boundary contains an open family of rank-(m-1) kernel directions: for a,beta>0 and ||v||²=a beta the null vector is (1,-v/beta). This is exactly the arrow family used in Milestone 58's entanglement-breaking decoder impossibility theorem.

## 2. The coherent star-Kraus CP cone quotient

For each i=2,...,m define the real skew m-by-m matrix
  B_i=e_i e_1^T-e_1 e_i^T.
Define the real CP map R:S^m->S^m,
  R(Y)=sum_(i=2)^m B_i Y B_i^T.
For a block matrix Y=[[z,w^T],[w,Z]] this has the EXACT form
  R(Y)=[[tr Z, -w^T],[-w, z I_(m-1)]].                (2.1)

**Theorem A (exact cone image).**
  R(S^m_+)=K_arrow.                                    (2.2)

Proof. Positivity follows from the Kraus representation, and every output has the required arrow shape, so R(S_+^m)⊂K_arrow.

Conversely, take X=[[a,v^T],[v,beta I]]≥0.
If beta>0, Schur complement gives a>=||v||²/beta. Set
  z=beta, w=-v,
  Z= vv^T/beta +[(a-||v||²/beta)/(m-1)] I_(m-1).
Then tr Z=a and the Schur complement Z-ww^T/z is PSD, so
  Y_X=[[beta,-v^T],[-v,Z]]≥0,
  R(Y_X)=X.
If beta=0, PSD forces v=0, a>=0. Choose
  Y_X=diag(0,(a/(m-1)) I_(m-1))≥0
and R(Y_X)=X. This establishes (2.2), including all boundary ranks.

The output trace obeys
  tr R(Y)=tr(QY), Q=diag(m-1,1,...,1)>0.              (2.3)
Hence the positive congruence Y->Z=Q^(1/2)YQ^(1/2) converts the weighted-trace slice to a NORMALIZED spectraplex:
  R({Y≥0:<Q,Y>=m}) = F
  D_star({Z≥0:trZ=m}) = F,
where
  D_star(Z)=R(Q^(-1/2) Z Q^(-1/2)).                    (2.4)
This is globally CP and positive, and importantly maps EVERY positive input Z into the cone over F (scaled by trZ/m), not merely all target-feasible Z.

## 3. Nonlinear lifting is ESSENTIAL: no affine positive section

For a rank-(m−1) arrow matrix
  X_v=[[1,v^T],[v,I_(m−1)]], ||v||=1,
the preimage under R is UNIQUE and rank one:
  Y_v=[[1,-v^T],[-v,vv^T]]
      =(1,-v)(1,-v)^T.                                (3.1)
Indeed any PSD preimage has z=1, w=-v and tr Z=1, while the PSD Schur complement forces Z>=vv^T of the same trace, so Z=vv^T.

For distinct unit leaf vectors u,v (possible for m>=3), the original matrices satisfy
  (X_u+X_(-u))/2
   =(X_v+X_(-v))/2
   =X_0=[[1,0],[0,I_(m−1)]].
But their uniquely forced positive preimages satisfy
  (Y_u+Y_(-u))/2=diag(1,uu^T)
  and
  (Y_v+Y_(-v))/2=diag(1,vv^T),
which differ. Therefore there is NO affine map J:F→S^m_+ with R(J(X))=X for every X in F. In particular R has no globally positive linear right inverse for this cone.

After fixed invertible Q congruence, the same no-affine-section obstruction applies to D_star. This shows the construction genuinely escapes the exact-positive-retract model rather than reparameterizing it.

Since R maps PSD matrices ONTO the arrow cone with an open family of rank-(m−1) kernel directions, it cannot be an entanglement-breaking CP map of finite measure-and-prepare form, by the independent direct cone-geometric theorem of Milestone 58. Its Kraus correlations are essential.

## 4. Two actual real orthonormal bases, order N=2m²

Set r=2m, N=mr=2m². As constructed explicitly in Milestone 19, there is a REAL ONB \(\psi_1,...,\psi_N\) of R^m⊗R^r such that each has maximally mixed first marginal
  Tr_aux(\psi_j\psi_j^T)=I_m/m.
One explicit basis is the realification of all m² complex Weyl unitaries, yielding 2m² real vectors \(\mathrm{vec}([\Re W,\Im W])/\sqrt m\) and \(\mathrm{vec}([-\Im W,\Re W])/\sqrt m\).

For generic real orthogonal R_aux∈SO(r), the second basis
  \psi'_j=(I_m⊗R_aux)\psi_j
is also maximally entangled. Every overlap <\psi_i,\psi'_j> can be chosen NONZERO by finite polynomial avoidance (each is a nonzero linear functional on SO(r), and there are finitely many). The bases are distinct and their transition is generically non-involutory.

Let the target two-basis data be the strictly positive uniform lists
  y=( (m/N)1_N, (m/N)1_N )
    =( (1/(2m))1_N, (1/(2m))1_N ).
Let
  T={W≥0 in S^N: diag_(psi) W=diag_(psi')W=(m/N)1_N}.
Let rho(W)=Tr_aux W be the ordinary positive partial trace, and define the COMPOSITE positive CP decoder
  D_final(W)=D_star(rho(W))
            =R(Q^(-1/2) rho(W) Q^(-1/2)).         (4.1)

**Theorem B (exact true TWO-BASIS surjective recovery).**
  D_final(T)=F.                                       (4.2)
All ambient PSD ranks are allowed; no positive linear encoder or bijective feasible-fibre embedding is asserted.

Proof (soundness). If W∈T, the first measured basis fixes trW=m. Thus rho(W)≥0,trrho=m. By (2.4), D_star(rho(W))∈F.

Proof (completeness). For every X∈F, use the explicit Schur positive preimage Y_X≥0 of Section 2, and set Z_X=Q^(1/2)Y_XQ^(1/2)≥0. Equation (2.3) gives trZ_X=trX=m. Set
  W_X=(Z_X⊗I_r)/r≥0.
Then rho(W_X)=Z_X, so D_final(W_X)=X. Every first/second ONB vector has reduced matrix I/m, hence both basis outcomes are
  \psi_j^T W_X\psi_j=(1/r)tr(Z_X I_m/m)=m/(rm)=m/N,
the prescribed data. Thus W_X∈T, proving (4.2).

## 5. Quantitative all-PSD decoded recovery and exact optimization

For EVERY symmetric ambient W and source cost matrix C,
  <C,D_final(W)>
   =< (Q^(-1/2) R*(C) Q^(-1/2))⊗I_r , W>.      (5.1)
Thus the source linear objective is represented EXACTLY by an ambient linear cost \(\widetilde C\), not just on feasible points. All objective values and optimum values over the exact feasible sets coincide by (4.2).

Let δ=||(diag_(psi)W,diag_(psi')W)-y||_2 for any W≥0. Both lists sum to s=trW, and both targets sum to m, so
  |s-m| <=sqrt(N/2) δ.                                (5.2)
The decoder output X=D_final(W)≥0 always has arrow form and trace
  tr X=trW=s
by (2.3) and rho trace preservation. Thus X lies in the homogeneous arrow cone K_arrow at trace s. If s>0, the rescaled
  X'=(m/s)X
lies in F and obeys
  ||X-X'||_F=(|s-m|/s)||X||_F<=|s-m|.
If s=0 then X=0 and choosing I_m∈F gives dist(0,F)<=||I_m||_F=√m<=m=|s-m|. Therefore the sharp global soundness estimate
  dist_F(D_final(W),F)<=sqrt(N/2)δ=m δ.         (5.3)
This holds for EVERY PSD ambient competitor, without a rank bound or local small-residual assumption.

For the original source data A(X)=b (X∈F), any arrow X with trace s satisfies
  A(X)=(s/m)b,
because its deviation from (s/m)I lies in the trace-zero arrow kernel V. Hence the ORIGINAL SDP residual is also linearly controlled:
  ||A(D_final(W))-b||_2
     =(|s-m|/m)||b||_2
     <=(||b||_2/m)sqrt(N/2)δ=||b||_2 δ.       (5.4)
This is an explicit polynomial (indeed linear) condition bound, with arbitrary ambient PSD competitors.

The preceding equations demonstrate a genuine approximation-preserving optimization/recovery reduction for this entire rational SDP arrow family: any nearly feasible two-basis point decodes to a source PSD point with O(δ) affine residual, and its objective value is the original cost value EXACTLY.

## 6. Complexity, rank, geometry and limits

The number of independent source measurements is p=D_m−m=Θ(m²), and the two-basis ambient order is N=2m²=O(m²+p). All formulas are finite algebraic; real Weyl basis coefficients are roots of unity and square roots, and a second generic ancilla rotation can be found by verified finite rational/algebraic parameter avoidance. Given a source PSD matrix, a witness lift is obtained using a Schur complement and a tensor product in polynomial algebraic operations; at beta=0 use the explicit limiting formula.

This source fibre is **special**: its arrow PSD cone is a rotated second-order cone and its polar has a small spectrahedral representation. Its constraints may be dense/noncommuting after a rational orthogonal conjugation, but this is not a generic dense SDP family. Do NOT infer that an arbitrary trace-controlled SDP admits such a cone quotient.

This result does NOT establish:
 - an exact ONE-TO-ONE positive-linear source encoding (indeed a positive affine section is IMPOSSIBLE here);
 - a two-basis encoding in which the second list carries distinct SOURCE-dependent data (the two bases themselves are genuinely distinct, but both target lists are uniform);
 - strict preservation of the source worst-case recovery modulus as a map between all ambient points (this is a surjective quotient, not an isometric embedding);
 - unrestricted N=O(m²+p) universality for all rational SDPs;
 - unconditional polynomial-Turing-bit exact SDP feasibility.

It DOES prove a complete coherent-CP, non-Jordan, nonlinear-lift, all-rank, polynomially conditioned, exact **TWO-BASIS** SDP normal form for a nontrivial bounded rational noncommuting family, and demonstrates a viable construction mechanism that escapes the earlier architecture-restricted lower bounds.
