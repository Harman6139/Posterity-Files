# Milestone 40 — remove trace-preserving hypothesis for any FAITHFUL positive decoder

Date: 2026-11-08. This strengthens Milestone 39 to globally positive but NOT NECESSARILY trace-preserving linear decoders whose trace effect E=D*(I) is positive definite on the full lifted space. There is NO encoder, exact section, singleton fibre or complete positivity hypothesis in the basic output-effect statement.

## Theorem 1 — faithful positive decoder's rescaled basis effects must be full rank

Let D:S^n ->S^m be a real positive linear map and assume
  E:=D*(I_m) is POSITIVE DEFINITE.
Let f_1,...,f_n be an arbitrary real orthonormal basis. Let T be a subset of S^n_+ with the same first-basis diagonal a_j=f_j^T Y f_j for all Y in T, where a_j>=0. Suppose
  D(T)={X>=0:tr X=tau}
for some tau>0.

Then for EVERY j,
  D(E^{-1} f_j f_j^T E^{-1}) >=(a_j/tau) I_m.       (1)
Therefore whenever a_j>0 the rescaled rank-one output effect is positive definite. If D is completely positive with Kraus rank t, it has rank at most t; consequently t>=m. This applies even if D is NOT trace preserving globally.

Proof. Define the normalized positive decoder
  Dhat(Z)=D(E^{-1/2} Z E^{-1/2}).
Its adjoint satisfies Dhat*(I_m)=E^{-1/2}E E^{-1/2}=I_n, so Dhat is trace preserving. For each Y in T write Z=E^{1/2}Y E^{1/2}, so Dhat(Z)=D(Y) and tr Z=trD(Y)=tau. In the normalized variables, the fixed original diagonal functional becomes
  a_j=f_j^T Y f_j = w_j^T Z w_j,
  w_j=E^{-1/2} f_j.
For every unit source u, choose Z_u normalized from a witness Y_u with Dhat(Z_u)=tau uu^T. As in Milestone 39, the positive contraction A_u=Dhat*(uu^T) satisfies 0<=A_u<=I and tr[(I-A_u)Z_u]=0, implying Z_u<=tau A_u. Therefore
  a_j=w_j^T Z_u w_j<=tau w_j^T A_u w_j
      =tau u^T Dhat(w_jw_j^T)u
      =tau u^T D(E^{-1} f_j f_j^T E^{-1})u.
Since u was arbitrary, (1) follows. If D is CP with t Kraus operators, the output of any rank-one input has rank <=t. Since sum_j a_j>0, at least one (1) has a strictly positive lower bound, so t>=m. QED.

## Theorem 2 — quantitative approximate recovery floor with inverse-effect conditioning

Assume D positive and E=D*(I)>0. Let a_j>=0 and A0=sum_j a_j>0. Fix epsilon,eta>=0. Suppose for EVERY unit u in R^m there exists Y_u>=0 such that
  ||diag_f(Y_u)-a||_2<=epsilon,
  ||D(Y_u)-tau uu^T||_*<=eta.
Let J be the set of coordinates for which
  D(E^{-1} f_j f_j^T E^{-1})
is SINGULAR.

Then
  sum_(j in J) a_j
   <= |J| epsilon
      + eta sum_(j in J) f_j^T E^{-1} f_j.         (2)
In particular, if EVERY rescaled effect is singular (as happens for any completely positive decoder of Kraus rank t<m),
  n epsilon+eta tr(E^{-1}) >= A0.                 (3)

Proof. Normalize Dhat and Z_u as above, and define w_j=E^{-1/2} f_j. For each j in J choose a unit source u_j annihilating the output Dhat(w_jw_j^T). Then A_j=Dhat*(u_ju_j^T)>=0 annihilates w_j. The positive contraction R_j=I-A_j has w_j as eigenvector with eigenvalue one, hence
  R_j >=w_jw_j^T/||w_j||².
For any Y>=0 and Z=E^{1/2}Y E^{1/2},
  f_j^T Y f_j=w_j^T Z w_j
   <=||w_j||² tr(R_j Z)
   =||w_j||² tr[(I_m-u_ju_j^T)D(Y)].
For the approximate source pure-state witness, the last trace is at most eta, so the jth observed diagonal entry is at most eta f_j^T E^{-1}f_j. The fixed-diagonal residual gives
  a_j<=epsilon+eta f_j^T E^{-1}f_j.
Summing over J proves (2), and J=all proves (3). QED.

If E>=alpha I_n, then tr E^{-1}<=n/alpha, so (3) implies
  epsilon+eta/alpha>=A0/n.                         (4)
This provides an explicit condition-controlled error floor for low-Kraus non-trace-preserving decoder schemes.

## Interpretation and exact scope

- Faithfulness here means E=D*(I)>0, equivalently D maps every nonzero PSD input to a nonzero PSD output. It does NOT mean D is injective as a linear map.
- Theorem 1 requires only positivity of D, not CP; t>=m is the CP specialization.
- There is no positive encoder, one-to-one correspondence, or fixed-rank restriction anywhere in the argument. Completeness for ALL source pure trace-tau states is the only source richness assumption.
- The quantitative bound survives tolerance-dependent bases and decoders whenever n stays fixed and the relevant spectral bound alpha and target diagonal sum A0 stay uniformly positive. No compactness argument is needed.
- A decoder with SINGULAR E can evade the theorem. For example a positive principal-block decoder has E a projection, and positive companion encodings can put extra mass in its kernel. This is a genuine architectural escape, not a proof gap: E^{-1} is undefined there.
- Therefore no unrestricted quadratic-size two-basis impossibility follows. The remaining candidates may use a decoder with a PSD-kernel effect (nonfaithful), a high-Kraus CP decoder (t>=m), or a nonlinear lifting architecture.
