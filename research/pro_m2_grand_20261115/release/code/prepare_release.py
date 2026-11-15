#!/usr/bin/env python3
"""Rebuild derived manuscript and exact certificates from the saved source.

Standard library suffices for TeX expansion and mathematical certificates.
--pdf additionally requires pdflatex; --markdown requires pandoc.
This does not implement the universal real-algebraic decision procedure.
"""
from __future__ import annotations
import argparse
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_DATA_HASH = 'ed0b5405a54353b35eaaa65312e77d08d5f1ead1ae41f5a3207ef914fe103117'


def run(command: list[str], cwd: Path = ROOT) -> None:
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(f'Command failed: {command}\n{result.stdout[-10000:]}\n{result.stderr[-10000:]}')
    if result.stdout:
        print(result.stdout.strip())


def expand_tex(path: Path, stack: tuple[Path, ...] = ()) -> str:
    path = path.resolve()
    if path in stack:
        raise ValueError(f'Recursive TeX input: {path}')
    text = path.read_text(encoding='utf-8')
    def replace(match: re.Match[str]) -> str:
        name = match.group(1)
        child = path.parent / (name if name.endswith('.tex') else name + '.tex')
        return expand_tex(child, stack + (path,))
    return re.sub(r'\\input\{([^}]+)\}', replace, text)


def markdown_companion(tex: str, aux: Path) -> None:
    if not shutil.which('pandoc'):
        raise RuntimeError('pandoc is required for --markdown')
    # Preserve separate, keyed bibliography entries instead of flattening them.
    bib = re.search(r'\\begin\{thebibliography\}\{[^}]+\}(.*?)\\end\{thebibliography\}', tex, re.S)
    if bib:
        entries = re.findall(r'\\bibitem\{([^}]+)\}(.*?)(?=\\bibitem|\Z)', bib.group(1), re.S)
        replacement = '\\section*{References}\n' + '\n'.join('\\paragraph{[' + key + ']} ' + body.strip() for key, body in entries)
        tex = tex[:bib.start()] + replacement + tex[bib.end():]
    result = subprocess.run(['pandoc', '-f', 'latex', '-t', 'markdown', '--wrap=none'], input=tex, capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    text = result.stdout
    labels: dict[str, str] = {}
    if aux.exists():
        labels = dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}', aux.read_text()))
    # Align theorem numbers to the compiled manuscript, when available.
    def theorem_number(match: re.Match[str]) -> str:
        label, kind, number = match.group(1), match.group(2), match.group(3)
        return '**' + kind + ' ' + labels.get(label, number) + '**'
    text = re.sub(r'::: \{#([^ ]+) \.\w+\}\n\*\*(Theorem|Lemma|Proposition|Corollary|Example|Remark) ([^*]+)\*\*', theorem_number, text)
    # Equation and theorem references point to the PDF numbering; equation
    # labels themselves are removed from the unnumbered Markdown displays.
    def reference(match: re.Match[str]) -> str:
        label, mode = match.group(1), match.group(2)
        number = labels.get(label, label)
        return '(' + number + ')' if mode == 'eqref' else number
    text = re.sub(r'\[(?:\\.|[^\[\]\n])*\]\(#([^)]*)\)\{reference-type="(eqref|ref)" reference="[^"]*"\}', reference, text)
    text = re.sub(r'^:::.*\n?', '', text, flags=re.M)
    text = re.sub(r' \{#[^}]+\}', '', text)
    text = re.sub(r'\\label\{[^}]+\}', '', text)
    text = re.sub(r'\[@([^\]]+)\]', lambda m: '[' + m.group(1).replace('@', '') + ']', text)
    header = '# Complete proofs: Arithmetic carriers of constrained Gram representations\n\n'
    header += 'Generated from the complete LaTeX source. The PDF is authoritative for typography and numbering; equation references here use its labels, while Markdown display equations are unnumbered. No proofs have been replaced by summaries.\n\n'
    (ROOT / 'COMPLETE_PROOFS.md').write_text(header + text, encoding='utf-8')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--pdf', action='store_true')
    parser.add_argument('--markdown', action='store_true')
    args = parser.parse_args()
    manuscript = ROOT / 'manuscript'
    tex = expand_tex(manuscript / 'MASTER_THEOREM.tex')
    (manuscript / 'MASTER_THEOREM_standalone.tex').write_text(tex, encoding='utf-8')
    run([sys.executable, str(ROOT / 'code/generate_new_certificates.py')])
    run([sys.executable, str(ROOT / 'code/verify_new_certificates.py')])
    data = ROOT / 'certificates/new_exact_certificates.json'
    actual = hashlib.sha256(data.read_bytes()).hexdigest()
    if actual != EXPECTED_DATA_HASH:
        raise RuntimeError(f'Certificate hash mismatch: {actual}')
    if args.pdf:
        if not shutil.which('pdflatex'):
            raise RuntimeError('pdflatex is required for --pdf')
        for _ in range(2):
            result = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'MASTER_THEOREM.tex'], cwd=manuscript, capture_output=True, text=True)
            if result.returncode:
                raise RuntimeError(result.stdout[-12000:] + result.stderr)
        print('Compiled manuscript/MASTER_THEOREM.pdf')
    if args.markdown:
        markdown_companion(tex, manuscript / 'MASTER_THEOREM.aux')
        print('Wrote COMPLETE_PROOFS.md')
    print('Exact data hash verified:', actual)

if __name__ == '__main__':
    main()
