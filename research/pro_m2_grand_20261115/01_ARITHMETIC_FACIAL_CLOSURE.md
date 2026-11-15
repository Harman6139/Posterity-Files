# Arithmetic facial closure of polyhedral Gram fibers

Research checkpoint 001, 2026-11-15. Internal proof completed below; historical priority and quantitative bounds are still under audit. This is not an editorial-percentile or external-verification claim.

## Definitions
Let P=(P_1,...,P_g) be finitely many closed rational polyhedral cones in R^n, with lineality and lower-dimensional members allowed. Put C(P)=cone_R{xx^T:x in union P_j} and R(P)=cone_Q{xx^T:x rational in union P_j}, with nonnegative coefficients. Four rational squares show that R(P) is equivalently the set of finite rational Gram factors with columns in the domains. Let H={X:L(X)=b} be a rational affine subspace of Sym_n, and d=n(n+1)/2.

## Closedness and rational reserve
C(P) is closed: its trace-one base is the convex hull of the compact set of normalized permitted rank-one matrices. Its span V is rational. Choose rational independent vectors in each P_j spanning span(P_j). Their squares and squares of pairwise sums span Sym(span(P_j)). Select an atom basis G_1,...,G_k of V from this finite family. Then B=sum G_i belongs ri C(P).

## Exact rational zero domains
For a real algebraic W nonnegative on the domains, choose a rational basis matrix B_F for the span of each polyhedral face F. Over a common number field expand
B_F^T W B_F=sum_{a=0}^{e-1} theta^a M_(F,a), with rational coefficient matrices and an irreducible power basis. Define
D_F=F intersect {B_F z: M_(F,a) z=0 for all a}.
Then the closure of the rational zero vectors of W in the original domains is exactly the finite union of the closed rational polyhedral cones D_F.
Proof: a zero x in the relative interior of its minimal face satisfies x^T W v=0 and v^T W v>=0 for every v in that face span, by evaluating W at x plus or minus small multiples of v. Thus the restriction annihilates x. If x and B_F are rational, so are its coordinates, and field-basis independence gives all the coefficient-kernel equations. Conversely these equations force a zero. Rational points are dense in each D_F. No PSD test is required to define the D_F; the PSD property is used only for the stationarity implication.

## Rational interior factors
Every rational X in ri C(P) belongs R(P). Choose rational tau>0 with X-tau B in C(P), and decompose the latter into at most d real permitted rank-one matrices. Approximate their vectors rationally in their respective polyhedral cones. In the rational atom basis G_i, the residual coefficients tend to tau, so sufficiently accurate approximations leave all residual coefficients rational and positive. Rational dependence elimination compresses the weighted factorization to at most k<=d atoms; four squares give at most 4d rational columns. Discovery complexity is treated separately.

## Master theorem
A finite algorithm returns either EMPTY or a finite union P_* of rational polyhedral cones contained in the original domains such that
closure(R(P) intersect H)=C(P_*) intersect H.
In the nonempty case H intersects ri C(P_*). At most d proper reductions are needed. The terminal cone can depend on choices, but its intersection with H is intrinsic.

Algorithm: compute V=span C(P). If C(P) intersect H is empty, return EMPTY. If H intersects ri C(P), stop. Otherwise properly separate H intersect V from ri C(P), obtaining W nonzero on V, nonnegative on C(P), and zero on H intersect V. Normalize <W,B>=1. All conditions have a rational first-order real-algebraic description, so an algebraic W can be sampled. Replace the domains by the D_F above and repeat.

Proof: the new closed Gram cone lies in C(P) intersect W-perp and therefore has smaller span dimension. A rational Gram completion X in H satisfies 0=<W,X>, a sum of nonnegative quadratic values of rational columns. Every column is a rational zero and belongs to a replacement domain. Conversely replacement domains are subsets of the originals. Thus the rational Gram completions are preserved exactly. Dimension descent proves termination, including degeneracies and non-exposed faces. At a nonempty terminal step, rational points are dense in the relatively open set H intersect ri C(P_*), since H intersect span C(P_*) is a rational affine space. The interior-factor lemma applies. Joining any point of the terminal slice to a relative-interior feasible point and then approximating rationally proves the displayed closure identity. An empty later real-feasibility test proves that the original rational-completion set was empty.

## Exact decision and robust rationalization
With H={A}, this decides rational constrained Gram factorability of every rational A, including real-feasible boundary cases. For arbitrary rational H it decides exact rational Gram completion.
For rational A in C(P) intersect H, a rational D in ker L exists such that A+tD has a rational constrained Gram factor for every rational 0<t<=1 if and only if A is in the terminal slice. Necessity is a limit argument. For sufficiency take rational X0 in H intersect ri C(P_*), set D=X0-A, and apply the interior-factor lemma to every positive point of the segment.

## Totally real descent preserving polyhedral column constraints
A rational affine constrained Gram problem has a rational Gram solution if and only if it has a Gram solution with all columns in a totally real number field.
Proof: only the reverse implication requires work. Follow the reduction with a surviving factorization X=sum x_jx_j^T in H over a totally real field E. At a selected W, let F_j be the minimal current face containing x_j. W is PSD on span(F_j). Every real embedding sigma:E->R sends x_j into this rational span, though it need not preserve the cone inequalities. The field average Xbar=(1/[E:Q])sum_sigma sum_j sigma(x_j)sigma(x_j)^T is rational and lies in H and the current rational matrix span. Hence <W,Xbar>=0. All summands are nonnegative. W therefore annihilates every conjugate within the corresponding face span. Their real span is the scalar extension of the rational coefficient span of x_j, because a number-field basis has an invertible embedding matrix. Thus x_j belongs to the rational kernel used by the replacement. The factorization survives every step; no real-feasibility test becomes empty, and the terminal relatively strictly feasible problem has a rational solution.
For rational X itself, this also shows X is in the relative interior of the Gram cone generated by the minimal faces intersected with the rational coefficient spans of its columns.
The unstructured SOS descent is classical (Hillar, Quarez, Scheiderer); its novelty is not claimed. Constraint preservation and the arithmetic-fiber algorithm are the specific claims undergoing comparison.

## Necessity example
Let H be the rational affine line A(t)=diag([[t,2],[2,2t]],[[2,t],[t,1]]). PSD feasibility, hence CP feasibility, forces t=sqrt(2). A real nonnegative factor consists of (2^(1/4),2^(3/4),0,0) and (0,0,sqrt(2),1). There is no rational matrix completion, hence no rational Gram completion. The factor field Q(2^(1/4)) is real but not totally real.
The PSD matrix W=diag([[2,-sqrt(2)],[-sqrt(2),1]],[[sqrt(2),-2],[-2,2sqrt(2)]]) has <W,A(t)>=0 for all t. Its coefficient of 1 in the basis (1,sqrt(2)) is invertible, so no nonzero rational vector is a zero. One arithmetic reduction leaves only zero, which does not meet H. This proves that arbitrary real fields cannot replace totally real fields, and that real feasibility alone cannot justify a rational-factor/strict-separator dichotomy.

## Remaining work at this checkpoint
Uniform bit-complexity accounting, exact implementations and independent checks, sharp nonsimplicial applications, full prior-source audit, and the preregistered published-paper comparison remain to be completed. The qualitative theorem above is not being marketed as a fully vetted flagship result.
