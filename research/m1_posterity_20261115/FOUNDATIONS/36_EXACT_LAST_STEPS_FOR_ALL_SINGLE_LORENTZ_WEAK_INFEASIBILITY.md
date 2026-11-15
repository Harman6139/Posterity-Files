# Milestone 36 — Exact last-step asymptotics for every weakly infeasible single-cone SOCP

Date: 2026-11-14.
Parent research snapshot: 68cf4b1f2b4c211c2b95da9494b9d2843b200ba4.

## Scope

This proves the requested last-step conclusion for EVERY weakly infeasible affine problem over ONE Lorentz cone, in arbitrary finite dimension, under PLAIN unanchored Douglas--Rachford from EVERY starting point. It gives exact state, last-step, shadow-distance, and original equation-residual leading terms. Every weakly infeasible real or complex Hermitian order-two SDP is included.

It does NOT prove the all-orders PSD statement or the case of arbitrarily coupled products of Lorentz cones. Companion 35 disproves the broader inference for analytic semialgebraic firmly nonexpansive maps, but supplies no affine/PSD counterexample. This proof is self-contained and does not depend on earlier project rate or cosmic-convergence claims. Historical priority is not certified.

## 1. Main theorem

Let K={(t,x) in R times R^(d-1):t>=||x||}, d>=3, and e=(1,0,...,0). Let U be a nonempty affine subspace with U intersect K empty and dist(U,K)=0. Set c=dist(0,U)>0. Define

    T(z)=z+P_K(2P_U z-z)-P_U z,
    z_(k+1)=Tz_k.                                      (1)

All projections use the Euclidean metric and the set order in (1).

**Theorem A.** From every initial point,

    z_k/sqrt(k) -> sqrt(2)c e,
    sqrt(k)(z_(k+1)-z_k) -> (c/sqrt(2))e,
    sqrt(k)||z_(k+1)-z_k|| -> c/sqrt(2).                (2)

There is one unit boundary-cone direction d0 in the direction space of U. With u_k=P_U z_k and v_k=P_K(2u_k-z_k),

    u_k/sqrt(k) ->c d0,
    v_k/sqrt(k) ->c d0,
    sqrt(k)dist(u_k,K)->c/2.                           (3)

For any equality description U={z:Bz=b}, including redundant equations,

    sqrt(k)(Bv_k-b)->(c/sqrt(2))B e !=0.                (4)

These are exact last-iterate limits, not differentiated state remainders. Constants depend on U but not on the starting point. Nonorthogonal cone automorphisms are not used: they would change the projection metric.

## 2. All weakly infeasible affine spaces have one normal form

A spatial orthogonal change of coordinates and then the orthogonal light-cone coordinates

    alpha=(t+x1)/sqrt(2), beta=(t-x1)/sqrt(2),
    z=(x2,...,x_(d-1))

put the pair into the form

    K={alpha,beta>=0:2 alpha beta>=||z||^2},
    U={(alpha,0,z0+w):alpha in R,w in W},              (5)

where W is a linear subspace, z0 perpendicular W, and ||z0||=c>0.

Proof: write U=u0+L and choose affine points approaching K. They cannot have a bounded subsequence, which would produce an intersection. Normalizing an unbounded subsequence gives a nonzero vector in L intersect K. It cannot be interior, since adding a large positive multiple to u0 would give feasibility. Rotate this boundary vector to the positive alpha-axis.

All directions of L have beta=0. Otherwise choose a sign giving a point of U with positive beta, then add a sufficiently large alpha-axis multiple to make it cone feasible. Thus beta is constant on U. A negative value gives positive distance from the cone; a positive value gives feasibility using the alpha-axis. Hence beta=0.

The full alpha-axis is in L, so alpha is free independently of the transverse affine set. Write that set z0+W with z0 perpendicular W. Infeasibility forces z0!=0, since a cone point at beta=0 has z=0. Orthogonality gives c=dist(0,U)=||z0||. A nonzero cone vector in L has beta=0,z=0, so its ray is unique. Conversely (5) is weakly infeasible, as (alpha,c^2/(2alpha),z0) lies in K and approaches U as alpha tends to infinity. This proves the classification.

## 3. Exact DRS recurrences

In (5), write a state as X=(a,b,z), and set

    w=P_W z, u=P_(W^perp)z, h=2z0-u,
    s=a+b, d=b-a.

Here u temporarily denotes a transverse component, not the full affine shadow in (3). The projection and reflection are

    P_U X=(a,0,z0+w), R_U X=(a,-b,w+h).

After one step a,b>=0. The new alpha is a cone-projection coordinate. The new beta is b+(P_K R_U X)_beta, nonnegative because P_K q-q=P_K(-q) belongs the self-dual cone.

Put

    D=sqrt(s^2+2(||h||^2+||w||^2)).

For D>0 the usual Lorentz projection formula gives exactly

    s_next=(s+D)/2,
    d_next=[(1+s/D)/2]d,
    w_next=[(1-d/D)/2]w,
    u_next=u/2-dh/(2D),
    h_next=z0+[(1+d/D)/2]h.                            (6)

For verification, put q=(1-d/D)/2. The projection of R_U X has transverse coordinate q(w+h), alpha coordinate (a-b+D)(1+s/D)/4, and beta coordinate (a-b+D)(1-s/D)/4. Substitution in (1) gives (6). This is the middle projection regime because |a-b|<=s<=D.

If D=0, then a=b=0,w=h=0,u=2z0. The next transverse state is z0 and the following reflected point has nonzero transverse component. After finitely many initial steps, s>0 and D>0 forever. Such initial steps do not affect any leading constant.

## 4. Leading state scale

From (6), s is nondecreasing, s>=|d|, and |d_next|<=|d|. Put l=<h,z0/c>. Then

    l_next=c+r l, r=(1+d/D)/2 in [0,1].                (7)

If l<0 it increases by at least c. Once nonnegative, it is at least c after one further step. Thus l>=c on a tail.

If s stayed bounded, its increments (D-s)/2 would tend to zero. Since s is bounded, this would imply

    ||h||^2+||w||^2=(D^2-s^2)/2 ->0,

contradicting l>=c. Hence s tends to infinity. Since d is bounded, d/D->0. Both r and 1-r eventually lie in [1/4,3/4]. Thus w decays geometrically. The affine contraction h_next=z0+r h gives bounded h and then

    h_k->2z0, w_k->0, u_k(transverse)->0.

Let H_k=||h_k||^2+||w_k||^2; then H_k->4c^2. Rationalizing (6),

    s_(k+1)-s_k=H_k/(D_k+s_k),
    s_(k+1)^2-s_k^2
       =H_k(3s_k+D_k)/[2(s_k+D_k)] ->4c^2.             (8)

Therefore

    s_k~2c sqrt(k), D_k/s_k->1.                        (9)

Since d is bounded, a=(s-d)/2 and b=(s+d)/2 are both asymptotic to c sqrt(k). Transforming back to standard Lorentz coordinates proves the state limit in (2).

## 5. Proving the last-step limit instead of differentiating

The multiplier of d is 1-e_k, with

    e_k=(D_k-s_k)/(2D_k)
       =H_k/[D_k(D_k+s_k)] ~1/(2k).

The infinite product tends to zero, so d_k->0. Furthermore

    d_(k+1)-d_k=-e_k d_k=o(1/k).                       (10)

The transverse normal component obeys

    u_(k+1)=u_k/2+f_k,
    f_k=-d_k h_k/(2D_k)=o(k^(-1/2)).                  (11)

Unwinding this stable scalar-coefficient vector recursion proves u_k=o(k^(-1/2)): split its geometric convolution at k/2, bound the early part exponentially, and use the arbitrarily small tail coefficient of j^(-1/2) on the late part. Consequently

    sqrt(k)(u_(k+1)-u_k)->0.

The W component decays geometrically and satisfies the same conclusion. Finally (8)--(9) imply

    sqrt(k)(s_(k+1)-s_k)->c.

Combining these estimates, in light-cone coordinates,

    sqrt(k)(X_(k+1)-X_k)->(c/2,c/2,0).

The orthogonal change back to (t,x) yields (c/sqrt(2))e and its norm c/sqrt(2). This proves all of (2).

## 6. Shadows and measured residuals

The affine shadow is (a_k,0,z0+w_k), so (9) and geometric decay of w give its scaled limit c d0. Its cone shadow differs by the DRS step and therefore has the same leading term.

For a>=0,

    dist((a,0,z0+w),K)
       =[sqrt(a^2+2||z0+w||^2)-a]/2
       =||z0+w||^2/[sqrt(a^2+2||z0+w||^2)+a].         (12)

Since a_k~c sqrt(k) and ||z0+w_k||->c, this gives sqrt(k)dist(u_k,K)->c/2.

Finally Bv_k-b=B(v_k-u_k)=B(z_(k+1)-z_k). Applying B to (2) proves (4). B e cannot vanish: otherwise the interior direction e lies in the direction space of U, and a large positive shift of an affine point would make it feasible. Thus (4) has a nonzero leading vector. No finite-time numerical infeasibility certificate is inferred.

## 7. Every weakly infeasible order-two SDP

The map

    [[r,b],[b,t]] -> ((r+t)/sqrt(2),(t-r)/sqrt(2),sqrt(2)b)

is a Euclidean isometry from the Frobenius space S^2 onto R^3 sending S_+^2 to the Lorentz cone. Hence Theorem A applies to EVERY weakly infeasible affine slice of S_+^2.

Equivalently an orthogonal congruence puts every such affine slice into

    U_b={[[0,b],[b,t]]:t in R}, b!=0.

A point cannot be weakly infeasible; a hyperplane is a scalar-functional level, whose PSD-cone image is a closed ray, line, or zero; and the full space is feasible. These exclusions also follow from the classification (5).

From every symmetric initial Z_0,

    Z_k/sqrt(k)->sqrt(2)|b| I_2,
    sqrt(k)(Z_(k+1)-Z_k)->|b|I_2/sqrt(2),
    sqrt(k)||Z_(k+1)-Z_k||_F ->|b|,
    sqrt(k)dist(P_U Z_k,S_+^2)->|b|/sqrt(2).           (13)

For the original equation operator, the scaled cone-shadow residual is (|b|/sqrt(2))A(I_2), equivalently (|b|/sqrt(2))A(E11) in canonical coordinates because A(E22)=0.

The order-two complex Hermitian cone is isometric to a four-dimensional Lorentz cone, so the corresponding real-affine Hermitian result also follows. Nothing here identifies higher-order PSD cones with a single Lorentz cone.

## 8. What remains unproved

This proves the proposed derivative law for the entire single-Lorentz class, with p=1/2 and V=sqrt(2)c e, including all order-two SDPs. The proof relies on the rank-two geometry that forces the normal form (5). Higher-rank PSD cones have multiple possible recession scales and do not reduce to (6).

Companion 35 shows that analyticity, semialgebraicity, firm nonexpansiveness and a correct state term alone do NOT fill this gap. It is not a conic-feasibility counterexample. Therefore the arbitrary-order weakly infeasible SDP last-step theorem is still unproved in this continuation. No all-SDP disproof, generic ADMM theorem, finite-precision guarantee, or publication-priority claim is made.

Context: Liu--Ryu--Yin, arXiv:1706.02374, studies divergent DRS iterates for pathological conic programs. The exact normal form and recurrences used here have complete proofs above. Feasible affine/SOC intersection rate results address a different regime.
