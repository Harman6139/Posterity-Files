# Current results — general SDP extension complexity, optimal conic lifts and universality

Date: 2026-11-13.
Repository: Harman6139/Posterity-Files.
Branch: laa-track02-gptpro-analytic-frontier-20261112.

This index records the continuation through milestone 19. MASTER_INDEX.md preserves the earlier trace-controlled normal forms through 09. The full earlier index through 16 remains at commit a4318f6ca7561b4b9018bd495eba140a9c29f76e. Every mathematical statement below has its proof in the named manuscript; finite numerical examples are not premises.

## 0. General extension complexity: exact criteria, finite certificates and compact applications

The general existence/size framework is the CLASSICAL slack-factorization theorem of Gouveia–Parrilo–Thomas. PSD-factor rescaling, finite-matrix lower semicontinuity and block-diagonal additivity also have established antecedents. The continuation does NOT claim to have newly solved the general lift-classification problem, computed every convex body's minimum order in closed form, or turned the scalar escape invariant into a complete invariant.

### 17_GENERAL_EXTENSION_COMPLEXITY_FINITE_SLACK_AND_SOS.md
Proof commit: c819a21a3aadea6f94ba282a003ffa3f99d91d51.

For any nonempty closed convex C, in the ordinary LMI-with-free-variables convention, use all tight nonnegative affine functions f with inf_C f=0. Normalize their slacks by

    S_C(x,f)=f(x)/[(1+||x||_1)(|a_f|+||b_f||_infinity)].

Then

    sxc(C)=sup_{finite I,J} rank_psd(S_C[I,J]).

For a convex body with zero in its interior the usual table 1-x.y on C times C^polar suffices. The manuscript proves a normalization independent of sample count: a table bounded by M admits order-d factors with tr P_i<=1,tr Q_j<=dM. Compactness glues all finite factorizations; finite-dimensional span turns the resulting infinite slack equations into a finite affine lift. Singular faces, unbounded sets and unattained supporting infima are handled explicitly. The same statement characterizes every fixed finite PSD block-size tuple.

Every failed finite proposed-order test admits a finite SOS certificate. On Gram-factor balls define

    L_S=sum_ij(S_ij-||U_i^T V_j||_F^2)^2.

Failure at order d is equivalent to a strictly positive compact minimum. Putinar/Lasserre give a finite SOS lower certificate; Powers' rational theorem makes the certificate rational for rational S after adding the explicit redundant integer-radius ball. Thus nested samples and increasing SOS degrees eventually detect EVERY true fixed-order lower bound. No polynomial sample/degree/runtime bound or finite stopping criterion for all orders simultaneously is asserted.

For rational semialgebraic input, a separately displayed first-order real formula decides existence at any SPECIFIED order d and implies existence of real-algebraic coefficients when a lift exists. This direct quantifier-elimination consequence is acknowledged as such, not advertised as a new efficient algorithm.

Standard sxc counts scalar inequalities when they occupy the conic block. The earlier curvature resource sum(d_j-1)+h, with arbitrarily many scalar inequalities free, is NOT sxc. A simplex explains why escape alone cannot characterize standard complexity.

### 18_ROBUST_FINITE_WITNESSES_AND_HAUSDORFF_CHARACTERIZATION.md
Proof commit: 58be1a7fbc579f410d1a00be466efeb1212f9d9c.

For finite primal/polar samples, the PSD rank of their slack table equals the smallest order of a convex body sandwiched between the inner sample polytope and the outer sample polytope. The proof includes compactness of the constructed intermediate lift. Sample nets give the explicit Hausdorff error max(epsilon_x,2R^2 epsilon_y).

If d<sxc(C), a finite table with no order-d factorization gives a positive Hausdorff separation from EVERY order-d body, allowing completely arbitrary competing coefficients and singular auxiliary fibres. A bounded-factor minimum Delta yields

    d_H(C,K)>=min(r/2, r^2 Delta/(r+R))

when rB subset C subset RB and sxc(K)<=d. A finite SOS loss certificate gives a corresponding explicit bound using sqrt(gamma/(number of entries)).

Hence sxc is lower semicontinuous under Hausdorff convergence to a full-dimensional body, and the smallest FIXED order permitting arbitrarily accurate approximation equals the exact order. Each fixed d has a positive approximation floor when C has no finite lift. These are exact consequences of the slack/compactness framework, not claims of polynomial gap bounds. They do not apply to curvature resource with unlimited free linear inequalities.

### 19_COMPACT_PROJECTIVE_OBSTRUCTIONS_AND_ADDITIVE_OPTIMAL_LIFTS.md
Proof commit: 23d1be827644bbb98b853b18db742aed02432e76.

A non-singleton compact convex body's homogeneous cone has a lift of the SAME matrix order and no additional cone factors. The proof shows why the homogenizing scale is automatically nonnegative; it does not silently add a scalar inequality. Thus the escape obstruction can be applied to arbitrary affine sections of that cone to lower-bound the original compact body's complexity.

For q=2^k the compact planar body

    C_k={(x,z):0<=x<=1, |z|^q<=x^(q-1)(1-x)}

has minimum single real OR complex PSD order exactly k+1, minimum number of Lorentz factors exactly k, and minimum mixed curvature resource k. Its rational upper lift has Y>=0 of order k+1, Y_ii=Y_(0,i+1), and Y_00+Y_kk=1. Every point has a rank-at-most-two witness; soundness is unrestricted-rank. For k>=2 no direct LMI in the two original coordinates represents C_k at any order.

PSD order is additive for products of proper cones, by the classical block-diagonal slack argument. The manuscript also proves additivity of the mixed curvature resource and of SOC-factor count when scalar inequalities are free: PSD support splitting and the zero/ray/full-face alternatives in a Lorentz factor allocate nonlinear resources to the independent components.

For the convex JOIN of C_(k_1),...,C_(k_s), the exact minimum single PSD order is sum_i(k_i+1), and the exact SOC count and mixed resource are sum_i k_i. A join is NOT a Cartesian product of bodies; no unsupported Cartesian-product additivity is claimed. These compact examples have positive fixed-order Hausdorff approximation gaps by 18.

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

The explicit upper lift is one Y>=0 of order k+1 with

    Y_ii=Y_(0,i+1) for 1<=i<=k-1,
    (x,t,z)=(Y_00,Y_kk,Y_01).

All unspecified entries are free. Every target point has a rank-at-most-two PSD witness, but soundness holds against the FULL unrestricted PSD cone. For k>=2 the target cone is not a spectrahedron in its original three coordinates at any direct LMI order; the proof is a determinant real-root obstruction.

If eta-optimal points of a convex target must have norm at least c eta^(-a), EVERY mixed-cone lift must have resource B>=ceil(log_2(1+a)). The same argument in the other coordinate gives ceil(log_2(1+max(a,1/a))) for t>=x^(-a).

The product-cone escape proof includes arbitrary-dimensional Lorentz cones. A partial PSD-face or Lorentz-boundary reduction changes the exponent by e->2e+1. Entire/polyhedral reductions do not. Thus the exponent is at most 2^B-1.

These are NOT semidefinite extension DEGREE lower bounds: extension degree allows arbitrarily many small PSD blocks, and these planar sets have extension degree two. Related established representation work by Wang, Blanco–Martinez-Anton and Scheiderer is cited in 15. No exact classification for all rational power weights is claimed.

## 2. Universal mixed SDP/SOCP/LP escape and regularization laws

**16_MIXED_CONE_ESCAPE_AND_REGULARIZATION_UNIVERSAL_LAW.md**
Proof commit: 42f1adddb0fa5ee490c22acfa77e107b307bb0fd.

For a product of real/complex PSD cones, arbitrary-dimensional Lorentz cones and nonnegative scalar cones, put

    B=sum_j(d_j-1)+number of nonpolyhedral Lorentz factors,
    E_B=2^B-1.

Every weakly infeasible system has minimum-size escape exponent a in the SHARP interval [1/E_B,E_B]. Its normalized approximate Farkas-certificate exponent is 1/a, with the exact functional duality and leading-constant relation from 12. The product upper bound and the same bound applied to the normalized dual prove both sides.

For any nonempty feasible optimization problem with finite UNATTAINED optimum v, use the resource B_F of its minimum feasible face. Its exactly feasible near-optimal profile has

    T(eta)~p0 eta^(-a), a in [1/(2^B_F-1),2^B_F-1].

Every minimizer of l(X)-v+lambda tau(X) has

    objective gap ~(a p0 lambda)^(1/(a+1)),
    gauge ~p0(a p0 lambda)^(-a/(a+1)),
    value ~[(a+1)/a](a p0 lambda)^(1/(a+1)).

The value exponent lies in [2^(-B_F),1-2^(-B_F)], with both endpoints attained by rational SOCPs. The number of variables, Lorentz dimensions and scalar inequalities do not change the exponent limits. ONE nonpolyhedral Lorentz factor forces square-root linear-gauge regularization; squared-norm regularization has cube-root value/cost-gap rate.

An attained optimum instead has value lambda times the minimum optimizer gauge plus o(lambda). All constants and thresholds remain instance dependent; these asymptotic statements are not finite-precision decision algorithms.

## 3. Sharp nonattainment laws for ordinary SDPs

**14_SHARP_NONATTAINMENT_AND_REGULARIZATION_PHASE_LAWS.md**
Proof commit: e9f76e9a21676dd93f7a890825ee3f22bf4af45c.

For every feasible finite-value SDP with maximum feasible rank r and unattained infimum, its exactly feasible near-optimal trace exponent lies in [1/(2^(r-1)-1),2^(r-1)-1]. The theorem gives all-minimizer leading trace-regularization asymptotics, sharp rational endpoint families, weighted traces, norm powers, and an attainment/nonattainment dichotomy without a zero-duality-gap assumption.

An equality correction followed by O(delta) mixing with a relative-interior point on the ACTUAL minimum face converts approximate augmented feasibility into exact source feasibility without multiplying a huge witness trace by a bad factor. The one-scale normal form in 11 preserves the ENTIRE regularization value function after trace normalization.

## 4. Uniform image geometry from finitely many escape directions

**13_UNIFORM_IMAGE_GEOMETRY_AND_FINITE_ESCAPE_RESERVOIR.md**
Proof commit: 1c1255ae997248f14342fbbeafb90cbee867bd7a.

For C=A(S_+^m), K=closure C and W=K intersect (-K), all divergent lifting is controlled by the signed vectors of any orthonormal basis of W. Every bounded datum in K is a uniformly bounded PSD lift plus a bounded vector in W.

The image is closed iff each signed basis datum is feasible, iff the unit cap of K admits uniformly bounded exact lifts. The best trace-lifting constant equals the global Lipschitz constant of

    dist(y,{z:A*z>=0})<=kappa max(0,-lambda_min(A*y)).

The exact capped-image/support duality is

    H_A(R)=max_{||y||<=1}[dist(y,D)-R nu(y)]
          =max_epsilon[h_A(epsilon)-R epsilon].

For a nonclosed image, the uniform lift exponent a belongs to [1,2^(m-1)-1], is attained at a SINGLE FIXED signed lineality datum, and theta=1/(a+1) is the homogeneous dual error exponent. Both endpoints are sharp. Slow pointwise escape from 12 cannot be the uniform worst case.

Qualitative closedness criteria have established antecedents. No efficient face-discovery or uniformly conditioned selector is asserted.

## 5. Foundation: exact general-cone escape-profile duality

**12_RECIPROCAL_ESCAPE_LAW_AND_SHARP_DIMENSIONAL_BOUNDS.md**
Proof commit: 2e2f8f75c99f49e4b6e51fad2a37b41891928901.

For a closed proper convex cone K, e in int K*, and weakly infeasible b, define primal minimum size R_b(delta), capped residual d_b(R), and normalized approximate Farkas profile

    Q_b(epsilon)=min{||y||:b.y=-1,A*y+epsilon e in K*}.

Then

    d_b(R)=sup_(0<epsilon<1/R)(1-R epsilon)/Q_b(epsilon).

For semialgebraic K, R_b(delta)~p0 delta^(-a) and Q_b(epsilon)~q0 epsilon^(-beta) imply

    a beta=1,
    p0^beta q0=beta^beta/(beta+1)^(beta+1).

For order-m PSD systems the sharp pointwise exponent envelope is [1/E_m,E_m], E_m=2^(m-1)-1. Both endpoints occur in bounded-coefficient rational systems. The proof quantifies a classical hyper-feasible partition and applies it to the normalized dual for the reverse envelope.

## 6. Foundation: all-rational unrestricted two-basis normal form

**10_ALL_RATIONAL_TWO_BASIS_COMPILER.md**
Proof commit: 31d40a5bf1100545564830bd70dc069ed4f118c8.

The bases, encoder/decoder coefficients, targets and rational objective pullbacks can all be rational. The Cayley frame

    G=[(I-Q)(I+Q)^(-1),2(I+Q)^(-1)B], Q=BB^T,

with a block-respecting source congruence preserves exact extraction without radicals or an algebraic sign oracle. This minimal rational construction is a reflection pair; the all-nonzero/nonreflection/positive-zero-data features belong to the separate construction in 08.

**11_OPTIMAL_ONE_SCALE_UNRESTRICTED_UNIVERSALITY.md**
Proof commit: cd97bc32a1febc3f37ad3803c7cd582d140cf04d.

For EVERY rational A:S^m->R^p, without trace control or a supplied certificate, construct in polynomial bit time rational real bases of order N=9m^2+4m+5+2p and completely positive E,D with

    D({Y>=0:exists t, B_U(Y)=Wb+t v})
      ={X>=0:A(X)=b}

for every b. The vector v is positive and exact lifts have t=trY/c=trD(Y), with 1<=c<=10m^5. Centered forward residuals are isometric; reverse residuals have a polynomial all-PSD bound.

Feasible/weakly infeasible/strongly infeasible data, primal and dual values and finite attainment, unboundedness, recession cones, escape exponents and exact regularization value functions are preserved. Higher ancillary levels use block observations. The normalized encoder gives heralded exact quantum recovery, not deterministic trace-preserving recovery.

Two bases and one free scale are necessary and sufficient in the stated datum-uniform positive-decoder model. These discrete-resource facts do NOT give a matching lower bound for the quadratic two-basis matrix order. This is a polynomial-time normal-form REDUCTION, not an exact-feasibility DECISION algorithm.

## 7. Prior history, code and precise limits

The unrestricted_rational/ directory retains the exact constructor, symbolic endpoint examples, results and instructions for 10–12. Earlier code and results for 01–09 remain in this directory and strengthening_audit/. All original historical numbered milestones and corrections remain inherited on this branch.

Milestones 13–19 are analytic manuscripts. Classical factorization, PSD scaling/semicontinuity, block-diagonal additivity, and SOS certificate theory are attributed explicitly rather than presented as newly discovered. The current progression supplies proved structural/certificate formulations and exact-family consequences; it does not evaluate standard extension complexity for all convex bodies by a new scalar formula.

No claim is made of a polynomial-time general PSD-rank algorithm, finite detection of nonrepresentability at ALL orders from finitely many rejected orders, a full characterization of all rational power weights, external priority certification, independent refereeing, or a journal acceptance decision.
