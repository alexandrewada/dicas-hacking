PY ?= python3

extract:
	$(PY) _build/extract_seed.py

build:
	$(PY) _build/build.py

audit:
	$(PY) _build/audit.py

audit-legacy:
	$(PY) _build/audit_anti_ia.py

refs-urls:
	$(PY) _build/check_refs_urls.py

check:
	$(PY) _build/build.py --check

.PHONY: extract build audit audit-legacy refs-urls check
