# Checkpoint 05 — exact projective duality for a conic alternative

Status: proved identities and conditional-on-the-inherited-state-theorem asymptotic consequences. This is NOT a proof or disproof of the arbitrary-order plain DRS last-step conjecture. Historical priority of the projective formula has not been certified.

## 1. Data and the alternative affine space

Let E be a finite-dimensional real inner-product space, K a closed self-dual cone, and U=a+L, with a perpendicular to L and a nonzero. Let P=P_L, Q=I-P, sigma=||a||^2, and E_a z=<a,z>a/sigma. Define

    L#=(L+span{a})^perp, P#=Q-E_a,
    a#=-a/sigma,
    U#=a#+L#={w: Pw=0, <a,w>=-1}.

The alternative operation is involutive: (U#)#=U. Both problems use the ORIGINAL inner product and the SAME cone K. In particular there is no metric change when K is the PSD cone. Let T and T# be the corresponding plain affine-first DRS operators.

For any z put h(z)=sigma-<a,z>. On the open halfspace h(z)>0 define Phi(z)=z/h(z).

## 2. Exact pointwise identities

For every z with h(z)>0,

    T#(Phi(z))=T(z)/h(z),                             (2.1)
    (T#-I)(Phi(z))=(T-I)(z)/h(z),                    (2.2)
    h#(Phi(z))=1/h(z),                               (2.3)
    Phi#(Phi(z))=z.                                  (2.4)

Here h#(w)=||a#||^2-<a#,w> and Phi# is defined using the alternative data.

Proof. Write J=2P-I and R_U z=Jz+2a. Since P#=I-P-E_a,

    R_(U#)(z/h)=-Jz/h-2E_a z/h-2a/sigma
               =-(Jz+2a)/h,

where h+<a,z>=sigma. Moreau decomposition for a self-dual cone gives R_K w=P_K w+P_K(-w)=R_K(-w). It is positively homogeneous. Hence, using T=(I+R_K R_U)/2,

    T#(z/h)=[z+R_K R_U z]/(2h)=Tz/h.

Subtract z/h for (2.2). Direct substitution gives h#(z/h)=1/sigma+<a,z>/(sigma h)=1/h, which also proves the involution. QED.

A second exact identity, valid for EVERY z without a sign restriction on h, is

    h(z)=<Tz,Tz-z>.                                  (2.5)

Indeed put x=Pz, y=Qz-a, d=Tz-z. The cone points v=a+x+d and s=y+d are complementary. Their inner product is

    0=<a,y>+<z,d>+||d||^2=-h(z)+<Tz,d>.

Thus also ||Tz||^2-||z||^2=2h(z)-||Tz-z||^2. (2.6)

## 3. Exact relation of zero-anchor discounted paths

Let q(t) be the unique solution Tq(t)-q(t)=q(t)/t, t>0. This section uses anchor ZERO, not the affine anchor a used in Checkpoint 01. Assume U is weakly infeasible. Then q(t) is nonzero: q(t)=0 would force T0=0 and hence a feasible point.

By (2.5), h(q(t))=(t+1)||q(t)||^2/t^2>0. Consequently (2.2) and uniqueness of the discounted fixed point give the EXACT formula

    q#(t)=Phi(q(t))
         =[t^2/(t+1)] q(t)/||q(t)||^2,              (3.1)
    ||q(t)|| ||q#(t)||=t^2/(t+1).                   (3.2)

The two discounted points lie on the same positive ray at every t, not only asymptotically.

## 4. The alternative is also weakly infeasible

First, U# has no point in K. If w were such a point, every u in U would satisfy <w,u>=-1. Choose v_j in K and u_j in U with ||v_j-u_j|| tending to zero, which is possible by original weak infeasibility. Self-duality gives <w,v_j>>=0, contradicting <w,v_j> tending to -1.

Second, q(t) tends to infinity in norm. Otherwise a bounded subsequence as t tends to infinity would, by its defining equation and continuity, yield a fixed point of T and hence a feasible point of U. By (3.1),

    ||T#q#(t)-q#(t)||
      =||q#(t)||/t=t/[(t+1)||q(t)||] -> 0.

The DRS displacement is the difference of a point in K and a point in U#. Thus dist(K,U#)=0. This proves weak infeasibility of the alternative, without needing semialgebraicity.

## 5. Complementary state exponents and reciprocal escape exponents

Assume now that K is semialgebraic (in particular K=S_+^m) and invoke the inherited common-state theorem of Milestones 30–31. Suppose

    q(t)=c t^p+o(t^p), 0<p<1, c nonzero,
    z_k=V k^p+o(k^p), c=p^p V.

Then (3.1) gives q#(t)=[c/||c||^2] t^(1-p)+o(t^(1-p)). Therefore EVERY plain DRS orbit for U# has

    z#_k=V# k^(1-p)+o(k^(1-p)),
    V#=V/[p^p (1-p)^(1-p)||V||^2].                  (5.1)

These are state statements, not last-step statements. The exponents satisfy p#=1-p. (5.2)

For weakly infeasible SDPs the inherited relation p=alpha/(1+alpha) between state and trace-escape exponents gives alpha#=1/alpha. (5.3)

Thus the alternative exchanges the small- and large-exponent regimes. Also (2.5) along q gives <a,c>=0 (divide h(q)=O(t^(2p-1)) by t^p). Hence P#V=QV and Q#V=PV: the leading primal and dual recession components exchange, up to the common scalar in (5.1).

## 6. Why this does NOT solve the requested last-step problem

For an actual orbit z_(k+1)=Tz_k, if both h_k=h(z_k) and h_(k+1) are positive, then w_k=Phi(z_k) satisfies

    w_(k+1)=[h_k/h_(k+1)] T# w_k,
    h_(k+1)=h_k-<a,z_(k+1)-z_k>.                    (6.1)

The multiplicative factor is generally not one. This is NOT a conjugacy of the two plain iterations. A last-step theorem for one plain orbit cannot be transferred to the other by simply applying Phi. Eventual positivity and sufficiently precise variation of h_k for all starts have not been established here. Those issues are material, particularly when p<1/2 and the central h tends to zero.

Moreover, applying firm nonexpansiveness of T# to consecutive transformed states reduces algebraically to firm nonexpansiveness of T; it is not an additional independent dissipation estimate.

## 7. Verification and next target

The independently runnable script diagnostics/projective_duality_check.py tests the projector, reflection, operator, residual, involution, and radial identities at 1,000 random symmetric-matrix inputs. The largest absolute discrepancy in the current run was below 2.0e-12. These floating-point checks corroborate but do not replace the algebraic proof above.

The missing universal theorem remains scalar saturation from Checkpoint 01, equivalently k^(1-p)(z_(k+1)-z_k) -> pV. A legitimate continuation must control the radial factor in (6.1), or obtain genuinely new cone-specific damping; the exact central-path identities alone do not close that gap.
