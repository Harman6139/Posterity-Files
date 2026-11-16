# Finite local models and linear-scale hardness — proof checkpoint

This supersedes checkpoint 00's preliminary location-dependent cofactor bound. The complete new manuscript is being packaged; the core analytical proofs and exact tests are complete locally. Historical first priority and the user-reported top-three comparison are not certified.

## 1. Finite local models
For every positive-definite H of order r, the epigraph g_H(b)=sup_(u>=0 integral,y>=1 integral)(1-H[u]-2y b^T u)/y^2 has a uniform positive gap above H[z], where z minimizes H[x]+2b^T x on x>=0. Write ell=b+Hz. At vertices, ell lies in [0,1/2]^r. Active denominators y are uniformly bounded; active residuals u-yz have uniformly bounded H-norm.

Normalize by k=floor(z), an integral shear. The normalized point has bbar=ell-H(z-k) and cbar=H[z-k]+c-H[z], both bounded. Every normalized active vector (u-yk,y) lies in one fixed finite signed integer box. Therefore finitely many normalized vertex and tangent-cone types occur. For rational H there is a common denominator for all vertices.

If H is a positive-definite perfect leading block, every full primitive tangent ray is U_k^T Rbar U_k with Rbar in a fixed finite set. Its top block is bounded independently of position, cross block grows at most linearly in |k|, and last entry at most quadratically. The number of active vectors and competing rays is uniformly bounded. Complete local active/ray/neighbor computation has polynomial bit cost for fixed H and dimension. This does not contradict prior large active sets with a singular leading block.

## 2. Abstract verifiable seed lifting
Let B=[B0 a;a^T alpha] be rational, positive definite, strictly entrywise positive and outside ordinary CP_n, with B0 in the interior of the finite normal cone V_H of H. Let q_B clear B0 denominators. A primitive escaping ray has leading cost at least 1/q_B. The sharper ray bounds imply that S_N B S_N, S_N=diag(NI,1), has no improving escaping extreme ray in an m-edge region as soon as N >= C_(H,B,R0)(m+1). This is LINEAR in m, rather than the former high power of m.

The complete proof gives explicit constants, a radius c/N^2 ball of normalized positive-definite strictly positive nonmembers, and a common strictly copositive rational separator of O(log N) height. Every strictly improving adjacent rule must take m pivots from any initial vertex in a fixed bounded region of the fixed-H face. Any fixed finite menu of such starts, or restarts within that region, is covered. Arbitrary distinct-H menus are not covered.

## 3. Stronger local certificate exclusion
The known PSD-principal-block lemma (Shaked-Monderer, LAA 509 (2016), Lemma 3.1) implies that no copositive certificate with a PSD leading (n-1)-block separates a doubly nonnegative target. Thus arbitrary nonnegative diagonal corrections and even arbitrary PSD corrections of every improving ray fail throughout the prefix. History combinations with PSD leading block are also excluded, across multiple runs. The lemma is explicitly credited; its application strengthens the original scalar-only certificate model.

## 4. Qualifying seeds not reducible to the five-cycle
For each odd n>=5, use t=1/2+1/(16n^2), F=I+t Adj(C_n), h=(I-t Adj(P_(n-1)))^-1 1, D=diag(h,1), and B=DFD+C/(32n^5), where C is the canonical interval anchor. B qualifies for H=T_(n-1). The copositive witness is D^-1(J-2 Adj(C_n))D^-1. Every proper principal submatrix is interior completely positive, with explicit rational factors and perturbation reserve. Consequently all proper-principal COP tests fail, even at order n-1, while full-order nonmembership persists. Weighted cycles satisfying a trace/edge inequality give an open additional seed class. These facts do not claim that odd-cycle obstructions themselves are new.

## 5. Independent intrinsic graph geometry
For every real H>0, the bounded-edge graph of its epigraph is connected, has uniformly bounded degree, and graph balls have Theta(R^r) vertices. It contains a quasi-isometrically embedded orthant lattice. For rational H, O(log N)-bit vertices exist at intrinsic distance Theta(N). The proof uses finite templates for the upper bound, c-descent to a finite bottom face for connectivity, and translated paths in the unrestricted integer epigraph for the lattice embedding. Shears are not asserted to preserve the whole orthant epigraph: only the chosen paths whose full active sets become nonnegative are transferred. The exact H=I_2 graph is Z_+^2.

## 6. Fresh checks
The independent standard-library verifier (no generator imports, Bareiss determinants) passed five seed families (orders 5,7,9,11 and a weighted order-7 family), 39 maximal-proper-principal factorizations with 2,092 weighted atoms, 15 scale cases, six sheared vertices with 129 full tangent rays, 25 geometric vertices with 300 pairwise adjacency checks, and two SPN decompositions. Seven corrupted data sets were rejected. For m=2^64 in order five, N has 575 bits, versus 4,823 in the prior conservative construction. No long trajectory was simulated.

Certificate SHA256: 0700e5c45c8df954a140b7d6bc3b5175aaead8f572b438fce213f4be1fdaea5a.

The theorem is analytical; tests do not replace proofs. Sources and PDF will be committed in the release directory after packaging. This checkpoint is durable even if packaging is interrupted.
