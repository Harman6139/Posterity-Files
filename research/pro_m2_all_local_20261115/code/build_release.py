#!/usr/bin/env python3
"""Rebuild the revised paper and exact certificates.

In the GitHub tree, unchanged sections are read from the inherited grand release.
The downloadable archive contains copies of those sections, so it is standalone.
--pdf requires pdflatex; --markdown requires pandoc. Certificate checks need only
Python's standard library. No general quantifier-elimination solver is implied.
"""
from pathlib import Path
import argparse, hashlib, re, shutil, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
EXPECTED='a1a98b26d1088df503c1ea16d56c40566093ef470cb259f41c788f080a47dbb7'
OLD='Finally, in every dimension at least four a fixed nonsimplicial cone has interior rational targets with constant-width factors but unique shadow walks of exponential binary length. Their carrier and observation condition remain fixed. Thus genuine arithmetic faces control certification, whereas an interior perfect-form subdivision can impose an independent local traversal cost.'
NEW='Finally, every dimension at least four admits a fixed nonsimplicial cone and robust positive-definite, strictly entrywise-positive nonmembers on which every strictly descending extreme-ray local rule is forced through an exponential prefix. An explicit strict rational separator has logarithmic binary height. Complementary interior examples keep the arithmetic carrier and observation condition fixed. Thus genuine arithmetic faces control certification, whereas a perfect-form subdivision can impose an independent local traversal cost even when the local pivot rule is unrestricted within the descending extreme-ray class.'

def run(cmd,cwd=ROOT):
    p=subprocess.run(cmd,cwd=cwd,text=True,capture_output=True)
    if p.returncode:raise RuntimeError(p.stdout[-10000:]+p.stderr[-10000:])
    return p.stdout

def expand(path):
    text=path.read_text()
    return re.sub(r'\\input\{([^}]+)\}',lambda m:expand(path.parent/(m[1] if m[1].endswith('.tex') else m[1]+'.tex')),text)

def markdown(tex,aux,out,title):
    bib=re.search(r'\\begin\{thebibliography\}\{[^}]+\}(.*?)\\end\{thebibliography\}',tex,re.S)
    if bib:
        entries=re.findall(r'\\bibitem\{([^}]+)\}(.*?)(?=\\bibitem|\Z)',bib[1],re.S)
        replacement='\\section*{References}\n'+'\n'.join('\\paragraph{['+k+']} '+v.strip() for k,v in entries)
        tex=tex[:bib.start()]+replacement+tex[bib.end():]
    p=subprocess.run(['pandoc','-f','latex','-t','markdown','--wrap=none'],input=tex,text=True,capture_output=True)
    if p.returncode:raise RuntimeError(p.stderr)
    labels=dict(re.findall(r'\\newlabel\{([^}]+)\}\{\{([^}]+)\}',aux.read_text())) if aux.exists() else {}
    text=re.sub(r'::: \{#([^ ]+) \.\w+\}\n\*\*(Theorem|Lemma|Proposition|Corollary|Example|Remark) ([^*]+)\*\*',lambda m:'**'+m[2]+' '+labels.get(m[1],m[3])+'**',p.stdout)
    text=re.sub(r'\[(?:\\.|[^\[\]\n])*\]\(#([^)]*)\)\{reference-type="(eqref|ref)" reference="[^"]*"\}',lambda m:'('+labels.get(m[1],m[1])+')' if m[2]=='eqref' else labels.get(m[1],m[1]),text)
    text=re.sub(r'^:::.*\n?','',text,flags=re.M)
    text=re.sub(r' \{#[^}]+\}|\\label\{[^}]+\}','',text)
    text=re.sub(r'\[@([^\]]+)\]',lambda m:'['+m[1].replace('@','')+']',text)
    out.write_text('# '+title+'\n\nComplete proof source; PDF numbering is authoritative. No proof has been replaced by a summary.\n\n'+text)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--pdf',action='store_true');ap.add_argument('--markdown',action='store_true');args=ap.parse_args()
    md=ROOT/'manuscript';md.mkdir(exist_ok=True)
    base=ROOT.parent/'pro_m2_grand_20261115'/'release'/'manuscript'
    names=['01_carrier','02_completion','03_complexity','04_angular','05_geometry','06_provenance']
    if base.exists():
        for name in names:shutil.copy2(base/(name+'.tex'),md/(name+'.tex'))
        template=(base/'MASTER_THEOREM.tex').read_text()
    else:
        if not all((md/(name+'.tex')).exists() for name in names):raise RuntimeError('Inherited manuscript sections are missing')
        template=(md/'MASTER_THEOREM.tex').read_text()
    template=template.replace(OLD,NEW)
    if '\\input{07_all_local}' not in template:template=template.replace('\\input{06_provenance}','\\input{07_all_local}\n\\input{06_provenance}')
    if '\\input{08_facet_relaxation}' not in template:template=template.replace('\\input{07_all_local}','\\input{07_all_local}\n\\input{08_facet_relaxation}')
    (md/'MASTER_THEOREM.tex').write_text(template)
    preamble=template.split('\\title{',1)[0]
    body=((md/'07_all_local.tex').read_text()+'\n'+(md/'08_facet_relaxation.tex').read_text()).replace('As proved in Section~\\ref{sec:paths}','As shown directly below (and in the companion carrier manuscript)').replace('Theorem~\\ref{thm:lattice}','The cone-relative lattice estimate in the companion carrier manuscript').replace('The preceding interior example concerns one shadow rule.','The preceding Manuscript II release gave an interior example for one shadow rule.')
    head='\\title{Every descending local rule can be exponentially slow\\\\[0.4em]\\large Robust nonmembers, an integral tangent-face gap, and short rational separators}\n\\author{Manuscript II --- proof supplement}\n\\date{15 November 2026}\n\\begin{document}\n\\maketitle\n'
    abstract='\\begin{abstract}For every fixed dimension at least four, we construct a fixed nonsimplicial rational column cone and positive-definite nonmembers for which every strictly objective-descending extreme-ray adjacent-vertex algorithm has an exponentially long forced prefix in the binary input length. The obstruction persists on an explicit ball of strictly entrywise-positive targets after a fixed integral congruence. An explicit strictly copositive rational separator has logarithmic height. The proof reduces all possible improving rays to one exposed tangent face by an integral height gap, then classifies that face exactly. This strengthens the preceding carrier manuscript from one shadow rule on interior members to every rule in the stated local class on robust nonmembers. Historical first priority and a journal-percentile assessment are not claimed.\\end{abstract}\n'
    (md/'ALL_LOCAL_THEOREM.tex').write_text(preamble+head+abstract+body+'\n\\end{document}\n')
    full=expand(md/'MASTER_THEOREM.tex');(md/'MASTER_THEOREM_standalone.tex').write_text(full)
    print(run([sys.executable,str(ROOT/'code/generate_all_local.py')]).strip())
    print(run([sys.executable,str(ROOT/'code/verify_all_local.py')]).strip())
    print(run([sys.executable,str(ROOT/'code/verify_facet_relaxation.py')]).strip())
    require_hash=hashlib.sha256((ROOT/'certificates/all_local_certificates.json').read_bytes()).hexdigest()
    if require_hash!=EXPECTED:raise RuntimeError('Certificate hash mismatch: '+require_hash)
    if args.pdf:
        if not shutil.which('pdflatex'):raise RuntimeError('pdflatex missing')
        for name in ('MASTER_THEOREM','ALL_LOCAL_THEOREM'):
            for _ in range(3):run(['pdflatex','-interaction=nonstopmode','-halt-on-error',name+'.tex'],md)
            log=(md/(name+'.log')).read_text()
            if 'Overfull' in log or 'undefined references' in log:raise RuntimeError('Review LaTeX log for '+name)
    if args.markdown:
        if not shutil.which('pandoc'):raise RuntimeError('pandoc missing')
        markdown(full,md/'MASTER_THEOREM.aux',ROOT/'COMPLETE_PROOFS.md','Complete proofs: arithmetic carriers and the all-local obstruction')
        markdown((md/'ALL_LOCAL_THEOREM.tex').read_text(),md/'ALL_LOCAL_THEOREM.aux',ROOT/'ALL_LOCAL_PROOF.md','Complete proof: every descending local rule')
    print('Rebuilt and checked; certificate SHA256:',require_hash)

if __name__=='__main__':main()
