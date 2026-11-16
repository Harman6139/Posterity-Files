# Introduction and the lifting principle

The ordinary completely positive and copositive cones are
$$\mathcal{CP}_n=\operatorname{cone}\{xx^{\mathsf T}:x\ge0\},\qquad
 \mathcal{COP}_n=\{P:x^{\mathsf T}Px\ge0\ (x\ge0)\}.$$ Their pairing is
$\langle A,P\rangle=\operatorname{tr}(AP)$. Let
$$\mathcal R_n=\{P:P[v]\ge1\text{ for }0\ne v\in\mathbb Z_+^n\},\qquad P[v]=v^{\mathsf T}Pv.$$
A vertex is a perfect copositive form. Its finitely many active vectors
generate its minimizing normal cone. These objects underlie the simplex
algorithm of Dutour Sikirić--Schürmann--Vallentin [@DSV]; their geometry
is developed in [@DS; @OS]. We study the local model that chooses an
arbitrary extreme tangent ray of strictly negative objective cost and
traverses its bounded edge. We do not restrict the computation used to
choose the ray.

The preceding version of this manuscript treated a specific five-cycle
seed from the canonical tridiagonal vertex. It used bounded edge
movement and location-dependent cofactor estimates. Here the main object
is instead the entire fixed-block face. Its finite local models yield a
stronger scale bound, a criterion for arbitrary seeds, and an
independent graph-growth theorem. Odd cycles are applications of the
criterion, not assumptions of it.

Put $r=n-1$, $d=n(n+1)/2$. Fix a rational positive-definite perfect form
$H\in\mathcal R_r$, and define
$$\mathcal M_H=\{v\in\mathbb Z_+^r:H[v]=1\},\qquad
 \mathcal V_H=\operatorname{cone}\{vv^{\mathsf T}:v\in\mathcal M_H\}.$$
The set $\mathcal M_H$ is finite and its squares span $\mathbb S^r$. The
face obtained by keeping these equalities in order $n$ is
$$\label{eq:face}
 \mathcal F_H=\left\{P(b,c)=\begin{pmatrix}H&b\\b^{\mathsf T}&c\end{pmatrix}\in\mathcal R_n\right\}.$$
It is nonempty and has dimension $r+1$;
Section [2](#sec:geometry){reference-type="ref"
reference="sec:geometry"} proves the needed local properties.

::: {#def:seed .definition}
**Definition 1** (Qualifying seed). A qualifying seed for $H$ is a
rational matrix
$$B=\begin{pmatrix}B_0&a\\a^{\mathsf T}&\alpha\end{pmatrix}$$ which is
positive definite, strictly entrywise positive, outside
$\mathcal{CP}_n$, and satisfies $B_0\in\operatorname{int}\mathcal V_H$.
:::

This is a finite verifiable criterion in each fixed dimension. Positive
definiteness is an exact rational test. Strict exposure is a finite LP:
require a representation of $B_0$ with positive coefficients on every
vector in $\mathcal M_H$. Nonmembership can be supplied with a rational
$W\in\mathcal{COP}_n$ and $\langle W,B\rangle<0$. Copositivity of a
rational seed witness can be checked by minimizing on all simplex
supports; no variable-dimensional polynomial claim is made. The
criterion does not require a five-cycle witness.

Here are explicit constants for the main theorem. Choose an integer
$q_0\ge2$ with $q_0^2\ge2r\lVert H\rVert_2$, and rational upper bounds
$$A_H\ge\max_i\sqrt{(H^{-1})_{ii}},\quad
 L_H\ge\max_i(1/2+2\sqrt{H_{ii}}).$$ Set $$\label{eq:constants}
 \begin{split}
 Y&=2q_0^r,\\
 M_H&=\left\lceil\max\{1,Y+A_H,\max_{v\in\mathcal M_H}\lVert v\rVert_\infty\}\right\rceil,\\
 F_H&=(d-1)![2M_H^2]^{d-1},\\
 K_H&=\lVert H^{-1}\rVert_\infty.
 \end{split}$$ The matrix norm in $K_H$ is the maximum absolute row sum.
Let $q_B$ be a positive integer clearing the denominators of $B_0$, and
let $R_0$ bound $\lVert b\rVert_\infty$ at every permitted initial
vertex. Put $$\label{eq:scale}
 \begin{split}
 T_B&=2\lVert a\rVert_1+\alpha+n+1,\\
 s_m&=1+rK_H(R_0+mL_H+1/2),\\
 N_m&=\left\lceil8q_BF_HT_Bs_m\right\rceil,\\
 S_N&=\operatorname{diag}(NI_r,1).
 \end{split}$$ In particular $N_m=\Theta_{H,B,R_0}(m+1)$.

For robustness, fix rational data
$$B\succeq\mu I,\quad b_*\le\min_{i,j}B_{ij},\quad
 W\in\mathcal{COP}_n,\quad\langle W,B\rangle\le-\gamma,\quad\lVert W\rVert_F\le\omega,$$
where $\mu,b_*,\gamma>0$. Let $\beta\ge\max(1,\lVert B\rVert_F)$ be
rational, and define $$\label{eq:robust}
 t_B=\frac\gamma{4\operatorname{tr}B},\quad w_B=\omega+t_B,\quad
 \eta=\min\{1,\mu/2,b_*/2,\gamma/(4w_B)\},\quad
 A_N=\frac{S_NBS_N}{2\beta N^2}.$$ Shrinking $\eta$ is always allowed.

::: {#thm:main .theorem}
**Theorem 2** (Normal-cone lifting; all local choices). *Let $H,B$
satisfy Definition [1](#def:seed){reference-type="ref"
reference="def:seed"}, and let the initial vertex be any vertex of
$\mathcal F_H$ with $\lVert b\rVert_\infty\le R_0$. For every $m\ge1$,
$N\ge N_m$, and symmetric $A$ with $$\label{eq:ball}
 \lVert A-A_N\rVert_F\le\frac\eta{2\beta N^2},$$ the following hold.*

1.  *$A$ is positive definite, strictly entrywise positive, has norm at
    most one, and is not completely positive.*

2.  *Every strictly improving extreme-ray adjacent rule makes at least
    $m$ pivots. Throughout this prefix every improving ray is tangent to
    $\mathcal F_H$ and bounded; an improving ray exists at each
    departure vertex.*

3.  *No copositive matrix whose leading $r\times r$ principal block is
    PSD separates $A$. This excludes arbitrary PSD corrections, hence
    arbitrary nonnegative diagonal corrections, of any visited improving
    ray. It also excludes history-based certificates
    $$\sum_j\lambda_jP_j+\sum_k\theta_kR_k+Q,
     \qquad \sum_j\lambda_j\ge0,\quad\theta_k\in\mathbb R,\quad Q\succeq0,$$
    whenever they are copositive. The $P_j$ may come from different runs
    on the same face.*

4.  *The rational matrix $$W_N=S_N^{-1}WS_N^{-1}+\frac{t_B}{N^2}I$$
    works for the whole ball, with
    $$W_N[x]\ge\frac{t_B}{N^2}\lVert x\rVert_2^2\ (x\ge0),\quad
     \lVert W_N\rVert_F\le w_B,\quad
     \langle W_N,A\rangle\le-\frac\gamma{4\beta N^2}.$$ In particular
    the distance from $A$ to $\mathcal{CP}_n$ is at least
    $\gamma/(4\beta w_BN^2)$.*

*For fixed seed and block, the centers $A_{N_m}$ have binary
input-and-distance precision $\Theta(\log(m+1))$, while the forced path
has length at least $m$. Each step inside the face, including the full
active set, tangent rays, and the selected neighbor, can be computed in
polynomial bit time in fixed dimension. A fixed finite menu of starts,
parallel runs, and restarts within the stated initial region do not
remove the required prefix on any successful run.*
:::

The number of starts need not be fixed in the assertion about the
region; there are only finitely many vertices in that region. The
theorem does not cover menus using different leading blocks, nonextreme
descent directions, or unrestricted nonlocal separator searches. Its
explicit separator is a global bypass. The robust encoding bound
concerns the rational centers, not arbitrary rational perturbations.

# Finite local models for a fixed quadratic block {#sec:geometry}

The geometric statements in this section require only $H\succ0$, not
perfection or an objective. Define
$$g_H(b)=\sup_{u\in\mathbb Z_+^r,\ y\in\mathbb Z_{\ge1}}
 \frac{1-u^{\mathsf T}Hu-2yb^{\mathsf T}u}{y^2},\qquad
 \mathcal E_H=\{(b,c):c\ge g_H(b)\}.$$ Let $z$ minimize
$x^{\mathsf T}Hx+2b^{\mathsf T}x$ over $x\ge0$, and write $\ell=b+Hz$.
Strong convexity gives a unique minimizer and $$\label{eq:kkt}
 z,\ell\ge0,\qquad z_i\ell_i=0.$$ Take $q_0,Y,A_H$ as above and
$\kappa=(2q_0^{2r})^{-1}$.

::: {#lem:gap .lemma}
**Lemma 3** (Transverse gap, active denominators, and edge movement).
*The supremum defining $g_H$ is attained and
$$z^{\mathsf T}Hz+\kappa\le g_H(b)\le z^{\mathsf T}Hz+1.$$ At an active
vector $(u,y)$, writing $e=u-yz$, one has $$\label{eq:active}
 y\le Y,\qquad e^{\mathsf T}He+2y\ell^{\mathsf T}u
 =1-y^2(g_H(b)-z^{\mathsf T}Hz)\le1,\qquad |e_i|\le A_H.$$ The epigraph
is locally polyhedral. At a vertex, $0\le\ell_i\le1/2$ for every $i$.
Along every bounded edge, $$\label{eq:movement}
 |b_i-b_i'|\le1/2+2\sqrt{H_{ii}}.$$ Its recession cone is
$\{(w,s):w\ge0,\ s\ge0\}$.*
:::

::: proof
*Proof.* Completing the square gives
$$\frac{1-H[u]-2yb^{\mathsf T}u}{y^2}
 =H[z]+\frac{1-H[e]-2y\ell^{\mathsf T}u}{y^2}.$$ This proves the upper
bound. On the positive support of $z$, put the $q_0^s+1$ fractional
vectors $jz$, $0\le j\le q_0^s$, into $q_0^s$ cubes of side $1/q_0$.
Subtract two in the same cube. This gives $1\le y\le q_0^r$ and integers
$u_i$ with $|u_i-yz_i|\le1/q_0$ on that support. The approximants are
nonnegative; set the other coordinates to zero. Thus
$\ell^{\mathsf T}u=0$ and $H[e]\le1/2$. If $z=0$, use $u=0,y=1$. This
proves the lower bound. Denominators larger than $Y$ cannot attain the
maximum. The finitely many remaining denominators have possible
maximizing numerators in a bounded ellipsoid around $yz$. This proves
attainment, [\[eq:active\]](#eq:active){reference-type="eqref"
reference="eq:active"}, and local polyhedrality; the minimizer $z(b)$ is
continuous by strong convexity.

At a vertex the active normals $(2u/y,1)$ span $\mathbb R^{r+1}$. For
each coordinate $i$, an active $u_i$ is positive; otherwise its
cross-column variable is unconstrained in the active system.
Equation [\[eq:active\]](#eq:active){reference-type="eqref"
reference="eq:active"} yields $2y\ell_i u_i\le1$ and hence
$\ell_i\le1/2$.

Endpoints of a bounded edge share an active $(u,y)$. At either endpoint,
$$b+Hu/y=\ell+He/y,$$ and $|(He)_i|\le\sqrt{H_{ii}}$ by Cauchy--Schwarz
in the $H$-metric. Both values of the left side lie in the same interval
$[-\sqrt{H_{ii}}/y,\,1/2+\sqrt{H_{ii}}/y]$. This proves
[\[eq:movement\]](#eq:movement){reference-type="eqref"
reference="eq:movement"}. Finally a recession direction satisfies
$s+2w^{\mathsf T}u/y\ge0$ for all $u,y$. Taking $u=0$, and then
$u=je_i,y=1$ with $j\to\infty$, proves the asserted signs; they are
sufficient. ◻
:::

For an integer vector $k$, define the shear $$\label{eq:shear}
 \mathsf S_k(b,c)=(b-Hk,\ c-2k^{\mathsf T}b+k^{\mathsf T}Hk),\qquad
 U_k=\begin{pmatrix}I_r&-k\\0&1\end{pmatrix}.$$ It acts on matrices by
$P\mapsto U_k^{\mathsf T}PU_k$. It need not preserve the whole orthant
Ryshkov set. We use it to normalize local data, not as an unqualified
symmetry.

::: {#thm:templates .theorem}
**Theorem 4** (Finite-template theorem). *Fix $H\succ0$. Every vertex
$(b,c)$ of $\mathcal E_H$ can be written
$$(b,c)=\mathsf S_k(\bar b,\bar c),\qquad k\in\mathbb Z_+^r,$$ where
$(\bar b,\bar c)$ belongs to a finite set depending only on $H$. After
this shear every active vector has integer coordinates bounded in
absolute value by $Y+A_H$ and has last coordinate in $\{1,\ldots,Y\}$.
The graph of bounded edges has uniformly bounded degree. If $H$ is
rational, all vertices have a common bounded denominator.*

*If additionally $H$ is perfect in $\mathcal R_r$, the *full* tangent
cones of $\mathcal R_n$ at vertices of $\mathcal F_H$ have finitely many
local models under these integral shears. Each primitive integral
extreme tangent ray has the form $$\label{eq:raymodel}
 R=U_k^{\mathsf T}\bar R U_k,\qquad
 \bar R=\begin{pmatrix}X&w\\w^{\mathsf T}&s\end{pmatrix},\qquad
 |\bar R_{ij}|\le F_H.$$ Consequently, with
$v_k=1+r\lVert k\rVert_\infty$, $$\label{eq:raybounds}
 |X_{ij}|\le F_H,\quad |R_{in}|\le F_Hv_k,\quad
 |R_{nn}|\le F_Hv_k^2,\quad \lVert R\rVert_F\le nF_Hv_k^2.$$ In
particular the number of active vectors and the number of competing rays
are bounded independently of position on the face.*
:::

::: proof
*Proof.* At a vertex put $k_i=\lfloor z_i\rfloor$ and
$\bar z=z-k\in[0,1)^r$. Set
$$\bar b=b+Hk,\qquad \bar c=c+2k^{\mathsf T}b+k^{\mathsf T}Hk.$$
Complementarity gives $k^{\mathsf T}\ell=0$, so
$$\bar b=\ell-H\bar z,\qquad
 \bar c=H[\bar z]+c-H[z].$$ These coordinates lie in a fixed compact
set. An active vector transforms to $(\bar u,y)=(u-yk,y)$, and
$|\bar u_i|\le y+A_H\le Y+A_H$. There are finitely many such integer
vectors. At a vertex $r+1$ independent active affine equations determine
$\bar b,\bar c$; therefore only finitely many normalized points occur.
Some of them need not be feasible orthant vertices before the shear,
which does not affect the conclusion. Local tangent cones are specified
by subsets of this finite list, giving a uniform degree bound. For
rational $H$, the finitely many normalized solutions are rational, and
integral shears preserve a common denominator.

For a full matrix vertex, include the fixed active vectors $(v,0)$,
$v\in\mathcal M_H$. This finite set together with the transformed
positive-last-coordinate vectors lies in the box of radius $M_H$ from
[\[eq:constants\]](#eq:constants){reference-type="eqref"
reference="eq:constants"}. The transformed tangent cone is full
dimensional and pointed. An extreme ray annihilates $d-1$ independent
rank-one equations whose integer coefficients are bounded by $2M_H^2$.
Cofactors yield a primitive integral representative bounded by $F_H$.
Congruence by the integral unimodular $U_k$ and its integral inverse
preserves primitivity. Expanding the blocks of
$U_k^{\mathsf T}\bar R U_k$ proves
[\[eq:raybounds\]](#eq:raybounds){reference-type="eqref"
reference="eq:raybounds"}. ◻
:::

For clarity about the face used above, the active equations of $H$ force
the leading block in [\[eq:face\]](#eq:face){reference-type="eqref"
reference="eq:face"} to equal $H$, and the remaining inequalities give
exactly $\mathcal E_H$. Every point of this face is strictly copositive:
for $a=c-H[z]\ge\kappa$,
$$P[(x,y)]=H[x-yz]+2y\ell^{\mathsf T}x+ay^2>0\quad(0\ne(x,y)\ge0).$$ A
neighborhood therefore has a common strict margin; only finitely many
integer constraints matter there. Vertices and edges of the face are
genuine vertices and edges of the full Ryshkov set. Finite edge
endpoints cannot disappear into a nonattained boundary.

::: {#cor:localcost .corollary}
**Corollary 5** (Cheap complete local information). *For fixed rational
$H$, the complete active set, full tangent rays at a vertex of
$\mathcal F_H$, and the neighbor along any bounded face edge can be
computed in polynomial bit time in the encoding of the vertex and ray.
The counts of lattice tests and linear systems depend on $H,n$, not on
the vertex height.*
:::

::: proof
*Proof.* Find $z$ by solving the $2^r$ possible support systems of the
positive-definite quadratic program and checking
[\[eq:kkt\]](#eq:kkt){reference-type="eqref" reference="eq:kkt"}. This
uses rational arithmetic. Compute $k=\lfloor z\rfloor$ and enumerate the
finite normalized box of
Theorem [4](#thm:templates){reference-type="ref"
reference="thm:templates"}, retaining $(\bar u+yk,y)\ge0$ and testing
equality. Enumerate the extreme rays from the finite active system. For
a bounded face neighbor,
[\[eq:movement\]](#eq:movement){reference-type="eqref"
reference="eq:movement"} and $z=H^{-1}(\ell-b)$ bound the change of $z$
by $K_H(L_H+1/2)$ in sup norm. Thus the endpoint's active numerators,
normalized by the *old* $k$, lie in another fixed box. Enumerate their
positive constraint ratios along the ray. The smallest is the exact edge
length because at least one newly active endpoint constraint is in this
list. All enumerations have fixed size; rational arithmetic has
polynomial bit cost. This is not a uniform polynomial bound when $H$ or
$n$ varies. ◻
:::

# From finite local models to long improving paths {#sec:lifting}

We first isolate the exact obstruction to the proposed stronger
certificate tests. This matrix decomposition is classical, not a new
theorem of this paper.

::: {#lem:spn .lemma}
**Lemma 6** (PSD principal block; Shaked-Monderer [@SM], Lemma 3.1). *If
$Z\in\mathcal{COP}_n$ and $Z_{[r],[r]}\succeq0$, then
$Z\in\mathcal{SPN}_n:=\mathbb S_+^n+\mathbb N^n$, where $\mathbb N^n$
denotes the symmetric entrywise nonnegative matrices. Hence
$\langle A,Z\rangle\ge0$ for every doubly nonnegative $A$.*
:::

::: proof
*Proof.* First let
$Z=\left(\begin{smallmatrix}G&b\\b^{\mathsf T}&c\end{smallmatrix}\right)$
with $G\succ0$. Minimize $x^{\mathsf T}Gx+2b^{\mathsf T}x$ on $x\ge0$,
with minimizer $z$ and residual $\ell=Gz+b\ge0$, $z^{\mathsf T}\ell=0$.
Copositivity at $(z,1)$ implies $c\ge z^{\mathsf T}Gz$. The
decomposition
$$Z=\begin{pmatrix}G&-Gz\\-z^{\mathsf T}G&z^{\mathsf T}Gz\end{pmatrix}
   +\begin{pmatrix}0&\ell\\\ell^{\mathsf T}&c-z^{\mathsf T}Gz\end{pmatrix}$$
is PSD plus nonnegative. For singular $G$, apply this result to
$Z+\varepsilon\operatorname{diag}(I_r,0)$ and let
$\varepsilon\downarrow0$. The SPN cone is closed: in a convergent
sequence $Z_j=P_j+N_j$, diagonal entries of $P_j\succeq0$ and $N_j\ge0$
are bounded; $|(P_j)_{ab}|\le\sqrt{(P_j)_{aa}(P_j)_{bb}}$ bounds $P_j$,
and then $N_j=Z_j-P_j$ is bounded. A convergent subsequence gives a
limiting decomposition. The pairing assertion follows from PSD and
entrywise nonnegative duality. ◻
:::

::: proof
*Proof of Theorem [2](#thm:main){reference-type="ref"
reference="thm:main"}.* Write $A=(B_N+Z)/(2\beta N^2)$, where
$B_N=S_NBS_N$ and $\lVert Z\rVert_F\le\eta$. Since $N\ge1$,
$B_N\succeq\mu I$ and every entry is at least $b_*$. The choice of
$\eta$ preserves positive definiteness and strict entrywise positivity.
Also $\lVert A\rVert_F\le(\beta N^2+1)/(2\beta N^2)\le1$.

Positive diagonal congruence preserves copositivity. Thus $W_N$ has cone
margin $t_B/N^2$, norm at most $w_B$, and
$$\langle W_N,B_N\rangle\le-\gamma+\frac{t_B}{N^2}\operatorname{tr}(B_N)
 \le-3\gamma/4.$$ The perturbation contributes at most
$\eta w_B\le\gamma/4$. Division by $2\beta N^2$ gives the stated pairing
and distance. In particular every ball input is outside the ordinary CP
cone.

Suppose a vertex is reachable in at most $m$ bounded edges within
$\mathcal F_H$ from one of the allowed starts.
Lemma [3](#lem:gap){reference-type="ref" reference="lem:gap"} gives
$$\lVert b\rVert_\infty\le R_0+mL_H,\qquad
 \lVert k\rVert_\infty\le\lVert z\rVert_\infty
 \le K_H(R_0+mL_H+1/2),$$ so $v_k\le s_m$. For a primitive integral
extreme ray $R$, define $$h(R)=\langle B_0,R_{[r],[r]}\rangle.$$ All
leading active constraints of $H$ remain active. Since $B_0$ is a
positive combination of all their normals, $$\label{eq:exposure}
 h(R)\ge0,\qquad h(R)=0\ \Longleftrightarrow\ R_{[r],[r]}=0.$$ The
reverse implication in the equality uses that the active squares span
$\mathbb S^r$. If $h(R)>0$, integrality gives $h(R)\ge1/q_B$. Applying
the sharper block bounds
[\[eq:raybounds\]](#eq:raybounds){reference-type="eqref"
reference="eq:raybounds"}, $$\begin{split}
 \langle B_N+Z,R\rangle
 &\ge\frac{N^2}{q_B}
       -2N\lVert a\rVert_1F_Hs_m
       -(\alpha+\eta n)F_Hs_m^2\\
 &\ge\frac{N^2}{2q_B}>0.
 \end{split}$$ For the last inequality, $N\ge8q_BF_HT_Bs_m$,
$F_H,q_B\ge1$, $\eta\le1$, and $T_B\ge\lVert a\rVert_1,\alpha+n,1$ bound
the two subtracted fractions by $1/4$ and $1/64$ of $N^2/q_B$,
respectively. Thus every improving extreme ray has zero leading block.
The position-dependent quadratic growth of its last entry does not
require a quadratic scale $N$: it is dominated by the $N^2$ leading
exposure once $N$ is linear in the shear parameter.

There is an improving extreme ray at every departure vertex. Otherwise
$A$ belongs to the minimizing normal cone, a finite cone generated by
active nonnegative integer squares, and hence to $\mathcal{CP}_n$, a
contradiction. The tangent cone is full dimensional and pointed by local
polyhedrality and perfection. Its improving extreme ray has zero leading
block and is therefore tangent to the face. It cannot be a recession
direction: by Lemma [3](#lem:gap){reference-type="ref"
reference="lem:gap"}, those directions have nonnegative cross and bottom
entries, so the strictly entrywise positive objective has positive cost
on every nonzero such direction. A finite endpoint exists by closedness
and local polyhedrality throughout the face; it is the adjacent vertex.
Lemma [6](#lem:spn){reference-type="ref" reference="lem:spn"} prevents a
negative pairing at the current vertex, and also rules out every
copositive certificate with PSD leading block. This proves the induction
for all choices through $m$ pivots.

For the stated history certificate, its leading block is
$(\sum_j\lambda_j)H+Q_{[r],[r]}\succeq0$, because every visited ray has
zero leading block. Lemma [6](#lem:spn){reference-type="ref"
reference="lem:spn"} applies even if the procedure optimizes the
correction or the history coefficients using unrestricted computation.
Arbitrary nonnegative diagonal corrections are included; in fact
arbitrary PSD corrections are included. The argument does not merely
bound a particular correction formula.

All constants are fixed for a fixed block, seed, and starting region,
and $N_m=\Theta(m+1)$. Entries of $A_{N_m}$ and $W_{N_m}$ have
$O(\log(m+1))$ bits. The last diagonal of $A_{N_m}$ is a fixed positive
rational multiple of $N_m^{-2}$, giving the matching lower encoding
bound after reducing fractions. The distance estimate gives the same
upper bound on logarithmic inverse distance. The local-cost claim is
Corollary [5](#cor:localcost){reference-type="ref"
reference="cor:localcost"}. Restarting within the starting region
repeats an uncompleted prefix rather than shortening it; history
certificates of the displayed form remain blocked across runs. ◻
:::

::: remark
*Remark 7* (An abstract exposure lemma). The confinement argument is not
peculiar to matrix cones. On a rational locally polyhedral set, let a
face be exposed on its tangent cones by an integral functional $h$ with
gap $1/q$ on primitive extreme rays outside the face. If local models
yield transverse components bounded by $C(1+t)$ and $C(1+t)^2$ within
graph distance $t$, the objective $N^2h+N\ell+a$ excludes every escaping
improving extreme ray for $N\ge C'(1+t)$. The matrix theorem supplies
verifiable hypotheses, the finite local models, and certificate
exclusion for an important nonpolyhedral cone; it is not merely a formal
restatement of this elementary domination argument.
:::

# Qualifying seeds without a five-cycle obstruction {#sec:seeds}

The criterion in Definition [1](#def:seed){reference-type="ref"
reference="def:seed"} is open in the seed data. The following class
demonstrates that its scope is not restricted to rescaling or embedding
the original order-five example. For every odd order it produces a
nonmember all of whose proper principal submatrices are CP, even after
making the matrix dense.

Let $n\ge5$ be odd, let $G$ be the cycle on $(1,2,\ldots,n)$, and put
$$\label{eq:cycle}
 t=\frac12+\frac1{16n^2},\quad F=I_n+t\operatorname{Adj}(G),\quad
 M=I_{n-1}-t\operatorname{Adj}(P_{n-1}),\quad h=M^{-1}\mathbf1.$$ Here
$P_{n-1}$ is the path on the first $n-1$ coordinates. Define
$$D=\operatorname{diag}(h_1,\ldots,h_{n-1},1),\quad
 C_{ij}=\min(i,j)(n+1-\max(i,j)),\quad
 \varepsilon=\frac1{32n^5},\quad B=DFD+\varepsilon C.$$

::: {#thm:cycles .theorem}
**Theorem 8** (Arbitrarily large principal-minimal seeds). *The matrix
$B$ is a qualifying seed for the canonical $H=T_{n-1}$. Every proper
principal submatrix of $B$ belongs to the interior of its ordinary CP
cone. It has an explicit rational weighted nonnegative Gram
factorization. The normal-cone lifting theorem therefore gives canonical
all-rule exponential lower bounds in every odd order, while all proper
principal CP tests fail to detect nonmembership. By shrinking $\eta$ in
[\[eq:robust\]](#eq:robust){reference-type="eqref"
reference="eq:robust"} to at most $\varepsilon/8$, these properties
persist throughout the entire robustness ball of the lifted targets.*
:::

::: proof
*Proof.* The least eigenvalue of $F$ is $1-2t\cos(\pi/n)$. Using
$\cos(\pi/n)\le1-2/n^2$, obtained from the chord bound for $\sin$, gives
$$\lambda_{\min}(F)\ge\frac{15}{8n^2}+\frac1{4n^4}>\frac1{n^2}.$$ The
path matrix $M$ has the same least eigenvalue. Its inverse is
nonnegative by the convergent Neumann series, and $h\ge\mathbf1$ is
rational. In the leading block of $DFD$, the adjacent-pair interval
square on $(i,i+1)$ has weight $t h_i h_{i+1}$. The remaining singleton
coefficient is $$h_i^2-t h_i\sum_{j:\,|i-j|=1}h_j=h_i>0.$$ The canonical
anchor $C$ is the sum of all consecutive-interval squares. Its leading
block has coefficient at least one on every top-interval square. Thus
$B_0\in\operatorname{int}\mathcal V_{T_{n-1}}$, and every entry of $B$
is positive.

For any triangle-free graph, $Q=J-2\operatorname{Adj}(G)$ is copositive.
A self-contained Motzkin--Straus argument [@MS] is as follows: maximize
the edge sum on the nonnegative simplex and choose a maximizer of
minimum support. Nonadjacent positive coordinates can be merged into one
of them without decreasing the sum, so the support is a clique. It has
at most two vertices and the edge sum is at most $1/4$. Therefore
$Q[x]\ge0$. For the cycle, $$\langle Q,F\rangle=n(1-2t)=-\frac1{8n}.$$
Set $W=D^{-1}QD^{-1}$. Since $h_i\ge1$, $\lVert W\rVert_F\le n$ and
$\lVert C\rVert_F\le\operatorname{tr}C\le n^3$. Consequently
$$\langle W,B\rangle\le-\frac1{8n}+\varepsilon n^4=-\frac3{32n}.$$ This
proves nonmembership; one may use $\gamma=1/(16n)$, $\omega=n$, and
$\mu=1/n^2$ as rational certificate parameters.

Let $S$ be a proper set of coordinates. The induced graph is a disjoint
union of paths. Its comparison matrix $M_S=I-t\operatorname{Adj}(G[S])$
is positive definite, since its path components have spectral radius at
most $2\cos(\pi/n)$. Put $v=M_S^{-1}\mathbf1>0$. Then the following
rational weighted factorization is exact: $$\label{eq:properfactor}
 F[S]=\sum_{i\in S}\frac1{v_i}e_ie_i^{\mathsf T}
 +\sum_{\{i,j\}\in E(G[S])}t v_i v_j
       (e_i/v_i+e_j/v_j)(e_i/v_i+e_j/v_j)^{\mathsf T}.$$ Indeed the
off-diagonal entries are $t$, and the diagonal at $i$ is
$(1+t\sum_{j\sim i}v_j)/v_i=1$. Congruence by $D[S]$ gives factors of
$(DFD)[S]$. Adding the restricted interval-square factors of
$\varepsilon C[S]$ gives factors of $B[S]$.

Moreover, these anchor atoms contain every consecutive-interval
indicator in the induced ordering of $S$, with coefficient at least
$\varepsilon$. Their squares span $\mathbb S^{|S|}$. Thus the
factorization contains a positive reserve on a full rational basis and
$B[S]\in\operatorname{int}\mathcal{CP}_{|S|}$. For a perturbation $Z$
with $\lVert Z\rVert_F\le\varepsilon/8$, express $Z[S]$ in that interval
basis. If entries outside the index range are set to zero, the
coefficient of $[i,j]$ is $$Z_{ij}-Z_{i-1,j}-Z_{i,j+1}+Z_{i-1,j+1}.$$
Its magnitude is at most $4\lVert Z\rVert_F\le\varepsilon/2$, so the
positive reserve remains. For the lifted target use $S_N^{-1}ZS_N^{-1}$,
whose norm cannot exceed $\lVert Z\rVert_F$. Positive scaling and
diagonal congruence preserve complete positivity and its interior. This
proves the robust assertion for all proper subsets at once. ◻
:::

The obstruction in order $n\ge7$ is therefore not a hidden order-five
witness: every $5\times5$ principal submatrix, and even every
$(n-1)\times(n-1)$ principal submatrix, is CP. Any copositive separator
supported on a proper coordinate set has nonnegative pairing with the
target. The difficulty is intrinsically global at that order. This
remains a statement about *ordinary* complete positivity, with no
restrictions on Gram columns.

::: corollary
**Corollary 9** (Weighted cycle class). *Let $F$ be any rational
positive-definite nonnegative matrix supported on an odd cycle of order
$n\ge5$ and its diagonal. Suppose
$$\operatorname{tr}F<2\sum_{\{i,j\}\in E(G)}F_{ij}.$$ There is a
rational positive diagonal scaling of its first $n-1$ coordinates and an
arbitrarily small positive rational canonical-anchor addition that
produce a qualifying seed for $T_{n-1}$. All proper principal
submatrices remain CP, and after the anchor addition they are interior
CP. Thus the family includes a full range of nonuniform edge weights and
diagonal data, not just the uniform matrices in
[\[eq:cycle\]](#eq:cycle){reference-type="eqref" reference="eq:cycle"}.*
:::

::: proof
*Proof.* Deleting the last vertex leaves a path. The leading comparison
matrix, obtained by negating its off-diagonal entries, is diagonally
sign-congruent to the leading block of $F$, hence positive definite. Its
inverse is nonnegative: write it as $sI-N$ with $N\ge0$ and $s>\rho(N)$.
Take $h$ to be its inverse applied to $\mathbf1$. The same scaled
diagonal-dominance identity gives positive singleton and adjacent-pair
interval coefficients. The witness $J-2\operatorname{Adj}(G)$ pairs
negatively by the displayed condition. Preserve that strict gap with a
small anchor addition. Every proper principal graph is a forest; the
same comparison-matrix construction, with its original diagonal entries
in place of one, gives a weighted factorization as in
[\[eq:properfactor\]](#eq:properfactor){reference-type="eqref"
reference="eq:properfactor"}. The anchor supplies interiority. ◻
:::

For even order $n\ge6$, one may insert a positive diagonal padding block
immediately before the distinguished last coordinate of an odd-order
seed, and add a sufficiently small full canonical anchor. The old
leading path occupies consecutive coordinates, and the distinguished old
last coordinate remains last. The resulting leading block still has a
positive interval representation and the embedded seed witness still
separates. This recovers all fixed orders $n\ge5$. The stronger
assertion that *every* proper principal submatrix is CP is made for the
odd-order construction, not for such padded examples.

# An independent theorem on intrinsic graph geometry {#sec:graph}

Let $\mathscr G_H$ denote the graph whose vertices are the vertices of
$\mathcal E_H$ and whose edges are its bounded one-dimensional faces.
Distances below are intrinsic to this graph. They need not equal
distances in a larger Ryshkov graph that permits leaving the fixed-block
face.

::: {#thm:graph .theorem}
**Theorem 10** (Graph growth and lattice embedding). *For every real
$H\succ0$ of order $r$, the graph $\mathscr G_H$ is connected and has
uniformly bounded degree. For every vertex $v$, there are positive
constants $c_{H,v},C_{H,v}$ and $R_{H,v}$ such that
$$c_{H,v}R^r\le |B_{\mathscr G_H}(v,R)|\le C_{H,v}(R+1)^r
 \qquad(R\ge R_{H,v}).$$ It contains a quasi-isometrically embedded copy
of $\mathbb Z_+^r$: there are vertices $v_a$, $a\in\mathbb Z_+^r$, and
constants $c_H,C_H>0$ with
$$c_H\lVert a-b\rVert_\infty\le d_{\mathscr G_H}(v_a,v_b)
 \le C_H\lVert a-b\rVert_1.$$ When $H$ is rational, there are pairs of
vertices of $O_H(\log(N+1))$ binary encoding length at distance
$\Theta_H(N)$. Thus exponential graph distance in binary height is a
geometric phenomenon independent of a separating objective or any
five-cycle construction.*
:::

::: proof
*Proof.* Uniform degree follows from
Theorem [4](#thm:templates){reference-type="ref"
reference="thm:templates"}. The edge bound implies that a radius-$R$
graph ball about $(b_0,c_0)$ has
$\lVert b\rVert_\infty\le\lVert b_0\rVert_\infty+L_HR$. At every vertex,
$z=H^{-1}(\ell-b)$ and $\ell\in[0,1/2]^r$. Hence its shear index
$k=\lfloor z\rfloor$ ranges over $O_{H,v}((R+1)^r)$ possibilities. There
are only finitely many normalized templates, proving the upper bound.

We record connectivity carefully, since an infinite locally polyhedral
set cannot be treated as a finite polytope without justification. Every
graph vertex with $c\le C$ has $H[z]\le C-\kappa$, hence bounded $z$,
and then bounded $b=\ell-Hz$. The finite-template theorem implies that
there are only finitely many such vertices. Since the constraint
$(u,y)=(0,1)$ gives $c\ge1$, and every $b\ge0$ gives $g_H(b)=1$, the
minimum of $c$ is one. At a vertex with $c>1$ there is an extreme
tangent direction decreasing $c$; otherwise the vertex minimizes $c$
globally. It is not a recession direction, so it gives a bounded edge.
Strict descent through a finite set of vertices reaches the face $c=1$.

That face is a finite pointed polyhedron in the $b$ variables. Indeed,
whenever $g_H(b)=1$, the gap estimate bounds $z$; every constraint
active there has $y\le Y$ and $u=yz+e$ bounded. Thus only finitely many
inequalities can become active anywhere on the face. These inequalities
suffice globally: start at a strictly positive $b$, where every
nonzero-$u$ constraint is strict, and take a segment to any alleged
point satisfying the finite list but violating another constraint. At
the first exit, local polyhedrality supplies an active defining
constraint, which is one of the finite list, a contradiction. The
recession cone of the face is $\mathbb R_+^r$. A positive linear
objective has compact lower level sets on it, and after a generic
perturbation uniquely minimizes at a vertex. Every other vertex has a
bounded decreasing edge to that vertex, because the polyhedron has
finitely many vertices and recession costs are positive. This proves
connectivity of its vertex graph, and hence of $\mathscr G_H$.

For the lower bound we use an auxiliary unrestricted-integer epigraph
$$g_H^{\mathbb Z}(b)=\sup_{u\in\mathbb Z^r,\ y\ge1}\frac{1-H[u]-2yb^{\mathsf T}u}{y^2},
 \qquad \mathcal E_H^{\mathbb Z}=\{c\ge g_H^{\mathbb Z}(b)\}.$$ Here
$z=-H^{-1}b$, $\ell=0$, and the same gap, denominator and
finite-template proofs apply, now with $k\in\mathbb Z^r$. Every
$\mathsf S_k$ from [\[eq:shear\]](#eq:shear){reference-type="eqref"
reference="eq:shear"} is an actual symmetry, since $u\mapsto u+yk$
permutes the integer numerators. The recession cone consists only of
nonnegative vertical directions. The sublevel estimate
$g_H^{\mathbb Z}(b)\ge b^{\mathsf T}H^{-1}b+\kappa$ gives finitely many
vertices at each bounded height. The minimum-$c$ face is $c=1$ and is
bounded: the inequalities for $u=\pm e_i,y=1$ imply $|b_i|\le H_{ii}/2$.
It is a nonempty finite polytope, by the same finite-active-list
argument. Its graph is connected; descending $c$ proves that the entire
bounded-edge graph is connected as well.

Choose a vertex $p$ of this auxiliary graph and, for each $i$, a finite
edge path from $p$ to $\mathsf S_{e_i}p$. There are finitely many
vertices in these paths and finitely many active vectors at each. Choose
an integer $K\in\mathbb Z_+^r$ so large that $u+yK\ge0$ for all their
active vectors. The same is true after adding any $a\in\mathbb Z_+^r$ to
$K$. Each shifted vertex is a vertex of the orthant epigraph: it is
feasible there, and all its spanning auxiliary active constraints are
retained. Its orthant and unrestricted tangent cones coincide, because
the auxiliary active set is fully retained. Consequently every shifted
edge of each chosen path is also a bounded edge of $\mathcal E_H$. More
explicitly, at the first endpoint the direction remains an extreme ray,
and the same next endpoint retains the active constraint that prevents
extension.

Define $v_a=\mathsf S_{K+a}p$. Let $D$ be the largest length of the
finitely many chosen generator paths. Translating these paths and
reversing them when necessary gives
$$d_{\mathscr G_H}(v_a,v_b)\le D\lVert a-b\rVert_1.$$ One may change
coordinates one at a time through nonnegative lattice indices, so no
translated path requires a negative index. Their cross coordinates
differ by $H(a-b)$. Along any graph path,
[\[eq:movement\]](#eq:movement){reference-type="eqref"
reference="eq:movement"} gives $$d_{\mathscr G_H}(v_a,v_b)
 \ge\frac{\lVert H(a-b)\rVert_\infty}{L_H}
 \ge\frac{\lVert a-b\rVert_\infty}{K_HL_H}.$$ This proves the embedding
and supplies $\Omega_H(R^r)$ vertices within radius $R$ of $v_0$.
Connectivity transfers the growth bound to any root with an additive
distance shift.

For rational $H$, the auxiliary vertex $p$ is rational, being determined
by rational active equations. Its shear by $K+Ne_1$ has coordinates
polynomial of degree at most two in $N$ with fixed rational
coefficients. Its encoding is $O_H(\log(N+1))$, while the two distance
bounds give $\Theta_H(N)$. This proves the last assertion. ◻
:::

::: {#cor:grid .corollary}
**Corollary 11** (A complete elementary model). *For $H=I_2$, the graph
$\mathscr G_H$ is exactly the nearest-neighbor graph of $\mathbb Z_+^2$.
Its vertices are $$b_i=-k_i-\tfrac12,\qquad c=1+k_1(k_1+1)+k_2(k_2+1),
 \qquad(k_1,k_2)\in\mathbb Z_+^2.$$ The graph distance is $\ell^1$
distance and the ball of radius $R$ about $(k_1,k_2)=(0,0)$ has
$\binom{\lfloor R\rfloor+2}{2}$ vertices.*
:::

::: proof
*Proof.* Let $z_i=\max(0,-b_i)$. Rounding each positive $z_i$ to its
nearest nonnegative integer gives a denominator-one value at least
$\lVert z\rVert_2^2+1/2$. Every denominator $y\ge2$ gives at most
$\lVert z\rVert_2^2+1/4$ and is therefore inactive. Thus
$$g_{I_2}(b)=1+\sum_{i=1}^2\max_{u_i\in\mathbb Z_+}(-u_i^2-2b_i u_i).$$
A vertex requires a tie in each coordinate, since otherwise the active
affine normals fail to span $\mathbb R^3$. Ties occur exactly between
$k_i$ and $k_i+1$ at $b_i=-k_i-1/2$. To obtain a bounded edge one tie is
retained and the other moves between successive breakpoints. There are
no diagonal edges: changing both ties leaves only one common active
slope, which is insufficient for a one-dimensional face in three
dimensions. The outward edges at $k_i=0$ are unbounded and are excluded
from the graph. The distance and ball count follow. ◻
:::

The auxiliary unrestricted epigraph is related to classical
inhomogeneous quadratic forms and Delaunay geometry [@Erdahl; @IE]. The
assertions here include the positive-orthant truncation, all integer
last-coordinate denominators, bounded local models at boundary vertices,
and an intrinsic graph-growth conclusion. Periodicity of an unrestricted
denominator-one lattice diagram alone would not prove these assertions.

# Necessary restrictions, verification, and comparison {#sec:scope}

## What the assumptions do and do not assert

The strict normal-cone condition is sufficient for the lifting theorem;
we do not claim it is necessary for every form of local-search hardness.
It is essential to this confinement mechanism. If
$B_0\notin\mathcal V_H$, separation gives a leading tangent direction
$X$ with $\langle B_0,X\rangle<0$. At any fixed vertex of
$\mathcal F_H$, extend it to a full tangent direction by choosing its
bottom entry sufficiently large: all finitely many
positive-last-coordinate active inequalities can then be satisfied,
while the leading active inequalities already hold. Decomposing the
pointed tangent cone into its extreme rays, at least one ray has
negative leading cost. For large $N$, that fixed ray improves the scaled
objective and leaves the face.

Boundary exposure can also fail. At $T_3$, the direction
$$R_{12}=R_{21}=1/2,\qquad R_{13}=R_{31}=-1/2,$$ with all other entries
zero is an extreme tangent ray: among the six interval inequalities only
the interval $[1,2]$ has positive value. With
$B=I_3+(e_1e_3^{\mathsf T}+e_3e_1^{\mathsf T})/4$, the leading block
$I_2$ lies on the boundary of $\mathcal V_{T_2}$ and
$\langle S_NBS_N,R\rangle=-N/4<0$. This example diagnoses the exposure
condition; it is not claimed to be a nonmember lower-bound example.

Multiple starts sharing the leading block are covered in full. Arbitrary
menus of distinct leading perfect blocks are not covered. If
$H_1\ne H_2$ are distinct perfect vertices, the interiors of their
minimizing normal cones are disjoint: a functional in either interior
uniquely minimizes at its vertex. Thus one leading seed cannot satisfy
both strict exposure conditions. This is an obstruction to this proof
strategy, not a theorem that all diverse-start methods are efficient or
that no other hardness construction exists.

The extreme-ray restriction is also real. Adding a sufficiently small
positive multiple of an escaping feasible tangent direction to a
strictly improving face ray still gives a feasible improving direction,
but leaves the face. Consequently this proof does not cover arbitrary
nonextreme descent directions, nonlocal jumps, or input-dependent
initializations. Arbitrary global certificate generation is
intentionally outside the lower bound; $W_N$ is a short explicit global
separator.

Positive definiteness is needed for the independent geometric theorem.
For example $H=0$ gives $\mathcal E_H=\{b\ge0,c\ge1\}$, which has only
one vertex rather than polynomial graph growth of positive degree. All
algorithmic claims with fixed $H,n$ allow constants depending on both;
the template bounds can be very large and do not imply uniformly
practical computation in variable dimension.

## Relationship to prior work

The simplex model, perfect matrices, finite normal cones, and
qualitative Ryshkov geometry are antecedents [@DSV; @DS; @OS]. The
bounded-edge displacement estimate and the canonical five-cycle all-rule
construction were proved in the preceding project manuscript, and are
reproved here rather than relabeled as new. The strengthening is the
finite-template normalization and its sharper ray bounds, the seed-based
linear-scale lifting theorem, its stronger certificate exclusions,
higher-order principal-minimal applications, and the independent
graph-growth theorem.

The PSD-principal-block lemma is explicitly attributed to [@SM]; it is
not a new matrix decomposition. Odd-cycle obstructions and the
distinction between doubly nonnegative and completely positive matrices
are classical. The new odd-cycle conclusion couples these seeds to
all-choice canonical hardness and retains complete positivity of every
proper principal block, even on a specified neighborhood.
Motzkin--Straus supplies the classical graph witness; a self-contained
proof was given above. The unrestricted lattice geometry is related to
[@Erdahl; @IE]; our conclusions concern a different, orthant-truncated
rational epigraph and its full adjacency graph. The recent algorithmic
work [@Minimum] studies the copositive minimum rather than a lower bound
on adjacent traversal.

These comparisons isolate the proposed new assertions. They are not an
exhaustive first-priority certificate. A lack of an identical result in
the sources inspected is not a proof of historical novelty. The earlier
suitable-pivot finite-termination conjecture is not contradicted: an
exponentially long path may still terminate. We do not assert eventual
termination of every permitted local rule.

## Reproducibility and status

The supplement contains exact rational seed certificates, finite
normal-system checks, shear-template checks, proper-principal CP
factors, and the two-dimensional graph model. A separately written
verifier imports no generator code and rejects deliberately corrupted
certificates. The original canonical certificate suite is retained and
rerun without modifying its formulas. The verification report records
the actual case counts and file hashes; finite tests supplement, rather
than replace, the proofs.

No production high-dimensional polyhedral library, external human proof
review, or proof-assistant formalization is claimed. The user-reported
randomized ten-paper benchmark is not recalibrated in this mathematical
supplement: the sample and its complete comparison rubric were not
available in the retrieved research files. The revised contribution is
suitable for a fresh skeptical comparison, but the paper does not assert
a top-three rank or an editorial probability.

::: thebibliography
9 M. Dutour Sikirić, A. Schürmann, F. Vallentin, A simplex algorithm for
rational cp-factorization, Math. Program. 187 (2021), 25--45.
doi:10.1007/s10107-020-01467-4. V. Dannenberg, A. Schürmann, Perfect
copositive matrices, Commun. Math. 31 (2023), 137--156.
doi:10.46298/cm.11141. A. Oertel, A. Schürmann, Generalized Perfect
Matrices, arXiv:2602.05841v2 (2026). N. Shaked-Monderer, SPN graphs:
when copositive = SPN, Linear Algebra Appl. 509 (2016), 82--113.
doi:10.1016/j.laa.2016.07.018. Lemma 3.1; arXiv:1604.02172v3. T. S.
Motzkin, E. G. Straus, Maxima for graphs and a new proof of a theorem of
Turán, Canad. J. Math. 17 (1965), 533--540. doi:10.4153/CJM-1965-053-6.
R. M. Erdahl, A cone of inhomogeneous second-order polynomials, Discrete
Comput. Geom. 8 (1992), 387--416. doi:10.1007/BF02293055. M. Dutour
Sikirić, A. Schürmann, F. Vallentin, Inhomogeneous extreme forms, Ann.
Inst. Fourier 62 (2012), 2227--2255. doi:10.5802/aif.2748. A. Oertel, A.
Schürmann, On Computing the Copositive Minimum and its Representatives,
arXiv:2509.23696 (2025).
:::
