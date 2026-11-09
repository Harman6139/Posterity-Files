# Milestone 42 — unconditional 2m input-order barrier for many-to-one fixed-diagonal CPTP density-state recovery

Date 2026-11-08. This theorem is unrelated to the positive-exact-retract dimension count of Milestones 07–08: it allows arbitrary nonlinear lift selection, arbitrary auxiliary-fibre multiplicity, any number of orthonormal basis measurement lists, and does not assume an encoder. It applies to EVERY completely positive trace-preserving decoder, with unrestricted Kraus rank. It is a NECESSARY dimension bound for the trace-only source SDP, not a proof of the general near-quadratic conjecture.

## Theorem A — n>=2m and strict inequality for m>=3

Let m>=2 and tau>0. Let D:S^n -> S^m be a real completely positive TRACE-PRESERVING linear map. Suppose for some real ONB f_1,...,f_n of R^n and fixed vector a=(a_j) with sum a_j=tau, a family T of PSD matrices satisfies
  f_j^T Y f_j=a_j for all Y in T and all j,
  D(T)={X>=0 in S^m:tr X=tau}.
Then
  n>=2m.
Moreover, for m>=3,
  n>=2m+1.                                           (1)
For m=2, the lower bound n>=4 is sharp: the real Bell basis and ordinary partial trace R²⊗R² ->R² give a fixed-uniform-diagonal fibre of order n=4 surjecting onto the full real 2×2 density body (Milestone 37).

The theorem remains true if a SECOND basis diagonal is fixed in addition to the first. No basis-overlap or positivity-of-individual-a_j assumption is required.

### Proof

Choose a real Kraus representation D(Y)=sum_(a=1)^t B_a Y B_a^T with sum B_a^T B_a=I_n. Its Stinespring map
  V:R^n ->R^m tensor R^t,
  Vv=sum_a B_a v tensor e_a
is an isometry.

For any unit source u, define the linear pure-output support space
  K_u={v in R^n:B_a v in span(u) for all a}
     =V^(-1)(span(u) tensor R^t).
If Y>=0 and D(Y)=tau uu^T, the PSD marginal support argument forces
  suppY subset K_u.
Every pure source state has a lift by surjectivity, so dim K_u>=1 for all u.

Suppose dim K_u=1. Then every PSD lift of tau uu^T is supported on a fixed line, and trace preservation fixes its only coefficient; hence its lift is UNIQUE and has rank ONE. But the number of real rank-one PSD matrices with a FIXED first-basis diagonal a is finite, at most 2^(k−1), where k is the number of positive diagonal entries. (A rank-one lift vv^T must have coordinates v_j=+/−sqrt(a_j), and v and −v produce the same matrix.) Since a single lifted matrix has only one decoded source pure state, dimK_u=1 can hold for only finitely many projective directions [u].

Consequently, for all but finitely many pure source directions,
  dim K_u>=2.                                          (2)

Choose m linearly independent unit source vectors u_1,...,u_m satisfying (2). The corresponding tensor subspaces span(u_i) tensor R^t are in direct sum because the u_i are linearly independent. Since V is an isometry, K_(u_1),...,K_(u_m) are also in direct sum. Therefore
  n>=sum_i dim K_(u_i)>=2m,
proving the first bound.

Suppose equality n=2m. Then necessarily each chosen K_(u_i) has dimension exactly two, and their direct sum is ALL of R^n. There exist 2-dimensional ancilla subspaces W_i of R^t such that
  V(R^n)=direct_sum_i [span(u_i) tensor W_i].
For a generic source vector u=sum_i c_i u_i with EVERY c_i nonzero, the membership condition
  u tensor w in V(R^n)
is equivalent to w in intersection_i W_i. Since one can choose such a u outside the finite exceptional projective set of (2), its K_u dimension is at least two. Thus dim intersection_i W_i>=2. Every W_i has dimension exactly two, so ALL W_i coincide with one common 2-dimensional subspace W_0.

It follows that
  V(R^n)=R^m tensor W_0.
By an orthogonal change of ancilla basis, the Stinespring map therefore uses at most TWO nonzero Kraus operators. But Milestone 37's independent full-rank-effect theorem (strengthened to all positive TP maps in Milestone 39) shows that any fixed-diagonal surjection onto the full trace-tau density body by a CP decoder must have Kraus rank at least m. Hence m<=2. For m>=3 this is a contradiction, proving n>=2m+1. QED.

## Theorem B — nonzero uniform approximation floor below the dimension threshold

Fix m>=3, n<=2m, tau>0. There exists a number
  c(m,n,tau)>0
such that NO choice of real ONB, CPTP decoder D:S^n ->S^m and proposed nonnegative target diagonal a with sum a_j=tau can satisfy the following uniformly over every unit source u:
  exists Y_u>=0 with
    ||diag_B Y_u-a||_2<=epsilon,
    ||D(Y_u)-tau uu^T||_*<=eta,
and epsilon+eta<c(m,n,tau).

Proof by contradiction/compactness: suppose epsilon_k+eta_k->0 for a sequence of such designs. The ONBs lie in compact O(n), the nonnegative a_k lie in the compact trace-tau simplex, and the CPTP maps form a compact finite-dimensional family. For the last assertion, pad Kraus representations with zeros to t<=mn (using the real Choi matrix rank bound); trace preservation bounds sum_a ||B_a||_F²=tr I_n=n, so the Kraus matrices have a convergent subsequence. Along one common subsequence all designs converge to a CPTP map D, an ONB B and diagonal a.

For any fixed unit source u, the associated positive witness Y_(k,u) has trace=tr D_k(Y_(k,u)), which is bounded by tau+eta_k. Therefore it has a convergent SUBSUBSEQUENCE (depending on u), and in the limit yields an exact PSD lift Y_u with
 diag_B Y_u=a, D(Y_u)=tau uu^T.
The common design subsequence is independent of u, so this conclusion holds for EVERY unit u. The convex set of all PSD matrices with diagonal a is compact; its image under D is compact and convex, contains ALL pure trace-tau source states, and is contained in the trace-tau PSD body because D is positive TP. It therefore equals that entire body, contradicting Theorem A for n<=2m, m>=3. Hence c>0 exists. QED.

The constant c is nonconstructive from this compactness argument, unlike Milestone 37's explicit tau/n floor for Kraus rank t<m. Since the design family is semialgebraic for fixed m,n and tau algebraic, it can in principle be bounded by real-algebraic quantifier elimination; no polynomial-time or polynomial-in-m explicit gap is claimed.

## Interpretation

- The obstruction applies to many-to-one PSD SHADOWS. No positive encoder, affine isomorphism, full-fibre uniqueness or target rank assumption is made.
- Its dimension bound is independent of the decoder's Kraus rank t; even arbitrarily high t cannot beat n>=2m+1 for m>=3.
- For m=2, n=4 is achievable with a real Bell basis, demonstrating exact sharpness at the smallest nontrivial order.
- The proof is REAL: a fixed first-basis diagonal has only finitely many rank-one PSD lifts. In complex Hilbert spaces phases create continuous families, so a modified argument would be needed.
- The dimension bound is linear in m, so it does NOT refute n=O(m²+p); it identifies a second genuine necessary condition for every universal two-basis CP quotient on the trace-only test instance.
- The approximate-gap theorem assumes a uniform source pure-state completeness guarantee and the CPTP class. It is not a claim about generic proper SDP fibres with no source pure states.
- For m>=3, the equality n=2m is excluded through a forced TWO-KRAUS Stinespring subsystem; this uses Theorem 37's independently proved effect-rank bound and does not assume any particular first ONB.
