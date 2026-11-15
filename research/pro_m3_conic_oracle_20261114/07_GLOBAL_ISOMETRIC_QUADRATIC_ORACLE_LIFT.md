# Checkpoint 07 — a global isometric quadratic-to-conic oracle equivalence

Continuation from 4cdd97d52b8e771996083e0f91c126924437024f. Source milestones remain unchanged. This is a completed algebraic reduction; a full randomized lower-bound theorem is NOT asserted here.

## Theorem: natural PSD distance with exactly the same information as a matrix-vector oracle

Let q(x)=||Cx-d||^2/2 = x^T A x/2-b^T x+c, where A=C^T C, b=C^T d, c=||d||^2/2, and 0 <= A <= I/2. Choose S with S^T S=I/2-A, and fix M>0. Let W(z)=[[0,1],[1,z]] and define the block-diagonal affine pencil

    X(x,z)=diag( [[0,(Cx-d)^T],[Cx-d,0]],
                 [[M,(Sx)^T],[Sx,M I]], W(z) ).

Each displayed zero or identity has the required row dimension. The first block is a symmetric star. Its only possible nonzero eigenvalues are +/-||Cx-d||. The second block has eigenvalues M+||Sx||, M-||Sx||, and M with the remaining multiplicity. Consequently its EXACT natural objective is

    f(x,z)=dist_F(X(x,z),S_+)^2/2
          =q(x)+(||Sx||-M)_+^2/2+phi(z),
    phi(z)=(sqrt(z^2+4)-z)^2/8.

The x-direction Gram matrix in the first block is 2A; that in the second is 2S^T S=I-2A. Their sum is I, and the z direction has disjoint support and unit norm. Thus these are genuinely orthonormal affine coordinates, and f is convex C1 and 1-smooth.

Suppose Cx_star=d and ||Sx_star||<=M. Then the affine space is genuinely weakly infeasible: the W block rules out PSD feasibility, while x=x_star and z tending to +infinity give distance tending to zero. If q(0)<=1/2, then f(0,0)<=1.

### Forward exact oracle simulation, for EVERY finite query

Grant the parameters b,c,M and the tail formula. One matrix-vector call p=Ax suffices to calculate the full natural value and coordinate gradient. Set P=I/2-A and r=sqrt(x^T P x). Then

    f=q+(r-M)_+^2/2+phi,
    grad_x f=p-b+k(x/2-p),
    k=0 if r<=M, and k=1-M/r otherwise.

The z gradient is phi'(z). This formula includes arbitrarily large queries. It is not an argument based on discarding a small spectral term.

### Reverse exact simulation

Given the value and coordinate gradient at (x,z), put

    h=||x||^2/4-b^T x+c-[f(x,z)-phi(z)].

Exact arithmetic gives h=r^2/2 for r<=M, and h=Mr-M^2/2 for r>=M. Thus

    r=sqrt(2h) if h<=M^2/2;
    r=(h+M^2/2)/M otherwise.

Recover k as above, and then

    Ax=(grad_x f+b-kx/2)/(1-k).

The denominator is strictly positive at every finite query because M>0. Therefore the two exact information models are equivalent, one query for one query. This equivalence is global, not confined to a prescribed ball.

### Comparator geometry

Whenever a comparator u for q satisfies ||u||<=sqrt(2)M, it also satisfies ||Su||<=M, since S^T S<=I/2. Such a comparator pays no padding cost. Thus a family of uniformly controlled prefix comparators, as in source milestone 27, retains its objective-versus-radius upper bound after this isometric conic lift. The fixed W tail supplies the beta=1/2 radius lower bound. More generally a separate known conic tail can be substituted for W.

### Rationality

If C,d are rational and I/2-A is positive semidefinite rational, S can be chosen rational with at most four times its rank many rows. Rational symmetric elimination gives an LDL^T factorization with rational nonnegative pivots (including a permutation and omission of zero pivots). Every positive rational pivot is a sum of four rational squares: write a/b=(n_1^2+...+n_4^2)/b^2 using the four-square theorem for the positive integer ab. Expanding each pivot into those four rows gives a rational Gram factor. No polynomial bit-height assertion is needed for this existence statement.

Rational orthogonal rotations preserve rationality. However a rational quadratic matrix A with rational b,c is exactly identified by a single algebraically independent algebraic query, as proved in checkpoint 03. The reverse simulation shows that the rational lifted family likewise collapses to one identification query. Thus rationalizing a Haar-distributed quadratic is NOT a valid way to obtain the handoff's rational exact-oracle lower bound.

Real-coefficient Haar rotations are not subject to that countable decoding argument. A fixed-distribution randomized quadratic lower bound, together with an explicitly verified uniform comparator profile, can be transferred through this theorem to a REAL-DATA natural conic family. Establishing that complete lower-bound statement is the next proof obligation. Such a theorem would still not resolve the handoff's rational-support exact-oracle target.

## Recovery status

The saved checkpoints 00--06 have been recovered and read in this continuation. Their stochastic/bias conclusions remain distinct from the missing noiseless sequential lower bound. The initial status file is historical, not an up-to-date complete reading ledger. No top-quintile benchmark has yet been earned.
