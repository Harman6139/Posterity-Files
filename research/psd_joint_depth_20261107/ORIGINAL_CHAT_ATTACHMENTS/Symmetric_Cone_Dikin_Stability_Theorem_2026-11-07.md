# Universal sharp recovery from the canonical barrier Hessian on every symmetric cone

Research memorandum — 7 November 2026. Generalization of the universal PSD Dikin–Hessian classifier to every finite-dimensional symmetric cone (finite direct products included). The Jordan-algebraic identities used are standard, while the canonical recovery-modulus comparison is proved directly. No bibliographic priority claim.

## Theorem

Let \(\mathcal E\) be a finite-dimensional Euclidean Jordan algebra with unit \(e\), rank \(R\), inner product \(\langle x,y\rangle=\operatorname{tr}(x\circ y)\), spectral determinant \(\det_J\), and symmetric cone \(\mathcal Q\) of Jordan squares. Let \(\mathcal L:\mathcal E\to\mathbb R^m\) be linear, \(x_*\in\mathcal Q\) the unique point of \(\mathcal Q\) with measurement \(\mathcal L x_*\), and \(K=\ker\mathcal L\). Let \(q=\|\mathcal L e\|_2>0\).

For every \(\varepsilon>0\), let \(x_\varepsilon\in\operatorname{int}\mathcal Q\) maximize \(\log\det_J x\) over \(x-x_*-\varepsilon e\in K\). Write \(P(z)=2L(z)^2-L(z^2)\) for the quadratic representation, where \(L(z)u=z\circ u\). For \(K\ne0\) define
\[
\lambda_\varepsilon=
\min_{\substack{h\in K\\\|h\|=1}}
\langle h,P(x_\varepsilon^{-1})h\rangle,
\qquad \rho_\varepsilon=\lambda_\varepsilon^{-1/2};
\]
put \(\rho_\varepsilon=0\) when \(K=0\). Then constants depending only on \(\mathcal L\) and the Jordan algebra satisfy
\[
\boxed{
\sup_{y\in\mathcal Q:\|\mathcal L(y-x_*)\|\le q\varepsilon}\|y-x_*\|
\ \asymp\ \varepsilon+\rho_\varepsilon.
}
\]
The entire optimal Hölder exponent is the vanishing order of one canonical restricted logdet-Hessian eigenvalue (capped above by one), for every symmetric cone and every singularity degree.

## Standard Jordan facts used

The symmetric cone is self-dual. Every interior \(x\) has a Jordan spectral decomposition with positive eigenvalues; \(\operatorname{tr}e=R\); \(\nabla(-\log\det_J x)=-x^{-1}\); \(\nabla^2(-\log\det_J x)=P(x^{-1})\). The self-adjoint order automorphism \(T_x=P(x^{-1/2})\) satisfies \(T_x x=e\), and \(T_x^2=P(x^{-1})\). The spectrum of \(T_x\) on Peirce diagonal/off-diagonal subspaces is \(\lambda_i(x)^{-1}\) or \((\lambda_i(x)\lambda_j(x))^{-1/2}\), respectively. Consequently
\[
\|T_x h\|^2=\langle h,P(x^{-1})h\rangle,
\qquad \|T_x\|\le 1/\lambda_{\min}(x).
\]
Every \(y\in\mathcal Q\) satisfies \(0\preceq y\preceq\operatorname{tr}(y)e\) and \(\|y\|\le\operatorname{tr}(y)\), where \(\preceq\) is the Jordan cone order. These hold equally for direct products of simple Euclidean Jordan algebras.

## Proof

Since \(x_*\) is uniquely feasible, \(K\cap\mathcal Q=\{0\}\). Strict separation of the compact trace-one slice of the proper self-dual cone from the image kernel gives \(w\in K^\perp\cap\operatorname{int}\mathcal Q\). Thus every shifted affine PSD-cone slice is bounded and contains the strict interior point \(x_*+\varepsilon e\). Strict concavity of \(\log\det_J\) yields a unique maximizer \(x_\varepsilon\), with stationarity \(x_\varepsilon^{-1}\in K^\perp\). Put \(z=\varepsilon x_\varepsilon^{-1}\in K^\perp\cap\mathcal Q\). As in the PSD proof,
\[
R=\langle x_\varepsilon^{-1},x_\varepsilon\rangle
=\langle x_\varepsilon^{-1},x_*\rangle
+\varepsilon\operatorname{tr}(x_\varepsilon^{-1}).
\]
Therefore \(\operatorname{tr}z\le R\), \(\|z\|\le R\), \(\langle z,x_*\rangle\le R\varepsilon\), and \(x_\varepsilon\succeq(\varepsilon/R)e\).

Choose a right inverse of \(\mathcal L^*\) on \(K^\perp\), norm \(\kappa\). Every \(y\in\mathcal Q\) with measurement residual at most \(\delta\) satisfies
\[
\varepsilon\langle x_\varepsilon^{-1},y\rangle
=\langle z,x_*\rangle+\langle\mathcal L^*R(z),y-x_*\rangle
\le R\varepsilon+\kappa R\delta.
\]
The order automorphism \(T_{x_\varepsilon}\) sends \(y\) into \(\mathcal Q\), with
\(\operatorname{tr}(T_{x_\varepsilon}y)=\langle x_\varepsilon^{-1},y\rangle\). Since every cone element is bounded above by its trace times \(e\), undoing the automorphism gives
\[
0\preceq y\preceq R(1+\kappa\delta/\varepsilon)x_\varepsilon.
\]
Thus \(x_*\preceq R x_\varepsilon\), and all competitors at residual \(q\varepsilon\) obey \(y\preceq C_0 x_\varepsilon\).

The Hessian-radius identity is
\[
\rho_\varepsilon=\max\{\|h\|:h\in K,\|T_{x_\varepsilon}h\|\le1\}.
\]
The norm ball sits inside the Jordan order interval \([-e,e]\), so \(x_\varepsilon\pm h\in\mathcal Q\) for every admissible \(h\), with residual \(q\varepsilon\). Triangle inequality yields \(\omega(q\varepsilon)\ge\rho_\varepsilon\). The competitor \(x_*+\varepsilon e\) yields \(\omega(q\varepsilon)\ge\varepsilon\|e\|\).

For the upper bound choose a right inverse \(J\) of \(\mathcal L\) on its range, norm \(j\). For any competitor \(y\in\mathcal Q\) with residual \(\le q\varepsilon\), put \(a=J(\mathcal L(y-x_\varepsilon))\), \(h=y-x_\varepsilon-a\in K\), so \(\|a\|\le2jq\varepsilon\). Since \(x_\varepsilon\succeq(\varepsilon/R)e\), the Peirce bound gives \(\|T_{x_\varepsilon}a\|\le2Rjq\). And since \(0\preceq T_{x_\varepsilon}y\preceq C_0e\), \(\|T_{x_\varepsilon}y\|\le C_0\sqrt R\). Thus \(\|T_{x_\varepsilon}h\|\le\sqrt R(C_0+1)+2Rjq\), and \(\|h\|\le C\rho_\varepsilon\).

Likewise \(h_0=x_\varepsilon-x_*-\varepsilon e\in K\). Using \(x_*\preceq R x_\varepsilon\), and \(\varepsilon\|x_\varepsilon^{-1}\|\le R\), gives \(\|T_{x_\varepsilon}h_0\|\le\sqrt R+R\sqrt R+R\), so \(\|h_0\|\le C'\rho_\varepsilon\). Finally
\[
y-x_*=h+h_0+a+\varepsilon e
\]
and the global upper modulus bound follows. QED.

## Interpretation and scope

This extends the arbitrary dense PSD theorem to all direct products of the five families of symmetric cones (real, complex and quaternionic Hermitian PSD, Lorentz/second-order cones, and the exceptional octonionic 3x3 cone), using their common Euclidean Jordan algebra structure. The proof uses only self-duality, homogeneous Jordan quadratic representations, and the logarithmic determinant barrier. This does not imply a comparable theorem for *spectrahedral shadows with projected recovery variables*, which are not in general symmetric cones.

References for standard Jordan identities: Euclidean Jordan algebra and symmetric-cone expositions; Hauser–Lim (2001), *Self-scaled barriers for irreducible symmetric cones*. Novelty of the composite recovery modulus theorem needs independent prior-art checking.