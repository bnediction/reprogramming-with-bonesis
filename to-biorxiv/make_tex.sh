#!/bin/sh
set -x
rm -rf paper_files
jupyter nbconvert --config config.py
#if [[ "$1" == "--patch" ]]; then
#    patch paper.tex manual.patch -o -
#fi
latexmk -f -pdf paper.tex
