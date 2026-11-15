# Checkpoint 07 — algebraic spectral observability across inactive branches

Date: 2026-11-15. Audited revision. This is a structural recovery theorem in the ORIGINAL rational exact-value model. Unlike constant-rank continuation, it can identify objectives across separating rank-loss hypersurfaces. It is still a subclass theorem: the unrestricted rational conic OPTIMIZATION frontier is not proved or disproved.

Revision note: the final order-three example in the initial commit incorrectly stated det X=-t_2. The correct determinant is -t_2-4t_1^3, and at t_1=1 the rank crossing is t_2=-4. Section 6 now gives the corrected null vector and crossing speed. None of the general recovery or escape proofs uses that erroneous illustrative determinant. The original version remains in Git history.

## 1. Definitions and the algebraic probe

Fix m,d>=1. Let X_a(x)=X_0+sum_i x_i H_i be a rational symmetric affine pencil with Frobenius-orthonormal H_i. Put

   f_a(x)=dist_F(X_a(x),S_+^m)^2/2,
   p_a(lambda,x)=det(lambda I-X_a(x)),
   R_a(z,x)=det(zI-X_a(x)^2),
   tau_a(x)=tr(X_a(x)^2)=||x||^2+2h_a.x+c_a.

Write F=Q(x_1,...,x_d). Irreducibility below always means irreducibility as a polynomial in the spectral variable OVER F. It must not be confused with absence of an obvious block decomposition, irreducibility of a graph, or generation of a full matrix algebra.

Choose the bounded algebraic probe q of checkpoint 02. Its degree depends only on m,d, and it can lie in any prescribed nonempty rational open ball. Equality of two natural values at q implies equality of their analytic germs at q. The query lies in the maximal-rank locus of every rational pencil of this format. When R_a is irreducible and m>1, det X_a is not identically zero, so X_a(q) is nonsingular.

The number k_a of negative eigenvalues at q is locally constant. On a neighborhood,

   h_a(x):=2 f_a(x)=sum_(i in S_a) mu_i(x),

where mu_i are the m roots of R_a (the squared eigenvalues), and |S_a|=k_a. One may shrink to a nonempty open subset with distinct squared eigenvalues when using individual roots; the natural value germ itself remains well defined.

## 2. An arithmetic inertia signature

THEOREM A. Suppose R_a is irreducible over F. Let P_a(w,x) be the monic minimal polynomial over F of the local algebraic element h_a=2f_a, and let M_a=deg_w P_a. Write Tr(P_a) for minus the coefficient of w^(M_a-1), the sum of its roots. Then

   Tr(P_a)/M_a = (k_a/m) tau_a.                       (1)

In particular the local negative inertia is determined by the scalar value germ and the known isometry:

   k_a = (m/M_a) [x_1^2] Tr(P_a).                    (2)

The trace polynomial in (1) is a polynomial in x; its quadratic part is (M_a k_a/m)||x||^2. Formula (2) is an exact algebraic-information identity, not a numerical estimator.

Proof. Work in a splitting field of R_a over F. Its Galois group acts transitively on the m roots because R_a is irreducible in characteristic zero. Average the conjugates of h_a over the group. Every root mu_i belongs to the image of S_a with probability k_a/m, so the average is (k_a/m)sum_i mu_i=(k_a/m)tau_a. Every distinct conjugate of h_a occurs equally often in this group average. Thus the same average is Tr(P_a)/M_a. The known quadratic part of tau_a gives (2). The argument permits different subsets to have the same sum and does not assume a full symmetric Galois group. QED.

The case k_a=m gives h_a=tau_a and contains no detailed spectral information; the signature still reports k_a=m. The case k_a=0 similarly reports zero. Neither is used as a full recovery theorem below.

## 3. One scalar query identifies the full spectral polynomial at extreme mixed inertia

THEOREM B. Consider a class of rational isometric pencils of this fixed format such that R_a is irreducible over F and, at the chosen common probe q, k_a is either 1 or m-1. One exact scalar natural VALUE f_a(q) identifies p_a(lambda,x) globally, hence identifies f_a globally. Both inertia alternatives may occur in the class, and separating rank-loss hypersurfaces elsewhere are allowed. No global analyticity or constant-rank assumption is made. For weakly infeasible members, unrestricted exact computation after this one query finds an epsilon-approximate point for every epsilon>0.

Proof. Two candidates with the same value have the same natural value germ and therefore the same monic minimal polynomial P of h=2f. Equation (2) gives the SAME local negative count k. For k=1, h is a root of irreducible R, so P=R. For k=m-1, h=tau-mu for the sole positive eigenvalue square mu. This affine substitution preserves irreducibility. Equation (1) recovers tau=Tr(P)/(m-1), and

   R(z)=(-1)^m P(tau-z).

Thus the two squared characteristic polynomials agree. This also treats m=2.

Near q the shared polynomial R supplies the same squared eigenvalue multiset. For k=1, h selects the square of the unique negative eigenvalue; all other eigenvalues are positive. For k=m-1, tau-h selects the square of the unique positive eigenvalue. The signed eigenvalue multiset is therefore determined. Coincident squared magnitudes do not alter this multiset conclusion. The ordinary characteristic polynomials agree on a nonempty open set, so their rational polynomial coefficients agree globally. Their negative-square sums determine f everywhere. QED.

This identifies a spectral invariant, not a unique affine coefficient list. Globally isospectral rational pencils and other equivalent representations cannot be distinguished from natural values alone.

### Decoder and promises

A declared rational ball on which all candidates have the stated extreme mixed inertia is sufficient for choosing q without the hidden coefficients. Alternatively, a known coefficient-height bound and a nonsingular anchor with the promised inertia give a computable small ball by determinant/norm eigenvalue bounds and Weyl perturbation. Section 6 supplies an explicit common ball.

Enumerate rational pencils satisfying the class promises, using exact factorization over the rational-function field and algebraic inertia tests at q. Evaluate each algebraic natural value and stop at the first match. The true input occurs at a finite index; every match has the correct spectral polynomial. Rational-point enumeration then finds f<epsilon when inf f=0. Factorization and real-algebraic computation are used for termination only: no polynomial runtime or practical probe degree is claimed.

The full unrestricted class need not have extreme mixed inertia at a known probe, and its squared characteristic polynomial need not be irreducible.

## 4. A broader sufficient criterion using subset-sum recovery

For 1<=k<m and 1<=r<=m define

   C_(m,k,r)=sum_(j=1)^k (-1)^(j-1) j^(r-1) binom(m,k-j).   (3)

THEOREM C. The same one-query global spectral-identification conclusion holds on a declared class for which R_a has Galois group S_m over F and

   C_(m,k_a,r) != 0 for all r=1,...,m.                (4)

The class can contain different admissible k_a; equation (2) identifies the local inertia. This is a sufficient criterion, not a classification when some coefficient vanishes. The information-uniqueness statement does not depend on an efficient algorithm for testing a Galois-group promise.

Proof. Distinct k-subsets have distinct sums in the splitting field. Otherwise their difference yields sum_i c_i mu_i=0 with nonconstant integer coefficients c_i. Choose i,j with c_i!=c_j and apply the Galois transposition exchanging these roots. Subtracting gives (c_i-c_j)(mu_i-mu_j)=0, contradicting separability. The full symmetric group acts transitively on k-subsets. Hence

   P(w)=product_(|I|=k) (w-sum_(i in I) mu_i),
   deg P=binom(m,k).

Put s_r=sum_i mu_i^r and S_r=sum_(|I|=k)(sum_(i in I)mu_i)^r. Newton identities recover S_r from P. The formal identity

   sum_(r>=0) S_r t^r/r! = [z^k] product_i(1+z exp(t mu_i))
     = [z^k](1+z)^m exp( sum_(r>=1) s_r t^r/r!
                         *sum_(j>=1)(-1)^(j-1)j^(r-1)z^j )

shows that

   S_r=C_(m,k,r)s_r+Q_(m,k,r)(s_1,...,s_(r-1)),

where Q is an explicitly computable rational polynomial. Under (4), recover s_1,...,s_m successively and then R by Newton identities. For two pencils sharing the observed germ, equation (2) gives the same k, and this reconstruction gives the same R. On a nonempty open subset, all its k-subset sums are distinct; h selects exactly the squared eigenvalues with negative signs. The resulting ordinary characteristic polynomials agree on an open set and thus globally, as in Theorem B. QED.

For k=1 all coefficients are one. For k=m-1 direct complementation recovers the spectrum. For k=2,

   C_(m,2,r)=m-2^(r-1),

so (4) holds when m is not a power of two. At m=4,k=2,r=3, it vanishes. Reflection of four numbers mu_i to (sum mu)/2-mu_i preserves the multiset of pair sums, so an unconditional subset-sum inversion would be false. Whether an affine spectral-pencil class excludes such ambiguities requires further proof.

The generating identity and coefficients belong to classical multiset recovery, often called Moser's problem; they are not claimed as new combinatorics. The conic synthesis is arithmetic germ decoding, isometric inertia detection, and signed spectral reconstruction. Primary literature includes Dmitri Fomin's survey, DOI 10.1080/00029890.2019.1577088, arXiv:1709.06046, and Moser Polynomials and Eulerian Numbers, arXiv:1903.04062. The exact publication history of the underlying recovery criterion is being audited.

## 5. A simple irreducibility test for the squared spectrum

LEMMA. If monic p(lambda) in F[lambda] is irreducible and p(-lambda)!=(-1)^m p(lambda), then R(z)=product_i(z-lambda_i^2) is irreducible. A nonzero trace coefficient of p suffices.

Proof. For a root lambda, let E=F(lambda) and E0=F(lambda^2). The degree [E:E0] is at most two. If it were two, the nontrivial automorphism would send lambda to -lambda and fix F. Thus -lambda would also be a root of p, forcing the excluded parity identity. Hence E=E0, so lambda^2 has degree m over F, and its monic degree-m annihilator R is its minimal polynomial. QED.

This does not identify matrix-algebra irreducibility with polynomial irreducibility.

## 6. Sharp-order weak-infeasibility escape with coupled spectral branches

For n=m-1>=1, use the rational isometric arrow pencil from old checkpoint 02, first in leaf variables t_1,...,t_n:

   X00=0, X01=1, Xii=t_i,
   X0,i+1=2t_i for i<n,
   Xij=0 for distinct positive i,j.

Set y_i=3t_i for i<n and y_n=t_n. Each first direction has squared norm 1/9+2(4/9)=1; the last has norm one, with disjoint supports. This has order n+1, unlike the larger constant-rank ladder in checkpoint 03.

### Irreducibility

Let a_1=1 and a_i=2t_(i-1) for i>=2. Then

   p_n(lambda)=lambda product_(i=1)^n(lambda-t_i)
                    -sum_(i=1)^n a_i^2 product_(j!=i)(lambda-t_j).

For n=1, p_1=lambda^2-t_1 lambda-1 is primitive and linear in t_1, hence irreducible over Q(t_1)[lambda]. For n>1, work over K=Q(t_1,...,t_(n-1)) and write

   p_n=(lambda-t_n)p_(n-1)
                         -4t_(n-1)^2 product_(i<n)(lambda-t_i).

The coefficients in t_n are coprime in K[lambda], since

   p_(n-1)(t_i)=-a_i^2 product_(j<n,j!=i)(t_i-t_j) != 0

for every i<n. Therefore this primitive degree-one polynomial in t_n is irreducible in K[lambda,t_n]. Being monic in lambda, it is irreducible over K(t_n)[lambda] by Gauss's lemma. Its trace sum_i t_i is nonzero, so the squared-spectrum polynomial is irreducible by Section 5.

### Normalization and a common index-one ball

Let y_bar=(3,...,3,1), so all t_i=1, and kappa=1/(10n). Set

   Y_n(x)=kappa X_n(y_bar+x/kappa)=kappa X_n(y_bar)+H x.

The directions remain rational and isometric. At x=0 the leaf block is kappa I and the top Schur complement is negative, so the inertia is (n positive, one negative). Interlacing gives positive eigenvalues at least kappa; the negative eigenvalue magnitude is at least kappa(sqrt(5)-1)/2>kappa/2. Since ||Hx||_op<=||x||, the ball ||x||<kappa/4 preserves this inertia.

The identity ||X_n(y_bar)||_F^2=9n-6 gives f_Y(0)<=kappa^2(9n-6)/2<1. Rational orthogonal coordinate changes preserve the ball, isometry, normalization, and radius profile. Rational orthogonal congruences preserve the objective. Invertible rational coordinate changes and the displayed shift/scaling preserve polynomial irreducibility. Thus one common algebraic probe identifies the full spectral polynomial and natural objective throughout this rational-chart family, independently of coefficient heights.

### True-distance escape under arbitrary perturbations

Put E_i=2^i-1 and E=E_n. If dist_F(X_n(y),S_+)<=delta<=1/2, then X_n(y)+delta I is PSD. The two-by-two principal minors imply

   t_1+delta>=1/delta,
   t_i+delta>=4t_(i-1)^2/delta, 2<=i<=n.

Induction gives t_i>=(1/2)delta^(-E_i), hence ||y||>=t_n>=(1/2)delta^-E. This applies to every approximate point.

For the upper bound take 0<e<=1, t_1=n/e, and t_i=4n t_(i-1)^2/e. The Schur sum of X_n(y)+eI is at most sum_i X0i^2/t_i=e, so that shifted matrix is PSD. Its residual is at most sqrt(n+1)e and its coordinate norm is O_n(e^-E). This proves matching minimum-radius growth Theta_n(delta^-E). The top zero diagonal and X01=1 preclude exact PSD feasibility, so the infeasibility is weak.

The shift of coordinate anchor changes minimum radii by at most ||y_bar|| and positive scaling rescales residuals. Consequently

   rho_(f_Y)(s)=Theta_n(s^(-(2^n-1)/2)).               (5)

Constants and onset are fixed for each n and uniform over rational orthogonal charts. This attains the fast-escape endpoint of the previous order-m envelope while remaining one-query observable. Slow rates for specified projection/acceleration trajectories remain algorithm-specific, not lower bounds on unrestricted exact information.

### Corrected order-three rank-changing example

For n=2,

   X=[[0,1,2t_1],[1,t_1,0],[2t_1,0,t_2]],
   det X=-t_2-4t_1^3.

At t_1=1, the rank crossing is t_2=-4. The leading two-by-two block has one eigenvalue of each sign. Its Schur complement for the final coordinate is t_2+4. Thus there is one negative eigenvalue when t_2>-4 and two when t_2<-4. At the crossing, (2,-2,1) is a null vector of squared norm 9. The crossing eigenvalue has derivative 1/9 with respect to t_2, since the derivative matrix is E_33. Its negative-part square contributes (t_2+4)_-^2/162 to leading order in the natural objective, with second-derivative jump 1/81; all other eigenvalue contributions are analytic nearby. The objective is therefore genuinely not C2 across this separating rank barrier.

This application is not merely a globally analytic recovery theorem. Algebraic irreducibility connects the formerly inactive spectral branch to the observed one.

## 7. Main-frontier status

Two mechanisms now rigorously defeat rational branch hiding:

1. Analytic continuation on a connected common regular locus, including codimension-two recovery in checkpoint 05.
2. Algebraic spectral coupling under Theorem B or C, even across separating rank-loss hypersurfaces.

Neither covers all rational pencils. Reducible spectral polynomials, intermediate subset-sum ambiguities, and fully negative or positive observations can lose information. A fixed-prior optimization lower bound must defeat these mechanisms while making the remaining ambiguity essential to finding near-feasible points. Checkpoint 01's identification-hard family is optimization-trivial.

The full rational exact-arithmetic OPTIMIZATION frontier remains unresolved. The finite exact symbolic verification script checks 286 identities and small instances; it is supporting evidence, not a universal proof or independent peer review. No grand-theorem completion or upper-quintile publication claim is made.