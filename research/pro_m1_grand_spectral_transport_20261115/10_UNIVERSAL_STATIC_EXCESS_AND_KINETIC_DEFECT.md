# Checkpoint 10 — universal static excess and kinetic defect

2026-11-15. A general replacement theorem for plain affine–cone DRS. The cone may be any closed self-dual semialgebraic cone in a finite-dimensional Euclidean space; products and arbitrary affine coupling are included. The theorem is not restricted to the order-seven example. No historical-priority assertion is made here.

## 1. Setup and a static convex profile

Let K=K* be a closed semialgebraic cone, U=a+L with a perpendicular to L, and U intersect K empty at distance zero. Put P=P_L, Q=I-P and

 Tz=z+P_K(2P_Uz-z)-P_Uz, z_(k+1)=Tz_k,
 z_k=a+x_k+y_k, x_k=Pz_k, y_k=Qz_k-a,
 d_k=z_(k+1)-z_k, q_k=||d_k||^2,
 v_k=P_K(a+x_k-y_k), s_k=P_K(-a-x_k+y_k).

Exactly,

 v_k=a+x_(k+1)+Delta y_k,
 s_k=y_(k+1)+Delta x_k,
 v_k,s_k in K, <v_k,s_k>=0.                            (1.1)

Define the static convex minimum-distance profile

 D(r)=min{||Qv-a||:v in K, ||Pv||<=r}, r>=0.             (1.2)

The minimum exists: on a bounded objective sublevel both P and Q components are bounded. It is positive at every finite r and tends to zero, by weak infeasibility. It is convex and nonincreasing in r, by taking convex combinations of competitors.

The common-state theorem, reproved briefly in Section 3, supplies rational 0<p<1 and V!=0 with z_k=V k^p+o(k^p) for every start. Write H=PV, G=QV, and A0=p^2||V||^2. Set

 r_k=||Pv_k||=||x_(k+1)||,
 delta_k=||Qv_k-a||=||Delta y_k||,
 e_k=delta_k^2-D(r_k)^2>=0.                            (1.3)

Thus e_k compares the ACTUAL cone shadow with the best cone point at the same permitted primal radius. It is not defined by the desired velocity or its direction.

For lambda>1, m=floor(lambda n), put

 I_(n,m)=sum_(j=n)^(m-1) j^(2p-2),
 X_n(lambda)=sum_(j=n)^(m-1)e_j / I_(n,m).              (1.4)

All limits below are for n tending to infinity; finite initial indices have no effect.

## 2. Main theorem

### A. Natural-scale dichotomy

The following are equivalent for a given orbit:

 (a) d_k=O(k^(p-1));
 (b) X_n(lambda) is bounded for one fixed lambda>1;
 (c) X_n(lambda) is bounded for every fixed lambda>1.

Without any extra hypothesis, liminf k^(1-p)||d_k||>=p||V||. If (a) fails, the scaled step norms have unbounded limsup; equivalently the static excess is unbounded on at least one, and hence every, fixed-ratio family of windows.

### B. Exact radial and energy laws on the natural scale

Under these equivalent conditions,

 k^(1-p)<Delta x_k,H> -> p||H||^2,
 k^(1-p)<Delta y_k,G> -> p||G||^2.                     (2.1)

For every fixed lambda>1,

 sum_(j=n)^(m-1) q_j
   = A0 I_(n,m)+2 sum_(j=n)^(m-1)e_j+o(I_(n,m)).       (2.2)

Equivalently,

 [sum_(j=n)^(m-1) j^(2p-2)||j^(1-p)d_j-pV||^2]/I_(n,m)
       =2X_n(lambda)+o(1).                            (2.3)

The factor two is exact: static shadow inefficiency is transferred to transverse kinetic energy by the two complementary shadows.

### C. Sharp exact-velocity criterion

Each of the following is equivalent:

 (i) k^(1-p)d_k -> pV;
 (ii) X_n(lambda)->0 for one fixed lambda>1;
 (iii) X_n(lambda)->0 for every fixed lambda>1;
 (iv) delta_k/D(r_k)->1.

No prior natural-scale assumption is required in these equivalences: (ii) itself implies part A. This strengthens a pointwise saturation criterion to an averaged, nonnegative static criterion.

### D. Exact norm coefficients

For e>=0, the following are equivalent:

 k^(2-2p)q_k -> A0+2e;
 X_n(lambda)->e for every fixed lambda>1.              (2.4)

It is enough in the second condition to use fixed ratios approaching one from above, together with bounded excess for one fixed ratio. One ratio alone is not asserted to determine a positive excess coefficient.

### E. Genuine equation residuals

For any equality description U={z:Az=b}, including redundant rows,

 Av_k-b=A Delta y_k,
 ||(AA*)^(dagger/2)(Av_k-b)||=delta_k.                  (2.5)

The vector k^(1-p)(Av_k-b) has a limit if and only if (i) holds, and its limit is then pAG!=0. Thus redundant equalities cannot conceal a persistent normal transverse mode. Ill-conditioning can change its measured size but not the equivalence.

## 3. The state, balance, and exact profile coefficient

For completeness, these foundational facts need no regularity of the actual orbit. The discounted point z(t) is the unique solution of

 z(t)=[a+t Tz(t)]/(1+t), equivalently Tz(t)-z(t)=(z(t)-a)/t.

The right-hand map is a contraction. Its graph is semialgebraic. The path diverges, because a bounded subsequence would yield a fixed point and hence a feasible point. Nonexpansiveness gives ||z(t)-a||<=t||Ta-a||. Comparison with an arbitrary approximate fixed point u gives

 ||z(t)-a||<=2||u-a||+t||Tu-u||.

Since inf||Tu-u||=0, the path is o(t). The one-variable semialgebraic Puiseux theorem therefore gives z(t)-a=c t^p+o(t^p), with nonzero c and rational 0<p<1, and the differentiated expansion along this path. Comparing the actual orbit with z(t0+k/p), whose local iteration defect is o(k^(p-1)), and summing the defects proves

 z_k=p^(-p)c k^p+o(k^p).

This uses only nonexpansiveness; it does not differentiate an actual-orbit remainder. Thus V=p^(-p)c.

Decompose the discounted point as a+x(t)+y(t). Its complementary shadows are

 v(t)=a+(1+1/t)x(t)+y(t)/t,
 s(t)=x(t)/t+(1+1/t)y(t).

With E(t)=||x(t)||^2+||y(t)||^2, complementarity gives exactly

 <a,y(t)>=-E(t)/t,
 t(t+1)E'(t)/2=E(t)+t||y(t)||^2.                      (3.1)

For the derivative identity, <v'(t),s(t)>=0: for fixed t the nonnegative pairing of v(t+h) with s(t) has a minimum at h=0. Substitute the displayed shadows and differentiate only the smooth Puiseux path. Leading terms in (3.1) give

 ||G||^2=p||V||^2, ||H||^2=(1-p)||V||^2,
 H,G in K, <H,G>=0, <a,G>=0.                         (3.2)

Both H and G are nonzero.

The central cone point v(t) uniquely minimizes over K the strictly convex quadratic

 ||Pv||^2/[2(t+1)^2]+||Qv-a||^2/2.

Its gradient is s(t)/(t+1), a cone point orthogonal to v(t), which is the exact optimality condition. Consequently D(||Pv(t)||)=||Qv(t)-a||. The Puiseux radius is eventually strictly increasing and covers a tail. Eliminating t yields

 D(r)~p||G||*||H||^((1-p)/p)*r^(-(1-p)/p),
 D(r_k)^2~p^2||G||^2*k^(2p-2).                       (3.3)

These are static optimization statements, not assumptions on actual last-step behavior.

## 4. Exact complementary-shadow energy

Firm nonexpansiveness gives q_k nonincreasing and

 q_k-q_(k+1)>=||d_(k+1)-d_k||^2.

Put w_k=<y_(k+1),Delta y_k>, phi_k=<v_(k+1),s_k> and psi_k=<v_k,s_(k+1)>. Self-duality makes phi_k,psi_k nonnegative. Expanding (1.1) at two consecutive indices gives

 ||Delta x_(k+1)||^2
   =w_k-w_(k+1)+<Delta y_k,Delta y_(k+1)>-psi_k,
 phi_k+psi_k=[q_k-q_(k+1)-||d_(k+1)-d_k||^2]/2.        (4.1)

In particular sum_(j=n)^(m-1)psi_j<=q_n/2. Summation, using the polarization identity for the normal increments and shifting the tangent endpoint once, gives

 sum_(j=n)^(m-1)q_j
   =2 sum_(j=n)^(m-1)delta_j^2+w_n-w_m+R_(n,m),
 |R_(n,m)|<=4q_n.                                    (4.2)

This identity is the conic energy transfer absent from a generic firmly nonexpansive map.

## 5. Bounded static excess implies the natural step bound

Suppose X_n(lambda) is bounded for one fixed lambda. Equation (3.3) implies that the sum of delta_j^2 on any fixed-ratio window is O(n^(2p-1)). A finite covering by lambda-windows gives the same estimate on every interval [an,bn] with fixed 0<a<b.

Choose an index l in [n/4,n/3] and an index r in [2n,3n] where delta_l^2 and delta_r^2 are at most C n^(2p-2); averaging ensures such choices. Since y_k=O(k^p), |w_l|+|w_r|=O(n^(2p-1)). Sum the first identity in (4.1) between l and r, drop the nonpositive psi term, and apply Cauchy–Schwarz to consecutive normal increments. This proves that the sum of tangent squared increments across this larger interval is O(n^(2p-1)). Adding the normal energies and using monotonicity of q on [n/2,n] gives

 n q_n=O(n^(2p-1)), hence q_n=O(n^(2p-2)).

This finite-window proof is valid also for p<=1/2; no divergent-tail estimate is used. Conversely the latter bound makes delta_j^2 and e_j at most q_j and immediately bounds X_n(lambda) for every lambda.

The unconditional lower bound follows from

 ||z_floor(lambda k)-z_k||<= (floor(lambda k)-k)||d_k||,

the state law, and then lambda decreasing to one.

## 6. Radial rigidity without differentiating the state

For a nonexpansive map, monotonicity of I-T gives

 <d_k-d_j,z_k-z_j><=0.

Under the natural step bound, insert z_k=V k^p+o(k^p). For j/k in [1+h,1+2h] this gives <d_k,V>>=<d_j,V>+o(k^(p-1)), uniformly. Averaging telescopes the d_j. A backward separated window gives the opposite bound. Letting h decrease to zero proves

 k^(1-p)<d_k,V> -> p||V||^2.                          (6.1)

To split it into tangent and normal parts, use the central shadows at t=k/p. Cross-cone positivity gives <v_k,s(t)>>=0. Their exact central pairing with a, (3.1), yields

 liminf k^(1-p)<Delta y_k,G>>=p||G||^2.

Actual complementarity gives exactly

 <a,y_(k+1)>=-<z_(k+1)-a,d_k>
             =-p||V||^2 k^(2p-1)+o(k^(2p-1)),

by (6.1). Now <v(t),s_k>>=0 gives the tangent liminf at least p||H||^2. Since their sum has the exact limit (6.1), both liminfs are equalities and the individual limits (2.1) follow. Consequently

 w_k=p||G||^2 k^(2p-1)+o(k^(2p-1)).                   (6.2)

No convergence of transverse step directions has been assumed.

## 7. The exact excess identity

Insert (6.2) and delta_j^2=D(r_j)^2+e_j into (4.2). For fixed lambda,

 w_n-w_m=p(1-2p)||G||^2 I_(n,m)+o(I_(n,m)).

At p=1/2 the leading endpoint terms cancel and their difference is o(1); I_(n,m)->log lambda, so the same formula applies. The q_n remainder is o(I_(n,m)) by the natural bound. Equations (3.2)–(3.3) then give

 2p^2||G||^2+p(1-2p)||G||^2
    =p||G||^2=p^2||V||^2=A0.

This proves (2.2). Expanding the squared distance to pV and using (6.1), uniformly over a fixed-ratio window, proves (2.3).

## 8. Why zero averaged excess forces individual velocities

Assume X_n(lambda)->0 for one fixed lambda. Part A gives the natural bound. Cauchy–Schwarz and (6.1) give the pointwise lower estimate

 q_j>=[A0-o(1)]j^(2p-2).

Suppose q_n>=(A0+epsilon)n^(2p-2) on a subsequence. Choose c<1 sufficiently close to one, with c>1/lambda, so that A0 c^(2p-2)<A0+epsilon/4. Monotonicity then forces q_j-A0 j^(2p-2) to be at least a positive multiple of epsilon n^(2p-2) throughout [cn,n]. Place this interval inside the lambda-window starting at ceil(n/lambda). Outside this subinterval the preceding pointwise lower estimate permits only an o(I) negative contribution. The resulting positive macroscopic excess contradicts (2.2) and X->0. Thus

 k^(2-2p)q_k->A0.

Together with (6.1), equality in the limiting Cauchy–Schwarz inequality gives k^(1-p)d_k->pV. Conversely this vector limit and (3.3) imply e_k=o(k^(2p-2)), hence zero excess on every fixed window and delta_k/D(r_k)->1.

Finally pointwise saturation directly implies e_k=o(k^(2p-2)); it therefore implies zero averaged excess and the full velocity. This proves every equivalence in part C.

## 9. Norm coefficients and original equations

If the norm coefficient in (2.4) exists, (2.2) immediately determines every excess limit. Conversely, if all fixed-window excess limits equal e, (2.2) gives the same fixed-window squared-speed averages with coefficient A0+2e. Forward and backward averages bound the nonincreasing q_k. Sending the window ratio to one proves the asserted norm coefficient. This is a monotone-density argument, not differentiation of an asymptotic sequence.

Equation (2.5) follows because ker A=L and A*(AA*)^dagger A=Q. If the scaled raw residual has any finite vector limit, apply the inverse of A restricted to L^perp to obtain a limit Y for k^(1-p)Delta y_k. Summing these actual increments and comparing with y_k=G k^p+o(k^p) forces Y=pG. Its norm therefore saturates (3.3), and part C gives the full step law. Conversely the full step law gives residual limit pAG. Since G is a nonzero member of L^perp, AG!=0.

## 10. Sharp realization and scope

The gamma=2 PSD resonance of Checkpoints 07–09 has

 X_n(lambda)->Rstar^2>0 for every lambda>1,

by its exact norm coefficient and (2.2). Its entire transverse circle has squared Frobenius radius 2Rstar^2, exactly matching (2.3). The invariant reference orbit has zero excess. Thus the same rational affine–PSD system realizes both zero and strictly positive defects with the same common state vector.

The regular-spectrum theorem in Checkpoint 02 gives a non-tautological sufficient condition for zero defect, valid for coupled products of real and complex PSD cones. The cut identity and the resonance amplitude equation explain how a singular spectral mode realizes positive defect. The universal theorem here additionally covers every self-dual semialgebraic cone, without matrix coordinates, spectral simplicity, regular faces, or full row rank of the equality description.

Without bounded excess, no natural-scale pointwise upper bound is asserted. The unconditional fixed-window vector law still follows from telescoping the state:

 n^(-p)sum_(j=n)^(floor(lambda n)-1)d_j -> (lambda^p-1)V.

This limitation is explicit rather than concealed inside an unproved universal residual-rate hypothesis.
