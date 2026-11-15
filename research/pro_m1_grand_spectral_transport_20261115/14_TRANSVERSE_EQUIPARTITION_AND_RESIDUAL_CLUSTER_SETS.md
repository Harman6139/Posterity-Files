# Checkpoint 14 — transverse equipartition and residual cluster sets

2026-11-15. The general statement uses Checkpoint 12's arbitrary closed convex semialgebraic cone theorem. The explicit spectral application uses the gamma=2 orbit in Checkpoints 07–09, not the original gamma=1 simulation.

## 1. A sharper form of the universal energy law

Use z_k=a+x_k+y_k, d_k=Delta x_k+Delta y_k, H=PV, G=QV, and

 e_k=||Delta y_k||^2-D(||x_(k+1)||)^2>=0.

Assume the equivalent natural-scale conditions of Checkpoint 12. The separate radial limits and static profile give, pointwise,

 k^(2-2p)e_k
   =||k^(1-p)Delta y_k-pG||^2+o(1).                 (1.1)

Proof: expand the square on the right. Its middle term tends to -2p^2||G||^2, while k^(2-2p)D(||x_(k+1)||)^2 tends to p^2||G||^2. This uses the actual radial normal-step limit, not differentiation of a state remainder.

For fixed lambda>1 and m=floor(lambda n), the full kinetic-defect law and orthogonality of P,Q therefore give

 sum_(j=n)^(m-1)j^(2p-2)||j^(1-p)Delta y_j-pG||^2/I_(n,m)
    =X_n(lambda)+o(1),
 sum_(j=n)^(m-1)j^(2p-2)||j^(1-p)Delta x_j-pH||^2/I_(n,m)
    =X_n(lambda)+o(1).                              (1.2)

Thus the nonnegative static inefficiency equals each of the two transverse kinetic defects separately, on proportional time windows. The factor two in the total defect is an asymptotic tangent/normal equipartition. It is valid for arbitrary closed convex semialgebraic cones, not just symmetric cones or the constructed example.

## 2. The gamma=2 normal projection

For the rational system of Checkpoint 08,

 H=cA(E00+E33), G=cA b0(E22+E55), p=1/4,
 P(F06)=F06, Q(F06)=0, P(F26)=0, Q(F26)=F26.

The complete step cluster set is V/4+Rstar{cos(theta)F06+sin(theta)F26}. Applying P and Q gives the exact tangent and normal cluster sets

 Clust{k^(3/4)Delta x_k}=H/4+[-Rstar,Rstar]F06,
 Clust{k^(3/4)Delta y_k}=G/4+[-Rstar,Rstar]F26.       (2.1)

In particular the whitened equation-residual norm does NOT have a leading constant, even though the whole DRS step norm does. Its full cluster interval is

 [||G||/4, sqrt(||G||^2/16+2Rstar^2)].               (2.2)

The radius profile has k^(3/4)D(||x_(k+1)||)->||G||/4. Consequently the pointwise static-efficiency ratio has cluster interval

 [1, sqrt(1+2(2-sqrt(3))/45)].                       (2.3)

The scaled static excess k^(3/2)e_k has cluster interval [0,2Rstar^2], while every proportional-window average X_n(lambda) tends to Rstar^2. Thus occasional near-optimal shadows do not imply eventual saturation or exact velocity.

## 3. Every equality representation sees the failure

Let U={z:A z=b} with ker A=L, allowing arbitrary redundant equations. Exactly Av_k-b=A Delta y_k. Therefore

 Clust{k^(3/4)(Av_k-b)}=A G/4+[-Rstar,Rstar]A(F26).  (3.1)

The vector A(F26) is nonzero because F26 is a nonzero member of L^perp and A is injective there. Hence the raw residual vector never converges at this scale for this orbit, under any equality description of U. Its Euclidean norm also cannot converge: the squared norm of A G/4+t A(F26) is a strictly convex quadratic in t on a nondegenerate interval, and so is not constant. All points of the interval are approached along subsequences by the phase-winding theorem.

Whitening with (AA*)^(dagger/2) restores the canonical interval (2.2), because A*(AA*)^dagger A=Q. Ill-conditioning changes the unwhitened cluster interval but cannot erase the vector obstruction. No full-row-rank hypothesis is needed.

## 4. Actual shadow increments

The spectral expansion gives k^(3/4)(d_(k+1)-d_k)->0: the leading transverse phase changes by O(k^(-1/2)), the radius changes at smaller order, and both scaled remainders tend to zero. Since u_k=P_U z_k and v_k=u_k+d_k, both affine-shadow and cone-shadow scaled increments have the same cluster segment H/4+[-Rstar,Rstar]F06. Their states still share the common leading PSD recession matrix H k^(1/4).

## 5. Scope

These conclusions strengthen the obstruction from a missing vector derivative to failure of a single canonical last-residual norm coefficient. They do not assert nonconvergence of the unscaled residuals, which tend to zero. They do not settle the original gamma=1 start. All cluster-set claims here are consequences of the exact gamma=2 nonlinear trapping and phase proof, not of finite numerical observations.
