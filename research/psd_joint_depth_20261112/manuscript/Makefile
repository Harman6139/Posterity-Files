.PHONY: all clean audit
all:
	python3 build.py
clean:
	rm -f manuscript.aux manuscript.bbl manuscript.blg manuscript.log manuscript.out manuscript.toc manuscript.fdb_latexmk manuscript.fls
audit:
	python3 supplement/independent_audit.py --output supplement/independent_audit.json
