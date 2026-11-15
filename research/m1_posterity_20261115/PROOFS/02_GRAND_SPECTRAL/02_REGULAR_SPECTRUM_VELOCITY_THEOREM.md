# Checkpoint 02 — regular spectral escape has an exact square-root velocity

2026-11-15. Status: complete proof below, with its additional spectral hypothesis explicit. This is not the arbitrary-order frontier: the balanced order-seven candidate violates that hypothesis. Historical originality is not certified.

## 1. The theorem

Let E be a finite product of real symmetric or complex Hermitian matrix spaces, with its real Frobenius inner product, and let K be the product of their positive semidefinite cones. Arbitrary coupling between blocks is allowed in the affine space U=a+L, where a is perpendicular to L. Assume U and K are disjoint at distance zero. Write P=P_L, Q=I-P, J=2P-I, and

    Tz=z+P_K(2P_Uz-z)-P_Uz=(z+|Jz+2a|)/2.

Suppose one actual orbit diverges in norm and has a cosmic limit N in int K:

    z_k/||z_k|| -> N, ||N||=1, every block of N positive definite.

Then there is V in int K, independent of the starting point, such that every orbit satisfies

    z_k=V sqrt(k)+o(sqrt(k)),
    sqrt(k)(z_(k+1)-z_k) -> V/2.

For the semialgebraic DRS systems here, the inherited cosmic theorem supplies the cosmic limit and a positive-power state remainder. Thus the theorem applies exactly when that common leading state is blockwise positive definite. In the notation of the handoff it forces p=1/2 and alpha=1. It does not assert that every weakly infeasible system has an interior cosmic direction.

Repeated nonzero eigenvalues are allowed throughout. The only spectral exclusion is a zero eigenvalue of the leading reflected matrix.

## 2. Complementary supports and exact radial energy

Nonexpansiveness makes step norms bounded. Dividing Tz_k=z_(k+1) by ||z_k|| gives T_0N=N, where T_0=(I+|J(.)|)/2. Consequently H=PN and G=QN belong to K, HG=0, and N=H+G. All products are blockwise. Because N is interior, in each block the support projections E and F of H and G are complementary. Zero-dimensional supports are permitted.

Every Y in L^perp intersect K satisfies <a,Y>>=0: take u_j in U and v_j in K with u_j-v_j tending to zero, and use <u_j,Y>=<a,Y> and <v_j,Y>>=0.

For every z, let d=Tz-z, u=P_Uz, v=(2u-z)_+, s=(z-2u)_+. Then v=u+d, s=z-u+d, vs=0. Scalar complementarity gives

    h(z):=||a||^2-<a,z>=<Tz,d>,
    ||Tz||^2-||z||^2=2h(z)-||d||^2.                  (2.1)

If <a,N> were positive, h(z_k) would tend to minus infinity and the squared norm would eventually strictly decrease, contradicting divergence. Thus <a,N><=0. Since a is perpendicular to H and weak feasibility gives <a,G>>=0, in fact <a,N>=<a,G>=0.

## 3. The center space and its strictly contractive complement

Define

    D_H={X in L:X=EXE},
    D_G={Y in L^perp:Y=FYF}, D=D_H orthogonal-sum D_G.

The support compressions are blockwise. H and G belong to the respective spaces. For Y in D_G, G plus or minus a sufficiently small multiple of Y belongs to K. Applying weak feasibility and <a,G>=0 to both signs gives <a,Y>=0. Hence a is perpendicular to D.

For n in D near N, with positive definite E and F blocks, put C_n=D|.|(Jn), M_n=(I+C_n J)/2. The absolute-value map is real analytic at the nonsingular Jn. In block eigenbases of n=H_n+G_n, C_n multiplies entries by

    +1 on E-E, -1 on F-F,
    (h_i-g_j)/(h_i+g_j) on E-F.

This follows by differentiating |S|^2=S^2: |S|C_n(B)+C_n(B)|S|=SB+BS. All denominators are positive. C_n is self-adjoint and contractive; its cross coefficients have modulus strictly less than one.

M_n is firmly nonexpansive, by differentiating that inequality for T_0. Its fixed space is exactly D. Indeed M_n x=x implies C_n Jx=x. Equality of norms forces Jx, and hence x, to be support-block diagonal. Then Px=ExE and Qx=FxF, so x belongs to D. The converse follows from the displayed derivative formula.

A linear contraction fixing D pointwise has adjoint fixing D pointwise, as follows by expanding ||M(d+t w)||^2<=||d+t w||^2 at t=0. Therefore D^perp is invariant under M_n. Firm nonexpansiveness implies that ||M_n w||=||w|| only if M_n w=w. Compactness gives

    ||M_n|_(D^perp)||<=q<1                           (3.1)

uniformly near N. Also C_n a is perpendicular to D, since C_n preserves D. This is the spectral mechanism: the only undamped modes are genuine support-preserving recession directions.

## 4. Two orders of nonlinear tracking

Decompose z=s+w, s=Pi_D z, w=Pi_(D^perp)z, r=||s||, n=s/r. Cosmic convergence gives r->infinity, n->N, w=o(r). Uniform Taylor expansion gives

    T(s+w)=s+M_n w+C_n a+r^(-1)F_1(n,w)
                     +O((||w||+1)^3/r^2),
    F_1(n,w)=D^2|.|(Jn)[Jw+2a,Jw+2a]/4.             (4.1)

For the first boundedness argument use the first-order remainder O((||w||+1)^2/r). Since w=o(r), (3.1) gives ||w_next||<=(q+o(1))||w||+O(1); hence w is bounded. Projection onto D yields

    s_next-s=O(1/r), r_next/r=1+O(r^(-2)),
    n_next-n=O(r^(-2)).                              (4.2)

Define smooth bounded normal functions

    w_0(n)=(I-M_n|_(D^perp))^(-1) C_n a,
    w_1(n)=(I-M_n|_(D^perp))^(-1)
                            Pi_(D^perp)F_1(n,w_0(n)).

Then

    w=w_0(n)+r^(-1)w_1(n)+O(r^(-2)).                (4.3)

Discrete details: subtracting w_0(n_next) from (4.1)'s normal projection gives a contraction recurrence with forcing O(1/r); (4.2) controls the change of w_0. Multiplication by r_next, using r_next/r->1, proves w-w_0=O(1/r). Substitute this into F_1 and subtract w_0(n_next)+r_next^(-1)w_1(n_next). The definition of w_1 cancels the forcing of order 1/r. What remains is O(r^(-2)); multiplication by r_next^2 proves (4.3). Both rescaled contraction factors remain strictly below one on a tail.

Consequently

    w_next-w=O(r^(-2)),
    d=r^(-1)b(n)+O(r^(-2)),
    b(n)=Pi_D F_1(n,w_0(n)).                         (4.4)

For the first assertion use (4.2)-(4.3). The difference of two O(r^(-2)) remainders is O(r^(-2)), which suffices; no orbit remainder is differentiated.

## 5. Positive radial drift and exact velocity

Put h_0(n)=||a||^2-<a,w_0(n)> and B=Jw_0(n)+2a. The defining equation gives w_0=C_n B. Hence

    4h_0(n)=||B||^2-||C_n B||^2>=0.                 (5.1)

Equality is impossible. It would force B and w_0 to be support-block diagonal. Then u_0=a+Pw_0=(B+w_0)/2 is supported entirely on E. Adding a sufficiently large multiple of H_n in L makes u_0 PSD, contradicting infeasibility. Thus h_0(N)>0.

Since a is perpendicular to D, (4.3) gives h(z_k)->h_0(N). Equation (4.4) gives d_k->0. From (2.1) and Cesaro averaging,

    ||z_k||^2/k -> 2h_0(N),
    r_k/sqrt(k) -> sqrt(2h_0(N)).                    (5.2)

Thus sqrt(k)d_k -> b(N)/sqrt(2h_0(N)). Summing this actual step asymptotic gives z_k/sqrt(k)->2b(N)/sqrt(2h_0(N)), whereas cosmic convergence and (5.2) give sqrt(2h_0(N))N. Therefore b(N)=h_0(N)N. Put V=sqrt(2h_0(N))N to obtain the theorem.

Every other orbit stays at bounded distance from the first and has the same interior cosmic limit. The proof applies to it with the same coefficient h_0(N), proving the all-start assertion.

## 6. Quantitative and residual consequences

The inherited semialgebraic state theorem gives some eta>0 with z_k=V sqrt(k)+O(k^(1/2-eta)). Smoothness of b in (4.4) implies, for zeta=min(eta,1/2)>0 or any smaller positive exponent,

    sqrt(k)d_k=V/2+O(k^(-zeta)).

Radial normalization annihilates the leading radial velocity, so normalized-state increments have norm O(k^(-1-zeta))+O(k^(-2)). Their total spherical length is finite. This corollary uses the inherited state remainder without differentiating it.

For H_V=PV, G_V=QV, the affine and cone shadows u_k,v_k satisfy u_k/sqrt(k),v_k/sqrt(k)->H_V and

    sqrt(k)(u_(k+1)-u_k), sqrt(k)(v_(k+1)-v_k) -> H_V/2.

Indeed v_k=u_k+d_k and sqrt(k)(d_(k+1)-d_k)->0. For U={z:A z=b}, including redundant equalities,

    sqrt(k)(A v_k-b) -> A G_V/2 !=0,
    sqrt(k)||(AA*)^(dagger/2)(A v_k-b)|| -> ||G_V||/2,
    sqrt(k)||d_k|| -> ||V||/2.

Whitening is exact since A*(AA*)^dagger A=Q. G_V cannot vanish, since an interior V in L would make a large affine shift feasible. Also G_V in L^perp implies A G_V cannot vanish.

## 7. Scope boundary

The proof covers coupled products of real and complex PSD cones, not merely independent Lorentz blocks. It assumes neither spectral simplicity nor the last-step conclusion. The condition N in int K makes JN nonsingular and supplies (3.1). The balanced order-seven candidate has singular N and lies outside this theorem. Thus this is a structural positive result, not either complete outcome required by the handoff.
