# Milestone 82 — tied-edge MIN–MAX games add NO sharp exponents at maximal facial depth

**2026-11-08. PROVED for EVERY strict finite tied-edge incidence PSD recovery family of checkpoints 74 and 77.** Arbitrarily many modes, arbitrarily many edges per mode, and arbitrary (globally distinct) tied offdiagonal supports are allowed. This is an exact equivalence of attainable sharp exponent sets **within the incidence classes**, not a theorem reducing every dense PSD kernel to a game.

## Theorem

Fix target nullity ν=h+1 and target rank r≥1. Among strict tied-edge MIN–MAX incidence systems with one source, h internal coordinates and one terminal, consider those with **maximal minimal facial-reduction degree d=ν**.

Then their exact set of attainable full-matrix Hölder recovery exponents is IDENTICAL to the strict independent-edge multi-action maximal-depth spectrum from checkpoint 70, and hence to the bounded primitive integer-gap spectrum of checkpoint 72:
\[
\boxed{
\Sigma^{\rm tied\!-\!edge}_{\nu,d=\nu}
=
\Sigma^{\rm independent\!-\!edge}_{\nu,d=\nu}
=
\mathcal C_\nu
=
\bigcup_{g\in\mathcal I_h}
\left\{\frac{\sum_{j<v}g_j}{2\sum_{j=0}^{h}g_j}:
\sum_{j<v}g_j\le2g_0\right\}.
}
\]
Here \(\mathcal I_h\) comprises primitive positive nondecreasing integer gaps \(g_0\le\cdots\le g_h\), total \(D\le2^h\), with one balanced contiguous interval-sum midpoint identity at every internal vertex, as explicitly defined and proved in checkpoint 72.

**In particular**, the new tied-edge mechanism that disproved *independent-edge* two-policy universality at \((\nu,d,\alpha)=(5,3,3/22)\) cannot enlarge the incidence-family maximal-depth spectrum. The extra expressiveness is confined to intermediate-depth profiles.

## Proof

**Step 1: maximal depth forces singleton descending exposure.** At any stage in the tied-edge AND–OR exposing closure (checkpoint 74), the highest-index remaining non-source vertex is individually exposable: every mode at that vertex has every edge's higher parent strictly larger than the child, and hence already removed, so each mode is inactive. Terminal is always eligible at the initial stage. Therefore a chain of length \(h+1\) with exactly \(h+1\) non-source vertices must remove one vertex per step, necessarily
\[
\{T\},\{h\},\{h-1\},\ldots,\{1\}.
\]

**Step 2: each internal vertex has a mode whose ALL edges point to the immediate higher neighbor.** Consider vertex i when the current remaining vertices are \(R=\{0,1,\ldots,i+1\}\), just before removing vertex i+1. If every mode at i had some edge touching an already removed vertex \(>i+1\), then every mode would be inactive at R. Consequently the exposing set \(\{i,i+1\}\) would be legal: i has no active mode, and the highest vertex i+1 has none. This would allow a rank-two first exposing step on this reduced face and contradict the singleton canonical schedule. Thus at least one mode at i is *active* in R, meaning EVERY edge (a,b) in that mode has both endpoints in R. As all edges satisfy \(a<i<b\), we must have \(b=i+1\) on every edge of this active mode. Its lower parent varies but always satisfies \(a\le i-1\).

**Step 3: exact discrete convexity.** Let the strict Shapley values satisfy
\[
w_i=\min_{a\in A_i}\max_{e=(u,v)\in E_{i,a}}(w_u+w_v)/2.
\]
For the mode from Step 2, every edge is (a,i+1) with a≤i-1. Therefore
\[
w_i\le\max_{(a,i+1)\ \mathrm{in\ that\ mode}}
\frac{w_a+w_{i+1}}2
\le\frac{w_{i-1}+w_{i+1}}2.
\]
Thus \(w_{i+1}-w_i\ge w_i-w_{i-1}\) for each i, so the strict game values are *discretely convex*.

**Step 4: select one harmonic policy and realize it using independent edges.** Choose at each internal i a Shapley-minimizing mode \(\mu_i\) and, within it, one edge \(e_i\) maximizing the average of w at its endpoints. Then
\[
2w_i=w_{a_i}+w_{b_i}.
\]
The selected edges are globally distinct, as they are drawn from the original disjoint family. Thus they give a strict one-action harmonic network with the *same* w. By Step 3 its weights are convex. Checkpoint 70 proves that appending independent nearest-neighbor edges (i−1,i+1) preserves w (these actions are slack or tied), forces **maximal** exposing depth, and realizes every valid leading half-weight exponent \(\alpha=\min(w_1,w_t/2)\) with matching full-PSD competitor upper and lower bounds. If \(\alpha=w_1\), it is also a valid half-weight: the selected harmonic edge at the minimum internal vertex 1 has lower parent source 0, so one parent has weight \(2w_1\). Every tied-edge instance's sharp exponent is therefore realized by an independent-edge multi-action instance at the same nullity and maximal degree.

The reverse inclusion is trivial, because one-edge modes are a special case of tied-edge modes. The integer-gap identity follows from checkpoint 72. QED.

## Consequences and exact scope

1. **Sharp collapse theorem:** at maximal facial degree, allowing tied edges within a mode DOES NOT enlarge the attainable exponent set relative to independent-edge multi-action incidence systems.
2. **Still more than the single-action family:** already at nullity six the common spectrum contains nonreciprocals \(3/46,3/23,2/15\) (checkpoint 68/70), which a single-action maximal-depth model misses.
3. **Depth-localization of extra game mechanisms:** tied-edge couplings can change the spectrum only at nonmaximal facial degrees within this incidence framework.
4. **NOT proved for arbitrary dense PSD maps:** There is still no theorem guaranteeing that every dense maximal-depth exponent yields a strict convex harmonic graph at the same nullity. Hence the displayed arithmetic set is a universally valid constructive inclusion, NOT a claimed full dense maximal-degree classification.

The argument uses only exact Shapley fixed-point equalities and the already proved AND–OR facial-peeling theorem. No new unverified representation assumption, no numerical SDP, and no implicit dense-to-graph claim are involved.