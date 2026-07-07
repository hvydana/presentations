#!/bin/bash
set -e
cd "$(dirname "$0")"

DOC=amd_india_opperunites

pdflatex -interaction=nonstopmode "$DOC.tex"
bibtex "$DOC"
pdflatex -interaction=nonstopmode "$DOC.tex"
pdflatex -interaction=nonstopmode "$DOC.tex"

echo "Built $DOC.pdf"
