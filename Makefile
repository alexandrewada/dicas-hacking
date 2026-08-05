PY ?= python3

extract:
	$(PY) _build/extract_seed.py

build:
	$(PY) _build/build.py

audit:
	$(PY) _build/audit_anti_ia.py

check:
	$(PY) _build/build.py --check

.PHONY: extract build audit check
