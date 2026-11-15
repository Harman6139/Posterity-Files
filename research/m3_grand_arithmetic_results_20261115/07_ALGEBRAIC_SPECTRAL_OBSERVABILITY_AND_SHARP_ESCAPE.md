# Checkpoint 07 — algebraic spectral observability across inactive branches

Date: 2026-11-15. This is a new structural recovery theorem in the ORIGINAL rational exact-value model. Unlike constant-rank continuation, it can identify objectives across separating rank-loss hypersurfaces. It is still a subclass theorem: the unrestricted rational conic OPTIMIZATION frontier is not proved or disproved.

## 1. Definitions and the algebraic probe

Fix m,d>=1. Let X_a(x)=X_0+sum_i x_i H_i be a rational symmetric affine pencil with Frobenius-orthonormal H_i. Put

   f_a(x)=dist_F(X_a(x),S_+^m)^2/2,
   p_a(lambda,x)=det(lambda I-X_a(x)),
   R_a(z,x)=det(zI-X_a(x)^2),
   tau_a(x)=tr(X_a(x)^2)=||x||^2+2h_a.x+c_a.

Write F=Q(x_1,...,x_d). Irreducibility below always means irreducibility as a polynomial in the spectral variable OVER F. It must not be confused with absence of an obvious block decomposition, irreducibility of a graph, or generation of a full matrix algebra.

Choose the bounded algebraic probe q of checkpoint 02. Its degree depends only on m,d, and it can lie in any prescribed nonempty rational open ball. Equality of two natural values at q implies equality of their analytic germs at q. The query lies in the maximal-rank locus of every rational pencil of this format. When R_a is irreducible and m>1, det X_a is not identically zero, so X_a(q) is nonsingular.

The number k_a of negative eigenvalues at q is then locally constant. On a neighborhood,

   h_a(x):=2 f_a(x)=sum_(i in S_a) mu_i(x),

where mu_i are the m roots of R_a (the squared eigenvalues), and |S_a|=k_a. One may shrink to a nonempty open subset with distinct squared eigenvalues when using individual roots; the natural value germ itself remains well defined.

## 2. An arithmetic inertia signature

THEOREM A. Suppose R_a is irreducible over F. Let P_a(w,x) be the monic minimal polynomial over F of the local algebraic element h_a=2f_a, and let M_a=deg_w P_a. Write Tr(P_a) for minus the coefficient of w^(M_a-1), the sum of its roots. Then

   Tr(P_a)/M_a = (k_a/m) tau_a.                       (1)

In particular the local negative inertia is determined by the scalar value germ and the known isometry:

   k_a = (m/M_a) [x_1^2] Tr(P_a).                    (2)

The trace polynomial in (1) is a polynomial in x; its quadratic part is (M_a k_a/m)||x||^2. Formula (2) is not a numerical estimator: it is an exact algebraic-information identity.

Proof. Work in a splitting field of R_a over F. Its Galois group acts transitively on the m roots because R_a is irreducible in characteristic zero. Average the conjugates of h_a over the group. Every root mu_i belongs to the image of S_a with probability k_a/m, so the average is (k_a/m)sum_i mu_i=(k_a/m)tau_a. Every distinct conjugate of h_a occurs equally often in this group average. Thus that same average is Tr(P_a)/M_a, proving (1). The known quadratic part of tau_a gives (2). This argument permits different subsets to have the same sum; it does not assume that the group is the full symmetric group. QED.

The case k_a=m gives h_a=tau_a and contains no detailed spectral information; the signature still correctly reports k_a=m. The case k_a=0 similarly reports zero. Neither case is used as a full recovery theorem below.

## 3. One scalar query identifies the full spectral polynomial at extreme mixed inertia

THEOREM B. Consider any class of rational isometric pencils of this fixed format such that:

   (i) R_a is irreducible over F;
   (ii) at the chosen common probe q, k_a is either 1 or m-1.

One exact scalar natural VALUE f_a(q) identifies p_a(lambda,x) globally, and hence identifies f_a globally. The class may include both inertia alternatives, and separating rank-loss hypersurfaces elsewhere are allowed. No global analyticity or constant-rank assumption is made. Consequently, on the weakly infeasible members, unrestricted exact computation after this one query finds an epsilon-approximate point for every epsilon>0.

Proof. Let two candidates a,b give the same value. Their natural value germs, and thus their local algebraic elements h=2f, coincide. Their monic minimal polynomials P are the same.

Equation (2) shows that they have the SAME local negative count k. For k=1, h is a single root of the irreducible polynomial R, so P=R. Thus R_a=R_b.

For k=m-1, h=tau-mu for the sole positive eigenvalue square mu. The affine change of variable preserves irreducibility. Equation (1) recovers tau=Tr(P)/(m-1). Then

   R(z)=(-1)^m P(tau-z),

so again R_a=R_b. This also treats m=2, where the two cases coincide.

In a sufficiently small regular neighborhood, the shared polynomial R supplies the same multiset of squared eigenvalues. For k=1, h selects the square of the unique negative eigenvalue; every other eigenvalue is positive. For k=m-1, tau-h selects the square of the unique positive eigenvalue. In either case the signed eigenvalue multiset is uniquely determined. Coincident squared magnitudes do not change this multiset argument. Therefore p_a(lambda,x)=p_b(lambda,x) on a nonempty open set. Its coefficients are rational polynomials in x, so equality holds globally. Finally the negative squares of the roots of p determine the natural objective everywhere. QED.

This recovers a spectral invariant, not a unique affine coefficient list: isospectral rational pencils can represent the same objective. No oracle can distinguish globally equivalent representations from their values alone.

### Decoder and promises

The query is chosen without the hidden coefficients. A declared rational ball on which all candidates have the stated extreme mixed inertia is sufficient. Alternatively, a known coefficient-height bound and a nonsingular anchor with the promised inertia give a computable small ball by determinant/norm eigenvalue bounds and Weyl perturbation. For the explicit family in Section 6 below, a common ball is displayed directly.

Enumerate rational pencils satisfying the class promises, using exact factorization over the rational-function field and algebraic inertia tests at q; evaluate their algebraic values there and stop at the first match. The true input appears at a finite index. The theorem makes every matching candidate spectrally correct. Real-algebraic point enumeration then finds f<epsilon if inf f=0. Effective polynomial factorization and real-algebraic computation are used only for termination; no polynomial runtime or practical probe degree is claimed.

This is NOT a theorem that the original unrestricted class always has extreme mixed inertia at a known probe, or that all its squared characteristic polynomials are irreducible.

## 4. A broader conditional theorem using subset-sum recovery

For 1<=k<m and 1<=r<=m define the explicit integers

   C_(m,k,r)=sum_(j=1)^k (-1)^(j-1) j^(r-1) binom(m,k-j).   (3)

THEOREM C. The one-query global spectral-identification conclusion also holds on a declared class for which R_a has Galois group S_m over F and

   C_(m,k_a,r) != 0 for every r=1,...,m.              (4)

The class may contain different admissible values of k_a; formula (2) identifies the local inertia from the germ. This is a sufficient criterion, not a classification at the exceptional integer pairs where (4) fails.

Proof that the subset sums are distinct. If two different k-subsets had equal sums, their difference would be a rational linear relation sum_i c_i mu_i=0 with nonconstant coefficients c_i in {-1,0,1}. Choose indices i,j with c_i!=c_j and apply the Galois transposition exchanging mu_i,mu_j. Subtracting the two relations gives (c_i-c_j)(mu_i-mu_j)=0, impossible because an irreducible characteristic-zero polynomial has distinct roots. Hence all k-subset sums are distinct. The full symmetric group acts transitively on them, so

   P(w)=product_(|I|=k) (w-sum_(i in I) mu_i),
   deg P=binom(m,k).

Let s_r=sum_i mu_i^r and S_r=sum_(|I|=k)(sum_(i in I)mu_i)^r. The polynomial P determines all S_r by Newton identities. The following formal generating identity proves the recovery triangularity:

   sum_(r>=0) S_r t^r/r! = [z^k] product_i(1+z exp(t mu_i))
     = [z^k](1+z)^m exp( sum_(r>=1) s_r t^r/r!
                         *sum_(j>=1)(-1)^(j-1)j^(r-1)z^j ).

In the coefficient of t^r, the term involving s_r is linear, with coefficient exactly C_(m,k,r); all remaining terms involve only s_1,...,s_(r-1). Thus

   S_r=C_(m,k,r)s_r+Q_(m,k,r)(s_1,...,s_(r-1)),

where Q is an explicitly computable rational polynomial. Under (4) these equations recover s_1,...,s_m successively, hence recover R by Newton identities.

For two pencils with the same observed germ, Theorem A gives the same k and the preceding reconstruction gives the same R. On an open subset where all k-subset sums are distinct, the common h singles out exactly which squared eigenvalues have negative signs. The remaining roots have positive signs. Their ordinary characteristic polynomials therefore agree on an open set and hence everywhere, as in Theorem B. QED.

For k=1 the coefficients are all one. For k=m-1 the spectrum is recovered simply by complements, as already proved. For k=2,

   C_(m,2,r)=m-2^(r-1),

so (4) holds whenever m is not a power of two. At m=4,k=2, the coefficient for r=3 vanishes; the argument does NOT prove recovery there. The familiar reflection of four numbers mu_i to (sum mu)/2-mu_i preserves their pair sums and explains why a naive unconditional subset-sum inversion would be false. Whether a particular spectral-pencil class rules out such ambiguities requires a separate proof.

The subset-sum generating identity and its coefficients belong to the classical multiset-recovery problem (often called Moser's problem). They are included with proof, not claimed as new combinatorics. The conic consequence is the combination with arithmetic germ decoding, isometric inertia detection, and signed spectral reconstruction.

## 5. A simple irreducibility test for the squared spectrum

LEMMA. If p(lambda) in F[lambda] is monic irreducible, and is not invariant under lambda->-lambda up to its leading sign, then R(z)=product_i(z-lambda_i^2) is irreducible. In particular a nonzero trace coefficient in p suffices.

Proof. For a root lambda, let E=F(lambda) and E0=F(lambda^2). The extension E/E0 has degree at most two. If its degree were two, its nontrivial automorphism would send lambda to -lambda while fixing F. Thus -lambda would also be a root of p, forcing p(-t)=(-1)^m p(t). This contradicts the hypothesis. Hence E=E0, so the square has the same degree m over F; its monic degree-m annihilator R is its minimal polynomial. QED.

This lemma does not equate matrix-algebra irreducibility with polynomial irreducibility.

## 6. Application: sharp-order weak-infeasibility escape with algebraically coupled branches

For n=m-1>=1, use the rational isometric arrow pencil from old checkpoint 02, written first in leaf variables t_1,...,t_n:

   X00=0, X01=1,
   Xii=t_i,
   X0,i+1=2t_i for i<n,
   Xij=0 for distinct positive i,j.

Use coordinates y_i=3t_i for i<n and y_n=t_n. Each first direction has squared norm 1/9+2(4/9)=1, and the last has norm one; supports are disjoint. This is an order-(n+1) rational isometric pencil, not the larger everywhere-nonsingular example of checkpoint 03.

### Polynomial irreducibility

Let a_1=1 and a_i=2t_(i-1) for i>=2. Its characteristic polynomial is

   p_n(lambda)=lambda product_(i=1)^n(lambda-t_i)
                    -sum_(i=1)^n a_i^2 product_(j!=i)(lambda-t_j).

For n=1, it is lambda^2-t_1 lambda-1, irreducible over Q(t_1) by primitivity as a linear polynomial in t_1.

For n>1, regard t_n as the last variable over K=Q(t_1,...,t_(n-1)). Then

   p_n=(lambda-t_n)p_(n-1)
                         -4t_(n-1)^2 product_(i<n)(lambda-t_i).

The two coefficients of this degree-one polynomial in t_n are coprime in K[lambda]. Indeed, p_(n-1)(t_i)=-a_i^2 product_(j<n,j!=i)(t_i-t_j) is nonzero in K for every i<n. Therefore p_(n-1) is coprime to the displayed product. A primitive degree-one polynomial in t_n is irreducible over K(lambda), hence in K[lambda,t_n]; because p_n is monic in lambda, Gauss's lemma gives irreducibility over K(t_n)[lambda]. Its trace sum_i t_i is not zero, so Section 5 proves irreducibility of R_n as well.

### A rational normalization with a common index-one probe ball

Let y_bar=(3,...,3,1), so every t_i=1, and put kappa=1/(10n). Define

   Y_n(x)=kappa X_n(y_bar+x/kappa)=kappa X_n(y_bar)+H x.

The directions remain rational and isometric. The leaf block at x=0 is kappa I. Its Schur complement at the zero top diagonal is strictly negative, so the inertia is exactly (n positive, one negative). The positive eigenvalues are at least kappa by interlacing. The negative eigenvalue has magnitude at least kappa(sqrt(5)-1)/2>kappa/2. Thus ||x||<kappa/4 preserves this inertia, since ||H x||_op<=||x||.

Also ||X_n(y_bar)||_F^2=9n-6, so f_Y(0)<=kappa^2(9n-6)/2<1. Rational orthogonal coordinate changes preserve the same ball, isometry, normalization, and escape profile; rational orthogonal matrix congruences preserve the objective. Polynomial irreducibility is preserved by these invertible rational changes and by the shift/scaling. A common algebraic probe in this ball therefore identifies the full spectral polynomial and natural objective from ONE scalar value for the entire declared rational-chart family, independently of coefficient heights.

### True PSD-distance escape, including all perturbations

Write E_i=2^i-1 and E=E_n. For the unshifted pencil, if dist_F(X_n(y),S_+)<=delta<=1/2, then X_n(y)+delta I is PSD. Its two-by-two principal minors give

   t_1+delta>=1/delta,
   t_i+delta>=4t_(i-1)^2/delta, 2<=i<=n.

Induction gives t_i>=(1/2)delta^(-E_i), hence ||y||>=t_n>=(1/2)delta^-E. This bounds all approximate points, not only an explicit curve.

Conversely, for 0<e<=1 choose t_1=n/e and recursively t_i=4n t_(i-1)^2/e. The Schur sum of X_n(y)+eI is at most

   sum_i X0i^2/t_i=e.

Its top diagonal is e, so X_n(y)+eI is PSD. The distance is at most sqrt(n+1)e and the coordinate norm is O_n(e^-E). Taking e=delta/sqrt(n+1) proves matching radius growth Theta_n(delta^-E). Exact feasibility is impossible because the top zero diagonal and X01=1 contradict PSD. Thus the infeasibility is weak.

Changing the coordinate anchor by y_bar alters radii by at most ||y_bar||, and multiplying matrices by kappa rescales residuals by kappa. The exponent is unchanged. Therefore

   rho_(f_Y)(s)=Theta_n(s^(-(2^n-1)/2)).                (5)

The constants and onset are fixed once n is fixed and are uniform over all sampled rational orthogonal charts. Equation (5) reaches the sharp fast-escape exponent of the earlier order-m envelope, now together with the one-query algebraic observability conclusion. The original algorithm-specific projection/acceleration slow rates still apply, but they are not lower bounds on this unrestricted exact information model.

### These pencils really can change rank and negative index

At n=2 the determinant is -t_2. Crossing t_2=0 changes the negative count from one (t_2>0) to two (t_2<0), while the negative eigenvalue already forced by the first two rows remains. At t_2=0 the zero eigenvalue crosses with nonzero speed; its negative-part square introduces a genuine second-derivative discontinuity. Thus this recovery application is not merely a restatement of globally analytic recovery. Irreducibility couples the inactive branch algebraically to the observed one.

## 7. What has actually been learned about the main frontier

There are now TWO distinct rigorous ways in which rational branch hiding fails:

1. Analytic continuation through a connected common regular locus, including the codimension-two theorem of checkpoint 05.
2. Algebraic spectral coupling: a local negative-energy germ determines the full squared spectrum and the sign selection under Theorem B or C, even when regular chambers are separated.

Neither theorem covers all rational pencils. Reducible spectral polynomials, intermediate subset-sum ambiguities, and probes at which all eigenvalues are negative can lose information. The fixed-prior optimization theorem would have to overcome these recovery mechanisms while making the remaining ambiguity essential to near-feasibility. The identification-hard family in checkpoint 01 remains optimization-trivial.

Thus the entire rational exact-arithmetic OPTIMIZATION frontier is still unresolved. No full grand theorem, upper-quintile ranking, or independent external verification is claimed.