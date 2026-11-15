# Checkpoint 16 — a uniform rational family of spectral resonances

Date: 2026-11-15. This continuation independently derives the parameter-dependent spectral coefficients and extends the separated-chamber argument of 07–09. It does not settle the original gamma=1 small-start orbit. The conclusion is for the exact Frobenius-metric, affine-first, unanchored DRS map. Historical priority and publication benchmarking are not inferred.

## 1. Statement

For gamma>0 put

 a=-(F01+F34)/2,
 L_gamma=span{E00+E33, E11-F02/2, E44-F35/2,
              E66+gamma(F02-F35), F06, E22-E55},
 U_gamma=a+L_gamma, T_gamma(Z)=Z+(2P_Ugamma Z-Z)_+-P_Ugamma Z.

All indices are 0,...,6. Put

 b0=1/sqrt(3), H0=sqrt(3)/4, N=9/16,
 kappa=9sqrt(3)/8, c0=27sqrt(3)/256, cB=27/256,
 cA=(4c0)^(1/4), V=cA diag(1,0,b0,1,0,b0,0),
 a0=2c0-N^2=27(2sqrt(3)-3)/256,
 B_gamma=3sqrt(3)gamma(22gamma+1)/4,
 F_gamma=a0/B_gamma=9(2-sqrt(3))/(64gamma(22gamma+1)),
 R_gamma=N sqrt(F_gamma)/cA^3.

**Theorem.** For every rational gamma in [3/2,5/2], and every integer M>=10^50000000000, the entirely rational initial matrix in Section 2 generates an exact orbit satisfying

 Z_k=V k^(1/4)+Z_const+O(k^(-1/4)),
 Z_const=-(F01+F34)/2+(sqrt(3)/4)(F12+F45),
 Clust{k^(3/4)(Z_(k+1)-Z_k)}
    =V/4+R_gamma{cos(theta)F06+sin(theta)F26:theta in R}.

In particular the scaled step does not converge. Its norm does converge, with

 k^(3/4)||Z_(k+1)-Z_k||_F
   ->(||V||_F/4)sqrt(1+(2-sqrt(3))/(gamma(22gamma+1))).

The normalized-state chordal length divided by log n tends to (2/3)sqrt(F_gamma)>0. Every starting point of the same operator has the same leading state V k^(1/4), by nonexpansiveness. The oscillatory conclusion holds on a relatively open set of starts in the invariant block space S^{(0,1,2,6)} direct-sum S^{(3,4,5)} containing each displayed starting point; no openness in the entire S^7 is asserted.

All these affine systems are weakly infeasible and have escape exponent alpha=1/3. The example is therefore a parameter family, not one isolated choice of coupling. The parameter threshold below is a threshold for a uniformly separated spectral chart, not a complete dynamical bifurcation classification.

## 2. Uniform rational entry

Let t=1/M and s=isqrt(3M^8)/M^4. Set epsilon=1/50 and

 J=-s(14gamma+1)/30000, R0=3/2500,
 Cfa=2sJ+2gamma R0, Ca=Cfa+3J/2,
 Ga=gamma R0-Cfa/2+3J/2, Q=R0-6gamma J.

The symmetric matrix Z0(gamma,M) has entries

 Z00=Z33=M, Z22=Z55=sM/3,
 Z11=t(3/8+3s/16)+t^3 Ca,
 Z44=t(3/8+3s/16)-t^3 Ca,
 Z02=3t(s-1)/16+t^3 Ga,
 Z35=3t(s-1)/16-t^3 Ga,
 Z01=Z34=-1/2+9s t^2/64,
 Z12=s/4+t^2 J, Z45=s/4-t^2 J,
 Z06=t/50, Z16=Z26=0, Z66=t^3 Q,

and every other entry zero. Rational gamma gives exact rational data and start. One particular uniform witness is M=10^(10^12); decimal expansion of this integer is unnecessary.

For gamma in [3/2,5/2], F_gamma is decreasing and

 F_gamma/2 < 1/2500 < 3F_gamma/2.

The smaller of the two uniform endpoint gaps exceeds 10^-6. These inequalities follow by substitution at gamma=3/2,5/2 and squaring the resulting rational bounds for sqrt(3).

Weak infeasibility is independent of the dynamics. A PSD solution would have X22=X55=0, hence X02=X35=0, and X11=2gamma X66, X44=-2gamma X66. Positivity kills all three diagonals, contradicting X01=-1/2. The two identical PSD blocks

 [[1/(2u),-1/2,-u/2],[-1/2,u,0],[-u/2,0,u^3]]

with zero seventh row violate only X22+X55=0 by 2u^3 and have trace of order u^-1. Conversely, an equality-residual-delta PSD point satisfies, with B=X33,d=X44,r=X66,

 d+2gamma r<=2sqrt(B delta)+delta,
 1/16<=Bd<=2B^(3/2)sqrt(delta)+B delta

for sufficiently small delta. Thus its trace is bounded below by a positive constant times delta^-1/3. The affine description and Frobenius metric are unchanged.

## 3. Exact coordinates and projection

Use A=(Z00+Z33)/2, B=(Z22+Z55)/2, t=1/A, tau=t^2, b=B/A; H=(Z12+Z45)/2; j=(Z12-Z45)/(2t^2); xi=Z06/t, eta=Z26/t, chi=Z16/t^2; C=(Z11+Z44)/(2t), G=(Z02+Z35)/(2t); Ca=(Z11-Z44)/(2t^3), Ga=(Z02-Z35)/(2t^3), Q=Z66/t^3. The auxiliary variables ad,bd,fa,f are exactly those of 07.

The affine Gram equations give, exactly,

 c=2(C-G)/3,
 r=(3Q+4gamma Ca+8gamma Ga)/(3+8gamma^2),
 caf=2(Ca-Ga+gamma r)/3, gaf=-caf/2+gamma r.

The physical affine entries on (11),(44) are t*c plus/minus t^3*caf; those on (02),(35) are -t*c/2 plus/minus t^3*gaf; and u66=t^3*r. This explicitly verifies that the projection is orthogonal in the original Frobenius metric.

The signed charge is independent of gamma:

 E=tr(DZ^2), D=diag(1,-1,-3,1,-1,-3,-1),
 E_next-E=-tr(Dd^2), d=T_gamma Z-Z.

Indeed the anticommutator with D annihilates a and preserves every generator of L_gamma. The exact charge formula for b in 07 Section 1 is unchanged. The compatible seventh-column cut obeys exactly

 ||W_next||^2+||Delta W||^2+2v66*s66=||W||^2,
 v=(2u-Z)_+, s=(Z-2u)_+.

These identities, not a frozen linearization, control radial drift and attenuation.

## 4. Weighted spectral chart and its sharp sign condition

The first reflected block in coordinates (0,1;2,6) is

 R_PP=[[a/t,-beta],[-beta,t*d]],
 R_QQ=[[-B_ref/t,-t*eta],[-t*eta,t^3*q]],
 R_QP=[[-t*K,-h],[t*xi,-t^2*chi]],

where

 a=1-tau^3 ad, B_ref=b-tau^3 bd,
 beta=1/2+tau*f+tau^2*fa,
 d=2c-C+tau(2caf-Ca), h=H+tau*j,
 K=c+G-tau(2gaf-Ga), q=2r-Q.

Its positive invariant graph is X=[[t^2*x,t*y],[t^2*zeta,t*omega]]. Substitution into the exact Riccati equation gives precisely the four polynomial equations of 07, with the just-displayed gamma-dependent affine coefficients. The second block has opposite asymmetric signs and no sixth-coordinate coupling.

At tau=0, near the symmetric reference state,

 y=-H/b0, x=(-c-G+y/2)/(1+b0),
 delta=2c-C+H^2/b0-1/4,
 omega=(xi/2-chi+H*eta/b0)/delta, zeta=xi+omega/2.

At the symmetric fast equilibrium and chi=H0*eta/b0,

 delta=1/8, x=-N, y=-3/4, zeta=3xi, omega=4xi.

The implicit graph Jacobian is invertible, with determinant factor b0(1+b0)delta. The charge plus both graph systems has determinant, up to sign, 2b0^3(1+b0)^2 delta. Nonzero eigenvalue multiplicities cause no problem here.

Define

 S_gamma(xi,eta)=(sqrt(3)/2)gamma(14gamma+1)xi^2
    +(sqrt(3)/2)gamma(2gamma-1)eta^2
    -3gamma(2gamma-1)xi*eta.

At the fast/filter targets derived below, the final small Schur eigenvalue has sign equal to

 -[S_gamma-sqrt(3)eta^2].

The determinant of the quadratic form S_gamma-sqrt(3)eta^2 is

 (3gamma/2)(8gamma^3-16gamma-1).

Its xi^2 coefficient is positive. Thus this form is positive definite precisely for gamma>gamma_c, where gamma_c is the unique positive zero of 8gamma^3-16gamma-1 (approximately 1.44448; this decimal is not used). On [3/2,5/2], its determinant is at least 9/2 and its trace is below 100, so its least eigenvalue exceeds 9/200. Also F_gamma>1/4000. On the thick annulus xi^2+eta^2>=F_gamma/4 the Schur margin therefore exceeds 10^-6.

A sufficiently small fixed thick neighborhood preserves this sign and delta>0. Hence the analytic graph is the actual positive spectral subspace, with inertia (2,2), throughout the chosen neighborhood. The second block has inertia (2,1).

## 5. Fast equilibrium and periodic filter

At H=H0, symmetric fast equilibrium and chi=(3/4)eta, the asymmetric fast update is

 Ca_next=caf+3j/2,
 Ga_next=[b0 Ga+(1-b0)gaf+(j-xi*eta)/2]/(1+b0),
 Q_next=Q+3xi^2-r,

up to O(tau). Its fixed point is

 R0=3xi^2, Cfa=2sqrt(3)j+2gamma R0+sqrt(3)xi*eta,
 psi_gamma=(Cfa+3j/2, gamma R0-Cfa/2+3j/2, R0-6gamma j).

Let M_gamma be the linear part of this map and W=diag(2,4,1). The three leading principal minors of W-M_gamma^T W M_gamma, in order, are

 [16gamma^2-18+16sqrt(3)]/(3+8gamma^2)^2,
 [(-128+96sqrt(3))gamma^2-64+44sqrt(3)]/(3+8gamma^2)^2,
 [-64+44sqrt(3)]/(3+8gamma^2)^2.

They are strictly positive for every gamma>=0. Thus the map is strictly contractive in the stated weighted norm, uniformly on any compact parameter interval. On [3/2,5/2], the normalized Gram-defect determinant is greater than 1/2000; since its eigenvalues are at most one, its least eigenvalue is at least 1/2000. A norm contraction factor at most 1-10^-4 is consequently valid. The symmetric fast matrix is unchanged from 05.

After fast tracking, the independent leading coefficients are

 Delta xi=N*tau*eta+O(tau^2),
 Delta eta=-N*tau*xi+O(tau^2),
 Delta j=tau[-kappa*j-(9gamma/2)xi^2-(3sqrt(3)/4)xi*eta]+O(tau^2).

For clarity, the last coefficient can be derived before setting r=R0. The leading asymmetric h increment is

 (1/b0)[(3/4)j-(3/8)j-H0*caf]
   =-kappa*j-(3gamma/2)r-(3sqrt(3)/4)xi*eta

at the fast fixed point. Substituting r=3xi^2 gives the displayed filter. This derivation retains the diagonal feedback.

The unique quadratic periodic target is

 j_gamma=-S_gamma/(6gamma).

It satisfies exactly

 N(eta partial_xi-xi partial_eta)j_gamma
  =-kappa*j_gamma-(9gamma/2)xi^2-(3sqrt(3)/4)xi*eta.

Thus the filter error has multiplier 1-kappa*tau, not an undamped independent parameter. At these targets, v66=3xi^2*t^3+O(t^5) and s66=S_gamma*t^3+O(t^5).

## 6. Exact averaging correction

Write S_gamma=A_gamma xi^2+B2_gamma eta^2+C_gamma xi*eta, where A_gamma,B2_gamma,C_gamma are its three displayed coefficients. Define the quartic

 P_gamma=(C_gamma/N)[(15/16)xi^4-(9/8)xi^2 eta^2-(9/16)eta^4]
        +(B_gamma-6A_gamma)xi^3 eta/N-B_gamma xi eta^3/N.

Direct polynomial differentiation proves

 N(eta partial_xi-xi partial_eta)P_gamma
   =6xi^2 S_gamma-B_gamma(xi^2+eta^2)^2.

This is a zero-angular-mean correction; at gamma=2 it is exactly the earlier P4. With

 F=A^2||W||^2=xi^2+eta^2+tau*chi^2,
 Ftilde=F+tau*P_gamma,

the exact cut identity, radial recurrence and this polynomial identity give

 Ftilde_next-Ftilde
  =tau^2[a0*Ftilde-B_gamma*Ftilde^2]+O(tau^3).

The coefficient a0 is positive and independent of gamma. The stable positive equilibrium is F_gamma. This proves the stated formula rather than extrapolating amplitudes from finite simulations.

## 7. Uniform nonlinear trapping

Here are the complete dependency steps; all constants below can be uniform on [3/2,5/2]. First choose a fixed compact spectral chamber with E in [-3,0], amplitude in [F_gamma/4,2F_gamma], and small fixed errors about the five targets. The sign margins in Section 4 ensure an analytic actual projection. Let

 e_s=(C,G)-Psi(H,b0), e_H=H-H0,
 e_chi=chi-H*eta/b0,
 e_a=(Ca,Ga,Q)-psi_gamma(j,xi,eta), e_j=j-j_gamma(xi,eta).

The exact chart, before imposing fine bounds, gives

 e_s,next=Ms e_s+O(tau),
 e_H,next=e_H+tau[f0(H)+O(||e_s||)+O(tau)],
 e_chi,next=O(tau),
 e_a,next=M_gamma e_a+O(||e_s||+|e_H|+|e_chi|+tau),
 e_j,next=(1-kappa*tau)e_j
       +O(tau(||e_s||+|e_H|+|e_chi|+||e_a||)+tau^2),

where f0(H)=H^2(3b0/2-2H)/b0^3 and f0'(H0)=-kappa. The moving targets have O(tau) increments on the thick chamber. No quotient e_j/tau is needed to bound the earlier fast forcing. The auxiliary ad,bd,fa have bounded reset leading maps independent of their own current values; the input orders tau^3,tau^3,tau^2 in the exact chart prove this. The coarse f map has leading value b0*x*y.

Choose a coarse f bound and auxiliary bounds first, then fine bounds K_s*tau,K_H*tau,K_chi*tau,K_a*tau,K_j*tau in that order, and the refined f bound last. Strict fast contraction absorbs O(tau) forcing; the slow contractions absorb O(tau^2) forcing. Changes of the fine widths are O(tau^3), smaller than the slow contraction margins. This triangular order precludes circular choices.

Before a hypothetical first amplitude or charge exit, these bounds imply

 t_next=t-c0*t^5+O(t^7), every physical step entry O(t^3),
 |Delta E|<=C*tau^3, tau-tau_next>=c0*tau^3.

The charge variation telescopes to at most (C/c0)tau_initial; an initial charge near -3/2 stays in [-3,0] for sufficiently small tau_initial. The corrected-amplitude drift is inward on [F_gamma/2,3F_gamma/4] and [5F_gamma/4,3F_gamma/2], uniformly in gamma. Its O(tau^3) error is absorbed by the order-tau^2 inward drift. One-step changes cannot jump across the bands. This preserves the thick annulus, hence the spectral signs. There is no finite first exit.

For the rational start, sqrt(3)-s is between zero and tau_initial^2. The five initial errors and the refined f error are O(tau_initial^2), uniformly in gamma; the auxiliary coordinates vanish; E=-3/2+O(tau_initial), Ftilde=1/2500+O(tau_initial). Thus all sufficiently large M enter strictly.

## 8. An explicit uniform bound, without a numerical orbit

The conservative envelope of inherited 09 extends uniformly with these changes, which are verified independently. Clearing 3+8gamma^2 from each Riccati equation gives seven polynomial equations in 24 variables. Their term counts are [14,40,40,34,38,34,34], totaling 234; total degrees are [8,8,8,8,7,8,8]; maximum rational coefficient is 16. Thus the envelope of 500 terms, degree at most 8, coefficient at most 1000 remains valid. The exact script gamma_spectral_chart.py derives the equations from the unscaled reflected matrix and checks these facts.

Keep K_aux=10^10000, B=10^100000, C=B^1000, rho=B^-4, and tau_*=C^-1000. At tau=0 the graph Jacobian is the same as in 09; clearing the denominators scales its six graph rows by 3+8gamma^2>=21 and cannot enlarge the maximum-row-sum inverse bound 10^20. The complex-parameter contraction proof, ordinary-transpose spectral reconstruction, and Cauchy bounds of 09 therefore apply with these same generous constants. The extra gamma variable changes dimension factors from 23 to 24 only. The denominator remains bounded away from zero on these tiny complex neighborhoods.

The fast contraction factor 1-10^-4 remains valid by Section 5. The leading small-eigenvalue margin is now taken as 10^-6, not 10^-5; the entry amplitude gap is taken as 10^-6, not 10^-4. The inward amplitude drift still exceeds 10^-7*tau^2. All common-error bounds C, C^42*tau^3 and C^50*tau^3, and the fine radii in 09 are unchanged and overwhelmingly smaller than these margins when tau<=C^-1000. Initial errors are bounded by 10^6*tau_initial^2 and charge/amplitude errors by 10^6*tau_initial. It follows that M>=C^500=10^50000000000 suffices uniformly.

This verifies an exact rational witness by explicit analytic inequalities. It does not claim reasonable bit length or a practical onset.

## 9. Limits, full steps, and relative openness

Trapping gives t_k^-4=4c0*k+O(sqrt(k)), sum tau_k^2=infinity, sum tau_k^3<infinity. Squaring the logistic error Ftilde-F_gamma gives a stable scalar recurrence with summable error, so Ftilde->F_gamma. The phase satisfies Delta theta=-N*tau+O(tau^2); it tends monotonically through infinitely many rotations with increments tending to zero. The first-crossing argument yields every angular cluster direction.

The second-order fast tracking in 08 is uniform in gamma: the symmetric fast forcing has the form g(H)+tau*r0(E,xi,eta,gamma), whose consecutive differences are O(tau^2). Hence Delta C,Delta G=O(tau^2). The complete physical step is

 d_k=t_k^3[c0(E00+E33)+cB(E22+E55)
             +N eta_k F06-N xi_k F26]+O(t_k^4).

This proves the full circle and norm limit in Section 1; no state remainder is differentiated. Radial normalization gives the angular coefficient (2/3)sqrt(F_gamma). Strict entry inequalities and continuity of all coordinate maps give the relatively open set of starts. Block embedding gives the same obstruction in every matrix order at least seven.

## 10. Precise remaining boundary

The separated-chart threshold gamma_c is exact. At gamma=1 the form S_gamma-sqrt(3)eta^2 is negative at xi=0, eta!=0. Consequently the above target dynamics cannot remain in the same inertia chart through a full rotation. This does NOT prove damping at gamma=1, nor does it rule out a switching periodic regime. The original small rational gamma=1 orbit remains unresolved here. The family theorem is a disproof of the universally quantified last-step law, not a classification of every singular SDP orbit or a completed publication/priority gate.
