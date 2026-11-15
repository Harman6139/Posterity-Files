# Checkpoint 03 — the regular spectral center dynamics is a saddle gradient

2026-11-15. Proved refinement of Checkpoint 02, not a resolution of the singular regime. Historical priority remains unaudited.

Use Checkpoint 02's complementary support spaces E,F and center D=D_H orthogonal-sum D_G. Formulas are written for one matrix block; for products sum the traces and retain arbitrary affine coupling between the cross blocks.

## 1. A nonempty affine cross-block space

Define C_U={C: there is A_E with [[A_E,C],[C*,0]] in U}. This is nonempty and closed affine. Indeed choose u_j in U and v_j in K with u_j-v_j->0. For G positive definite on F, <G,v_j>-><G,a>=0, so positivity makes the F-F blocks tend to zero. The image of U under F-F compression is a closed affine space and therefore contains zero. Cross compression of that slice gives C_U, again closed affine. Moreover 0 is not in C_U: otherwise adding a large multiple of the E-supported recession H would produce feasibility.

For positive definite H in D_H and G in D_G on their supports, put

    Phi(H,G)=min_(C in C_U) tr(H^(-1) C G C*).        (1)

This has a unique minimizer, smooth in H,G, by strictly convex quadratic minimization on a fixed affine subspace. Phi>0, with degrees -1 in H, +1 in G and zero under simultaneous scaling.

## 2. The stationary normal point solves the quadratic problem

Let n=H+G and w_0 be the normal stationary point of Checkpoint 02. Set u_0=a+P w_0, s_0=Qw_0-a, B=u_0-s_0=Jw_0+2a. The equation w_0=D|.|(Jn)B, together with w_0=u_0+s_0, gives

    (u_0)_FF=0, (s_0)_EE=0,
    (s_0)_EF=-H^(-1)(u_0)_EF G.                     (2)

Entrywise the cross identity is u+s=(h-g)(u-s)/(h+g), equivalently g u+h s=0. Every cross variation delta C in C_U lifts to delta u in L with zero F-F block. Since s_0 is in L^perp, (2) gives the first-order condition for (1). Thus C=(u_0)_EF is its unique minimizer. Also

    h_0=||a||^2-<a,w_0>=-<u_0,s_0>=2Phi(H,G).        (3)

## 3. Leading center drift

For Checkpoint 02's b(n),

    b_H=-grad_(D_H)Phi,
    b_G=+grad_(D_G)Phi.                              (4)

Proof. Differentiating the quadratic minimum by its first-order condition gives

    -grad_H Phi=Pi_(D_H)(H^(-1) C G C* H^(-1)),
    grad_G Phi=Pi_(D_G)(C*H^(-1)C).                  (5)

To identify the matrix Taylor coefficient, expand |H-G+epsilon B|=n+epsilon B_1+epsilon^2 B_2+O(epsilon^3). Then B_1=w_0 and n B_2+B_2 n=B^2-B_1^2. In H,G eigenbases B_EF,ij=(h_i+g_j)C_ij/h_i. The E-E entry (i,l) of B^2-B_1^2 is 2(h_i+h_l)sum_j g_j C_ij conjugate(C_lj)/(h_i h_l). Hence (B_2)_EE=2H^(-1) C G C*H^(-1), and similarly (B_2)_FF=2C*H^(-1)C. The DRS factor 1/2 gives (5). QED.

The center field is therefore a saddle gradient, not descent for one convex objective. Euler identities give

    <H,b_H>=<G,b_G>=Phi(H,G).                         (6)

Its homogeneous flow preserves ||H||^2-||G||^2 and has squared-radius derivative 4Phi. At an actual cosmic ray, b(N)=h_0(N)N by Checkpoint 02; (3),(6) imply ||H||^2=||G||^2=1/2 when N is unit.

## 4. Explicit all-order constant check

For r>=1 and nonzero b in R^r take U={[[0,b*],[b,t I_r]]:t real}. It is weakly infeasible with escape exponent one by Schur complements. The inherited common-state and primal-dual balance theorems imply its leading H=h I_r and G=g E00 have h,g>0, so Checkpoint 02 applies. Here Phi=g||b||^2/h. Solving b(V)=V/2 yields

    h=sqrt(2)||b|| r^(-1/4),
    g=sqrt(2)||b|| r^(1/4),
    V=diag(g,h I_r), sqrt(k)d_k -> V/2,
    sqrt(k)||d_k|| -> ||b|| r^(1/4).

This family checks constants; it is not used to prove the structural theorem. The inherited balance dependency in proving that this family's cosmic direction is interior is explicit.
