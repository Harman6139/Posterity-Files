# Checkpoint 11 — rational conic hardness under arbitrarily small input-relative error

This is a polynomial-encoding rational conic theorem in a precisely specified inexact information model. Unlike a radius restriction, it permits every finite query at unit sample cost. It does not prove the original noiseless rational theorem: the positive error allowance is essential to the lower-bound construction.

## 1. Information model and main statement

Let P_beta^Q be the class of rational, isometrically parametrized, genuinely weakly infeasible affine PSD pencils with f(0)<=1 and fixed uniform profile constants rho_f(s) comparable to s^-beta on a fixed small interval, as in the preceding checkpoints. Matrix data are hidden. Fix a positive rational beta.

A coordinate-gradient measurement at q has conditional mean grad f(q)+b and conditional centered variance bounded by

    ||b|| <= zeta(1+||q||),
    E||G-E[G|history]||^2 <= tau^2(1+||q||)^2.         (1)

These are input-relative, not residual-relative, errors. They are a mathematical measurement specification, not a theorem about every floating-point projection routine. Queries are arbitrary finite vectors, computation is unrestricted, and outputs need not have been queried. Exact population values are not returned.

THEOREM. There are positive constants depending only on beta and the fixed profile class such that, for every sufficiently small epsilon and EVERY

    0 < zeta <= c_beta epsilon^(2beta+1),

the minimax expected-error sample complexity in (1) is

    Theta_beta(epsilon^(-beta-1/2)
                    +tau^2 epsilon^(-4beta-2)).       (2)

The constants are uniform in tau>=0 and in positive zeta in that interval. If

    zeta >= C_beta epsilon^(2beta+1),

an expected-epsilon guarantee is impossible, regardless of the number of queries. The same powers hold at a fixed success probability. The lower distributions are fixed before the algorithm's seed and consist of rational conic instances; the sequential construction has polynomial matrix order in the horizon and polynomial coefficient bit length in the horizon and log(1/zeta).

At zeta=0 the variance lower bound remains valid, but the sequential lower bound for the full rational class is NOT established here. For the specific rational quadratic-lift subclass used below, one exact gradient query suffices at zeta=tau=0. Thus the positive-zeta assertion must not be extended to its zero endpoint by continuity.

## 2. Upper bound

Take a comparator u with f(u)<=epsilon/4 in the known ball Q of radius

    R=max(1,C_beta(epsilon/4)^-beta).

On Q, the input-relative model implies the absolute bounds

    bias <= zeta(1+R), variance <= tau^2(1+R)^2.

The accelerated batched energy estimate from source milestone 39, reproduced in the standalone manuscript, yields cost

    O(R/sqrt(epsilon)+tau^2(1+R)^2 R^2/epsilon^2)

provided zeta(1+R)<=epsilon/(8R). Since R>=1, this proves the upper half of (2) and the sufficient error scale. The iterates themselves remain in Q; the model nevertheless allows arbitrary queries.

## 3. Real hard rotations with a fixed rational linear term

Use the construction of checkpoint 09 with A0 positive definite, b0=a^2 e1, q0(x)=x^T A0 x/2-b0^T x+c0, and the common tail. Instead of Haar measure on O(D), take Haar measure on the stabilizer

    G={U in O(D):Ue1=e1}.

The deferred-rotation proof is unchanged: its initial assigned subspace is span(e1), whose image is now fixed rather than uniformly sampled. Conditional on every later assignment, the remaining map between orthogonal complements is Haar. The Gaussian augmentation and repeated-eigenspace projection estimate are identical. Thus all conclusions of checkpoint 09 hold with the SAME known rational b=b0 for every instance.

Write the natural objective as

    f_U(x,y)=F(U^T x)+g_beta(y),
    F(x)=q0(x)+(sqrt(x^T P0 x)-M)_+^2/2,
    P0=I/2-A0, I/4 <= P0 <= I/2.

Here F is nonnegative, 1-smooth, F(0)=c0, grad F(0)=-b0, and every U fixes b0. The scale M is max(1,ceil(||x_star||)) and is polynomial in the horizon.

For any U,V in G with ||U-V||_op<=delta, 1-smoothness gives the GLOBAL inequalities

    ||grad_x f_U(x,y)-grad_x f_V(x,y)|| <=2delta||x||,
    |f_U(x,y)-f_V(x,y)| <=delta||x||^2.                (3)

To prove the first, write H(z)=grad F(z)+b0. Then H(0)=0, H is 1-Lipschitz, and the difference is U H(U^T x)-V H(V^T x), bounded by delta||x||+delta||x||. The tail gradients coincide. Integrating this gradient difference along the segment from 0 to x proves the second, since both functions have the same value at x=0. These estimates do not deteriorate with M or with query magnitude beyond the displayed homogeneous factor.

## 4. Finite rational quantization of the fixed distribution

For every delta>0, the compact group G has a finite delta-net consisting of rational orthogonal matrices that fix e1. Moreover each net matrix may be chosen with coefficient bit length polynomial in D and log(1/delta).

Here is an explicit encoding argument. Every element of O(D-1) is a product of at most D-1 Householder reflections. A reflection H(v)=I-2vv^T/(v^Tv), for nonzero v, is rational whenever v is rational. Approximate each unit reflection vector by a dyadic vector with Euclidean error at most delta/(16D). Such vectors can be chosen on a finite grid with coordinate bit length O(log(D/delta)). The reflection error is at most four times the vector error after a harmless adjustment of the constant; telescoping the product gives total operator error at most delta. Multiplying D rational matrices increases coefficient bit lengths by at most a polynomial factor. Embed the resulting matrices as diag(1,V). Taking all products of the finite grid reflections gives a finite rational net. No efficient enumeration of this enormous net is claimed.

Fix an ordering of this net and a measurable nearest-net selector Q_delta. Draw a single U Haar in G BEFORE the algorithm's seed and set V=Q_delta(U). The true instance is the rational pencil for f_V. The measurement oracle returns

    G(x,y)=grad f_U(x,y).                              (4)

Conditional on U it is one fixed deterministic vector field, itself the natural gradient of another genuinely weakly infeasible conic instance. By (3), it is admissible in (1) whenever 2delta<=zeta. If one conditions only on the true rational instance V, U is latent oracle randomness; the pointwise bias bound still holds after every adaptive transcript. A joint prior on instances and admissible deterministic oracle fields is legitimate for minimax lower bounds. There is no seed-adaptive instance selection.

## 5. Output control and transfer of actual success

The lower padding bound P0>=I/4 gives, for every rotation V,

    f_V(x,y) >= (||x||/2-M)_+^2/2.

For epsilon<=1/2, f_V(x,y)<=epsilon therefore implies ||x||<=4M, regardless of the unqueried output's tail coordinates. Let ell_T be the lower objective threshold in checkpoint 09, so ell_T is a fixed beta-dependent constant times (T+1)^(-2/(2beta+1)), and put epsilon_T=ell_T/4. Choose

    delta <= min(zeta/2, epsilon_T/(16M^2)).            (5)

If an output succeeds for the rational instance, f_V(output)<=epsilon_T, equation (3) implies

    f_U(output)<=epsilon_T+delta(4M)^2<=2epsilon_T.

But the fixed-Haar theorem gives f_U(output)>=ell_T=4epsilon_T with probability at least 7/8 for EVERY T-query adaptive randomized algorithm. The transcript in (4) is exactly its genuine f_U gradient transcript. Knowledge of the quantization net, all templates, and the fixed rational b0 is allowed and does not invalidate that theorem. Consequently

    Pr{f_V(output)>epsilon_T}>=7/8.                   (6)

This proves the sequential lower term in (2) for every positive zeta. The dimension and matrix order are O_beta(T^3). The rational base factors have polynomial bit length; the rational rotations from Section 4 have polynomial bit length in T and log(1/zeta), since M and 1/epsilon_T are powers of T. The support is finite, albeit very large.

## 6. Why exact arithmetic collapses this same rational subclass

The known-template rational rotated family has rational A_V and the known rational b0,c0,M. Query a sufficiently small vector

    v=(alpha,alpha^2,...,alpha^D)/(4D),
    alpha=2^(1/(D+1)).

Its norm is less than 1, so the padding is inactive for M>=1 and the exact gradient is A_V v-b0. The numbers 1,alpha,...,alpha^D are linearly independent over Q, because X^(D+1)-2 is irreducible by Eisenstein. Each gradient coordinate therefore uniquely determines the corresponding rational row of A_V. Unlimited exact computation can enumerate rational rows and test equality until it finds the unique one. No polynomial-time decoding assertion is made.

After decoding A_V, compute x_star=A_V^-1 b0, which has the known rotation-invariant norm and zero padding. Append a sufficiently accurate point on the known tail. One exact gradient query therefore attains every positive objective tolerance on this rational subclass. Zero queries cannot uniformly select the hidden core minimizer at the hard scales, but that extra statement is unnecessary for the discontinuity comparison.

The positive-error lower distributions change as zeta decreases; their coefficient height can grow. This is a minimax discontinuity over the class of all rational encodings, not a discontinuity for one fixed finite list of bounded-height inputs.

## 7. Sharp input-relative bias and variance: a rational curvature pair

Use the rational carrier parameters of checkpoint 02 with t<=1/16:

    a(t)=2t/(1+2t^2), c(t)=(1-2t^2)/(1+2t^2),
    A1=a(t)^2, A2=a(2t)^2, lambda=A2/A1 in [3,4].

Choose dyadic R0 as there and set b=A1 R0, r1=R0, r2=b/A2=R0/lambda. Both instances have the natural rational isometric pencil

    diag( [[0,a_i(x-r_i)],[a_i(x-r_i),0]],
           c_i(x+2R0), tail_beta(y) ),

with objective

    f_i(x,y)=g_beta(y)+(A_i/2)(x-r_i)^2
                        +[(1-2A_i)/2]min(x+2R0,0)^2. (7)

Put Delta=A1 R0^2/2=Theta_beta(R0^(-1/beta)). Then

    A1=Theta_beta(Delta^(2beta+1)).

Both core zeros lie in [R0/4,R0], and their initial core values are Delta and Delta/lambda. The same two-case comparison argument as checkpoint 02 proves a common all-scale escape profile. Three independent copies still have f(0)<1 at sufficiently small Delta and common profile constants.

Let m(x)=min(x+2R0,0) and k(x)=x-2m(x). Directly checking x>=-2R0 and x<-2R0 gives |k(x)|<=|x|. The exact x gradient of (7) is

    m(x)-b+A_i k(x).                                  (8)

### Bias

The common midpoint gradient replaces A_i by (A1+A2)/2. Its error is at most (3A1/2)|x|. It is admissible under input-relative bias zeta>=3A1/2.

The average of the two quadratic cores has minimum

    Delta (lambda-1)^2/[2lambda(lambda+1)] >=Delta/6.

The filler and tail are nonnegative. Thus the common oracle prevents an expected error below Delta/6 for any query budget. Choosing Delta a sufficiently large fixed multiple of epsilon gives the necessary scale zeta>=C_beta epsilon^(2beta+1).

For confidence, a wrong decision relative to the midpoint (r1+r2)/2 has core loss at least Delta/9. With three independent hidden binary choices, the common oracle leaves eight disjoint success alternatives when epsilon<Delta/9, so average failure is at least 7/8.

### Variance

Draw Y=A_i+xi with xi~N(0,tau^2) independently on each call, and return m(x)-b+Y k(x), together with the exact tail gradient. Its conditional centered variance is tau^2 k(x)^2<=tau^2||q||^2. Every transcript is simulated by iid observations Y; arbitrary query magnitudes cannot improve that statistical experiment. Three independent carrier coordinates, each with such a Y, still have total gradient variance at most tau^2 sum_j x_j^2<=tau^2||q||^2.

For the three-copy fixed uniform prior, the optimal probability of identifying all labels from N samples is

    [Phi((A2-A1)sqrt(N)/(2tau))]^3.

If N<=tau^2/[4(A2-A1)^2], this is less than 1/3. Since success at epsilon<Delta/9 requires the correct three labels, this gives the fixed-confidence lower term

    Omega_beta(tau^2 epsilon^(-4beta-2)).

An expected-risk lower bound follows as well. The pair is rational, its order is fixed for beta, and its coefficients have O_beta(log(1/epsilon)) bits. Exact population values are excluded; their constants differ and would invalidate this statistical reduction.

Combining this variance obstruction with (6), and using max(S,V)>= (S+V)/2, completes the lower half of (2). The upper bound was proved in Section 2.

## 8. Interpretation and boundary

This establishes a nontrivial, unrestricted-query rational conic frontier with a natural input-relative error specification and a sharp error tolerance. At beta=1/2 the sample law is Theta(epsilon^-1+tau^2 epsilon^-4), and the input-relative bias threshold is Theta(epsilon^2). For residual delta it is Theta(delta^-2+tau^2 delta^-8), with bias scale Theta(delta^4).

It does NOT refute or prove the original exact rational conic minimax problem. It does explain precisely why a proof that merely rationalizes a real hard distribution fails at zero error, and how an arbitrarily small, explicitly quantified measurement uncertainty restores the hard distribution with polynomial rational encodings. No adversarial rounding theorem for a specified hardware format is asserted.
