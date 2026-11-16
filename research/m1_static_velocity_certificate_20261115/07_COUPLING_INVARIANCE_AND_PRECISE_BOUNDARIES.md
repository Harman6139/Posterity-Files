# Checkpoint 07 — arbitrary affine coupling can leave the escape coefficient unchanged

Date: 2026-11-15. This gives a second arbitrary-order, explicitly solvable application of the finite certificate and records routes that remain incomplete.

## 1. A coupled family, not a direct sum of independent algorithms

Fix r,s>=1 and a nonzero rectangular C0 in R^(r by s). Let Amap:S_0^s->S^r and Dmap:S_0^s->R^(r by s) be ANY linear maps, where S_0^s denotes the trace-zero symmetric matrices. Define

 U={ [[t I_r+Amap(S), C0+Dmap(S)],
       [C0*+Dmap(S)*, S]] : t real, S in S_0^s }.

All projections use the original Frobenius metric. No bound on the coupling maps is imposed.

### Theorem

This pair is weakly infeasible. Set c=||C0||_F and

    h=sqrt(2)c/(rs)^(1/4),
    g=sqrt(r/s) h,
    V=diag(h I_r,g I_s).

For EVERY start, its plain affine-first DRS orbit satisfies

    Z_k=V sqrt(k)+O(log k),
    Z_(k+1)-Z_k=V/(2sqrt(k))+O(log(k)/k),
    sqrt(k)||Z_(k+1)-Z_k||_F -> (r/s)^(1/4)c.

The affine and PSD shadow cross blocks both tend to C0. The coefficient V is COMPLETELY INDEPENDENT of the two coupling maps, although the transients, constants in the error bounds and stationary normal correction can depend strongly on them.

### Proof

A PSD member of U has a PSD lower block S with trace zero, hence S=0. Its zero lower block would force C0=0, a contradiction. The matrices with upper block tI_r, cross block C0 and lower block C0*C0/t are PSD and approach U at rate O(1/t), proving weak infeasibility.

In the direction space, any PSD matrix must again have S=0, so its range lies in the upper r coordinates; the direction diag(I_r,0) is positive there. Any PSD matrix in L^perp annihilates that direction, hence is supported on the lower s coordinates. Orthogonality to every trace-zero S makes it a scalar multiple of I_s. Thus the canonical supports are complementary, A=span(I_r), B=span(I_s), and the zero-F-F cross slice is exactly {C0}.

For H=h I_r, the Schur-minimal S in the static program is C0*C0/h. Its projection onto B is [c^2/(s h)] I_s. The scalar objective is therefore

    r h^2/4+c^4/(s h^2).

Its unique minimizer satisfies h^4=4c^4/(rs); G=2R=[2c^2/(s h)]I_s=g I_s. Both are positive. Theorem A of Checkpoint 03 applies and gives the result. The optimum is sqrt(r/s)c^2, yielding the claimed speed. None of these reduced objects depends on Amap or Dmap. QED.

## 2. Fully rational order-four illustration

Take r=s=2 and C0=diag(1,0). Then V=I4 and kappa_*=1. Let S1=diag(1,-1), S2=[[0,1],[1,0]]. For any rational q, choose

 Amap(S1)=q[[1,-1],[-1,-1]],
 Amap(S2)=q[[0,2],[2,1]],
 Dmap(S1)=q[[1,2],[-1,1]],
 Dmap(S2)=q[[0,1],[2,-2]].

Every q gives rational affine data and the exact coefficient V=I4 for every start. Coupling q is not required to be small. The static certificate is H=G=I2, C=C0, S=C0*C0, R=I2/2, Q=0, Z=S-R. Its dual is [-C0;I2][-C0*,I2]. The primal and dual values both equal 1.

Floating-point diagnostics from zero at 100000 iterations gave scaled whole-step norms 1.00001809 for q=0, 1.00001896 for q=1, and 0.99979349 for q=3, with predicted limit 1. These runs corroborate the formulas but are not their proof.

## 3. Boundary optimizer is not a failure certificate

The finite test characterizes an INTERIOR leading spectrum. It must not be misreported as a necessary condition for every exact-velocity limit.

For example, the arrow family with fixed cross vector c=(1,0) has a boundary optimizer H=diag(sqrt(2),0), G=sqrt(2). Its block-diagonal invariant orbit consists of an ordinary weakly infeasible order-two problem and a free zero scalar coordinate. Along that orbit the exact last-step law holds, but the common leading state is singular. Thus failure of the interior test does not establish resonance.

The original gamma=1 order-seven switching orbit is also not settled by this certificate. Its support degeneracy is precisely outside the regular regime.

## 4. Routes not closed in this continuation

### Universal raw bound

The desired unrestricted bound ||d_k||=O(k^(p-1)) remains unproved. Firm nonexpansiveness and tracking a central path yield energy estimates, but the inherited state remainder can be too large to force this pointwise scale. The universal local-averaging theorem recovers genuine cone feasibility and exact averaged residual constants without assuming that bound; it is NOT a proof of the raw bound.

### Transferring one good orbit below p=1/2

Square-summable velocity differences alone are insufficient below the half-power threshold: k^(p-1) itself has summable square when p<1/2. Therefore a leading scaled transverse component can coexist with such square summability. This route cannot erase the earlier resonance just by nonexpansiveness.

### Extending the positive certificate through a singular optimum

At a zero eigenvalue the uniform normal contraction used in Checkpoint 03 can disappear. A limiting argument from nearby positive optimizers does not give an orbit estimate uniform in the vanishing eigenvalue. The current proofs do not interchange those limits.

### Journal claims

The new results answer the input-checkable-certificate and algorithmic-recovery targets in the preceding editorial memo. They do not establish acceptance probabilities, an upper-quintile published-paper ranking, or a complete general nonlinear-science resonance theorem. Mathematical advancement and editorial prediction remain different assertions.
