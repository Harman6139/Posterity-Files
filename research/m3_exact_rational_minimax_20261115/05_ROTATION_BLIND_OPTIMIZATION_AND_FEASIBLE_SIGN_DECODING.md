# Checkpoint 05 — unknown rotations do not repair the scalar construction

Date: 2026-11-15. Parent research snapshot: b075a164511df3e83ce5df21e6578d1830fe3c95.

## Status

This checkpoint proves two obstruction theorems for proposed higher-dimensional extensions of the exact-rational construction in checkpoints 01–04. It does NOT close the unrestricted dimension-growing rational minimax problem. It makes no historical-priority claim for the elementary zonotope argument used below.

## 1. Reference scalar identities

Let H_w be the squared-hinge core in checkpoint 01, for a sign word w of length n. Put

    h=1/8, a=1/4, lambda=1/64, eta=lambda*h^2=1/4096,
    kappa=5/4096, v0=(77/192)*eta.

For a prefix v of length k, write

    c_v=a sum_{j=1}^k v_j h^(j-1), c_empty=0.

For every word w and every k<n, the exact identities at the corresponding prefix center are

    H_w(c_{w[:k]}) = v0 eta^k,
    H'_w(c_{w[:k]}) = -kappa (eta/h)^k w_{k+1}.       (1)

At k=n, both expressions are zero (the second with no next sign). All ancestor reservoir losses vanish on a neighborhood of the prefix center. Thus the local recursion reduces to eta^k H_suffix((t-c_prefix)/h^k). At the origin of a nonempty suffix the selected child is centered at +/-a, so the child's standardized argument is -/+2. Its exterior derivative is -/+5/8. The chain rule gives H'_suffix(0)=-lambda*h*(5/8)w_1=-kappa w_1. The value is eta Q_+(2)=(77/192)eta. This proves (1), including its independence of every later sign.

## 2. A rotation-blind optimizer in every dimension

Let D>=1, U be ANY real orthogonal D-by-D matrix, and w_1,...,w_D be arbitrary sign words of a common length n. The rotation U and all the words may be hidden. Set

    F(x)=(1/D) sum_{i=1}^D H_{w_i}(sqrt(D)*(U^T x)_i). (2)

This is convex, nonnegative, and 1-smooth, and F(0)=v0 independently of D. Give only the exact gradient of F. Define

    x_0=0,
    x_{k+1}=x_k-(a/kappa) lambda^(-k) grad F(x_k),
                     0<=k<n.                         (3)

THEOREM A. For every hidden U and every collection of words, the iterates satisfy

    x_k = (1/sqrt(D)) U (c_{w_1[:k]},...,c_{w_D[:k]}),
    F(x_k)=v0 eta^k                 for 0<=k<n,
    F(x_n)=0,
    ||x_k||<=2/7                   for every k.       (4)

The method does not recover U, does not identify individual words in physical coordinates, and does not need function values.

PROOF. The state identity is true at k=0. At a state of the asserted form, the standardized coordinates in (2) are exactly the corresponding prefix centers. Equation (1) and the chain rule give

    grad F(x_k)=-(kappa/sqrt(D))(eta/h)^k U s_{k+1},

where s_{k+1} is the vector of the next hidden signs. Multiplying by the prescribed step in (3) gives the increment

    (a/sqrt(D)) lambda^(-k)(eta/h)^k U s_{k+1}
       =(a/sqrt(D)) h^k U s_{k+1},

because eta=lambda*h^2. This is precisely the next prefix-center increment, proving the state identity by induction. Averaging the identical values v0 eta^k in (1) proves the objective identity; at depth n every scalar core vanishes. Finally |c_v|<=a/(1-h)=2/7, and orthogonality yields ||x_k||^2=D^(-1)sum_i c_{w_i[:k]}^2<=(2/7)^2. QED.

The large factors lambda^(-k) are allowed by the stated exact-oracle model. They are not a practical floating-point recommendation. Despite these growing step lengths, the actual states remain uniformly bounded.

## 3. Genuine rational isometric conic consequences

When D is a perfect square and U is rational orthogonal, (2) has an exact rational isometric diagonal PSD-distance realization. If the scalar pencil for H_{w_i} has entries b_{ir}(t-t_{ir}) (with either orientation), replace each entry by

    (b_{ir}/sqrt(D)) [sqrt(D)*(U^T x)_i-t_{ir}].

Its squared distance contribution is H_{w_i}(sqrt(D)*(U^T x)_i)/D. The coefficient Gram matrix from the i-th group is u_i u_i^T, because the original atom masses sum to one. Summing gives I_D. All coefficients are rational for square D, including the offsets. Append the known weak-infeasibility block

    W(z)=[[0,1],[1,z]].

The result is a rational natural PSD-distance objective

    f(x,z)=F(x)+phi(z),
    phi(z)=(sqrt(z^2+4)-z)^2/8.

The chart is Frobenius isometric, f(0,0)=v0+1/2<1, and the W block makes every instance weakly infeasible. Since every zero core has radius at most 2/7, the previous direct calculation gives the SAME dimension-independent profile

    (1/2)s^(-1/2)<=rho_f(s)<=s^(-1/2), 0<s<=1/8.      (5)

For example the upper witness is a core zero and z=(2s)^(-1/2)-sqrt(2s); its squared norm is at most 4/49+1/(2s)<=1/s.

The x component of the natural gradient is grad F and is independent of z. Run (3) with z=0 in each query. After T<n calls the core value is v0 eta^T; after T>=n it is zero. For any requested epsilon, choose T so that v0 eta^T<=epsilon/2, or stop after n calls, and append a finite z with phi(z)<=epsilon/2. This uses

    O(1+log(1/epsilon))

queries uniformly in D, U, n, and the words. A concrete output is z=epsilon^(-1/2)-sqrt(epsilon), for which phi(z)=epsilon/2.

Consequently an arbitrary unknown rational or real orthogonal rotation of arbitrarily many equal-scale copies DOES NOT create the missing polynomial-in-T objective barrier. This is stronger than the known-coordinate separability observation in checkpoint 04: here neither the basis nor the scalar-coordinate labels are known to the algorithm.

This theorem does not cover arbitrary nonorthogonal coupling, unequal unannounced scalar scales, different types of multivariate cores, or arbitrary additional padding. A new padding term could change the gradient identity and requires its own proof.

## 4. Feasibility prevents a second proposed aggregate-information trick

Let a_1,...,a_M be known vectors in R^d, let p_i>0 be known, and consider sign vectors theta in {-1,+1}^M. Suppose the allowed sign patterns satisfy

    there exists u_theta with theta_i <a_i,u_theta>>0 for all i.  (6)

LEMMA B (feasible-sign injectivity). The map

    theta -> z_theta=sum_i p_i theta_i a_i             (7)

is injective on the patterns in (6). In fact an allowed theta has a unique preimage among ALL sign patterns, allowed or not.

PROOF. If theta' differs from theta and z_theta=z_theta', take the inner product of the difference with u_theta. Each differing coordinate contributes

    p_i(theta_i-theta'_i)<a_i,u_theta>
      =2p_i theta_i<a_i,u_theta> >0,

and each equal coordinate contributes zero. The sum cannot vanish. QED.

Quantitative version: if ||u_theta||<=R and theta_i<a_i,u_theta>>=r_i>0, then for every theta'!=theta,

    ||z_theta-z_theta'|| >= (2/R) sum_{i:theta_i!=theta'_i} p_i r_i. (8)

This follows by Cauchy–Schwarz from the same calculation. Positive margins exclude u_theta=0, so R may be taken positive. For affine signs <a_i,u>-b_i, replace a_i by (a_i,-b_i) and u by (u,1); the denominator becomes sqrt(R^2+1) for a witness of norm at most R.

Geometrically, z_theta is the uniquely selected vertex of the zonotope sum_i[-p_i a_i,p_i a_i] in direction u_theta. This is the classical zonotope/hyperplane-arrangement correspondence, not a new result about zonotopes.

## 5. Application to coupled first-level hidden bits

Consider

    F_theta(x)=sum_i p_i H_{theta_i}( <a_i,x> ),

where H_{theta_i} is the one-bit member of the scalar construction (or a deeper word whose first bit is theta_i). Suppose the family contains only instances whose cores have a common zero for all their summands; this is necessary for a zero-infimum direct sum with a separate positive tail. Such a zero u obeys

    theta_i<a_i,u> >= 3/16

because every zero interval of the word lies inside its first selected zero interval. At the origin,

    grad F_theta(0)=-kappa sum_i p_i theta_i a_i.        (9)

Thus a SINGLE exact gradient query identifies ALL first-level signs, even with redundant and nonorthogonal known normals. Enumerating the finitely many sign patterns and matching (9) is a finite decoder; no efficient runtime is asserted. If deeper signs are present, this theorem identifies their first levels only, not their entire words.

The argument shows why merely arranging collisions of signed sums for arbitrary bit strings is insufficient: the collision patterns may be excluded by the requirement that the displayed conic core actually have a zero. No claim is made for unknown a_i or for arbitrary coupled nonlinear spectral blocks.

## 6. Frontier status

Neither theorem proves a fast optimizer for every rational PSD-distance instance, and neither supplies a new hard prior at polynomial accuracy. They eliminate specific attempted ways of amplifying the established scalar construction. The full dimension-growing exact-rational minimax frontier remains open in this work.
