# Checkpoint 01 — primal–dual balance and an exact scalar saturation criterion

Date: 2026-11-14. This reconstructs and checks the mathematical reduction visible in the surviving eleven-page draft preview. It is NOT a proof of the universal last-iterate conjecture, and is not claimed as a new result relative to that lost draft. The proof below is complete conditional on the inherited common-state theorem (Milestones 30–31).

## 1. Setup and exact shadow identities

Work in a finite-dimensional Euclidean space E with a closed self-dual cone K. For the target problem E=S^m with the Frobenius inner product and K=S_+^m. Write U=a+L, where a=P_U(0) lies in L^perp, P=P_L, Q=I-P. Assume U is weakly infeasible. Let

    Tz=z+P_K(2P_Uz-z)-P_Uz,    z_(k+1)=Tz_k.

Set

    z_k=a+x_k+y_k,  x_k=Pz_k,  y_k=Qz_k-a,
    d_k=z_(k+1)-z_k=Delta x_k+Delta y_k,
    v_k=P_K(a+x_k-y_k),
    s_k=P_K(-a-x_k+y_k).

Moreau decomposition and the update give EXACTLY

    v_k=a+x_(k+1)+Delta y_k,
    s_k=y_(k+1)+Delta x_k,
    v_k,s_k in K,  <v_k,s_k>=0.                       (1.1)

For PSD matrices this also gives v_k s_k=0. No differentiability or spectral simplicity is used.

Since T=(I+R_K R_U)/2 and the reflected projections are nonexpansive, T is firmly nonexpansive. Thus q_k=||d_k||^2 is nonincreasing. Moreover

    q_k-q_(k+1) >= ||d_(k+1)-d_k||^2.                (1.2)

The inherited theorem gives, for all starts,

    z_k=V k^p+o(k^p),  V!=0, 0<p<1,
    H=PV, G=QV,  V=H+G.                             (1.3)

In the SDP setting p=alpha/(1+alpha), where alpha is the minimum-trace escape exponent. We do not differentiate (1.3).

## 2. Discounted path and exact primal–dual balance

Let z(t) solve

    Tz(t)-z(t)=(z(t)-a)/t,

and set x(t)=Pz(t), y(t)=Qz(t)-a, E(t)=||x(t)||^2+||y(t)||^2. The contraction equation makes this path unique. The inherited semialgebraic theorem supplies

    z(t)-a=p^p V t^p+o(t^p),

with differentiable Puiseux expansions on a tail. Its complementary shadows are

    v(t)=a+(1+1/t)x(t)+y(t)/t,
    s(t)=x(t)/t+(1+1/t)y(t).                          (2.1)

Complementarity yields the exact scalar identity

    <a,y(t)>=-E(t)/t.                                (2.2)

On a smooth tail, <v'(t),s(t)>=0. Indeed for fixed t the nonnegative function h -> <v(t+h),s(t)> has a minimum zero at h=0. Substituting (2.1) gives

    t(t+1) E'(t)/2=E(t)+t||y(t)||^2.                 (2.3)

Apply Puiseux asymptotics only to this definable path, not the actual orbit. Since E(t)~p^(2p)||V||^2 t^(2p), (2.3) proves

    ||G||^2=p||V||^2,
    ||H||^2=(1-p)||V||^2.                            (2.4)

Also (2.1) gives H,G in K; P,Q give <H,G>=0; and (2.2) gives <a,G>=0. In particular BOTH H and G are nonzero. For PSD matrices HG=0 and V is PSD.

This balance is unconditional for the target SDP class, using the inherited common-state theorem. In particular a leading unwhitened equation residual, if the proposed last-step law holds, CANNOT vanish merely because the equality description is redundant: if U={z:Az=b}, then ker A=L, so AG=0 and G in L^perp would force G=0, contrary to (2.4). Ill-conditioning may make its norm small but not zero.

## 3. Exact minimum-radius profile

Define

    D(r)=min{||Qv-a||: v in K, ||Pv||<=r}.

The minimum exists: v=0 gives a finite residual bound; on any relevant sublevel the P and Q components are both bounded, so compactness applies. Weak infeasibility implies D(r)>0 for finite r and D(r)->0.

For t>0, v(t) is the UNIQUE minimizer over K of

    F_t(v)=||Pv||^2/[2(t+1)^2]+||Qv-a||^2/2.         (3.1)

Indeed its gradient at v(t) is s(t)/(t+1), an element of K orthogonal to v(t), which is exactly the convex optimality condition. The positive quadratic weights give strict convexity and coercivity.

Consequently, with r(t)=||Pv(t)|| and delta(t)=||Qv(t)-a||,

    D(r(t))=delta(t).

A smaller residual at no larger P-radius would contradict (3.1). On a tail r(t) is strictly increasing and tends to infinity by its Puiseux expansion, so these radii cover a tail. Put beta=(1-p)/p. The expansions in Section 2 yield

    D(r) ~ p ||G|| ||H||^beta r^(-beta).              (3.2)

In particular every actual orbit satisfies the sharp lower bound

    liminf k^(1-p)||Delta y_k|| >= p||G||.            (3.3)

This is because v_k is cone-feasible, Pv_k=x_(k+1), Qv_k-a=Delta y_k, and ||x_(k+1)||~||H||k^p.

## 4. Two-shadow energy, exactly

Define nonnegative cross-complementarity terms

    phi_k=<v_(k+1),s_k>, psi_k=<v_k,s_(k+1)>,
    w_k=<y_(k+1),Delta y_k>.

Expanding (1.1) at consecutive indices gives

    ||Delta x_(k+1)||^2
       =w_k-w_(k+1)+<Delta y_k,Delta y_(k+1)>-psi_k,  (4.1)

and

    phi_k+psi_k
       =[q_k-q_(k+1)-||d_(k+1)-d_k||^2]/2.          (4.2)

For (4.2), expand <v_(k+1)-v_k,s_(k+1)-s_k>; complementarity makes it -(phi_k+psi_k), while the P/Q decomposition makes it [q_(k+1)-q_k+||d_(k+1)-d_k||^2]/2.

Thus for any m>n,

    0<=sum_(j=n)^(m-1) psi_j<=q_n/2.                 (4.3)

These identities retain the PSD/cone complementarity structure absent from an arbitrary firmly nonexpansive resolvent. They do not by themselves establish scalar saturation.

## 5. A longitudinal rigidity lemma

Let a nonexpansive map on a finite-dimensional Euclidean space have an orbit z_k=Vk^p+o(k^p), V!=0, 0<p<1. Suppose d_k=O(k^(p-1)). Then

    k^(1-p)<d_k,V> -> p||V||^2.                       (5.1)

Proof. Monotonicity of I-T gives

    <d_k-d_j,z_k-z_j><=0.

For j/k in a compact interval separated from 1, insert the state asymptotic and the assumed uniform step bound. Uniformly on such intervals,

    <d_k,V> >= <d_j,V>+o(k^(p-1))  when j>k,
    <d_k,V> <= <d_j,V>+o(k^(p-1))  when j<k.

Average the first inequality over j between ceil((1+h)k) and floor((1+2h)k). The average on the right telescopes to an inner product of two states. Hence

    liminf k^(1-p)<d_k,V>
       >=||V||^2[((1+2h)^p-(1+h)^p)/h].

Average the second inequality over j between ceil((1-2h)k) and floor((1-h)k), 0<h<1/2, to obtain the corresponding upper bound with [(1-h)^p-(1-2h)^p]/h. Let h decrease to zero. Both bounds tend to p||V||^2. This proves (5.1).

No discrete state remainder is differentiated.

## 6. The exact criterion

Under the target SDP hypotheses and inherited state theorem, the following three statements are EQUIVALENT for a given orbit:

(A) k^(1-p)d_k -> pV.
(B) k^(1-p)||Delta y_k|| -> p||G||.
(C) ||Qv_k-a|| / D(||Pv_k||) -> 1.

Thus the full vector last-step conjecture is exactly equivalent to asymptotic saturation of the minimum equation-distance profile by the ACTUAL cone shadows. A proof that all affine–PSD DRS orbits satisfy (C) is still missing.

Proof. (A) implies (B) by applying Q. Formula (3.2) and the inherited state law make (B) and (C) equivalent. It remains to prove (B) implies (A).

### 6.1 Coarse bound on the whole step

Under (B), Delta y_k=O(k^(p-1)), y_k=O(k^p), and w_k=O(k^(2p-1)). Sum (4.1) on a window n<=j<m with m comparable to 2n, dropping -psi_j. This gives

    sum_(j=n)^(m-1)||Delta x_(j+1)||^2=O(n^(2p-1)).

The corresponding Delta y squared sum has the same bound. Monotonicity of q then gives q_k=O(k^(2p-2)). This argument remains valid when 2p-1 is negative or zero: it is a finite-window estimate, not an invalid divergent-tail summation.

### 6.2 The normal vector itself converges

Compare the actual v_k with the central dual cone point s(t) at t=k/p. Cone positivity gives <v_k,s(t)>=0. By (2.2), its term involving a is known exactly. Using (1.1), the state expansions, and the coarse normal-step bound, divide by k^(2p-1) to obtain

    0 <= -p||V||^2+p||H||^2
                  +<k^(1-p)Delta y_k,G>+o(1).

Hence liminf <k^(1-p)Delta y_k,G> >= p||G||^2. Assumption (B) fixes the norm at p||G||. Expanding the squared distance to pG gives

    k^(1-p)Delta y_k -> pG.                            (6.1)

### 6.3 Exact macroscopic-window energies

Equation (6.1) gives

    w_k=p||G||^2 k^(2p-1)+o(k^(2p-1)),
    <Delta y_k,Delta y_(k+1)>
       =p^2||G||^2 k^(2p-2)+o(k^(2p-2)).

For each fixed lambda>1, sum (4.1) from n to floor(lambda n)-1. By (4.3) and the coarse q bound, the sum of psi terms is O(n^(2p-2)), negligible on the n^(2p-1) scale. The endpoint term and Riemann sum give

    sum ||Delta x_(j+1)||^2
       =p(1-p)||G||^2 integral_n^(lambda n) t^(2p-2)dt
          +o(n^(2p-1))
       =p^2||H||^2 integral_n^(lambda n) t^(2p-2)dt
          +o(n^(2p-1)),

where (2.4) is used in the last equality. At p=1/2 the integral is log(lambda), the leading endpoint constants cancel, and their remaining difference is o(1); the same formula holds without division by 2p-1.

Adding the Q energies, and shifting endpoints by at most one index, yields

    sum_(j=n)^(floor(lambda n)-1) q_j
       =p^2||V||^2 integral_n^(lambda n) t^(2p-2)dt
          +o(n^(2p-1)).                              (6.2)

### 6.4 Monotone density and the vector

Forward and backward macroscopic-window averages bound the nonincreasing q_k. Insert (6.2), then let lambda decrease to 1. This proves

    k^(2-2p)q_k -> p^2||V||^2.                        (6.3)

The longitudinal lemma gives k^(1-p)<d_k,V> -> p||V||^2. Combining it with (6.3) and expanding ||k^(1-p)d_k-pV||^2 proves (A). QED.

## 7. Equality residuals, including redundancy

For any equality description A with ker A=L, Av_k-b=A Delta y_k. On range A, use the Moore–Penrose square root. Then exactly

    ||(AA*)^(dagger/2)(Av_k-b)||=||Delta y_k||.

This follows because A*(AA*)^dagger A=Q. No full row rank is needed. Under any equivalent condition in Section 6,

    k^(1-p)(Av_k-b) -> pAG !=0,
    k^(1-p)||d_k|| -> p||V||,
    k^(1-p)||Delta y_k|| -> p||G||,
    k^(1-p)||Delta x_k|| -> p||H||.

The nonvanishing pAG is unconditional as a candidate coefficient by Section 2; the asserted vector convergence remains conditional on saturation.

## 8. Exact unresolved statement

The universal task has NOT been completed. The outstanding statement is

    ||Qv_k-a|| / min{||Qv-a||:v in S_+^m,
                                  ||Pv||<=||Pv_k||} -> 1

for every weakly infeasible affine–PSD pair, every matrix order, and every start. Proving lower bounds, norm orders, ergodic averages, or the same property for a discounted/anchored path does not prove this statement. A generic-map counterexample does not refute it. This checkpoint deliberately makes no originality, journal-percentile, or submission-ready claim.
