#!/usr/bin/env bash
# Build the gesture-mimic GTAC 2026 paper.
# Usage: ./build.sh [basename]   (default: gesture_mimic)

set -e

DOC="${1:-padim-optimization}"

echo "==> pdflatex pass 1"
pdflatex -interaction=nonstopmode -halt-on-error "${DOC}.tex"

echo "==> bibtex"
bibtex "${DOC}"

echo "==> pdflatex pass 2"
pdflatex -interaction=nonstopmode -halt-on-error "${DOC}.tex"

echo "==> pdflatex pass 3"
pdflatex -interaction=nonstopmode -halt-on-error "${DOC}.tex"

echo "==> done: ${DOC}.pdf"
