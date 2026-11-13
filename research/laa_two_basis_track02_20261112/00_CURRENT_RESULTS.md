# Current results — optimal conic lifts, uniform geometry and SDP universality

Date: 2026-11-13.
Repository: Harman6139/Posterity-Files.
Branch: laa-track02-gptpro-analytic-frontier-20261112.

This index records the continuation through milestone 16. MASTER_INDEX.md preserves the earlier trace-controlled normal forms through 09. Every theorem below has a full mathematical proof in the identified manuscript; finite numerical examples are not premises. The new results in 13–16 are analytic and are not claims that a particular named classical conjecture has been settled or that historical priority has been exhaustively established.

## 1. Exact optimal PSD and SOC lifts in fixed target dimension

**15_ESCAPE_LOWER_BOUNDS_AND_OPTIMAL_POWER_CONE_LIFTS.md**
Proof commit: c2c42bb6a7c7cdcfc08abe10fef870ba36ef9ce5.

For every k>=1 put q=2^k and

    P_k={(x,t,z):x,t>=0, x^(q-1)t>=|z|^q},
    S_k={(x,t):x>0,t>=x^(-(q-1))}.

The minimum single PSD matrix order for either set is EXACTLY k+1, for real symmetric OR complex Hermitian lifts. The minimum number of Lorentz-cone factors in ANY SOC representation is EXACTLY k, even when the Lorentz dimensions are unrestricted and arbitrarily many linear inequalities and auxiliary variables are allowed.

More generally, a lift using PSD orders d_j, h nonpolyhedral Lorentz factors and any number of scalar/polyhedral factors must satisfy

    sum_j(d_j-1)+h>=k.

The lower bound is intrinsic, not restricted to the proposed construction, positive decoders, unique lifts, rational coefficients, or simple/mediated-graph SOC formulations.

The explicit upper lift is just one Y>=0 of order k+1 with

    Y_ii=Y_(0,i+1) for 1<=i<=k-1,
    (x,t,z)=(Y_00,Y_kk,Y_01).

All unspecified entries are free. Every target point has a rank-at-most-two PSD witness, but soundness holds against the FULL unrestricted PSD cone. For k>=2 the target cone is not a spectrahedron in its original three coordinates at any direct LMI order; the proof is an elementary determinant real-root obstruction. The projected representation nevertheless has the exact finite order above.

The lower-bound principle is general: if eta-optimal points of a convex target must have norm at least c eta^(-a), then EVERY mixed-cone lift must have resource B>=ceil(log_2(1+a)). The same argument in the other coordinate gives the bound ceil(log_2(1+max(a,1/a))) for the inverse-power epigraph t>=x^(-a).

The manuscript proves the required product-cone escape estimate, including arbitrary-dimensional Lorentz cones. A partial PSD-face or Lorentz-boundary reduction changes the growth exponent by e->2e+1. Entire/polyhedral reductions do not. Thus the exponent is at most 2^B-1 for B=sum(d_j-1)+h. This is why arbitrarily many linear constraints cannot circumvent the lower bound.

The number/order results are NOT semidefinite extension DEGREE lower bounds: extension degree allows arbitrarily many small PSD blocks, and these planar sets have extension degree two. Related established representation work by Wang, Blanco–Martinez-Anton and Scheiderer is explicitly cited in 15. No exact classification for all rational power weights is claimed.

## 2. Universal mixed SDP/SOCP/LP escape and regularization laws

**16_MIXED_CONE_ESCAPE_AND_REGULARIZATION_UNIVERSAL_LAW.md**
Proof commit: 42f1adddb0fa5ee490c22acfa77e107b307bb0fd.

For a product of real/complex PSD cones, arbitrary-dimensional Lorentz cones and arbitrarily many nonnegative scalar cones, put

    B=sum_j(d_j-1)+number of nonpolyhedral Lorentz factors,
    E_B=2^B-1.

Every weakly infeasible system has minimum-size escape exponent a in the SHARP interval [1/E_B,E_B]. Its normalized approximate Farkas-certificate exponent is 1/a, with the exact general-cone functional duality and leading-constant relation from 12. The product-cone upper bound in 15 and the same bound applied to the normalized dual prove both sides.

For any nonempty feasible optimization problem with finite UNATTAINED optimum v, use the resource B_F of its actual minimum feasible face. The minimum gauge of an exactly feasible eta-optimal point has

    T(eta)~p0 eta^(-a),  a in [1/(2^B_F-1),2^B_F-1].

Every minimizer of the gauge-regularized objective l(X)-v+lambda tau(X) has

    objective gap ~(a p0 lambda)^(1/(a+1)),
    gauge ~p0(a p0 lambda)^(-a/(a+1)),
    regularized value ~[(a+1)/a](a p0 lambda)^(1/(a+1)).

Thus the value exponent lies in [2^(-B_F),1-2^(-B_F)]. Both endpoints are attained by bounded-coefficient rational SOCPs. The number of variables, Lorentz dimensions and linear inequalities do not affect these exponent limits.

In particular ANY finite unattained optimum with only ONE nonpolyhedral Lorentz factor has exact square-root linear-gauge regularization and reciprocal-linear near-optimal escape. Squared-norm regularization has exact cube-root value/cost-gap rate. These are global-minimizer asymptotics, not convergence rates for a particular numerical algorithm.

An attained optimum instead has regularized gap lambda times the minimum gauge of an optimizer plus o(lambda). All constants and validity thresholds remain instance dependent. These asymptotic statements do not constitute finite-precision decision algorithms.

## 3. Sharp nonattainment laws for ordinary SDPs

**14_SHARP_NONATTAINMENT_AND_REGULARIZATION_PHASE_LAWS.md**
Proof commit: e9f76e9a21676dd93f7a890825ee3f22bf4af45c.

For every feasible finite-value SDP with maximum feasible rank r and unattained infimum, its exactly feasible near-optimal trace profile has exponent in

    [1/(2^(r-1)-1), 2^(r-1)-1].

It proves exact all-minimizer leading asymptotics under trace regularization, both sharp rational endpoint families, positive-definite weighted traces, norm-power regularization, and an attainment/nonattainment dichotomy. It makes no zero-duality-gap assumption.

The load-bearing step is an explicit equality correction followed by O(delta) mixing with a relative-interior feasible point on the ACTUAL minimum face. It converts approximate feasibility of the augmented optimal-value system into exact feasibility without multiplying a huge witness trace by a bad factor. This justifies use of weak-infeasibility escape to analyze exact feasible near-optimization.

The two-basis one-scale normal form from 11 preserves the ENTIRE regularization value function exactly after the known lifted trace normalization, not merely its exponent.

## 4. Uniform image geometry from finitely many fixed escape directions

**13_UNIFORM_IMAGE_GEOMETRY_AND_FINITE_ESCAPE_RESERVOIR.md**
Proof commit: 1c1255ae997248f14342fbbeafb90cbee867bd7a.

For C=A(S_+^m), K=closure C and W=K intersect (-K), all divergent lifting behavior is controlled by the finitely many signed vectors of ANY orthonormal basis of W. Every bounded datum in K decomposes into a uniformly bounded PSD lift plus a bounded vector in W.

The image is closed iff each signed basis datum is exactly feasible, iff the unit cap of K admits uniformly bounded exact PSD lifts. The best such trace-lifting constant equals EXACTLY the global Lipschitz constant of the homogeneous dual LMI error bound

    dist(y,{z:A*z>=0}) <= kappa max(0,-lambda_min(A*y)).

For the uniform capped-image distance H_A(R) and homogeneous dual error profile h_A(epsilon), the exact identity is

    H_A(R)=max_{||y||<=1}[dist(y,D)-R nu(y)]
          =max_epsilon[h_A(epsilon)-R epsilon].

If the image is nonclosed, the uniform lift exponent a lies in [1,2^(m-1)-1], is attained by a SINGLE FIXED signed lineality datum, and is related to the dual error exponent theta by

    theta=1/(a+1) in [2^(-(m-1)),1/2].

Both endpoints are sharp. The theorem proves, in particular, that every nonclosed PSD image has some fixed weakly infeasible datum with at least reciprocal-linear trace growth. Slow pointwise escape from 12 therefore cannot be the uniform worst case.

Qualitative closedness criteria have established antecedents; 13 does not claim that closedness itself was an unsolved problem. No efficient maximum-rank-face discovery or uniformly conditioned selector is asserted.

## 5. Foundation: exact general-cone escape-profile duality

**12_RECIPROCAL_ESCAPE_LAW_AND_SHARP_DIMENSIONAL_BOUNDS.md**
Proof commit: 2e2f8f75c99f49e4b6e51fad2a37b41891928901.

For a closed proper convex cone K, e in int K*, and weakly infeasible b for A(K), define

    R_b(delta)=min{<e,x>:x in K,||Ax-b||<=delta},
    d_b(R)=min{||Ax-b||:x in K,<e,x><=R},
    Q_b(epsilon)=min{||y||:b.y=-1,A*y+epsilon e in K*}.

The exact functional identity is

    d_b(R)=sup_(0<epsilon<1/R)(1-R epsilon)/Q_b(epsilon).

For semialgebraic K, if R_b(delta)~p0 delta^(-a) and Q_b(epsilon)~q0 epsilon^(-beta), then

    a beta=1,
    p0^beta q0=beta^beta/(beta+1)^(beta+1).

For order-m PSD systems the sharp pointwise escape exponent envelope is [1/E_m,E_m], E_m=2^(m-1)-1. Both endpoints occur in explicit bounded-coefficient rational systems. The proof quantifies a classical hyper-feasible partition by a Schur recurrence and applies it to the normalized Farkas-dual affine system for the reverse envelope.

## 6. Foundation: all-rational, fully unrestricted two-basis normal form

**10_ALL_RATIONAL_TWO_BASIS_COMPILER.md**
Proof commit: 31d40a5bf1100545564830bd70dc069ed4f118c8.

The two bases, encoder/decoder coefficients, targets and rational objective pullbacks can all be rational. The rational Cayley frame

    G=[(I-Q)(I+Q)^(-1),2(I+Q)^(-1)B], Q=BB^T,

is combined with a block-respecting positive congruence of the source lift. It retains exact source extraction without square-root gates, eigenvectors or an algebraic sign oracle. The minimal rational construction is a reflection pair; all-nonzero/nonreflection/positive-zero-data features belong to the separate construction in 08.

**11_OPTIMAL_ONE_SCALE_UNRESTRICTED_UNIVERSALITY.md**
Proof commit: cd97bc32a1febc3f37ad3803c7cd582d140cf04d.

For EVERY rational A:S^m->R^p, without trace control or a supplied certificate, construct in polynomial bit time two rational real bases of order

    N=9m^2+4m+5+2p

and completely positive E,D with

    D({Y>=0:exists t, B_U(Y)=Wb+t v})
      ={X>=0:A(X)=b}

for every datum b. The vector v is strictly positive. Exact lifts have t=trY/c=trD(Y), with 1<=c<=10m^5. Centered forward source residuals are isometric; reverse residuals have an explicit polynomial all-PSD bound.

The reduction preserves feasible/weakly infeasible/strongly infeasible data, primal and dual objective values and finite attainment, unboundedness, recession cones and escape exponents. It also preserves exact-feasible regularization value functions after trace normalization. Ancillary amplification is block-valued at higher matrix levels. The normalized encoder admits heralded exact quantum recovery, not deterministic trace-preserving recovery.

Two bases and one free scale are necessary and sufficient in the specified datum-uniform positive-decoder model. Fixed diagonal data always give compact PSD fibres and a closed measurement cone; one basis would force a full PSD-cone singleton decoder through a finitely generated cone. No matching lower bound for the quadratic TWO-BASIS matrix order is claimed by these discrete-resource statements or by the power-cone results in 15.

This is a polynomial-time normal-form REDUCTION, not a polynomial-time exact feasibility DECISION algorithm.

## 7. Prior history, code and scope

The unrestricted_rational/ directory retains the exact SymPy constructor, symbolic endpoint examples, recorded outputs and reproduction instructions for 10–12. Earlier source code and results for 01–09 remain in this directory and strengthening_audit/. All original numbered historical milestones and corrections are inherited on this branch.

The mathematical proofs for all dimensions and ranks are in the manuscripts. No historical scripts were rerun merely to justify a new theorem. The latest 13–16 conclusions are proved analytically; finite tests are not substitutes for their arguments.

Related primary literature, precise representation models and limits are stated in each new manuscript. External priority and independent referee certification are not claimed. In particular this index does not assert resolution of the general exact-SDP complexity question, all rational power-cone minimum sizes, or a generalist journal's acceptance decision.
