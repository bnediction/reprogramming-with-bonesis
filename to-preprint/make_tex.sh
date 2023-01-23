#!/bin/sh
set -x
rm -rf paper_files
jupyter nbconvert --config config.py
if [[ "$1" != "--no-patch" ]]; then
    patch paper.tex fixtures.patch
fi
latexmk -f -pdf paper.tex
