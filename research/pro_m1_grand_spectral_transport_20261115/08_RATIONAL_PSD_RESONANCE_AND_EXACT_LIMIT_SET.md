# Checkpoint 08 — rational PSD resonance and its exact last-step limit set

2026-11-15. This checkpoint derives the counterexample theorem from the uniform nonlinear trapping proof in Checkpoint 07. Its starting family is entirely rational. A deliberately conservative explicit numerical threshold is supplied separately in Checkpoint 09; without that additional bound, the theorem here quantifies over all sufficiently large integers M. This is the gamma=2 system, not a resolution of the earlier gamma=1 switching orbit. No historical-priority or journal-percentile claim is made.

## 1. The rational affine system and escape exponent

In S^7, with indices 0,...,6, let Fij=Eij+Eji and

 a=-(F01+F34)/2,
 L=span{E00+E33, E11-F02/2, E44-F35/2,
        E66+2(F02-F35), F06, E22-E55}, U=a+L.

Use the Frobenius orthogonal projections and the plain map

 T(Z)=Z+(2P_U Z-Z)_+-P_U Z.

An explicit equality description is

 X00-X33=0, X22+X55=0,
 X11+2X02-4X66=0, X44+2X35+4X66=0,
 X01=X34=-1/2,
 Xij=0 for every other off-diagonal pair except (0,2),(0,6),(3,5).

There are 22 independent equations. All coefficients and right-hand sides are rational. In the last line the already displayed pairs (0,1),(3,4) are excluded from the zero list.

An exact PSD solution would have X22=X55=0. PSD zero-row propagation then gives X02=X35=0. Writing c=X11,d=X44,r=X66, the equalities give c=4r,d=-4r. Nonnegativity forces c=d=r=0, contradicting X01=-1/2. Thus the system is infeasible.

For u>0 use two identical blocks on (0,1,2) and (3,4,5),

 [[1/(2u),-1/2,-u/2],[-1/2,u,0],[-u/2,0,u^3]],

and a zero seventh row and column. The two positive leaf diagonals have Schur sum 1/(4u)+1/(4u)=1/(2u), so both blocks are PSD. The only nonzero equality residual is X22+X55=2u^3. The trace is 1/u+2u+2u^3. Hence weak infeasibility and R_b(delta)=O(delta^(-1/3)) follow.

Conversely, a PSD matrix with Euclidean equality residual at most delta has X55<=delta, |X34|>=1/4 when delta<=1/4, and, with B=X33,d=X44,r=X66,

 d+4r<=2|X35|+delta<=2sqrt(B delta)+delta.

The (3,4) minor therefore gives 1/16<=Bd<=2B^(3/2)sqrt(delta)+B delta. For sufficiently small delta this forces B>=(1/64)delta^(-1/3). Thus the escape exponent is exactly alpha=1/3, independently of the dynamical proof.

## 2. An explicit rational starting family

For any positive integer M put t=1/M and s=isqrt(3M^8)/M^4, where isqrt denotes the integer floor of the nonnegative square root. Set

 J=-29s/30000, R0=3/2500,
 Cfa=2sJ+4R0, Ca=Cfa+3J/2,
 Ga=2R0-Cfa/2+3J/2, Q=R0-12J.

Define Z0(M) by symmetry and the following entries, all others being zero:

 Z00=Z33=M, Z22=Z55=sM/3,
 Z11=t(3/8+3s/16)+t^3 Ca,
 Z44=t(3/8+3s/16)-t^3 Ca,
 Z02=3t(s-1)/16+t^3 Ga,
 Z35=3t(s-1)/16-t^3 Ga,
 Z01=Z34=-1/2+9s t^2/64,
 Z12=s/4+t^2 J, Z45=s/4-t^2 J,
 Z06=t/50, Z16=Z26=0, Z66=t^3 Q.

These are exact rational numbers, not rounded algebraic numbers. Checkpoint 07 proves that every sufficiently large M enters a forward-invariant nonlinear spectral chamber.

## 3. The theorem

Put

 b0=1/sqrt(3), N=9/16, c0=27sqrt(3)/256,
 cA=(4c0)^(1/4), Fstar=(2-sqrt(3))/640,
 V=cA*diag(1,0,b0,1,0,b0,0),
 Rstar=N*sqrt(Fstar)/cA^3.

For every sufficiently large integer M, the exact orbit starting at Z0(M) has

 Zk=V k^(1/4)+Zconst+O(k^(-1/4)),
 Zconst=-(F01+F34)/2+(sqrt(3)/4)(F12+F45),

and its complete scaled last-step cluster set is

 Clust{k^(3/4)(Z_(k+1)-Zk)}
   = V/4 + Rstar {cos(theta)F06+sin(theta)F26:theta in R}.       (3.1)

In particular Rstar>0 and the proposed universal last-step law is false for this rational affine–PSD problem with rational starts. The Frobenius radius of the circle in (3.1) is sqrt(2)Rstar, because ||Fij||_F=sqrt(2).

The norm nevertheless has an exact limit:

 k^(3/4)||Z_(k+1)-Zk||_F
   -> (||V||_F/4)*sqrt(1+(2-sqrt(3))/90).                     (3.2)

The normalized-state chordal length satisfies

 [sum_(k=K)^(n-1)||Z_(k+1)/||Z_(k+1)||-Zk/||Zk||||]/log n
   -> (2/3)sqrt(Fstar)>0.                                   (3.3)

Thus even finite angular length of normalized states fails, although their direction converges. All matrix norms without a subscript in (3.3) are Frobenius norms.

## 4. Radius, amplitude and phase

Use the scaled coordinates of Checkpoint 07, and write tau=t^2. Its all-time trapping bounds imply

 t_next=t-c0*t^5+O(t^7),
 Delta xi=N*tau*eta+O(tau^2), Delta eta=-N*tau*xi+O(tau^2),
 Ftilde_next-Ftilde=tau^2[a0*Ftilde-B0*Ftilde^2]+O(tau^3),

where a0=2c0-N^2>0, B0=135sqrt(3)/2 and Fstar=a0/B0. All remainders are uniform along the actual orbit.

The first recurrence makes t decrease to zero: a positive limit would contradict its negative increment bounded away from zero. Expanding reciprocal fourth powers gives

 t_k^(-4)=4c0 k+O(sqrt(k)),
 t_k~(4c0 k)^(-1/4), sum tau_k^2=infinity, sum tau_k^3<infinity.

The O(sqrt(k)) refinement follows by first obtaining the leading equivalence and then summing the O(t_k^2) error in the reciprocal recurrence.

On the trapped amplitude interval Ftilde is bounded above and bounded away from zero. For Y=Ftilde-Fstar, squaring its recurrence gives

 Y_next^2<=Y^2-c*tau^2*Y^2+C*tau^3

for fixed c,C>0 on a sufficiently late tail. The positive error is summable. The usual elementary product iteration proves Y->0: subtract the summable error tail to obtain a convergent almost-decreasing quantity, then use sum tau^2=infinity to exclude a positive limit. Hence xi^2+eta^2->Fstar.

Choose a continuous unwrapped argument theta_k of xi_k+i eta_k. The phase recurrence and the positive amplitude lower bound yield

 theta_(k+1)-theta_k=-N*tau_k+O(tau_k^2).

The increments are eventually negative, tend to zero, and have divergent sum in magnitude. Every angle modulo 2pi is therefore approached along a first-crossing subsequence. More precisely theta_k=-3^(1/4)sqrt(k)+O(log k), up to an additive constant. No interpolation or differentiation of an orbit remainder is used.

## 5. Remove the apparent leading symmetric fast steps

The O(tau) trapping bounds alone would allow symmetric fast increments of order t^3, so an additional tracking argument is needed for the COMPLETE cluster set (3.1).

Put u_k=(C_k,G_k). Analyticity of the exact chart and the established fine bounds give

 u_(k+1)=Ms*u_k+g(H_k)+tau_k*r0(E_k,xi_k,eta_k)+O(tau_k^2),

where r0 is smooth on the fixed compact chamber. To see why no uncontrolled coordinate appears in r0, replace C,G by Psi(H,b0), chi by H*eta/b0, the asymmetric coordinates by psi_a, j by jstar, and f by fs0. Each replacement changes the coefficient by O(tau); multiplied by tau this is O(tau^2). The auxiliary coordinates ad,bd,fa enter too late in the exact polynomial chart to affect this coefficient. Replacing H by H0 inside r0 has the same permissible error. The dependence on E is retained.

Write b_k=g(H_k)+tau_k*r0(E_k,xi_k,eta_k) and u_k^*=(I-Ms)^(-1)b_k. The trapping recurrences give Delta H=O(tau^2), Delta E=O(tau^3), and Delta(xi,eta)=O(tau). Consequently b_(k+1)-b_k=O(tau_k^2). Strict contraction of Ms and tau_(k+1)/tau_k->1 imply u_k-u_k^*=O(tau_k^2) on a tail. Indeed multiply the error recurrence by tau_k^(-2); its contraction factor stays below one and its forcing is bounded. Thus

 Delta C_k=O(tau_k^2), Delta G_k=O(tau_k^2).

Returning to physical entries, their steps are O(t^5), not order t^3. The other nonradial entries outside positions (0,6),(2,6) have increments O(t^4) or smaller. The exact leading step is therefore

 d_k=t_k^3[c0(E00+E33)+cB(E22+E55)
                       +N eta_k F06-N xi_k F26]+O(t_k^4),
 cB=27/256=b0*c0.                                           (5.1)

This is obtained from the update equations, not by differentiating the state expansion.

The radius expansion and bounded scaled coordinates give the asserted state expansion directly. Equation (5.1), t_k^3*k^(3/4)->cA^(-3), and the complete phase cluster set prove (3.1). Orthogonality of the displayed matrix entries gives (3.2); the exact simplification is

 2Rstar^2/(||V||_F^2/16)=(2-sqrt(3))/90.

## 6. Infinite angular motion with an exact coefficient

The leading state is radial, with ||Z_k||_F~t_k^(-1)sqrt(8/3). The two transverse entries in (5.1) are orthogonal to its leading direction and have Frobenius magnitude sqrt(2)N sqrt(Fstar)t_k^3(1+o(1)). Radial normalization therefore gives

 ||Z_(k+1)/||Z_(k+1)||-Zk/||Zk||||
   =(sqrt(3)/2)N sqrt(Fstar)t_k^4(1+o(1)).

The effects of the fixed state term, all other step entries, and the quadratic normalization remainder are respectively O(t_k^5), O(t_k^5), and O(t_k^8), negligible here. Since t_k^4~1/(4c0 k), summation proves (3.3).

## 7. Exact nonlinear attenuation budget

Let W_k=(Z06,Z16,Z26), r_k=||W_k||, and

 rho_k=(||Delta W_k||^2+2v66,k*s66,k)/r_k^2,
 L_n=sum_(k=K)^(n-1)-log(1-rho_k).

The exact cut identity gives r_n^2=r_K^2 exp(-L_n). Since r_n^2~Fstar*t_n^2,

 L_n=(1/2)log n+C+o(1).

Furthermore

 ||Delta W_k||^2/r_k^2=N^2*t_k^4+O(t_k^6)
                    =sqrt(3)/(4k)+O(k^(-3/2)),
 rho_k=O(1/k).

Expanding -log(1-rho_k), with a summable quadratic remainder, proves

 sum_(k=K)^(n-1) v66,k*s66,k/r_k^2
     =(1/4-sqrt(3)/8)log n+C'+o(1).                         (7.1)

This is the critical accumulated complementarity loss for p=1/4. The positive equilibrium of the corrected amplitude equation makes the nonlinear loss exactly balance the rescaling gain. Thus the persistent mode is not a frozen linearization artifact.

## 8. Same state, good and bad actual orbits; higher orders

Two identical three-by-three state blocks with a zero seventh row and column form an invariant subspace. Set the transverse and asymmetric coefficients in Section 2 to zero, retaining its rational approximations to the symmetric reference values. For all sufficiently large M the three-by-three chart, symmetric fast contraction, H filter, and charge argument give the same radial asymptotic, with all transverse entries identically zero. The two-order fast tracking of Section 5 then gives k^(3/4)d_k->V/4 for this actual reference orbit.

Nonexpansiveness bounds the distance between any two actual orbits by their initial distance. Hence every start for this affine system has the same leading state V k^(1/4). Yet the good reference orbit and the rational resonant family have different last-step norm coefficients. This also shows that one-good-orbit transfer below p=1/2 fails already for affine–PSD DRS, not merely for general firmly nonexpansive maps.

For any m>=7 impose a block-diagonal affine system U direct-sum {0_(m-7)} and start from Z0(M) direct-sum 0. Both Frobenius projections preserve the block decomposition. The same exact obstruction therefore occurs in every matrix order at least seven.

## Scope

This disproves the universally quantified last-step law once the trapping theorem is accepted; it does not classify all singular PSD systems. The general static-excess/kinetic-energy replacement theorem is separate. The original gamma=1 starting orbit and the historical-priority/publication requirements are not settled by this checkpoint.
