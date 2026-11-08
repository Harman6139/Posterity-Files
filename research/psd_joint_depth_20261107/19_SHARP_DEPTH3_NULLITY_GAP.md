# Sharp dimension-dependent separation from square-root stability at sparse facial depth >=3

**2026-11-07. Fully proved for sparse harmonic midpoint PSD recovery.** This note is NOT a universal dense-map exclusion of alpha=1/2 at depth>=3. It yields a precise structural frontier and sharp numerical function of nullity.

Let nu>=3, h=nu-1 internal harmonic vertices (allow h smaller if unused dimensions are fully measured), weights 0=w_0<w_1<...<w_h<1=w_T, each internal vertex i having distinct parents a(i)<i<b(i) and satisfying 2w_i=w_a+w_b. Let alpha be a sharp exponent of the sparse PSD recovery pencil with this network and its optional leading edge, with alpha<=w_1. Let d be the exact minimal facial-reduction degree computed by the greedy stress peeling rule.

## Theorem A: an exact depth-two threshold for the network

    d>=3   if and only if   w_1<1/2.
    d<=2   if and only if   w_1>=1/2.

**Proof.** The first maximal exposing stress removes precisely the terminal T: a candidate simultaneous exposing set containing an internal vertex would, following the strictly decreasing-weight parent repeatedly while both parents remain, eventually require the source 0, which cannot be exposed.

If w_1>=1/2, then every internal weight is >=1/2. Every internal vertex whose lower parent is the source has weight exactly 1/2 and higher parent T (since 2w_i=w_0+w_high and w_high<=1). After T is removed, the entire set of internal vertices satisfies the greedy closure: for a vertex with both parents still remaining, neither is source, so both parents are internal and included. Thus the second stress removes all internal vertices and d<=2.

If w_1<1/2, its smaller parent is necessarily the source 0, and its larger parent is another internal vertex of weight 2w_1<1. At the second stage, both these parents remain, so the closure condition forbids removing the minimum-weight vertex. Thus d>=3. QED.

## Theorem B: exact sharp upper bound for all sparse networks of depth >=3

For nu>=3 and d>=3,
\[
\boxed{\alpha\le w_1 \le \frac{2^{\nu-2}-1}{2^{\nu-1}-1}<\frac12.}
\]
The bound is attained for every nu at **exact depth three**, so it is the exact largest exponent at fixed nullity among sparse systems with depth >=3.

**Proof.** Put a=w_1<1/2. Its parent pair is (0,z), where z=2a<1 is an internal vertex. Since each internal weight is the terminal-absorption probability of the simple random walk that selects one of the two parents equiprobably, the deficit 1-w_v is the probability of eventual absorption at source 0.

Follow the strictly decreasing-weight parent from z until reaching either the minimum-weight vertex a or the source 0. If the path first reaches a after L steps, it uses at most h-1 other internal vertices, so L<=h-1. Conditional on the event of following that exact path (probability 2^-L), the remaining source absorption probability is 1-a. Therefore 1-z>=2^-L(1-a)>=2^-(h-1)(1-a).

If the path reaches source 0 without visiting a, it can visit at most h-1 other internal vertices (a is excluded), so its length L<=h-1; hence 1-z>=2^-L>=2^-(h-1)(1-a). The same inequality holds in either case.

Since z=2a, rearrange
    1-2a >= 2^-(h-1)(1-a)
to obtain
    a <= (2^(h-1)-1)/(2^h-1)
      = (2^(nu-2)-1)/(2^(nu-1)-1).

**Sharp construction.** Put m=nu-2. Take source O=0, root R=a_m, terminal T=1, and intermediate vertices
    x_i=1-2^-i(1-a_m), i=1,...,m,
where a_m=(2^m-1)/(2^(m+1)-1). Assign root parents (O,x_m) and, for each i, parents (x_(i-1),T), interpreting x_0=R. The midpoint equalities hold; x_m=2a_m. Peeling removes T, all x_i in one step, and R in a third step, so d=3. The minimum weight is a_m and the corresponding diagonal coordinate supplies the sharp full-matrix recovery exponent alpha=a_m. This attains equality with h=m+1=nu-1. QED.

## Audit and limitations

- The argument uses **all** arbitrary ambient PSD competitors via the earlier exact sparse harmonic recovery theorem, not only structured arcs.
- The probabilistic walk is absorbing because the strictly increasing parent path always reaches terminal. The lower-bound event is *one specific finite parent-selection path*; other paths can only add source absorption probability.
- The sharp bound requires d>=3; it is false without that restriction, since degree-two networks can realize alpha=3/8 at nullity three and alpha near 1/2.
- For h<nu-1, the same argument gives the stronger bound with h+1 in place of nu; the displayed function is increasing with h.
- This is not a proof of the corresponding *universal* dense-kernel gap or of the sparse-depth-preservation conjecture. The dense weighted-flag extraction gives a harmonic network but does NOT prove its peeling depth must be >=d or preserve d.
- In particular whether an arbitrary dense SDP can have alpha=1/2 and minimal facial-reduction degree d>=3 remains unresolved.
- Exact rational enumeration of every sparse harmonic network with nullity up to six confirms the sharp bound; the proof is symbolic and does not rely on the enumeration.