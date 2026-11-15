# Checkpoint 07 — exact normalized-map audit

2026-11-15. This resolves the specific leading-dependence gap recorded in Checkpoint 05, Section 6. The calculations below use exact arithmetic over Q(sqrt(3)), not eigensolver samples. The explicit quantitative entry threshold and the assembled counterexample theorem are to be recorded separately. No publication-priority or grand-completion claim is made here.

## 1. Blow-up coordinates

Put tau=t^2, s=sqrt(3), b0=s/3, H0=s/4, ell=3/4, N=9/16. Rename the phase coordinates xi,eta as x,y in this checkpoint. Use a bounded parameter B and normalized errors

    b=b0+tau B, H=H0+tau h,
    (C,G)=Psi(H,b)+tau(ec,eg),
    chi=ell y+tau echi,
    j=jstar(x,y)+tau ej,
    (Ca,Ga,Q)=psi_a(j,x,y)+tau(eac,eag,eq),
    Ad=t^5 ad, Bd=t^5 bd, fa=t^4 fa_error,
    fs=-1/2+tau fs0+tau^2 efs.

Here Psi, psi_a, jstar and fs0 are exactly those of Checkpoint 05. All symbols on the right are independent bounded coordinates when computing the map. B is controlled by the charge identity, not assumed to converge.

For the two slow normalized errors h and ej, the polynomials below denote (error_next-error)/tau. For every other normalized error they denote error_next itself. Their omitted terms are uniformly O(tau) on each fixed compact set. Equivalently the omitted terms in the slow updates are O(tau^2).

## 2. Exact leading dependency table

The dependency order required by Checkpoint 06 is confirmed:

    outputs ad,bd,fa_error: depend only on x,y;
    outputs (ec,eg): depend only on x,y,(ec,eg);
    h drift: depends only on x,y,B,h,(ec,eg);
    echi output: depends only on x,y,B,h;
    (eac,eag,eq): depend only on x,y,B,h,ec,eg,echi,
                 fa_error and (eac,eag,eq);
    ej drift: depends only on all preceding blocks and ej;
    efs output: depends only on x,y,B,h,ec,eg.

The self-matrices of the two fast pairs/triples are precisely Ms and Ma in Checkpoint 05. Both slow self-coefficients are -9sqrt(3)/8. Every auxiliary self-coefficient is zero. In particular NO later error enters an earlier displayed forcing. This is an exact algebraic statement around the entire phase circle.

Some explicit polynomials (fa below means the normalized fa_error):

    ad_next = fa_next
      =-261s x^2/64+81xy/32-27s y^2/64+O(tau),
    bd_next=-351x^2/64+117s xy/32-81y^2/64+O(tau),

    ec_next=2ec/3-2eg/3+O(tau),
    eg_next=(-2+s)ec/3+(1+s)eg/6+(-3+s)xy/4+O(tau),

    (h_next-h)/tau
      =27s B/32+(1/4-s/6)ec+(5/4-s/12)eg
        -9s h/8+(3-3s)xy/8+O(tau),

    echi_next=-3s By/4+s hy-116s x^3+259x^2y/4
                    -13s xy^2/2-3y^3/4+O(tau),

    efs_next=-27B/32+(-1+s)ec/4+(-1+s)eg/8
                        +27h/16+(-9+3s)xy/16+O(tau).

The asymmetric Ga equation includes the previously easy-to-miss term

    (-3+3sqrt(3)) fa_error/8.

It is harmless because the auxiliary reset is ordered first, but it must not be dropped.

The complete asymmetric and ej polynomials are retained in the exact-arithmetic output and runnable audit script; their dependency table above is enough for the invariant-box argument, while their diagonal terms and contraction matrices are essential.

The same exact calculation gives

    Delta A = (27sqrt(3)/256)t^3+O(t^5),
    Delta xi = (9/16)tau eta+O(tau^2),
    Delta eta = -(9/16)tau xi+O(tau^2),
    v66 =3xi^2 t^3+O(t^5),
    s66 =(29sqrt(3)xi^2-18xi eta+3sqrt(3)eta^2)t^3+O(t^5).

## 3. Why the formal coefficients are actual uniform Taylor coefficients

Use the weighted positive-space graph in Checkpoint 05,

    Xgraph=[[t^2 X,t Y],[t^2 Z,t W]],

with leading values (-9/16,-3/4,3xi,4xi). After division by t,1,t,t^2, the four Riccati equations are analytic in tau, all the normalized errors, B,xi,eta and the four graph variables. At tau=0 their Jacobian is triangular in two 2-by-2 blocks. Its relevant nonzero diagonal factors are b0,1+b0,1 and C0-1/4=1/8. The sole additional off-block derivative is -eta+sqrt(3)xi. Consequently it is nonsingular uniformly on every compact phase set.

The analytic implicit-function theorem supplies the unique graph branch and uniform Taylor remainders on fixed compact parameter sets. On a phase annulus the last Schur coefficient is

    -(S2-sqrt(3)eta^2),
    S2-sqrt(3)eta^2 >= xi^2+eta^2>0.

The positive restriction has Schur coefficient 1/8. Thus for sufficiently small positive tau this graph is the ACTUAL positive spectral space, not a selected formal invariant space. The second 3-by-3 block is handled by the first two graph equations.

The exact polynomial calculation solves the graph coefficients through tau^2 by the displayed invertible Jacobian, substitutes into

    Vplus=[I;Xgraph](R_PP+R_PQ Xgraph)
                   (I+Xgraph*Xgraph)^(-1)[I;Xgraph]*,

and forms the true DRS update. The first omitted graph terms affect the relevant output entries only two or more powers of t later than the coefficients used here. Every negative-power coefficient in the normalized output expansions cancels exactly. Hence the table consists of genuine Taylor identities with compact-uniform remainders.

## 4. Independent quantitative chart check

A separate exact rational majorant calculation verifies a uniform complex-analytic chart for

    |xi|,|eta|,|B|<=1,
    each normalized error <=10^20,
    |tau|<=10^-100.

In the infinity-norm graph ball of radius 10^-12 about the leading graph, it proves

    ||F_tau||_infinity < 10^8*10^20,
    ||F_(tau,U)||_infinity < 10^8*10^20,
    ||F_(U,U)||_infinity < 10^6.

The inverse leading Jacobian has infinity norm below 100. Therefore the fixed-Jacobian Newton map is a contraction of constant below 1/2 and its displacement at the center is less than half the graph-ball radius. The inequalities use rational arithmetic and |a+b sqrt(3)|<=|a|+2|b|; displayed decimal approximations are not premises. The second arrow block satisfies the same conservative bounds.

This quantitative check is for the analytic graph. The full forward-invariant tube additionally uses the charge, amplitude, and normalized error bounds. That assembly, including an explicit rational entry, is the next checkpoint.

## 5. Precise consequence of this audit

The supposed circularity in Checkpoint 05 can be removed: the leading normalized system is genuinely triangular in the order stated in Checkpoint 06. The general trapping lemma therefore applies once the compact charge and amplitude controls are included. This is stronger than a one-step numerical check or a pointwise expansion. It does not resolve the original gamma=1 orbit, whose spectral-sign switching is a different issue.
