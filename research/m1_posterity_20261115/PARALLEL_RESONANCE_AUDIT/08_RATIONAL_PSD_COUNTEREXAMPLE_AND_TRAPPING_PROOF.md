# Checkpoint 08 — a rational affine–PSD resonance counterexample

2026-11-15. This checkpoint assembles a proof from the exact identities, normalized polynomial audit, and uniform trapping argument. It concerns the balanced gamma=2 system, not the original gamma=1, epsilon=1/10 start. The historical-priority and publication-quality gates remain separate and uncompleted. The proof and the exceptionally conservative numerical entry threshold are exposed below for independent checking.

## 1. Exact rational data and theorem

Write Fij=Eij+Eji and use indices 0,...,6. In the Frobenius space S^7 let

    a=-(F01+F34)/2,
    L=span{E00+E33, E11-F02/2, E44-F35/2,
           E66+2(F02-F35), F06, E22-E55},
    U=a+L, K=S_+^7,
    T(Z)=Z+P_K(2P_U Z-Z)-P_U Z.

All displayed generators and affine data are rational. These definitions specify the equality system completely; equivalently impose the entry relations in Section 2. There is no change of metric or algorithm.

Put s=sqrt(3) and

    b0=s/3, H0=s/4, N=9/16,
    c0=27s/256, cB=27/256,
    cA=(4c0)^(1/4), Fstar=(2-s)/640,
    D=diag(1,0,b0,1,0,b0,0), V=cA D,
    rstar=N sqrt(Fstar)/cA^3.

For every integer M>=10^5000 use the following EXACT rational start. Set t=1/M,

    sM=floor(sqrt(3 M^8))/M^4,
    J=-29sM/30000, R=3/2500,
    Cf_a=2sM J+4R,
    Ca=Cf_a+3J/2, Ga=2R-Cf_a/2+3J/2, Q=R-12J.

The nonzero upper-triangular entries of Z0(M) are

    Z00=Z33=M, Z22=Z55=sM M/3,
    Z11=t(3/8+3sM/16)+t^3 Ca,
    Z44=t(3/8+3sM/16)-t^3 Ca,
    Z02=t*3(sM-1)/16+t^3 Ga,
    Z35=t*3(sM-1)/16-t^3 Ga,
    Z01=Z34=-1/2+t^2*9sM/64,
    Z12=sM/4+t^2 J, Z45=sM/4-t^2 J,
    Z06=t/50, Z66=t^3 Q.

All other entries, including Z16 and Z26, are zero; complete by symmetry. Thus M=10^5000 specifies one particular rational matrix, without an unspecified 'sufficiently large' parameter. This huge value is only a deliberately conservative analytic certificate, not a useful numerical starting scale.

### Theorem

The affine system is weakly infeasible, and its minimum-trace escape exponent is exactly alpha=1/3. Every orbit starting at Z0(M) as above has

    Z_k/k^(1/4) -> V,

and its scaled-step cluster set is exactly

    { V/4 + rstar[cos(theta) F06+sin(theta) F26] :
                                                   theta in R }.

In particular

    k^(3/4)||Z_(k+1)-Z_k||_F
       -> sqrt(||V||_F^2/16+2rstar^2) > ||V||_F/4.

Thus the proposed universal vector last-step law is false for an actual rational affine–PSD system under plain DRS. The Frobenius radius of the displayed circle is sqrt(2)rstar; rstar is the radius in the two entry coordinates (06,26).

For n_k=Z_k/||Z_k||_F and L_n=sum_(k<n)||n_(k+1)-n_k||_F,

    L_n/log n -> (2/3)sqrt(Fstar)>0.

Hence even the normalized states can have infinite spherical length while converging to a single cosmic direction. Zero-block embedding gives rational counterexamples in every matrix order at least seven.

## 2. Weak infeasibility and exact escape exponent

The affine entries can be parametrized by real A,c,d,r,u,z:

    X00=X33=A, X11=c, X44=d, X66=r,
    X02=-c/2+2r, X35=-d/2-2r,
    X22=z, X55=-z, X06=u,
    X01=X34=-1/2,

with all other entries zero. An exact PSD member would have X22=X55=0. Zero diagonal entries kill their rows, so c=4r and d=-4r. Nonnegativity of c,d,r forces all three to vanish. Then X11=0 kills X01, a contradiction.

For epsilon>0 take two identical PSD arrow blocks on (0,1,2) and (3,4,5):

    Y00=1/(2epsilon), Y11=epsilon, Y22=epsilon^3,
    Y01=-1/2, Y02=-epsilon/2, Y12=0,

and a zero seventh row/column. The leaf Schur sum is 1/(2epsilon), so the blocks are PSD. All affine equations except X22+X55=0 hold exactly; that residual is 2epsilon^3. The trace is 1/epsilon+2epsilon+2epsilon^3. This proves weak infeasibility and an upper trace bound O(delta^(-1/3)).

For a PSD residual-delta competitor, use the equations X22+X55=0, X34=-1/2, and X44+2X35+4X66=0. For small delta,

    0<=X55<=delta, |X34|>=1/4,
    d+4r<=2|X35|+delta<=2sqrt(B delta)+delta,

where B=X33. Thus

    1/16<=Bd<=2B^(3/2)sqrt(delta)+B delta.

This implies B>=c delta^(-1/3) for a fixed c>0. Norm equivalence handles any fixed Euclidean equality-residual norm. Therefore alpha=1/3 exactly. This argument does not use a dynamical conjecture.

## 3. Exact map and conserved-charge balance

The block pattern (0,1,2,6) plus (3,4,5) is invariant. Use the sixteen real state coordinates A,Ad,B,Bd,cs,ca,gs,ga,hs,ha,fs,fa,w,z,v,q of Checkpoint 05. The exact Frobenius projection is

    u00=u33=A, u22=Bd, u55=-Bd,
    caff=2(cs-gs)/3, r=(3q+8ca+16ga)/35,
    cafa=2(ca-ga+2r)/3, gafa=-cafa/2+2r,
    u11=caff+cafa, u44=caff-cafa,
    u02=-caff/2+gafa, u35=-caff/2-gafa,
    u66=r, u06=w, u01=u34=-1/2.

For R=2u-Z, vplus=R_+, sminus=(-R)_+, d=vplus-u, exactly

    vplus=u+d, sminus=Z-u+d, vplus sminus=0.

For W=(Z06,Z16,Z26), block complementarity gives

    ||W_next||^2-||W||^2=-||Delta W||^2-2vplus66 sminus66.    (3.1)

For Dcharge=diag(1,-1,-3,1,-1,-3,-1), put E=tr(Dcharge Z^2). Its congruence map X->Dcharge X+X Dcharge preserves L and annihilates a. Therefore

    E_next-E=-tr(Dcharge d^2), |Delta E|<=3||d||_F^2.          (3.2)

In state coordinates

    E=2(A^2-3B^2)+2Ad^2-6Bd^2-2cs^2-2ca^2
      -4gs^2-4ga^2-8hs^2-8ha^2-q^2-2v^2-4z^2.              (3.3)

Both identities are exact finite-difference identities. No asymptotic state remainder is differentiated.

## 4. Analytic coordinates, error boxes, and actual PSD branch

Set tau=t^2, t=1/A, and use the normalized coordinates of Checkpoint 07. Use |B_parameter|<=1 for B_parameter=(B/A-b0)/tau. The phase annulus and charge/amplitude windows are

    E in [-3,0], Fbar in [Fstar/2,3Fstar/2],
    Fstar/4 <= xi^2+eta^2 <= 3Fstar,
    Fbar=xi^2+eta^2+tau chi^2+tau P4(xi,eta),

where

    P4=18eta^4-120s eta^3xi+36eta^2xi^2
                         -(568s/3)eta xi^3-30xi^4.

Choose the following normalized error bounds, in this order:

    |ad|,|bd|,|fa_error| <=1000;
    sqrt(ec^2+2eg^2)<=2000;
    |h|<=10^5;
    |echi|<=10^6;
    sqrt(2eac^2+4eag^2+eq^2)<=10^11;
    |ej|<=10^13;
    |efs|<=10^6.

The exact leading dependency table in Checkpoint 07 is triangular in precisely this order. Ms and Ma have weighted norms less than 999/1000. Both slow diagonal coefficients are -kappa=-9s/8; all auxiliary diagonal coefficients vanish. Exact rational majorants for the leading forcings, respectively, are less than

    14; 1; 2291; 173485; 19224711; 112803274227; 169301.

For the auxiliary group each coordinate is covered by 14. For the symmetric and asymmetric groups these are bounds in their displayed weighted norms. These numbers give strict inward margins in every chosen box; the smallest fast margin exceeds 1/2. The matrix norm bounds follow by Sylvester's criterion for q^2 W-M*WM with q=999/1000, W=diag(1,2) or diag(2,4,1), using exact arithmetic in Q(sqrt(3)).

For the first matrix block the positive spectral space is written as the graph

    Xgraph=[[t^2 X,t Y],[t^2 Z,t W]],

with leading values (-N,-ell,3xi,4xi), ell=3/4. The weighted Riccati equations have a nonsingular leading Jacobian and hence an analytic branch. Their last Schur coefficient is

    -[S2-s eta^2],
    S2=29s xi^2+3s eta^2-18xi eta.

Exactly S2-s eta^2>=xi^2+eta^2, because the 2-by-2 matrix obtained after subtracting the identity has positive diagonal and determinant 94-31sqrt(3)>0. The positive restriction has Schur coefficient 1/8. Thus on the annulus, for sufficiently small t, this analytic branch is the actual PSD positive part. The second arrow block has two positive eigenvalues and one negative eigenvalue.

## 5. Quantitative remainder bound and explicit onset

Here are conservative constants sufficient to make the previous 'sufficiently small' effective. On the complex tau disk |tau|<=r=10^-100, allow |xi|,|eta|,|B_parameter|<=1 and every normalized error at most 10^20. The graph variables lie in the infinity-norm ball of radius 10^-12 about their leading values.

The exact rational majorant certificate gives

    ||F_tau||<10^28, ||F_(tau,U)||<10^28, ||F_(U,U)||<10^6.

The inverse leading graph Jacobian has infinity norm below 100: solving its four triangular equations bounds the four components by 2,2,31,60 times the right-hand infinity norm. Therefore the fixed-Jacobian Newton map is a contraction below 1/2 on that graph ball, and its center displacement is below half the ball radius. This supplies a unique complex-analytic graph uniformly in all real parameters in the box. The second block satisfies the same bounds.

For clarity, the crude Cauchy estimates used after this chart are also made explicit. The primitive scaled state coefficients have modulus below 10^4; the scaled entries of the reconstructed positive part have modulus below 10^8. The Gram determinant of [I;Xgraph] is within 10^6 r of 1. The updated scaled top diagonal is within 10^12 r of 1, and the updated b-ratio remains of modulus greater than 1/4. Thus the inverses in the coordinate reconstruction are bounded. After clearing at most six powers of tau, the numerators of all normalized updates, charge and amplitude quotients, and scaled Schur coefficients have modulus below 10^100. This follows directly from the formulas for Vplus and the coordinate definitions: normalized errors require at most three inverse powers, and the charge quotient requires at most four; six is an overestimate. Degrees in the bounded phase variables are at most four in these reconstructions.

The exact coefficient cancellations in Checkpoint 07 remove the apparent poles. Cauchy's estimate on the disk r bounds their Taylor remainders on |tau|<=r/2 by 10^1000 times the required next power of tau. Squaring the step bound in (3.2), and enlarging for all components and norms, is covered by the single common constant

    C=10^3000.

In particular all recurrence and Schur remainder estimates below hold with this C for

    0<tau<=tau0=10^-10000.

Since C tau0=10^-7000, it is smaller than every error-box inward margin, the phase-annulus margin, and the positive/negative Schur margins. This is why M>=10^5000 is sufficient; no floating-point experiment selects the threshold.

## 6. Closing the no-first-exit argument

The exact normalized map now gives, uniformly in the tube,

    tau_next=tau-2c0 tau^3+O(tau^4),
    Delta E=O(tau^3),
    Delta xi=N tau eta+O(tau^2),
    Delta eta=-N tau xi+O(tau^2),
    vplus66=3xi^2 t^3+O(t^5),
    sminus66=S2 t^3+O(t^5).

Every step component is O(t^3). The exact cut identity and the polynomial identity

    N(eta partial_xi-xi partial_eta)P4
      =6xi^2 S2-(135s/2)(xi^2+eta^2)^2

give

    Fbar_next-Fbar=tau^2[a0 Fbar-B0 Fbar^2]+O(tau^3),
    a0=27(2s-3)/256>0, B0=135s/2, a0/B0=Fstar.          (6.1)

The mixed-speed triangular trapping lemma in Checkpoint 06 applies to the error blocks with the explicit bounds of Section 4. Its proof is a finite no-first-exit induction, not an assumption of infinite-time tracking. The charge cannot exit: tau-tau_next>=c0 tau^3, so its total change on every finite segment is at most (C/c0)tau_initial, far smaller than the initial margin. The amplitude cannot exit because (6.1) is strictly inward on protective bands adjacent to both endpoints; one-step changes are much smaller than the band widths.

The two redundant compact controls also cannot exit. The exact charge formula gives

    E=-4sqrt(3) B_parameter-3/2+O(tau).

Moreover B_parameter,next=B_parameter+O(tau^2). Hence a putative first exit past |B_parameter|=1 would still have |B_parameter,next|<=2, where the displayed charge formula and E in [-3,0] instead force |B_parameter,next|<1/2. Likewise

    Fbar=xi^2+eta^2+O(tau)

and the phase increments are O(tau); the amplitude window rules out a first exit from the larger phase annulus. The spectral Schur margins therefore persist as well. This completes the uniform nonlinear trapping proof.

## 7. Rational entry really lies in the tube

For the start of Section 1,

    0<=sqrt(3)-sM<t^4=tau^2.

The symmetric fast errors are EXACTLY zero, since H=sM/4 and b=sM/3 give H/b=3/4 and the displayed Psi values. All other normalized errors are O(tau), with elementary absolute constants below 10^5; the auxiliary errors and echi are zero. B_parameter=O(tau),

    E=-3/2+O(tau),
    Fbar=1/2500-30tau/50^4.

The leading amplitude 1/2500 is strictly inside the chosen window. At tau<=10^-10000 all the stated bounds and strict initial charge margins follow directly. Thus the explicit rational family enters the tube, and Section 6 applies forever.

## 8. Exact asymptotics and persistent phase

The scalar recursion gives

    tau_k^(-2)/k ->4c0,
    t_k^(-4)/k ->4c0,
    sum tau_k^2=infinity, sum tau_k^3<infinity.

The scalar inward-drift argument gives Fbar_k->Fstar. Since Fbar-(xi^2+eta^2)=O(tau), the phase radius tends to sqrt(Fstar)>0. Its unwrapped angle has increment

    -N tau_k+O(tau_k^2).

These increments tend to zero and have divergent negative sum. First crossings of prescribed angles modulo 2pi give every angular cluster direction. The coordinate bounds yield the state limit Z_k/k^(1/4)->cA D directly.

For the full step, all normalized fast errors change by O(tau) on a tail. To prove this without differentiating an orbit remainder, start with the auxiliary resets, then track each constant strictly contractive matrix toward its slowly changing frozen fixed point. The forcing changes by O(tau); multiplication by tau_next^(-1), with tau_next/tau=1+O(tau^2), gives an O(tau) tracking error. The slow h and ej updates already change by O(tau). Induction over the dependency table proves the assertion for every block. Also B_parameter changes by O(tau^2).

Substitute these finite-difference bounds into the state coordinates. All step entries except the four growing diagonal entries and the 06,26 entries are o(t^3). Explicitly,

    d_k=t_k^3[c0 D+N(eta_k F06-xi_k F26)]+o(t_k^3).       (8.1)

This proves the entire circle of cluster vectors and the exact norm limit in Section 1. In particular it proves a positive transverse limsup for this exact rational SDP, not merely for a linearization.

## 9. Infinite spherical length and additional sharp consequences

Radial normalization has differential equal to the tangent projection divided by the radius. In (8.1) the tangent projection kills c0 D and preserves the off-diagonal circle. Consequently

    ||n_(k+1)-n_k||_F
       ~ [sqrt(2)N sqrt(Fstar)/||D||_F] t_k^4
       ~ (2/3)sqrt(Fstar)/k.

The quadratic normalization remainder is smaller. Summation gives the exact logarithmic spherical-length limit.

The accumulated travel has the exact inefficiency factor

    sum_(j<k)||d_j||_F / ||Z_k-Z_0||_F
       -> sqrt(1+(64/9)Fstar)>1.

The leading primal and normal state components are

    H=cA(E00+E33), G=cA b0(E22+E55).

Thus the actual normal residual has an oscillating leading norm: its scaled cluster vectors are G/4-rstar sin(theta)F26, whereas the affine tangential component contains the F06 oscillation. This explicitly demonstrates failure of asymptotic saturation of the minimum-residual profile, despite the correct common leading state and primal-dual balance.

Zero-block embedding preserves all calculations in higher matrix orders. These consequences show that the obstruction is dynamical spectral transport, not a defect in state cosmic convergence.

## 10. Scope ledger

This is a negative resolution of the universally quantified plain affine–PSD last-step assertion, through the gamma=2 rational family. It does NOT prove the fate of the older gamma=1, epsilon=1/10 numerical orbit. It also does not by itself finish the requested all-cone replacement, historical novelty verification, manuscript, or published-paper comparison. Those remain separately identified obligations. No 80% editorial-acceptance claim is made.
