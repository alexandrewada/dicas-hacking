#!/usr/bin/env python3
"""Reconstrói _build/seed.json + _build/titles.json a partir das 380 notas base.

As notas em tecnicas/ são a única fonte de verdade (o seed original em /tmp se
perdeu). O parser inverte os 6 layouts base do gerador antigo e grava as seções
em PROSA FINAL — build.py vira renderizador puro, sem re-aplicar clean()/
FOCUS_EXPAND sobre o conteúdo.

O split fid/slug é ambíguo no nome do arquivo (ex.: recon-passive-dns-crtsh);
é resolvido pelo hash de layout (H(fid/slug) % 6 bate com a estrutura da nota)
e desambiguado pela tag de 6 hex que examples_bank grava nos fences.

Campos não recuperáveis das notas (não afetam a renderização — documentado):
  - extras / ftitle: só alimentavam expand_focus; o foco vai pronto em `focus`
  - owasp: só aparece no meta dos layouts 0/3/5 (ausente nos layouts 1/2/4)
  - mitre: ausente nos layouts 2/4; recuperado da variante --detecao quando há
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

from build import ANGLES, BANK, CATS, H, clean, pick_bank
from examples_bank import example_block

ROOT = Path(__file__).resolve().parents[1]
TEC = ROOT / "tecnicas"
HERE = Path(__file__).resolve().parent
SEED_OUT = HERE / "seed.json"
TITLES_OUT = HERE / "titles.json"

ANGLE_RE = re.compile(r"--(detecao|lab|evidencia|path|hardening)\.md$")
ANGLE_ACC = {"detecao": "detecção", "lab": "lab", "evidencia": "evidência", "path": "path", "hardening": "hardening"}

EX_HEADERS = {"Exemplo", "PoC mínimo", "No lab ficou assim", "Sinal / query"}
META_RE = re.compile(r"^\*\*(.+?)\*\* · `(.+?)`\s*$")
MITRE_ONLY_RE = re.compile(r"^`(.+?)`\s*$")
REV_RE = re.compile(r"\n*_rev \d+_\s*$")

LAYOUT_SIGS = {
    0: ["## O que muda aqui", "## Como testo", "## Campo", "## Já me queimei", "## Blue"],
    1: ["## Por que importa", "## Passo a passo", "## Nota de operador", "## Armadilha", "## Depois"],
    2: ["## Detalhe", "## Execução", "## OpSec", "## Cuidados", "## Fechamento"],
    4: ["## Leitura rápida", "## Foco", "## Mãos na massa", "## Pitfall", "## Detecção / remediação", "## Prova"],
    5: ["## Como eu faço", "## Diferencial desta nota", "## Onde já errei", "## Entrega"],
}

# cabeçalho da seção de foco por ângulo
ANGLE_FOCUS_H = {
    "detecção": "Hipótese",
    "lab": "Variante",
    "evidência": "O que precisa aparecer",
    "path": "Por que pivota",
    "hardening": "Controles desta variante",
}
ANGLE_PITS_H = {
    "detecção": "Freio",
    "lab": "Pitfall",
    "evidência": "Armadilha",
    "path": "Freio",
    "hardening": "Armadilha",
}
# ângulos cuja seção de pits leva um parágrafo de banco colado no fim
ANGLE_PITS_BANK = {"detecção", "lab"}


def tag6(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()[:6]


def detect_layout(text: str) -> int | None:
    for lay, sigs in LAYOUT_SIGS.items():
        if all(s in text for s in sigs):
            return lay
    if "**Método**" in text and "**Freio:**" in text and "Detecto via:" in text:
        return 3
    return None


def split_segments(text: str) -> tuple[str, list[tuple[str, str]]]:
    """Divide em (texto pré-headers, [(cabeçalho ##, corpo)]). Fence-aware."""
    pre_lines: list[str] = []
    segs: list[tuple[str, list[str]]] = []
    cur: tuple[str, list[str]] | None = None
    in_fence = False
    for ln in text.splitlines():
        if ln.strip().startswith("```"):
            in_fence = not in_fence
        m = None if in_fence else re.match(r"^#{2,3}\s+(.+?)\s*$", ln)
        if m:
            if cur is not None:
                segs.append(cur)
            cur = (m.group(1), [])
            continue
        (cur[1] if cur is not None else pre_lines).append(ln)
    if cur is not None:
        segs.append(cur)
    pre = "\n".join(pre_lines).strip("\n")
    return pre, [(h, "\n".join(b).strip("\n")) for h, b in segs]


def seg(segs: list[tuple[str, str]], *names: str) -> str | None:
    for h, b in segs:
        if h in names:
            return b
    return None


def bullets(body: str) -> list[str]:
    return [ln[2:] for ln in body.splitlines() if ln.startswith("- ")]


def numbered(body: str) -> list[str]:
    return [re.sub(r"^\d+\.\s*", "", ln) for ln in body.splitlines() if re.match(r"^\d+\.\s", ln)]


def paragraphs(body: str) -> list[str]:
    return [p.strip() for p in re.split(r"\n\s*\n", body) if p.strip()]


def marked(body: str, markers: list[tuple[str, str]]) -> dict[str, str]:
    """Parseia blocos 'prefixo: valor' com linhas de continuação."""
    out: dict[str, str] = {}
    curk: str | None = None
    curv: list[str] = []
    for ln in body.splitlines():
        hit = None
        for k, pref in markers:
            if ln.startswith(pref):
                hit = (k, ln[len(pref):])
                break
        if hit:
            if curk is not None:
                out[curk] = "\n".join(curv).strip()
            curk, curv = hit[0], [hit[1]]
        elif curk is not None:
            curv.append(ln)
    if curk is not None:
        out[curk] = "\n".join(curv).strip()
    return out


def strip_fence(body: str) -> str:
    return re.sub(r"```[\w+-]*\n.*?```\n?", "", body, count=1, flags=re.S).strip("\n")


def strip_bank(row: dict, body: str, n: int) -> str:
    """Remove parágrafos finais que casam com o banco esperado (regenerado)."""
    expected = pick_bank(row, n)
    paras = paragraphs(body)
    while paras and expected and paras[-1] == expected[-1]:
        paras.pop()
        expected.pop()
    return "\n\n".join(paras).strip()


FP_PATTERNS = [
    re.compile(r"^Já abri High demais em (.+?) por sintoma sem efeito\. Cruzei com: ", re.S),
    re.compile(r"^Falso amigo em (.+?): UI/log gritam, impacto não\. Exijo ", re.S),
    re.compile(r"^Antes de Critical em (.+?), confiro se a telemetria que eu cobraria reagiria — ", re.S),
    re.compile(r"^(.+?): se não reproduz efeito \(authz/dado/exec\), não infla severidade\. Referência de sinal: ", re.S),
]
FALLBACK_FOCUS_RE = re.compile(r"^Variante (.+?): trato separado da família `(.+?)`\.$")
REPORT_LABEL_RE = re.compile(r"^Título: (.+)$", re.M)


def resolve_fid_slug(name: str, text: str) -> tuple[str, str, int] | None:
    """Split fid/slug do nome do arquivo, validado por layout + tag do fence."""
    lay = detect_layout(text)
    if lay is None:
        return None
    rest = name[:-3][5:]  # drop .md e NNNN-
    parts = rest.split("-")
    cands = []
    for i in range(1, len(parts)):
        fid, slug = "-".join(parts[:i]), "-".join(parts[i:])
        if H(f"{fid}/{slug}") % 6 != lay:
            continue
        cands.append((tag6(f"{fid}/{slug}/base") in text, fid, slug))
    best = [c for c in cands if c[0]]
    if len(best) == 1:
        return best[0][1], best[0][2], lay
    if not best and len(cands) == 1:
        return cands[0][1], cands[0][2], lay
    return None


def extract_base(text: str, fid: str, slug: str, layout: int, cat: str) -> dict:
    """Extrai os campos da nota base conforme o layout. Prosa final."""
    text = REV_RE.sub("\n", text.rstrip()) + "\n"
    pre, segs = split_segments(text)
    pre_lines = pre.splitlines()
    row: dict = {"fid": fid, "slug": slug, "cat": cat}
    warns: list[str] = []

    row["title"] = pre_lines[0].lstrip("# ").strip()
    meta = next((META_RE.match(ln) for ln in pre_lines if META_RE.match(ln)), None)
    if meta:
        row["owasp"], row["mitre"] = meta.group(1), meta.group(2)
    else:
        m = next((MITRE_ONLY_RE.match(ln) for ln in pre_lines[1:] if MITRE_ONLY_RE.match(ln)), None)
        row["owasp"] = ""
        row["mitre"] = m.group(1) if m else ""

    if layout == 0:
        row["teoria"] = seg(segs, "Contexto") or ""
        row["focus"] = bullets(seg(segs, "O que muda aqui") or "")
        row["steps"] = numbered(seg(segs, "Como testo") or "")
        campo = paragraphs(seg(segs, "Campo") or "")
        row["fp"] = campo[-1] if campo else ""
        row["pits"] = (seg(segs, "Já me queimei") or "").strip()
        blue = marked(seg(segs, "Blue") or "", [("detect", "- Detectar: "), ("mitigate", "- Fechar: ")])
        row["detect"], row["mitigate"] = blue.get("detect", ""), blue.get("mitigate", "")
        row["evidence"] = (seg(segs, "Evidência") or "").strip()
        row["refs"] = bullets(seg(segs, "Refs") or "")
    elif layout == 1:
        row["teoria"] = seg(segs, "Por que importa") or ""
        row["focus"] = bullets(seg(segs, "Variante") or "")
        row["steps"] = numbered(seg(segs, "Passo a passo") or "")
        arm = paragraphs(seg(segs, "Armadilha") or "")
        row["fp"] = arm[-1] if arm else ""
        row["pits"] = "\n\n".join(arm[:-1]).strip()
        depois = marked(seg(segs, "Depois") or "",
                        [("detect", "Detecção — "), ("mitigate", "Remediação — "), ("evidence", "No PDF — ")])
        row["detect"] = depois.get("detect", "")
        row["mitigate"] = depois.get("mitigate", "")
        row["evidence"] = depois.get("evidence", "")
        row["refs"] = bullets(seg(segs, "Refs") or "")
    elif layout == 2:
        row["teoria"] = seg(segs, "Contexto") or ""
        row["focus"] = bullets(seg(segs, "Detalhe") or "")
        row["steps"] = numbered(seg(segs, "Execução") or "")
        row["opsec"] = (seg(segs, "OpSec") or "").strip()
        row["pits"] = (seg(segs, "Cuidados") or "").strip()
        fech = marked(seg(segs, "Fechamento") or "",
                      [("detect", "| Detecção | "), ("mitigate", "| Remediação | "), ("evidence", "| Evidência | ")])
        for k in ("detect", "mitigate", "evidence"):
            row[k] = re.sub(r"\s*\|\s*$", "", fech.get(k, ""))
        row["refs"] = bullets(seg(segs, "Refs") or "")
    elif layout == 3:
        vpos = next(i for i, ln in enumerate(pre_lines) if ln.startswith("**Variante:** "))
        mpos = next(i for i, ln in enumerate(pre_lines) if ln == "**Método**")
        meta_end = next(i for i, ln in enumerate(pre_lines) if META_RE.match(ln)) + 1
        row["teoria"] = "\n".join(pre_lines[meta_end:vpos]).strip("\n").strip()
        row["focus_joined"] = pre_lines[vpos][len("**Variante:** "):]  # foco real vem do ângulo
        row["steps"] = numbered("\n".join(pre_lines[mpos + 1:]))
        ex_body = strip_fence(seg(segs, *EX_HEADERS) or "")
        freio = re.search(r"^\*\*Freio:\*\* (.*)$", ex_body, re.M)
        row["pits_first"] = freio.group(1).strip() if freio else ""
        after = ex_body[freio.end():] if freio else ex_body
        det_pos = after.find("Detecto via: ")
        row["fp"] = after[:det_pos].strip() if det_pos >= 0 else ""
        vals = marked(after, [("detect", "Detecto via: "), ("mitigate", "Corrijo com: "),
                              ("evidence", "Levo no report: "), ("refs", "Refs: ")])
        row["detect"] = vals.get("detect", "")
        row["mitigate"] = vals.get("mitigate", "")
        row["evidence"] = vals.get("evidence", "")
        row["refs"] = [r.strip() for r in vals.get("refs", "").split(", ") if r.strip()]
    elif layout == 4:
        row["teoria"] = seg(segs, "Leitura rápida") or ""
        row["focus"] = bullets(seg(segs, "Foco") or "")
        row["steps"] = numbered(seg(segs, "Mãos na massa") or "")
        row["pits"] = (seg(segs, "Pitfall") or "").strip()
        det = paragraphs(seg(segs, "Detecção / remediação") or "")
        row["detect"] = det[0] if det else ""
        row["mitigate"] = det[1][2:].strip() if len(det) > 1 and det[1].startswith("→ ") else (det[1] if len(det) > 1 else "")
        row["evidence"] = (seg(segs, "Prova") or "").strip()
        row["refs"] = bullets(seg(segs, "Refs") or "")
    else:  # layout 5
        row["teoria"] = seg(segs, "Contexto") or ""
        row["steps"] = numbered(seg(segs, "Como eu faço") or "")
        dif = seg(segs, "Diferencial desta nota") or ""
        dif_lines = dif.splitlines()
        last_bullet = max((i for i, ln in enumerate(dif_lines) if ln.startswith("- ")), default=-1)
        row["focus"] = bullets(dif)
        row["fp"] = "\n".join(dif_lines[last_bullet + 1:]).strip()
        row["pits"] = strip_bank(row, seg(segs, "Onde já errei") or "", 1 + (H(f"{fid}/{slug}") % 2))
        ent = marked(seg(segs, "Entrega") or "",
                     [("detect", "- blue: "), ("mitigate", "- fix: "), ("evidence", "- proof: ")])
        row["detect"] = ent.get("detect", "")
        row["mitigate"] = ent.get("mitigate", "")
        row["evidence"] = ent.get("evidence", "")
        row["refs"] = bullets(seg(segs, "Refs") or "")

    row["_warns"] = warns
    return row


def extract_angle(text: str, angle: str, row_stub: dict) -> dict:
    """Campos autoritativos das variantes: foco, pits completos, refs, mitre."""
    text = REV_RE.sub("\n", text.rstrip()) + "\n"
    pre, segs = split_segments(text)
    out: dict = {}
    focus_b = seg(segs, ANGLE_FOCUS_H[angle])
    if focus_b:
        out["focus"] = bullets(focus_b)
    pits_b = seg(segs, ANGLE_PITS_H[angle])
    if pits_b is not None:
        if angle in ANGLE_PITS_BANK:
            out["pits"] = strip_bank(row_stub, pits_b, 1)
        else:
            out["pits"] = pits_b.strip()
    refs_b = seg(segs, "Refs")
    if refs_b:
        out["refs"] = bullets(refs_b)
    if angle == "detecção":
        m = re.search(r"Gap de detecção em `(.+?)` / ", pre) or re.search(r"amarrado a `(.+?)`", text)
        if m:
            out["mitre"] = m.group(1)
    return out


def label_candidates(row: dict, base_text: str) -> list[str]:
    """Candidatos a label: fp (variante conhecida), fallback de foco, fence de report."""
    cands: list[str] = []
    fp = row.get("fp") or ""
    if fp:
        variant = H(f"fp/{row['fid']}/{row['slug']}") % 4
        m = FP_PATTERNS[variant].match(fp)
        if m:
            cands.append(m.group(1))
    for item in row.get("focus") or []:
        m = FALLBACK_FOCUS_RE.match(item)
        if m:
            cands.append(m.group(1))
    m = REPORT_LABEL_RE.search(base_text)
    if m:
        cands.append(m.group(1).strip())
    cands.append(row["title"])
    seen, out = set(), []
    for c in cands:
        if c and c not in seen:
            seen.add(c)
            out.append(c)
    return out


def fences_of(text: str) -> list[str]:
    return [f.strip() for f in re.findall(r"## (?:Exemplo|PoC mínimo|No lab ficou assim|Sinal / query)\n\n```[\w+-]*\n.*?```", text, re.S)]


def pick_label(row: dict, cands: list[str], notes: list[str]) -> tuple[str, bool]:
    """Escolhe o label que reproduz os fences (base + ângulos) da família.

    O fence na nota passou pelo clean() final do pipeline — replica-se aqui.
    """
    expected = sorted(f for n in notes for f in fences_of(n))
    if not expected:
        return cands[0], True
    for label in cands:
        test = dict(row, label=label)
        got = [clean(example_block(test, None)).strip()]
        got += [clean(example_block(test, ang)).strip() for ang in row.get("_angles", [])]
        if sorted(got) == expected:
            return label, True
    return cands[0], False


def main() -> int:
    files = sorted(TEC.rglob("*.md"))
    bases = [p for p in files if not ANGLE_RE.search(p.name)]
    angles: dict[str, list[tuple[str, Path]]] = {}
    for p in files:
        m = ANGLE_RE.search(p.name)
        if m:
            fam = p.name[: m.start()][5:]
            angles.setdefault(fam, []).append((ANGLE_ACC[m.group(1)], p))

    rows: list[dict] = []
    titles: dict[str, str] = {}
    problems: list[str] = []
    label_fences_fail: list[str] = []
    missing = Counter()

    for p in sorted(bases, key=lambda x: x.name):
        text = p.read_text()
        resolved = resolve_fid_slug(p.name, text)
        if resolved is None:
            problems.append(f"split/layout não resolvido: {p.name}")
            continue
        fid, slug, layout = resolved
        row = extract_base(text, fid, slug, layout, p.parent.name)
        fam_key = f"{fid}-{slug}"
        angle_notes = angles.get(fam_key, [])
        row["_angles"] = [a for a, _ in angle_notes]

        # campos autoritativos via variantes (layout 3 trunca pits/foco/refs)
        stub = {"fid": fid, "slug": slug, "cat": row["cat"]}
        for ang, ap in angle_notes:
            got = extract_angle(ap.read_text(), ang, stub)
            if layout == 3:
                for k in ("focus", "pits", "refs"):
                    if got.get(k) and not row.get(k):
                        row[k] = got[k]
                    elif got.get(k) and row.get(k) and got[k] != row[k]:
                        row[k] = got[k]  # variante é autoritativa
            if not row.get("mitre") and got.get("mitre"):
                row["mitre"] = got["mitre"]

        if layout == 3 and not row.get("focus"):
            problems.append(f"{fam_key}: layout 3 sem foco recuperado")
        if row.get("pits_first") and layout == 3:
            if not row.get("pits") or not row["pits"].startswith(row["pits_first"]):
                problems.append(f"{fam_key}: pits da variante não bate com Freio do layout 3")

        label, ok = pick_label(row, label_candidates(row, text), [text] + [ap.read_text() for _, ap in angle_notes])
        row["label"] = label
        if not ok:
            label_fences_fail.append(fam_key)

        if not row["owasp"]:
            missing["owasp"] += 1
        if not row["mitre"]:
            missing["mitre"] += 1
        for k in ("teoria", "steps", "focus", "pits", "detect", "mitigate", "evidence", "refs"):
            if not row.get(k):
                missing[k] += 1
                problems.append(f"{fam_key}: campo vazio {k}")

        titles[f"{fid}/{slug}"] = row["title"]
        metodo = "\n".join(f"{i}. {s}" for i, s in enumerate(row.pop("steps"), 1))
        row.pop("_angles")
        warns = row.pop("_warns")
        problems.extend(f"{fam_key}: {w}" for w in warns)
        row.pop("focus_joined", None)
        row.pop("pits_first", None)
        rows.append({
            "fid": fid,
            "slug": slug,
            "cat": row["cat"],
            "label": row["label"],
            "ftitle": "",  # não recuperável: só alimentava expand_focus (aposentado)
            "title": row["title"],
            "owasp": row["owasp"],
            "mitre": row["mitre"],
            "teoria": row["teoria"],
            "metodo": metodo,
            "focus": row["focus"],
            "pits": row["pits"],
            "detect": row["detect"],
            "mitigate": row["mitigate"],
            "evidence": row["evidence"],
            "refs": row["refs"],
            "extras": [],  # não recuperável: foco já vai pronto em `focus`
            "fp": row.get("fp") or None,
            "opsec": row.get("opsec") or None,
        })

    SEED_OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
    TITLES_OUT.write_text(json.dumps(titles, ensure_ascii=False, indent=2) + "\n")

    print(f"técnicas extraídas: {len(rows)} (esperado 380)")
    print(f"campos ausentes (placeholders): {dict(missing)}")
    if label_fences_fail:
        print(f"label sem reproduzir fences ({len(label_fences_fail)}): {label_fences_fail[:10]}")
    if problems:
        print(f"problemas ({len(problems)}):")
        for pr in problems[:30]:
            print(" -", pr)
    else:
        print("sem problemas de parsing")
    return 0 if len(rows) == 380 and not problems else 1


if __name__ == "__main__":
    sys.exit(main())
