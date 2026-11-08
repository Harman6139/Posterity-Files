# Universal Dikin–Hessian sharp stability on **all symmetric cones**

**PROVED, 2026-11-07.** Extension of the universal PSD theorem (checkpoint 10) to every finite-dimensional symmetric cone, including direct products. Euclidean Jordan algebra theory and logdet Hessian identities are established mathematical ingredients; no literature priority claim.

## Theorem

Let (E,∘,<.,.>) be a Euclidean Jordan algebra, unit e, Jordan rank R, trace tr and symmetric cone Q of squares. Let L:E→R^m be real linear, x*∈Q uniquely determined by Lx* among Q, K=ker L, and q=||L e||>0. For ε>0 define the unique canonical Jordan maximum-determinant center
    x_ε = argmax{log det_J x: x∈int Q, x-x* - ε e ∈K}.
Let P(z)=2 L_z^2-L_(z²) denote the quadratic representation and define the restricted barrier-Hessian smallest eigenvalue
    λ_ε = min{ <h,P(x_ε^{-1})h>:h∈K, ||h||=1 }.
Put ρ_ε=λ_ε^{-1/2}; if K=0, put ρ_ε=0. Then with fixed positive constants
    SUP{ ||y-x*|| : y∈Q, ||L(y-x*)||≤q ε }  ~  ε+ρ_ε
(two-sided comparison uniformly for all ε>0). Thus the sharp exponent on EVERY symmetric cone is the rational Puiseux order of one canonical restricted barrier-Hessian eigenvalue, capped at one.

## Standard Jordan facts

Q is self-dual; tr e=R. ∇(-logdet_J x)=-x^{-1}, ∇²(-logdet_J x)=P(x^{-1}). The quadratic representation T_x=P(x^{-1/2}) is an order automorphism sending x to e, with T_x²=P(x^{-1}). For h∈E,
    ||T_x h||²=<h,P(x^{-1})h>,
    ||T_x||≤1/min Jordan_eigenvalue(x).
This follows by Peirce decomposition: T_x has multipliers λ_i(x)^(-1) on diagonal Peirce directions, (λ_i(x)λ_j(x))^(-1/2) on offdiagonal ones. Every y∈Q satisfies 0≼y≼tr(y)e and ||y||≤tr(y).

## Proof

Uniqueness implies K∩Q={0}. A strict separator w∈int(Q)∩K⊥ gives bounded shifted affine sections and existence of a unique interior maxdet center. Stationarity along K gives x_ε^{-1}∈K⊥. Put z=ε x_ε^{-1}. The exact trace identity
    R=<x_ε^{-1},x_ε>=<x_ε^{-1},x*>+ε tr(x_ε^{-1})
gives tr z≤R, ||z||≤R, <z,x*><=R ε and x_ε≽(ε/R)e.

Choose a bounded right inverse of L* on K⊥, norm κ. For y∈Q with residual δ,
    ε<x_ε^{-1},y>=<z,x*>+<z,y-x*>
                     ≤R ε + κ R δ.
Apply the order automorphism T_{x_ε}; since tr(T_{x_ε}y)=<x_ε^{-1},y> and every cone element is bounded by its trace times e,
    0≼y≼R(1+κδ/ε)x_ε.                                  (1)
In particular x*≼R x_ε and y≼C0 x_ε at residual δ=qε.

The Dikin radius satisfies
    ρ_ε=max{||h||:h∈K, ||T_{x_ε}h||≤1}.
For any such h, the Jordan spectral norm is ≤1, so e±T_{x_ε}h∈Q, and hence x_ε±h∈Q with residual qε. Their separation 2h gives ω(qε)≥ρ_ε. Independently x*+εe∈Q is a competitor at residual qε and has displacement ε||e||. Thus ω(qε)≥c(ρ_ε+ε).

For an arbitrary competitor y with residual ≤qε choose a right inverse J of L on its image, norm j. Let a=J(L(y-x_ε)) and h=y-x_ε-a∈K. Then ||a||≤2jqε and the Peirce bound gives ||T_{x_ε}a||≤2Rjq. By (1), ||T_{x_ε}y||≤C0√R; also T_{x_ε}x_ε=e. Consequently ||T_{x_ε}h||≤C and ||h||≤Cρ_ε.

Similarly h0=x_ε-x* -εe∈K, and
    ||T_{x_ε}h0||≤√R+R√R+ε||x_ε^{-1}||≤√R+R√R+R,
so ||h0||≤C'ρ_ε. Since y-x*=h+h0+a+εe, we get
    ||y-x*||≤C''ρ_ε+C''' ε.
Taking the supremum proves the universal equivalence. QED.

## Scope and supporting literature

By classification of symmetric cones, this includes real/complex/quaternionic Hermitian PSD, Lorentz (SOC) cones, the exceptional rank-three cone, and finite direct products. It does NOT assert the analogous result for spectrahedral shadows with projected recovery variables. The Jordan identities follow standard Euclidean Jordan theory; see Hauser–Lim (2001), "Self-scaled barriers for irreducible symmetric cones" and standard EJA texts. Bibliographic novelty of the *recovery-modulus consequence* is not independently established.

The theorem unifies sharp stability via one canonical Hessian metric rather than facial-depth-only exponents. The separate fixed-(n,r,d) *arithmetic realization spectrum* remains an open refinement; instance-wise exponent classification is complete.