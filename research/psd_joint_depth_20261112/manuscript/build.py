#!/usr/bin/env python3
"""Build the exact manuscript PDF, choosing an available BibTeX executable."""
from pathlib import Path
import shutil
import subprocess

root = Path(__file__).resolve().parent
latex = shutil.which('pdflatex')
bibtex = shutil.which('bibtex') or shutil.which('bibtex.original') or shutil.which('bibtex8')
if not latex or not bibtex:
    raise SystemExit('Install a TeX distribution with pdflatex and BibTeX.')
commands = [[latex, '-interaction=nonstopmode', '-halt-on-error', 'manuscript.tex'],
            [bibtex, 'manuscript'],
            [latex, '-interaction=nonstopmode', '-halt-on-error', 'manuscript.tex'],
            [latex, '-interaction=nonstopmode', '-halt-on-error', 'manuscript.tex']]
logdir = root / 'build'
logdir.mkdir(exist_ok=True)
for i, command in enumerate(commands, 1):
    with (logdir / f'build_{i}.log').open('w') as out:
        result = subprocess.run(command, cwd=root, stdout=out, stderr=subprocess.STDOUT)
    if result.returncode:
        raise SystemExit(f'Build failed; inspect build/build_{i}.log')
log = (root / 'manuscript.log').read_text(errors='replace')
for marker in ('undefined references', 'undefined citations', 'Overfull \\hbox'):
    if marker in log:
        raise SystemExit(f'PDF produced but preflight failed: {marker}')
print(root / 'manuscript.pdf')
