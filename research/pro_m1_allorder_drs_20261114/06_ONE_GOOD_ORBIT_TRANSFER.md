# Checkpoint 06 — one-good-orbit transfer above the square-root threshold

Status: the theorem and proof below are complete. They do NOT prove that a good orbit exists for every weakly infeasible SDP. Hence they do not close the requested all-order last-step theorem. No historical-priority assertion is made.

## Theorem

Let T be firmly nonexpansive on a finite-dimensional Euclidean space. Suppose one orbit w_(k+1)=T w_k satisfies

    w_k=V k^p+o(k^p), V nonzero, 1/2<=p<1,
    k^(1-p)(w_(k+1)-w_k) -> pV.

Then EVERY orbit z_(k+1)=T z_k satisfies

    z_k=V k^p+o(k^p),
    k^(1-p)(z_(k+1)-z_k) -> pV.

In particular, for the target affine–PSD DRS class with p>=1/2, proving the last-step law for a single actual orbit suffices to prove it for all starts. A regularized or anchored path is not such an orbit.

## 1. Square-summable difference of velocities

Put d_k=z_(k+1)-z_k and e_k=w_(k+1)-w_k. Firm nonexpansiveness gives

    ||z_(k+1)-w_(k+1)||^2+||d_k-e_k||^2
        <=||z_k-w_k||^2.

Consequently

    sum_(k>=0)||d_k-e_k||^2<=||z_0-w_0||^2.          (1)

Nonexpansiveness also gives bounded distance between the states, hence the asserted state expansion for z. Both scalar sequences ||d_k|| and ||e_k|| are nonincreasing. Set c=p||V||>0 and a=1-p in (0,1/2]. The hypothesis says ||e_k||~c k^(-a).

## 2. A monotone-window argument fixes the step norm

We prove ||d_k||~c k^(-a). Suppose first that, on an infinite subsequence,

    ||d_k|| >= (1+epsilon)c k^(-a)

for some epsilon>0. Choose lambda in (0,1) sufficiently close to one that lambda^(-a)<1+epsilon/4. Uniform regular variation of the explicit power and ||e_j||~c j^(-a) imply, for all large such k and every integer j between lambda k and k,

    ||e_j|| <= (1+epsilon/2)c k^(-a).

Monotonicity gives ||d_j||>=||d_k|| on that window. The reverse triangle inequality thus yields

    sum_(j=ceil(lambda k))^k ||d_j-e_j||^2
        >= C k^(1-2a) = C k^(2p-1),                 (2)

where C>0 is independent of the subsequence. But the sum on the left is bounded by the tail of the convergent series (1), which tends to zero. The right is bounded below by C since p>=1/2. Contradiction.

For a lower deviation ||d_k||<=(1-epsilon)c k^(-a), with 0<epsilon<1, choose lambda>1 close enough that lambda^(-a)>1-epsilon/4. On the forward window k<=j<=lambda k, monotonicity gives ||d_j||<=||d_k|| and the asymptotic for e gives ||e_j||>=(1-epsilon/2)c k^(-a). The same contradiction follows. Therefore

    k^(1-p)||d_k|| -> p||V||.                         (3)

The fact that a macroscopic window has nonvanishing squared energy at p=1/2 is exactly what makes the endpoint work. No disjoint-subsequence selection is needed, because the whole series tail tends to zero.

## 3. Recovering the vector from the state and norm

For completeness we give the needed longitudinal argument. Monotonicity of I-T gives

    <d_k-d_j,z_k-z_j><=0.                            (4)

By (3), d_k=O(k^(p-1)). Fix h in (0,1/2). Uniformly for j/k in [1+h,1+2h], the state expansion and the step bound in (4) give

    <d_k,V> >= <d_j,V>+o(k^(p-1)).                   (5)

Average over those j. The average of d_j telescopes between the two corresponding endpoints, so

    liminf k^(1-p)<d_k,V>
      >=||V||^2[(1+2h)^p-(1+h)^p]/h.

Using j/k in [1-2h,1-h] similarly gives

    limsup k^(1-p)<d_k,V>
      <=||V||^2[(1-h)^p-(1-2h)^p]/h.

Let h decrease to zero. Both bounds tend to p||V||^2. Together with (3), expansion of the squared distance gives

    ||k^(1-p)d_k-pV||^2 -> 0.

This proves the theorem.

## 4. Limits of this route

For p<1/2, the lower bound in (2) tends to zero and is compatible with a finite total difference energy. Milestone 35 already supplies a semialgebraic analytic firmly nonexpansive map with one good axial orbit and bad nonaxial orbits at p=1/5. Thus transfer for all positive p is false in the general firmly nonexpansive class. Whether the additional affine–PSD structure repairs it below 1/2 is precisely part of the unresolved task.

The theorem does NOT establish existence of a good orbit at p>=1/2. In particular, treating a discounted curve as an actual orbit would be an invalid shortcut. The projective duality in Checkpoint 05 also does not remove this issue: its transformed actual iterates carry a nonconstant radial multiplier.

## 5. Priority clarification on Checkpoint 05

Milestone 12 of the immutable baseline already proves reciprocity of the original and normalized-alternative SDP escape exponents. Thus alpha#=1/alpha in Checkpoint 05 is not a new project result. The additional formulas established there are the exact pointwise DRS projective identity, exact zero-anchor discounted-path relation, and the resulting explicit common-state coefficient. Their historical originality has not been independently certified.
