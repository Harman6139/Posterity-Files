#!/usr/bin/env python3
"""Rebuild exact certificates and optional manuscript outputs.

The exact checks require only Python's standard library. --pdf requires
pdflatex; --markdown requires pandoc. This does not implement a general
convex rational-point solver or a general quadratic-form isotropy solver.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_DATA_SHA256 = '2f432846643e31e100935ba1a4f3c58adb19bbce89bee89f2e652efc055969f7'


def run(args: list[str], cwd: Path | None = None) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf', action='store_true')
    parser.add_argument('--markdown', action='store_true')
    args = parser.parse_args()
    run([sys.executable, str(ROOT / 'code/generate_certificates.py')])
    run([sys.executable, str(ROOT / 'code/verify_certificates.py')])
    data = ROOT / 'certificates/quadratic_certificates.json'
    actual = hashlib.sha256(data.read_bytes()).hexdigest()
    if actual != EXPECTED_DATA_SHA256:
        raise RuntimeError(f'Certificate hash mismatch: {actual}')
    man = ROOT / 'manuscript'
    source = (man / 'MASTER_THEOREM.tex').read_text(encoding='utf-8')
    source = re.sub(r'\\input\{([^}]+)\}',
                    lambda m: (man / m.group(1)).read_text(encoding='utf-8'), source)
    standalone = man / 'MASTER_THEOREM_standalone.tex'
    standalone.write_text(source, encoding='utf-8')
    if args.pdf:
        if shutil.which('pdflatex') is None:
            raise RuntimeError('--pdf requires pdflatex on PATH')
        for _ in range(2):
            run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                 'MASTER_THEOREM.tex'], cwd=man)
        log = (man / 'MASTER_THEOREM.log').read_text(errors='replace')
        if 'undefined references' in log or 'Overfull' in log:
            raise RuntimeError('Inspect unresolved references or overfull boxes')
    if args.markdown:
        if shutil.which('pandoc') is None:
            raise RuntimeError('--markdown requires pandoc on PATH')
        run(['pandoc', '-f', 'latex', '-t', 'markdown+tex_math_dollars',
             '--standalone', '--wrap=none', str(standalone),
             '-o', str(ROOT / 'COMPLETE_PROOFS.md')])
    tracked = sorted([*man.glob('*.tex'), *ROOT.glob('*.md'),
                      *ROOT.glob('code/*.py'), *ROOT.glob('certificates/*.json')])
    records = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
               for p in tracked if p.name != 'SOURCE_MANIFEST.json'}
    (ROOT / 'SOURCE_MANIFEST.json').write_text(
        json.dumps(records, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print('PASS: exact verification, seven corruption rejections, and fixed data hash.')


if __name__ == '__main__':
    main()
