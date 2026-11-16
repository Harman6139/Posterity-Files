# Checkpoint 03 — a data-only exact-velocity theorem for plain DRS

Date: 2026-11-15. This closes the connection left open in Checkpoint 02: a finite convex optimization certificate predicts an ACTUAL last-iterate law for every start. The proof is independent of the proposed gamma=2 counterexample and does not assume a state expansion or differentiate an orbit remainder.

## 1. Statement

Use the affine–PSD data, canonical support spaces E,F, linear spaces A,B, affine cross-space C and convex program (P) from Checkpoint 02. Let its unique coefficient pair be H_*, G_*=2R_*.

### Theorem A — finite characterization of regular spectral escape

For a weakly infeasible U=a+L, the following are equivalent:

1. Some plain DRS orbit escapes to infinity with a positive-definite normalized limiting state.
2. E direct-sum F is the whole coordinate space, and the optimizer of (P) has H_*>0 on E and G_*>0 on F.
3. There exist finite matrices H,G,C,W satisfying the positive-definite balancing equations (4.2) of Checkpoint 02.

When these hold, V=H_*+G_* is positive definite in the original coordinates and EVERY initial point satisfies

    z_k=V sqrt(k)+O(log k),
    z_(k+1)-z_k=V/(2sqrt(k))+O(log(k)/k).           (1.1)

The constants may depend on the instance and start. In particular

    sqrt(k)||z_(k+1)-z_k|| -> ||V||/2=sqrt(kappa_*),

where kappa_* is the optimum of (P). The normalized-state angular tail obeys

    sum_(k>=N)||z_(k+1)/||z_(k+1)||-z_k/||z_k||||
                       =O(log(N)/sqrt(N)).          (1.2)

The criterion is finite and determined by the affine data. In particular any verified primal–dual pair satisfying the strict eigenvalue/gap test (5.3) in Checkpoint 02 certifies (1.1) for EVERY start. A boundary optimum does not establish a rotating mode; it means that the fully regular leading-spectrum condition fails.

### Theorem B — residual and profile constants

Let P=P_L, Q=I-P, u_k=P_Uz_k, v_k=P_PSD(2u_k-z_k), and let the original equation description be Mz=b, ker M=L. Then

    u_k/sqrt(k), v_k/sqrt(k) -> H_*,
    sqrt(k)(u_(k+1)-u_k), sqrt(k)(v_(k+1)-v_k) -> H_*/2,
    sqrt(k)(M v_k-b) -> M G_*/2 !=0,
    sqrt(k)||(MM*)^(dagger/2)(M v_k-b)|| -> ||G_*||/2,
    lim_(r->infinity) r D(r)=kappa_*.

Here D(r)=min{||Qv-a||:v PSD, ||Pv||<=r}. Redundant equality rows are permitted. In particular the same finite convex program computes both the leading DRS squared-speed constant and the asymptotic static feasibility constant.

## 2. The linear spectral mechanism

We prove the dynamic part directly. Suppose first that a finite positive-definite balancing solution H,G,C exists. Put V=H+G, J=2P-I and

    D_H={X in L:X=EXE},
    D_G={Y in L^perp:Y=FYF},
    D=D_H orthogonal-sum D_G.

These identify with A and B. The anchor a is perpendicular to D by Checkpoint 02. Since H in L and G in L^perp, JV=H-G is nonsingular and |JV|=V. For a positive block pair s=H_s+G_s in D near V, write

    C_s=D|.|(Js), M_s=(I+C_s J)/2.

Matrix absolute value is real analytic on a neighborhood of every nonsingular symmetric matrix, including matrices with repeated eigenvalues. In eigenbases of H_s,G_s, C_s multiplies entries by

    +1 on E-E, -1 on F-F,
    (h_i-g_j)/(h_i+g_j) on E-F.                    (2.1)

This formula follows by differentiating |X|^2=X^2 and solving the resulting Sylvester equation. Every cross multiplier has absolute value strictly below one.

The homogeneous map T0(z)=(z+|Jz|)/2 is firmly nonexpansive. Differentiating its firm inequality shows that M_s is a firmly nonexpansive linear map. Its fixed space is exactly D. In fact equality C_s Jw=w forces equality of norms in the contraction C_s. All cross entries of Jw and w must therefore vanish. Formula (2.1) then implies Pw=EwE and Qw=FwF, which is precisely w in D. The converse is immediate.

A linear contraction fixing D pointwise also has its adjoint fixing D pointwise: expand its norm inequality at d+epsilon w with d in D. Hence D^perp is invariant. If ||M_s w||=||w||, firm nonexpansiveness gives M_s w=w. Compactness of the unit sphere in D^perp therefore yields

    ||M_s restricted to D^perp||<=q<1             (2.2)

uniformly for s in a sufficiently small positive neighborhood of V. Also C_s a is in D^perp because C_s is self-adjoint and preserves D.

## 3. Stationary normal point and the cross-block minimization

Define the smooth normal point

    w0(s)=(I-M_s restricted to D^perp)^(-1) C_s a.

It satisfies w0=C_s(Jw0+2a). Set u0=a+Pw0, s0=Qw0-a. Since w0=u0+s0 and Jw0+2a=u0-s0, (2.1) gives

    (u0)_FF=0, (s0)_EE=0,
    (s0)_EF=-H_s^(-1)(u0)_EF G_s.                 (3.1)

Let C_s^0=(u0)_EF. It belongs to the affine cross-space C. Every cross variation in Cdir lifts to an element of L with zero F-F block. Orthogonality of s0 to L and (3.1) therefore prove that C_s^0 is the unique minimizer of

    Phi(H_s,G_s)=min_(C in C) tr(H_s^(-1) C G_s C*).

The quadratic form is strictly convex in C. In particular at the balancing pair H,G its minimizer is the C in the finite certificate.

For any fixed w, the uniform Taylor expansion is

 T(t s+w)=t s+M_s w+C_s a+t^(-1)F1(s,w)+O(t^(-2)),
 F1(s,w)=D^2|.|(Js)[Jw+2a,Jw+2a]/4.                (3.2)

The bound is uniform on compact sets of positive s and bounded w. Write

    b(s)=P_D F1(s,w0(s)).

We now calculate this coefficient exactly. Expand |H_s-G_s+epsilon B|=s+epsilon w0+epsilon^2 B2+O(epsilon^3), with B=Jw0+2a. Then

    s B2+B2 s=B^2-w0^2.

Equation (3.1) gives B_EF=C_s^0+H_s^(-1)C_s^0 G_s and (w0)_EF=C_s^0-H_s^(-1)C_s^0 G_s. The diagonal Sylvester equations consequently yield

    (B2)_EE=2H_s^(-1)C_s^0 G_s(C_s^0)*H_s^(-1),
    (B2)_FF=2(C_s^0)*H_s^(-1)C_s^0.

The DRS factor one half gives

 b_H(s)=P_A[H_s^(-1)C_s^0 G_s(C_s^0)*H_s^(-1)],
 b_G(s)=P_B[(C_s^0)*H_s^(-1)C_s^0].                (3.3)

Thus the finite balancing equations are EXACTLY

    b(V)=V/2.                                      (3.4)

No actual-orbit assumption has entered this calculation. The field b is smooth and homogeneous of degree -1 under simultaneous scaling of H_s,G_s.

## 4. Constructing an approximate orbit from the data

At s=V set

    w1=(I-M_V restricted to D^perp)^(-1)
                             P_(D^perp)F1(V,w0(V)),
    q_k=sqrt(k)V+w0(V)+k^(-1/2)w1.

Substitute this explicit path into (3.2). Since M_V w0+C_Va=w0 and M_Vw1+F1=w1+b(V), (3.4) gives

    Tq_k=q_k+V/(2sqrt(k))+O(1/k),
    q_(k+1)=q_k+V/(2sqrt(k))+O(k^(-3/2)).

Hence ||Tq_k-q_(k+1)||<=C/k on a sufficiently late tail. Nonexpansiveness of T gives for ANY actual orbit

    ||z_k-q_k|| <= constant + sum_(j<k)C/j = O(log k).

This proves the state estimate in (1.1), and establishes its interior direction from the STATIC certificate. It is not an invocation of a pre-existing regular cosmic orbit.

## 5. Two-order tracking proves the actual last step

Write the actual state as z=s+w, s=P_D z, w=P_(D^perp)z, r=||s||, n=s/r. The preceding state estimate gives r comparable to sqrt(k), n->V/||V||, and w=o(r). Applying the first-order Taylor expansion with remainder O((||w||+1)^2/r), together with (2.2), gives

    ||w_next|| <= (q+o(1))||w||+O(1).

Thus w is bounded. Projecting (3.2) onto D now gives

    s_next-s=O(1/r),
    r_next/r=1+O(r^(-2)), n_next-n=O(r^(-2)).        (5.1)

The smooth functions w0(n) and

    w1(n)=(I-M_n restricted to D^perp)^(-1)
                                   P_(D^perp)F1(n,w0(n))

track the normal component to two orders:

    w=w0(n)+r^(-1)w1(n)+O(r^(-2)).                 (5.2)

Here are the discrete estimates. Subtract w0(n_next) in the normal Taylor recurrence. Its defining equation cancels the constant forcing; (5.1) bounds its change by O(r^-2). The remaining recurrence has contraction M_n and forcing O(r^-1). Multiplying the error by r_next, whose ratio to r tends to one, proves w-w0(n)=O(r^-1). Substitute this bound back into F1 and subtract w0(n_next)+r_next^-1 w1(n_next). The equation for w1 cancels all forcing of order r^-1. The remaining forcing is O(r^-2); multiplying by r_next^2 proves (5.2). These are contraction recurrences, not derivatives of a sequence remainder.

Equations (5.1)–(5.2) imply

    w_next-w=O(r^(-2)),
    d_k=r^(-1)b(n)+O(r^(-2))=b(s)+O(r^(-2)).        (5.3)

Since s=sqrt(k)V+O(log k), smoothness and degree -1 homogeneity give

    b(s)=k^(-1/2)b(V)+O(log(k)/k)
         =V/(2sqrt(k))+O(log(k)/k).

This proves the actual last-step estimate. Radial normalization, using the state and velocity bounds, gives an angular increment O(log(k)/k^(3/2))+O(k^-2). Summation proves (1.2). This completes sufficiency for every start.

## 6. Necessity: an interior cosmic ray must solve the finite program

Suppose an actual orbit diverges and z_k/||z_k||->N>0. Nonexpansiveness bounds all step norms by the first. Dividing Tz=(z+|Jz+2a|)/2 by ||z|| therefore gives |JN|=N. Hence H_N=PN and G_N=QN are PSD, complementary, and N=H_N+G_N.

Exactly, with d=Tz-z, complementary shadows yield

    h(z):=||a||^2-<a,z>=<Tz,d>,
    ||Tz||^2-||z||^2=2h(z)-||d||^2.                (6.1)

If <a,N> were positive, the squared norm would eventually decrease, contradicting divergence. Thus <a,N><=0. On the other hand <a,H_N>=0 and weak feasibility gives <a,G_N>>=0. Therefore <a,G_N>=0. The ranges of H_N,G_N are complementary. Orthogonality to these positive matrices forces every matrix in R and N (the two cones of Section 1 of Checkpoint 02) into the corresponding supports; their supports are consequently the canonical E,F, and E+F=I.

Repeat the normal contraction argument of Sections 2,3,5 near the ray N; it uses only w=o(r), not any prescribed power. It gives (5.2)–(5.3). Put

    h0(N)=||a||^2-<a,w0(N)>.

It is strictly positive. Indeed, with B=Jw0+2a and w0=C_N B,

    4h0(N)=||B||^2-||C_N B||^2>=0.

If equality held, (2.1) would force B and w0 to have zero cross blocks. Equation (3.1) would then give an affine point u0 supported on E; adding a large multiple of H_N would make it PSD, contradicting infeasibility.

Thus h(z_k)->h0(N)>0 and d_k->0. The exact radial identity (6.1) gives

    ||z_k||^2/k -> 2h0(N).

Equation (5.3) gives sqrt(k)d_k->b(N)/sqrt(2h0(N)). Summing these actual increments and comparing with the known radial norm and direction forces b(N)=h0(N)N. Therefore V=sqrt(2h0(N))N satisfies b(V)=V/2. Its cross minimizer satisfies all finite balancing equations. Checkpoint 02 proves that this is the unique optimizer coefficient, and it is interior. This proves necessity and the equivalence of all three assertions.

## 7. Residuals and the static coefficient

The affine shadow is u_k=a+Pz_k and the cone shadow is v_k=u_k+d_k. Thus their states have leading term H_*sqrt(k). Their increments have the claimed leading term because (1.1) implies sqrt(k)(d_(k+1)-d_k)->0. Exactly

    Mv_k-b=M Qd_k,
    ||(MM*)^(dagger/2)(Mv_k-b)||=||Qd_k||.

The last-step estimate proves the stated residual limits, and M G_*!=0 because G_* is nonzero in L^perp.

For clarity, the static profile constant can also be recovered without assuming its previous formula. Let z(t) solve Tz(t)-z(t)=(z(t)-a)/t. For an affine–cone DRS pair, its cone shadow is the unique minimizer of

    ||Pv||^2/[2(t+1)^2]+||Qv-a||^2/2 over v PSD.

The standard tame central-path comparison, proved in baseline 30/31, identifies its leading state as 2^(-1/2)V sqrt(t), since the actual state coefficient is V and p=1/2. It follows that its primal radius is asymptotic to ||H_*||sqrt(t/2), and its equation-distance is asymptotic to ||G_*||/sqrt(2t). Eliminating t gives

    D(r)~||H_*||||G_*||/(2r).

The balancing equality ||H_*||=||G_*|| from Checkpoint 02 identifies this coefficient as ||V||^2/4=kappa_*. This STATIC consequence explicitly uses the inherited central-path comparison; the raw state/velocity proof in Sections 2–6 does not.

## 8. Weak infeasibility itself can be certified on these supports

One may start without assuming weak infeasibility: it is enough to exhibit a complementary split E,F, a positive H0 in L supported on E, a positive G0 in L^perp supported on F, and a nonempty cross-affine slice C that excludes zero. An element u0=[[A0,C0],[C0*,0]] in U gives <a,G0>=0. Any feasible PSD point would then be supported on E, contradicting 0 not in C. Conversely, for sufficiently large t,

 X_t=[[A0+tH0,C0],[C0*,C0*(A0+tH0)^(-1)C0]] >=0

approaches u0+tH0 in U at rate O(1/t). Hence the pair is weakly infeasible.

This also gives escape exponent alpha=1. For the lower bound, a PSD X at distance delta from U has tr(X_FF)=O(delta), by pairing with G0. A fixed linear right inverse for F-F compression corrects P_UX to an element of U with zero F-F block, by O(delta). Its cross block belongs to C. Since dist(0,C)>0, ||X_EF|| is bounded below for small delta. The PSD inequality ||X_EF||_F^2<=tr(X_EE)tr(X_FF) now forces tr(X)>=c/delta. The displayed Schur path supplies the matching upper bound. Norm-equivalent equality residuals have the same exponent.

This is a finite geometric weak-infeasibility certificate for the stated class; it is not a decision algorithm for all SDPs.

## 9. Exact scope

The theorem applies to coupled products of real and complex PSD cones by summing the blockwise formulas; no independence of affine constraints is required. It replaces the previous DYNAMIC assumption 'the leading state is interior' by a finite convex program, an exact dual and a verifiable gap/eigenvalue test. It computes the coefficient rather than merely proving that one exists.

It does NOT prove the natural-scale raw bound in all singular cases and does NOT resolve the original gamma=1 switching orbit. Those remain distinct. The present theorem is a substantive static-to-dynamic certificate, not a claim that every weakly infeasible system passes the test.
