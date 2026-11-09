# Milestone 46 — a complete rank-two-avoidance obstruction to the entire balanced 2m-order positive companion family

Date: 2026-11-08. This milestone is a proved, exact linear-algebraic NO-GO for applying the successful balanced-complement compiler (Milestone 35) DIRECTLY to an arbitrary dense source measurement space. The theorem is generic for codimension s>2m−2. It does NOT contradict Milestone 35, which applies to sources ALREADY rank-one-generated, and does NOT exclude more general matrix-valued positive companions or many-to-one PSD shadows.

## Definitions

Fix m>=3 and let L<=S^m be a real linear measurement space containing I_m. Write s=codim L and ell=dim L=D_m−s where D_m=m(m+1)/2. Suppose

  L ∩ {H∈S^m: 0<rank H<=2} = empty.                (H2)

For positive scalars 0<alpha<=beta define the balanced positive companion
  J_(alpha,beta)(X)
     = (alpha X) direct-sum (beta trX I_m −alpha X) in S^(2m).

It is globally PSD-positive because for X>=0 the eigenvalues of X are bounded by trX; its positive principal-block left inverse is D_0(Y)=alpha^(−1)Y_(top m-by-m). The dual map on B=[A,C;C^T,D] is
  J*(B)=alpha(A−D)+beta tr(D) I_m.

Let W_J=(J*)^(−1)(L) be the exact compressed measurement space needed to represent the full original affine kernel under J. Since I in L,
  W_J={ [A,C;C^T,D] : A−D in L }
and
  dim W_J = D_(2m)−s =2m²+m−s.

## Theorem 1 — every admissible rank-one vector is a paired diagonal

Assume (H2). A nonzero rank-one projector vv^T, with v=(a,b)∈R^m direct-sum R^m, belongs to W_J IF AND ONLY IF b=a or b=−a, with a!=0.

Proof. The pullback is
  J*(vv^T)=alpha(aa^T−bb^T)+beta||b||²I.
Since I∈L and alpha>0, membership in L is equivalent to aa^T−bb^T∈L. The difference has rank <=2. By (H2), it must vanish: aa^T=bb^T. If nonzero, equality of real rank-one PSD projectors implies b=+a or b=−a. Conversely such pairs have pullback beta||a||² I∈L. QED.

## Theorem 2 — exact rank-one generated subspace and dimension gap

Under (H2), the span of ALL admissible rank-one projectors of W_J is EXACTLY
  R_J = { [S,T;T,S]:S,T∈S^m }.
Its dimension is
  dim R_J=2D_m=m(m+1).
Therefore
  codim_(W_J)(R_J)=dim W_J−dim R_J
                 =m²−s.                               (1)

Since s<=D_m−1 for a nonzero measurement space containing I, m²−s >= m²−D_m+1=m(m−1)/2+1>0. In particular W_J is NEVER rank-one generated when (H2) holds, regardless of alpha,beta.

Proof. For b=+a and b=−a,
  (a,±a)(a,±a)^T=[aa^T, ±aa^T; ±aa^T, aa^T].
Taking their sum and difference yields respectively diagonal common blocks [aa^T,0;0,aa^T] and symmetric off-diagonal blocks [0,aa^T;aa^T,0]. Since real rank-one aa^T span S^m, their real linear span equals R_J. The rank and codimension formulae follow directly. QED.

## Corollary 3 — not even an arbitrary rank-one POVM can encode the entire affine fibre via this lift

Let A:S^m→R^p have range A*=L, and choose b=A(I_m) so F_b has a strictly positive interior matrix. Suppose a family of rank-one PSD linear measurements on the compressed 2m-by-2m space is DATA-FAITHFUL for the positive embedding J_(alpha,beta), meaning that every individual measurement outcome is constant on J(F_b), and suppose the induced exact compressed PSD feasible fibre equals J(F_b).

Then such a family DOES NOT EXIST under (H2). In particular no two-basis dilation based exclusively on compressed rank-one projectors can give an exact positive-linear face-retract embedding through J_(alpha,beta), regardless of the number of ambient basis coordinates.

Proof. If a compressed rank-one measurement projector P has constant expectation over all J(I+epsilon K), K∈ker A=L^perp, for sufficiently small epsilon of both signs, then <J*P,K>=0 for all K, hence J*P∈L and P∈W_J. By Theorem 2, the entire measurement span is contained in R_J, a proper subspace of W_J. Consequently its kernel strictly contains W_J^perp=J(ker A). At J(I)>0, every nonzero extra kernel direction permits small positive/negative PSD perturbations with identical measurements but outside J(F_b), contradicting exact fibre equality. QED.

This is an obstruction to ALL admissible rank-one POVMs under this fixed positive lift, not only to two MASAs. In particular, adding an arbitrarily large Naimark ambient dimension alone does not repair the missing cross-block linear constraints; one must CHANGE the source positive lift or introduce nontrivial additional PSD auxiliary degrees of freedom.

## Theorem 4 — genericity of the obstruction

For m>=3 and codimension s satisfying
  2m−2 < s <=D_m−1,
condition (H2) holds on a nonempty Zariski-open dense set of real measurement spaces L containing I. This set contains rational L.

Proof. In the complex projective symmetric matrix space P(S^m_C), the projective determinantal variety of nonzero rank<=2 matrices has dimension 2m−2. The projective point [I] is outside it when m>=3. The incidence of projective (D_m−s−1)-planes through [I] meeting that variety has dimension at most the Grassmannian dimension minus s plus (2m−2). If s>2m−2, the incidence image is a proper closed algebraic subset; its complement is Zariski open and nonempty. Real rational L containing I are Zariski dense in the real Grassmannian and thus meet this open set. This is the same elementary incidence proof as Milestone 01, specialized to rank two. QED.

## Explicit example without genericity

Take L=span{I_m} for m>=3, for which s=D_m−1 and no nonzero rank<=2 matrix belongs to L (since rank I=m>2). Then EVERY rank-one projector allowed by the balanced complement lift comes from a vector (a,+/-a), and their span is only R_J. The source trace-only fibre contains all trace-one density matrices. The balanced companion J_(1/2,1) therefore cannot be realized as an EXACT single-face rank-one measurement fibre, despite the fact that DIFFERENT order-O(m²) many-to-one two-basis shadows of the trace-only body exist (Milestone 19).

## Conceptual consequence

The balanced complement construction is UNIVERSAL for rank-one-generated source operator systems (Milestones 31-35), but it CANNOT directly replace the tensor/purification compiler for generic dense operator systems. A new globally positive order-O(m) lift would have to use a substantially different matrix-valued companion than beta tr(X)I−alpha X, or abandon exact full-fibre positive-linear retraction. This cleanly isolates why the already solved SHARPNESS problem does not automatically solve unrestricted O(m²+p) size universality.

## Audit

- The theorem assumes NO nonzero rank<=2 matrix in L, not simply no rank-one PSD matrix; the stronger condition is needed because aa^T−bb^T can have rank two and indefinite sign.
- The projective determinantal avoidance threshold s>2m−2 is exact for this incidence method, not a claimed necessary threshold for all L.
- Every nonzero vector v in the paired family has b=+/−a; the zero vector is irrelevant to rank-one projectors.
- The rank-one span includes both common symmetric diagonal and symmetric off-diagonal blocks but lacks skew cross blocks and independent W-valued diagonal differences; the deficit is m²−s>0.
- J(I_m) is positive definite on all 2m dimensions because alpha>0, beta m−alpha>0 for m>=3 and beta>=alpha. Thus extra compressed measurement kernel directions REALLY give neighboring PSD exact competitors, so the obstruction is full-fibre, not formal.
- The conclusion is architecture-specific; no assertion about unrestricted quadratic-sized many-to-one positive quotient universality follows.
