# Universal dyadic rigidity and simultaneously optimal (dimension, degree)
Research checkpoint — 2026-11-07. PROVED under the dense weighted-flag extraction theorem of the earlier full project memorandum. Does not assert a universal sparse depth-preserving map.

Let X_*>=0 be the unique PSD solution, target rank r>=1, nullity nu=n-r, optimal exponent alpha, and minimal singularity degree d. Sturm gives alpha>=2^(-d), d<=nu. The prior dense weighted-flag theorem says: for alpha<=1/2, a sharp flag of actual coefficient matrices in ker(L) induces a finite set S of h<=nu-1 distinct midpoint weights in [alpha,1), with 2alpha in S union {1}. The midpoint constraints come from active PSD order inequalities 2w_i>=w_j+w_k. (See Sharp_PSD_Stability_Weighted_Flags_Memorandum.md, Sections 2–4 for the full proof: Puiseux sharp arcs; fixed PSD diagonal-leading flag; rescaling each kernel coefficient of order e by exp(sigma*e^2) to force all full-matrix minors positive; componentwise least point of the rational support polytope.)

## Theorem A — exact determinant/feedback principle
For a harmonic midpoint graph S={w_1,...,w_h} with boundary weights 0,1, and directed parent edges v->a(v),b(v), define M with ith reduced row 2e_i-e_a-e_b (boundary columns zero). Then
    det(M) = number of assignments choosing one of the two parents at every vertex that contain NO directed cycle among internal vertices.
In particular 1<=det(M)<=2^h; each internal weight's reduced denominator divides det(M); and det(M)=2^h iff the full parent graph is acyclic. An acyclic graph produces only dyadic weights, hence a **non-dyadic sharp exponent of an arbitrary dense PSD recovery problem forces a directed feedback cycle in every sharp mediated graph**.

Proof: expand each row of M as (e_i-e_a)+(e_i-e_b). Each of the 2^h determinants is zero if its functional digraph has a directed cycle (cycle rows are dependent), and +1 otherwise (simultaneously permute rows and columns topologically, giving a triangular matrix with ones on the diagonal). There exists an absorbing choice because repeatedly choosing the larger-weight parent reaches boundary 1. Thus det positive. Cramer's rule yields denominator divisibility. For an acyclic full parent graph, topologically evaluate all midpoint weights starting with 0,1; they are dyadic. QED.

## Theorem B — rigid extremal Sturm-spine for EVERY dense kernel
If nu>=2 and alpha=2^(-nu), then:
(i) d=nu exactly;
(ii) every sharp extracted harmonic certificate has exactly h=nu-1 internal levels, necessarily
    S={2^(-(nu-1)),...,1/4,1/2};
(iii) every parent pair is uniquely (0,next larger dyadic level), ending in (0,1);
(iv) the corresponding dense sharp flag has nu one-dimensional diagonal null blocks. Its leading exponent alpha is achieved by a nonzero support-to-first-null kernel coefficient, and each subsequent active dyadic midpoint arises from a kernel coefficient with positive diagonal compression and nonzero support-to-next-level block.

Proof: d<=nu and Sturm alpha>=2^(-d) force d=nu. The weight 2alpha=2^(-(nu-1)) must occur in S. With h<=nu-1, Theorem A implies 2^(nu-1) divides det(M)<=2^h<=2^(nu-1); hence h=nu-1 and det(M)=2^h. The entire parent graph is acyclic. A node of weight w is an absorption probability for the fair parent random walk. Following the increasing-weight parent from any node reaches boundary 1 within at most h steps; this event has probability >=2^(-h), so every internal weight is >=2^(-h). The node w=2alpha=2^(-h) attains equality. Its increasing-parent path must have exactly h steps and visit every internal node. The probability of that single successful path already equals w, so every alternate parent along the path must have zero absorption probability. Each internal node has positive absorption probability; hence every alternate parent is 0. This gives uniquely the stated dyadic chain. Since h+1=nu diagonal levels occupy nu null dimensions, all blocks are 1-dimensional. The off-diagonal-leading coefficient at alpha must couple target support to the first null block (2alpha=w_1), and the active midpoint constraints give the subsequent support-to-next-level kernel blocks. QED.

## Theorem C — simultaneous optimal dimension AND singularity degree for every maximal dyadic denominator
For each nu>=2 and odd 1<=a<2^(nu-1), put alpha=a/2^nu. Then there exists a rank-one PSD recovery instance of matrix order nu+1 whose optimal exponent is exactly alpha and whose minimal singularity degree equals
    e=ceil(log2(1/alpha)).
Both nullity nu and degree e are individually minimal, hence attained SIMULTANEOUSLY. Adding a fully measured positive-definite block raises the rank to any r>=1 while preserving alpha, nu, and e. Every minimal-nullity realization has an acyclic maximal-size sharp harmonic certificate.

Proof of lower bounds: the reduced denominator of 2alpha=a/2^(nu-1) is 2^(nu-1). By Theorem A and the dense flag extraction, any instance of nullity nu' must satisfy 2^(nu-1)<=2^(nu'-1), hence nu'>=nu. Sturm gives d>=ceil(log2(1/alpha)).

Construction: set x=2alpha=a/2^(nu-1). Bisect [0,1] toward x. At step j=1,...,nu-1 add the midpoint m_j of the current interval and record its endpoints as parents. Because a is odd, the first equality m_j=x occurs at the last step. Every parent is boundary 0/1 or an earlier midpoint, so the graph is acyclic. Each midpoint m=(L+R)/2 obeys m>=R/2>=x/2=alpha, giving the *full-state auxiliary-coordinate barrier*. Add a free offdiagonal leading coordinate on edge (0,x); no midpoint is alpha, since alpha has reduced denominator 2^nu, so this edge is unused by the parent graph. Use the already-proved sparse PSD pencil with diagonal variables x_v, weak parent-edge entries lambda*x_v, measurements projecting off the pencil plus trace and terminal diagonals, and target E_00. For arbitrary ambient PSD competitors, principal-minor inequalities and the harmonic maximum principle give the sharp upper bound delta^alpha. The curve x_v=t^(w_v), free extra entry t^alpha, with trace normalization, is PSD by diagonal dominance after diagonal congruence and attains this bound.

For exact degree let k=ceil(log2(1/x)). The source-parent midpoints in the bisection are exactly m_1=1/2,...,m_k=2^(-k); all later nodes have both parents distinct from source 0. The sparse peeling rule gives an admissible facial reduction in k+1 steps: first terminal; then m_1,...,m_(k-1) singly; finally m_k and all remaining internal vertices together. In the last step any internal vertex whose two parents remain has both parents in the removal set; m_k's higher parent was already removed. Thus d<=k+1=ceil(log2(1/alpha))=e; Sturm gives equality. QED.

Examples with nu=5: odd numerators 1,3,5,7,9,11,13,15 over 32 have simultaneous minimal depths 5,4,3,3,2,2,2,2, all at minimum nullity 5.

## Limit and novelty discipline
These extremal theorems do NOT resolve the arbitrary fixed-(n,r,d) sparse-versus-dense compatibility for d>=3, nor the endpoint alpha=1/2 at d>=3. The determinant/mediated-graph combinatorics has significant prior literature (Jie Wang 2024; Blanco–Martinez-Anton 2026); the universal PSD-specific conclusion is its combination with the dense sharp weighted-flag mechanism and dimension/depth rigidity. The previous maximal-rank facial reduction lemma is standard prior art.

An exact-rational checker has independently verified all 511 binary-bisection instances for nullity 2..10 and uniquely forced dyadic chains through nullity six, but the conclusions above are proved symbolically.