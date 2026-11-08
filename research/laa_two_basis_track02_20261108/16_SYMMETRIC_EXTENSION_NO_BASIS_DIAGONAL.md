# Milestone 16 — symmetric-square surjective PSD shadow cannot have EVEN ONE fixed-diagonal orthonormal basis

Date 2026-11-08. This is a complete no-go theorem for the attractive quadratic-size symmetric-square shadow of Milestone 15, and it explains why that shadow does not solve two-basis universality. It is NOT an impossibility for all quadratic-size many-to-one lifts.

## Theorem (pure-state uniqueness forces diagonal measurement impossibility)

Let m>=2, V=Sym^2(R^m), d=m(m+1)/2, and D:S^d -> S^m be the symmetric-square partial-trace decoder of Milestone 15. Fix tau>0. Let T subset S^d_+ be ANY set (not necessarily a spectrahedron) such that
  D(T)={X>=0:tr X=tau}.
Then there does not exist even ONE real orthonormal basis psi_1,...,psi_d of V for which the diagonal data
  <psi_j,Y psi_j>=a_j
are independent of Y in T. In particular the trace-one density-matrix body is NOT the D-image of any PSD fibre defined by one or two fixed-diagonal orthonormal-basis measurement lists in S^d.

**Proof.**
For each unit u in R^m, the source pure state X_u=tau uu^T has a UNIQUE PSD preimage under D on the symmetric tensor subspace, namely
  Y_u=tau (u tensor u)(u tensor u)^T.
Indeed positivity and rank-one first marginal imply the range of Y is contained in span(u) tensor R^m. Intersecting with the symmetric tensor subspace leaves the one-dimensional line span(u tensor u); trace fixes the coefficient.

Since D(T) is the full trace-tau PSD body, every Y_u lies in T. Suppose a nonzero vector psi in V has constant quadratic measurement on all Y_u. Via the canonical symmetric-matrix identification of V, write psi=vec_s(A) for A in S^m. Then
  <psi,Y_u psi>=tau (u^T A u)^2.
Hence (u^T A u)^2 is constant for every unit u. Since the sphere S^{m-1} is connected for m>=2 and u->u^T A u is continuous, it cannot change sign unless the constant is zero. Consequently u^T A u is itself constant on the sphere; spectral testing at its eigenvectors yields A=cI. If the constant were zero, A=0, contradicting psi nonzero.

Thus EVERY vector in any putative admissible basis must lie on the ONE-dimensional line spanned by vec_s(I). But V has dimension d>=3, so no orthonormal basis exists. QED.

## Quantification of the large-slack escape

For the trace-only source fibre F={X>=0:trX=tau}, its affine dimension is D_m-1. The symmetric-square lifted PSD fibre T_all={Y>=0 on V:trY=tau} has relative interior I_d*(tau/d) and affine dimension D_d-1. The partial-trace decoder is surjective. Its decoder-invisible affine tangent dimension is
  a=(D_d-1)-(D_m-1)=D_d-D_m=Theta(m^4).
Its CP Kraus rank is exactly m in the standard partial-trace representation. This is precisely the giant auxiliary slack phenomenon predicted by the surjective-Kraus tradeoff (Milestone 09): such large slack is geometrically realizable at compressed order d=Theta(m^2). But the no-basis theorem shows that this particular realization has no room for a single fixed-diagonal observation list.

## Scope / checks

- The obstruction applies to EVERY possible fixed first-basis target data, not just uniform data or positive data. It uses only exact surjectivity onto the whole trace-tau PSD cone.
- It applies to the minimal symmetric-square Hilbert space itself; an enlarged tensor ancilla can evade it because a pure source state then has many nonunique PSD lifts with the same partial trace. In fact the maximally-entangled-basis construction from Milestone 14 gives such an enlarged order-2m^2 hybrid with a complete constant first-basis diagonal.
- The uniqueness proof is valid over real Hilbert spaces. The continuity argument uses m>=2, so S^{m-1} is connected.
- The theorem is not a no-go for a proper sub-fibre F_b containing no pure states: source pure-state uniqueness is the decisive hypothesis.
- The result does not rule out order-O(m^2) two-basis universality with a different CP decoder whose pure-state preimages have positive-dimensional freedom.
