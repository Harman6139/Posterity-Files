# A fully terminating enumeration of every dimension-, rank-, and depth-conditioned PSD stability spectrum

Research note — 7 November 2026. This closes the finite-candidate enumeration step in the earlier all-degree algebraic membership theorem. It is a constructive **algorithmic classification** for all triples \((n,r,d)\), independent of a depth-preserving sparse-midpoint representation. It is **not** a short arithmetic or combinatorial closed formula; it uses effective real quantifier elimination and an elementary Newton-polygon bound. The novelty lies, if any, in the universal PSD Dikin–Hessian invariant that makes this possible; the semialgebraic methods themselves are prior mathematics.

## Theorem

For every fixed integers \(n\ge2\), \(0\le r\le n\) and every admissible minimal facial-reduction degree \(d\), there exists an explicitly computable integer \(D=D(n,r)\) such that **every** uniquely recoverable PSD inverse problem with matrix order \(n\), target rank \(r\), and sharp exponent \(\alpha\) satisfies
\[
\boxed{\alpha=1\quad\text{or}\quad\alpha=\frac{p}{2q}\quad\text{for some}\quad1\le p,q\le D,\quad p<2q.}
\]
Moreover there is an algorithm that takes \((n,r,d)\), lists this finite rational superset, tests membership for each candidate using the polynomial first-order predicate of the all-degree joint compatibility theorem, and returns **exactly** the attainable sharp exponents \(\Sigma_{n,r,d}\). The algorithm always terminates. When desired, a successful real-algebraic sample provides a realizing measurement map; a negative decision certifies impossibility. No efficient running-time bound is claimed.

## Proof

**Normalize the target and kernel.** A cone congruence and equivalent norm changes reduce every rank-\(r\) target to \(X_*=\operatorname{diag}(I_r,0)\). Represent its arbitrary measurement kernel \(K\subseteq\mathbb S^n\) as the image of an \(N\times N\) orthogonal projector \(\Pi\) on Frobenius coordinates, \(N=n(n+1)/2\), with \(\Pi^2=\Pi=\Pi^\top\). Disjoin over \(k=\operatorname{tr}\Pi=0,\ldots,N\). When \(k=0\), the exponent is one.

**A uniform semialgebraic graph.** For \(k\ge1\), choose existentially a Frobenius-orthonormal basis \(H_1,\ldots,H_k\in\operatorname{range}\Pi\). Define the polynomial matrix \(A_{ij}(X)=\operatorname{tr}(\operatorname{adj}(X)H_i\operatorname{adj}(X)H_j)\) and polynomial scalars \(N(X)=(\det X)^2 e_{k-1}(A(X))\), \(D(X)=\det A(X)\). For each \(\Pi\) with unique target and for each \(t>0\), the central equations
\[
X\succ0,\quad
\Pi(X-X_*-tI)=X-X_*-tI,\quad
\Pi(\operatorname{adj}X)=0
\]
have a **unique** solution \(X=X_t\). Define the single positive scalar
\[
u_\Pi(t)=\frac{N(X_t)}{D(X_t)}=\operatorname{tr}(G_t^{-1})>0,
\]
where \(G_t\) is the logdet-Hessian Gram restriction to \(K\). The graph \(\{(\Pi,t,u):u=u_\Pi(t),\ t>0,\Pi\text{ uniquely feasible}\}\) is the projection of a finite polynomial semialgebraic set over the variables \((\Pi,t,u,X,H_1,\ldots,H_k)\). Therefore ordinary quantifier elimination produces one **finite Boolean combination of polynomial sign conditions** \(P_j(\Pi,t,u)\gtrless0\) defining this graph. Let \(D\) be the maximum total degree of all resulting nonconstant polynomials, enlarged to at least one and maximized over the finitely many \(k\).

**Elementary uniform Newton-polygon valuation bound.** Fix any admissible specialized projector \(\Pi_0\). For all sufficiently small \(t>0\), there is an index \(j\) such that \(P_j(\Pi_0,t,u_{\Pi_0}(t))=0\) but the specialized bivariate polynomial \(P_j(\Pi_0,t,u)\) is not identically zero. If this failed at some point, every non-identically-zero sign polynomial would remain nonzero on a neighborhood, while the identically zero specializations remain zero everywhere. The Boolean sign formula would then hold on an open neighborhood of a point of the graph, contradicting that the graph of a single-valued function has empty interior in the \((t,u)\)-plane.

The zero sets for the finitely many specialized polynomials along the semialgebraic graph are semialgebraic subsets of the small interval \((0,t_0)\). A finite union covering that interval must have one member containing an entire interval \((0,t_1)\) (each semialgebraic subset of the line has finitely many components). Hence **one nonzero specialized polynomial** \(P(t,u)\), of degree at most \(D\), satisfies
\[
P(t,u_{\Pi_0}(t))=0\quad\text{for every sufficiently small}\quad t>0.
\]
By the general semialgebraic growth theorem, \(u_{\Pi_0}(t)\asymp t^s\) with \(s\in\mathbb Q\), since singleton uniqueness plus the Dikin recovery comparison force \(u(t)\to0\). Write \(P(t,u)=\sum_{i,j}c_{ij}t^iu^j\) with some nonzero coefficients. If only one monomial had smallest exponent \(i+sj\) on substitution, its nonzero coefficient would prevent \(P(t,u(t))\) from vanishing. Therefore at least two distinct pairs \((i_1,j_1)\ne(i_2,j_2)\), each with \(i,j\le D\), satisfy
\[
i_1+s j_1=i_2+s j_2.
\]
Thus \(s=(i_2-i_1)/(j_1-j_2)>0\) is a rational with reduced numerator and denominator at most \(D\). This is an **effective uniform finite candidate set** for all central determinant-ratio valuations.

**Translate back to the recovery exponent.** By the universal Dikin–Hessian theorem and its scalar determinant-ratio corollary,
\[
\omega(t\|\mathcal LI\|)\asymp t+\sqrt{u_\Pi(t)},
\]
so \(\alpha=\min\{1,s/2\}\). Therefore \(\alpha=1\) or \(\alpha=p/(2q)<1\) for \(1\le p,q\le D\). Finally, checkpoint 14 supplies a necessary-and-sufficient **finite first-order polynomial predicate** deciding occurrence at exact singularity degree \(d\) for each candidate \(\alpha\). Evaluate it on every candidate and retain exactly the true cases. This terminates and yields the complete \(\Sigma_{n,r,d}\). QED.

## Important limits

- The computed degree bound \(D(n,r)\) can be astronomically large; the algorithm is rigorous but likely impractical beyond tiny matrix orders.
- No optimal matrix-dimension formula depending only on a fraction is asserted by this method. The earlier sparse midpoint formulas remain sharper when applicable.
- The theorem decides every high-depth endpoint case at each **specified finite** \(n,r,d\), but it does not automatically settle the uniform statement \(\exists n,r: \alpha=1/2,d\ge3\) because \(n\) is unbounded. That is a logically distinct infinite-dimensional quantification across all finite sizes.
- Ordinary semialgebraic quantifier elimination, Puiseux expansions, and Newton polygons are prior mathematics. Their role here is to finitely implement the newly proved intrinsic Dikin–Hessian structural invariant.