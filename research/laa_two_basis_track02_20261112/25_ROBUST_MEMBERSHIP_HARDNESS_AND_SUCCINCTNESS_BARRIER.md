# Milestone 25 — robust membership hardness and the succinctness barrier

Date: 2026-11-13 (America/Toronto).
Repository: Harman6139/Posterity-Files.
Branch: laa-track02-gptpro-analytic-frontier-20261112.
Parent snapshot: 721c8e2675cbcfdf127ebf51496cfdfd2ce4d5f5.

## Status: this is not the full proposed smooth-body breakthrough

The goal discussed in the conversation was a uniformly constructible polynomial-total-description family, with dimension-independent roundness/curvature and fixed-error superpolynomial SDP approximation hardness. This manuscript does NOT prove that goal or disprove its possibility for other bodies.

It proves why the suggested route of merely compressing the Boolean-moment family from 24 is substantially harder than a technical simplification. Its coefficient oracle is easy, but even inverse-polynomial-gap membership encodes Simple Max Cut. Any uniformly polynomial-time evaluable convex body sufficiently close to this family would imply P=NP. This applies to alternative defining polynomials, not just the original moment formula. Exact evaluation also encodes the complete cut histogram in one oracle call, and the integer homogeneous moment is #P-complete under polynomial-time oracle reductions. The original expanded polynomial is unconditionally superpolynomially dense.

The arithmetic-circuit conclusion is stated in the rational bit model. A division-free circuit with polynomial-bit rational constants computing a polynomial of known polynomial degree and coefficient height can be evaluated in polynomial bit time by modular arithmetic, even when intermediate exact values have enormous bit length. Thus unbounded intermediate cancellation is not a loophole for such circuits. Arbitrary unencoded real constants, unknown coefficient heights, and variable-division gates are not silently covered.

No lower-bound theorem from 20–24 is used as a premise. Only the explicitly displayed polynomial from 24 is used. The external hardness inputs are the classical NP-completeness of Simple Max Cut and the classical #P-hardness of the Tutte evaluation T_G(3,2). The reductions to this polynomial are proved below. No historical novelty claim is made for the general use of large moments or radix encoding.

## 1. The fixed family and elementary inclusions

For n>=2 put

    D=1+n+binom(n,2),
    w(s)=(1,(s_i)_i,(s_i s_j)_(i<j)), s in {-1,1}^n.

Let p=p(n) be the least power of two at least 2^16 n^4, and L=2p. Define

    H_n(x)=sum_s <w(s),x>^L,
    P_n(x)=||x||^2/(4D)+H_n(x),
    C_n={x:P_n(x)<=1},
    T_n={x:|<w(s),x>|<=1 for all s}.

The Boolean characters are orthonormal:

    2^(-n)sum_s w(s)w(s)^T=I_D, ||w(s)||=sqrt(D).

Consequently T_n is contained in the UNIT Euclidean ball, since

    ||x||^2=2^(-n)sum_s <w(s),x>^2<=1   (x in T_n).

This is stronger than the outer-radius bound used in 24. It is not a new approximation-complexity assertion.

Set a=2^(-(n+1)/L). Then

    a T_n subset C_n subset T_n.                       (1)

The second inclusion follows because every summand is nonnegative. For x in a T_n,

    H_n(x)<=2^n a^L=1/2,
    ||x||^2/(4D)<=a^2/(4D)<=1/16,

so P_n(x)<1. In particular (1) holds without any imported SDP theorem.

The Hessian is

    Hess P_n(x)=I_D/(2D)+L(L-1)sum_s
                       <w(s),x>^(L-2)w(s)w(s)^T.

Thus P_n is globally strongly convex and SOS-convex, C_n is a compact convex body, and all representation-model qualifications in this manuscript concern description/evaluation, not a failure of convexity.

## 2. A direct polynomial-time reduction from Simple Max Cut

Let G be a simple graph on n vertices with m>=1 edges. The decision problem asks whether its maximum cut c*(G) is at least an integer k.

Values k<=m/2 can be answered YES without an oracle, by averaging all cuts; values k>m can be answered NO. For a many-one reduction these trivial answers can instead be sent to fixed promised OUT and IN queries, respectively: the one-edge graph at threshold one, and the triangle at threshold three. We therefore restrict to

    m/2<k<=m.

Let h=2k-1, and define a rational query point x(G,k) by

    x_empty=m/h,
    x_i=0,
    x_ij=-1/h for edges {i,j}, and zero otherwise.       (2)

Its total description length is polynomial in n, and each coordinate has O(log n) bits. Since h>=m and h< n^2,

    ||x(G,k)||^2=(m^2+m)/h^2<=2,
    1/h>1/n^2.

For any sign assignment s, let c_G(s) denote its cut size. Then EXACTLY

    <w(s),x(G,k)>= [m-sum_edges s_i s_j]/h
                       =2 c_G(s)/h.                  (3)

### Theorem A: constant value gap and inverse-polynomial geometric gap

Put rho_n=1/(8n^3). Then:

    c*(G)<=k-1  =>  x(G,k)+rho_n B_2 subset {P_n<=1/2}; (4)
    c*(G)>=k    =>  P_n(x(G,k))>=2,
                    dist(x(G,k),C_n)>1/n^3.           (5)

### Proof of the NO-cut / interior case

If all cuts have size at most k-1, (3) gives

    |<w(s),x>|<=1-1/h<=1-1/n^2.

For ||u||<=rho_n, since D<=n^2,

    |<w(s),x+u>|<=1-1/n^2+sqrt(D)/(8n^3)
                         <=1-7/(8n^2).

Also ||x+u||<2, so its quadratic contribution is at most 1/D<=1/4. Its moment contribution satisfies

    H_n(x+u)<=2^n(1-7/(8n^2))^(2p)
             <=exp(n log 2-7p/(4n^2))<=1/4.

The last inequality follows immediately from p>=2^16 n^4; the weaker bound p>=4n^2(n+1) would already suffice. Adding the two contributions proves (4).

### Proof of the YES-cut / exterior case

Choose a cut with at least k edges. For its assignment s, (3) gives

    <w(s),x>>=1+1/h.

Its single moment term is at least

    (1+1/h)^(2p)>=1+2p/h>=2.

Moreover C_n is contained in the halfspace <w(s),y><=1. The Euclidean distance from x to that halfspace is

    [<w(s),x>-1]/sqrt(D)>=1/(h sqrt(D))>1/n^3.

This proves (5). QED.

Therefore even distinguishing P_n(x)<=1/2 from P_n(x)>=2, on polynomial-bit rational inputs of norm less than two, is NP-hard (the YES label is the latter case). An additive-error 1/4 evaluator would suffice for this distinction. No exact real arithmetic or exponentially fine input precision is used.

## 3. Promise weak-membership completeness

Set gamma_n=1/(16n^3). Consider rational inputs x with ||x||<=2, promised to satisfy one of:

    IN:  x+gamma_n B_2 subset C_n;
    OUT: dist(x,C_n)>=gamma_n.                         (6)

The OUT problem is NP-hard under promise-respecting polynomial-time reductions by Theorem A. It also has a polynomial certificate: a sign assignment s such that

    |<w(s),x>|>1.                                    (7)

An IN point cannot satisfy (7), because C_n subset T_n. Conversely, an OUT point cannot belong T_n. Indeed, if x belonged T_n, then ax belonged C_n by (1), and

    dist(x,C_n)<=(1-a)||x||
                <=(n+1)log(2)/p
                <1/(16n^3)=gamma_n.

Thus an OUT point has a certificate (7), checked by exact rational arithmetic. This proves NP-completeness of OUT, or coNP-completeness of IN, in the stated PROMISE sense. It does not identify the complexity of unpromised exact membership at points arbitrarily near the boundary.

The substantial distinction is between the complexity of the explicit input vector and the complexity of describing/evaluating the FIXED family P_n. Its coefficient oracle does not supply a polynomial-time membership oracle.

## 4. The obstruction persists for every sufficiently close convex body

Let A_n be ANY convex body satisfying

    d_H(A_n,C_n)<=delta_n, delta_n=1/(32n^3).           (8)

Its description, coefficients, dimension of auxiliary constructions and uniqueness of representations are unrestricted.

### Theorem B: robust alternative-description barrier

For the same query points (2),

    c*(G)<=k-1  =>  x(G,k)+gamma_n B_2 subset A_n;
    c*(G)>=k    =>  dist(x(G,k),A_n)>gamma_n.            (9)

Consequently a uniform polynomial-time promised-membership algorithm for the family A_n implies P=NP. The conclusion also holds for an exact membership algorithm, which is stronger than the required promise algorithm.

### Proof

Hausdorff distance between compact convex bodies equals the uniform distance between their support functions. If x+rho_n B_2 is contained in C_n, then for every unit u,

    h_A_n(u)>=h_C_n(u)-delta_n
                >=u.x+rho_n-delta_n.

Therefore x+(rho_n-delta_n)B_2 is contained in A_n. Since rho_n-delta_n=3/(32n^3)>gamma_n, this proves the first assertion.

The distance-to-set functions differ by at most Hausdorff distance. In the exterior case,

    dist(x,A_n)>=dist(x,C_n)-delta_n
                    >31/(32n^3)>gamma_n.

This proves the second assertion. A promised-membership test now decides Simple Max Cut. QED.

The tolerance used for the SDP lower bound in 24,

    2^(-20)n^(-4),

is much smaller than delta_n. Thus any proposed succinct replacement that stays close enough to inherit that particular lower bound is covered by Theorem B.

### Consequences for descriptions

1. Suppose A_n has a uniformly polynomial-time constructible description by polynomially many rational polynomials, each with polynomial degree, coefficient bit length, and total listed-monomial count. Exact evaluation of this description is polynomial-time on rational inputs. If (8) holds, P=NP.
2. If such descriptions merely EXIST nonuniformly for every n, their coefficients form polynomial advice, implying NP subset P/poly. This is a different consequence, not an unconditional contradiction.
3. The same uniform/nonuniform consequences apply to rational division-free arithmetic-circuit descriptions with polynomial size, final degree, constant height and coefficient-height bounds. Section 6 proves the needed bit-evaluation statement even with huge intermediate values.
4. They also apply directly to any polynomial-time weak-membership or stable numerical-evaluation algorithm. No polynomial sparse description can evade the conclusion by changing the defining polynomial while preserving (8).

These are CONDITIONAL impossibility consequences. This manuscript does not prove P!=NP or NP not-subset P/poly. Nor do they rule out a DIFFERENT succinct smooth family with difficult SDP representations but easy membership.

## 5. Unconditional density of the original coefficient list

For every multi-index beta on the D coordinates with |beta|=p, the coefficient of x^(2beta) in H_n is

    2^n (2p)! / product_A (2beta_A)! > 0.              (10)

Indeed w_A(s)^(2beta_A)=1 for every s and every coordinate A. There is no cancellation in these even monomials. Hence P_n has at least

    binom(p+D-1,D-1)                                  (11)

nonzero monomials. Since D<=n^2 and p>=2^16 n^4, this count is at least D^(D-1), and in particular is 2^(Omega(D log D)).

Thus a polynomial-length expanded coefficient list for THIS polynomial is unconditionally impossible. This monomial count does not by itself give an arithmetic-circuit lower bound: a dense polynomial can have a small circuit. The circuit consequences require the complexity reduction in Sections 2–4 or 7.

## 6. A modular-evaluation lemma closing the intermediate-growth loophole

### Lemma

Let Q in Q[x_1,...,x_D] have degree at most d and every reduced coefficient numerator and denominator have at most H bits. Suppose it is given by a division-free rational arithmetic circuit of size s with input constants of at most H0 bits. Let x be a rational input with at most B bits per coordinate.

Then Q(x) can be computed exactly in bit time polynomial in D,d,H,s,H0,B. This does NOT require polynomial intermediate values, polynomial syntactic circuit degree, or a numerical stability promise. The final degree and coefficient-height bounds are essential.

### Proof: an efficiently bounded common denominator

Let G be the product of the positive denominators of all circuit constants. Every coefficient computed by the circuit belongs to Z[1/G]. Hence every prime in the reduced denominator of any final coefficient divides G.

Because a final denominator is at most 2^H, the exponent of each of its prime divisors is at most H. Therefore every final coefficient denominator divides G^H. This conclusion requires NO integer factorization: G^H is an explicitly computable multiple of all final denominators, with polynomial bit length H log_2 G.

Let q be the product of the coordinate denominators of x. Since deg Q<=d,

    D0=G^H q^d

is a known denominator for Q(x). The integer Z=D0 Q(x) has a polynomial bit bound. For example, the number of degree-at-most-d monomials is binom(D+d,d), coefficient absolute values are at most 2^H and |x_i|<=2^B. Thus

    |Z| <= D0 binom(D+d,d) 2^(H+dB).

Choose an explicit integer H1 strictly larger than the binary logarithm of this bound. Its VALUE is polynomial in the stated parameters.

### Proof: modular evaluation without enormous intermediates

Define the integer modulus

    M=1+2^(H1+2) G q.

Then gcd(M,Gq)=1. Every circuit constant and input-coordinate denominator is invertible modulo M. Evaluate every addition, subtraction and multiplication gate modulo M, starting with these rational residues. Multiply the final residue by D0 modulo M. It is Z modulo M. Since |Z|<2^H1<M/2, its centered residue is the exact integer Z. Return Z/D0.

The modulus has polynomial bit length. Extended Euclid supplies all inverses, and modular gate arithmetic has polynomial bit cost. Primality of M is unnecessary. The proof never forms an enormous exact intermediate. QED.

For P_n the final coefficient height is explicitly polynomial by the parity formula, and the quadratic denominator is known. Consequently uniform polynomial-size division-free rational circuits with polynomial-bit constants computing P_n would imply polynomial-time exact evaluation, hence P=NP (and indeed polynomial-time evaluation of the #P-hard moment in Section 7).

For an alternative circuit-defined polynomial Q_n in Section 4, the same conclusion applies when its final degree, coefficient height, and circuit size/constant heights are polynomially bounded. The coefficient list itself need not be available or short: the circuit and those bounds are enough. The description can consist of polynomially many such sign conditions.

Arbitrary unencoded real constants or gates dividing by input-dependent expressions are NOT silently covered. The lemma is a rational division-free circuit statement; it does not prove a general algebraic-circuit lower bound over arbitrary constants.

## 7. One exact moment evaluation recovers every cut count

This section sharpens value hardness. It does not assume any result about extension complexity.

Define the integer function

    EvalMoment(n,z)=H_n(z)=sum_s <w(s),z>^L,
                       z in Z^D.                     (12)

Its input is n and the full integer vector z in binary. This function belongs to #P: guess s, compute the nonnegative integer v=|<w(s),z>|^L, then guess a sufficiently long binary integer t and accept iff 0<=t<v. Both the bit length of v and the witness length are polynomial in the input, since L=O(n^4). Exactly v witnesses are accepted for each s.

Given a graph G with m edges, write N_j for the number of sign assignments with cut size j. Assume L>=m; padding the graph with isolated vertices ensures this for arbitrary explicitly listed multigraphs, while a simple n-vertex graph already satisfies it. Set

    b0 = 2^[n+L ceil(log2(1+2m))+2],
    z_empty=b0+m,
    z_ij= - multiplicity({i,j}),
    z_i=0.

Then

    H_n(z)=sum_s (b0+2c_G(s))^L
           =sum_(j=0)^L A_j b0^(L-j),
    A_j=binom(L,j)2^j sum_(t=0)^m N_t t^j.            (13)

For every j,

    0<=A_j<=2^n(1+2m)^L<b0.

Thus there are NO carries in (13). Base-b0 digit extraction from the ONE returned integer gives every A_j and therefore the moments

    mu_j=sum_t N_t t^j, j=0,...,m.

Recover N_t by the Lagrange polynomials

    L_t(u)=product_(0<=v<=m,v!=t) (u-v)/(t-v)
           =sum_(j=0)^m ell_(t,j)u^j:
    N_t=sum_(j=0)^m ell_(t,j)mu_j.                    (14)

The input b0 has O(n+L log(m+1)) bits, and the evaluated integer has O(nL+L^2 log(m+1)) bits. These are polynomial. All digit extraction and rational interpolation steps have polynomial bit complexity. Isolated vertices multiply all counts by a known power of two, which is divided out if padding was used.

This recovers the full cut-size distribution from one exact evaluation. In particular it computes

    Z_G=sum_s 2^(number of monochromatic edges)
        =sum_j N_j 2^(m-j)
        =2^(number of connected components) T_G(3,2).

The last equality follows by expanding product_edges(1+1_{same spin}) and summing spins, then using the defining subset expansion of the Tutte polynomial. Jaeger–Vertigan–Welsh prove #P-hardness of T_G(3,2). Therefore (12) is #P-complete under polynomial-time oracle reductions. The reduction can use graphs with explicitly listed parallel edges; padding handles their edge count. Loops contribute a known scalar and can be removed.

Exact rational evaluation of P_n is at least as hard, since subtracting its known quadratic term gives H_n. By scaling z to z/(b0+m), the same conclusion holds for exact rational evaluations at vectors of Euclidean norm at most two, with polynomial-bit rational inputs and outputs.

Thus the constant-value-gap decision hardness and the exact counting hardness are separate assertions: fixed additive accuracy already decides Max Cut, while exact output reveals all cut counts.

## 8. What must change in a successful full breakthrough

This result does not rule out a polynomial-description, uniformly regular family with superpolynomial approximate SDP order. Such a family could have easy membership and still have no small SDP lift; computational and formulation complexity are distinct resources.

It DOES rule out the suggestion that one can simply replace the exponentially summed moment body by a uniformly evaluable nearby polynomial body and retain the present robust transfer, unless P=NP. The new family would need a different source of formulation hardness rather than preserve this membership-hard geometry at the scale of (8).

Accordingly the full desired theorem remains unproved in this continuation. The strongest verified conclusion is the complete route-specific computational obstruction, including robust membership, exact moment counting, and the unconditional expanded-support lower bound. It must not be advertised as an unrestricted impossibility theorem for the overall smooth-body goal, or as a resolution of P versus NP.

## References and provenance

- M. R. Garey, D. S. Johnson, L. Stockmeyer, Some simplified NP-complete graph problems, Theoretical Computer Science 1 (1976), 237–267. DOI: 10.1016/0304-3975(76)90059-1. Its Simple Max Cut NP-completeness is the decision-hardness input.
- F. Jaeger, D. L. Vertigan, D. J. A. Welsh, On the computational complexity of the Jones and Tutte polynomials, Mathematical Proceedings of the Cambridge Philosophical Society 108 (1990), 35–53. DOI: 10.1017/S0305004100068936. Its T_G(3,2) hardness is the counting input.
- Project manuscript 24 supplies the displayed moment polynomial and its separate SDP lower-bound theorem. Only the formula is used here; the membership and counting arguments are independent of the LRS reduction and all earlier counting-based geometric results.

Finite exact checks in the accompanying script verify the query identity and the radix histogram reconstruction on small graphs. They are illustrations of the algebraic proofs, not evidence that closes the different full breakthrough target.
