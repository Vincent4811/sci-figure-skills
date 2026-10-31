#!/usr/bin/env bash
# Verify fonts are embedded (emb=yes) and not Type 3. Requires poppler-utils.
for f in "$@"; do echo "== $f"; pdffonts "$f"; done
