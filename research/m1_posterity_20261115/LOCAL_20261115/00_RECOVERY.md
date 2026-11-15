# Manuscript I continuation — recovery checkpoint

Date: 2026-11-15. Status: **the arbitrary-order plain-DRS last-iterate theorem is NOT proved or disproved.**

## Authoritative remote baseline

Repository: `Harman6139/Posterity-Files`.
Research branch: `research/pro-m1-allorder-drs-20261114`.
Last commit verified in the preceding attempt: `2d1f975c4a0ecd3ec6b47baeee3be33639ad0118`.
Directory: `research/pro_m1_allorder_drs_20261114`.
Files 01–03 contain the saturation equivalence, rational order-seven candidate, and exact matrix virial identities. The original mathematical baseline is `22ed4becd320695b41f8a11f1223ea090ef89ecf`.

## Exact target

For U=a+L, K=S_+^m, and plain Frobenius DRS Tz=z+P_K(2P_Uz-z)-P_Uz, the inherited result is z_k=Vk^p+o(k^p), 0<p<1. The missing assertion is k^(1-p)(z_(k+1)-z_k) -> pV. No differentiation of the discrete little-o remainder is valid.

## Recovered rigorous identities

Let P=P_L, Q=I-P, z=a+x+y, x=Pz, y=Qz-a, d=Tz-z. Then v=a+x+d and s=y+d are PSD and vs=0. Thus

    Tz=(z+|2P_Uz-z|)/2,
    (Tz)^2-z^2=-(P_Uz)y-y(P_Uz)-d^2.

For symmetric D with Da+aD=0 and E_D(z)=tr[D(z-a)^2],

    E_D(Tz)-E_D(z)=-tr(Dd^2)-<Dx+xD,y>.

These are exact identities, not a positive Lyapunov function without additional sign information.

The prior saturation equivalence identifies the missing PSD-specific assertion as

    ||Qv_k-a|| / min{||Qv-a||: v>=0, ||Pv||<=||Pv_k||} -> 1.

There is a typographical error in prior checkpoint 01, Section 6.2: cross-cone positivity gives <v_k,s(t)> >= 0, not equality. The ensuing inequality uses the correct sign.

## Pending analytical modification, NOT a counterexample

Use indices 0,...,6 and Fij=Eij+Eji. The original doubled-arrow direction space has generators E00,E33,E11-F02/2,E44-F35/2,E66+gamma(F02-F35),F06, with a=-(F01+F34)/2. Its numerical oscillations may be transient because of nonlinear charge feedback.

The new balanced variant replaces E00,E33 by E00+E33 and adds E22-E55. This retains an invariant doubled-arrow orbit and the same weak infeasibility/escape exponent, while removing two antisymmetric neutral diagonal modes. Whether it produces genuine persistent oscillations remains UNPROVED. The preceding interrupted calculation gave a scaled one-column transverse amplitude about 0.03134 after 200000 floating-point iterations, which is diagnostic only.

## Persistence note

The preceding runtime's local files did not survive. This recovery note is therefore being supplied as a conversation attachment in addition to local storage. A remote write has not been performed in this continuation.
