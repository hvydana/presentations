#!/bin/bash
set -e
cd "$(dirname "$0")"

DOC=solving_model_roi_execution_summary

pdflatex -interaction=nonstopmode "$DOC.tex"
bibtex "$DOC"
pdflatex -interaction=nonstopmode "$DOC.tex"
pdflatex -interaction=nonstopmode "$DOC.tex"

echo "Built $DOC.pdf"
