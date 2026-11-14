"""Rebuild the full five-dimensional strict-separation certificate.

Python 3.10+, standard library only. No floating-point mathematical decisions.
Timing is metadata only; rational output is deterministic.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import time
from exact_algorithms import nonlocal_separate, pairing, serialize_matrix, solve_det


def main():
    n = 5
    raw = [[F(1) if i == j else F(3, 5) if (i-j) % n in (1, 4)
            else F(0) for j in range(n)] for i in range(n)]
    minors = [solve_det([row[:k] for row in raw[:k]], [0]*k)[1]
              for k in range(1, n+1)]
    expected = [F(1), F(16,25), F(7,25), F(31,625), F(11,3125)]
    if minors != expected or not all(x > 0 for x in minors):
        raise ArithmeticError('Sylvester positive-definiteness certificate failed')
    a = [[x/3 for x in row] for row in raw]
    start = time.perf_counter()
    w, certificate = nonlocal_separate(a, initial_precision=4, max_iterations=1500)
    record = {
        'input': serialize_matrix(a),
        'separator': serialize_matrix(w),
        'certificate': certificate,
        'target_pairing': str(pairing(a, w)),
        'unnormalized_input_leading_principal_minors': [str(x) for x in minors],
        'elapsed_seconds': time.perf_counter()-start,
        'all_passed': True,
    }
    target = Path(__file__).resolve().parent / 'five_cycle_nonlocal_certificate.json'
    target.write_text(json.dumps(record, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'file': target.name, 'center_tests': certificate['iterations'],
                      'epsilon': certificate['epsilon'],
                      'supports': len(certificate['cop_certificate_for_W_minus_epsilon_I'])}, indent=2))

if __name__ == '__main__':
    main()
