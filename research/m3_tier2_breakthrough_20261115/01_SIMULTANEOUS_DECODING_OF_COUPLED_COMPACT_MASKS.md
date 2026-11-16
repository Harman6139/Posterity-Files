# Checkpoint 01 — simultaneous decoding defeats arbitrarily many coupled compact masks

Date 2026-11-15. Original exact rational scalar value/coordinate-gradient oracle; no noisy or radius-charged substitution. This is a new dimension-independent theorem for a precisely stated, genuinely coupled natural conic class. It is NOT a theorem for all affine PSD pencils.

## 1. Full definition of the class

Use h=1/8, a=1/4, lambda=1/64, eta=lambda*h^2=1/4096. The rational measures mu_w^-,mu_w^+ for a word w of length n are as follows. At the empty word, mu^- has mass 1/6 at each of -1,-3/4,-1/2, and mu^+ is its reflection. At each nonempty word with first sign theta, append a child of mass lambda under t -> theta*a+h*t. The lower reservoir weights at (-1,-3/4,-1/2) are

    theta=-1: (2665,2942,2457)/16384,
    theta=+1: (2121,4286,1657)/16384.

Upper reservoirs are obtained by reflection and replacing theta by -theta. Repeat recursively. Every measure has mass 1/2; its first moment is -3/8 on the lower side and +3/8 on the upper side; second moment is 29/96 on either side. Every support is contained in [-1,1]. These identities are direct rational Vandermonde identities (the original exact-rational checkpoint 01 supplies the full expansion). The smallest support point of every lower measure is -1, with atom mass at least

    nu0=2121/16384.

For the empty measure the mass there is 1/6>nu0. Reflection gives the corresponding upper endpoint property.

Fix any ambient d>=2 and any number M>=1 of masks. KNOWN data consist of rational p_i in R^d, rational unit vectors e_i, rational C_i>=2, and positive rational weights omega_i with sum_i omega_i=1. Put

    c_i^+=p_i+C_i e_i, c_i^-=p_i-C_i e_i.

Assume all 2M centers c_i^+,c_i^- are pairwise distinct. The pairing and weights are supplied side information common to the entire class. Unknown labels are arbitrary words w_i in {-1,+1}^n. Define

    K_i(x)=(1/4) int (||x-c_i^+||-(C_i-s))_+^2 dmu_(w_i)^-(s)
           +(1/4) int (||x-c_i^-||-(C_i+s))_+^2 dmu_(w_i)^+(s),
    F(x)=sum_i omega_i K_i(x),
    f(x,z)=F(x)+phi(z),
    phi(z)=(sqrt(z^2+4)-z)^2/8.

Require that the zero sets of the K_i have a common point. These are coupled constraints on the SAME vector x, not independent coordinate sums, and no orthogonality among the e_i is assumed. A class with the original normalization/profile is obtained by additionally restricting f(0,0)<=1 and the declared common profile bounds. The algorithmic upper theorem does not need those extra restrictions.

The oracle returns exactly f and its coordinate gradient. In fact the algorithm below uses scalar values alone. Query radii, degrees, computation and unqueried outputs are unrestricted as in the original model.

## 2. Exact rational isometric conic realization

For each radial term with radius r>0 and coefficient w/2, write w as a sum of at most four nonnegative rational squares b_l^2. The rational arrow b_l [[r,(x-c)^T],[x-c,r I_d]] has negative-square energy b_l^2(||x-c||-r)_+^2/2 and coordinate Gram matrix 2b_l^2 I_d. Here choose each radial weight w=omega_i*(measure atom weight)/2. Their total is 1/2. The total x-coordinate Gram is therefore I_d, and directions from different x coordinates are orthogonal. Append W(z)=[[0,1],[1,z]], whose direction is unit and disjoint.

Each positive rational w has a four-square rational representation: if w=A/B, represent integer AB as a sum of four integer squares and divide those integers by B. This is an exact existence/encoding argument, not an approximation. Matrix order is O(M(n+1)(d+1)); bit lengths are polynomial in n, M, d and the lengths of the supplied geometry and weights. The actual natural PSD-distance loss is exactly f.

The W block has determinant -1, ruling out exact PSD feasibility. At a common zero of all K_i, let z tend to infinity. Hence every such instance is genuinely weakly infeasible. Unlike an SDP epigraph reduction, this is equality of the entire natural loss at every finite query.

## 3. A scalar algebraic observation separates active first-radius moments

For a fixed center c, write Q_c(x)=||x-c||^2. At a point where no center-distance equals an atom radius, the local formula for F is

    F(x)=P(x)-sum_c beta_c sqrt(Q_c(x)),                 (1)

where P is a rational quadratic polynomial and

    beta_(c_i^+)=(omega_i/2) int_(s>A_i(x)) (C_i-s) dmu_(w_i)^-(s),
    beta_(c_i^-)=(omega_i/2) int_(s<B_i(x)) (C_i+s) dmu_(w_i)^+(s),
    A_i(x)=C_i-||x-c_i^+||,
    B_i(x)=||x-c_i^-||-C_i.

The integrals use the active atoms at the queried point; they are constant coefficients on its regular neighborhood. The triangle inequality gives

    A_i(x)<=B_i(x)                                    (2)

at every x, since the two centers are distance 2C_i apart.

LEMMA 1. In any prescribed nonempty rational open ball, one can choose a real-algebraic q such that F(q) uniquely determines P and all the beta_c in (1) among the known finite word candidates. The query is on no candidate radius boundary. No derivatives need be returned.

PROOF. For d>=2, each Q_c is irreducible over Q[x]: it is a translated sum of at least two squares and has no real affine-linear factor. Distinct centers give nonassociate irreducibles, so their square classes are independent in Q(x)^*/Q(x)^{*2}. Consequently 1 and the sqrt(Q_c) are linearly independent over Q(x). If two coefficient tuples in (1) differ, their difference E is a nonzero element of the multiquadratic extension. Its field norm, formed by independently changing the signs of all at most 2M radicals, is a NONZERO rational polynomial of degree at most D=2^(2M+1). Evaluated equality implies that polynomial vanishes.

Put L=D+1, N=L^d, alpha=2^(1/N), and v_j=alpha^(L^(j-1)). Eisenstein shows deg_Q alpha=N. No nonzero rational polynomial of total degree <=D vanishes at v: its distinct monomials become distinct powers of alpha, all of degree below N. Rational translation and nonzero rational scaling preserve this property. Each v_j lies between 1 and 2, so a sufficiently small rational scale places q in the prescribed rational ball. Since D>=2, q also avoids every polynomial Q_c-r^2 for rational candidate r, and Q_c itself. Equal exact observations must therefore give identical coefficient tuples. To decode, evaluate the finitely many candidate losses algebraically at q and choose a matching candidate; its local coefficients are the true coefficients. The true candidate exists, so this is a finite terminating procedure. Complexity and algebraic degree are NOT claimed small. QED.

## 4. Positive-radius-moment gap exposes the next bit

For a known prefix v of length k<n let

    c_v=a sum_(j=1)^k v_j h^(j-1), r=h^k.

Then |c_v|<=2/7. Suppose a query satisfies

    c_v-r/2 < A_i(q) <= B_i(q) < c_v+r/2.             (3)

All ancestor reservoir contributions are inactive in both one-sided losses. Only the child measure remains after the current prefix, with weight lambda^(k+1). Normalize the observable lower beta by multiplying it by 2/omega_i.

LEMMA 2. The two observable beta coefficients at the pair of centers determine the next unknown sign, regardless of all later bits.

PROOF. First suppose A_i(q)<=c_v. For next sign +1, the query lies below ALL support of the next lower child: its support begins at c_v+(a-h)r=c_v+r/8. Its normalized active radius moment is therefore EXACTLY

    L_+=lambda^(k+1)[(C_i-c_v-a r)/2+3h r/8].         (4)

For next sign -1 the full lower-child radius moment is

    L_-=L_+ + lambda^(k+1) a r.                      (5)

If the query lies before that child's first atom, the observation is L_->L_+. Otherwise it omits the first atom, whose mass is at least lambda^(k+1)nu0 and whose radius is C_i-c_v+(a+h)r=C_i-c_v+3r/8. Every omitted radius contribution is positive. Thus the observation is at most

    L_- -lambda^(k+1)nu0(C_i-c_v+3r/8) < L_+.        (6)

For the strict inequality, C_i>=2, |c_v|<=2/7 and 0<r<=1 imply

    nu0(C_i-c_v+3r/8)-ar
       >= r[nu0(12/7+3/8)-1/4]
       = (2683/131072)r >0.                          (7)

Hence next sign +1 holds if and only if the normalized observable lower coefficient equals (4). For sign -1 the value is strictly above or below it, but never equal. Candidate radius equality boundaries were avoided in Lemma 1.

If A_i(q)>c_v, equation (2) gives B_i(q)>c_v. Reflect the upper measure: mu_w^+ is the reflection of mu_(-w)^-. Apply the argument just proved to lower argument -B_i(q) <= -c_v, reflected prefix center -c_v, and reflected word -w. The target equality then corresponds to original next sign -1. This determines the original next sign. QED.

The strict positive gap (7) is the essential new mechanism. It prevents cancellation among arbitrary later branches; merely knowing that two scalar functions differ would not suffice. Lemma 1 isolates the moments at DISTINCT centers even when the geometric constraints on x are strongly coupled.

## 5. A common feasible comparison region permits ALL labels to advance at once

Suppose k bits of every word have been learned. Define the known open convex set

    O_k={x: A_i(x)>c_(v_i)-h^k/2 and
                B_i(x)<c_(v_i)+h^k/2 for every i}.    (8)

Equivalently this is the intersection of the open balls with centers c_i^+,c_i^- and radii

    C_i-c_(v_i)+h^k/2,  C_i+c_(v_i)+h^k/2,

respectively.

LEMMA 3. For k<n, O_k is nonempty and contains a full open ball, despite arbitrary coupling among masks.

PROOF. Take any common core-zero point u of the true instance. If r'=n-k>=1 signs remain, the true scalar zero interval of the remaining word has endpoints whose absolute values are at most

    a(1-h^r')/(1-h)+h^r'/2 <= 5/16.

Indeed the maximum is at r'=1 and equals a+h/2=5/16. A core-zero point therefore satisfies A_i(u)>=c_(v_i)-(5/16)h^k and B_i(u)<=c_(v_i)+(5/16)h^k. This leaves a margin at least (3/16)h^k in every inequality (8). Each A_i,B_i is 1-Lipschitz. Thus a ball about u of radius smaller than (3/16)h^k lies in O_k. QED.

All data defining O_k are known rational parameters, so one may enumerate rational balls whose closures are contained in O_k, using exact norm comparisons; a ball exists and this terminates. Select q inside it by Lemma 1 and query f(q,0). Subtract phi(0)=1/2. Recover all active coefficients, and apply Lemma 2 to EVERY i simultaneously. One query has now learned one further bit of EVERY hidden word.

There is no independent-coordinate assumption: q solves one simultaneous convex feasibility problem. Its offline computation is permitted by the original unlimited-computation model. The response is only a scalar natural loss, not the projection matrix or a new groupwise oracle.

## 6. Dimension-independent optimization bound

THEOREM 4. For every epsilon>0, the described class is optimized to f<=epsilon using at most

    min{ n, max(0,ceil(log(9/(8epsilon))/log(4096))) }  (9)

exact scalar natural queries, with the convention that n queries completely recover the words and allow an exact common core zero. The bound is independent of ambient d, mask count M, coefficient heights, and geometry condition numbers.

PROOF. After k<n rounds all prefixes of length k are known. Choose any x in O_k without another oracle call. Every ancestor reservoir vanishes, and (3) places both standardized arguments in (-1/2,1/2). The support of either remaining measure lies in [-1,1] with mass 1/2. Each scalar one-sided loss is therefore at most (1/2)(1/2)(3/2)^2=9/16. The radial core is half the sum of those two losses, so

    K_i(x)<= (9/16)eta^k,  F(x)<=(9/16)eta^k,         (10)

using sum omega_i=1. For the chosen k in (9), this is at most epsilon/2. Append z=epsilon^(-1/2)-sqrt(epsilon), which has phi(z)=epsilon/2.

If n rounds finish first, every word and the true zero interval of every mask are known. Their common zero set is the intersection of the two corresponding CLOSED balls per mask; it is nonempty by hypothesis. Exact real-algebraic computation returns a point in it, and the same finite tail output completes the guarantee. No queried-output restriction is used. QED.

Restrict now to members satisfying f(0)<=1 and a fixed beta=1/2 escape profile. The theorem still applies. Conversely, the original one-pair radial family in exact-rational checkpoint 12 (d=2, p=0, C=2, omega=1) lies in this restricted class. One radial query is simulated by at most two first-mismatch word queries; success at epsilon_n=(5/768)4096^-n identifies its hidden word. Its fixed uniform prior gives Omega(log(1/epsilon)) calls at fixed confidence. Therefore, over ALL ambient dimensions and ALL numbers of DISTINCT center pairs in the present declared class,

    N(epsilon; success 2/3)=Theta(log(1/epsilon)).     (11)

This closes the previously growing-center possibility for this specific moment-template architecture, not merely the fixed-center subclass. All locations are arbitrary finite real points and all original pencil coefficients are rational.

## 7. Boundaries and what remains of Tier II

The new theorem extends beyond independent rotated scalar copies and beyond a fixed number of radial centers: the constraints may be arbitrarily coupled, and M may grow polynomially or faster with a horizon. The actual algebraic query degree can grow exponentially with M and d; such degrees are FREE in the original information model and must be disclosed.

Material hypotheses: the center pairing, radii base C_i, weights and moment templates are known; the 2M centers are distinct; only the words are hidden; a common core zero exists. Repeated centers mix the identifiable radius moments and are NOT covered by Lemma 1's groupwise use. Arbitrary unknown radial distributions, unknown pair assignments, anisotropic pencils, arbitrary irreducible matrix pencils and a weakly infeasible nonseparable core are not covered.

The original all-pencil beta=1/2 bracket is still logarithmic lower versus epsilon^-1 upper. This checkpoint rules out a major concrete coupled masking extension at polynomial loss; it does not establish either universal branch of the flagship dichotomy. Source ingredients are from exact-rational checkpoints 01,11,12, with the new active-moment gap, simultaneous feasible probe construction, and uniform-in-M decoding proof supplied here.
