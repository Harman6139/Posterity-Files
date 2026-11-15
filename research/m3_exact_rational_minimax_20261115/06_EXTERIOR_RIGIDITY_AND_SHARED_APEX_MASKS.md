# Checkpoint 06 — exterior rigidity and the shared-apex obstruction

Date: 2026-11-15. Continuation of the exact-rational minimax research. These are route obstructions, not a universal negative resolution.

## 1. Exterior rigidity for finite squared-hinge sums

THEOREM A. Let d>=2. Let Q be a polynomial on R^d of degree at most two, and let

    G(x)=Q(x)+(1/2)sum_{j=1}^M c_j(<a_j,x>-b_j)_+^2,

where M is finite, c_j are arbitrary real numbers, and every a_j is nonzero. If G(x)=0 for every ||x||>R for some finite R, then G is identically zero.

No convexity, rationality, coefficient bound, or sign restriction on c_j is needed.

PROOF. Group all terms that have the same unoriented zero hyperplane. Choose one affine defining form ell_H(x)=<n_H,x>-t_H for each distinct hyperplane H. A proportional defining form is s ell_H with nonzero s. For s>0 its squared hinge contributes s^2(ell_H)_+^2. For s<0 use the identity

    (-ell_H)_+^2=ell_H^2-(ell_H)_+^2.

Absorb the resulting polynomials into Q. Thus

    G(x)=Q_tilde(x)+(1/2)sum_H gamma_H(ell_H(x))_+^2, (1)

with finitely many DISTINCT hyperplanes.

Fix H. Because d>=2, H is an unbounded affine space of positive dimension. Its intersections with the other distinct hyperplanes form a finite union of proper affine subspaces (parallel hyperplanes do not intersect). These cannot cover the exterior of a ball in H. Choose p in H with ||p||>R that lies on no other hyperplane. There is a ball around p wholly outside B(0,R) that meets no other hyperplane. On each side of H inside that ball, every other summand in (1) has a fixed polynomial expression. The difference of the two constant Hessians is

    gamma_H n_H n_H^T.

Both Hessians are zero because G vanishes on both open half-balls. Since n_H!=0, gamma_H=0. This holds for every H. The remaining polynomial Q_tilde vanishes on an open set and is therefore zero everywhere. QED.

COROLLARY A1. Two finite sums of squared affine hinges in at least two variables cannot be distinct while agreeing outside a Euclidean ball. Thus no nontrivial globally compact difference can be manufactured by changing only a finite diagonal PSD core (or a simultaneously diagonalizable affine core).

An affine symmetric pencil whose coefficient matrices commute internally has a fixed orthogonal simultaneous diagonalization. Its natural PSD-distance objective is a finite sum of squared affine hinges. Two such pencils may use different diagonalizing matrices; the theorem still applies to their difference, since the union of the two finite ridge lists is finite. The result is real-arithmetic as well as rational-arithmetic.

A commuting affine pencil alone cannot be weakly infeasible: its feasibility problem is polyhedral. The relevant application is a commuting core plus a COMMON noncommuting weak-infeasibility tail; the tail cancels in the comparison.

### Critical limitations

This does not imply that a fixed number of arbitrary large queries identifies a hinge objective. A nonzero difference may vanish on open unbounded cones while surviving in an unbounded slab. The theorem gives pairwise rigidity under equality on the ENTIRE Euclidean exterior, not a universal distinguishing query.

It also does not cover all PSD pencils. Noncommuting affine blocks have curved spectral transition sets and need not be finite affine-ridge sums. It cannot be used to refute every conic radial masking construction.

In d=1 the assertion is false: transition hyperplanes are isolated points, and the earlier moment-matched cores do differ only on a bounded interval. Embedding such a function as G(x_1) in R^d produces an unbounded slab of disagreement, not a bounded disagreement region. There is no conflict with the old examples.

## 2. Radial PSD masking exists, but a common center can make optimization trivial

For r>=0 and a known center c in R^d, the rational arrow pencil (when r,c are rational)

    B_r(x)=[[r,(x-c)^T],[x-c,r I_d]]

has eigenvalues r+||x-c||, r-||x-c||, and r with multiplicity d-1. Therefore

    dist_F(B_r(x),S_+)^2/2=(||x-c||-r)_+^2/2.        (2)

Weighted sums of (2) with matching first three radius moments can have common exterior expressions and different interior expressions. Hence Theorem A must not be extended from affine hinges to all PSD-distance objectives.

However every nonnegative combination of (2) vanishes at the same known c, whatever its radii and weights. Appending a known weak-infeasibility tail leaves a zero-query approximate optimizer: choose x=c and take a sufficiently accurate known tail point. This is identification ambiguity, not optimization hardness.

## 3. The more general shared-apex Lorentz construction

Fix a known c and put y=x-c. Consider any finite collection of blocks

    B_i(y)=[[b_i+<a_i,y>, y^T],
            [y, (b_i+<a_i,y>) I_d]],

with ||a_i||<=1. A block is PSD exactly when

    b_i+<a_i,y> >= ||y||.                            (3)

If all blocks are simultaneously feasible at some finite y, (3) implies, for every i,

    b_i >= ||y||-<a_i,y> >= (1-||a_i||)||y|| >=0.

It follows that every B_i(0) is PSD. Thus the known common apex x=c is feasible for every feasible instance in this entire class, independently of all hidden b_i,a_i. Positive weights and additional zero scalar blocks do not change the conclusion.

The argument also applies if the blocks merely have distance tending to zero along a sequence: if b_i<0, their least eigenvalue obeys b_i+<a_i,y>-||y||<=b_i<0 at EVERY y, making a zero residual impossible. Hence zero infimum again requires all b_i>=0 and supplies the common apex.

This rules out a proposed architecture in which every unknown constraint is hidden inside a common radial exterior with subunit affine tilt and the nonattainment is supplied separately. It does not cover different centers, superunit tilts, other spectral couplings, or arbitrary pencils.

## 4. Research consequence and attribution

These proofs identify two concrete difficulties with a global conic mask: finite affine hinges have unbounded transition hyperplanes, while the displayed common-center radial alternatives possess a common feasible point. Neither mechanism yields the requested new hard distribution.

The Hessian-jump reasoning is elementary and related to standard ridge-function/ReLU identification arguments. No independent historical-priority certification is claimed. The Clifford-size obstruction in checkpoint 07 addresses a different radial architecture; no assertion that all radial PSD masks need exponential matrix order is made.

The original rational exact lower bound and a universal disproof remain unproved.
