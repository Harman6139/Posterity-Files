# Checkpoint 05 — every positive rational escape exponent

## Theorem

For EVERY positive rational beta, there is an explicitly constructed rational affine pencil Y(y), with Frobenius-orthonormal direction matrices, whose affine space is weakly infeasible and whose natural objective

    g(y)=dist_F(Y(y),S_+^m)^2/2

satisfies g(0)=1/2 and rho_g(s)=Theta_beta(s^-beta) on a fixed interval 0<s<=s_beta. All constants depend only on beta. If 2beta=p/q in positive relatively prime integers, the construction uses O(p+q) matrix order and coordinates, with rational coefficients of O(log(p+q)) bits.

Consequently the testing carrier of checkpoint 02 proves genuine rational conic stochastic lower bounds Omega_beta(sigma^2 epsilon^(-2beta-2)) and sharp adversarial absolute-gradient-bias scale Theta_beta(epsilon^(beta+1)) for EVERY positive rational beta, not merely the two exponent ladders. Matrix order is fixed as epsilon varies, and the carrier data have O_beta(log(1/epsilon)) bits. The matching upper sample cost remains O_beta(epsilon^(-beta-1/2)+sigma^2 epsilon^(-2beta-2)); therefore samples match in the noise-dominated regime sigma^2>=epsilon^(beta+3/2). The original noiseless sequential lower term is still unproved.

## 1. Binary tree pencil

Write a=2beta=p/q. Let N=2^k be the smallest power of two at least p+q; k>=1. Consider a full binary tree with N leaves. Label q leaves by a single variable t, p leaves by the constant 0, and the remaining r=N-p-q leaves by the constant 1. The order of these leaf labels can be fixed arbitrarily once and for all.

At every nonroot internal node v introduce a variable u_v. At the root set u_root=1. For each internal node v, with children carrying labels a_v and b_v, put the 2x2 block

    [[a_v,u_v],[u_v,b_v]]

in a block-diagonal matrix. There are N-1 such blocks. For each nonroot internal node append one scalar block u_v. Finally, put M=ceil(sqrt(q)) and append M^2-q scalar blocks t (possibly none).

Use coordinates

    y_t=M t, y_v=2u_v for nonroot internal nodes v.

The resulting matrix order and coordinate dimension are

    m=3N-4+M^2-q, d=N-1.

All constants and coefficients are rational. Each variable u_v appears in its own block's two symmetric off-diagonal positions, once in its parent's diagonal, and once in its scalar padding block. Its coordinate coefficient is 1/2 in those four positions, so its direction has norm one. The t variable appears in exactly M^2 diagonal positions, each with coordinate coefficient 1/M. Distinct directions have disjoint supports, so they are Frobenius orthonormal.

At y=0 the root block is [[0,1],[1,0]], including the case N=2 when its leaves are t and 0. All other blocks are PSD diagonal matrices. Thus g(0)=1/2.

## 2. Exact infeasibility

Choose one of the p zero leaves. If the block-diagonal matrix were PSD, its zero diagonal would force the corresponding off-diagonal u_v to be zero. At the parent node this becomes a zero diagonal, again forcing the parent's off-diagonal to vanish. Propagate to the root. Its off-diagonal is fixed at 1, a contradiction. Thus the affine space is disjoint from the PSD cone.

## 3. Explicit small-residual curve and upper escape bound

For 0<e<=1, temporarily replace every zero leaf by e and set

    t=e^(-p/q).

At each nonroot internal node choose u_v to be the geometric mean of all descendant leaf values. Equivalently, u_v is the positive square root of the product of its two child labels. The product of all N leaves is t^q e^p=1, so the resulting root geometric mean is exactly 1, as required. Every 2x2 block is therefore PSD of rank one. The scalar padding entries are nonnegative as well.

Return to the true affine pencil by changing only the p zero-leaf diagonal entries from e back to zero. The Frobenius change is sqrt(p)e. Hence

    dist_F(Y(y(e)),S_+^m)<=sqrt(p)e.

Every leaf value lies between e and t, and every internal geometric mean is at most t. Consequently

    ||y(e)|| <= sqrt(M^2+4(N-2)) e^(-p/q).

Taking e=delta/sqrt(p) proves a coordinate-radius upper bound C_beta delta^(-p/q) at matrix residual delta, on a fixed small interval. It also proves that the distance between the affine space and the cone is zero, so the infeasibility is weak.

## 4. Lower escape bound, including perturbations of ALL blocks

Suppose dist_F(Y(y),S_+^m)<=delta with 0<delta<=1. Then Y(y)+delta I is PSD. Thus every shifted 2x2 block obeys

    u_v^2 <= (a_v+delta)(b_v+delta).

Every shifted diagonal is nonnegative. In particular u_v+delta>=0 whenever u_v is a nonroot node (it occurs on its parent's diagonal). For the t leaves put

    T=max(t+delta,delta).

Replace their shifted leaf value by this larger T. The other shifted leaf values are delta and 1+delta. All comparison leaf values are at least delta.

For a nonroot internal node of height h above its leaves, let G_v be the geometric mean of its comparison leaves. We claim

    0<=u_v+delta<=(h+1)G_v.

At height one, the determinant inequality gives u_v+delta<=sqrt((a_v+delta)(b_v+delta))+delta<=2G_v, because G_v>=delta. If the two child inequalities hold at height h-1, then

    u_v+delta <= sqrt((a_v+delta)(b_v+delta))+delta
               <=h sqrt(G_left G_right)+delta
               <=(h+1)G_v.

This also proves the induction when a child is a leaf, using its direct comparison. At the root, whose off-diagonal is the fixed number 1, the determinant inequality therefore gives

    1 <= k [T^q delta^p (1+delta)^r]^(1/N).

For k=1 there are no nonroot nodes, and this is just the root determinant inequality. Hence

    T >= c delta^(-p/q),
    c=k^(-N/q) 2^(-r/q)>0.

Choose delta0=min(1,(c/2)^(1/(1+p/q))). For 0<delta<=delta0 the last lower bound is at least 2delta. Thus T=t+delta rather than delta, and

    t>=T/2 >= (c/2)delta^(-p/q),
    ||y||>=|y_t|>=t.

This proves the matching lower bound. Notice that the proof allows errors in every matrix block, not merely perturbations of the designated zero leaves. It is therefore a genuine natural-distance lower bound, not just a calculation along the explicit curve.

## 5. Objective exponent and normalization

The minimum coordinate radius at residual delta is Theta_beta(delta^(-p/q)). Substituting delta=sqrt(2s) yields rho_g(s)=Theta_beta(s^(-p/(2q)))=Theta_beta(s^-beta). All constants and the onset are fixed once p/q is fixed. The number of coordinates is N-1, matrix order is as above, and each coefficient is 0, 1, 1/2 or 1/M, up to placement. Since N<2(p+q), the size assertions follow.

## 6. Attribution and scope

The binary geometric-mean/rotated-cone representation is classical, not claimed as an invention. Relevant primary work includes Jie Wang, 'Weighted Geometric Mean, Minimum Mediated Set, and Optimal Simple Second-Order Cone Representation', SIAM J. Optimization 34(2) (2024), 1490--1514, DOI 10.1137/22M1531257; and V. Blanco and M. Martinez-Anton, 'On Minimal Extended Representations of Generalized Power Cones', SIAM J. Optimization 34(3) (2024), 3088--3111, DOI 10.1137/23M1617205. Those representation results must not be mistaken for oracle lower bounds.

The specific facts proved here are rational isometric normalization, exact weak infeasibility, the matching natural PSD-distance escape exponent despite arbitrary block perturbations, and its use as a FIXED known tail in the already proved conic Gaussian/bias experiment. This is a static tail construction and a query-level statistical realization, not an oracle-preserving SDP compiler for arbitrary hidden functions. No optimal matrix order for a prescribed exponent is asserted; the two earlier ladders can be much smaller at their special exponents.
