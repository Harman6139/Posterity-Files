# Checkpoint 008: exact angular conditioning of bounded-moment grids

Date: 2026-11-15. Analytic theorem and proof; historical priority is not certified by this checkpoint.

Let -1=a_0<a_1<...<a_m=1 be any scalar grid. Put

 e(G)=max_j [1-a_j*a_(j+1)-sqrt((1-a_j^2)(1-a_(j+1)^2))]/2
     =max_j sin^2((arccos(a_j)-arccos(a_(j+1)))/2).

For K_r={(t,z):t>=0, |z_i|<=t}, use the tensor product of possibly different scalar grids G_i. Let Phi_e preserve A_00 and all offdiagonals and replace A_ii by (1-e_i)A_ii+e_i A_00. Then

 Phi_e(CP(K_r)) subset cone{(1,z)(1,z)^T: z_i in G_i}

if and only if e(G_i)<=e_i<=1 for every i. In particular the least common coefficient is max_i e(G_i). The dual inclusion is exactly the adjoint map; Phi_e is not self-adjoint. The statement is valid over real grids, and rational grids give rational finite cones.

Proof in one coordinate. For y in [a,b] between consecutive nodes, the minimum variance of a grid-valued random variable of mean y is v_min=(y-a)(b-y). The endpoint distribution has maximum variance v_max=1-y^2. Every variance between them is realized by mixing the two distributions. Thus the required second moment y^2+e(1-y^2) is possible exactly when e >= sup v_min/v_max and e<=1. Direct discriminant calculation gives

 sup_(a<y<b) (y-a)(b-y)/(1-y^2)
 = [1-ab-sqrt((1-a^2)(1-b^2))]/2.

Endpoint gaps are interpreted by limits: a=-1 gives (1+b)/2 and b=1 gives (1-a)/2. Independent coordinate distributions preserve means and all cross products. Apply this to each permitted rank-one atom and sum.

Necessity also has an exact dual witness: Q(t,z)=(z_i-a t)(z_i-b t) is nonnegative at every tensor-grid atom, and on the corrected atom (1,y), its pairing is -(y-a)(b-y)+e_i(1-y^2). For every coefficient below the claimed bound a rational y with strict negative pairing exists when the grid is rational. Thus there are rational extremizing witnesses (strict witnesses at every suboptimal coefficient), not merely floating-point tests.

Optimal grids. The m angular gaps sum to pi, so the least possible correction over all m-interval grids is sin^2(pi/(2m)). Equality forces every angular gap to be pi/m, namely the cosine grid. Among rational grids this minimum is attained exactly for m=1,2,3. For m>=4, equality would force 2*cos(pi/m) to be a rational algebraic integer strictly between sqrt(2) and 2, impossible. Rational grids are dense, so the same value is their infimum but is not attained. This is a precise arithmetic obstruction to attaining the geometrically optimal constant.

Explicit rational near-optimal-rate grids. For q>=1 use
 G_q={+/- (q^2-j^2)/(q^2+j^2): j=0,...,q},
with duplicates removed. There are 2q+1 nodes. Their largest angular gap is 2*arctan(1/q), since arctan is increasing and concave on [0,1]. Therefore

 e(G_q)=1/(q^2+1),

exactly. Node heights are O(log q). In contrast, the equally spaced m-interval grid has exact coefficient 1/m. Thus the earlier 1/q uniform-grid result is correct for that grid but is not an intrinsic rate barrier.

Rational factorization consequence. If A in CP(K_r) is rational, set D=diag(0,A_00-A_11,...,A_00-A_rr). For rational 0<epsilon<=1 choose q with q^2+1>=1/epsilon. The matrix A+epsilon D belongs to the rational grid cone and has at most d=(r+1)(r+2)/2 weighted rational atoms. Clearing each atom's rational denominator and applying Cramer's rule gives coefficient bit length O(L+d*(r*log q+log d)); four squares gives at most 4d rational Gram columns of polynomial binary height. This preserves mass, first moments, every cross moment, and every saturated variance (D_ii=0). The finite grid still has (2q+1)^r atoms, so enumeration is not polynomial in binary precision. The arithmetic facial-reduction algorithm supplies the distinct nonlocal fixed-dimension route.

Rational boxes [l_i,u_i] follow by affine homogenization. Replace each second moment by (1-e_i)A_ii+e_i[(l_i+u_i)A_0i-l_i*u_i*A_00]. This is an exact nonnegative face-slack correction. The same angular formula applies to the rescaled nodes.

This sharp theorem is to be integrated as a concrete measurement-preserving application, not advertised alone as the grand breakthrough. The general structural result remains arithmetic facial closure of rational Gram fibers.
