#!/usr/bin/env python3
"""Checa URLs canônicas do refs_bank (mapa, não 1000×N notas).

Falha só se bases críticas (mitre/owasp/portswigger) caírem ou se
muitas URLs reais do mapa quebrarem. Timeout curto; HEAD→GET fallback.
"""
from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "_build" / "refs_bank.py"

TIMEOUT = 10
WORKERS = 6
FAIL_RATIO = 0.35
MAX_FAILURES_ABS = 25

# bases que devem responder (path raiz / host)
CRITICAL_HOSTS = (
    "attack.mitre.org",
    "owasp.org",
    "portswigger.net",
    "cheatsheetseries.owasp.org",
)

UA = (
    "Mozilla/5.0 (compatible; dicas-hacking-refs-check/1.0; "
    "+https://github.com/alexandrewada)"
)


def extract_urls(text: str) -> list[str]:
    found = re.findall(r"https?://[^\s\"')>]+", text)
    cleaned: list[str] = []
    seen: set[str] = set()
    for u in found:
        u = u.rstrip(".,);]")
        # ignora templates f-string / format
        if "{" in u or "}" in u:
            continue
        if u not in seen:
            seen.add(u)
            cleaned.append(u)
    return cleaned


def _request(url: str, method: str) -> tuple[bool, str]:
    req = urllib.request.Request(
        url,
        method=method,
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            code = getattr(resp, "status", 200) or 200
            # lê pouco pra fechar conexão em GET
            if method == "GET":
                resp.read(256)
            return 200 <= code < 400, f"{method} {code}"
    except urllib.error.HTTPError as e:
        # anti-bot / rate-limit / gateway flaky → não conta como link quebrado canônico
        if e.code in (403, 429, 502, 503, 999):
            return True, f"skip {e.code}"
        if method == "HEAD" and e.code in (404, 405, 501):
            return _request(url, "GET")
        return False, f"{method} HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        if method == "HEAD":
            return _request(url, "GET")
        # hosts flaky (crt.sh etc.) — não derrubam o gate
        if "crt.sh" in url:
            return True, f"skip flaky: {type(e).__name__}"
        return False, f"{type(e).__name__}: {e}"


def probe(url: str) -> tuple[str, bool, str]:
    ok, msg = _request(url, "HEAD")
    return url, ok, msg


def host_of(url: str) -> str:
    m = re.match(r"https?://([^/]+)", url)
    return (m.group(1) if m else "").lower()


def main() -> int:
    if not REFS.is_file():
        print(f"FAIL missing {REFS}")
        return 1
    urls = extract_urls(REFS.read_text())
    print(f"refs_bank unique URLs: {len(urls)}")

    results: list[tuple[str, bool, str]] = []
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futs = [pool.submit(probe, u) for u in urls]
        for fut in as_completed(futs):
            results.append(fut.result())

    failed = [(u, msg) for u, ok, msg in results if not ok]
    ok_n = len(results) - len(failed)
    print(f"ok={ok_n} fail={len(failed)}")

    for u, msg in sorted(failed)[:25]:
        print(f"  FAIL {u} ({msg})")
    if len(failed) > 25:
        print(f"  ... +{len(failed) - 25} more")

    # bases críticas: pelo menos 1 URL daquele host deve ter OK
    errors: list[str] = []
    for host in CRITICAL_HOSTS:
        host_results = [(u, ok, m) for u, ok, m in results if host_of(u) == host or host_of(u).endswith("." + host)]
        if not host_results:
            continue
        if not any(ok for _, ok, _ in host_results):
            errors.append(f"critical host down: {host}")

    ratio = len(failed) / max(len(results), 1)
    if len(failed) >= MAX_FAILURES_ABS and ratio >= FAIL_RATIO:
        errors.append(
            f"too many broken refs URLs: {len(failed)}/{len(results)} ({ratio:.0%})"
        )

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print("PASS")
    if failed:
        print(f"(aviso: {len(failed)} URL(s) falharam mas abaixo do limiar / anti-bot)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
