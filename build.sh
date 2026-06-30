#!/bin/bash
set -e
cd GTAC2026-Submission-Template-LaTeX-2026

pdflatex chapter_14_15_16.tex
bibtex chapter_14_15_16
pdflatex chapter_14_15_16.tex
pdflatex chapter_14_15_16.tex
