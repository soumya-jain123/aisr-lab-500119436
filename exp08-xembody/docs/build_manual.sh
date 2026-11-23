#!/usr/bin/env bash
# Rebuild docs/MANUAL.pdf from MANUAL.md (needs pandoc + a XeTeX engine such as tectonic or xelatex).
set -e
cd "$(dirname "$0")/.."
ENGINE=$(command -v tectonic >/dev/null && echo tectonic || echo xelatex)
pandoc MANUAL.md -o docs/MANUAL.pdf --pdf-engine="$ENGINE" \
  -V geometry:margin=2.2cm -V fontsize=11pt -V mainfont="Times New Roman" -V monofont="Menlo" \
  -V colorlinks=true -V linkcolor=black -V urlcolor=black \
  -V header-includes='\usepackage{float}\floatplacement{figure}{H}' \
  --resource-path=. 
echo "wrote docs/MANUAL.pdf"
