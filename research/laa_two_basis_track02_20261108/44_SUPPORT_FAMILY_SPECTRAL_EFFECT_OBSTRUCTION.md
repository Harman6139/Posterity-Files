# Milestone 44 — support-family spectral constraints for arbitrary-rank PSD shadows

Date 2026-11-08. This is an exact and robust extension of Milestones 39–43 from the full pure-state trace body to arbitrary nonempty families of PSD source states, including proper spectrahedral fibres and high-rank singular feasible points. It requires only positivity and trace preservation of the linear decoder, not complete positivity, an encoder, unique fibre representation, or a particular basis design.

## Theorem A — all exact feasible supports constrain every basis effect

Let D:S^n ->S^m be a real positive TRACE-PRESERVING linear map. Fix a real ONB f_1,...,f_n and target diagonal a=(a_j)>=0. Let F be ANY nonempty subset of {X>=0:tr X=tau} for tau>0. Suppose T⊂S^n_+ has fixed first-basis diagonal a and satisfies D(T)=F exactly.

For each source X in F, write P_X for the orthogonal projector onto ran X. Let E_j=D(f_j f_j^T)>=0 (trace E_j=1).

Then for EVERY X in F and EVERY input basis index j,
  tr(P_X E_j)>=a_j/tau.                        (1)
Equivalently,
  inf_(X in F) tr(P_X E_j)>=a_j/tau.           (2)

Proof. Choose Y_X>=0 with D(Y_X)=X. Since D is TP, trY_X=tau. The adjoint is positive unital, so A_X=D*(P_X) satisfies 0<=A_X<=I_n. Since X is supported on P_X,
  tr(A_X Y_X)=tr(P_X D(Y_X))=trX=tau.
Thus tr[(I-A_X)Y_X]=0, which forces suppY_X inside the eigenvalue-one subspace of A_X. Consequently
  0<=Y_X<=tau A_X
(as A_X is identity on that eigenvalue-one subspace and nonnegative on its orthogonal complement).
Evaluate on f_j:
  a_j=f_j^TY_X f_j <=tau f_j^TA_X f_j
      =tau tr(P_X D(f_j f_j^T))
      =tau tr(P_X E_j).
Since X and j were arbitrary, (1)-(2) follow. QED.

## Theorem B — robust arbitrary-rank output approximation

Suppose for every X in F there is Y_X>=0 satisfying
  ||diag_fY_X-a||_2<=epsilon,
  ||D(Y_X)-X||_*<=eta.
For every X in F and every j, put e_(j,X)=tr(P_X E_j) in [0,1]. Then
  sqrt((a_j-epsilon)_+)
    <=sqrt((tau+eta)e_(j,X))+sqrt(eta),        (3)
and therefore
  inf_(X in F) tr(P_X E_j)
    >=[max(0,sqrt((a_j-epsilon)_+)-sqrt(eta))]^2/(tau+eta).
                                                       (4)

Proof. Use the two-term positive contraction Cauchy-Schwarz argument of Milestone 41 with A_X=D*(P_X) instead of D*(uu^T). The source target X has zero mass on I-P_X. Hence the decoded output error controls
  beta=tr[(I-P_X)D(Y_X)]<=eta,
while alpha=tr[P_X D(Y_X)]<=tau+eta.
The same decomposition f=A_X^(1/2)A_X^(1/2)f+(I-A_X)^(1/2)(I-A_X)^(1/2)f yields (3). Taking the infimum over X and rearranging yields (4). QED.

## Corollary C — Ky Fan spectral obstruction for a full rank-r support family

Assume F contains the normalized rank-r projection
  X_P=(tau/r)P
for EVERY orthogonal rank-r projector P on R^m, where 1<=r<m.
Then for every j,
  sum_(i=1)^r lambda_i^up(E_j) >=a_j/tau,    (5)
where lambda_1^up<=...<=lambda_m^up denote the eigenvalues in ASCENDING order.

Proof. Equation (1) holds for all rank-r P. The minimum of tr(P E_j) over rank-r orthogonal projectors is the sum of the r smallest eigenvalues of E_j (Ky Fan minimum principle). QED.

If a_j>0, (5) requires rank E_j >=m-r+1; otherwise its kernel would have dimension >=r and the sum of the r smallest eigenvalues would vanish. If D is CP with t Kraus operators, rank E_j<=t, so
  t>=m-r+1.
The case r=1 recovers the sharp t>=m lower bound.

## Corollary D — constrained source subspaces

If F contains tau uu^T for every unit u in a fixed k-dimensional subspace S⊂R^m, then
  P_S E_j P_S >=(a_j/tau)P_S,
and CP Kraus rank t>=k whenever some a_j>0. This follows by applying (1) to every rank-one support u⊂S.

## Scope and hostile audit

- A general feasible X need not be a normalized projection; only its SUPPORT projector P_X enters the universal inequality, and the proof uses nothing else about its positive eigenvalues.
- The family F may be a singleton, a proper SDP feasible set, a full density body or any convex/nonconvex subset of the trace-tau PSD cone. It need not contain any rank-one matrices.
- The fixed-diagonal target a may have zero entries; the inequalities remain valid but only positive entries force nontrivial output-effect support.
- Complete positivity is needed only for the numerical Kraus-rank consequences, not for the positive-decoder support inequalities.
- The rank-r full-Grassmannian source family is a deliberately rich test family; a generic proper affine SDP fibre may not contain it, so the corollary does not claim generic dense SDPs satisfy a uniform rank obstruction.
- The robust estimate is in nuclear norm and converts from Frobenius output error eta_F by eta<=sqrt(m)eta_F.
- These results are NECESSARY support-compatibility tests, not sufficient conditions for a universal two-basis design. The unrestricted O(m²+p) many-to-one problem remains open.
