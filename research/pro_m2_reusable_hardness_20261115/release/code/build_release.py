#!/usr/bin/env python3
"""Rebuild exact certificates, complete proof text, and optionally the PDF.

Python certificate checks require only the standard library. Markdown conversion
uses pandoc; PDF compilation uses pdflatex. No network access is needed.
"""
from __future__ import annotations
import argparse, hashlib, json, re, shutil, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def run(args,cwd=ROOT):
    subprocess.run(args,cwd=cwd,check=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--pdf',action='store_true');ap.add_argument('--markdown',action='store_true');ap.add_argument('--baseline',action='store_true');a=ap.parse_args()
    run([sys.executable,str(ROOT/'code/generate_certificates.py')])
    run([sys.executable,str(ROOT/'code/verify_certificates.py')])
    if a.baseline:
        old=ROOT/'original_baseline/code/verify_certificates.py'
        if not old.exists():raise FileNotFoundError('Original baseline verifier not packaged')
        run([sys.executable,str(old)])
    source=(ROOT/'manuscript/MAIN.tex').read_text()
    source=re.sub(r'\\input\{([^}]+)\}',lambda m:(ROOT/'manuscript'/m[1]).read_text(),source)
    out=ROOT/'manuscript/MAIN_standalone.tex';out.write_text(source)
    if a.markdown:
        if not shutil.which('pandoc'):raise RuntimeError('pandoc is required for --markdown')
        run(['pandoc',str(out),'-f','latex','-t','markdown+tex_math_dollars','--wrap=none','-o',str(ROOT/'COMPLETE_PROOFS.md')])
    if a.pdf:
        if not shutil.which('pdflatex'):raise RuntimeError('pdflatex is required for --pdf')
        for _ in range(2):run(['pdflatex','-interaction=nonstopmode','-halt-on-error','MAIN.tex'],ROOT/'manuscript')
        log=(ROOT/'manuscript/MAIN.log').read_text(errors='replace')
        bad=[line for line in log.splitlines() if 'Overfull' in line or ('undefined' in line and 'Warning' in line)]
        if bad:raise RuntimeError('PDF log requires review: '+'; '.join(bad))
    files=['manuscript/MAIN_standalone.tex','certificates/exact_certificates.json','certificates/verification_report.json']
    if a.markdown:files.append('COMPLETE_PROOFS.md')
    report={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files}
    (ROOT/'certificates/rebuild_hashes.json').write_text(json.dumps(report,indent=2)+'\n')
    print('Rebuild hashes:',json.dumps(report,indent=2))
if __name__=='__main__':main()
