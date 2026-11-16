# Introduction and model

The difference between describing a certificate and reaching it by local search is especially visible for completely positive matrices. Put $$\begin{gathered}
 \mathcal{CP}_n=\operatorname{cone}\{xx^{\mathsf T}:x\in\mathbb R_+^n\},\qquad
 \mathcal{COP}_n=\{W:x^{\mathsf T}Wx\ge0\ (x\ge0)\},\\
 \mathcal R_n=\{P:P[v]\ge1\ (0\ne v\in\mathbb Z_+^n)\}.
 \end{gathered}$$ The trace pairing is $\langle X,Y\rangle=\operatorname{tr}(XY)$ and $P[v]=v^{\mathsf T}Pv$. A perfect copositive matrix is a vertex of $\mathcal R_n$. The simplex-type method of Dutour Sikirić--Schürmann--Vallentin [@DSV] moves along an extreme tangent ray $R$ with $\langle A,R\rangle<0$, to its adjacent endpoint when the edge is bounded. The current vertex and a copositive improving ray can be separating certificates. Our earlier construction [@Baseline] gives robust exponentially long prefixes from the canonical tridiagonal vertex for every such choice, on positive definite and strictly positive ordinary $\mathcal{CP}_n$ nonmembers.

The present paper isolates the mechanism rather than another trajectory. The main amplification theorem requires a finite normal-cone certificate for a principal block of an otherwise arbitrary seed. Its geometric input is a finite shear-normal-form theorem for lattice epigraphs. This strengthens location-dependent cofactor estimates: in sheared coordinates all active vectors and all primitive rays belong to fixed bounded lists. As a result, a scale $N$ proportional to the desired prefix length suffices. The same normal forms give an independent statement about denominators and intrinsic graph growth. Finally, a graphical Schur interval constructs qualifying seeds with no five-cycle principal obstruction.

The permitted local model allows any strictly improving adjacent edge choice, any bounded portfolio of starting vertices in the stated face, the usual vertex and ray exits, and arbitrary copositivity tests on diagonal corrections or linear combinations of the stored face rays. We also identify larger sparsity-limited test classes. A globally constructed unrelated separator, input-dependent distant initialization, nonadjacent jumps, or non-descending moves is not charged as an adjacent-pivot rule. No claim about the eventual termination of every rule is needed for a finite lower-bound prefix.

Dannenberg--Schürmann [@DS] study perfect copositive matrices and their neighborhood graph; Oertel--Schürmann [@OS] establish generalized perfectness and the qualitative Interior Ryshkov property. Simultaneous approximation is already an ingredient of that theory. Finiteness under affine lattice equivalence also has substantial antecedents in inhomogeneous reduction theory [@Inhom]. Here the fixed positive definite block, bounded denominator layers, orthant boundary, and the quantitative local-search consequence are essential. The graphical CP and SPN ingredients used below are classical [@Drew; @Barioli; @SPN]; we prove the specific elementary forms needed and distinguish their role from the new amplification statement.

# Finite shear types and intrinsic graph geometry

Let $H\in\mathbb S^r$ be positive definite, not necessarily rational. Define $$g_H(b)=\sup_{u\in\mathbb Z_+^r,\ y\in\mathbb Z_{\ge1}}
 \frac{1-u^{\mathsf T}Hu-2yb^{\mathsf T}u}{y^2},\qquad
 E_H=\{(b,c):c\ge g_H(b)\}.$$ The edge graph uses vertices and bounded one-dimensional faces of this epigraph. It is the graph of a fixed-block face of $\mathcal R_{r+1}$ when $H$ is a perfect vertex of $\mathcal R_r$. For general $H$ it is still a well-defined lattice-convex object.

::: {#lem:gap .lemma}
**Lemma 1** (Uniform gap and edge movement). *Choose an integer $q\ge2$ with $r\lVert H\rVert_2/q^2\le1/2$, and set $$\kappa=(2q^{2r})^{-1},\quad Y=2q^r,\quad
 t\in\mathbb Z_{\ge1},\quad t\ge\max_i\sqrt{(H^{-1})_{ii}},\quad K=Y+t.$$ Let $z$ minimize $x^{\mathsf T}Hx+2b^{\mathsf T}x$ over $x\ge0$, and put $\ell=b+Hz$. Then $$z,\ell\ge0,\quad z_i\ell_i=0,\qquad
 z^{\mathsf T}Hz+\kappa\le g_H(b)\le z^{\mathsf T}Hz+1.$$ The supremum is attained and $E_H$ is locally polyhedral. At any active $(u,y)$ on its graph, $$\label{eq:residual}
 y\le Y,\qquad (u-yz)^{\mathsf T}H(u-yz)+2y\ell^{\mathsf T}u
 =1-y^2(g_H(b)-z^{\mathsf T}Hz)\le1.$$ At each vertex, $0\le\ell_i\le1/2$. Endpoints of every bounded edge satisfy $$\label{eq:move}
 |b'_i-b_i|\le\tfrac12+2\sqrt{H_{ii}}.$$*
:::

::: proof
*Proof.* For $e=u-yz$, completing the square gives $$\frac{1-u^{\mathsf T}Hu-2yb^{\mathsf T}u}{y^2}
 =z^{\mathsf T}Hz+\frac{1-e^{\mathsf T}He-2y\ell^{\mathsf T}u}{y^2}.$$ The last numerator is at most one. Dirichlet's simultaneous approximation on the positive coordinates of $z$ gives $1\le y\le q^r$ and integers $u_i$ within $1/q$ of $yz_i$; take $u_i=0$ on the other coordinates. These integers are nonnegative, $\ell^{\mathsf T}u=0$, and $e^{\mathsf T}He\le1/2$. This proves the lower gap. If $z=0$, use $u=0,y=1$. The approximation follows directly by putting $q^s+1$ fractional-part vectors into $q^s$ boxes, where $s$ is the support size.

Terms with $y>Y$ lie strictly below the lower gap. For the remaining denominators, a term reaching the gap has $e$ in a bounded ellipsoid. This proves attainment and local polyhedrality, uniformly on compact sets since $z(b)$ is continuous by strong convexity. At a vertex the active affine normals $(2u/y,1)$ span $\mathbb R^{r+1}$, so some active $u_i\ge1$ for each $i$. Equation [\[eq:residual\]](#eq:residual){reference-type="eqref" reference="eq:residual"} then gives $\ell_i\le1/2$.

A bounded edge has a common active $(u,y)$ at its endpoints. At either endpoint, $b+Hu/y=\ell+He/y$, and $|(He)_i|\le\sqrt{H_{ii}}$ by Cauchy--Schwarz in the $H$-inner product. Thus both endpoint values of $b_i+(Hu/y)_i$ lie in the same interval $[-\sqrt{H_{ii}}/y,1/2+\sqrt{H_{ii}}/y]$, proving [\[eq:move\]](#eq:move){reference-type="eqref" reference="eq:move"}. ◻
:::

Define the integral shear $$S_a=\begin{pmatrix}I_r&a\\0&1\end{pmatrix},\qquad a\in\mathbb Z^r.$$ For $P=\left(\begin{smallmatrix}H&b\\b^{\mathsf T}&c\end{smallmatrix}\right)$ write $$\overline P=S_a^{\mathsf T}PS_a,
 \quad\bar b=b+Ha,\quad\bar c=c+2b^{\mathsf T}a+a^{\mathsf T}Ha.$$

::: {#thm:templates .theorem}
**Theorem 2** (Finite shear-normal forms). *At every vertex of $E_H$, take $a=\lfloor z\rfloor\in\mathbb Z_+^r$. Then:*

1.  *Every active vector $(u,y)$ has sheared coordinates $(v,y)=(u-ay,y)$ in the fixed finite set $$\mathcal D_H=\{(v,y):v\in\mathbb Z^r,\ |v_i|\le K,\ 1\le y\le Y\}.$$*

2.  *The pairs $(\bar b,\bar c)$ belong to a finite explicitly enumerable containing list, depending only on $H$. More precisely, $$|\bar b_i|\le\tfrac12+\sum_j|H_{ij}|,\qquad
     \kappa\le\bar c\le1+r\lVert H\rVert_2,$$ and each pair is determined by $r+1$ independent equations selected from $\mathcal D_H$.*

3.  *If $D_HH$ is integral, all coordinates of all vertices of $E_H$ have a common denominator dividing $$\Delta_H=D_H\operatorname{lcm}(1,2,\ldots,F_H),\qquad
     F_H=(r+1)![2K^2]^{r+1}.$$ This is an effective, nonoptimized bound, independent of the vertex's location.*

4.  *If $H$ is a positive definite perfect vertex of $\mathcal R_r$, let $n=r+1$, $d=n(n+1)/2$, and $$E_*=(d-1)![2K^2]^{d-1}.$$ Every full tangent cone of $\mathcal R_n$ at a vertex with leading block $H$, after the above shear, is defined by a subset of a fixed finite integer-normal list. Every primitive integral extreme ray $R$ has $$\label{eq:shearedrays}
     |(S_a^{\mathsf T}RS_a)_{ij}|\le E_*.$$ In particular, with $T=1+\lVert a\rVert_1$, the original leading, cross, and last blocks of $R$ have entry bounds $E_*$, $E_*T$, and $E_*T^2$, respectively.*

*The containing list may include unrealized templates; no decision of which template occurs at a prescribed integer translate is assumed.*
:::

::: proof
*Proof.* Put $f=z-a\in[0,1)^r$. From [\[eq:residual\]](#eq:residual){reference-type="eqref" reference="eq:residual"}, $|u_i-yz_i|\le\sqrt{(H^{-1})_{ii}}\le t$, hence $|v_i|\le Y+t=K$. Also $\bar b=\ell-Hf$. Complementarity gives $\ell^{\mathsf T}a=0$: if $\ell_i>0$ then $z_i=a_i=0$. Consequently $$\bar c=(c-z^{\mathsf T}Hz)+f^{\mathsf T}Hf.$$ This proves the bounds in (2). Independence of active affine equations is preserved by the invertible shear. Each selected equation is $$2yv^{\mathsf T}\bar b+y^2\bar c=1-v^{\mathsf T}Hv.$$ There are finitely many choices. Its coefficient entries have magnitude at most $2K^2$. Cramer's rule gives denominators dividing $D_H\det M$ with $0<|\det M|\le F_H$. Inverting the shear introduces only integral coefficients and entries of $H$, proving (3).

For (4), an active vector with last coordinate zero satisfies $H[u]=1$, so $|u_i|\le t$ and is unchanged by the shear. All other active vectors belong to $\mathcal D_H$ after shearing. A full extreme tangent ray annihilates $d-1$ independent integer equations. Cofactors give a generator bounded by $E_*$. Integral unimodular congruence preserves the integral symmetric lattice and primitiveness, proving [\[eq:shearedrays\]](#eq:shearedrays){reference-type="eqref" reference="eq:shearedrays"}. The inverse shear changes blocks by $$(D,w,s)\longmapsto(D,w-Da,s-2a^{\mathsf T}w+a^{\mathsf T}Da),$$ which proves the last bounds. ◻
:::

The denominator bound is stronger than a bit-height bound that grows with the vertex. The same finite alphabet bounds the number of active constraints and the degree of the edge graph, uniformly over a fixed positive definite block. It does not bound the number of vertices in the entire face.

::: {#thm:growth .theorem}
**Theorem 3** (Intrinsic graph growth). *For every real positive definite $H$, the bounded-edge graph of $E_H$ is connected, has uniformly bounded degree, and has polynomial ball growth of exact degree $r$: for each vertex $v$ there are constants $0<c_v\le C_v$ such that $$c_vR^r\le |B_{\mathrm{graph}}(v,R)|\le C_v(1+R)^r$$ for all sufficiently large integers $R$. In the variant $E_H^{\mathbb Z}$ obtained by allowing $u\in\mathbb Z^r$, the edge graph is quasi-isometric to $\mathbb Z^r$. On the region $$z=-H^{-1}b,\qquad z_i>\sqrt{(H^{-1})_{ii}}\quad\text{for every }i,$$ the two epigraphs coincide locally; the full-lattice graph is periodic under integral shears there.*
:::

::: proof
*Proof.* For $E_H$, its recession cone is $\{(w,s):w\ge0,s\ge0\}$: test $u=0$ and then arbitrarily large $u=ke_i$. The affine functional $p(b,c)=c+\sum_i b_i$ has compact sublevel sets on $E_H$. Indeed $c\ge1$ and, when $b_i<0$, taking the nearest nonnegative integer to $-b_i/H_{ii}$ in a $y=1$ constraint gives $$c\ge1+(b_i^-)^2/H_{ii}-H_{ii}/4.$$ Thus negative coordinates of $b$ are $O_H(\sqrt{c+1})$, so $p\le T$ first bounds $c$ and then the positive coordinates. Compact sets meet only finitely many active constraints and vertices. From any nonminimizing vertex a descending extreme ray for $p$ is bounded, since $p$ is positive on every nonzero recession direction. Descending within the finite sublevel graph reaches a minimizing face; this is a compact polytope with connected edge graph. This proves connectivity. The finite active alphabets give bounded degree.

The movement bound gives $\lVert b\rVert_\infty=O_{H,v}(R+1)$ in a radius-$R$ graph ball. At vertices $z=H^{-1}(\ell-b)$ and $\ell\in[0,1/2]^r$, so $a=\lfloor z\rfloor$ has only $O_{H,v}((R+1)^r)$ possibilities. There are finitely many templates over each $a$, proving the upper bound.

For $E_H^{\mathbb Z}$, the continuous center is $z=-H^{-1}b$ and $\ell=0$. The gap, finite alphabets, and finite templates have the same proofs, now with $a\in\mathbb Z^r$. The transformations $$\Psi_a(b,c)=(b-Ha,c-2b^{\mathsf T}a+a^{\mathsf T}Ha)$$ are graph automorphisms. Their action on vertices is free and has a finite quotient. The functional $c$ has compact sublevels, since $c\ge b^{\mathsf T}H^{-1}b+\kappa$, so the same descent argument proves graph connectivity. Connect a fixed representative to the other finitely many representatives and to its translates by $\pm e_i$. Translating these finitely many paths gives an upper distance bound linear in $\lVert a\rVert_1$. The movement bound gives a matching lower bound up to additive constants. This proves the asserted quasi-isometry without invoking a group-action theorem.

If all center coordinates exceed the stated thresholds, every constraint with a negative coordinate in $u$ has $e^{\mathsf T}He>1$, by $e^{\mathsf T}He\ge e_i^2/(H^{-1})_{ii}$. Such a constraint lies below the continuous quadratic value, whereas the nonnegative constraints exceed it by $\kappa$. Thus it does not affect the epigraph, proving local coincidence.

Take the finite connecting paths from a full-lattice base vertex to its $+e_i$ translates. Translate all of them sufficiently far into the above open region. Every additional nonnegative integral translate remains there. This embeds a network indexed by $\mathbb Z_+^r$ in the bounded-edge graph of $E_H$, with generator paths of a fixed finite length. Distinct indices give distinct vertices. Therefore a graph ball at its base contains $\Omega_H(R^r)$ vertices. Connectivity transfers the lower bound, with a fixed distance offset, to any other base vertex. ◻
:::

::: corollary
**Corollary 4** (Large intrinsic distance at small encoding height). *For rational $H>0$, the graph of $E_H$ contains vertex pairs at graph distance $\Omega_H(M)$ and coordinate bit height $O_H(\log(M+1))$. For $H=T_r$ one may use canonical forms translated by $a=Me_1$; their cross columns differ by $MH e_1$. The distance lower bound follows from [\[eq:move\]](#eq:move){reference-type="eqref" reference="eq:move"}. This concerns the intrinsic face graph, not distances after allowing paths outside the face.*
:::

# A general fixed-block amplification theorem

We now separate a small, verifiable seed from the scale that makes local search difficult.

::: {#def:seed .definition}
**Definition 5** (Certified seed). Let $n=r+1$. A certified seed consists of:

1.  a rational positive definite perfect vertex $H\in\mathcal R_r$;

2.  a rational matrix $B=\left(\begin{smallmatrix}C&c\\c^{\mathsf T}&a\end{smallmatrix}\right)\succ0$ with all entries positive;

3.  nonnegative integer vectors $v_j$ with $H[v_j]=1$, whose squares span $\mathbb S^r$, and positive rational $\lambda_j$ such that $$\label{eq:reserve} C=\sum_j\lambda_jv_jv_j^{\mathsf T};$$

4.  a rational $W\in\mathcal{COP}_n$ with $\langle W,B\rangle=-\gamma<0$.

A copositivity proof for $W$ is part of the seed certificate. No dimension-uniform polynomial copositivity oracle is assumed.
:::

These conditions are finite and exactly checkable. For $H>0$, integer-minimum feasibility is reduced to finitely many vectors using $\lambda_{\min}(H)\ge1/\operatorname{tr}(H^{-1})$. The spanning and positive-combination tests are rational linear algebra. In a fixed dimension copositivity also has exact finite decision procedures; the graphical seeds in the next section have direct copositivity proofs.

Here are explicit constants for the theorem. They are deliberately generous. Use $q,Y,t,K,E_*$ from Theorem [2](#thm:templates){reference-type="ref" reference="thm:templates"}, with $q$ chosen using $\lVert H\rVert_\infty$ instead of $\lVert H\rVert_2$. Fix $b_0\ge0$ bounding the cross-column norm at every allowed starting vertex. Set $$\begin{split}
 h&=\lVert H\rVert_\infty,\quad j=\lVert H^{-1}\rVert_\infty,\quad
 L=1+2h,\quad B_*=b_0+L+1,\\
 Z_*&=\max\{1,\lceil j(B_*+1/2)\rceil\},\quad T_*=1+rZ_*,\\
 P_*&=rh+2rB_*+rhZ_*^2+1,\quad
 \alpha=\langle C,H\rangle>0.
 \end{split}$$ The norm $\lVert \cdot\rVert_\infty$ here is the maximum absolute row sum. Let $D_C\ge1$ be an integer with $D_CC$ integral, $w=1+\sum_{ij}|W_{ij}|$, and define positive rational constants $$\label{eq:robustconstants}
 \begin{split}
 \mu&=1/\operatorname{tr}(B^{-1}),\quad \theta=\gamma/(4\operatorname{tr}B),\\
 \zeta&=\min\{1,\mu/2,\tfrac12\min_{ij}B_{ij},
                    \gamma/[4(w+n\theta+1)]\},\\
 s_0&=1+\sum_{ij}B_{ij}+\zeta.
 \end{split}$$ One may decrease $\zeta$ to retain further open properties of the seed. Finally put $$\begin{split}
 u&=2\lVert c\rVert_1 E_*T_*,\qquad v=(a+n\zeta)E_*T_*^2,\\
 u_2&=2\lVert c\rVert_1 B_*,\qquad v_2=\zeta P_*,\\
 \Gamma&=\left\lceil\max\{1,4D_C(u+v+1),4(u_2+v_2+1)/\alpha\}\right\rceil.
 \end{split}$$ All constants depend only on the certified seed and the bounded starting region.

::: {#thm:amplification .theorem}
**Theorem 6** (Seed amplification, all choices and bounded portfolios). *Given a certified seed, let $m\ge1$, $N=\Gamma(m+1)$, $D_N=\operatorname{diag}(NI_r,1)$, and $$A_N=\frac{D_NBD_N}{s_0N^2},\qquad
 W_N=D_N^{-1}WD_N^{-1}+\frac\theta{N^2}I.$$ For every symmetric $A$ in the ball $$\label{eq:ball}
 \lVert A-A_N\rVert_F\le\frac\zeta{s_0N^2},$$ we have $\lVert A\rVert_F\le1$, $A\succ0$, all entries of $A$ positive, and $A\notin\mathcal{CP}_n$. Starting at *any* vertex of $\mathcal R_n$ with leading block $H$ and $\lVert b\rVert_\infty\le b_0$, every strictly improving adjacent-pivot rule makes at least $m$ pivots before a current-vertex or selected-ray separator can occur. Every improving ray during this prefix remains tangent to the fixed-block face and has a bounded adjacent endpoint.*

*No arbitrary diagonal correction of any of these rays can be a separator. The same holds for diagonal corrections of arbitrary real linear combinations of any stored prefix rays. More generally, every copositive candidate with a fixed SPN sparsity mask is ineffective on these inputs.*

*One rational separator works on the entire ball: $$W_N[x]\ge\theta N^{-2}\lVert x\rVert_2^2\quad(x\ge0),\qquad
 \lVert W_N\rVert_F\le w+n\theta,\qquad
 \langle W_N,A\rangle\le-\frac\gamma{2s_0N^2}.$$ Thus $\operatorname{dist}_F(A,\mathcal{CP}_n)\ge\gamma/[2s_0(w+n\theta)N^2]$. For each fixed seed the rational centers have input-and-distance bit parameter $\Theta(\log(m+1))$, whereas their forced pivot count is at least $m$. The separator entries and all objects visited in the prefix have $O(\log(m+1))$ bit height. Generation from a certified seed is polynomial in the seed-certificate length and $\log(m+1)$ for fixed dimension.*
:::

::: proof
*Geometric and arithmetic confinement.* The equalities $P[(v_j,0)]=1$ define the face with leading block $H$, because the squares in [\[eq:reserve\]](#eq:reserve){reference-type="eqref" reference="eq:reserve"} span. This face is $E_H$. Every point in it is strictly copositive: with the notation of Lemma [1](#lem:gap){reference-type="ref" reference="lem:gap"}, $$P[(x,y)]=(x-yz)^{\mathsf T}H(x-yz)+2y\ell^{\mathsf T}x+(c-z^{\mathsf T}Hz)y^2>0$$ for nonzero $(x,y)\ge0$. Hence the full Ryshkov set is locally polyhedral there, with the usual pointed tangent cone at a vertex.

Write $M=m+1$. Any vertex reachable in at most $m$ bounded face edges from the allowed starting region has $$\lVert b\rVert_\infty\le B_*M,\quad \lVert z\rVert_\infty\le Z_*M,\quad
 1+\lVert \lfloor z\rfloor\rVert_1\le T_*M,\quad \lVert P\rVert_F\le P_*M^2.$$ These follow from the movement bound and $z=H^{-1}(\ell-b)$; $c\le z^{\mathsf T}Hz+1$ gives the last estimate. For any full primitive integral extreme ray write $R=\left(\begin{smallmatrix}D&w_R\\w_R^{\mathsf T}&s_R\end{smallmatrix}\right)$. Theorem [2](#thm:templates){reference-type="ref" reference="thm:templates"} yields $$|D_{ij}|\le E_*,\quad |(w_R)_i|\le E_*T_*M,\quad
 |s_R|\le E_*T_*^2M^2,\quad \lVert R\rVert_F\le nE_*T_*^2M^2.$$ Feasibility at the top minimal vectors gives $$\langle C,D\rangle\ge0,\qquad \langle C,D\rangle=0\ \Longleftrightarrow\ D=0.$$ Since $R$ is integral, a positive value is at least $1/D_C$.

Write the positively rescaled perturbed objective as $\widetilde B=s_0N^2A=D_NBD_N+Z$, $\lVert Z\rVert_F\le\zeta$. Every ray with $D\ne0$ consequently satisfies $$\langle \widetilde B,R\rangle\ge N^2/D_C-uNM-vM^2
 \ge\frac{3N^2}{4D_C}>0.$$ So every improving ray has $D=0$. The recession directions of $E_H$ have nonnegative cross column and nonnegative last entry; the strictly positive objective makes their costs positive. Thus an improving ray is bounded and reaches a face neighbor. Also, since $c_P\ge1$ and $a>0$, $$\langle \widetilde B,P\rangle\ge\alpha N^2-u_2NM-v_2M^2
 \ge3\alpha N^2/4>0.$$ No current vertex separates.

Nonmembership ensures an improving extreme ray exists: otherwise the objective lies in the minimizing normal cone generated by the active nonnegative rank-one matrices, hence in $\mathcal{CP}_n$. This contradicts the separator below. The argument applies inductively to all choices, simultaneously from every allowed start. The finite-prefix induction does not require eventual termination or uniqueness. ◻
:::

::: proof
*Robust separator and resource statements.* Since $N\ge1$, the least eigenvalue and least entry of $D_NBD_N$ are bounded below by $\mu$ and $\min B_{ij}$. The choices of $\zeta$ preserve strict positivity and positive definiteness. The normalization $s_0$ bounds the Frobenius norm by one. Positive diagonal congruence preserves copositivity, and $$\langle D_N^{-1}WD_N^{-1},D_NBD_N\rangle=-\gamma,
 \qquad \operatorname{tr}(D_NBD_N)\le N^2\operatorname{tr}B.$$ The diagonal correction costs at most $\gamma/4$, and the perturbation costs at most $\gamma/4$. This proves the pairing bound, positive cone margin, and distance estimate.

All seed-dependent constants are fixed. Since $N=\Gamma(m+1)$, center and separator heights are $O(\log(m+1))$. The nonzero last diagonal of $A_N$ is a fixed rational multiple of $N^{-2}$, giving the reverse encoding bound. The distance estimate gives the upper precision bound. The finite-template denominator theorem and inverse-shear formulas bound every visited vertex; the sheared-ray bound does the same for rays. All square roots in parameter upper bounds can be replaced by integer ceilings obtained by rational comparisons. Determinants and inverses have polynomial bit growth in a fixed dimension. No cost of discovering or proving the seed's copositivity certificate is hidden in the generation claim. ◻
:::

## Why arbitrary diagonal corrections do not help

The following is the arrow case of the classical SPN theory [@SPN Theorem 5.4]; its direct proof makes the algorithmic consequence transparent.

::: {#lem:arrow .lemma}
**Lemma 7** (Copositive arrow matrices). *If $$Q=\begin{pmatrix}\operatorname{diag}(p)&w\\w^{\mathsf T}&a\end{pmatrix}$$ is copositive, it is a sum of a positive semidefinite matrix and an entrywise nonnegative matrix. In particular it cannot have negative pairing with a doubly nonnegative matrix.*
:::

::: proof
*Proof.* We have $p_i,a\ge0$, and $p_i=0$ forces $w_i\ge0$. Restricting the quadratic form to the indices with $w_i<0$ and minimizing at last coordinate one gives $$a\ge\sum_{w_i<0} w_i^2/p_i.$$ Replace all positive spokes by zero. The resulting arrow matrix is positive semidefinite by this Schur-complement inequality; what was removed is entrywise nonnegative. The trace pairing with a doubly nonnegative matrix is nonnegative on both summands. ◻
:::

Every prefix ray has zero leading block. Its arbitrary diagonal correction, and the diagonal correction of any linear combination of stored rays, is an arrow matrix. This proves the corresponding clauses of Theorem [6](#thm:amplification){reference-type="ref" reference="thm:amplification"}, even if the diagonal correction has signed entries, provided the resulting matrix is copositive.

A graph is called SPN when every copositive matrix supported on it is PSD plus nonnegative. Any separator test confined to that matrix support is therefore ineffective on a doubly nonnegative input, regardless of its internal computation. As a concrete larger test class, partition the leaf indices into groups of at most three and allow arbitrary entries inside each group, as well as all spokes and diagonals. The resulting graph is a vertex-sum of cliques of order at most four, hence SPN [@SPN Corollaries 4.4 and 5.3]. This allows entire small-block corrections, not just a scalar or diagonal update. The graph fact is prior work; its application to every stored tangent direction is the present algorithmic conclusion.

## What the seed hypotheses do and do not imply

Strict exposure in [\[eq:reserve\]](#eq:reserve){reference-type="eqref" reference="eq:reserve"} is a sufficient condition, not asserted necessary for every possible hard instance. It is necessary for this positive-gap confinement argument: if $C$ is outside the normal cone of $H$, a top tangent direction $D$ has $\langle C,D\rangle<0$. At a fixed starting vertex it extends to a full tangent direction by choosing a sufficiently large last entry. Decomposition into finitely many extreme rays gives one with negative top cost; for large $N$ that ray improves and leaves the fixed-block face.

Arbitrary fixed portfolios with *different* leading perfect blocks are not covered. No single $C$ can be in the interiors of the minimizing normal cones of two distinct perfect blocks: it would make both the unique minimizer. This is an obstruction to applying the present certificate simultaneously, not a proof that a different hardness construction for such portfolios is impossible.

# Graphical seeds: an exact interval and collective obstructions

The amplification theorem does not require a five-cycle or a Horn witness. We give an entire class of seeds and an exact structural criterion for when it works. Comparison-matrix facts in this section are classical [@Drew; @Kogan]; the new use is to supply certified local-search obstructions and examples without a smaller principal obstruction.

For a symmetric nonnegative matrix $X$, let $M(X)$ retain its diagonal and negate its off-diagonal entries.

::: {#lem:comparison .lemma}
**Lemma 8** (Triangle-free comparison criterion). *If $X\ge0$ is symmetric and $M(X)\succeq0$, then $X\in\mathcal{CP}$. Conversely, if the support graph of $X$ is triangle-free and $X\in\mathcal{CP}$, then $M(X)\succeq0$.*
:::

::: proof
*Proof.* For $M(X)\succ0$, its inverse is nonnegative: write it as $tI-K$ with $K\ge0$ and $t>\rho(K)$, and use the Neumann series. Thus $d=M(X)^{-1}{\bf1}>0$. The matrix $\operatorname{diag}(d)X\operatorname{diag}(d)$ is diagonally dominant and nonnegative, since its $i$th diagonal excess is $d_i(M(X)d)_i=d_i$. It is a positive combination of singleton squares and squares $(e_i+e_j)(e_i+e_j)^{\mathsf T}$. Positive diagonal congruence preserves complete positivity. If $M(X)$ is only semidefinite, apply this argument to $X+\varepsilon I$ and use closedness of $\mathcal{CP}$ (its trace-one base is the convex hull of a compact set of normalized nonnegative rank-one matrices).

For the converse, structural zeros force each nonnegative Gram column to be supported on a clique. A triangle-free graph has cliques of size at most two. Negating the off-diagonal entry of a two-supported rank-one matrix gives another PSD rank-one matrix. Summing these comparison matrices proves the assertion. ◻
:::

Let $A_0\in\mathbb S^r(\mathbb Q)$ be positive definite, nonnegative, and supported on a disjoint union of paths, with strictly positive edge weights. Singletons are allowed. Label the components consecutively. Let $c\in\mathbb Q_+^r$, with no two adjacent positive entries. Joining a hub to the positive coordinates of $c$ gives a triangle-free graph $G$. Put $$M_0=M(A_0),\quad v=M_0^{-1}c,\quad
 \alpha=c^{\mathsf T}A_0^{-1}c,\quad\beta=c^{\mathsf T}M_0^{-1}c,\quad
 F(a)=\begin{pmatrix}A_0&c\\c^{\mathsf T}&a\end{pmatrix}.$$

::: {#thm:seedinterval .theorem}
**Theorem 9** (Exact seed interval and normal-cone realization). *For $a\ge0$, $$F(a)\succ0\iff a>\alpha,\qquad
 F(a)\in\mathcal{CP}_{r+1}\iff a\ge\beta.$$ In particular the positive definite non-CP interval is exactly $(\alpha,\beta)$. It is nonempty precisely when, in some path component, the hub attaches to both bipartition classes. Under the no-adjacent-attachment assumption this is equivalent to $G$ containing an odd cycle of length at least five.*

*Whenever $\alpha<a<\beta$ is rational, a rational positive diagonal congruence followed by an explicitly small CP reserve turns $F(a)$ into a certified seed for the canonical leading block $T_r$. Thus every such weighted graphical obstruction produces the all-rule canonical exponential lower bound, including the arbitrary-diagonal test and multi-start conclusions of Theorem [6](#thm:amplification){reference-type="ref" reference="thm:amplification"}.*
:::

::: proof
*Proof.* Bipartite sign switching gives $M_0=JA_0J\succ0$ for a diagonal $J$ with entries $\pm1$. Its inverse is nonnegative, and strictly positive within each nontrivial connected component. The two Schur complements and Lemma [8](#lem:comparison){reference-type="ref" reference="lem:comparison"} give the two equivalences. If the color classes are $U,V$, then $$\beta-\alpha
 =4\sum_{\substack{i\in U,\ j\in V}}c_ic_j(M_0^{-1})_{ij}.$$ Terms between distinct components vanish. This proves the strictness criterion. A path between opposite-colored attachments has odd length; excluding adjacent attachments makes that length at least three, and adding the hub makes an odd cycle of length at least five. Conversely every cycle in a path forest plus a hub arises this way.

The separator is explicit. Let $Q_G={\bf1}{\bf1}^{\mathsf T}-2\operatorname{Adj}(G)$. This is copositive because a triangle-free graph satisfies $\sum_{ij\in E(G)}x_ix_j\le(\sum_i x_i)^2/4$. For clarity, on the simplex choose a maximizer with smallest support; merge nonadjacent positive coordinates into the one with larger neighbor sum, without reducing the objective. The support becomes a clique, of size at most two, where the bound is elementary. Hence $$W_F=\operatorname{diag}(v,1)Q_G\operatorname{diag}(v,1)\in\mathcal{COP}_{r+1},\qquad
 \langle W_F,F(a)\rangle=a-\beta<0.$$ Zero entries of $v$ cause no problem.

Set $d=M_0^{-1}{\bf1}>0$ and $D=\operatorname{diag}(d,1)$. The leading block of $DF(a)D$ has the exact decomposition $$\operatorname{diag}(d)A_0\operatorname{diag}(d)
 =\sum_i d_i e_ie_i^{\mathsf T}
 +\sum_{ij\in E(A_0)}(A_0)_{ij}d_id_j(e_i+e_j)(e_i+e_j)^{\mathsf T}.$$ All displayed vectors are minimal for $T_r$, since each path edge joins consecutive coordinates. Let $C_n$ be the sum of all consecutive-interval squares in dimension $n=r+1$. Its entries are $\min(i,j)(n+1-\max(i,j))$. Put $$W'=D^{-1}W_FD^{-1},\quad \gamma_0=\beta-a,\quad
 w'=1+\sum_{ij}|W'_{ij}|,\qquad
 \varepsilon=\frac{\gamma_0}{4w'\operatorname{tr}C_n}.$$ Then $$B=DF(a)D+\varepsilon C_n$$ is positive definite and strictly positive. Its leading block is a positive combination of all top-interval squares, which span $\mathbb S^r$. Finally $\langle W',B\rangle\le-3\gamma_0/4<0$, because $\lVert C_n\rVert_F\le\operatorname{tr}C_n$. These are the certified-seed conditions. The identity $$T_j[x]=\tfrac12\left(x_1^2+x_j^2+\sum_{i<j}(x_i-x_{i+1})^2\right)$$ proves integer minimum one, with positive consecutive-interval minimal vectors whose squares span. Thus $T_r$ is perfect, and the face contains the actual canonical start $T_n$. ◻
:::

This is a sharp characterization *within the stated graphical class*. If all attachments stay within one color class per component, $\alpha=\beta$ and no choice of hub diagonal can be both positive definite and non-CP. It does not classify arbitrary nonmembers or arbitrary support graphs.

## Long odd cycles and collective minimal nonmembers

For a single even-length path with $s\ge4$ vertices, take $$A_0=I_s+\tfrac14\operatorname{Adj}(P_s),\qquad c=e_1+e_s.$$ The support of $F(a)$ is the chordless odd cycle of length $s+1$. The interval in Theorem [9](#thm:seedinterval){reference-type="ref" reference="thm:seedinterval"} is nonempty. Already at lengths seven and nine there is no five-cycle principal support, so these are not padded or diagonally rescaled five-cycle examples.

More substantially, use any number of path components, each attached to the hub at both endpoints (and, optionally, singleton leaves). Require at least one even-length path with at least four vertices and no component that creates a triangle. All coordinates of $v=M_0^{-1}c$ are then positive and $\beta>\alpha$. For each top coordinate put $$\Delta_i=\frac{v_i^2}{(M_0^{-1})_{ii}}>0,\qquad
 \delta=\tfrac12\min\{\beta-\alpha,\min_i\Delta_i\},\qquad a=\beta-\delta.$$

::: {#thm:minimal .theorem}
**Theorem 10** (Collective principal-minimal obstructions). *The matrix $F(a)$ is rational, positive definite, nonnegative, and not completely positive, while *every proper principal submatrix is completely positive*. The same is true after the normal-cone congruence and CP reserve in Theorem [9](#thm:seedinterval){reference-type="ref" reference="thm:seedinterval"}, except that the resulting seed is strictly entrywise positive. Thus the amplification theorem applies to positive definite, strictly positive nonmembers of unbounded order with no smaller principal nonmember. In particular this holds for bouquets of two or more chordless seven-cycles sharing only their hub, which contain no five-cycle.*
:::

::: proof
*Proof.* The full matrix has Schur complement $a-\alpha=\beta-\alpha-\delta>0$, while the comparison Schur complement is $a-\beta=-\delta<0$. For deletion of a top coordinate $i$, block inversion gives the exact identity $$c^{\mathsf T}M_0^{-1}c-c_{-i}^{\mathsf T}(M_0[-i])^{-1}c_{-i}
 =v_i^2/(M_0^{-1})_{ii}=\Delta_i.$$ Thus the comparison matrix of $F(a)[-i]$ is positive definite: its Schur complement is $\Delta_i-\delta>0$. It is CP by Lemma [8](#lem:comparison){reference-type="ref" reference="lem:comparison"}. Deleting the hub leaves $A_0$, whose comparison matrix is positive definite, so it too is CP. Every smaller principal submatrix is contained in one of these. Positive diagonal congruence and addition of a CP matrix preserve complete positivity on every proper principal submatrix; the separator retains global nonmembership after the prescribed reserve. ◻
:::

For two six-vertex paths, so $n=13$, each path has $$\alpha_0=\frac{152}{71},\qquad \beta_0=\frac{88}{41},\qquad
 \beta_0-\alpha_0=\frac{16}{2911}.$$ The deletion margins in the two-block matrix exceed $16/2911$. More generally, the proof allows any $0<\delta<\min(\beta-\alpha,\min_i\Delta_i)$, so one may take $\delta=16/2911$ and $$a=2\beta_0-\frac{16}{2911}=\frac{12480}{2911}.$$ Each seven-cycle principal block is CP, as is every other proper principal block, yet the complete thirteen-dimensional matrix is not. The strict reserve preserves this fact. This is a shared-diagonal-budget obstruction, not an inherited bad five-dimensional principal block.

The strict reserve also makes each proper principal submatrix an interior CP point: on any ordered subset, restricted interval vectors include all consecutive intervals of that subset. Their squares span. Therefore the principal-minimal property persists on a sufficiently small open ball. An effective rational radius is obtained from any such finite atom basis: if $B_I$ is its sum, the inverse basis map bounds the perturbation coefficients, and half the smallest positive reserve coefficient is an admissible threshold. Taking the minimum over the finitely many proper index sets and decreasing $\zeta$ in [\[eq:robustconstants\]](#eq:robustconstants){reference-type="eqref" reference="eq:robustconstants"} preserves the property throughout the amplified ball. This is a finite exact calculation for fixed order, not an unquantified claim of a uniform dimension-free radius.

::: {#cor:principaltests .corollary}
**Corollary 11** (All proper-principal certificate tests are ineffective). *For the principal-minimal amplified families, no copositive matrix supported on a proper principal index set can separate the input, nor can any nonnegative combination of such certificates. This holds throughout an explicitly computable perturbation ball. Thus even exact tests on *all* proper principal submatrices do not bypass these examples.*
:::

::: proof
*Proof.* For every proper $I$, complete positivity of $A[I]$ gives $\langle A[I],W[I]\rangle\ge0$ for every copositive $W[I]$. Summation proves the assertion for conic combinations.

Here is one finite radius that also makes the preceding robustness statement explicit. In the full CP reserve select $d=n(n+1)/2$ independent atom squares with coefficients at least one. Let $U$ have their upper-triangle coordinate vectors as columns, and set $L_U=\max_i\sum_j|(U^{-1})_{ij}|$. A perturbation $Z$ of Frobenius norm at most $\varepsilon/(2\max(1,L_U))$ has basis coefficients bounded by $\varepsilon/2$. Therefore $\varepsilon\mathcal B+Z$ is CP, where $\mathcal B$ is the reserve. For a proper principal set $I$, embed any perturbation of its block with zeros outside $I$, apply this fact, and restrict back to $I$. Adding the already-CP principal block of the unreserved seed proves the claim. Positive diagonal scaling with entries at least one does not enlarge a perturbation under its inverse. Consequently decreasing $\zeta$ in [\[eq:robustconstants\]](#eq:robustconstants){reference-type="eqref" reference="eq:robustconstants"} to this radius suffices. For the interval reserve $C_n$, the interval-weight inverse uses four-term differences, so $L_U\le4$ and $\varepsilon/8$ is sufficient. The tree reserve also has an explicit full atom basis, described in Proposition [12](#prop:tree){reference-type="ref" reference="prop:tree"}; its inverse is a finite rational calculation. The supplied certificates include this calculation. ◻
:::

## Canonical portfolios and noncanonical perfect blocks

The canonical choice is one admissible start, but not the only one. Integral shears of $T_n$ by any fixed nonnegative integer vector preserve its leading block and give perfect vertices: the inverse images of the original interval minimal vectors remain nonnegative and their squares still span. Any bounded collection of these, and indeed all vertices in any bounded cross-column region of the face, is covered simultaneously by Theorem [6](#thm:amplification){reference-type="ref" reference="thm:amplification"}. The general theorem also applies to other positive definite perfect leading blocks whenever the finite reserve certificate is provided. We do not claim that the interval construction automatically supplies seeds for every such block.

## Branched leading blocks: a second normal geometry

The tridiagonal block is not essential even to the graphical realization. Let $T$ be a tree on $r$ vertices such that $$H_T=I_r-\tfrac12\operatorname{Adj}(T)>0.$$ For each unordered pair of vertices, including repeated pairs, let $p_{ij}$ be the indicator of their unique tree path. The integer quadratic form $H_T[x]=\sum_i x_i^2-\sum_{ij\in E(T)}x_ix_j$ is positive integral on nonzero integer vectors, and $H_T[p_{ij}]=1$. These path squares span $\mathbb S^r$: the four-term difference of path quadratic values, obtained by deleting either endpoint or both, is $2X_{ij}$. Thus $H_T$ is a positive definite perfect vertex.

::: {#prop:tree .proposition}
**Proposition 12** (Tree normal-cone realization). *Theorem [9](#thm:seedinterval){reference-type="ref" reference="thm:seedinterval"} and its principal-minimal construction extend when the leading support is a forest contained in such a tree $T$. The certified leading block is then $H_T$. In particular they apply to the branched $D_r$ trees, $r\ge4$, and to every bounded portfolio in their fixed-block faces.*
:::

::: proof
*Proof.* The comparison and Schur-complement proofs are unchanged. Every singleton and every support-edge pair is now a minimal vector of $H_T$, so the same positive diagonal scaling puts the leading block in the appropriate normal cone. For a strictly positive reserve use $$\mathcal B_T=
 \sum_{i\le j}\bigl[(p_{ij},0)(p_{ij},0)^{\mathsf T}+
                       (p_{ij},1)(p_{ij},1)^{\mathsf T}\bigr]+e_ne_n^{\mathsf T}.$$ Its leading block is twice the sum of all path squares. All its entries are positive. The summands span $\mathbb S^n$: the unlifted terms span the leading block, $e_ne_n^{\mathsf T}$ gives the last entry, and the singleton lifted terms supply the cross columns. Hence $\mathcal B_T$ is an interior CP matrix. Add $\varepsilon\mathcal B_T$, where $\varepsilon=(\beta-a)/(4w'\operatorname{tr}\mathcal B_T)$, exactly as before. This preserves the separator and provides a positive normal reserve. Proper principal matrices remain CP, and become interior after the reserve.

For completeness the $D_r$ tree has edges $i(i+1)$ for $1\le i\le r-2$ and $(r-2)r$. Its matrix is half the Gram matrix of the independent vectors $e_1-e_2,\ldots,e_{r-1}-e_r,e_{r-1}+e_r$, so it is positive definite. Attach the last new vertex to vertex $1$ to obtain a $D_{r+1}$ tree; its perfect form is an explicit starting vertex with leading block $H_T$. The matrix $H_T$ is not a permutation or positive diagonal congruence of a tridiagonal block, since its off-diagonal support is branched. ◻
:::

For example, on $D_7$ use $A_0=I+\operatorname{Adj}(D_7)/4$ and attach the hub to vertices $1$ and $6$. The resulting support has a seven-cycle and a pendant branch, and no five-cycle. The principal-minimal choice of the hub diagonal makes every proper principal matrix CP while the full order-eight seed is non-CP. The amplified family starts at a $D_8$ perfect form, whereas the path families above continue to start at the actual canonical $T_n$. The role of the new example is to demonstrate a different qualifying normal geometry, not to replace or weaken the canonical theorem.

# Restrictions, provenance, and reproducibility

## Three failed extrapolations

Positive definiteness of the leading block is substantive for the finite-type geometry. For the singular but strictly copositive block $H={\bf1}{\bf1}^{\mathsf T}$ of order two, $$g_H(b_1,b_2)=g_1(\min(b_1,b_2)),$$ since for a fixed integer $u_1+u_2$ all mass can be assigned to a coordinate of minimum $b_i$. For $H=1$, nearest-integer rounding shows that $y=1$ constraints suffice: for $b<0$ they give $g_1(b)\ge b^2+3/4$, whereas $y\ge2$ gives at most $b^2+1/4$; for $b\ge0$, $g_1(b)=1$. It follows that the vertices of $E_H$ are exactly $$b_1=b_2=-(k+\tfrac12),\quad c=k^2+k+1,\qquad k=0,1,\ldots.$$ At such a vertex the active last-coordinate-one vectors include every $(u_1,u_2,1)$ with $u_1+u_2=k$ or $k+1$, a total of $2k+3$. The bounded-edge graph is a ray: the increasing parts of $g_1$ force the two coordinates to coincide at a vertex, and consecutive common affine pieces join exactly successive $k$. Thus the active cardinality is unbounded and growth has degree one rather than the block order two. Strict copositivity cannot replace positive definiteness in Theorems [2](#thm:templates){reference-type="ref" reference="thm:templates"}--[3](#thm:growth){reference-type="ref" reference="thm:growth"}.

The triangle-free restriction in the comparison criterion also matters. The all-ones matrix of order three is CP, but its comparison matrix $2I-J$ has negative value on ${\bf1}$. Consequently the exact hub-budget criterion is not asserted for arbitrary graphs. Even within the triangle-free class, if all attachments stay in one bipartition class, the two thresholds coincide and there is no positive-definite nonmember interval.

Finally, a positive definite top objective need not expose the intended face. At $H=T_2$, the tangent matrix $$D=\begin{pmatrix}2&-1\\-1&0\end{pmatrix}$$ is feasible at the three minimal vectors, but has pairing $-2$ with $C=\left(\begin{smallmatrix}1&2\\2&5\end{smallmatrix}\right)>0$. Thus mere positive definiteness of $C$ cannot replace the positive normal-cone reserve. The preceding discussion of distinct leading blocks further limits the multi-start conclusion.

## What is new in the argument

The amplification theorem is the principal assertion. It makes the original lower-bound construction reusable for any certified seed, and its finite shear alphabet improves the sufficient scale to $N=\Gamma(m+1)$. The separate graph-growth theorem applies even when no nonmember objective is supplied. The principal-minimal families show that the additional scope is not an embedded five-cycle with unused coordinates. The branched $D_r$ example changes the normal geometry as well as the seed support.

Several important ingredients are not new. The simplex method and perfect-form framework are due to [@DSV; @DS]. Qualitative generalized Interior Ryshkov theory, including simultaneous approximation, appears in [@OS]. Affine lattice reduction and finiteness of inhomogeneous perfect forms have a substantial earlier theory [@Inhom]; the present claim concerns a fixed principal block, all bounded denominator layers, and the nonnegative-coordinate boundary. Comparison-matrix criteria and the CP graph characterization are classical [@Drew; @Kogan]. Barioli [@Barioli] already studies the difference between the positive-semidefinite and CP thresholds for a bordered matrix, including odd cyclic and excellent graphs. Accordingly we do not claim the first such threshold phenomenon. Our exact graphical formulas are a constructive route into the amplification hypotheses, and their collective deletion margins prevent a smaller principal certificate from explaining the lower bound.

The arrow SPN lemma and the SPN block-sum rule are prior results [@SPN]. We use the acyclic and order-at-most-four block statements, not the broader triangular-book claim affected by the corrigendum [@SPNcorr]. The current survey [@SPNsurvey] was also consulted. The new algorithmic statement is that all tested prefix directions, including linear combinations, remain in the arrow space, and that an entire principal-minimal amplified family defeats every proper-principal separator test. A proof of our sufficient conditions is not an assertion that all nonmembers satisfy them, and a targeted literature comparison is not an exhaustive historical first-priority certificate.

## Exact checks and preservation

The universal conclusions above are analytical. The accompanying standard-library generator and separately written verifier test eight seed families: cycles of lengths five, seven, and nine; two seven-cycles with a common hub; a five-cycle and a four-cycle; a five-cycle with a leaf; a weighted multiple-attachment path; and a branched $D_7$ leading block. They check 65 maximal proper principal CP certificates, 18 exact scale choices, the positive normal decompositions, exact copositive witness pairings, and rational reserve inverses for principal stability. The greatest prescribed prefix is $m=2^{64}$; it is certified by the theorem, not simulated.

The geometric checks cover 20 vertices, 142 active identities, and 128 tangent rays, including large integer shears. An independent upper-line-hull implementation reproduces seven full-lattice templates for $H=1,4,9$, including active denominators two and three. Three arbitrary-diagonal arrow decompositions and four failed-generalization groups are checked. Nine deliberately corrupted data sets are rejected. Integer Bareiss determinants, modular rank witnesses, and direct inverse-product checks provide a code path independent of the generator. These tests are not human peer review or proof-assistant verification.

The original canonical theorem, its source, and its verification suite are retained unchanged in the release. The original suite was rerun successfully, preserving its certificate hash. The new manuscript neither changes the local-rule definition to evade that theorem nor substitutes a constrained-column cone for ordinary complete positivity. Every new family remains an ordinary $\mathcal{CP}_n$ nonmember.

The mathematical limitation left by the present theory is precise: an arbitrary portfolio spanning distinct leading perfect blocks, arbitrary input-dependent restarts, nonlocal jumps, and unrestricted global certificate searches are not covered. The latter can succeed quickly on these families because the separator is explicitly available. The large constants are effective bounds, not a proposed practical hard-instance generator in high dimension.

::: thebibliography
12 M. Dutour Sikirić, A. Schürmann, F. Vallentin, A simplex algorithm for rational cp-factorization, Mathematical Programming 187 (2021), 25--45. DOI: 10.1007/s10107-020-01467-4. V. Dannenberg, A. Schürmann, Perfect copositive matrices, Communications in Mathematics 31 (2023), 137--156. DOI: 10.46298/cm.11141. A. Oertel, A. Schürmann, Generalized perfect matrices, arXiv:2602.05841v2 (2026). M. Dutour Sikirić, A. Schürmann, F. Vallentin, Inhomogeneous extreme forms, Annales de l'Institut Fourier 62 (2012), 2227--2255. DOI: 10.5802/aif.2748. N. Shaked-Monderer, SPN graphs: When copositive = SPN, Linear Algebra and its Applications 509 (2016), 82--113. DOI: 10.1016/j.laa.2016.07.018. J. H. Drew, C. R. Johnson, R. Loewy, Completely positive matrices associated with M-matrices, Linear and Multilinear Algebra 37 (1994), 303--310. DOI: 10.1080/03081089408818334. N. Kogan, A. Berman, Characterization of completely positive graphs, Discrete Mathematics 114 (1993), 297--304. DOI: 10.1016/0012-365X(93)90374-3. F. Barioli, Decreasing diagonal elements in completely positive matrices, Rendiconti del Seminario Matematico della Università di Padova 100 (1998), 13--25. Numdam identifier: RSMUP_1998\_\_100_13_0. N. Shaked-Monderer, Corrigendum to "SPN graphs: when copositive = SPN", Linear Algebra and its Applications 541 (2018), 285--286; arXiv:1712.05115. N. Shaked-Monderer, CP graphs and SPN graphs, Communications in Optimization Theory 2025 (2025), Article 3, 1--10. DOI: 10.23952/cot.2025.3. H. Singh, Exponential local pivot complexity for ordinary completely positive separation, research manuscript, 15 November 2026. Immutable project source: Harman6139/Posterity-Files, commit 11ffd7fe0e83b7eda47459d1d9b90b7358a4fcfc. Original proof and tests retained unchanged in the accompanying release.
:::
