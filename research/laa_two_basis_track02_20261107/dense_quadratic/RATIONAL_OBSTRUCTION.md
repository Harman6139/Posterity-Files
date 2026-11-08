# Exact rational coefficients can be impossible for a direct rank-one two-basis representation

This is a precise arithmetic obstruction, not a claim against algebraic or approximated bases.

Let
 K = [[1,0,0,2],
      [0,1,0,0],
      [0,0,1,0],
      [2,0,0,-3]]
and L={H in S^4:<K,H>=0}. The matrix K is rational, nonzero, traceless and indefinite, so I_4 belongs to L and the corresponding trace-normalized PSD inverse problem is trace controlled. One may define A by choosing a rational basis of L.

**Proposition.** There is no nonzero rational vector v in Q^4 such that v^T K v=0. Consequently there is no rational matrix F with FF^T=I_5 and with an affine single-copy anchor encoding
 E(X)=F^T(X direct-sum [1])F
for which all first-basis outcomes are functions only of A(X) on every positive-definite source fibre. This is true independently of the proposed second orthogonal basis, even if that basis is rational.

Proof. For x in Q^4,
 x^T K x=(x_1+2x_4)^2+x_2^2+x_3^2-7x_4^2.
Thus a rational K-null vector would produce a nonzero integer solution to
 a^2+b^2+c^2=7d^2.
If d is odd, the right-hand side is 7 modulo 8, impossible because a sum of three integer squares cannot be 7 modulo 8. If d is even, reduction modulo 4 shows that a,b,c are all even. Dividing by four gives another solution with smaller |d|. Infinite descent proves the only integer solution is zero.

For a single-copy affine face embedding, the first-basis jth projector pulls back to f_j f_j^T on the source, where f_j is the top four-coordinate portion of the jth column of F. To have a constant measurement over every affine fibre {X>0:A(X)=b} for all positive-definite b, the corresponding functional must lie in L, meaning <K,f_j f_j^T>=f_j^T K f_j=0. Rational F would make every f_j rational, so every top source column must be zero. This contradicts FF^T=I_5.

The null cone has real and algebraic (nonrational) points, so the single-copy algebraic construction of the hyperplane theorem is unaffected. The proposition only excludes exact rational *canonical one-copy frames* for this rational problem, not arbitrary auxiliary rational encodings or rational approximations of algebraic bases.

The construction is a rational congruence of the classical anisotropic rational quaternary form a^2+b^2+c^2-7d^2: use the invertible rational map (x_1,x_2,x_3,x_4) -> (x_1+2x_4,x_2,x_3,x_4). The transformed matrix has trace zero even though the original diagonal form does not. This explains why trace control by itself does not force rational isotropy.

Implication: polynomial-size algebraic circuits, isolating intervals, or certified numerical basis approximations are natural output models; imposing an unqualified exact rational-frame requirement is strictly stronger than mathematical universality.
