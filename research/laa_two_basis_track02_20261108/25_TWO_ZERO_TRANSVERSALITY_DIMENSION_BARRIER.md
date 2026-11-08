# Milestone 25 — a sharp 2d−1 first-order stability barrier for ALL minimal two-zero Naimark constructions

Date 2026-11-08. This extends the exact Gram-graph cross-rank formula of Milestone 23 to two arbitrary, possibly different Parseval frames, and proves a structural obstruction to sharp first-order source residual recovery in any minimal two-zero exposing construction. It does NOT obstruct signed-stress or many-to-one designs of different architecture.

## 1. Setup

Let G in R^{d x M_1}, H in R^{d x M_2} be rank-one Parseval frames (GG^T=HH^T=I_d), with nonzero columns and M_i>d. Let
  W=span{g_jg_j^T (all j), h_kh_k^T (all k)} <= S^d,
  q=dim W.
For each frame define its Gram projection P_G=G^T G and P_H=H^T H and the support graphs Gamma_G,Gamma_H, where distinct columns i,j are adjacent whenever the corresponding Gram projector entry is nonzero. Let c_G,c_H denote the numbers of graph components.

Consider a minimal two-zero Naimark realization of these two frames, with ambient order
  N=M_1+M_2-d,
source face V of dimension d, first-basis M_1 nonzero projected frame columns G and M_2-d zero columns, and second-basis M_2 nonzero projected frame columns H and M_1-d zero columns. Assume their zero-vector subspaces span V^perp, as is necessary for exposure by the zero outcomes alone. The canonical construction and small exterior rotations in Milestone 21 realize such a model.

The compressed source-data map is
  M_src(Z)=(M_G(Z),M_H(Z)).
The first-order exterior cross data form the image of Y_cross=K+K^T with K=P_V K P_(V^perp).

## Theorem — exact cross quotient dimension

In such a minimal realization, after discarding the identically zero slots, the first-order exterior cross-data image has dimension
  (M_1-c_G)+(M_2-c_H).
Moreover, its quotient of the source-data image has dimension at most
  c_G+c_H-1 <= 2d-1.
Consequently, if q>c_G+c_H-1, there exists a nonzero source perturbation H_0 in S^d with nonzero source measurement signal, and an exterior cross block K_0 such that
  B(E(H_0)+K_0+K_0^T)=0,
where B is the full two-basis measurement map and E embeds the face.

If the source reference Z_*>0, the corresponding first-order cancellation admits an actual PSD curve Y(t) with
  ||B(Y(t)-E(Z_*))||=Theta(t²),
  ||M_src(D(Y(t))-Z_*)||=Theta(t),
where D is the positive compression decoder. In particular the linear estimate
  ||M_src(D(Y)-Z_*)|| <= C ||B(Y-E(Z_*))||
is IMPOSSIBLE for all PSD ambient competitors, no matter how large the constant C.

A necessary condition for such a linear residual decoder within this zero-only architecture is therefore
  dim W <= c_G+c_H-1 <= 2d-1.                      (1)
This is sharp as a dimension threshold: two orthonormal-basis frames themselves have c_G=c_H=d and their combined measurement span has dimension at most 2d-1.

## Proof

1. Complete G by K_G in R^{(M_1-d) x M_1} with [G;K_G] orthogonal; likewise complete H by K_H. In the canonical minimal dilation the source exterior Q decomposes as the direct sum of two spaces of dimensions M_1-d and M_2-d. The first-basis surviving vectors have exterior components given by the rows of K_G in the first component, while the second-basis surviving vectors have components given by K_H in the other component. A small exterior rotation preserving exact exposure changes the input coordinates by an invertible map; it does not change the output image or the rank counts.

2. The first cross map is
   T_G(X)=diag(G^T X K_G), X in R^{d x(M_1-d)};
and the second is the analogous T_H. Since the two exterior components can be chosen independently, the full cross-data image is their direct sum. Milestone 23 proves directly that the adjoint kernel of T_G is the set of lambda satisfying
   [P_G,diag(lambda)]=0,
which consists of vectors constant on components of Gamma_G. Hence rank T_G=M_1-c_G. Similarly rank T_H=M_2-c_H. This proves the exact cross rank.

3. The quotient R^{M_1}/ran T_G has dimension c_G and can be identified with the component-sum functionals. The analogous second quotient has dimension c_H. For every source symmetric Z, the sum of all first-frame measurements equals tr Z and the sum of all second-frame measurements equals the SAME tr Z, because both are Parseval. Therefore the image of M_src in the direct sum of these quotients obeys one nontrivial linear relation (equality of the two total sums). Its quotient image dimension is at most c_G+c_H-1.

4. The source measurement map has rank q. If q>c_G+c_H-1, its quotient image has a nonzero kernel. Choose H_0 with M_src(H_0)!=0 but whose outputs belong to the cross-data image. By independence of the two exterior blocks, choose K_0 so the full two-basis first-order data cancel:
   B(E(H_0)+K_0+K_0^T)=0.
The trace of H_0 must vanish, since cross-data in each basis have zero total sum.

5. Let Z_*>0. For small t>0 the source block Z_*+tH_0 remains positive definite. Choose a fixed exterior PSD matrix G_Q satisfying
   G_Q >= 2 K_0^T E(Z_*)^dagger K_0
on V^perp. The Schur complement shows that
   Y(t)=E(Z_*+tH_0)+t(K_0+K_0^T)+t²G_Q
is PSD for sufficiently small t. The first-order measurement term cancels, so
   B(Y(t)-E(Z_*))=t²B(G_Q).
Choose G_Q positive definite on V^perp; the measured trace makes ||B(G_Q)||>0. Positive compression decodes D(Y(t))=Z_*+tH_0, so its source data residual is exactly t||M_src(H_0)||>0. This proves the quantitative cancellation.

6. Each graph component of Gamma_G corresponds to a mutually orthogonal, nonzero subspace spanned by its frame vectors. Hence c_G<=d, and similarly c_H<=d. This proves the final inequality in (1). QED.

## Consequences and scope

- For a generic Parseval frame with connected Gram graph, c_G=1. If both frames are connected, only the trace direction survives first-order cross elimination, regardless of the potentially very large dim W. This includes the tetrahedral source system d=3,M=4,dim W=4 (Milestone 23).
- For a source operator space of dimension q>>d, NO minimal zero-only two-ONB exposed-face lift based on these frames can have a uniform linear residual decoder. The O(sqrt(delta)) compressed residual bound in Milestone 21 is not just a loose inequality for strictly feasible source points.
- The positive-observation second lift in Milestone 24 composes with this first stage; it retains exact fibres and objectives but cannot retrospectively restore the source first-order information that the zero-only stage hides.
- This no-go is NOT an unrestricted lower bound against signed exposing stresses, nonlinear decoders, or large-slack surjective representations.
- The argument is algebraic and works for REAL PSD matrices of all ranks. Strict feasibility Z_*>0 is needed only for the Schur-repaired quantitative curve, not for the cross-rank identity.
