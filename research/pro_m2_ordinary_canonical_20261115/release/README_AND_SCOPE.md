# Ordinary CP: canonical initialization and every descending adjacent rule

Research date: 15 November 2026.

## Main result

The standalone manuscript proves, for every fixed n>=5, a robust exponential lower bound in binary input-and-distance precision for EVERY strictly objective-descending extreme-ray adjacent rule on the ordinary copositive Ryshkov set, starting from the actual canonical tridiagonal T_n. The rational inputs are positive definite, strictly entrywise positive, normalized, and outside ordinary CP_n. There are no additional restrictions on Gram columns.

All improving choices are covered, not just the minimum-ratio shadow rule. The construction does not need a unique path: the checked order-five canonical target has two improving rays; the checked order-six target has three. A fixed-positive-definite-block face has the universal bounded-edge movement law |b_i'-b_i|<=1/2+2sqrt(H_ii), hence 5/2 for the canonical leading block. An integral exposure gap and cofactor heights keep every improving ray in that face for the full prefix.

No current-vertex/ray certificate can stop the prefix. Even an arbitrary scalar identity correction R+tau I of any improving ray fails to separate there. An unrelated explicit strict copositive separator nevertheless has short rational height and polynomial construction time. Algorithms that can use that global bypass, nonlocal jumps, non-descending moves, or input-dependent initialization are not covered by the local lower bound.

The conservative construction uses N=20000 n^3 E^2 with E=(d-1)!(2U^2)^(d-1), U=2Y n^2(m+1), Y=2(2n)^(n-1), and d=n(n+1)/2. It forces at least m pivots on O_n(log(m+1))-bit centers. The radius 1/(1600 n^4 N^2) preserves all claims, while arbitrary rational perturbations in this ball may have longer encodings. Constants and the quantitative exponent are not claimed optimal.

## Files and rebuild

- manuscript/MAIN.tex: complete self-contained proof, with bibliography.
- manuscript/MAIN.pdf: compiled nine-page manuscript in the conversation archive.
- COMPLETE_PROOF.md: generated readable proof companion.
- code/generate_certificates.py: exact target/separator generator and short complete branching-prefix constructor.
- code/verify_certificates.py: separately written verifier using Bareiss determinants/cofactors, with no generator imports.
- certificates/exact_certificates.json: generated exact data.
- certificates/verification_report.json: exact check and corruption-rejection results.
- certificates/rebuild_and_remote_hashes.json: clean rebuild and source identity record.

From the release directory:

```sh
python code/generate_certificates.py
python code/verify_certificates.py
pdflatex -interaction=nonstopmode -halt-on-error -output-directory manuscript manuscript/MAIN.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory manuscript manuscript/MAIN.tex
pandoc manuscript/MAIN.tex -f latex -t markdown -s -o COMPLETE_PROOF.md
```

The two Python programs need only the standard library (Python 3.9+). PDF compilation requires a normal LaTeX installation with the packages listed in the source; Markdown conversion requires pandoc. No general copositive solver or quantifier-elimination engine is required for these explicit certificates. Avoid Python's `-O` flag, because the generator deliberately uses assertions as additional checks. The separate verifier uses explicit rejection conditions.

## Fresh checks and their meaning

Six parameter families were checked in orders 5,6,8,10. All 36 canonical tangent rays in the tested orders 5 and 6 were verified. A complete improving-branch prefix through depth three in order five contains 18 distinct vertices and 26 edges. Its vertex feasibility certificates include 7,869 exact lattice evaluations and a quadratic-gap exclusion of all remaining candidate vectors/denominators. The verifier checks 119 shared-active incidences and the 5/2 movement bound. Seven deliberately corrupted data sets were rejected.

The m=2^64 family is an analytical guarantee of at least 18,446,744,073,709,551,616 pivots, NOT a simulated trajectory. For that n=5 input, N has 4823 bits, not 64 bits. The full theorem rests on analytical induction over all possible improving choices, not on the tested finite prefix.

Certificate data SHA256:
048031057335bfb9fc7c86df3ecba5f3cc55fc32c484e6013d9f79efd577f95f

## Prior work and precise novelty scope

The algorithmic model is Dutour Sikiric--Schurmann--Vallentin, Mathematical Programming 187 (2021), 25--45, DOI 10.1007/s10107-020-01467-4, arXiv:1807.01382v4. Its Procedure 3 chooses a negative-cost extreme tangent ray and tests the current vertex/ray for separation. Conjecture 3.2 concerns eventual termination under a suitable rule, not polynomial complexity. The present result is compatible with finite termination.

Dannenberg--Schurmann, Communications in Mathematics 31 (2023), 137--156, DOI 10.46298/cm.11141, arXiv:2303.17310v4, supply prior perfect-copositive and locally finite polyhedral geometry. Oertel--Schurmann, Generalized Perfect Matrices, arXiv:2602.05841v2 (2026), generalize qualitative perfect-form/Interior Ryshkov theory. The canonical A_n form, Dirichlet approximation, cofactors, Horn copositivity, and diagonal congruence are antecedents.

These primary sources and targeted current searches were inspected in this continuation. No claim of exhaustive historical first-priority certification is made. The asserted new mechanism in this project is the general bounded-coordinate-movement theorem and its use to confine ALL improving choices from T_n for ordinary CP nonmembers. Earlier project results covered different combinations of initialization, cone, and rule restrictions; the present proof does not silently transfer their conclusions.

## Validation limits

Complete internal analytical proof and reproducible exact checks are supplied. These are not independent human review or proof-assistant certification. No variable-dimensional intrinsic separation lower bound, lower bound against unrestricted algorithms, sharp numerical exponent, or upper-quintile journal/acceptance probability is claimed. The prior registered journal benchmark remains a separate unfinished task.
