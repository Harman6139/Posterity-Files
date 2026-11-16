#!/usr/bin/env python3
"""Rebuild exact data, verify, expand sources, and optionally compile the paper.
Only certificate tasks require Python alone. --pdf requires pdflatex;
--markdown requires pandoc. --baseline reruns the inherited suite in a tempdir.
"""
from pathlib import Path
import argparse, hashlib, json, shutil, subprocess, tempfile
ROOT=Path(__file__).resolve().parents[1]

def run(args,cwd=None):subprocess.run(list(map(str,args)),cwd=cwd,check=True)
def expand(path):
    import re
    text=path.read_text()
    return re.sub(r'\\input\{([^}]+)\}',lambda m:expand(path.parent/m[1]),text)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--pdf',action='store_true');ap.add_argument('--markdown',action='store_true');ap.add_argument('--baseline',action='store_true');o=ap.parse_args()
    run(['python3',ROOT/'code/generate_certificates.py']);run(['python3',ROOT/'code/verify_certificates.py'])
    standalone=ROOT/'manuscript/MAIN_standalone.tex';standalone.write_text(expand(ROOT/'manuscript/MAIN.tex'))
    if o.baseline:
        candidates=[ROOT/'baseline/code']+[p/'research/pro_m2_ordinary_canonical_20261115/release/code' for p in ROOT.parents]
        source=next((p for p in candidates if (p/'generate_certificates.py').exists()),None)
        if source is None:raise FileNotFoundError('Inherited baseline source not found; pass --baseline only in the repository or complete archive')
        with tempfile.TemporaryDirectory() as tmp:
            t=Path(tmp);(t/'code').mkdir()
            for name in ('generate_certificates.py','verify_certificates.py'):shutil.copy2(source/name,t/'code'/name)
            run(['python3',t/'code/generate_certificates.py']);run(['python3',t/'code/verify_certificates.py'])
            shutil.copy2(t/'certificates/verification_report.json',ROOT/'certificates/baseline_verification_report.json')
    if o.pdf:
        for _ in range(2):run(['pdflatex','-interaction=nonstopmode','-halt-on-error','MAIN.tex'],ROOT/'manuscript')
        log=(ROOT/'manuscript/MAIN.log').read_text()
        if 'Overfull' in log or 'undefined' in log:raise RuntimeError('Unresolved LaTeX warning; inspect MAIN.log')
    if o.markdown:run(['pandoc','-f','latex','-t','markdown',standalone,'-o',ROOT/'COMPLETE_PROOFS.md'])
    files=[ROOT/'manuscript/MAIN.tex',standalone,ROOT/'certificates/exact_certificates.json',ROOT/'certificates/verification_report.json']
    if o.markdown:files.append(ROOT/'COMPLETE_PROOFS.md')
    report={'status':'PASS','files':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'scope':'Rebuild hashes. PDF hashes are not assumed reproducible across TeX versions or timestamps.'}
    (ROOT/'certificates/build_report.json').write_text(json.dumps(report,indent=2)+'\n')
if __name__=='__main__':main()
