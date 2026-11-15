# Checkpoint 07 — uniform trapping and rational entry for gamma=2

2026-11-15. This supplies the missing first-exit argument for the separated gamma=2 chamber. The conclusion is for every sufficiently large member of the explicit rational starting family, not for a numerically selected value of M. It makes no claim about the original gamma=1 switching orbit. Historical priority and the full publication brief remain separate.

## 1. Replace the drifting ratio by an exact charge coordinate

Use all coordinates and constants of Checkpoint 05. Put tau=t^2, H=hs, ad=Ad/t^5, bd=Bd/t^5, fa=(Z01-Z34)/(2t^4), f=((Z01+Z34)/2+1/2)/t^2. The exact charge E=tr(D Z^2) gives

 b^2 = 1/3 - tau(E+8H^2)/6
       - tau^2(2C^2+4G^2+4eta^2)/6
       - tau^3(8j^2+2chi^2)/6
       - tau^4(2Ca^2+4Ga^2+Q^2)/6
       + tau^6(2ad^2-6bd^2)/6.

Take its positive square root. Hence b is analytic near tau=0 on any fixed bounded coordinate set, and b=b0+O(tau), b0=1/sqrt(3). There is no independent ratio-error recursion to close.

## 2. The entire weighted projection chart is explicit

For the first reflected block, ordered (0,1;2,6), define

 a=1-tau^3 ad, B=b-tau^3 bd,
 beta_f=1/2+tau*f+tau^2*fa,
 c=2(C-G)/3, r=(3Q+8Ca+16Ga)/35,
 ca_f=2(Ca-Ga+2r)/3, ga_f=-ca_f/2+2r,
 d=2c-C+tau*(2ca_f-Ca), h=H+tau*j,
 K=c+G-tau*(2ga_f-Ga), q=2r-Q.

Exactly,

 R_PP=[[a/t,-beta_f],[-beta_f,t*d]],
 R_QQ=[[-B/t,-t*eta],[-t*eta,t^3*q]],
 R_QP=[[-t*K,-h],[t*xi,-t^2*chi]].

The graph X=[[t^2*x,t*y],[t^2*zeta,t*omega]] is determined by the following four polynomial equations, obtained by dividing the exact Riccati equation by t,1,t,t^2 entrywise:

 F1=-K-(a+B)x+beta_f*y-tau*eta*zeta+tau*x*y*h
       +tau^2*x^2*K-tau^2*zeta*(x*xi-y*chi),
 F2=-h-B*y+tau*(-eta*omega+beta_f*x-d*y+y^2*h)
       +tau^2*(x*y*K-omega*(x*xi-y*chi)),
 F3=xi-a*zeta+beta_f*omega+tau*(-eta*x+x*omega*h)
       +tau^2*(q*zeta+x*zeta*K-zeta*(zeta*xi-omega*chi)),
 F4=-chi-eta*y+beta_f*zeta-d*omega+y*omega*h
       +tau*(q*omega+y*zeta*K-omega*(zeta*xi-omega*chi)).

At tau=0 the solution is

 y=-H/b0,
 x=(-c-G+y/2)/(1+b0),
 delta=2c-C+H^2/b0-1/4,
 omega=[xi/2-(chi-H*eta/b0)]/delta,
 zeta=xi+omega/2.

The graph Jacobian determinant, up to sign, is b0(1+b0)delta. At the symmetric reference point delta=1/8. The parameterized implicit function theorem supplies an analytic branch uniformly on a compact neighborhood of the entire amplitude annulus. The second reflected block uses the first two equations, zero couplings to coordinate 6, and opposite asymmetric signs.

The positive part is exactly

 vplus=[I;X](R_PP+R_PQ X)(I+X*X)^(-1)[I;X]*.

The positive middle Schur complement has leading term t*delta. The remaining Schur complement of the full first block, after eliminating the large positive/negative directions and the positive middle direction, has leading coefficient

 t^3{2r-Q+eta^2/b0-[xi^2+(xi/2-(chi-H*eta/b0))^2/delta]}.

At the intended equilibria this is -t^3[S2-sqrt(3)eta^2]. The exact inequality S2-sqrt(3)eta^2 >= xi^2+eta^2 gives a uniform strictly negative sign on a compact annulus bounded away from zero. By continuity it remains negative on a fixed sufficiently small thick neighborhood. The graph therefore represents the actual PSD projection on that neighborhood for all sufficiently small positive t, not an analytically continued wrong-sign branch.

## 3. A fixed thick chamber precedes all fine constants

Let Psi(H,b0) be the symmetric fast target of Checkpoint 05, and psi_a(j,xi,eta) its asymmetric target. Set

 e_s=(C,G)-Psi(H,b0), e_H=H-H0,
 e_chi=chi-H*eta/b0,
 e_a=(Ca,Ga,Q)-psi_a(j,xi,eta),
 e_j=j-jstar(xi,eta).

First choose a thick compact chamber: E in [-3,0]; xi^2+eta^2 in [Fstar/4,2Fstar]; the five errors in sufficiently small fixed neighborhoods of zero; f in a fixed neighborhood of fs0. Shrink these fixed neighborhoods so that the spectral signs in Section 2 have a uniform margin and f_H stays strictly negative near H0. Fine estimates such as |e_H|<=K_H*tau have NOT been imposed at this stage.

The coordinates ad,bd,fa may subsequently be allowed any fixed sufficiently large compact bounds: they do not appear in the leading chart at tau=0. They have reset, not neutral, leading maps, as established below.

## 4. Exact leading derivatives give a triangular hierarchy

On the thick chamber, the analytic map gives the following estimates. The constants are uniform there:

 (i) e_s,next = Ms*e_s + O(tau).
 (ii) e_H,next = e_H + tau*[f0(H)+O(||e_s||)+O(tau)],
      f0(H)=H^2(3b0/2-2H)/b0^3.
 (iii) e_chi,next=O(tau).
 (iv) e_a,next=Ma*e_a+O(||e_s||+|e_H|+|e_chi|+tau).
 (v) e_j,next=(1-kappa*tau)e_j
       +O(tau*(||e_s||+|e_H|+|e_chi|+||e_a||)+tau^2).

Here Ms,Ma are the strictly contractive matrices from Checkpoint 05, with the exact positive Gram-defect minors independently checked in the accompanying symbolic script. Their norms are taken in C^2+2G^2 and 2Ca^2+4Ga^2+Q^2. Also f0(H0)=0 and f0'(H0)=-kappa<0.

Here are derivations of the relevant leading derivatives, to make the dependency assertion checkable. The symmetric map is

 C_next=2(C-G)/3+H^2/b0+O(tau),
 G_next=[b0*G+(b0-1)*c/2+H/2]/(1+b0)+O(tau).

Its fixed point for fixed H is Psi(H,b0). At that point x=-H^2/b0^2, y=-H/b0, and the leading H drift is -x/2+c*y=f0(H). Before imposing this point, the difference from f0(H) is bounded by a constant times ||e_s||. The leading chi update is H*eta/b0; subtracting the target at the next point changes it by O(tau), because all slow coordinates have O(tau) increments on the thick chamber.

At H=H0, e_s=e_chi=0, write beta=1/2, c0f=3/8, x0=-9/16, y0=-3/4. If ay and ax denote half the differences of the first tau derivatives of y and x in the two blocks, the polynomial chart gives

 ay=-(j+2xi*eta)/b0,
 ax=[beta*ay+(2ga_f-Ga)-(3/2)xi*eta]/(1+b0).

The asymmetric coefficient of the first derivative of the scaled positive (1,1) entry is 2ca_f-Ca+3j/2. Hence

 Ca_next=ca_f+3j/2+O(tau),
 Ga_next=[b0*Ga+(1-b0)*ga_f+(j-xi*eta)/2]/(1+b0)+O(tau),
 Q_next=Q+3xi^2-r+O(tau).

This is the affine map with matrix Ma and fixed point psi_a. Perturbing H,e_s,e_chi gives the error in (iv). The target psi_a changes by O(tau) on the thick chamber; its derivative is bounded and j,xi,eta have O(tau) increments. No bound for e_j/tau is used.

The leading asymmetric H filter is

 -beta*ax+c0f*ay+y0*(2ca_f-Ca+3j/2).

At psi_a this simplifies exactly to -kappa*j-9xi^2-(3sqrt(3)/4)xi*eta. The leading phase coefficients are Delta xi=N*tau*eta, Delta eta=-N*tau*xi; perturbations are bounded by the preceding errors, plus O(tau^2). The polynomial identity for jstar in the symbolic script therefore yields (v). Smoothness on the fixed chamber bounds all remaining terms uniformly.

For (i), subtracting the moving Psi target costs O(tau) on the entire thick chamber. This does not involve e_H/tau. For (iv), the moving asymmetric target likewise costs O(tau), without e_j/tau. These facts are what prevent circular fine constants.

## 5. Auxiliary coordinates reset at leading order

Exactly,

 Ad_next=(s00-s33)/2,
 Bd_next=(v22-v55)/2,
 fa_next=(s01-s34)/(2*t_next^4),
 f_next=(s01+s34)/(2*t_next^2).

The first two identities use physical Ad,Bd; divide by t_next^5 for their scaled coordinates. In the two blocks s00 has the same leading t^3 coefficient, v22 has the same leading t^3 coefficient, and s01 has the same leading t^2 coefficient. Their differences start at t^5,t^5,t^4, respectively. The input ad,bd first enter the polynomial chart at order tau^3 and input fa at order tau^2, too late to enter these leading differences. Thus the scaled next ad,bd,fa have bounded smooth leading functions independent of their own current values, plus O(tau) remainders. Choosing their compact bounds larger than these leading suprema, then decreasing tau0, preserves them.

Moreover f_next=b0*x*y+O(tau). At symmetric equilibrium this is H^3/b0^2, equal to fs0 at H0. This first preserves a coarse fixed bound for f, and later gives |f_next-fs0|<=C*tau once e_s,e_H have their fine bounds. The coarse f bound is chosen before the auxiliary bounds; the refined f bound is chosen last.

## 6. Choose constants in a genuine order

A strict contraction inequality e_next<=q e+C*tau preserves e<=K*tau for any K>C/(1-q) and sufficiently small tau. A slow filter inequality e_next<=(1-c*tau)e+C*tau^2 preserves e<=K*tau for K>C/c. The change of the barrier K*tau_next from K*tau is O(tau^3), smaller than the slow contraction margin of order tau^2.

Choose, in order: a coarse f bound; coarse ad,bd,fa bounds; K_s from (i); K_H from (ii); K_chi from (iii); K_a from (iv); K_j from (v); and the refined K_f. Each uses only earlier fine bounds or the original thick compact chamber. Finally decrease tau0 so all fine regions lie inside that thick chamber and all displayed one-step barriers hold. The radial estimate tau_next=tau+O(tau^3), needed here, already holds on the thick chamber because the mean top increment is O(t^3); its positive leading coefficient at the target is c0.

Consequently, before any hypothetical first amplitude/charge exit, all five errors are O(tau), the auxiliary coordinates remain bounded, and f-fs0=O(tau).

## 7. Close the charge and amplitude windows

Under these bounds the exact chart gives

 t_next=t-c0*t^5+O(t^7),
 Delta xi=N*tau*eta+O(tau^2), Delta eta=-N*tau*xi+O(tau^2),
 v66=3xi^2*t^3+O(t^5), s66=S2*t^3+O(t^5).

Every physical entry of d=TZ-Z is O(t^3): the symmetric fast errors are O(tau), the H and j changes have the indicated additional factors, and f-fs0=O(tau). The exact congruence identity gives |Delta E|<=3||d||_F^2<=C*tau^3. For small tau, tau-tau_next>=c0*tau^3, so the total variation of E is at most (C/c0)*tau_initial. An initial E in [-2,-1] therefore cannot leave [-3,0] after decreasing tau_initial.

For F=A^2||W||^2 and Ftilde=F+tau*P4, the exact cut identity and polynomial rotation identity give

 Delta Ftilde=tau^2[a0*Ftilde-B0*Ftilde^2]+O(tau^3),
 a0=27(2sqrt(3)-3)/256>0, B0=135sqrt(3)/2,
 Fstar=a0/B0=(2-sqrt(3))/640.

The drift is uniformly positive on [Fstar/2,3Fstar/4] and negative on [5Fstar/4,3Fstar/2]. Decrease tau0 until the O(tau^3) error is smaller than half either inward drift. Bounded one-step changes also cannot jump across a protective band. Thus Ftilde stays in [Fstar/2,3Fstar/2]. Since Ftilde=xi^2+eta^2+O(tau), this preserves the thick annulus and its spectral sign margin.

There can therefore be no first exit, at any finite index. The exact nonlinear orbit is trapped for all time. The argument does not replace the map by an accumulated linearization.

## 8. Exact rational entry

For the explicit family Z0(M) of Checkpoint 04, let s=isqrt(3*M^8)/M^4. Then 0<=sqrt(3)-s<M^-4=tau_initial^2. Direct substitution gives

 E=-3/2+O(tau_initial), Ftilde=1/2500+O(tau_initial),
 e_s,e_H,e_chi,e_a,e_j=O(tau_initial^2),
 ad=bd=fa=0, f-fs0=O(tau_initial^2).

Also Fstar/2<1/2500<3Fstar/2. Every sufficiently large integer M therefore satisfies all entry inequalities, and the exact all-time trapping theorem applies to its entirely rational initial matrix. The proof gives existence of a finite threshold by explicit finite inequalities and analytic compact bounds; this checkpoint does not report a numerical value for that threshold.

The original gamma=1 orbit is outside the separated chart and is not settled by this theorem. The consequences for the scaled-step limit set are recorded separately to keep logical dependencies visible.
