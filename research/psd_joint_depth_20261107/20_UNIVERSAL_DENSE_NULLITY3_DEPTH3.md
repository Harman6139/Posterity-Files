# Universal *dense* nullity-three / degree-three theorem: sharp exponent at most 1/3

2026-11-07 — New result for **every** arbitrary dense real PSD measurement kernel, not merely sparse midpoint constructions.

Let L:S^n -> R^m have a uniquely recoverable PSD target X* with positive rank r and nullity nu=n-r=3. Suppose its **minimal** facial reduction degree is d=3. Then the sharp full-matrix recovery exponent satisfies
\[
\boxed{\alpha(L,X_*)\le 1/3.}
\]
Moreover, using the previously established universal nullity-three exponent spectrum and the explicit sparse realizations, the exact **joint** spectrum for target nullity three is
\[
\boxed{
\Sigma_{3,1}=\{1,1/2\},\qquad
\Sigma_{3,2}=\{1/2,3/8,1/4\},\qquad
\Sigma_{3,3}=\{1/3,1/4,1/6,1/8\}.}
\]
Here target rank r>=1 is arbitrary; appending a fully measured positive block preserves all claims. The maximal-depth dense exclusion alpha>1/3 is *proved without weighted-flag theory*, via primal kernel directions dual to the two exposing stresses. This is the first complete dense joint-depth spectrum beyond the nullity-two classification in the earlier memorandum.

## I. Exact dense theorem and proof

Put K=ker L and U=range X*. Since nu=3 and d=3, **every** valid minimal facial-reduction sequence removes exactly one null direction per step. Choose one such sequence. Let e1,e2,e3 be a null-space orthonormal basis in reverse exposing order, so that the first exposing stress, after normalization, is Z0=E33 in K^perp, and the second exposing stress Z1 in K^perp has compression on
   W1=U+span{e1,e2}
equal to E22. Here Eij=e_i e_j^T and Fij=e_i e_j^T+e_j e_i^T for i!=j; indices 1,2,3 denote null directions. Since Z0=E33, we have
   H33=0 for **every H in K**.                               (1)
Let K1=K intersect S(W1), where S(W1) denotes all symmetric matrices supported on W1. Orthogonality to the second compressed stress gives
   H22=0 for **every H in K1**.                             (2)

### Lemma 1: first-level null-direction kernel mode exists
There exists A in K1 with A11>0 and A12=0.

**Proof.** On K1 consider linear functionals f(H)=H11 and g(H)=H12. Suppose f=c g for some c in R (including c=0). Choose the 2x2 symmetric matrix
   T= E11-(c/2)F12 + M E22,
where M>c²/4. Its W1 compression is PSD, positive definite on span{e1,e2}, and annihilates U. By (2),
   <T,H>=H11-c H12+M H22=0 for every H in K1.
The elementary orthogonal-complement identity
   (K intersect S(W1))^perp inside S(W1)
     = P_W1 K^perp P_W1
shows that T is the compression to W1 of some full ambient stress Z in K^perp. (Proof: both sides are annihilators, because the adjoint of the compression map is the inclusion S(W1)->S^n.) Z would expose *both* e1 and e2 after the first facial step. Hence d<=2, contradicting d=3. Thus f is not proportional to g. There exists A∈K1∩ker g with f(A)≠0, and change sign so A11>0. QED.

### Lemma 2: second-level null-direction kernel mode exists
There exists B∈K with B22>0 and B23=0.

**Proof.** Define phi(H)=H22 and psi(H)=H23 on K. If phi=c psi, choose the *globally* PSD stress
   Z=E22-(c/2)F23+M E33
with M>c²/4. Since H33=0 for every H in K by (1),
   <Z,H>=H22-c H23+M H33=0.
Thus Z∈K^perp is PSD and exposes both e2 and e3 in *one* step, implying d<=2, contradiction. Therefore phi is not proportional to psi, giving B in ker psi with phi(B)>0 after sign choice. QED.

### Cubic PSD curve

Write D=X*|U>0. Let a=A11>0, b=B22>0, and choose positive constants M,C later. Set
\[
X(t)=X_*+tA+Mt^2B+Ct^3 E_{33},\quad 0<t\ll1.
\]
Because A is supported on W1, and A12=B23=0, the Schur complement of its U block, indexed by e1,e2,e3, has the orders
\[
S(t)=
\begin{pmatrix}
a t+O(t^2)&O(t^2)&O(t^2)\\
O(t^2)&(Mb-\|D^{-1/2} P_U A e_2\|^2)t^2+O(t^3)&O(t^3)\\
O(t^2)&O(t^3)&C t^3+O(t^4)
\end{pmatrix}.
\]
Here the e1–e3 coefficient of order t² may depend on M. Choose M large enough to make the middle diagonal coefficient positive. Normalize S(t) by diag(t^{1/2},t,t^{3/2}) on its null coordinates. Then the limiting matrix is
\[
\begin{pmatrix}
a&0&c_{13}(M)\\0&Mb-\|D^{-1/2}P_UAe_2\|^2&0\\c_{13}(M)&0&C
\end{pmatrix}.
\]
For large C this is positive definite. Hence X(t)≻0 for all sufficiently small t>0.

Because A,B∈K, the measurement residual is
   ||L(X(t)-X*)||=C t³||L E33||=Theta(t³).
It is nonzero since E33∈K^perp\{0}. Meanwhile ||X(t)-X*||=Theta(t), because A≠0. Therefore
   omega(delta)>=c delta^{1/3},
and the optimal recovery exponent is <=1/3. QED.

**Note:** The existence of A and B is forced by the *minimality of facial degree*, not by any sparse structure or any chosen recovery curve. This is the decisive dense compatibility mechanism.

## II. Exact all-degree nullity-three catalogue

Prior independently proved universal weighted-flag/midpoint extraction for nullity nu<=3 gives the unconditioned exact set
   {1,1/2,3/8,1/3,1/4,1/6,1/8}.
The midpoint patterns at h<=2 internal levels are explicitly:
   no internal levels -> exponent 1/2;
   {1/2} -> 1/2,1/4;
   {1/4,1/2} -> 1/4,1/8;
   {1/3,2/3} -> 1/3,1/6;
   {1/2,3/4} -> 1/2,3/8,1/4.
Lipschitz stability gives 1.

Depth d=1 gives exactly {1,1/2} by a full-null exposing stress and the tangent-cone criterion. The previously proved universal degree-two spectrum at nu=3 gives {1/2,3/8,1/4}; it follows from the degree-two compression/denominator obstruction in the weighted-flag theorem (checkpoint 03 and the earlier nullity-three work). By the new theorem, d=3 excludes 1,1/2,3/8. Therefore d=3 can only have {1/3,1/4,1/6,1/8}. Conversely all four, and all the degree-two values, are explicitly realized by the verified sparse harmonic graph construction with exactly the indicated degree. Hence all three joint sets above are equalities.

## III. Fully explicit *dense* example attaining 1/3 at depth 3

In S^4 let X*=E00 and K=span{A,B,C}, with
\[
A=E_{11}-E_{00}+F_{03},\qquad
B=E_{22}-E_{00}+F_{13},\qquad
C=F_{03}+F_{02}.
\]
Take L to be orthogonal projection onto K^perp. Then X* is uniquely PSD-feasible. Every first exposing PSD stress annihilating X* is supported on e3 (the K^perp equations force Z11=Z22=0). After first removing e3, every valid second exposing compression is supported on e2: orthogonality to C forces Z03=0, orthogonality to A then forces Z11=0. Thus minimal degree d=3. The explicit exact-feasible-sharp curve is
\[
X(t)=E_{00}+t(A-C)+2t^2B+5t^3E_{33}
=
\begin{pmatrix}
1-t-2t^2&0&-t&0\\
0&t&0&2t^2\\
-t&0&2t^2&0\\
0&2t^2&0&5t^3
\end{pmatrix}.
\]
It is PSD for all sufficiently small t>0: after simultaneous row/column permutation into {0,2}|{1,3}, the 2x2 determinant tests are
   det block(0,2)=t²(1-2t-4t²)>0,
   det block(1,3)=t⁴(5-4)=t⁴>0;
both diagonal blocks have positive diagonal entries. Its residual is Theta(t³), displacement Theta(t). Thus alpha<=1/3. The universal nullity-three catalogue (or direct PSD minor elimination) gives alpha>=1/3 here, so equality.

## IV. Scope

This is a universal dense-map structural result for *exact* (nullity 3, minimal facial reduction degree 3), answering the dense compatibility gap at the first previously unresolved dimension. It does not prove the sparse depth-preservation principle or universal analogues of the sparse maximal-depth reciprocal theorem for nu>=4. Larger nullities may have multiple directions peeled at each step and different cross-block interactions. The canonical greedy-stress criterion used is established prior theory; the order-three primal mechanism is proved directly here. Bibliographic novelty/priority requires independent audit.