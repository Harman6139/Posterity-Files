# Exact closed reciprocal spectrum at maximal sparse facial depth

**2026-11-07. Proved theorem, no dense-to-sparse universality asserted.**

Let nu>=2 be target nullity, and consider the *sparse harmonic midpoint-network PSD recovery pencils* defined in prior checkpoints: target E_00, one terminal of weight one, h=nu-1 internal nodes of distinct weights (0,1), a midpoint parent pair for each internal node, a weak coefficient at every parent edge, optional leading source-to-2alpha edge, trace and terminal measurement, and orthogonal projection off the pencil range. Each such pencil has a full-state sharp exponent alpha and exact minimal facial degree equal to the proven greedy peeling count.

## Main theorem
**Among these sparse pencils with minimal facial-reduction degree d=nu (maximal possible), the exact set of sharp exponents is**
\[
\boxed{\Sigma^{\rm sparse}_{\nu,d=\nu}=
\{1/q:\nu\le q\le 2^{\nu-1},\ q\in\mathbb Z\}
\ \cup\
\{1/(2q):\nu\le q\le2^{\nu-1},\ q\in\mathbb Z\}.}
\]
All are realized by explicit *rational* rank-one PSD systems of matrix order nu+1; adjoining a fully measured positive block realizes any prescribed positive target rank without changing nullity or degree. This is a complete **closed arithmetic spectrum at maximal depth within this broad construction family**, not a universal necessity theorem for arbitrary dense maps.

## Proof of necessity

Since there are nu non-source vertices and the *minimal* greedy peeling chain has length nu, each greedy step removes exactly one vertex. The first peeled vertex is the terminal, denoted v_1. Denote the remaining vertices in peeling order by v_2,...,v_nu, with source v_(nu+1) (weight zero). For each j=2,...,nu, the parent edge of v_j must contain v_(j-1): if both parents remained at step j then including v_j would force both parents to be peeled at that step (impossible with singleton layers); if a parent had been removed earlier than step j-1 then v_j would have been eligible earlier, contradicting the greedy sequence. The other parent must be some v_(ell_j), ell_j in {j+1,...,nu+1}. Thus the harmonic equations, now in *peeling order*, are
    2 w_j = w_(j-1) + w_(ell_j),
    w_1=1, w_(nu+1)=0,
where ell_j>j and the two parent indices are distinct.

Define gaps Delta_j=w_(j-1)-w_j, j=2,...,nu+1. The harmonic equations give
    Delta_j = sum_(k=j+1)^(ell_j) Delta_k.
Since the last gap Delta_(nu+1)=w_nu>0, all gaps are strictly positive. Write c_(nu+1)=1 and c_j=sum_(k=j+1)^(ell_j) c_k, so Delta_j=c_j w_nu with each c_j a positive integer. Normalization w_1-w_(nu+1)=1 yields
    w_nu=1/Q,  Q=sum_(j=2)^(nu+1)c_j.
The recursion gives c_j>=1, hence Q>=nu. It also gives c_j<=sum_(k=j+1)^(nu+1)c_k; letting S_j=sum_(k=j)^(nu+1)c_k, we have S_j<=2 S_(j+1) and S_(nu+1)=1, so Q=S_2<=2^(nu-1).

The last two internal weights are w_nu=1/Q and w_(nu-1)=(c_nu+c_(nu+1))/Q=2/Q (for nu=2, w_(nu-1)=w_1=1=2/Q). In the sparse construction, alpha is either the smallest internal diagonal weight or half of the weight of an internal or terminal vertex, and alpha may not exceed the smallest internal weight. Thus any leading doubled weight is at most 2/Q. Because all vertex weights are *integer multiples* of 1/Q, the only possibilities are
    alpha=1/Q or alpha=1/(2Q).
This establishes necessity.

## Constructive sufficiency for **every** nu <= Q <= 2^(nu-1)

We explicitly construct integers c_(nu+1)=1, c_nu,...,c_2 and indices ell_j∈{j+1,...,nu+1} satisfying c_j=sum_(k=j+1)^(ell_j)c_k and sum c_j=Q. Induct on nu.

For nu=2, Q=2, take c_2=c_3=1 and ell_2=3.

For nu>=3 and Q<=2nu-2, put k=Q-nu, so 0<=k<=nu-2, and assign
    c_2=...=c_(k+1)=2 (k terms);
    c_(k+2)=...=c_(nu+1)=1.
For indices j<k+1 set ell_j=j+1; at j=k+1 (if k>0) take ell_(k+1)=k+3 so c_(k+1)=1+1=2; for later indices take ell_j=j+1. This fulfills the recurrence and total Q=nu+k.

For Q>2nu-2 let Q'=ceil(Q/2). Then nu-1<=Q'<=2^(nu-2). By induction construct a valid (nu-1)-stage tail of length nu-1 with sum Q'. Shift its indices up by one, obtaining c_3,...,c_(nu+1), with c_(nu+1)=1. If Q is even set ell_2=nu+1 and c_2=Q'; if Q is odd set ell_2=nu and c_2=Q'-1 (sum of tail except its last unit). In both cases c_2+Q'=Q and all recurrences hold.

Now solve the harmonic equations explicitly from the positive gaps:
    w_j=(c_(j+1)+...+c_(nu+1))/Q,  1<=j<=nu+1,
with w_1=1,w_(nu+1)=0. These weights are strictly descending in peeling order, all in (0,1) internally. Use parent pair (v_(j-1),v_(ell_j)) for v_j.

**The greedy depth is exactly nu.** Initially any internal vertex contained in a simultaneous exposing set would force inclusion of its higher-index parent, then successively of later parents until the source v_(nu+1), which is forbidden. Hence only v_1 can peel. Once v_1,...,v_(j-1) have been removed, v_j is eligible because one parent v_(j-1) is gone; every v_k, k>j, still has both parents remaining and cannot be in a valid exposing set without eventually forcing the source. The greedy layers are precisely {v_1},{v_2},...,{v_nu}.

The sparse pencil built from this graph has sharp exponent 1/Q when its leading direction is the internal coordinate at the minimum weight w_nu=1/Q (or the optional source-to-w_(nu-1) edge). It has exponent 1/(2Q) when the optional leading offdiagonal source-to-w_nu edge is added. That edge is not occupied by a parent relation: all parent edges have first endpoint a vertex among v_1,...,v_(nu-1), whereas the source v_(nu+1) is only paired with its higher-weight parent v_(nu-1) in v_nu's existing midpoint equation. Full-matrix sharpness for arbitrary PSD competitors follows from the earlier exact harmonic inequality and diagonally dominant normalized PSD curve. Both systems have exact peeling degree nu.

## Reproducibility

The exact Fraction generator in the companion file 18_MAX_DEPTH_RECIPROCAL_GENERATOR.py implements the induction and verifies the midpoint equations, strict positivity, and singleton peeling. It passed all 4028 cases with 2<=nu<=12, including every integer nu<=Q<=2^(nu-1). Exhaustive comparison with the independent general sparse-network catalogue agrees through nu=6.

## Scope and next frontier

This completely classifies maximal-depth **sparse** realizations and gives a universal *lower inclusion* for the fixed-(n,r,d=nu) PSD spectrum. The reciprocal **necessity** for arbitrary dense kernels at d=nu remains an open implication: current dense weighted-flag extraction preserves alpha and nullity but does not prove that the extracted harmonic network has the same minimal peeling degree. In particular, the displayed formula must **not** be stated as the full dense universal spectrum without a new depth-preserving theorem or a separate necessity proof.

The greedy facial reduction mechanism is established prior literature, and integer averaging recurrences may be related to known mediated-graph combinatorics; bibliographic priority of the combined sparse classification has not been audited.