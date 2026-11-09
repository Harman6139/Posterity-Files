# Milestone 37 — universal Kraus-rank lower bound for fixed-diagonal PSD shadows, including nonlinear and approximate lifts

Date: 2026-11-08. Independently proved real finite-dimensional theorem. This is a new obstruction for the remaining weak, many-to-one two-basis SDP normal-form programme. Unlike the positive-retract lower bounds in Milestones 05–12, it needs NO positive encoder, no linear right inverse, no exact affine fibre isomorphism, and NO assumption about a second basis. The decoder IS assumed to be completely positive and globally TRACE PRESERVING. It does not rule out general positive non-CP decoders, nor CP decoders that are not trace preserving on the whole ambient PSD cone.

## Theorem 1 — Kraus rank at least source order, unconditionally

Let m>=2, n>=1, tau>0, and let
  D:S^n -> S^m
be a real completely positive trace-preserving map with a Kraus representation
  D(Y)=sum_{a=1}^t B_a Y B_a^T,
  sum_a B_a^T B_a=I_n.
Let f_1,...,f_n be ANY real orthonormal basis of R^n. Suppose a nonempty family T of PSD matrices has a fixed basis diagonal
  f_j^T Y f_j=a_j   for all Y in T and all j,
and the positive decoder is SURJECTIVE onto the full trace-tau PSD density body:
  D(T)={X>=0 in S^m:tr X=tau}.
Then necessarily
  t>=m.
More precisely, if tau>0, for EVERY j the positive output effect
  E_j=D(f_j f_j^T)
satisfies
  E_j >= (a_j/tau) I_m.                                      (1)
Thus any j with a_j>0 forces rank E_j=m, and rank E_j<=t implies t>=m.

The result remains true with TWO or more fixed orthonormal-basis diagonals, since it uses only the first complete one. The assertion is independent of n, of any excess auxiliary feasible dimension, and of any right-inverse encoding construction.

### Proof

Use the explicit real Stinespring isometry
  V:R^n ->R^m tensor R^t,
  V z=sum_a B_a z tensor e_a.
The trace-preserving identity gives V^T V=I_n, and
  D(Y)=Tr_anc(V Y V^T).

Fix an arbitrary unit vector u in R^m. Surjectivity gives Y_u in T with D(Y_u)=tau uu^T, Y_u>=0 and trY_u=tau. Put W_u=VY_uV^T>=0. Its marginal is tau uu^T. Positivity then forces
  supp W_u subset span(u) tensor R^t:
for w perpendicular to u,
  tr[(ww^T tensor I_t)W_u]=w^T D(Y_u)w=0;
a PSD matrix has zero expectation on an entire subspace only when it annihilates that subspace. Let P_u=uu^T tensor I_t; therefore
  W_u=P_u W_u P_u.

Since W_u>=0 with trace tau, one has the operator inequality
  0<=W_u<=tau P_u.                                        (2)
For any basis vector f_j, let z_j=Vf_j (unit by V isometric). Then
  a_j=f_j^T Y_u f_j=z_j^T W_u z_j
      <=tau z_j^T P_u z_j
      =tau sum_a (u^T B_a f_j)^2
      =tau u^T E_j u.
This holds for EVERY unit u, so E_j>=(a_j/tau)I_m. Since sum_j a_j=trY_u=tau>0, some a_j>0, hence E_j positive definite. But E_j=sum_a (B_a f_j)(B_a f_j)^T has rank at most t. Therefore t>=m. QED.

## Theorem 2 — stable error floor for approximate pure-state surjectivity

Retain D CPTP of Kraus rank t<m and first basis f_j. Let a=(a_j) be prescribed nonnegative diagonal data satisfying sum_j a_j=tau>0. Suppose for EVERY unit u in R^m there exists Y_u>=0 with
  ||diag_f(Y_u)-a||_2 <= epsilon,
  ||D(Y_u)-tau uu^T||_* <= eta,
where ||.||_* denotes nuclear/trace norm.

Then NECESSARILY
  epsilon+eta >=tau/n.                                  (3)
In particular no fixed-size or varying-design family with t<m can achieve sound and complete recovery of the entire trace-tau PSD body at arbitrarily fine accuracy, even if the basis and decoder change with the requested tolerance, as long as n stays fixed.

**Proof.** For each j, E_j=D(f_jf_j^T) has rank<=t<m. Choose a unit u_j in ker E_j. Then B_a f_j perpendicular to u_j for every a, hence z_j=Vf_j is orthogonal to span(u_j) tensor R^t. For the completeness witness Y_{u_j}, set W=VY_{u_j}V^T and Q_j=(I_m-u_ju_j^T) tensor I_t. As z_j lies in ran Q_j, and W>=0,
  f_j^T Y_{u_j} f_j=z_j^T W z_j <=tr(Q_j W)
    =tr[(I_m-u_ju_j^T)D(Y_{u_j})]
    <=||D(Y_{u_j})-tau u_ju_j^T||_* <=eta.
(The last inequality follows from the dual characterization of the trace norm, using a projector of operator norm one.)
The fixed diagonal error bound implies a_j<=eta+epsilon. Summing over j gives tau=sum_j a_j<=n(eta+epsilon), proving (3). QED.

A version allowing a target diagonal a with |sum a-tau|<=xi gives epsilon+eta>=(tau-xi)/n when tau>xi.

## Theorem 3 — sharpness of the Kraus threshold

For m=2^k (k>=1), there is a trace-preserving partial-trace decoder with EXACTLY t=m Kraus operators and an orthonormal basis whose every vector has reduced state I_m/m. Therefore a constant complete first-basis diagonal is compatible with surjectivity onto the entire trace-one density body, and the lower bound t>=m is sharp at infinitely many m.

Construct the four real 2-by-2 orthogonal matrices
  I=[[1,0],[0,1]], Z=[[1,0],[0,-1]], X=[[0,1],[1,0]], J=[[0,1],[-1,0]].
They are pairwise orthogonal in the Frobenius inner product and each satisfies Q Q^T=I_2. Their k-fold tensor products form an orthogonal basis of the real m-by-m matrix space: there are 4^k=m^2 matrices Q_j, each Q_j Q_j^T=I_m, tr(Q_j^T Q_l)=m delta_jl. The vectors vec(Q_j)/sqrt m form an orthonormal basis of R^m tensor R^m, each with partial trace I_m/m.

Let D be partial trace over the second factor (CPTP, Kraus rank exactly m) and E(X)=X tensor I_m/m. For any X>=0 of trace tau, first-basis outcomes are
  <vec(Q_j)/sqrt m, E(X) vec(Q_j)/sqrt m>=tau/m^2
for all j, and D(E(X))=X. Conversely every PSD Y with that fixed diagonal has trace tau, so D(Y)>=0, trD(Y)=tau. Therefore the image of the fixed-diagonal PSD fibre is exactly the trace-tau PSD cone. This is a ONE-basis realization, so it also proves sharpness of the necessary t>=m threshold for two-basis architectures at the level of one compulsory basis.

For arbitrary m, the realification of the complex Weyl basis gives a corresponding construction with r=2m, showing the threshold is always sufficient within a factor two for this partial-trace architecture.

## Corollary — implication for low-rank positive quotient proposals

Any proposed universal two-basis SDP normal form with a globally CPTP decoder whose Kraus rank is o(m) fails already on the trace-only source SDP, irrespective of auxiliary freedom, nonlinear/b-dependent encoders, full rank of ambient competitors, basis symmetry, or the number of available basis measurement lists. This recovers and greatly generalizes the specific 2-Kraus trace-only obstruction in Milestone 36.

The bound is a NECESSARY condition, not an impossibility for a quadratic-size normal form with Kraus rank Theta(m) or for arbitrary trace-controlled non-trace-preserving CP decoders. It does not by itself address noncommuting source constraints.

## Adversarial audit

1. The Stinespring representation is built explicitly from the Kraus matrices and is an ISOMETRY only because D is globally trace preserving. This hypothesis cannot be dropped silently.
2. The proof uses the full family of source pure states in the trace-only problem. It need not apply to an arbitrary proper source fibre with few/no rank-one points.
3. The operator bound W_u<=tau P_u follows from positive semidefiniteness, trace tau and support inclusion; no false rank-one-lift uniqueness assumption is made.
4. The quantitative lower bound uses a DIFFERENT pure state u_j for each input coordinate j; the completeness assumption is correctly quantified over ALL pure states.
5. Nuclear norm error eta bounds the orthogonal output mass; it is not confused with Frobenius error without a norm-conversion factor.
6. The threshold is sharp for m powers of two with an explicit REAL orthogonal error basis; no unjustified claim about the existence of such bases for arbitrary real m is made.
7. Nothing assumes an original or lifted PSD target is unique; indeed the trace-only problem has the entire density-matrix body as its fibre.
8. The result is necessary for any one complete basis diagonal; adding a second basis can only constrain the feasible fibre further.
9. This does not solve the unrestricted N=O(m^2+p) problem with Kraus rank Theta(m), arbitrary positive decoders or source fibres not containing all pure states.
