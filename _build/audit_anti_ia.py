#!/usr/bin/env python3
"""Gate anti-IA — falha se boilerplate/duplicação/ângulos ruins."""
from __future__ import annotations

import collections
import hashlib
import re
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "tecnicas"

BANNED = [
    r"eu não reaproveito o playbook genérico da família",
    r"Eu valido isso cedo — muda targeting",
    r"Nesta variante, o detalhe operacional é",
    r"Mapeamento: `",
    r"sintoma no log/UI sem side-effect",
    r"só então abro severidade alta",
    r"Outro analista repete em ≤90 minutos",
    r"eu faço eu faço",
    r"é o que muda targeting e o que sobe no report",
]

ANGLE_SUFFIX = {
    "--detecao.md": "detecção",
    "--lab.md": "lab",
    "--evidencia.md": "evidência",
    "--path.md": "path",
    "--hardening.md": "hardening",
}


def angle_of(name: str) -> str:
    for suf, label in ANGLE_SUFFIX.items():
        if name.endswith(suf):
            return label
    return "base"


def main() -> int:
    files = list(OUT.rglob("*.md"))
    errors: list[str] = []
    if len(files) != 1000:
        errors.append(f"count={len(files)} want 1000")

    hashes = [hashlib.sha256(p.read_bytes()).hexdigest() for p in files]
    if len(set(hashes)) != len(hashes):
        errors.append(f"duplicate content hashes: {len(hashes) - len(set(hashes))}")

    for pat in BANNED:
        rx = re.compile(pat, re.I)
        hits = [p for p in files if rx.search(p.read_text())]
        if hits:
            errors.append(f"banned '{pat}' in {len(hits)} files e.g. {hits[0].name}")

    ang = collections.Counter(angle_of(p.name) for p in files)
    print("angles", dict(ang))
    for k in ("path", "evidência", "hardening", "lab", "detecção"):
        if ang[k] < 80:
            errors.append(f"angle {k}={ang[k]} < 80")
    if ang["base"] < 350:
        errors.append(f"base={ang['base']} too low")

    seqs = collections.Counter()
    for p in files:
        hs = tuple(re.findall(r"^## .+$", p.read_text(), re.M))
        if hs:
            seqs[hs] += 1
    if seqs:
        top_n = seqs.most_common(1)[0][1]
        pct = 100 * top_n / len(files)
        print(f"top header seq share {pct:.1f}%")
        if pct > 15:
            errors.append(f"header sequence dominance {pct:.1f}% > 15%")

    dup_files = 0
    for p in files:
        t = p.read_text()
        bullets = re.findall(r"^- .{40,}$", t, re.M)
        seen = set()
        for b in bullets:
            if b in seen:
                dup_files += 1
                break
            seen.add(b)
    print(f"files with duplicated bullets: {dup_files}")
    if dup_files > 50:
        errors.append(f"too many duplicated bullets: {dup_files}")

    lens = [len(p.read_text()) for p in files]
    sd = statistics.stdev(lens)
    print(f"len min/avg/max {min(lens)} {sum(lens)//len(lens)} {max(lens)} stdev {sd:.0f}")
    if sd < 200:
        errors.append(f"length too uniform stdev={sd:.0f}")

    # 100% das notas com ≥1 fence; diversidade do bloco de exemplo
    fence_re = re.compile(r"```[\w+-]*\n.*?```", re.S)
    missing_fence = []
    fence_bodies: collections.Counter[str] = collections.Counter()
    for p in files:
        t = p.read_text()
        fences = fence_re.findall(t)
        if len(fences) < 1:
            missing_fence.append(p.name)
        for f in fences:
            fence_bodies[f] += 1
    print(f"notes missing fence: {len(missing_fence)}")
    if missing_fence:
        errors.append(f"missing fence in {len(missing_fence)} notes e.g. {missing_fence[0]}")
    if fence_bodies:
        top_body, top_n = fence_bodies.most_common(1)[0]
        pct = 100 * top_n / len(files)
        print(f"top example share {pct:.2f}% (n={top_n})")
        if pct >= 3.0:
            errors.append(f"example dominance {pct:.2f}% >= 3%")

    samples = {
        "kerberoast-rc4": list(OUT.rglob("*kerberoast-rc4.md")),
        "idor": list(OUT.rglob("*idor-numeric.md")),
        "esc1": list(OUT.rglob("*ad-cs-esc1.md")),
        "imds": list(OUT.rglob("*ssrf-imds.md")),
        "jwt-det": list(OUT.rglob("*jwt-alg-none--detecao.md")),
        "mass-base": list(OUT.rglob("*mass-assignment-query-param.md")),
        "any-lab": list(OUT.rglob("*--lab.md"))[:1],
        "any-path": list(OUT.rglob("*--path.md"))[:1],
        "any-hard": list(OUT.rglob("*--hardening.md"))[:1],
    }
    for k, v in samples.items():
        if not v:
            errors.append(f"missing sample {k}")
        else:
            txt = v[0].read_text()
            print(f"sample {k}: {v[0].name} ({len(txt)}c) fences={len(fence_re.findall(txt))}")
            if not fence_re.search(txt):
                errors.append(f"sample {k} has no example fence")

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
