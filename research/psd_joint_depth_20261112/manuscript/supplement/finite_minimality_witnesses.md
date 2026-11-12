# Four finite-minimality witnesses

Extracted from the supplied Milestone 139 research packet for the optional computer-assisted minimum-nullity appendix. The main Theorems A–C do not depend on this finite minimality claim. This note deliberately omits the separate product program and the superseded terminal cut-rank formulation.

## 7. Minimum separating nullity: a separately certified finite result

The separation at nullity six is analytic. The statement that it is the first separation is computer-assisted, using the exact arithmetic program 140. No numerical SDP oracle or exponent fitting occurs.

At each nu<=5, the necessary complex tuples are enumerated from the established harmonic/survivor-table theorem 137. Every such tuple is then certified by a real one-switch construction with multiplicities (128/132), a real single-policy construction with multiplicities, or one of four explicit tied-edge witnesses below. The exact cardinalities are:

    nu   complex tuples   one-switch/single-policy   extra witnesses
     1         2                    2                      0
     2         4                    4                      0
     3        11                   11                      0
     4        48                   48                      0
     5       292                  288                      4.

These count distinct (profile,alpha) pairs, not policies or labelled schedules. The real constructions have source rank one; fully observed support padding covers every positive rank. The four remaining pairs at nu=5 are

    ((1,2,1,1), 2/7),
    ((1,2,2),   5/16),
    ((1,2,2),   7/18),
    ((1,2,2),   4/9).

A single tied family handles all four. With p in {2,3,4}, take tight parents

    ((0,p),(1,4),(2,4),(3,5)),

the corresponding four standard generators E_ii-E_00+lambda R_(P_i), and add the unused source release lambda R_05 to the third generator. At the second step the explicit stress E_33+E_44-c(R_05+R_35) exposes {3,4}. If p=2, H_1 still blocks coordinate 1, so the last two steps expose {2},{1}. If p=3 or 4, both remaining coordinates can be exposed together by E_11+E_22-c(R_(0,p)+R_14). The first maximal exposure is {5}, and the source-row argument proves second-step maximality. All edges used as releases are distinct from tight edges.

Use these weight/leading-edge choices:

    p=2: (2/7,4/7,5/7,6/7,1), no leading edge;
    p=3: (3/8,5/8,3/4,7/8,1), add lambda R_02;
    p=4: (4/9,2/3,7/9,8/9,1), add lambda R_03 or no edge.

The exponents are respectively 2/7, 5/16, 7/18 and 4/9. Every listed edge respects its assigned order. Unique tight pivots and the convex-square positive separator give the full-ambient bound; the thick monomial arc gives sharpness. The leading edges are unused by the displayed stresses. These are exact matrix constructions, not numerical witnesses.

The program includes the full enumerator and all four exact pairing checks. The finite set equality is the load-bearing computer-assisted part of the minimum-nullity assertion. It must not be described as an all-dimensional real classification.

