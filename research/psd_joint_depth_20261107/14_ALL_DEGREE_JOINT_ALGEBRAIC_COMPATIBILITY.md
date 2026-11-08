# Complete all-degree joint exponent/depth **membership** classification via one polynomial contact invariant

**PROVED, 2026-11-07.** For every (n,r,d) and rational alpha, an explicitly constructible first-order real-algebraic sentence decides whether a uniquely recoverable n-by-n PSD problem of target rank r, minimal facial reduction degree d and sharp recovery exponent alpha exists. Unlike earlier weighted-flag based checkpoint 03, this uses only the universal canonical Dikin–Hessian theorem and standard facial reduction. Does not claim a simple arithmetic catalogue.

Fix X*=diag(I_r,0), N=n(n+1)/2. Represent any measurement kernel K in S^n by an N-by-N Frobenius orthogonal projector Pi, Pi=Pi^T=Pi². Disjoin over its finite possible ranks k=tr Pi=0,...,N. A canonical measurement is L=I-Pi to K^perp.

**Uniqueness** is a first-order polynomial predicate: for all Y>=0, Pi(Y-X*)=Y-X* implies Y=X*. PSD is a finite list of principal minor inequalities.

**Minimal singularity degree** is also a finite first-order polynomial predicate: an exact j-step exposing chain is represented by coordinate face projectors P0=I,...,Pj=P_U and stress matrices Z_i with Pi Z_i=0 and S_i=P_(i-1) Z_i P_(i-1)>=0, P_i P_(i-1)=P_i, P_i P_U=P_U, S_i P_i=0, S_i+P_i+I-P_(i-1)>0, and strict rank decrease tr(P_i)<tr(P_(i-1)). The PD condition ensures P_i is *exactly* the within-face kernel of S_i. Exact depth d means a valid chain of length d exists and no valid chain of shorter length exists; finitely many clauses since d<=n-r.

Choose a Frobenius orthonormal basis H_1,...,H_k for range Pi, encoded by Pi H_i=H_i and tr(H_iH_j)=delta_ij. For X>0 define the **polynomial** Gram matrix
    A_ij(X)=tr(adj(X) H_i adj(X) H_j);
    D(X)=det A(X)>0;
    N(X)=(det X)^2 e_(k-1)(A(X))>0.
(For k=0, exponent is 1.)

The uniquely determined canonical central point at epsilon=t^b is specified *only* by the polynomial conditions
    X>0,
    Pi(X-X*-t^b I)=X-X*-t^b I,
    Pi(adj X)=0.
Uniqueness+bounded PSD slice ensure existence and uniqueness for every t>0.

**Exact exponent predicate:** for reduced rational alpha=a/b with 0<alpha<1, assert existence of c,C,eta>0 such that for all t∈(0,eta), some X satisfies the central equations above and the polynomial inequalities
    c t^(2a) D(X) <= N(X) <= C t^(2a) D(X).
The Dikin–Hessian determinant ratio theorem (checkpoint 12) gives omega(||LI||t^b)=Theta(t^b+sqrt(N(X)/D(X))). Since a<b, the displayed inequalities are **equivalent** to alpha being the exact optimal full Frobenius exponent. For alpha=1, impose N(X)<=C t^2 D(X) at epsilon=t (or k=0); the lower modulus Omega(epsilon) makes this necessary and sufficient.

Every statement here is a first-order real-closed-field formula involving finitely many real variables and polynomial inequalities, with rational coefficients. Real quantifier elimination terminates and decides it. A true existential semialgebraic sample gives a realizing measurement kernel; false means rigorous impossibility for this triple/exponent. This is an exact and **complete algorithmic classification of all joint compatibilities for all degrees d**, independent of a sparse network reduction.

**Scope.** The structural ingredient is the independently proved exact Frobenius Dikin-Hessian comparison, not the generic fact that real QE exists. This is a membership algorithm, potentially enormous; it is not an elementary closed arithmetic formula listing Σ_(n,r,d), and no efficient complexity estimate is claimed. Generic/structural enumeration and the unresolved high-depth alpha=1/2 question are different refinements.