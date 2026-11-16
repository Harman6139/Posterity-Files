"""Compile twice and record exact build inputs and PDF identity."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parent
BUILD = ROOT / "build"
BUILD.mkdir(exist_ok=True)
for number in (1, 2):
    run = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "-recorder", "main.tex"],
        cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    (BUILD / f"compile-{number}.txt").write_bytes(run.stdout)
    if run.returncode:
        raise SystemExit(f"Compilation {number} failed; see build/compile-{number}.txt")
log = (ROOT / "main.log").read_text(errors="replace")
issues = [line for line in log.splitlines()
          if any(term in line for term in ("Warning:", "Overfull", "Underfull"))]
if issues:
    raise SystemExit("Build needs inspection:\n" + "\n".join(issues))
inputs = {}
for line in (ROOT / "main.fls").read_text(errors="replace").splitlines():
    if line.startswith("INPUT "):
        path = Path(line[6:])
        if not path.is_absolute():
            path = ROOT / path
        if path.is_file() and path.suffix not in (".aux", ".out"):
            inputs[str(path.resolve())] = hashlib.sha256(path.read_bytes()).hexdigest()
pdf = (ROOT / "main.pdf").read_bytes()
project_sources = {
    path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
    for path in sorted(ROOT.rglob("*.tex"))
    if "build" not in path.relative_to(ROOT).parts
}
project_sources["build.py"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
source_tree_sha256 = hashlib.sha256(
    "\n".join(name + "\0" + digest for name, digest in sorted(project_sources.items())).encode()
).hexdigest()
record = {
    "pages": int(re.search(r"Output written on main.pdf \((\d+) pages", log).group(1)),
    "pdf_bytes": len(pdf), "pdf_sha256": hashlib.sha256(pdf).hexdigest(),
    "source_sha256": hashlib.sha256((ROOT / "main.tex").read_bytes()).hexdigest(),
    "source_tree_sha256": source_tree_sha256,
    "project_sources": project_sources,
    "warnings": issues,
    "engine": subprocess.check_output(["pdflatex", "--version"]).decode().splitlines()[0],
    "class": "article 2025/01/22 v1.4n; 11pt; A4; 27mm margins",
    "input_dependencies": inputs,
}
(BUILD / "build_record.json").write_bytes((json.dumps(record, indent=2) + "\n").encode())
print(json.dumps({k: v for k, v in record.items() if k not in ("input_dependencies", "project_sources")}, indent=2))
