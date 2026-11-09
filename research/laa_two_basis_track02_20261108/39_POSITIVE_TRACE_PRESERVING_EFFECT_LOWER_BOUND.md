# Milestone 39 — universal full-rank-effect obstruction for ANY positive trace-preserving PSD quotient

Date: 2026-11-08. This is a STRICT strengthening of Milestone 37: the central exact and robust obstruction requires only positivity and trace preservation of the decoder, NOT complete positivity, Kraus operators, a Stinespring representation, a right-inverse encoder, a fixed lifted rank, or uniqueness of an auxiliary extension.

## Theorem A — every positive-diagonal input basis effect must be positive definite

Let m>=2, n>=1, tau>0. Let
  D:S^n -> S^m
be REAL linear, POSITIVE on the full PSD cone, and TRACE PRESERVING:
  D(S^n_+) subset S^m_+,
  tr D(Y)=trY for all symmetric Y.
Let f_1,...,f_n be any orthonormal basis of R^n. Suppose a set T subset S^n_+ satisfies fixed first-basis diagonal outcomes
  <f_jf_j^T,Y>=a_j for every Y in T,
and its decoder image is the full trace-tau PSD body:
  D(T)={X>=0:trX=tau}.

Then for EVERY j,
  E_j:=D(f_jf_j^T) >= (a_j/tau) I_m.                (1)
In particular every index with a_j>0 has a positive-definite output effect E_j, even if D is positive but not completely positive.

Proof. The adjoint D*:S^m->S^n is positive and UNITAL: D*(I_m)=I_n. Fix any unit u in R^m, and choose Y_u in T with D(Y_u)=tau uu^T. Set
  A_u=D*(uu^T).
Then 0<=A_u<=I_n because 0<=uu^T<=I_m and D* is positive/unital. The trace equalities are
  trY_u=tau,
  tr(A_uY_u)=tr(uu^T D(Y_u))=tau.
Therefore tr[(I_n-A_u)Y_u]=0. Both I_n-A_u and Y_u are PSD, so their product has zero positive pairing only when
  supp Y_u subset ker(I_n-A_u),
the eigenvalue-ONE subspace P_1 of A_u. Since Y_u>=0 and trY_u=tau,
  Y_u<=tau P_1<=tau A_u.
Evaluate on f_j:
  a_j=f_j^T Y_u f_j<=tau f_j^T A_u f_j
      =tau u^T D(f_jf_j^T)u=tau u^T E_j u.
This holds for every unit u, yielding E_j>=(a_j/tau)I_m. QED.

The effects obey tr E_j=1 by trace preservation, so automatically a_j<=tau/m. If D is CP of Kraus rank t, rank E_j<=t, and because sum_j a_j=tau>0 at least one effect is positive definite: hence t>=m. This recovers Milestone 37 as a COROLLARY without invoking Stinespring in the principal obstruction proof.

## Theorem B — stable error floor for any positive TP map with singular effects

Let D be positive and trace preserving and let the proposed fixed first-basis target diagonal a have sum tau>0. Let J be a nonempty set of coordinates whose output effects E_j=D(f_jf_j^T) are SINGULAR. Suppose for every unit source u there is a PSD lift Y_u with
  ||diag_fY_u-a||_2<=epsilon,
  ||D(Y_u)-tau uu^T||_*<=eta.
Then
  sum_(j in J) a_j <=|J| (epsilon+eta).             (2)
In particular, if EVERY E_j is singular,
  epsilon+eta>=tau/n.                                 (3)
This applies to all positive TP decoders, including non-CP ones, without any compactness or limit-design hypothesis.

Proof. For each j in J choose a unit u_j in ker E_j. Positivity of A_j=D*(u_ju_j^T) and f_j^T A_j f_j=u_j^TE_j u_j=0 implies A_j f_j=0. Since 0<=A_j<=I_n, the PSD operator
  B_j=I_n-A_j
has f_j as an eigenvector with eigenvalue ONE. Thus B_j>=f_jf_j^T.

For the approximate pure-source witness Y_(u_j)>=0,
  f_j^T Y_(u_j)f_j <=tr(B_j Y_(u_j))
  =tr[(I_m-u_ju_j^T)D(Y_(u_j))]
  <=||D(Y_(u_j))-tau u_ju_j^T||_* <=eta.
The first-basis residual bound yields a_j<=epsilon+eta. Sum over J to obtain (2); if J is every index, sum a_j=tau and (3) follows. QED.

## Theorem C — a uniform numerical conditioning constraint

Under exact surjectivity in Theorem A, for each coordinate with a_j>0,
  lambda_min(E_j)>=a_j/tau>0.
Thus any numerical representation with fixed positive first diagonal forces every output effect to be uniformly full rank with the reciprocal smallest-eigenvalue conditioning
  kappa_effect_j <=tau/a_j.
The inequality itself is exact and dimension independent. For a uniform target diagonal a_j=tau/n, every E_j must satisfy E_j>=I_m/n.

This does NOT imply a dimension-only bound on decoder condition number; the inequality is a necessary lower effect margin, not a sufficient construction condition.

## Theorem D — subspace version

Suppose the source feasible set contains every rank-one trace-tau projector tau uu^T with u ranging over the unit sphere of a fixed k-dimensional subspace E⊂R^m. The same argument gives
  P_E E_j P_E >=(a_j/tau) P_E.
If D is CP of Kraus rank t and some a_j>0, then t>=k. This applies to proper spectrahedral fibres that retain a complete k-dimensional pure-state sector.

## Sharpness and scope

- For m a power of two, the real Pauli tensor orthogonal-error-basis construction of Milestone 37 with input n=m² and partial-trace decoder of Kraus count m realizes full density-body surjectivity with every a_j=tau/m²>0. This shows the Kraus-rank threshold t>=m is sharp on infinitely many m.
- The theorem is based ONLY on unital positivity of D*, not complete positivity. No positive encoder or unique pure-state preimage is assumed.
- A source fibre without a complete projective family of pure rank-one states may evade the theorem; the full trace-only SDP is the decisive universal test instance.
- Globally non-trace-preserving positive decoders are outside the statement. Normalizing such a decoder generally changes the orthonormal-basis geometry and cannot be silently assumed harmless.
- A quadratic-order universal representation with a positive TP decoder whose every positive first-basis output effect is full rank and whose CP Kraus rank is Theta(m) is not ruled out.
- The theorem works over real symmetric PSD matrices; the proof is entirely order-theoretic and also extends to complex Hermitian PSD matrices.
- Numeric exactness: the approximate lower bound is expressed in nuclear norm output error. If only Frobenius output error eta_F is available, use eta <=sqrt(m) eta_F, giving epsilon+sqrt(m)eta_F>=tau/n when every E_j is singular.
