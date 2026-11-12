# Fresh analytic milestone 03 — conditioning, exact representation, and recovery guarantees

Date: 2026-11-12. Companion to the explicit normal-form proof in 02_UNIVERSAL_QUADRATIC_TWO_BASIS_NORMAL_FORM.md, proof commit 9030a69bab7f5358065f836a826e9f5a9bbe2c86.

## 1. Scope and computational model

The source consists of rational symmetric matrices A_1,...,A_p of order m>=1, rational data b, and, for optimization, a rational symmetric cost C. Trace control means that range(A*) meets the positive-definite cone. It does NOT mean that the feasible source fibre has a positive-definite point.

Two precisely distinguished input models are supported.

**Certificate-input model.** A rational vector z with H=A*z>0 is included. The construction in 02 takes polynomial time in the ordinary bit length of A,z,b,C and produces polynomial-size exact arithmetic/radical expressions. The correctness and positive-definiteness of the certificate can be checked by rational arithmetic.

**Conditioned certificate-search model.** Only rational A is supplied, with the promise of trace control. Section 6 gives a self-contained rational algorithm to find a certificate. Its running time is polynomial in the input bit length, m,p, and a specified numerical inverse margin kappa. This is a polynomial-CONDITIONED algorithm, not an assertion of an unconditioned polynomial-time exact SDP solver. Once the certificate is found, the first model applies.

Exact output coefficients use rational arithmetic and square roots of positive rational numbers, recorded by a shared expression graph. This is an explicit exact algebraic representation. We do not expand a potentially large multiquadratic number field into minimal polynomials. Polynomial-size expression graphs, and arbitrary-precision evaluation of them, are the declared representation model.

The mathematical existence theorem covers every trace-controlled rational A, whether or not its trace-control certificate was supplied. Positivity is an open condition; therefore even if trace control was initially witnessed only by algebraic or real coefficients, a rational certificate exists. Section 6 finds one with the stated conditioning dependence.

## 2. Explicit norms and scaling

Retain all definitions from 02:

  H=A*z>0, rho=tr(H^(-1)) or any positive rational rho with rho H>=I,
  alpha=m rho^2, tau=z.b,
  N=9m^2+4m+3+2p,
  S_A=sum_i ||A_i||_F^2,
  L=4m^2+6m+2p+6+2S_A,
  T=33m^2+10m+9+8p,
  K_r=3 sqrt(2) L (1+sqrt(T)) sqrt(9S_A/16+p/8).

Then ||D||_(F->F)=1, ||D*C||_F=||C||_F, and

  ||A(D(Y))-b||_2 <= K_r ||B_U(Y)-Phi b||_2        for every Y>=0.  (1)

This bound does not involve the minimum positive eigenvalue of any feasible point, the source singularity degree, a facial-reduction gap, or an inverse singular value of A. Matrix magnitudes remain explicit in S_A. Under ordinary row normalization of A, K_r is a polynomial in m and p. For unnormalized input it is a polynomial in the displayed source magnitudes.

### Forward encoder norm

For arbitrary symmetric X put t=<H,X>, B=X-rho t I/2. Directly from the two blocks of J in 02,

  ||E(X)||_F^2=||J(X)||_F^2
    =4||B||_F^2+(m rho^2/2+1+m^2 alpha^2)t^2.

The equality ||F^T Z F||_F=||Z||_F used here follows from FF^T=I. Applying

  ||B||_F^2 <= 2||X||_F^2+(m rho^2/2)t^2

gives the explicit bound

  ||E||_(F->F) <= K_E
   :=sqrt(8+[(5/2)m rho^2+1+m^2 alpha^2]||H||_F^2).        (2)

### Data map norm

Define

  C_0=2+[1+rho+alpha+alpha S_A+rho sqrt(m S_A)]||z||_2,
  K_f=sqrt(2N) C_0.

Every unscaled raw target row in 02 has Euclidean coefficient norm at most C_0. For the source-equation pair this follows from

  c_(i,+/-)^0(b)
   =[1+alpha||A_i||_F^2 +/-(-rho tr A_i)] z.b +/-2b_i

and |tr A_i|<=sqrt(m)||A_i||_F. The coordinate, base-block, and copy rows satisfy the same bound immediately. Every completion column h has ||h||^2<=1 because hh^T<=I-epsilon Q_0<=I, so its target row also satisfies that bound. All subsequent measurement weights are at most one. There are 2N final data coordinates. Thus

  ||Phi||_(2->2) <= K_f.                                 (3)

A sharper bound is available simply by computing the Frobenius norm of the explicit rational matrix Phi. The rough formula (3) suffices for polynomial conditioning.

Together with B_U E=Phi A and DE=id, equations (1)–(3) imply

  ||B_U(E(X))-Phi b|| <= K_f ||A(X)-b||    for all symmetric X.   (4)

## 3. Feasible-set distance and approximate optimization

Assume F_b={X>=0:A(X)=b} is nonempty. Then tau>=0 and every PSD source competitor with residual at most t obeys

  ||X||_F <= tr X <= rho <H,X>
           =rho z.A(X) <= rho(tau+||z||_2 t).              (5)

Consequently all bounded-residual source sets are bounded. The fibre F_b is compact. Its recovery modulus

  omega_b(t)=sup {dist_F(X,F_b):X>=0, ||A(X)-b||_2<=t}

is finite for every finite t, and omega_b(t)->0 as t decreases to zero.

**Proof of the latter assertion.** Otherwise there would be t_j->0 and PSD X_j with residual <=t_j but distance at least a fixed positive number. Bound (5) supplies a convergent subsequence. Its limit is PSD and satisfies A(X)=b, contradicting that distance bound. No uniqueness or relative-interior hypothesis is used.

For EVERY ambient PSD Y, with delta=||B_U(Y)-Phi b||, the contraction decoder and (1) give

  dist_F(D(Y),F_b) <= omega_b(K_r delta).                  (6)

This is a statement about decoded source distance for the entire ambient PSD cone. In particular, whenever the source has a justified error bound omega_b(t)<=M_b t^theta on 0<=t<=t_0, the same exponent transfers:

  dist_F(D(Y),F_b)<=M_b K_r^theta delta^theta,
  0<=delta<=t_0/K_r.

There is no additional exponent halving from the compiler. M_b and theta remain the actual source constants; no fake rank-uniform conditioning is asserted for degenerate SDPs.

Let T_b={Y>=0:B_U(Y)=Phi b} be the ENTIRE lifted fibre. For points on the encoder image, both ambient-distance bounds are available:

  dist_F(X,F_b) <= dist_F(E(X),T_b)
                <= K_E dist_F(X,F_b),        X>=0.        (7)

The first inequality follows from ||D||=1, DE=id and D(T_b)=F_b. For the second, choose a nearest feasible source X_0 and use E(X_0) in T_b. Equation (7) is not an upper bound for arbitrary ambient Y; such a stronger assertion is unnecessary for the quotient normal form.

### Approximate optimization

Let v=min_{X in F_b}<C,X>. It is attained by compactness. The lifted problem with cost C_tilde=D*C has exactly the same feasible objective-value set and optimum. Define

  v_delta=inf {<C_tilde,Y>:Y>=0, ||B_U(Y)-Phi b||<=delta}.

Then

  v-||C||_F omega_b(K_r delta) <= v_delta <= v.            (8)

To prove the lower bound, decode any admissible Y, choose a nearest X_0 in F_b, and apply (6) and Cauchy–Schwarz. The upper bound follows from an exact lift of a source optimizer. If Y is epsilon-optimal for this relaxed lifted problem, it decodes to a PSD source point with residual <=K_r delta, with exactly the same objective value, and some feasible source point X_0 satisfies

  <C,X_0> <= v+epsilon+||C||_F omega_b(K_r delta).

This is an existence/error guarantee, not a claim that computing the exact nearest feasible point needs no optimization.

At b=0, trace control forces F_0={0}; equation (5) gives omega_0(t)<=rho||z||t. The zero-data case therefore has a linear decoded recovery bound under the very same formulas.

## 4. Infeasible data and weak-feasibility gaps

The construction and global residual inequality are defined for arbitrary rational b, not only feasible data. Put

  r_src(b)=inf_{X>=0}||A(X)-b||_2,
  r_lift(b)=inf_{Y>=0}||B_U(Y)-Phi b||_2.

Positivity of D and (1) give r_src<=K_r r_lift. Positivity of E and (4) give the reverse bound with the forward constant:

  r_src(b)/K_r <= r_lift(b) <= K_f r_src(b).               (9)

Thus an approximate YES witness with source residual <=eta lifts with residual <=K_f eta. A NO promise r_src>=gamma transfers to r_lift>=gamma/K_r. These are explicit weak-feasibility promises, including inconsistent source data. Exact infeasibility is preserved by the entire-fibre theorem in 02.

In this trace-controlled setting A(S_+^m) is closed: if A(X_j) converges with X_j>=0, then tr X_j<=rho z.A(X_j) is bounded, so a subsequence converges to a PSD preimage of the limiting datum. Hence an infeasible fixed datum has strictly positive r_src. This observation does NOT supply a uniform lower bound on that gap in terms of input length, nor an unconditioned polynomial-time exact feasibility decision algorithm.

The two-basis PSD image is also closed: convergence of its first diagonal list bounds trace and hence bounds every PSD preimage. There is no appeal to the false general statement that every linear image of a PSD cone is closed.

## 5. Bit complexity and numerical evaluation of the exact design

All steps before frame factorization are rational arithmetic: form H, invert H, compute rho and alpha, build raw vectors, the rational frame operator Q_0, epsilon=1/(2L), and R_c=I-epsilon Q_0. The completion matrix satisfies

  (1/2)I <= R_c <= I.                                    (10)

Its nontrivial block is the k-by-k auxiliary block, k=m^2. Compute its rational LDL^T decomposition without pivoting. Each pivot is positive; in fact all pivots lie in [1/2,1]. To see the lower bound for a successive Schur complement, minimize the quadratic form of a positive matrix bounded below by I/2 over its eliminated coordinates. The minimum is still at least half the squared norm of the remaining coordinates. The upper bound follows by choosing eliminated coordinates zero. The same bounds propagate through elimination.

The LDL coefficients are rational quotients of minors. If the rational entries initially have bit length B_0, clearing denominators and applying the elementary determinant expansion bounds their numerator and denominator bit lengths by a polynomial in k and B_0. Rational Gaussian elimination, with exact reduction of fractions or a fraction-free implementation, therefore takes polynomially many bit operations. The same argument applies to computing H^(-1), with its actual input bit length included.

For a completion block R_c=L_c diag(d_j)L_c^T, use columns

  h_j=sqrt(d_j) (L_c)_:j.

Every d_j is a positive rational; ||h_j||^2=d_j||(L_c)_:j||^2 is rational. The only additional roots are sqrt(epsilon), sqrt(2/3), 1/sqrt(3) and 1/sqrt(2), and the scalar completion roots. It follows that G,F,U=2F^TF-I,V,E and D have polynomial-size exact radical expression graphs, while c(b), Phi, and Phi b are rational with polynomial bit length. Dense output matrices have order polynomial in the input dimensions, so listing these expressions explicitly also has polynomial total size.

This assertion is NOT a claim that the minimal polynomial of every entry, or the degree of the joint number field, is polynomial. Expanding that field is neither part of the representation nor needed for evaluating the construction. All polynomial identities used to establish orthogonality and positivity are certified by the rational factorization and the displayed matrix formulas.

Square roots of positive rational numbers can be evaluated to an additional s binary digits by bisection/Newton iteration using polynomially many bit operations in their input lengths and s. The factorization gap (10) prevents small completion pivots. Bounds (1)–(5) make every required accuracy and scale explicit.

For example, suppose a numerical evaluation U_hat has ||U_hat-U||_op<=eta. For any symmetric Y,

  ||diag(U_hat^T Y U_hat)-diag(U^T Y U)||_2
       <=(2eta+eta^2)||Y||_F.                             (11)

This follows by expanding with E_U=U_hat-U and using ||U||=1 and the Frobenius contraction of diagonal extraction. The same estimate controls the error of V_hat Y V_hat^T when ||V_hat-V||_op<=eta. The latter approximate decoder remains PSD-positive exactly, since it is still a compression by a real matrix.

For feasible b, the exact first target diagonal has sum

  s_b=(m rho+1+m^2 alpha)tau.

Every ambient PSD Y with residual at most delta has

  ||Y||_F<=tr Y<=s_b+sqrt(N)delta.                         (12)

Thus design-evaluation error eta adds at most (2eta+eta^2)(s_b+sqrt(N)delta) to the second-list residual, and the analogous explicit decoded-source/objective error. Entrywise evaluation to Frobenius error eta ensures the stated operator error. The required precision is polynomial in the exact expression/input bit lengths and in log(1/eta); desired output tolerances are obtained by substituting the displayed K_r,K_f,K_E,s_b and objective norms.

The exact symbolic U is orthogonal. A rounded matrix U_hat need not be; equation (11) is a perturbation/evaluation guarantee, not a false assertion that arbitrary rounded columns are exactly orthonormal. Exact coefficients or the certified defining factorization specify the mathematical bases.

## 6. Finding a trace-control certificate without a supplied one

This section gives an elementary rational algorithm and complete termination proof. It is included to avoid silently restricting the existence theorem to problems furnished with a certificate.

Let

  B_A=1+sum_{i,j,h}|(A_i)_(j,h)|,
  A_bar=A/B_A.

Then ||A_bar*||_(2->F)<=1. Define the normalized positive-cone margin

  gamma=max_{||u||_2<=1} lambda_min(A_bar*u),
  kappa=1/gamma.

Trace control is exactly gamma>0, and 0<gamma<=1, so kappa>=1. This is an explicit conditioning quantity of the measurement space. The algorithm need not know gamma or kappa.

### The rational rounded update algorithm

For q=1,2,4,..., restart w=0. Use at most T_q=16q^2 updates in this stage. At each update:

1. Test by exact rational symmetric elimination whether A_bar*w-I is positive definite. If it is, output z=w/B_A, so A*z=A_bar*w>I, and stop.
2. Otherwise produce a nonzero rational vector v with v^T(A_bar*w-I)v<=0.
3. Form the rational vector u with coordinates

     u_i=(v^T A_bar_i v)/(v^T v).

4. Round each coordinate of u to a nearest multiple of 1/(100 p q^2), obtaining u', and replace w by w+u'.

If the stage exhausts its updates, double q and restart.

The elementary rational elimination in step 2 is constructive. A negative diagonal pivot gives a negative direction after undoing the rational congruence. A zero diagonal with a nonzero offdiagonal entry gives a rational two-coordinate vector of negative quadratic value. If all remaining entries vanish, a rational null vector suffices. If every pivot is positive, the matrix is positive definite. Congruence elimination and the required directions involve rational coefficients whose bit lengths are bounded by rational minor bounds; there is no numerical eigenvalue-sign test.

### Termination and update bound

At each failed test, ||u||_2<=1 and w.u<=1. Write e=u'-u; the chosen mesh ensures

  ||e||_2<=epsilon_q:=1/(100q^2).

Let z_* be a maximizer in the definition of gamma. For every unit vector v/||v||,

  z_*.u >= gamma,

and therefore z_*.u'>=gamma-epsilon_q. Suppose q>=kappa and the stage did not terminate through T=T_q updates. Starting at w_0=0 gives

  ||w_T||_2 >= z_*.w_T >= T(gamma-epsilon_q) >=0.99 T/q.   (13)

On the other hand ||w_j||<=j(1+epsilon_q), and

  ||w_(j+1)||^2
   <=||w_j||^2+2+2||w_j||epsilon_q+(1+epsilon_q)^2.

Summing for j=0,...,T-1 gives

  ||w_T||^2
   <=T[2+(1+epsilon_q)^2]
      +epsilon_q(1+epsilon_q)T(T-1)
   <3.2T.                                                (14)

But (13), together with T=16q^2, gives ||w_T||^2>=15.6816T, contradicting (14). Thus the first stage with q>=kappa must terminate. Its q is less than 2kappa except for the harmless initial equality case. The total update count over all doubling stages is O(kappa^2).

Every w in a stage lies on the stated rational mesh and has norm at most 16q^2(1+epsilon_q). The bit lengths of its coefficients are O(log p+log q), apart from fixed encoding conventions. The separation witness and u have bit lengths polynomial in the source input length, m,p,log q; rounding resets the update denominator and prevents iterative denominator blow-up. Thus the entire algorithm uses polynomially many bit operations in the input length, m,p,kappa.

The output satisfies, conservatively,

  H=A*z>I,
  ||H||_F<=65kappa^2,
  ||z||_2<=65kappa^2/B_A,
  rho=tr H^(-1)<m,
  alpha=m rho^2<m^3.                                     (15)

All forward encoding and data-map constants are consequently polynomial in the declared normalized inverse margin and source magnitudes. Reverse soundness (1) was already independent of this certificate condition.

The dependence polynomial in numerical kappa, rather than an unproved polynomial in log kappa or in input length alone, is intentional. No assertion that every trace-controlled rational system has a uniformly well-conditioned trace certificate is needed.

## 7. Final quantitative interpretation

Combining 02 and this supplement gives one explicit construction for every dimension, every trace-controlled rational measurement operator, every datum, every feasible rank and singularity degree, and every objective:

- order N=9m^2+4m+3+2p;
- two complete real orthonormal bases;
- a globally PSD-positive contraction decoder;
- exact surjection of the ENTIRE lifted feasible fibre onto the source fibre;
- an explicit globally positive linear encoder of every source PSD point, without asserting bijectivity of feasible fibres;
- exact objectives and norm-preserving cost pullback;
- global all-PSD residual control with a displayed polynomial constant;
- source-distance and approximate-optimization bounds through the actual source recovery modulus;
- two-sided weak-feasibility gap transfer, including NO instances;
- polynomial-size rational/radical output, polynomial bit construction given a certificate, and a proved polynomial-conditioned rational certificate-finding algorithm when none is supplied.

The optional stronger ambient bi-Hölder law, a prescribed rank/depth transformation, nonreflection U and all-nonzero basis overlaps are not used. No exact SDP complexity-class claim or automatic external novelty certification is made.
