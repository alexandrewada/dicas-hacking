#!/usr/bin/env python3
"""Gate de qualidade do caderno — unicidade, ângulos, frontmatter, refs e links."""
from __future__ import annotations

import collections
import hashlib
import re
import statistics
import sys
from pathlib import Path

import yaml

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

FM_REQUIRED = ("id", "categoria", "slug", "angulo", "mitre", "tags")
FM_FAMILY_KEYS = ("familia", "fid")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
URL_REF_RE = re.compile(r"\[[^\]]+\]\(https?://[^)]+\)")
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
REL_SECTION_RE = re.compile(r"^## Relacionadas\s*$", re.M)
REL_BODY_RE = re.compile(r"^## Relacionadas\n(.*?)(?=\n## |\Z)", re.S | re.M)


def angle_of(name: str) -> str:
    for suf, label in ANGLE_SUFFIX.items():
        if name.endswith(suf):
            return label
    return "base"


def parse_frontmatter(text: str) -> dict | None:
    m = FM_RE.match(text)
    if not m:
        return None
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def is_external_or_anchor(href: str) -> bool:
    h = href.strip()
    return (
        h.startswith(("http://", "https://", "mailto:", "#"))
        or h.startswith("//")
    )


def resolve_ok(base: Path, href: str) -> bool:
    """Resolve link relativo a partir do dir da nota (ignora âncora #frag)."""
    path_part = href.split("#", 1)[0].strip()
    if not path_part:
        return True
    target = (base / path_part).resolve()
    try:
        target.relative_to(ROOT.resolve())
    except ValueError:
        return False
    return target.is_file()


def main() -> int:
    files = sorted(OUT.rglob("*.md"))
    errors: list[str] = []
    if len(files) != 1000:
        errors.append(f"count={len(files)} want 1000")

    hashes = [hashlib.sha256(p.read_bytes()).hexdigest() for p in files]
    if len(set(hashes)) != len(hashes):
        errors.append(f"duplicate content hashes: {len(hashes) - len(set(hashes))}")

    texts = {p: p.read_text() for p in files}

    for pat in BANNED:
        rx = re.compile(pat, re.I)
        hits = [p for p, t in texts.items() if rx.search(t)]
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
        hs = tuple(re.findall(r"^## .+$", texts[p], re.M))
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
        bullets = re.findall(r"^- .{40,}$", texts[p], re.M)
        seen: set[str] = set()
        for b in bullets:
            if b in seen:
                dup_files += 1
                break
            seen.add(b)
    print(f"files with duplicated bullets: {dup_files}")
    if dup_files > 50:
        errors.append(f"too many duplicated bullets: {dup_files}")

    lens = [len(texts[p]) for p in files]
    sd = statistics.stdev(lens) if len(lens) > 1 else 0.0
    print(f"len min/avg/max {min(lens)} {sum(lens)//len(lens)} {max(lens)} stdev {sd:.0f}")
    if sd < 200:
        errors.append(f"length too uniform stdev={sd:.0f}")

    fence_re = re.compile(r"```[\w+-]*\n.*?```", re.S)
    missing_fence = []
    fence_bodies: collections.Counter[str] = collections.Counter()
    for p in files:
        t = texts[p]
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

    # --- gates Fase 5: frontmatter, Relacionadas, refs URL, links internos ---
    bad_fm: list[str] = []
    missing_rel: list[str] = []
    missing_url_ref: list[str] = []
    broken_rel: list[str] = []
    broken_body = 0

    for p in files:
        t = texts[p]
        fm = parse_frontmatter(t)
        if fm is None:
            bad_fm.append(p.name)
        else:
            miss = [k for k in FM_REQUIRED if k not in fm]
            if not any(k in fm for k in FM_FAMILY_KEYS):
                miss.append("familia|fid")
            # mitre pode ser string vazia; tags deve ser lista
            if "mitre" in fm and fm["mitre"] is None:
                miss.append("mitre(null)")
            if "tags" in fm and not isinstance(fm["tags"], list):
                miss.append("tags(not-list)")
            if miss:
                bad_fm.append(f"{p.name}:{','.join(miss)}")

        if not REL_SECTION_RE.search(t):
            missing_rel.append(p.name)

        if not URL_REF_RE.search(t):
            missing_url_ref.append(p.name)

        rel_m = REL_BODY_RE.search(t)
        if rel_m:
            for href in MD_LINK_RE.findall(rel_m.group(1)):
                if is_external_or_anchor(href):
                    continue
                if not resolve_ok(p.parent, href):
                    broken_rel.append(f"{p.name} -> {href}")

        # corpo (fora de Relacionadas): idealmente também resolve; conta mas não amostra todas
        body = REL_BODY_RE.sub("", t)
        # remove frontmatter e fences para não pegar paths fictícios em PoCs
        body = FM_RE.sub("", body, count=1)
        body = fence_re.sub("", body)
        for href in MD_LINK_RE.findall(body):
            if is_external_or_anchor(href):
                continue
            if not resolve_ok(p.parent, href):
                broken_body += 1

    print(f"frontmatter inválido: {len(bad_fm)}")
    print(f"sem ## Relacionadas: {len(missing_rel)}")
    print(f"sem ref URL Markdown: {len(missing_url_ref)}")
    print(f"links quebrados em Relacionadas: {len(broken_rel)}")
    print(f"links relativos quebrados no corpo: {broken_body}")

    if bad_fm:
        errors.append(f"frontmatter inválido em {len(bad_fm)} notes e.g. {bad_fm[0]}")
    if missing_rel:
        errors.append(f"missing ## Relacionadas in {len(missing_rel)} notes e.g. {missing_rel[0]}")
    if missing_url_ref:
        errors.append(
            f"missing Markdown URL ref in {len(missing_url_ref)} notes e.g. {missing_url_ref[0]}"
        )
    if broken_rel:
        errors.append(
            f"broken Relacionadas links: {len(broken_rel)} e.g. {broken_rel[0]}"
        )
    # corpo: falha só se houver volume significativo (PoCs podem citar paths fictícios)
    if broken_body > 20:
        errors.append(f"too many broken body relative links: {broken_body}")

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
            txt = texts.get(v[0]) or v[0].read_text()
            print(f"sample {k}: {v[0].name} ({len(txt)}c) fences={len(fence_re.findall(txt))}")
            if not fence_re.search(txt):
                errors.append(f"sample {k} has no example fence")
            if parse_frontmatter(txt) is None:
                errors.append(f"sample {k} missing frontmatter")
            if not REL_SECTION_RE.search(txt):
                errors.append(f"sample {k} missing Relacionadas")

    if errors:
        print("FAIL")
        for e in errors:
            print(" -", e)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
