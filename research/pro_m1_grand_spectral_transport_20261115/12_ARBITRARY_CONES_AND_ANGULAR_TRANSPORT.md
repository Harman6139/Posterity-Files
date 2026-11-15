# Checkpoint 12 — arbitrary cones and angular transport of static excess

2026-11-15. This extends Checkpoint 10 beyond self-dual cones and identifies its spherical-length consequence. It does not assert a solution for the originally simulated gamma=1 orbit.

## 1. Self-duality is unnecessary

Let K be any closed convex semialgebraic cone in a finite-dimensional Euclidean space E. No pointedness, full dimensionality, homogeneity, or self-duality is assumed. Let U=a+L be disjoint from K at distance zero, with a perpendicular to L. Write P=P_L, Q=I-P and iterate plain affine-first Douglas–Rachford:

    Tz=z+P_K(2P_Uz-z)-P_Uz, z_(k+1)=Tz_k.

Put z_k=a+x_k+y_k and d_k=z_(k+1)-z_k. Use the positive dual cone K*={s:<s,v>>=0 for all v in K}. Moreau decomposition gives

    v_k=P_K(a+x_k-y_k)=a+x_(k+1)+Delta y_k,
    s_k=P_(K*)(-a-x_k+y_k)=y_(k+1)+Delta x_k,
    v_k in K, s_k in K*, <v_k,s_k>=0.

Thus <v_i,s_j>>=0 for all indices i,j. These cross-pairings, not self-duality, are the exact property used in Checkpoint 10. Its common-state, balance, profile, finite-window energy, radial-rigidity, saturation, and norm-coefficient arguments carry over without changing any constant. The central facts and new angular consequences are proved below.

## 2. Central path, profile, and balance

The semialgebraic discounted path uniquely solves Tz(t)-z(t)=(z(t)-a)/t. Nonexpansiveness, divergence, and zero infimal displacement imply a Puiseux first term c t^p, with c nonzero and rational 0<p<1. Comparing the actual orbit with z(t0+k/p), whose iteration defect is o(k^(p-1)), and summing defects proves, for every start,

    z_k=V k^p+o(k^p), V=p^(-p)c.

Put H=PV and G=QV. The central shadows are

    v(t)=a+(1+1/t)x(t)+y(t)/t in K,
    s(t)=x(t)/t+(1+1/t)y(t) in K*.

With E(t)=||x(t)||^2+||y(t)||^2, complementarity gives

    <a,y(t)>=-E(t)/t,
    t(t+1)E'(t)/2=E(t)+t||y(t)||^2.

For the derivative identity, differentiate at the minimum of the nonnegative function h -> <v(t+h),s(t)>. Only the smooth central path is differentiated. Consequently

    H in K, G in K*, <H,G>=0, <a,G>=0,
    ||H||^2=(1-p)||V||^2, ||G||^2=p||V||^2.

Define D(r)=min{||Qv-a||:v in K, ||Pv||<=r}. The minimum exists, is positive at finite r, and decreases to zero. The central point v(t) minimizes the strictly convex function ||Pv||^2/[2(t+1)^2]+||Qv-a||^2/2 over K: its gradient is s(t)/(t+1), in K* and complementary to v(t). Therefore D(||Pv(t)||)=||Qv(t)-a||. Elimination of t gives

    D(r)~p||G|| ||H||^((1-p)/p) r^(-(1-p)/p).

For actual shadows put r_k=||Pv_k||, delta_k=||Qv_k-a||=||Delta y_k||, and e_k=delta_k^2-D(r_k)^2>=0. Then D(r_k)^2~p^2||G||^2 k^(2p-2).

## 3. Universal energy transfer and criterion

For fixed lambda>1 and m=floor(lambda n), put

    I_(n,m)=sum_(j=n)^(m-1) j^(2p-2),
    X_n(lambda)=sum_(j=n)^(m-1)e_j/I_(n,m), A0=p^2||V||^2.

The natural-scale bound d_k=O(k^(p-1)) is equivalent to bounded X_n(lambda) for one, equivalently every, fixed lambda>1. Under that bound,

    k^(1-p)<d_k,V> -> p||V||^2,
    sum_(j=n)^(m-1)||d_j||^2
       =A0 I_(n,m)+2sum_(j=n)^(m-1)e_j+o(I_(n,m)),
    sum_(j=n)^(m-1)j^(2p-2)||j^(1-p)d_j-pV||^2/I_(n,m)
       =2X_n(lambda)+o(1).

The exact vector law k^(1-p)d_k->pV is equivalent to X_n(lambda)->0 for one fixed lambda, and to pointwise static saturation delta_k/D(r_k)->1. No separate natural-scale assumption is required: bounded excess implies it.

### Proof details

Write q_k=||d_k||^2 and w_k=<y_(k+1),Delta y_k>. Firm nonexpansiveness makes q nonincreasing. Expanding the complementary shadows gives, for psi_k=<v_k,s_(k+1)>>=0,

    ||Delta x_(k+1)||^2=w_k-w_(k+1)
                  +<Delta y_k,Delta y_(k+1)>-psi_k,
    sum_(j=n)^(m-1)psi_j<=q_n/2.

Polarization and endpoint shifts imply

    sum_(j=n)^(m-1)q_j=2sum_(j=n)^(m-1)delta_j^2+w_n-w_m+R,
    |R|<=4q_n.

Bounded static excess bounds normal squared energy on all fixed-ratio windows. Averaging selects endpoints in [n/4,n/3] and [2n,3n] with delta^2=O(n^(2p-2)); their w terms are O(n^(2p-1)). Sum the tangent identity and drop -psi to bound tangent squared energy on the intervening interval. Monotonicity of q gives q_n=O(n^(2p-2)); the converse is immediate.

Monotonicity of I-T, the state law, and this bound give longitudinal rigidity by averaging over separated forward/backward proportional windows. Cross-pair actual and central shadows at t=k/p to obtain separate scaled radial limits p||H||^2 and p||G||^2. Thus w_k=p||G||^2 k^(2p-1)+o(k^(2p-1)). Substitute into the exact energy formula and use the profile and balance to get the factor-two law. At p=1/2 the constant leading w endpoints cancel and I tends to log lambda, so no division by 2p-1 occurs.

If X_n(lambda)->0, radial rigidity yields q_j>=[A0-o(1)]j^(2p-2). A fixed positive excess of q_n over A0 n^(2p-2) persists, by monotonicity, on a proportional backward interval. Its positive energy cannot be canceled by the o(1) lower error elsewhere in a containing lambda-window, contradicting the energy law. Hence k^(2-2p)q_k->A0. Expanding ||k^(1-p)d_k-pV||^2 gives the vector law. Its converse and the pointwise-saturation equivalence follow from the profile coefficient. All cross-pairings used here are between K and K*, not two copies of K.

## 4. Spherical-energy identity

Assume the equivalent natural-scale conditions and put nu_k=z_k/||z_k|| on a tail. Radial normalization gives

    k(nu_(k+1)-nu_k)
      =[I-nu_k nu_k*] k^(1-p)d_k/(||z_k||/k^p)+O(1/k).

The scaled steps are bounded, nu_k->V/||V||, and longitudinal rigidity holds. Hence

    k^2||nu_(k+1)-nu_k||^2
      =||k^(1-p)d_k-pV||^2/||V||^2+o(1).

Combining this pointwise geometric identity with Section 3 yields

    sum_(j=n)^(m-1)j^(2p)||nu_(j+1)-nu_j||^2/I_(n,m)
      =2X_n(lambda)/||V||^2+o(1).

The same nonnegative static inefficiency controls both conic shadow optimization and angular kinetic energy. No matrix coordinates or spectral regularity are assumed.

## 5. Exact angular-length and travel constants

For e>=0, the conditions

    X_n(lambda)->e for every fixed lambda>1,
    k^(2-2p)||d_k||^2->A0+2e

are equivalent by the energy identity and monotone density of q. Under either condition, the pointwise identity in Section 4 gives

    k||nu_(k+1)-nu_k|| -> sqrt(2e)/||V||.

Summing actual angular and step norms proves, for fixed K on the tail,

    sum_(k=K)^(n-1)||nu_(k+1)-nu_k||/log n
      ->sqrt(2e)/||V||,
    sum_(k=K)^(n-1)||d_k||/||z_n-z_K||
      ->sqrt(1+2e/(p^2||V||^2)).

For e=0 the angular conclusion is o(log n), NOT finite angular length. For e>0 it is a positive logarithmic divergence despite normalized-state convergence. The theorem applies to all cones in Section 1.

The gamma=2 resonance has e=Rstar^2, giving angular coefficient sqrt(2)Rstar/||V||=(2/3)sqrt(Fstar) and travel factor sqrt(1+(2-sqrt(3))/90), consistent with its independent spectral derivation.

## 6. Exact scope

This is a universal criterion and sharp defect law, not an assertion that all conic orbits have bounded excess or a limiting excess coefficient. Without bounded excess the scaled step norm has unbounded limsup; the natural-scale angular formulas are then not asserted. The saved regular-spectrum theorem supplies zero excess and a power remainder in its stated matrix class, hence finite angular length there. The original gamma=1 orbit and complete historical/journal certification remain separate obligations.
