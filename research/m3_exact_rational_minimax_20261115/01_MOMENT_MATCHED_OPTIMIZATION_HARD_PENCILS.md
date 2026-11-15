# Checkpoint 01 — exact rational pencils with optimization-relevant branch hiding

Date: 2026-11-15. Parent research snapshot: f843934bd5c83280b732bface3967737207e93da. Earlier source files are unchanged.

## Scope

This construction addresses the ORIGINAL unrestricted, exact natural value-and-coordinate-gradient oracle with rational affine coefficients and rational orthonormal coordinates. It uses neither positive oracle error nor a query-radius charge. Unlike the earlier objective-identification example, its different members have disjoint small-objective regions. The resulting accuracy lower bound is logarithmic, not yet the requested dimension-uniform power law. The exact query game and matching fixed-coordinate-dimension theorem are proved separately in checkpoint 02.

## 1. Fixed rational moment data

Put h=1/8, a=1/4, lambda=1/64 and eta=lambda*h^2=1/4096. Let L=(-1,-3/4,-1/2). The base lower measure has weight 1/6 at each point of L; the base upper measure is its reflection. Their moments of orders 0,1,2 are respectively

    M^-=(1/2,-3/8,29/96),  M^+=(1/2,3/8,29/96).

For c in {-a,a}, define the following three positive reservoir weights, indexed by L in its displayed order:

    r^-(-a)=(2665,2942,2457)/16384,
    r^-( a)=(2121,4286,1657)/16384.

Let r^+(c) put the weights r^-(-c), in the SAME indexed order, at -L=(1,3/4,1/2). Write T_c(t)=c+h*t. These weights solve, for k=0,1,2,

    sum_i r_i^-(c) L_i^k + lambda integral T_c(t)^k dmu^-(t)=M_k^-,
    sum_i r_i^+(c) (-L_i)^k + lambda integral T_c(t)^k dmu^+(t)=M_k^+,

whenever the child measures have moments M^- and M^+. This is a three-by-three Vandermonde calculation. All reservoir weights are strictly positive. Their total mass on each side is (1-lambda)/2.

## 2. Recursive finite measures

For a sign word w=(w_1,...,w_n) in {-1,1}^n, recursively define

    mu_w^- = sum_i r_i^-(w_1*a) delta_(L_i) + lambda (T_(w_1*a))# mu_(w_2,...,w_n)^-,
    mu_w^+ = sum_i r_i^+(w_1*a) delta_(-L_i) + lambda (T_(w_1*a))# mu_(w_2,...,w_n)^+.

At the empty word use the base measures. Every measure is positive, rational and supported on [-1,1]. Each side has 3(n+1) atoms before merging and the same three moments as its base measure, independently of the entire word.

Define the convex squared-hinge objective

    H_w(x)=1/2 integral (t-x)_+^2 dmu_w^-(t)
           +1/2 integral (x-t)_+^2 dmu_w^+(t).

It is nonnegative, convex, C1, and has derivative Lipschitz constant at most one because the total measure mass is one.

Let

    c_w=a sum_(j=1)^n w_j h^(j-1),
    I_w=c_w+h^n[-1,1],
    J_w=c_w+h^n[-1/2,1/2].

The two child intervals at any node are disjoint and lie inside the node's middle half. Every lower reservoir atom is to the left of both child intervals, and every upper reservoir atom is to their right. Induction therefore gives

    argmin H_w=J_w,  min H_w=0.

Indeed the largest lower threshold and smallest upper threshold are respectively c_w-h^n/2 and c_w+h^n/2. In particular the minimum centers lie in [-2/7,2/7]. The intervals I_w of distinct words of a common length are disjoint.

## 3. Exact exterior equality and recursive locality

For every word, the exterior expressions are the SAME quadratics:

    H_w(x)=Q_-(x)=x^2/4+3x/8+29/192, x<=-1,
    H_w(x)=Q_+(x)=x^2/4-3x/8+29/192, x>=1.

This follows directly by expanding the squared hinges and using the three common moments. Their derivatives agree there as well; the identities include the endpoints.

At a node with first center c=w_1*a,

    H_w(x)=R_c(x)+eta H_tail((x-c)/h),

where R_c is the sum of the six reservoir squared hinges. On [-1/2,1/2], R_c and its derivative vanish. If x is outside the selected child interval c+h[-1,1], its child contribution is one of the known quadratics, independently of every later sign. Thus the exact value and gradient depend only on the prefix up to the first child interval that fails to contain x. This is an equality of responses at every real x, not a small-signal argument. Arbitrarily large queries supply only the fixed exterior quadratic.

Nonnegativity of reservoir terms at every level also gives, globally,

    H_w(x)>=eta^n H_empty((x-c_w)/h^n).

The base function has H_empty(-1)=H_empty(1)=5/192 and is monotone outward from its zero interval. Consequently

    x not in interior I_w  ==> H_w(x)>= (5/192) eta^n.

For epsilon_n=(5/384)eta^n, any epsilon_n-successful output must have x in I_w. Hence successful optimization identifies the hidden word; unlike the earlier shared-solution example, zero-query optimization is not possible at these scales.

## 4. Actual rational isometric PSD pencils

Every positive reservoir weight is a sum of four rational squares with FIXED coefficients: its denominator is 16384=128^2, and its numerator is a sum of four integer squares. The base weight 1/6 is (1/6)^2+(1/6)^2+(1/3)^2+0^2. At level j the common multiplier is lambda^j=(1/8^j)^2, so each square root factor remains rational. No approximation of a real rotation is used.

For a lower atom (t,w) with w=sum_(r=1)^4 b_r^2, put the four scalar diagonal entries b_r(x-t) in the pencil. For an upper atom put b_r(t-x). Append the two-by-two weak-infeasibility block

    W(z)=[[0,1],[1,z]].

The full block-diagonal matrix X_w(x,z) is rational of order m=24(n+1)+2 (zero factors may be retained). Its exact natural squared PSD distance is

    f_w(x,z)=H_w(x)+phi(z),
    phi(z)=(sqrt(z^2+4)-z)^2/8.

The x direction has squared Frobenius norm sum of all measure weights=1. The z direction has norm one and disjoint support. Thus the two coordinate directions are Frobenius orthonormal. All three affine coefficient matrices are rational. Each nonzero entry uses O(n) bits, there are O(n) nonzero entries, and the total ordinary explicit encoding is O(n^2) including zero locations/entries. The order and encoding are polynomial in n.

There is no PSD point because W(z) always has determinant -1. At x=c_w all scalar blocks are PSD, and phi(z) decreases to zero as z increases to infinity. Therefore every instance is genuinely weakly infeasible.

Moreover, the total moment identities give the strong uniform matrix normalization

    <X0,Hx>=<X0,Hz>=0,
    ||X0||_F^2=2+29/48=125/48,
    ||X_w(x,z)||_F^2=125/48+x^2+z^2.

The hidden information is not encoded in an unbounded origin shift or a nonrational coordinate chart. Since all thresholds have magnitude at most one and total weight one, H_w(0)<=1/2 and f_w(0,0)<=1.

## 5. Common all-scale escape profile

For 0<s<=1/8, phi(z)<=s implies

    z >= (2s)^(-1/2)-sqrt(2s) >= (1/2)s^(-1/2).

This supplies the lower radius bound for f_w. For the upper bound take x=c_w and z=(2s)^(-1/2)-sqrt(2s). The objective equals s, |c_w|<=2/7, and

    x^2+z^2 <= 4/49+1/(2s) <= 1/s

on the displayed interval. Hence ALL depths and words satisfy

    (1/2)s^(-1/2) <= rho_f_w(s) <= s^(-1/2),  0<s<=1/8.

This is the original normalized beta=1/2 class, with constants and onset independent of n, matrix order, encoding height and sampled word.

A fixed rational conic tail of any other prescribed positive rational beta can replace W. Its known all-scale profile gives corresponding uniform constants, because the core minimizer stays in [-2/7,2/7]. That extension uses only the tail construction of earlier checkpoint 05; beta=1/2 above is wholly explicit and self-contained.

## 6. What the construction does and does not prove

The hidden word can be chosen uniformly before the algorithm's independent random seed. The exact locality holds for all real queries, with no restrictions on their magnitude, degree or precision. Successful optimization at epsilon_n determines the word. The next checkpoint proves the exact binomial minimax success law and a matching logarithmic fixed-coordinate-dimension frontier.

Because epsilon_n=(5/384)4096^(-n), this particular construction does NOT yield failure at a polynomial-in-T objective threshold. It cannot be called the requested Omega(epsilon^(-beta-1/2)) dimension-uniform lower bound. Its contribution is a genuine exact-rational OPTIMIZATION hard family, rather than merely a hard global-identification family or a different oracle model. Historical novelty and independent review remain separate obligations.