---
abstract: |
  For each fixed order $n\ge5$ we construct strictly entrywise-positive,
  positive-definite rational matrices outside the ordinary completely
  positive cone on which every strictly descending adjacent-vertex rule,
  initialized at the canonical tridiagonal perfect form, requires
  exponentially many pivots in the binary input-and-distance parameter.
  The lower bound holds on an explicit Frobenius ball and does not
  require uniqueness of the improving ray. A dimension-independent bound
  of $5/2$ on the movement of each cross-column coordinate along a
  bounded edge of a fixed-positive-definite-block Ryshkov face replaces
  trajectory-specific analysis. An arithmetic gap and a cofactor height
  bound prevent every improving extreme ray from leaving that face
  during the entire prefix. No scalar identity correction of any
  improving ray separates the inputs there. In contrast, a strictly
  copositive rational separator with logarithmic coordinate height is
  explicit. The proof is for ordinary $\mathcal{CP}_n$, without
  additional column restrictions, and uses the standard canonical
  initialization without preprocessing. The constants are conservative;
  historical first priority and external proof certification are not
  asserted.
author:
- Manuscript II research continuation
date: 15 November 2026
title: |
  Exponential local pivot complexity for ordinary completely positive
  separation\
  Every descending adjacent rule, canonical initialization, and robust
  positive inputs
---

# Model and main statement

The pairing is $\langle A,P\rangle=\operatorname{tr}(AP)$. Set
$$\mathcal{CP}_n=\operatorname{cone}\{xx^{\mathsf T}:x\in\mathbb R_+^n\},\qquad
 \mathcal{COP}_n=\{P:P[x]\ge0\text{ for }x\ge0\},$$ where
$P[x]=x^{\mathsf T}Px$, and
$$\mathcal R_n=\{P\in\mathbb S^n:P[v]\ge1\text{ for all }0\ne v\in\mathbb Z_+^n\}.$$
Let $T_j$ have diagonal one, adjacent entries $-1/2$, and all other
entries zero. A local rule in this paper starts at $T_n$, chooses any
extreme tangent ray $R$ with $\langle A,R\rangle<0$, and moves to the
adjacent vertex if the ray is bounded. The standard certificate exits
are $\langle A,P\rangle<0$ at the current vertex or
$R\in\mathcal{COP}_n$. We additionally allow testing $R+\tau I$ for
arbitrary real $\tau$. No computational restriction is imposed on
choosing among the improving rays; in particular the choice may be
randomized, history dependent, or informed by the entire input.

This is the adjacent-pivot model of Procedure 3 in [@DSV], augmented by
the stated identity correction. An unrelated separator, an
input-dependent starting vertex, nonadjacent jumps, or a non-descending
move is outside the model. The existence of a short global separator is
compatible with the lower bound precisely because it is a nonlocal
bypass.

For $n\ge5$, $m\ge1$, define $$\label{eq:params}
 \begin{split}
 r&=n-1,\qquad d=n(n+1)/2,\qquad q=2n,\qquad Y=2q^r,\\
 U&=2Yn^2(m+1),\qquad E=(d-1)![2U^2]^{d-1},\\
 N&=20000n^3E^2,\qquad \epsilon=\frac1{100n^3},\qquad
 \rho=\frac1{1600n^4N^2}.
 \end{split}$$ Let $G$ be the adjacency matrix of the five-cycle on the
ordered coordinates $(1,2,3,4,n)$, zero elsewhere, and put
$$\label{eq:targets}
 \begin{split}
 F&=I_n+\frac35G,\qquad D=\operatorname{diag}(1,8/5,8/5,1,\ldots,1),\\
 C_{ij}&=\min(i,j)(n+1-\max(i,j)),\\
 B&=DFD+\epsilon C,\qquad S_N=\operatorname{diag}(N,\ldots,N,1),\\
 B_N&=S_NBS_N,\qquad A_N=\frac{B_N}{4nN^2}.
 \end{split}$$ All objects in these formulas are explicit and rational.

::: {#thm:main .theorem}
**Theorem 1** (Canonical, ordinary-cone, all-rule lower bound). *For
every $n\ge5$, $m\ge1$, and every symmetric $A$ satisfying
$$\label{eq:ball}\lVert A-A_N\rVert_F\le\rho,$$ the following statements
hold.*

1.  *$\lVert A\rVert_F\le1$, $A\succ0$, every entry of $A$ is positive,
    and $A\notin\mathcal{CP}_n$.*

2.  *Every local rule in the model above makes at least $m$
    adjacent-vertex pivots from $T_n$. During these pivots an improving
    extreme ray always exists, every such ray is bounded, and neither
    standard certificate exit applies.*

3.  *At every departure vertex in this prefix and for every improving
    extreme ray $R$, no real $\tau$ makes $R+\tau I$ a copositive
    separator of $A$.*

4.  *One explicit rational $W_N$ separates the entire ball and satisfies
    $$W_N[x]\ge\frac{\lVert x\rVert_2^2}{20nN^2}\quad(x\ge0),\qquad
     \lVert W_N\rVert_F\le6,\qquad
     \langle W_N,A\rangle\le-\frac1{6nN^2}.$$ Consequently
    $\operatorname{dist}_F(A,\mathcal{CP}_n)\ge1/(36nN^2)$.*

*For each fixed $n$, the rational centers have total input length
$O_n(\log(m+1))$ and $W_N$ has coordinate bit height $O_n(\log(m+1))$.
If $L_m$ is the center's total rational encoding length and
$$H_m=L_m+\left\lceil\log_2\frac1{\operatorname{dist}_F(A_N,\mathcal{CP}_n)}\right\rceil+2,$$
then $H_m=\Theta_n(\log(m+1))$. Thus the required number of pivots is
$2^{\Omega_n(H_m)}$.*
:::

The bit-length assertion is for the explicit centers. Rational
perturbations may have arbitrarily long encodings, even inside a small
ball. The theorem does not assert that every rule eventually terminates;
it asserts an unavoidable finite prefix before any of the allowed exits.
It also does not assert a unique path. All possible improving choices
are covered.

# A bounded-movement theorem for fixed positive-definite blocks

This section supplies the geometric ingredient independently of the
constructed objective.

Let $H\in\mathbb S^r$ be positive definite. Consider the epigraph
defined by $$\label{eq:g}
 g_H(b)=\sup_{u\in\mathbb Z_+^r,\ y\in\mathbb Z_{\ge1}}
 \frac{1-u^{\mathsf T}Hu-2y b^{\mathsf T}u}{y^2},\qquad
 \mathcal E_H=\{(b,c):c\ge g_H(b)\}.$$ Fix any integer $q\ge2$ with
$\lVert H\rVert_2r/q^2\le1/2$ and let
$$\kappa=\frac1{2q^{2r}},\qquad Y=2q^r.$$ For each $b$, let $z$ be the
unique minimizer of $x^{\mathsf T}Hx+2b^{\mathsf T}x$ on $\mathbb R_+^r$
and set $\ell=b+Hz$. The optimality conditions give $$\label{eq:kkt}
 z\ge0,\quad\ell\ge0,\quad z_i\ell_i=0.$$

::: {#lem:gap .lemma}
**Lemma 2** (Uniform transverse gap and active-height control). *For
every $b$, $$\label{eq:gap}
 z^{\mathsf T}Hz+\kappa\le g_H(b)\le z^{\mathsf T}Hz+1.$$ The supremum
is attained. At an active constraint $(u,y)$ on the graph of $g_H$, with
$e=u-yz$, $$\label{eq:active}
 y\le Y,\qquad e^{\mathsf T}He+2y\ell^{\mathsf T}u
 =1-y^2\bigl(g_H(b)-z^{\mathsf T}Hz\bigr)\le1.$$ The epigraph is locally
polyhedral. At each of its vertices, $0\le\ell_i\le1/2$ for every $i$.*
:::

::: proof
*Proof.* Completing the square gives $$\label{eq:complete}
 \frac{1-u^{\mathsf T}Hu-2yb^{\mathsf T}u}{y^2}
 =z^{\mathsf T}Hz+\frac{1-e^{\mathsf T}He-2y\ell^{\mathsf T}u}{y^2}.$$
Its last numerator is at most one, proving the upper bound. On the
positive support of $z$, simultaneous Dirichlet approximation supplies
$1\le y\le q^r$ and integers $u_i$ with $|u_i-yz_i|\le1/q$. Set $u_i=0$
on the other coordinates. Each approximating integer is nonnegative: a
negative integer would have error at least one. Moreover
$\ell^{\mathsf T}u=0$. Hence
$e^{\mathsf T}He\le\lVert H\rVert_2r/q^2\le1/2$, proving the lower
bound. If $z=0$, take $u=0,y=1$.

For completeness, the approximation follows by placing the $q^s+1$
points $\{kz_S\}$, $0\le k\le q^s$, in $q^s$ boxes of side $1/q$, where
$s$ is the positive-support size. Subtract two points in one box.

In [\[eq:complete\]](#eq:complete){reference-type="eqref"
reference="eq:complete"}, all denominators $y>Y$ give values strictly
below the lower bound in [\[eq:gap\]](#eq:gap){reference-type="eqref"
reference="eq:gap"}. For the remaining finitely many denominators, a
value at least $z^{\mathsf T}Hz+\kappa$ requires $u-yz$ in a fixed
ellipsoid. Thus only finitely many numerators matter; the supremum is
attained, and [\[eq:active\]](#eq:active){reference-type="eqref"
reference="eq:active"} follows. The same bounds on a neighborhood of $b$
prove local polyhedrality. Continuity of $z(b)$ follows, for example,
from strong convexity of the minimized quadratic.

At a vertex $c=g_H(b)$ and the active affine normals $(2u/y,1)$ span
$\mathbb R^{r+1}$. For each $i$, some active $u_i$ is therefore
positive. Equation [\[eq:active\]](#eq:active){reference-type="eqref"
reference="eq:active"} implies $2y\ell_i u_i\le1$, and hence
$\ell_i\le1/2$. ◻
:::

::: {#thm:movement .theorem}
**Theorem 3** (Bounded coordinate movement along every edge). *If
$(b,c)$ and $(b',c')$ are endpoints of a bounded edge of $\mathcal E_H$,
then $$\label{eq:movement}
 |b'_i-b_i|\le\frac12+2\sqrt{H_{ii}}\qquad(1\le i\le r).$$ For $H=T_r$
this is $\lVert b'-b\rVert_\infty\le5/2$, independently of dimension,
location, degeneracy, and edge choice.*
:::

::: proof
*Proof.* A bounded edge in a full-dimensional $(r+1)$-dimensional
locally polyhedral epigraph has a common active constraint $(u,y)$ at
its two endpoints (indeed at least $r$ independent common normals). At
either endpoint, $$b+H(u/y)=\ell+He/y.$$ Cauchy--Schwarz in the
$H$-inner product and [\[eq:active\]](#eq:active){reference-type="eqref"
reference="eq:active"} give $|(He)_i|\le\sqrt{H_{ii}}$. By
Lemma [2](#lem:gap){reference-type="ref" reference="lem:gap"}, the $i$th
coordinate lies in $$[-\sqrt{H_{ii}}/y,\ 1/2+\sqrt{H_{ii}}/y].$$ The
same $u,y$ occur at both endpoints. Taking the length of this interval
and using $y\ge1$ proves the assertion. ◻
:::

::: {#lem:recession .lemma}
**Lemma 4** (Recession directions). *The recession cone of
$\mathcal E_H$ is $\{(h,a):h\ge0,\ a\ge0\}$.*
:::

::: proof
*Proof.* A recession direction must satisfy $a+2h^{\mathsf T}u/y\ge0$
for all $u\in\mathbb Z_+^r,y\ge1$. Taking $u=0$ gives $a\ge0$, and
taking $u=ke_i,y=1$ with arbitrarily large $k$ gives $h_i\ge0$. These
conditions are also sufficient. ◻
:::

# The canonical face and arithmetic ray heights

The identity $$\label{eq:root}
 T_j[x]=\frac12\left(x_1^2+x_j^2+\sum_{i=1}^{j-1}(x_i-x_{i+1})^2\right)$$
shows that its nonnegative integer minimum is one, attained precisely at
the consecutive-interval indicators. Their rank-one matrices are
linearly independent: the diagonal entries are recovered from singleton
intervals and the off-diagonals from four-term interval differences.
Thus $T_j$ is a perfect vertex, with exactly $j(j+1)/2$ active normals.

Retain, at $T_n$, all interval equalities on the first $r=n-1$
coordinates. Their intersection with $\mathcal R_n$ is the face
$$\label{eq:face}
 \mathcal F=\left\{P(b,c)=\begin{pmatrix}T_r&b\\b^{\mathsf T}&c\end{pmatrix}: c\ge g_{T_r}(b)\right\}.$$
It has relative dimension $r+1$ and contains $T_n=P(-e_r/2,1)$. For
$T_r$, $\lVert T_r\rVert_2<2$, so the choices $q=2n$, $Y=2q^r$ in
[\[eq:params\]](#eq:params){reference-type="eqref"
reference="eq:params"} are valid in
Lemma [2](#lem:gap){reference-type="ref" reference="lem:gap"}.

Every point of this face is strictly copositive. Indeed, with $\ell,z$
as above and $a=c-z^{\mathsf T}T_rz\ge\kappa$,
$$P[(x,y)]=(x-yz)^{\mathsf T}T_r(x-yz)+2y\ell^{\mathsf T}x+ay^2>0$$ for
every nonzero $(x,y)\ge0$. Thus the full Ryshkov set is locally
polyhedral at every point of $\mathcal F$: a sufficiently small
neighborhood has a uniform positive copositivity margin, so only
finitely many integer vectors can define constraints there. Standard
local polyhedral edge and tangent-cone facts are consequently
applicable. This also proves that a nonrecession extreme tangent ray in
$\mathcal F$ reaches a genuine adjacent endpoint, rather than a
nonattained boundary infimum.

::: {#lem:heights .lemma}
**Lemma 5** (Heights in the first $m$ possible steps). *Any vertex of
$\mathcal F$ reachable from $T_n$ in at most $m$ bounded edges of
$\mathcal F$ satisfies $$\lVert b\rVert_\infty\le3(m+1),\quad
 \lVert z\rVert_\infty\le n^2(m+1),\quad
 0<c\le3n^5(m+1)^2,\quad
 \lVert P\rVert_F\le10n^5(m+1)^2.$$ Every active vector of the full
$\mathcal R_n$ at this vertex has coordinates at most $U$ from
[\[eq:params\]](#eq:params){reference-type="eqref"
reference="eq:params"}. Every extreme tangent ray has a primitive
integral generator $R$ with $$\label{eq:rayheight}
 |R_{ij}|\le E,\qquad \lVert R\rVert_F\le nE.$$*
:::

::: proof
*Proof.* The movement theorem gives
$\lVert b\rVert_\infty\le1/2+5m/2\le3(m+1)$. The inverse formula
$$(T_r^{-1})_{ij}=\frac{2\min(i,j)(n-\max(i,j))}{n}$$ gives row sums
$i(n-i)\le n^2/4$ and diagonal entries at most $n/2$. Since
$z=T_r^{-1}(\ell-b)$ and $0\le\ell_i\le1/2$, the displayed bound on $z$
follows. The upper bound on $g$ and $\lVert T_r\rVert_2<2$ give the
bounds on $c$ and $P$.

An active vector with last coordinate zero is a top interval indicator.
Otherwise write it $(u,y)$. Lemma [2](#lem:gap){reference-type="ref"
reference="lem:gap"} gives $y\le Y$ and
$$|u_i-yz_i|\le\sqrt{(T_r^{-1})_{ii}}\le\sqrt{n/2}.$$ Therefore
$u_i\le Yn^2(m+1)+\sqrt{n/2}\le U$.

In upper-triangular coordinates an active equation has integer
coefficients $v_i^2$ on the diagonal and $2v_iv_j$ off the diagonal, all
of magnitude at most $2U^2$. At a vertex the tangent cone is full
dimensional and pointed. Its extreme ray annihilates $d-1$ independent
active equations. The cofactor formula produces an integral generator
bounded by $(d-1)![2U^2]^{d-1}=E$. Dividing by a greatest common divisor
can only reduce this bound. No simplicity assumption is used. ◻
:::

# An ordinary completely positive obstruction compatible with the face

Write the fixed matrix $B$ in
[\[eq:targets\]](#eq:targets){reference-type="eqref"
reference="eq:targets"} as
$$B=\begin{pmatrix}B_0&c_0\\c_0^{\mathsf T}&a_0\end{pmatrix}.$$

::: {#lem:data .lemma}
**Lemma 6** (Fixed objective data). *The matrix $B$ is strictly
entrywise positive, $B\succ\frac1{40}I$, and $\lVert B\rVert_F\le3n$.
Every entry is at least $\epsilon$. Also
$$0<a_0<2,\qquad c_0>0,\qquad \sum_i(c_0)_i<2.$$ The leading block $B_0$
is a strictly positive combination of all rank-one top-interval normals,
with every coefficient at least $\epsilon$. All entries of $B$ have
common denominator $500n^3$, and $\langle B_0,T_r\rangle\ge1$. There is
a rational $W_0\in\mathcal{COP}_n$ with $\lVert W_0\rVert_F\le5$ and
$\langle W_0,B\rangle\le-19/20$.*
:::

::: proof
*Proof.* The smallest eigenvalue of the five-cycle block of $F$ is
$(7-3\sqrt5)/10>1/40$; the remaining eigenvalues outside the block are
one. Since the diagonal entries of $D$ are at least one,
$DFD\succ I/40$. The anchor $C$ is the sum of the squares of all
interval indicators. It is positive definite, every entry is at least
one, and $\lVert C\rVert_F\le\operatorname{tr}C=n(n+1)(n+2)/6\le n^3$.

The leading block of $DFD$ has the following interval decomposition. The
singleton weights on indices $1,2,3,4$ are respectively
$$1/25,\quad8/125,\quad8/125,\quad1/25,$$ the weights on
$[1,2],[2,3],[3,4]$ are $24/25,192/125,24/25$, and any other top
coordinate has singleton weight one. The leading block of $C$ gives
weight one to each top interval, plus one more to those ending at $r$.
This proves the exposure assertion. The base weights alone sum to
$r-42/125>1$.

Here $a_0=1+\epsilon n$, while $c_0$ has base values $3/5$ at indices
$1,4$ and zero elsewhere, plus $\epsilon i$ at index $i$. Thus its sum
is $6/5+\epsilon n(n-1)/2<2$. Every entry of $B$ is below three, proving
the norm bound. The denominator claim follows because $125$ and $100n^3$
both divide $500n^3$.

Let $H_5=J_5-2\operatorname{Adj}(C_5)$ be the Horn matrix. It is
copositive. To see this directly, maximize
$\sum_{\{i,j\}\in E(C_5)}x_ix_j$ on $x\ge0$, $\sum x_i=1$, choosing a
maximizer with smallest support. Two positive nonadjacent coordinates
can be merged into the one with larger neighbor sum without reducing the
objective, so the support is a clique. The cycle is triangle free, and
the maximum over a clique is at most $1/4$. Hence $H_5[x]\ge0$.

Embed $H_5$ on the ordered coordinates $(1,2,3,4,n)$, zero elsewhere,
and let $W_0=D^{-1}H_5D^{-1}$ (with this embedding understood). Then
$W_0\in\mathcal{COP}_n$, $\lVert W_0\rVert_F\le5$, and
$$\langle W_0,DFD\rangle=\langle H_5,I_5+(3/5)\operatorname{Adj}(C_5)\rangle=5-6=-1.$$
The anchor changes this pairing by at most
$\epsilon\lVert W_0\rVert_F\lVert C\rVert_F\le1/20$. ◻
:::

::: {#lem:separator .lemma}
**Lemma 7** (One strict separator for the whole perturbation ball).
*Define $$\label{eq:separator}
 W_N=S_N^{-1}W_0S_N^{-1}+\frac1{20nN^2}I.$$ Every $A$ in
[\[eq:ball\]](#eq:ball){reference-type="eqref" reference="eq:ball"} has
all the positivity, norm, separation, and distance properties in
Theorem [1](#thm:main){reference-type="ref" reference="thm:main"}.*
:::

::: proof
*Proof.* Positive diagonal congruence preserves ordinary complete
positivity and copositivity. The first term in
[\[eq:separator\]](#eq:separator){reference-type="eqref"
reference="eq:separator"} is copositive with norm at most five and
pairing with $B_N$ at most $-19/20$. Since
$\operatorname{tr}B_N\le3nN^2$, the identity addition increases that
pairing by at most $3/20$. Thus $$\langle W_N,B_N\rangle\le-4/5,\quad
 \langle W_N,A_N\rangle\le-1/(5nN^2),\quad \lVert W_N\rVert_F\le6.$$ The
positive identity coefficient is the stated cone margin.

We have $\lVert A_N\rVert_F\le3/4$, $\lambda_{\min}(A_N)>1/(160nN^2)$,
and every entry of $A_N$ is at least $\epsilon/(4nN^2)=4\rho$. These
facts survive the perturbation and give $\lVert A\rVert_F\le1$. The
pairing increases by at most $6\rho$, which leaves it at most
$-1/(6nN^2)$. Finally, for any $X\in\mathcal{CP}_n$,
$$\lVert A-X\rVert_F\ge\frac{-\langle W_N,A\rangle}{\lVert W_N\rVert_F}\ge\frac1{36nN^2}.$$ ◻
:::

# All improving choices remain in the canonical face

For an $A$ in the ball, multiply the objective by the positive factor
$4nN^2$ and write
$$\widetilde B=4nN^2A=B_N+Z,\qquad \lVert Z\rVert_F\le\epsilon/4.$$ This
scaling changes no improving direction.

::: {#lem:confinement .lemma}
**Lemma 8** (Arithmetic confinement). *At every vertex covered by
Lemma [5](#lem:heights){reference-type="ref" reference="lem:heights"},
every improving extreme tangent ray of the full $\mathcal R_n$ lies in
the tangent cone of $\mathcal F$. Every such improving ray is bounded
and has an adjacent endpoint in $\mathcal F$.*
:::

::: proof
*Proof.* Normalize a ray $R$ as in
[\[eq:rayheight\]](#eq:rayheight){reference-type="eqref"
reference="eq:rayheight"}. Define
$$h(R)=\langle B_0,R_{[r],[r]}\rangle.$$ Each top-interval vector is
active, so each of its quadratic values on $R$ is nonnegative.
Lemma [6](#lem:data){reference-type="ref" reference="lem:data"} gives
$h(R)\ge0$, with equality exactly when the top block of $R$ vanishes. If
$h(R)>0$, integrality and the common denominator yield
$h(R)\ge1/(500n^3)$. Hence $$\begin{aligned}
 \langle \widetilde B,R\rangle
 &\ge\frac{N^2}{500n^3}-(4N+2)E-\frac{nE\epsilon}{4}\\
 &\ge\frac{N^2}{500n^3}-7NE
 \ge\frac{N^2}{1000n^3}>0,
\end{aligned}$$ where the last step uses $N=20000n^3E^2$ and $E\ge1$.
Thus every improving ray has top block zero.

The hyperplane $h=0$ exposes the tangent face corresponding to
$\mathcal F$. Its rays are tangent rays of the epigraph
[\[eq:face\]](#eq:face){reference-type="eqref" reference="eq:face"}. The
recession directions there have nonnegative cross-column and bottom
entry by Lemma [4](#lem:recession){reference-type="ref"
reference="lem:recession"}. Since $\widetilde B$ has strictly positive
entries, none can be improving. Every improving extreme ray is therefore
bounded and reaches a neighboring vertex in $\mathcal F$. ◻
:::

::: {#lem:noexit .lemma}
**Lemma 9** (No vertex exit and no identity-corrected ray exit). *At
every vertex covered by Lemma [5](#lem:heights){reference-type="ref"
reference="lem:heights"}, $$\langle \widetilde B,P\rangle\ge N^2/4>0.$$
For every improving extreme ray there, no real $\tau$ makes $R+\tau I$ a
copositive separator of $A$.*
:::

::: proof
*Proof.* Put $M=m+1$ and $\alpha=\langle B_0,T_r\rangle\ge1$. Since
$c>0$ and $a_0>0$, $$\begin{aligned}
 \langle \widetilde B,P\rangle
 &\ge N^2-12NM-\frac\epsilon4\,10n^5M^2\\
 &=N^2-12NM-\frac{n^2M^2}{40}\ge N^2/4.
\end{aligned}$$ The parameter choice implies $N\ge24M$ and $N\ge nM$.

For the second claim use the primitive integral generator, which is
harmless under positive rescaling. By confinement,
$$R=\begin{pmatrix}0&w\\w^{\mathsf T}&s\end{pmatrix},\qquad |w_i|,|s|\le E.$$
Strict positivity of the objective implies that an improving $R$ has
$s<0$ or some $w_i<0$. Copositivity of $R+\tau I$ requires $\tau\ge0$.
If $s<0$, it requires $\tau\ge-s\ge1$. Otherwise, for a negative integer
$w_i$, its $(i,n)$ principal block requires
$$\tau(s+\tau)\ge w_i^2\ge1.$$ If $\tau<1$, then $s+\tau\le E+1\le2E$,
so in all cases $\tau\ge1/(2E)$. Also
$$\langle \widetilde B,R\rangle\ge-7NE,\qquad \operatorname{tr}\widetilde B\ge N^2.$$
It follows that $$\langle \widetilde B,R+\tau I\rangle
 \ge-7NE+\frac{N^2}{2E}>0,$$ since $N>14E^2$. Therefore a copositive
correction cannot separate. In particular the uncorrected improving ray
is not copositive. ◻
:::

::: proof
*Proof of Theorem [1](#thm:main){reference-type="ref"
reference="thm:main"}.* Lemma [7](#lem:separator){reference-type="ref"
reference="lem:separator"} proves the target and certificate assertions.
Starting at $T_n\in\mathcal F$, suppose fewer than $m$ pivots have
occurred. Every previous improving step remains in $\mathcal F$ by
confinement, so the movement theorem and
Lemma [5](#lem:heights){reference-type="ref" reference="lem:heights"}
apply to the current vertex. The objective cannot be in its minimizing
normal cone, because that cone is generated by nonnegative integer
rank-one matrices and is contained in $\mathcal{CP}_n$, whereas
$A\notin\mathcal{CP}_n$. Since the local tangent cone is polyhedral and
pointed, it has an improving extreme ray. Every possible such ray is
bounded and remains in $\mathcal F$, by
Lemma [8](#lem:confinement){reference-type="ref"
reference="lem:confinement"}. Neither allowed exit is possible, by
Lemma [9](#lem:noexit){reference-type="ref" reference="lem:noexit"}.
Induction therefore forces at least $m$ pivots, independently of all
choices.

For fixed $n$, [\[eq:params\]](#eq:params){reference-type="eqref"
reference="eq:params"} gives $$N=K_n(m+1)^{4(d-1)},\qquad
 K_n=20000n^3\bigl((d-1)!\bigr)^2(8Y^2n^4)^{2(d-1)}.$$ Every center
entry has denominator dividing $2000n^4N^2$ and magnitude at most one,
so $L_m=O_n(\log N)$. The distance lower bound bounds the
reciprocal-distance term by $O_n(\log N)$ as well. Conversely the
positive bottom entry is a fixed nonzero rational multiple of $N^{-2}$,
whose reduced denominator has bit length $\Omega_n(\log N)$. Thus
$H_m=\Theta_n(\log(m+1))$. The separator entries have logarithmic height
by [\[eq:separator\]](#eq:separator){reference-type="eqref"
reference="eq:separator"}. All its construction and verification
identities require only polynomially many fixed-dimensional rational
operations on these bit lengths. ◻
:::

# Interpretation, prior work, and reproducibility

The result is an ordinary-cone statement in every dimension where
positive definite, strictly positive nonmembers are possible. There is
no rectangular embedding of a constrained column cone, no noncanonical
shear start, no assumed shadow trajectory, and no uniqueness premise.
The fixed positive-definite-block face contains many possible
trajectories; the bounded-movement theorem controls them all.

The two mechanisms are separate but compatible. Rank-one exposing
normals and an integral objective gap confine all improving directions
to a face. The geometry of a uniformly positive quadratic epigraph
bounds the length of every edge in the remaining coordinates. Scaling
the fixed nonmember produces an exponentially long unavoidable residence
in that face. The same nonmember still has a directly available
Horn-based separator. Thus local traversal complexity is not
certificate-size complexity.

The simplex and neighboring-perfect-form framework is due to Dutour
Sikirić, Schürmann, and Vallentin [@DSV]. Their Conjecture 3.2 concerns
termination for a suitable pivot rule, not a polynomial pivot bound. The
present theorem neither refutes finite termination nor claims a
complexity lower bound for all separation algorithms.
Dannenberg--Schürmann [@DS] study the neighborhood graph and locally
finite polyhedral structure; the canonical root-lattice form and that
geometry are antecedents. Oertel--Schürmann [@OS] generalize
perfect-matrix theory and qualitative Interior Ryshkov results.
Dirichlet approximation, determinant bounds, the Horn separator, and
positive diagonal congruence are classical ingredients. The specific
asserted contribution is the bounded-coordinate-movement lemma and its
all-rule, canonical-start, ordinary-CP consequence.

The exact programs accompanying this paper verify the explicit
target/separator arithmetic, the top-interval decomposition, all finite
universal parameter inequalities used above, the canonical tangent rays,
and sampled branching prefixes of the fixed-block face. A separate
verifier imports no generator code and rejects deliberately corrupted
data. Tests are supplements to the universal proof; no long trajectory
is simulated. A proof over every pivot choice cannot be replaced by a
finite sampling of choices. No independent human review, formal
proof-assistant certification, exhaustive historical novelty
certificate, or journal-percentile claim is made.

::: thebibliography
9 M. Dutour Sikirić, A. Schürmann, and F. Vallentin, A simplex algorithm
for rational cp-factorization, *Mathematical Programming* **187**
(2021), 25--45. DOI: 10.1007/s10107-020-01467-4. arXiv:1807.01382v4. V.
Dannenberg and A. Schürmann, Perfect copositive matrices,
*Communications in Mathematics* **31** (2023), 137--156. DOI:
10.46298/cm.11141. arXiv:2303.17310v4. A. Oertel and A. Schürmann,
Generalized Perfect Matrices, arXiv:2602.05841v2 (2026).
:::
