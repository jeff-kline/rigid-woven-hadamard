SHELL := /bin/sh
PY ?= python3

PDFLATEX ?= pdflatex
export SOURCE_DATE_EPOCH := 1795478400
export FORCE_SOURCE_DATE := 1
export OPENBLAS_NUM_THREADS := 1
export VECLIB_MAXIMUM_THREADS := 1
export OMP_NUM_THREADS := 1
export PYTHONDONTWRITEBYTECODE := 1

CHECKS := gauge_check count1600 meisner_equal_terms check1600 prod_check reg_check \
          meisner-stage2-checks arith size_two_fibres_check figure_recovery

.PHONY: paper verify figure node-check

# Three passes from a clean extraction; no inherited auxiliaries are required.
paper:
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	cd paper && $(PDFLATEX) -interaction=nonstopmode -halt-on-error main.tex >/dev/null
	@! grep -E 'Warning:|Overfull|undefined references|undefined citations' paper/main.log
	@echo "paper built: paper/main.pdf"

# Run every check from code/ (Python 3 with NumPy; about 25 seconds on one core) and compare each
# output with the pinned copy in evidence/.
verify:
	@mkdir -p build
	@for c in $(CHECKS); do \
	  (cd code && $(PY) $$c.py) > build/$$c.txt 2>&1 || { echo "FAILED $$c"; exit 1; }; \
	  if cmp -s evidence/$$c.txt build/$$c.txt; then echo "MATCH $$c"; \
	  else echo "MISMATCH $$c"; exit 1; fi; \
	done
	@echo "verify: all outputs match evidence/"

# Redraw paper/fig-recovery.pdf and figures/recovery.png (deterministic).
figure:
	cd code && $(PY) figure_recovery.py --write

# Optional second implementation of the order-1600 check (Node.js); not part of verify.
node-check:
	cd code && node check1600.mjs
