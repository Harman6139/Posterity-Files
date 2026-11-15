# Effective arithmetic reduction and sharp cone conditioning

Checkpoint 003, 2026-11-15. Standard singly-exponential real-algebraic sampling and one-block quantifier elimination are explicit algorithmic primitives, not unit-cost oracles. Constants below are absolute and effective, not optimized.

## Fixed-dimensional bit complexity

Let g rational polyhedral cones in R^n have a total of s inequality/equality rows, let L be total binary input length including measurements, and d=n(n+1)/2. Remove redundant measurement equations, leaving at most d or an immediate inconsistency. The arithmetic facial-closure algorithm has at most d proper updates. A conservative deterministic bit bound is (L+2)^(C n^10), with algebraic degrees at most 2^(C n^6) and coefficient bit heights at most (L+1)2^(C n^6), for a universal effective constant C. This is polynomial for fixed n, not uniformly in n, and requires neither Slater feasibility nor a positive distance promise.

Each current domain has form P_i intersect U with P_i original and U rational. Compress equalities to n rows. Enumerate subsets of at most n original inequality rows on U; for J choose B_J spanning U intersect ker H_J and intersect with the coefficient kernels of B_J^T W B_J. The actual minimal face's active row span has such a basis, so the list is complete. Extra candidates remain valid because the kernel equations force zero. Thus the number of domains after j updates is at most g(s+1)^(nj), and at termination at most g(s+1)^(nd).

Real feasibility is an existential formula in nd<=n^3 variables u_1,...,u_d, of degree two: each column belongs to the domain union and L(sum u_j u_j^T)=b. Relative strict feasibility adds tau>0 and tau B, where B is the rational atom reserve. The Boolean formula is kept as an AND of domain disjunctions, not expanded into a Cartesian list.

An exposer has d free variables W and one universal n-variable block x. Add linear equations making W vanish on the rational affine H intersect V and <W,B>=1; impose [x in current domains implies x^T W x>=0]. The total degree is at most three. Standard one-block elimination and algebraic sampling yield degree/height multipliers 2^poly(n), polynomial dependence on coefficient bit length, and a formula-size exponent O(n^5). Together with domain growth this is absorbed by the n^10 bound.

After sampling W, factor its univariate representation over Q, select the isolating real root, expand all matrix entries in the irreducible power basis, and take rational coefficient kernels. The algebraic field is then discarded: the next domain descriptions are rational. Consequently at most d iterations multiply heights by 2^poly(n), rather than forming a tower of extensions. This rational reset is the complexity invariant.

## Exact terminal construction

Choose a rational atom basis G_i=a_i a_i^T for V and B=sum G_i. Sampling gives tau>0 and permitted algebraic u_j with L(sum u_j u_j^T+tau B)=b. Express u_j in rational polyhedral generators and approximate its nonnegative coefficients rationally, obtaining permitted r_j; approximate tau by positive rational tau0. Let M have columns L(G_i), and let R be a rational right inverse on image M. Define

 e=tau0*1+R[b-L(sum r_j r_j^T)-tau0 M1].

Then X=sum r_jr_j^T+sum e_iG_i has exact measurements. Under sufficiently accurate approximation, all e_i approach tau>0. Exact positivity checks and dyadic refinement terminate; algebraic root-separation and Cramer bounds give the stated heights. Rational conic dependence elimination leaves at most d weighted atoms.

At most 4d rational Gram columns exist by four squares, with the same height order. A deterministic polynomial algorithm need not assume a polynomial four-square routine: for a positive rational weight a/b, expand ab in binary; an even binary power is one integer square and an odd power is two identical integer squares. Divide by b. This produces O(bitlength(ab)) columns per weight and stays within the stated bit bound. Thus the 4d width is an existence guarantee; the deterministic algorithm may output more columns.

A prescribed rational target in the terminal slice can be approximated within 2^-p with the same measurements by using the rational segment toward a terminal interior completion. The construction and factor heights are polynomial in L+p for fixed n. A full production arbitrary-quantifier-elimination driver is not represented as having been run by the separate small exact-certificate scripts.

## Exact alternatives, not a false strict-separation theorem

A real-feasible but arithmetically infeasible fiber cannot have a true separator of the original cone. Its certificate is the finite chain of algebraic nonnegative exposers, rational coefficient-kernel restrictions, and final real infeasibility. A complete sign-cell/elimination transcript is reproducible within the same bound; no short variable-dimension coNP certificate is asserted.

Even an empty real measurement fiber need not have strict separation: for CP_2 and L(X)=(X_11,X_12), b=(0,1) is infeasible but approached by [[epsilon,1],[1,1/epsilon]]. This disproves a universal factor/strict-separator alternative for arbitrary measurements.

For full-matrix membership the cone is closed. If ||A||_F<=1 and dist(A,C)=delta>0, conic projection gives W in C* with ||W||=1 and <W,A>=-delta. Add delta/(4n)I and round every entry with error at most delta/(16n^2). The rational matrix has permitted unit-vector margin at least 3delta/(16n) and pairing below -delta/2, with entry height O(log n+log(1/delta)). Projection plus rounding is an existence proof; algebraic sampling and exact open-set rationalization give fixed-dimensional polynomial discovery. All cone-verification work is counted separately.

## Sharp lattice conditioning

If K is generated by integer vectors of norm at most R>=1 and has span dimension r, and P[v]>=1 for all nonzero integer v in K, then for M>=max(1,||P||_F),

 min_{x in K,||x||=1}P[x]>=1/[8r^2R^2(16r^2R^2M)^(r-1)].

Every x is a nonnegative combination of at most r independent generators. Pulling P back to s<=r such generators gives norm at most sR^2M and orthant integer minimum at least one. The inherited sharp-order Dirichlet/stationarity bound is 1/[8s(16s^2R^2M)^(s-1)]. Since ||Ba||^2<=sR^2||a||^2, the stated estimate follows.

For every fixed rational polyhedral cone with relative-interior dimension r>=2, exponent r-1 is optimal even among relatively perfect forms. Choose a lattice basis B with columns inside the cone by extending a primitive interior lattice vector and adding large positive multiples of it to the other basis columns. With T_r the canonical tridiagonal form and V_q=I-qS, define P_q[Bz]=z^T V_q^TT_rV_qz. Integer minimum is at least one. Since V_q inverse is nonnegative, inverse images of interval minimal vectors lie in K and their squares span Sym(span K), proving relative perfection. The norm is O_K(q^2); the minimal vector B(q^(r-1),...,1) has norm Omega_K(q^(r-1)), giving margin O_K(q^(-2(r-1))). No smaller norm exponent works.

The qualitative generalized Interior Ryshkov theorem and the earlier quantitative orthant theorem are antecedents, not new claims. Exact coefficient kernels and approximate Dirichlet recurrence use the same facial stationarity. The nonsimplicial DNN path in checkpoint 002 shows why polynomial coefficient heights do not bound adjacent face crossings.
