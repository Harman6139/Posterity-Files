# Checkpoint 01 — universal local averaging with a sharp efficiency constant

Date: 2026-11-15. This is a theorem about postprocessing the original plain DRS orbit. It neither changes the iteration nor claims that raw last steps converge. Its proof does NOT use the proposed order-seven counterexample or assume bounded static excess.

## 1. Setup and exact theorem

Let K be any closed convex semialgebraic cone in a finite-dimensional Euclidean space. Let U=a+L, a perpendicular to L, be disjoint from K at distance zero. Set P=P_L, Q=I-P and

    Tz=z+P_K(2P_U z-z)-P_U z, z_(k+1)=Tz_k,
    x_k=Pz_k, y_k=Qz_k-a,
    d_k=z_(k+1)-z_k,
    v_k=P_K(a+x_k-y_k).

All starts are allowed. The inherited tame common-state theorem gives, for some rational p in (0,1), V!=0 and eta>0,

    z_k=V k^p+O(k^(p-eta)).                         (1.1)

Shrink eta to be less than p when necessary. Put H=PV and G=QV. The complementary-shadow balance and static-profile theorem gives

    ||H||^2=(1-p)||V||^2, ||G||^2=p||V||^2,
    D(r)=min{||Qv-a||:v in K, ||Pv||<=r},
    D(r)=K0 r^(-beta)(1+O(r^(-kappa))),
    beta=(1-p)/p, K0=p||G|| ||H||^beta, kappa>0.    (1.2)

The positive-power remainder for D follows from one-variable semialgebraic growth. The underlying proofs are in baseline 30–31 and spectral checkpoints 10/12. Only the tame CENTRAL path is differentiated there; (1.1) is not differentiated.

Take integer h=h_n with h/n asymptotic to 1/log(n), and n-h>=1. Define

    vbar_n=(1/(2h)) sum_(j=n-h)^(n+h-1) v_j,
    dbar_n=(z_(n+h)-z_(n-h))/(2h).

Then vbar_n belongs to K exactly. Every such orbit satisfies

    n^(1-p) dbar_n -> pV,
    n^(-p) P vbar_n -> H,
    n^(1-p)(Q vbar_n-a) -> pG.                     (1.3)

More precisely, writing rho=h/n,

    n^(1-p) dbar_n
       =pV+[p(p-1)(p-2)/6] rho^2 V+o(rho^2),
    n^(-p) P vbar_n
       =H+[p(p-1)/6] rho^2 H+o(rho^2),
    n^(1-p)(Q vbar_n-a)
       =pG+[p(p-1)(p-2)/6] rho^2 G+o(rho^2).       (1.4)

In particular the exact asymptotic cost of nonnegative local averaging is

    (log n)^2 [ ||Q vbar_n-a||/D(||P vbar_n||)-1 ]
         -> (1-p)/6.                              (1.5)

The averaged cone shadows are therefore asymptotically optimal for the independent static problem D, at their own achieved primal radius. This is valid with singular leading spectra, unknown p and eta, and regardless of any natural-scale bound for the individual d_k.

## 2. Proof by finite differences, not differentiating an orbit

The exact complementary-shadow identity is

    v_j=a+x_(j+1)+(y_(j+1)-y_j).

Thus

    P vbar_n=(1/(2h)) sum_(j=n-h)^(n+h-1)x_(j+1),
    Q vbar_n-a=(y_(n+h)-y_(n-h))/(2h).             (2.1)

Convexity of K proves cone feasibility of vbar_n.

For a general vector sequence w_j=W j^p+O(j^(p-eta)), the centered secant satisfies, uniformly when h=o(n),

 n^(1-p)(w_(n+h)-w_(n-h))/(2h)
   = W [((1+rho)^p-(1-rho)^p)/(2rho)]
       +O(n^(-eta)/rho).

Taylor expansion of the SCALAR function (1+s)^p on |s|<=1/2 gives

    ((1+rho)^p-(1-rho)^p)/(2rho)
      =p+p(p-1)(p-2)rho^2/6+O(rho^4).

Since rho is asymptotic to 1/log n, n^(-eta)/rho=o(rho^2). This proves the first and third expansions in (1.4), applying the finite difference to z and y respectively.

For the mean of x_(j+1), monotonicity of the scalar function t^p bounds its right Riemann sum minus its integral by O(n^(p-1)). Therefore

 (1/(2h)) sum_(j=n-h)^(n+h-1)(j+1)^p
  = n^p {[(1+rho)^(p+1)-(1-rho)^(p+1)]/[2rho(p+1)]
           +O(1/n)}
  = n^p {1+p(p-1)rho^2/6+O(rho^4+1/n)}.

The mean of the state remainders is O(n^(p-eta)). Both n^-1 and n^-eta are o(rho^2), proving the middle expansion. This proves (1.3)–(1.4) without ever taking a discrete derivative of an unspecified little-o remainder.

## 3. The efficiency coefficient

Since H,G are nonzero, (1.4) yields

 rbar_n=||P vbar_n||
   =||H|| n^p [1+p(p-1)rho^2/6+o(rho^2)],
 deltabar_n=||Q vbar_n-a||
   =p||G|| n^(p-1)
      [1+(p-1)(p-2)rho^2/6+o(rho^2)].

Insert rbar_n into (1.2). The Puiseux relative remainder is O(n^(-p*kappa)), hence o(rho^2). Consequently

 D(rbar_n)=p||G|| n^(p-1)
      [1+(1-p)^2 rho^2/6+o(rho^2)].

Subtract the two coefficients:

    [(p-1)(p-2)-(1-p)^2]/6=(1-p)/6.

Since rho^2(log n)^2->1, (1.5) follows. In particular the sharp second-order inefficiency is positive, as it must be because D is the best attainable residual at the permitted radius. QED.

## 4. Original equation residuals, including redundant equations

For any equality description U={z:A z=b} with ker A=L, the exact identity is

    A vbar_n-b=A(Q vbar_n-a).

On range A, the Moore–Penrose whitening satisfies

    ||(AA*)^(dagger/2)(A vbar_n-b)||=||Q vbar_n-a||.

Therefore

    n^(1-p)(A vbar_n-b)->pAG!=0.

The nonzero coefficient follows because G is a nonzero member of L^perp and A is injective on L^perp. Ill-conditioning can change its norm but redundant equations cannot erase the limit. The same second-order scalar coefficient in (1.4) multiplies AG.

For PSD cones, tr(vbar_n)~tr(H)n^p. Hence the construction attains residual exponent 1-p=1/(1+alpha) while its size has exponent p=alpha/(1+alpha), along the ORIGINAL unanchored orbit. The size-versus-residual optimum asserted is for D and the specified Frobenius primal radius, not an oracle-complexity minimax result.

## 5. Streaming implementation with constant matrix storage

The theorem does not require storing a sliding window of n/log n states. Choose an initial block start b>=3 and put

    h=max(1,floor(b/log(b+2))), n=b+h.

During the next 2h ordinary DRS steps accumulate v_j in one running sum and retain the starting state z_b. At the end output

    vbar=sum(v_j)/(2h), dbar=(z_(b+2h)-z_b)/(2h),

then start the next block at b+2h. These block centers satisfy h/n~1/log n, and successive output times have ratio tending to one. The entire theorem holds along them. The required storage is a fixed number of vectors/matrices, independent of the iteration count. No estimate of p, alpha, eta, a spectral phase, or D is needed to run the postprocessor. D is used only to prove the efficiency guarantee.

A measured equation residual is a valid finite approximate-feasibility certificate for the output cone point. It does NOT certify weak infeasibility in finite time. Also dbar is a mean displacement; it is NOT asserted equal to T applied to a mean state minus that state.

## 6. More general windows and what cannot be inferred

For any h=o(n), the proof gives a normalized velocity error

    O((h/n)^2+n^(1-eta)/h).

If a valid eta is known, h of order n^(1-eta/3) balances these errors and yields O(n^(-2eta/3)), after reducing eta below 1 if necessary. The logarithmic choice is parameter-free and valid for every positive eta. It is intentionally more conservative.

The theorem makes no raw last-iterate claim and leaves the universal raw bound open. Its new optimization consequence is an implementable, vanishing-relative-window recovery of the exact residual vector and an asymptotically optimal cone point, including a sharp universal efficiency coefficient, with no bounded-excess assumption.
