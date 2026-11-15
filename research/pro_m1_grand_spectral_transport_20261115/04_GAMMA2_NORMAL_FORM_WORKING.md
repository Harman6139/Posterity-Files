# Checkpoint 04 — gamma=2 spectral separation and candidate averaged invariant region

2026-11-15. IMPORTANT: leading analytic calculations, not yet a certified counterexample. The uniform nonlinear trapping argument and a certified threshold for the rational start family remain under audit. Do not promote high-precision one-step checks to an asymptotic proof.

## 1. Why change gamma

For the balanced affine family, the formal negative-small-eigenvalue branch gives

    S_gamma=(sqrt(3)/2)gamma(14gamma+1)xi^2
           +(sqrt(3)/2)gamma(2gamma-1)eta^2
           -3gamma(2gamma-1)xi eta.

Consistency requires S_gamma-sqrt(3)eta^2>0. Gamma=1 violates this for some phases. At gamma=2,

    S=29sqrt(3)xi^2+3sqrt(3)eta^2-18xi eta,
    S-sqrt(3)eta^2 >= xi^2+eta^2.

The last inequality is exact: the 2x2 matrix minus identity has positive diagonal and determinant 94-31sqrt(3)>0. More generally the determinant before subtracting identity is (3gamma/2)(8gamma^3-16gamma-1); gamma>=3/2 gives positivity. This removes the leading sign-switch obstruction, but does not itself control exact iterates.

## 2. Scaling and fast variables

In the invariant block pattern (0,1,2,6) and (3,4,5), put

    A=(Z00+Z33)/2, B=(Z22+Z55)/2, t=1/A, b=B/A,
    Hs=(Z12+Z45)/2, Ha=(Z12-Z45)/2=t^2 j,
    Z06=t xi, Z26=t eta, Z16=t^2 chi.

Constants:

    b0=1/sqrt(3), H0=sqrt(3)/4, ell=3/4,
    Caff=3/8, N=9/16, kappa=9sqrt(3)/8,
    c0=27sqrt(3)/256, cB=27/256,
    Cs0=3/8+3sqrt(3)/16,
    Gs0=3(sqrt(3)-1)/16, fs0=9sqrt(3)/64.

Let Ca=(Z11-Z44)/(2t^3), Ga=(Z02-Z35)/(2t^3), Q=Z66/t^3. At gamma=2 the exact affine formulas are

    R=r/t^3=(3Q+8Ca+16Ga)/35,
    Cafa=(2/3)(Ca-Ga+2R), Gafa=-Cafa/2+2R.

The proposed fast equilibrium is, with R0=3xi^2,

    S0=-12j,
    Cafa0=2sqrt(3)j+4R0+sqrt(3)xi eta,
    Ca0=Cafa0+(3/2)j,
    Ga0=2R0-Cafa0/2+(3/2)j,
    Q0=R0-12j.                                      (2.1)

## 3. Fast maps and filter

The leading asymmetric fast map is

    Ca_next=Cafa+(3/2)j,
    Ga_next=b0 Ga/(1+b0)+(1-b0)Gafa/(1+b0)
                      +((1/2)j-xi eta/2)/(1+b0),
    Q_next=Q+3xi^2-R.

Its linear matrix is

    [[34/35,-2/35,4/35],
     [(-2+sqrt(3))/35,(97-31sqrt(3))/70,
                                      (8-4sqrt(3))/35],
     [-8/35,-16/35,32/35]].

It is strictly contractive in norm squared 2Ca^2+4Ga^2+Q^2, by its positive Gram defect (equivalently its firmly nonexpansive representation and trivial fixed space). The largest weighted singular value is approximately 0.986324, a diagnostic not a proof premise.

The symmetric fast (Cs,Gs) matrix is

    [[2/3,-2/3],[-2/3+sqrt(3)/3,(1+sqrt(3))/6]],

strictly contractive in norm squared Cs^2+2Gs^2. Its quasi-equilibrium at H,b is Caff(H,b)=2H^2/b^2-H/b, Cs=Caff+H^2/b, Gs=H^2/b-Caff/2. The symmetric h drift is

    Delta Hs=t^2 f(Hs,b)+O(t^4),
    f(H,b)=H^2(3b/2-2H)/b^3,
    partial_H f(H0,b0)=-kappa.

At (2.1), the asymmetric filter is

    Delta j=t^2[-kappa j-9xi^2-(3sqrt(3)/4)xi eta]+O(t^4).

With Delta xi=N t^2 eta+O(t^4), Delta eta=-N t^2 xi+O(t^4), the quadratic periodic solution is j_*=-S_2/12. The desired uniform estimate j-j_*=O(t^2) is a trapping obligation, not yet a conclusion in this checkpoint.

## 4. Exact identities behind the expansion

D=diag(1,-1,-3,1,-1,-3,-1) annihilates a by anticommutator and its congruence map preserves L. Hence E=tr(DZ^2) satisfies E_next-E=-tr(D d^2) exactly. If d=O(t^3) and Delta A>=c t^3 hold in an invariant region, E stays bounded and b=b0+O(t^2).

The first block's positive spectral subspace can be expressed over coordinates (0,1) as the graph

    X=[[t^2 x,t y],[t^2 z,t w]], rows (2,6).

Its Riccati equation R_QP+R_QQ X-X R_PP-X R_PQ X=0 is analytic in t^2 after dividing the four entries by t,1,t,t^2. At t=0 the solution is x=-N,y=-ell,z=3xi,w=4xi. The Jacobian is invertible, with factors b0,1+b0,Caff-1/4=1/8. This supplies local uniform weighted Taylor remainders. It represents the actual PSD projection only while the small Schur eigenvalue is negative, with leading coefficient -S+sqrt(3)eta^2.

Under the intended O(t^2) fast-error estimates, direct blocks of v s=0 and rank-two Schur formulas give

    Delta Z06=N eta t^3+O(t^5),
    Delta Z26=-N xi t^3+O(t^5),
    v66=3xi^2 t^3+O(t^5), s66=S t^3+O(t^5),
    Delta A=c0 t^3+O(t^5).

For example (vs)06 has leading equation A Delta Z06-(beta ell+lambda Caff)eta t^2=0, where beta=lambda=1/2 and beta ell+lambda Caff=N. The (sv)26 equation gives the second phase component. The positive rank-two Schur formula gives v66; the negative Schur formula gives s00=b0 N^2 t^3. No state remainder is differentiated.

## 5. Averaging

For F=A^2||Z_[0:6,6]||^2 the exact cut energy gives

    Delta F=t^4[(2c0-N^2)F-6xi^2 S_2]+O(t^6).

Put

    P4=18eta^4-120sqrt(3)eta^3 xi+36eta^2xi^2
                         -(568sqrt(3)/3)eta xi^3-30xi^4,
    Ftilde=F+t^2 P4.

Exact symbolic differentiation yields

    N(eta partial_xi-xi partial_eta)P4
        =6xi^2 S_2-(135sqrt(3)/2)(xi^2+eta^2)^2.

Thus the proposed recurrence is

    Delta Ftilde=t^4[a0 Ftilde-B0 Ftilde^2]+O(t^6),
    a0=27(2sqrt(3)-3)/256>0, B0=135sqrt(3)/2,
    F_*=a0/B0=(2-sqrt(3))/640>0.

A successful trapping proof would yield t^(-4)/k->4c0, summability of the t^6 errors, Ftilde->F_*, infinite phase winding, and transverse scaled last-step amplitude N sqrt(F_*)/(4c0)^(3/4)>0. These consequences are conditional here.

## 6. Rational start family to certify

For integer M>=1 set t=1/M, s=floor(sqrt(3 M^8))/M^4, xi=1/50, eta=0,

    J=-29s/30000, R=3/2500,
    Cafa=2s J+4R, Ca=Cafa+(3/2)J,
    Ga=2R-Cafa/2+(3/2)J, Q=R-12J.

Define symmetric Z by

    Z00=Z33=M, Z22=Z55=s M/3,
    Z11=t(3/8+3s/16)+t^3 Ca,
    Z44=t(3/8+3s/16)-t^3 Ca,
    Z02=t*3(s-1)/16+t^3 Ga,
    Z35=t*3(s-1)/16-t^3 Ga,
    Z01=Z34=-1/2+t^2*9s/64,
    Z12=s/4+t^2 J, Z45=s/4-t^2 J,
    Z06=t/50, Z16=Z26=0, Z66=t^3 Q,

with all other entries zero. These entries are exactly rational. Its initial F=1/2500 lies in [F_*/2,3F_*/2]. A proof must establish a sufficiently-large-M threshold, preferably certified numerically, rather than guess it from floating-point stability.

## 7. Remaining obligations

75-decimal one-step checks at t=0.1,0.05,0.025,0.0125,0.00625 corroborate the coefficients with errors decreasing quadratically in t. They are not interval certificates.

Still required: a forward-invariant region for every scaled variable; uniform fast/filter O(t^2) bounds; an effective rational-start threshold; an independent full-rotation audit; resolution of the original gamma=1 switching problem; and the general replacement, priority and journal gates. No grand closure is claimed.
