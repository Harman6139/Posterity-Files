# Checkpoint 010: the canonical arithmetic carrier

Date: 2026-11-15. This strengthens and corrects a scope statement in checkpoint 001. The terminal domain, not only its affine matrix slice, is independent of the choices of exposing forms. Earlier notes allowed possible dependence; the argument below proves uniqueness.

## Definitions

For a finite union P of closed rational polyhedral cones and a rational affine matrix slice H, let R(P) be the matrices with rational permitted Gram columns. Assume R(P) intersect H is nonempty. Define the set of viable rational column directions

 V_Q(P,H)={u in P intersect Q^n: there exist X in R(P) intersect H and rational tau>0 with X-tau*u*u^T in R(P)}.

The positive coefficient is essential: a prescribed column of arbitrary length need not fit a fixed trace constraint. Define the arithmetic carrier A(P,H)=closure(V_Q(P,H)) in vector space, not matrix space.

## Canonical carrier theorem

The arithmetic facial-reduction algorithm of checkpoint 001 returns exactly A(P,H). Consequently A(P,H) is a finite union of closed rational polyhedral cones, is computable in at most d=n(n+1)/2 proper matrix-span reductions, and is independent of all choices of exposing matrices. Different executions may give different redundant descriptions, but not different sets.

Furthermore

 R(P) intersect H = R(A(P,H)) intersect H,
 closure(R(P) intersect H)=C(A(P,H)) intersect H,
 H intersects ri C(A(P,H)).

Proof. Let P_* be any nonempty terminal output. Every rational feasible Gram factorization survives every reduction column by column, because its nonnegative exposed quadratic values sum to zero. Therefore every u in V_Q(P,H) belongs to P_*; a rational positive weight may be split into rational squares, and positive rescaling does not change membership in a cone.

Conversely choose rational X0 in H intersect ri C(P_*). Such a point exists because H intersect span C(P_*) is a rational affine space and the relevant intersection is relatively open. For any rational u in P_*, choose a sufficiently small positive rational tau with X0-tau*u*u^T still in ri C(P_*). The rational interior-factor lemma gives X0-tau*u*u^T in R(P_*). Hence u is viable. Thus V_Q(P,H)=P_* intersect Q^n. Rational points are dense in each component of P_*, and P_* is a finite union of closed sets, so closure(V_Q)=P_*. This proves uniqueness and all displayed identities.

If no rational completion exists, define the carrier to be empty. The algorithm detects this, even when the original real fiber is feasible. Empty and zero carriers must be distinguished: when the sole feasible matrix is zero, the carrier is {0}, and the empty Gram sum is a valid factorization.

## One completion witnesses every viable rational direction

The same rational X0 works for all u in A(P,H) intersect Q^n, with the coefficient tau allowed to depend on u. There is a rational factorization of X0 containing a strictly positive reserve on a rational rank-one basis of span C(A(P,H)). Such a full-span factorization can be constructed with at most 2d weighted rational atoms (and at most 8d rational Gram columns by four squares). Compressing for width alone gives at most d weighted atoms or 4d Gram columns, but need not preserve the full-span reserve.

Let G_1,...,G_k be the basis atoms, write X0=Y+sum e_i G_i with Y rationally factorable and all e_i>0, and write uu^T=sum a_i G_i. Taking

 0<tau<=min_i(e_i)/(2(1+max_i|a_i|))

keeps every e_i-tau*a_i positive. This gives an explicit insertion certificate. Cramer's rule shows that the coefficient tau and the resulting factors have binary height polynomial in the stored reserve height and the height of u, for fixed n. Thus the carrier is constructive, rather than just an existential restatement of rational factorability.

## Exact rank-one dual alternative

For rational u in the original P, exactly one of the following holds:

(1) u is in the carrier and admits the preceding rational insertion certificate;
(2) the arithmetic reduction chain is infeasible, or at some first stage a selected algebraic quadratic exposer is strictly positive at u, while being nonnegative on the current vector domain and vanishing on every current feasible matrix.

Indeed a rational zero of a selected exposer always survives that step by the coefficient-kernel lemma. Thus a rational direction first removed from a nonempty chain must have strictly positive exposed value. Exposers after the first step need not be copositive on the original domain: the complete preceding restriction chain is part of the certificate. For irrational directions, removal can occur even at quadratic value zero, which is precisely why ordinary real facial reduction is insufficient.

## Consequences and scope

This gives a computable intrinsic vector-domain invariant for exact rational matrix completion, permits simultaneous small insertion of any finite set of viable rational directions, and yields the robust-direction tests in checkpoint 009. It also supplies the invariant preserved in the totally-real descent proof.

In the nonsimplicial interior family of checkpoint 007, the carrier is the full fixed K for every target A_N. The entire shadow objective line lies in the interior of the same genuine matrix-cone face, while crossing N-1 cells of the perfect-form tessellation. The distinction is therefore exact: genuine arithmetic faces govern rational certificate availability, while interior subdivision cells govern local walk length. No polynomial bound in carrier depth, observation coercivity, rational factor heights, input length and binary interior conditioning can control that specified local walk. This is not an impossibility assertion about arbitrary artificial invariants or all local rules.

The canonical-carrier proof is complete internally. A full historical comparison and external proof review are separate requirements; this checkpoint does not certify a journal percentile.
