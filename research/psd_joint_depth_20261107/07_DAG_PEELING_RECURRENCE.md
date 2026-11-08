# Exact-depth recursion for acyclic harmonic PSD networks

**Theorem.** Suppose the parent-directed graph of a finite harmonic PSD network is acyclic. Give the permanent source O the peeling time t(O)=+infinity and every terminal T the time t(T)=1. Recursively in a topological ordering of the internal vertices, set
  t(v)=min(t(a(v)),t(b(v))) + 1_{ t(a(v)) != t(b(v)) }.
Then the *minimal* facial-reduction degree of the associated sparse PSD pencil equals max_v t(v). Each greedy exposing layer is exactly {v:t(v)=j}. This holds even when the network has multiple source-glued components.

Proof. The previously proved sparse stress-peeling theorem says that a subset C of currently remaining non-source vertices can be exposed together if and only if, whenever v in C has both parents remaining, both are also in C. Let u=t(a), v=t(b). If u=v=j, the child can be exposed simultaneously with both parents in layer j, and not earlier: both parents still remain and cannot themselves be removed before j. If u< v, the child cannot be removed by layer u, because the later parent still remains and the earlier parent cannot be removed before u; it can be removed at layer u+1 since the earlier parent is then absent, with no condition on the later parent. The case of one parent O has time infinity and gives one extra step after the other parent. As the graph is acyclic, the parent times have already been determined, and induction proves the formula for every node and gives a valid greedy layer partition. Minimality among *all possibly rotated* facial chains follows from the sparse greedy maximal-stress theorem. QED.

**Universal significance.** In the extremal maximal-denominator dyadic regime alpha=a/2^nu (a odd), the dense weighted-flag structural necessity forces its extracted harmonic graph to be acyclic (checkpoint 05). This recursion therefore computes the facial depth of any corresponding sparse realization in one graph pass; it does NOT establish that the dense original has the same depth. The distinction between exponent-preserving extraction and depth-preserving extraction remains the missing general universality claim.

**Examples with target nullity nu=5 and full reduced denominator 32.** All are dimension-minimal, and the bisection construction attains the minimum possible degree. Sparse DAG enumeration also gives alternative degrees for some numerators:
alpha=1/32: {5};
alpha=3/32: {4};
alpha=5/32,7/32: {3};
alpha=9/32,11/32: {2,3};
alpha=13/32,15/32: {2}.
These are exact within-family sets, *not* asserted to equal the dense all-kernel degree spectrum.