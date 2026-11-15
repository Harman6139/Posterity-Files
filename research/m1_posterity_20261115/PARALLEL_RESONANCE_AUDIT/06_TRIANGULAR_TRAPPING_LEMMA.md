# Checkpoint 06 — a mixed-speed triangular trapping lemma

2026-11-15. Parent research snapshot 637d4417c63751d1bfaef51d4ecd23549081ae15. This lemma is proved below. Its application to the gamma=2 SDP still requires the normalized-map audit in Section 5. No SDP counterexample is certified by this checkpoint alone.

## 1. Abstract hypotheses

Consider a discrete map in variables tau>0, a scalar charge E, an amplitude F, compact angular variables theta, and finitely many error blocks e_1,...,e_r. Each error block carries a fixed norm. Fix F_*>0 and a closed amplitude interval [l,u] containing F_* in its interior, with 0<l<F_*<u. Work on a slightly larger compact amplitude/angular domain and a charge interval [E_-,E_+]. Suppose the following expansions are uniform whenever all error blocks belong to fixed bounded sets:

    tau_next = tau - c tau^3 + O(tau^4), c>0;
    E_next-E = O(tau^3);
    F_next-F = tau^2 g(F) + O(tau^3).

Here g is continuous and locally Lipschitz, is positive on [l,F_*), negative on (F_*,u], and vanishes at F_*. Angular variables remain in their prescribed compact space (a circle, for example). A redundant radial representation of angle is also allowed if its radius is controlled by F and the bounded errors.

For each error block j, assume one of the following two forms, uniformly on compact sets of all variables:

FAST:
    e_j,next = A_j(theta,E,F)e_j
                  + f_j(theta,E,F,e_1,...,e_(j-1)) + O(tau),
    ||A_j|| <= q_j < 1.

SLOW:
    e_j,next = e_j + tau[-B_j(theta,E,F)e_j
                  + f_j(theta,E,F,e_1,...,e_(j-1))] + O(tau^2),
    ||I-tau B_j|| <= 1-kappa_j tau for all small tau,
    kappa_j>0.

All f_j are continuous. Remainder constants may depend on every chosen error bound, but the DISPLAYED leading forcing for block j depends only on earlier blocks. This last assertion is an algebraic hypothesis, not a consequence of pointwise big-O notation.

## 2. The invariant-region theorem

There are finite bounds M_j and tau_0>0 such that any state with

    0<tau<=tau_0, ||e_j||<=M_j,
    F in [l,u], E in a fixed strict interior subinterval

generates an infinite orbit satisfying the same amplitude and error bounds and staying in [E_-,E_+]. The initial charge margin must exceed C tau_0; equivalently choose tau_0 after fixing that margin. This statement includes all initial errors tending to zero as tau tends to zero.

Proof. Choose M_j successively. Once the earlier M_i are fixed, continuity on a compact set bounds the leading forcing by K_j. In a fast block choose M_j>K_j/(1-q_j)+1. In a slow block choose M_j>K_j/kappa_j+1. Only after all these finitely many choices are made choose tau_0. Then all remainder constants are finite. In fast blocks the strict leading inward margin dominates O(tau); in slow blocks its positive multiple of tau dominates O(tau^2). Thus none of the error blocks can be the first to leave its ball. This is the precise step that avoids circular choices of big-O constants.

For the amplitude, choose small fixed protective bands next to l and u on which g has the corresponding strict inward sign. For small tau, the O(tau^3) term is dominated by the tau^2 drift there. Uniformly small one-step changes prevent a jump across a whole protective band. Thus F cannot exit [l,u].

For the charge, shrink tau_0 so that

    (c/2) tau^3 <= tau-tau_next <= (3c/2) tau^3.

Consequently sum_(k<n) tau_k^3 <= 2 tau_initial/c on every finite orbit segment in the region. A uniform bound |Delta E|<=C_E tau^3 gives total charge change at most 2 C_E tau_initial/c. Choose tau_0 to make this smaller than the initial charge margin. Positivity and decrease of tau also hold for small tau. A finite no-first-exit induction now proves invariance for every n. No infinite-time estimate has been assumed to prove the finite induction.

## 3. Asymptotic conclusions

Within the invariant region tau decreases to zero. A positive limiting tau would contradict its decrement lower bound. Expansion gives

    tau_next^(-2)-tau^(-2)=2c+O(tau),
    tau_k^(-2)/k -> 2c.

In particular sum tau_k^2=infinity and sum tau_k^3<infinity. For every fixed epsilon>0, g is bounded away from zero on the compact portions of [l,u] outside (F_*-epsilon,F_*+epsilon). The O(tau^3) error is eventually dominated by half this drift. The divergent sum of tau^2 forces entry into that neighborhood; small jumps and the inward signs prevent exit from a slightly larger neighborhood. Letting epsilon decrease to zero proves F_k->F_*.

If an unwrapped phase obeys

    phi_next-phi = -omega tau+O(tau^2), omega>0,

then its increments tend to zero and its sum tends to minus infinity, because tau_k is asymptotic to (2ck)^(-1/2). First crossings of angles modulo 2pi prove that every angular direction is a cluster direction.

## 4. How this repairs the draft's logical structure

For Checkpoint 05 set tau=t^2, c=2c0, g(F)=a0 F-B0 F^2. The amplitude equilibrium is F_*=(2-sqrt(3))/640. Its proposed normalized errors, in the required order, are:

1. auxiliary reset blocks Ad/t^5, Bd/t^5, fa/t^4;
2. ((C,G)-Psi(H,b))/tau;
3. (H-H0)/tau;
4. (chi-ell eta)/tau;
5. ((Ca,Ga,Q)-psi_a(j,xi,eta))/tau;
6. (j-jstar(xi,eta))/tau;
7. ((fs+1/2)/tau-fs0)/tau.

The symmetric and asymmetric fast matrices are Ms and Ma in Checkpoint 05. The two slow diagonal coefficients should both be kappa=9sqrt(3)/8. The other blocks should be resets at leading order. The bounded parameter beta=(b-b0)/tau is controlled by the exact charge identity, rather than treated as an unproved decaying error.

This lemma removes the need to guess tube constants numerically IF the exact normalized map has this triangular form. Merely restating the old unnormalized expansions is not enough to verify it.

## 5. Audit currently underway, not a theorem claim

An independent 80-decimal one-step diagnostic was run using the actual Frobenius affine projection and separate 4x4/3x3 PSD eigendecompositions. At tau=10^-12, xi=1/50, eta=1/100, it supports the proposed order: the leading normalized auxiliary outputs do not depend on the error inputs; the symmetric fast block depends on itself; the H slow block depends on it; the chi reset depends on H; the asymmetric fast block depends only on previous blocks and itself; the j slow block depends only on previous blocks and itself; and the fs reset is last.

For example the asymmetric Ga error has a leading dependence on the auxiliary fa error. This must be retained, but it is harmless if fa is placed first. A proof must establish these vanishing dependencies exactly and uniformly around the full phase circle. The finite diagnostic is not that proof, nor a uniform trapping certificate.

Current status: the abstract lemma and its asymptotic conclusions are proved. Its gamma=2 application, the original gamma=1 switching orbit, the full replacement theorem, and the publication/priority gates remain open at this checkpoint.
