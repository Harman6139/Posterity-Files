# Checkpoint 05 — a local resonant orbit construction (proof draft)

2026-11-15. Status: proof draft, NOT yet promoted to a certified counterexample. The remaining audit concerns uniformity of the invariant tube and an effective numerical threshold for the rational family. This draft does not settle the original gamma=1 start. The purpose is to expose the last analytic gap, not to promote a formal amplitude equation to proof.

## 1. Proposed theorem

Use U=a+L in S^7, indices 0,...,6, with

    a=-(F01+F34)/2,
    L=span{E00+E33, E11-F02/2, E44-F35/2,
           E66+2(F02-F35), F06, E22-E55}.

Let Z0(M) be the exact rational family in Checkpoint 04, Section 6. Put

    b0=1/sqrt(3), H0=sqrt(3)/4, ell=3/4,
    C0=3/8, N=9/16, kappa=9sqrt(3)/8,
    c0=27sqrt(3)/256, cB=27/256,
    cA=(4c0)^(1/4), Fstar=(2-sqrt(3))/640,
    V=cA diag(1,0,b0,1,0,b0,0).

Proposed: for every sufficiently large integer M, the exact plain DRS orbit has Zk/k^(1/4)->V and the cluster set of k^(3/4)(d06,d26) is the circle of radius N sqrt(Fstar)/cA^3. Its normalized-state chordal length Ln satisfies liminf Ln/log n >=(2/3)sqrt(Fstar)>0. The weak infeasibility and escape exponent 1/3 are already established geometrically. The proposed orbit proof does not assume the inherited cosmic theorem.

## 2. Exact formulas

The pattern of blocks (0,1,2,6) and (3,4,5) is invariant. Define

    A=(Z00+Z33)/2, Ad=(Z00-Z33)/2,
    B=(Z22+Z55)/2, Bd=(Z22-Z55)/2,
    cs=(Z11+Z44)/2, ca=(Z11-Z44)/2,
    gs=(Z02+Z35)/2, ga=(Z02-Z35)/2,
    hs=(Z12+Z45)/2, ha=(Z12-Z45)/2,
    fs=(Z01+Z34)/2, fa=(Z01-Z34)/2,
    w=Z06, z=Z26, v=Z16, q=Z66.

The affine projection u has

    u00=u33=A, u22=Bd, u55=-Bd,
    caff=2(cs-gs)/3, r=(3q+8ca+16ga)/35,
    cafa=2(ca-ga+2r)/3, gafa=-cafa/2+2r,
    u11=caff+cafa, u44=caff-cafa,
    u02=-caff/2+gafa, u35=-caff/2-gafa,
    u66=r, u06=w, u01=u34=-1/2.

For R=2u-Z, vplus=R_+, s=(-R)_+, d=vplus-u,

    Z_next=u+s, vplus=u+d, s=Z-u+d, vplus s=0.

For W=(Z06,Z16,Z26), exactly

    ||W_next||^2-||W||^2=-||Delta W||^2-2vplus66 s66.  (2.1)

For D=diag(1,-1,-3,1,-1,-3,-1), E=tr(DZ^2), the congruence identity gives E_next-E=-tr(Dd^2), because Da+aD=0 and X->DX+XD preserves L. Explicitly

    E=2(A^2-3B^2)+2Ad^2-6Bd^2-2cs^2-2ca^2
        -4gs^2-4ga^2-8hs^2-8ha^2-q^2-2v^2-4z^2.   (2.2)

## 3. Scaled spectral chamber

Set t=1/A, b=B/A, xi=w/t, eta=z/t, chi=v/t^2, j=ha/t^2, Ca=ca/t^3, Ga=ga/t^3, Q=q/t^3, C=cs/t, G=gs/t. The symmetric leading values are

    Cs0=3/8+3sqrt(3)/16, Gs0=3(sqrt(3)-1)/16,
    fs0=9sqrt(3)/64.

For H,b near H0,b0, define Cf=2H^2/b^2-H/b and Psi(H,b)=(Cf+H^2/b,H^2/b-Cf/2). For j,xi,eta define

    R0=3xi^2, Cf_a=2sqrt(3)j+4R0+sqrt(3)xi eta,
    psi_a=(Cf_a+3j/2, 2R0-Cf_a/2+3j/2, R0-12j),
    S2=29sqrt(3)xi^2+3sqrt(3)eta^2-18xi eta,
    jstar=-S2/12,
    P4=18eta^4-120sqrt(3)eta^3xi+36eta^2xi^2
                         -(568sqrt(3)/3)eta xi^3-30xi^4,
    F=A^2||W||^2=xi^2+eta^2+t^2 chi^2,
    Ftilde=F+t^2 P4.

Consider a tube with fixed constants:

    E in [-3,0], Ftilde in [Fstar/2,3Fstar/2],
    hs-H0=O(t^2), (C,G)-Psi(hs,b)=O(t^2),
    chi-ell eta=O(t^2), (Ca,Ga,Q)-psi_a=O(t^2),
    j-jstar=O(t^2), Ad,Bd=O(t^5), fa=O(t^4),
    (fs+1/2)/t^2-fs0=O(t^2).                         (3.1)

These O bounds define a proposed tube; they are not assumed orbit conclusions. Equation (2.2) gives b=b0+O(t^2) uniformly in the tube.

### Analytic projector chart

For the first block, order positive coordinates P=(0,1), negative Q=(2,6). Its positive invariant space is the graph X=[[t^2 x,t y],[t^2 zeta,t omega]]. The Riccati equation is

    R_QP+R_QQ X-X R_PP-X R_PQ X=0.

Divide its four equations by t,1,t,t^2. They are analytic in tau=t^2 and bounded tube coordinates. At tau=0 the solution is y=-ell, x=-N, omega=4xi, zeta=3xi. The first two linear factors are b0 and 1+b0. The final two equations are zeta-beta omega=xi and C0 omega-beta zeta=0, beta=1/2, with determinant C0-beta^2=1/8. The implicit function theorem gives a uniform branch on compact parameter sets.

Writing Fgraph=[I;X], the candidate positive part is

    vplus=Fgraph Y Fgraph*,
    Y=(R_PP+R_PQ X)(I+X*X)^(-1).

The Schur complement of Y is t/8+O(t^3)>0. Eliminating coordinates 0,2, then the remaining positive middle coordinate, the last Schur complement of R has coefficient

    t^3[2Raff-Q-3xi^2+eta^2/b0],
    Raff=(3Q+8Ca+16Ga)/35.

At fast equilibrium this is -t^3[S2-sqrt(3)eta^2]+O(t^5). Exactly S2-sqrt(3)eta^2>=xi^2+eta^2. Indeed the associated matrix minus I has positive diagonal and determinant 94-31sqrt(3)>0. Thus on the annulus the branch is the actual PSD projection. The second block similarly has two positive eigenvalues and one negative eigenvalue. The weighted equations are analytic in t^2; omitted terms advance by two powers of t.

## 4. Leading recurrences

### Fast variables

    C_next=Caff+hs^2/b+O(t^2),
    G_next=bG/(1+b)+(b-1)Caff/[2(1+b)]
                         +hs/[2(1+b)]+O(t^2),
    Caff=2(C-G)/3.

At b0 the matrix is Ms=[[2/3,-2/3],[-2/3+sqrt(3)/3,(1+sqrt(3))/6]], strictly contractive in C^2+2G^2. Its frozen fixed point is Psi.

    Ca_next=Cafa+3j/2+O(t^2),
    Ga_next=b0 Ga/(1+b0)+(1-b0)Gafa/(1+b0)
                         +(j/2-xi eta/2)/(1+b0)+O(t^2),
    Q_next=Q+3xi^2-Raff+O(t^2),
    Cafa=2(Ca-Ga+2Raff)/3, Gafa=-Cafa/2+2Raff.

The fixed point is psi_a. The linear matrix is

    Ma=[[34/35,-2/35,4/35],
        [(-2+sqrt(3))/35,(97-31sqrt(3))/70,(8-4sqrt(3))/35],
        [-8/35,-16/35,32/35]].

It is strictly contractive in 2Ca^2+4Ga^2+Q^2. Both contractions can be proved as firmly nonexpansive linear maps with trivial fixed space. Alternatively their positive Gram-defect leading principal minors are, respectively,

    Ms: (8sqrt(3)-9)/9, (11sqrt(3)-16)/9;
    Ma: (46+16sqrt(3))/1225,
        (428sqrt(3)-576)/1225, (44sqrt(3)-64)/1225.

For the asymmetric recurrence, the negative Schur formula gives s11 asymmetric coefficient 2H0j/b0. The (vplus s)02 equation gives the asymmetric coefficient of s02 as [j/2+b0(Cafa+Ga-4Raff)-xi eta/2]/(1+b0). Finally the positive Schur formula gives vplus66=3xi^2t^3+O(t^5).

### Slow filters and phase

    Delta hs=t^2 f(hs,b)+O(t^2||(C,G)-Psi||+t^4),
    f(H,b)=H^2(3b/2-2H)/b^3,
    partial_H f(H0,b0)=-kappa,
    chi_next=hs eta/b+O(t^2).

Once the fast errors are O(t^2),

    Delta xi=N t^2 eta+O(t^4),
    Delta eta=-N t^2 xi+O(t^4),
    Delta j=t^2[-kappa j-9xi^2-(3sqrt(3)/4)xi eta]+O(t^4).

For the last coefficient, put S0=-12j. Fast equilibrium gives s02_asym/t^3=Ga+Cafa/2-2R0=-S0/8. Taking the antisymmetric part of (vplus s)12 yields

    Delta ha/t^4=b0^(-1)[-(1/2)S0/8-C0 j-H0 Cafa]+O(t^2).

Substitution proves the filter. The vplus16 s62 term contributes only at the next order. The polynomial jstar satisfies exactly N(eta partial_xi-xi partial_eta)jstar=-kappa jstar-9xi^2-(3sqrt(3)/4)xi eta, so its error obeys e_next=(1-kappa t^2)e+O(t^4).

For phase, (vplus s)06 gives A Delta Z06-(beta ell+lambda C0)eta t^2=O(t^4), beta=lambda=1/2, beta ell+lambda C0=N. The (s vplus)26 equation gives b0 N xi t^2+(b0/t)Delta Z26=O(t^4).

### Radius and amplitude

Positive Schur gives vplus22=cB t^3+O(t^5): inverse(PP)00=3t+O(t^3), vplus02=-3t/16+O(t^3). Negative Schur gives s00=b0N^2t^3+O(t^5)=c0t^3+O(t^5). Its extra rank-two term has numerator [s06-s02 s26/s22]^2=O(t^10) and denominator bounded below by a positive multiple of t^3, so is O(t^7). Therefore

    Delta A=c0t^3+O(t^5), t_next=t-c0t^5+O(t^7),
    Delta E=O(t^6).

Every step component is O(t^3). Also Ad_next,Bd_next=O(t^5), fa_next=O(t^4), and (fs_next+1/2)/t_next^2=fs0+O(t^2).

The exact cut identity gives

    Delta F=t^4[(2c0-N^2)F-6xi^2S2]+O(t^6).

Since exactly

    N(eta partial_xi-xi partial_eta)P4
        =6xi^2S2-(135sqrt(3)/2)(xi^2+eta^2)^2,

we obtain

    Delta Ftilde=t^4[a0 Ftilde-B0 Ftilde^2]+O(t^6),
    a0=27(2sqrt(3)-3)/256>0, B0=135sqrt(3)/2,
    a0/B0=Fstar.

## 5. Elementary tracking inequalities

If t_next=t+O(t^5), e_next<=q e+C t^2+O(t^4), q<1, then e<=K t^2 is invariant for K>C/(1-q) and sufficiently small t. If e_next<=(1-kappa t^2)e+C t^4+O(t^6), it is invariant for K>C/kappa. The changing width K t_next^2 differs from Kt^2 only by O(t^6), smaller than the respective contraction margins. Signed errors use upper and lower barriers.

## 6. Uniform trapping — still under adversarial audit

Choose compact amplitude and charge windows as in (3.1), and slightly larger compact neighborhoods for the scaled variables. The analytic chart supplies uniform Taylor constants. Choose tube constants in this order: coarse auxiliary asymmetry and scaled-fs bounds; symmetric fast errors; hs-H0; chi-ell eta; asymmetric fast errors; j-jstar; finally the refined fs error.

The intended triangular mechanism is that a later slow error influences an earlier fast forcing only at an additional power of t^2. In particular Psi(hs,b) changes by O(t^4), versus an O(t^2) fast contraction margin. The target psi_a changes by O(t^2) through the bounded leading phase and filter, not through the quotient (j-jstar)/t^2. After all constants are fixed, sufficiently small t absorbs the higher-order dependencies. The tracking inequalities would then preserve all errors in (3.1).

The charge boundary is separate: t^2-t_next^2>=c0t^6, so total variation of E is at most a constant times t0^2. An initial charge in [-2,-1] remains in [-3,0] for small enough t0. The amplitude drift is positive on [Fstar/2,3Fstar/4] and negative on [5Fstar/4,3Fstar/2]. The O(t^6) remainder is dominated by the inward t^4 drift, and small one-step changes prevent jumps across the protective bands. Thus amplitude cannot exit. Its positive lower bound and the preserved filter errors keep the small eigenvalue negative. A finite no-first-exit induction would close the exact nonlinear argument.

This section must be checked against the full weighted expansion to ensure that no omitted leading dependence defeats the triangular choice. Until then the proposed counterexample is NOT certified. In particular a finite one-step high-precision test cannot establish uniform infinite-time trapping.

## 7. Consequences conditional on trapping

Then t_k^(-4)/k->4c0, sum t_k^4=infinity, sum t_k^6<infinity. The logistic recurrence and inward bands force Ftilde->Fstar. The phase increment is -Nt^2+O(t^4), tends to zero and has divergent negative sum; the first-crossing argument gives every angular cluster direction. This yields the proposed transverse circle.

The bounded scaled coordinates give the state limit directly. For normalized states, the cut increment has norm N sqrt(Fstar)t^4/sqrt(8/3)+o(t^4); counting both symmetric copies and using t^4~1/(4c0k) gives liminf Ln/log n >=(2/3)sqrt(Fstar). Block embedding preserves the obstruction in every order at least seven.

## 8. Rational entry and exact unresolved items

The rational start family uses s=floor(sqrt(3M^8))/M^4, error below t^4. Direct substitution gives initial hs, symmetric fast, asymmetric fast, and filter errors O(t^4), chi=eta=0, Ad=Bd=fa=0, E=-3/2+O(t^2), F=1/2500. Thus it enters every positive tube for all sufficiently large M, PROVIDED the trapping statement is valid. This does not yet specify a certified numerical M0.

The original gamma=1 switching orbit is not covered. A numerical M0, the complete universal replacement, priority verification, and the requested publication benchmark remain outstanding. No grand completion is asserted.
