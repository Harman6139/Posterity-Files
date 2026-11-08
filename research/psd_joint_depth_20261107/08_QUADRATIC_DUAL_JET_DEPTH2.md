# Quadratic dual stress jets characterize facial depth <= 2
Research checkpoint, 2026-11-07. This is a rigorous exact algebraic criterion, not a claim that the sharp exponent 1/2 automatically gives degree <=2.

Let K=ker(L), X* PSD uniquely feasible of rank 1<=r<n, U=range(X*), V=U^perp, C=P_V. Uniqueness supplies a positive definite W in K^perp. Let d be minimal facial-reduction degree.

**Theorem.** The following are equivalent:
(a) d<=2.
(b) There are Z0,Z1 in K^perp, lambda>0 and epsilon>0 such that
    S(t)=Z0+t(Z1-C)+lambda*t^2*W >=0 (PSD) for every 0<t<epsilon,
and <S(t),X*> = O(t^2). The contact condition is equivalent to <Z0,X*>=<Z1,X*>=0.

Proof (b=>a): Let t->0 to get Z0>=0. Target contact and CX*=0 imply Z0 and Z1 pair to zero with X*. If Z0=0, S(t)/t -> Z1-C>=0, so Z1>=C, exposing the full nullspace in one stress (d=1). Otherwise Z0 is a first stress with kernel W1 containing U. Compress S(t)/t to W1 and take t->0:
 P_W1 Z1 P_W1 >= P_W1 C P_W1 = P_(W1 intersect V).
Thus Z1 gives a PSD compressed stress positive definite on all remaining null directions; d<=2.

Proof (a=>b): If d=1 choose a first full-null exposing Z0>=0 in K^perp, Z1=0. Then Z0-tC+lambda*t^2W>=0 for small t, and target pairing is lambda*t^2<W,X*>. If d=2 choose first full-rank-in-its-range exposing Z0>=0 and let W1=ker Z0. Choose second stress Z1 in K^perp whose compression to W1 is PSD, annihilates U and is positive definite on W1 intersect V; scale it so L=P_W1(Z1-C)P_W1 is PSD and positive definite on W1 intersect V, zero on U. In decomposition R0=range(Z0), W1=ker Z0, the top-left block of S(t) is A+O(t) with A=Z0|R0>0, the cross block is tB+O(t^2), and the lower block is tL+lambda*t^2 W_W1. Schur complement:
 tL + t^2(lambda W_W1-B^*A^-1B)+O(t^3).
Choose lambda large enough for the parenthesized matrix to be positive definite. Then S(t)>=0 for small t; target pairing is lambda*t^2<W,X*>. QED.

Finite verification: principal minors of S(t) are polynomials. Each must vanish identically or have positive leading nonzero coefficient as t->0+. Thus the certificate is semialgebraically decidable for exact algebraic data.

**Frontier relevance.** If one could show that an optimal square-root *full-matrix* recovery estimate automatically admits such an *integer-power quadratic dual certificate* for C=P_V, this theorem would imply alpha=1/2 => d<=2. But support-function SDP dual multipliers are generally Puiseux, with fractional-order intermediate terms; eliminating them without destroying PSD and contact order is UNPROVED. Hence the endpoint alpha=1/2 at d>=3 is still unresolved.

See local extended memo PSD_Dual_Stress_Jet_Depth2_2026-11-07.md for fuller argument.