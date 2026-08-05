#!/usr/bin/env python3
"""Gera as 1000 notas do caderno a partir de _build/seed.json (prosa final).

Sucessor de rebuild_expert.py: o seed reconstruído por extract_seed.py já traz
as seções limpas (teoria, foco, passos, pits, detect, mitigate, evidence, refs,
fp, opsec), então este script é um RENDERIZADOR — aplica os 6 layouts base e os
5 layouts de ângulo sobre as seções prontas, sem re-aplicar clean()/
FOCUS_EXPAND sobre o conteúdo do seed. Mantém do pipeline original: banco de
campo (pick_bank), exemplos (examples_bank), colapso de linhas em branco,
clean() final (idempotente sobre a prosa extraída) e unicidade (_rev n_).
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
from pathlib import Path

from examples_bank import example_block

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
SEED = HERE / "seed.json"
TITLES = HERE / "titles.json"
TARGET = 1000

CATS = [
    ("01-recon", "Recon / OSINT"),
    ("02-web", "Web"),
    ("03-api", "API"),
    ("04-auth", "Auth"),
    ("05-injection", "Injection"),
    ("06-client", "Client-side"),
    ("07-ssrf-xxe", "SSRF / XXE"),
    ("08-network", "Rede"),
    ("09-ad", "AD"),
    ("10-windows", "Windows"),
    ("11-linux", "Linux"),
    ("12-aws", "AWS"),
    ("13-azure", "Azure / Entra"),
    ("14-k8s", "K8s"),
    ("15-mobile", "Mobile"),
    ("16-wireless", "Wireless"),
    ("17-redteam", "Red team"),
    ("18-evasion", "Purple / detecção"),
    ("19-crypto", "TLS"),
    ("20-report", "Report / ROE"),
]

# 5 ângulos × 124 = 620; + 380 bases = 1000
# Sufixo com -- para não colidir com slug 'hardening' / 'path' / 'lab'
ANGLES = [
    ("detecção", "--detecao"),
    ("lab", "--lab"),
    ("evidência", "--evidencia"),
    ("path", "--path"),
    ("hardening", "--hardening"),
]

# 1–2 frases por nota, escolhidas por hash — nunca dump do banco inteiro
BANK: dict[str, list[str]] = {
    "01-recon": [
        "Achado de recon que eu reporto: ativo fora do inventário com superfície autenticada, ou takeover com prova de controle — lista crua de subdomínio não conta.",
        "CT + DNS history + SANs viram mapa. Scan wide fora do ROE porque o ASN 'parece' do cliente é pedrada.",
        "CNAME órfão com cache CDN mentindo: confirmo NXDOMAIN/whois do alvo antes de Critical.",
    ],
    "02-web": [
        "Parâmetro é boundary: de onde veio o valor (cookie, claim, hidden) importa mais que o payload da vez.",
        "WAF bypass só depois da prova de impacto. Senão vira discussão de tool com o blue.",
        "Impacto que eu aceito: ATO, cross-tenant, escrita privilegiada, RCE. Reflection sem sink útil vira Informational.",
    ],
    "03-api": [
        "Começo pelo contrato real (OpenAPI/HAR/introspection), não pelo PDF de arquitetura.",
        "Batch e webhook: ACL costuma autorizar o primeiro ID do array e ignorar o resto. Testo isso cedo.",
        "403 no gateway com 200 no origin — path direto e Host conforme ROE.",
    ],
    "04-auth": [
        "Mint → store → use → revoke. Quebro o fluxo e testo cada perna.",
        "MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.",
        "Spray/lockout só com acordo escrito e contas canário.",
    ],
    "05-injection": [
        "Sink e context primeiro. O mesmo input vira SQL, LDAP, OS ou template — classes diferentes de impacto.",
        "Blind/time depois de error/boolean. Baseline de latência antes de claimar RCE.",
        "Payload destrutivo (DROP/shutdown) fica no lab. Em prod: boolean/read-only.",
    ],
    "06-client": [
        "XSS/CSRF: preciso do sink e da condição de auth. alert(1) sem abuso de sessão é demo.",
        "CSP bypass só se atravesso a política atual do alvo, não CSP de lab antiga.",
        "Não persisto payload em produção sem janela e plano de purge.",
    ],
    "07-ssrf-xxe": [
        "SSRF prova alcance (IMDS, admin interno, file://) e o que voltou. Open redirect sozinho não é SSRF.",
        "IMDSv2 hop limit é controle — não desculpa pra parar o teste se o ROE cobre metadata.",
        "DNS callback sem leitura de resposta mapeia egress; insuficiente pra claim de RCE.",
    ],
    "08-network": [
        "Mensuro SMB/LDAP signing e EPA antes de montar relay. Sem isso o path é teatro.",
        "Responder/ntlmrelayx em segmento acordado — sem poisoning do floor inteiro.",
        "Evidência: auth capturado + ação pós-relay em conta teste. Não hash dump do prédio.",
    ],
    "09-ad": [
        "Path até tier0 com ACE/edge exato (GenericAll, WriteDacl, ForceChangePassword). 'Deu certo' sem grafo não fecha.",
        "Ritmo no KDC/LDAP. Conta low-priv. Zero mudança destrutiva em objeto prod sem janela.",
        "RC4/AES fraco ≠ mesmo playbook. Etype e pre-auth mudam o ROI.",
    ],
    "10-windows": [
        "LOLBin: parent-child + linha de comando que o EDR deveria ter visto.",
        "DLL/serviço: path writable + binário sob identidade privilegiada. Sem os dois, não é privesc.",
        "LSASS só em lab ou ROE explícito. Em prod prefiro DPAPI/registry com conta teste.",
    ],
    "11-linux": [
        "SUID/capabilities/docker.sock/sudo -l antes de kernel exploit barulhento.",
        "Escape de container precisa de host PID/FS. Namespace cosmético não é host compromise.",
        "Exploit local com crash potencial fica no lab clonado.",
    ],
    "12-aws": [
        "Identidade > rede. Role chain e policies antes de port scan de VPC.",
        "S3: PublicAccessBlock, bucket policy e ACL podem discordar — testo os três.",
        "CloudTrail eventName + accessKeyId de teste + ARN. Screenshot da console sozinha não basta.",
    ],
    "13-azure": [
        "Entra: consent, PRT, CA e roles. Grafo de identity manda mais que NSG.",
        "Managed identity com permissão ampla = local admin da cloud.",
        "Graph com throttle. Sem spam de CA challenge em prod.",
    ],
    "14-k8s": [
        "SA token + RBAC excessivo. Leio RoleBinding antes de kubectl bomb.",
        "privileged / hostPath / CAP_SYS_ADMIN — mostro node FS ou cred do node.",
        "Lab namespace dedicado. Não mexo em prod fora do ROE.",
    ],
    "15-mobile": [
        "Frida em build de teste ≠ pin quebrado na store. Deixo a nuance no report.",
        "Deep link / WebView / exported: intent até token sink é o ROI.",
        "Keystore vs SharedPreferences plaintext — backup flags entram com nuance.",
    ],
    "16-wireless": [
        "ROE de RF por escrito: potência, canal, horário, área.",
        "Capturo handshake/credencial de conta teste — não pulverizo o prédio.",
        "Beacon spoof sem associação autenticada é demo incompleta.",
    ],
    "17-redteam": [
        "Objetivo do ROE manda. Corto path quando o goal já está provado.",
        "C2/persistência com kill-switch e janela. Beacon sem objetivo é ego.",
        "Timeline + decisões de não-exploração pesam no report.",
    ],
    "18-evasion": [
        "Uma execução limpa, telemetria ligada: alertou? Silêncio = finding de gap.",
        "Não desligo EDR pra passar. Bypass documentado é produto separado.",
        "Sigma/KQL amarrado ao MITRE da técnica — 'suspicious powershell' genérico não conta.",
    ],
    "19-crypto": [
        "TLS no stack real do app, não só ssllabs no apex.",
        "Secret leak: provo que a chave autentica no escopo. String sem uso ≠ Critical automático.",
        "Downgrade só com cliente vulnerável no escopo.",
    ],
    "20-report": [
        "Finding sem reteste path e cleanup vira pingue-pongue.",
        "Executivo: risco em 3 frases. Técnico: PoC redigido. Misturar perde os dois públicos.",
        "CVSS é input. Justifico environmental e impacto real do cliente.",
    ],
}


def H(s: str) -> int:
    return int(hashlib.sha256(s.encode()).hexdigest()[:8], 16)


def title_for(row: dict, titles: dict) -> str:
    return titles.get(f"{row['fid']}/{row['slug']}", row.get("title") or row["label"])


def clean(text: str) -> str:
    """Passada final do pipeline original (idempotente sobre a prosa do seed)."""
    pairs = [
        ("O teste expert ", "No teste, "),
        ("O pentester expert ", ""),
        ("Especialistas validam", "Valido"),
        ("Especialistas diferenciam", "Diferencio"),
        ("Especialistas ", ""),
        ("diferenciam SSRF", "Diferencio SSRF"),
        ("validam a biblioteca", "Valido a biblioteca"),
        ("Em nível especialista, eu provo", "Na prática provo"),
        ("em nível especialista, eu provo", "na prática provo"),
        ("você prova", "eu provo"),
        ("O relatório deve enfatizar", "No relatório enfatizo"),
        ("encadeia com", "encadeio com"),
        ("e trocar IDs", "e troco IDs"),
        ("ainda assim testar ACL", "ainda assim testo ACL"),
        ("foque contas", "foco contas"),
        ("Foque em", "Foco em"),
        ("foque ", "foco "),
        ("prefira provar", "prefiro provar"),
        ("mostre amostra", "mostro amostra"),
        ("revogue sempre", "revogo sempre"),
        ("Revogue sempre", "Revogo sempre"),
        ("Não execute ", "Não executo "),
        ("Não pulverize", "Não pulverizo"),
        ("Não escaneie", "Não escaneio"),
        ("Não emita", "Não emito"),
        ("Não mexa", "Não mexo"),
        ("Não faça ", "Não faço "),
        ("Não cause ", "Não causo "),
        ("Não use ", "Não uso "),
        ("Não desabilite", "Não desabilito"),
        ("Não exfiltre", "Não exfiltro"),
        ("Evite ", "Evito "),
        ("Prefira ", "Prefiro "),
        ("Documente ", "Documento "),
        ("Documentar ", "Documento "),
        ("Verifique ", "Verifico "),
        ("Confirme ", "Confirmo "),
        (" e reportar ", " e reporto "),
        ("reportar templates", "reporto templates"),
        ("eu faço eu faço ", "eu faço "),
        ("false negative", "alerta que não veio"),
        ("Recomendar ", "Recomendo "),
        ("Correlacionar ", "Correlaciono "),
        ("Rotacionar ", "Rotaciono "),
        ("avaliar LSASS", "avalio LSASS"),
        ("mapear claims", "mapeio claims"),
        ("use contas de teste", "uso contas de teste"),
        ("use cautela", "com cautela"),
    ]
    out = []
    for ln in text.splitlines():
        if not ln.strip() or ln.strip().startswith("#") or ln.strip().startswith("```"):
            out.append(ln.rstrip())
            continue
        lead = re.match(r"^(\s*)", ln).group(1)
        body = ln.strip()
        for a, b in pairs:
            body = body.replace(a, b)
        body = re.sub(r"[ \t]{2,}", " ", body)
        out.append(lead + body)
    return "\n".join(out)


def steps_of(row: dict) -> list[str]:
    """Passos em prosa final: seed só desnumera, sem transformar texto."""
    out = []
    for ln in row["metodo"].splitlines():
        ln = ln.strip()
        if not ln:
            continue
        out.append(re.sub(r"^\d+\.\s*", "", ln))
    return out


def pick_bank(row: dict, n: int = 2) -> list[str]:
    bank = BANK.get(row["cat"], BANK["02-web"])
    h = H(f"{row['fid']}/{row['slug']}/bank")
    picks = []
    for i in range(n):
        picks.append(bank[(h + i * 3) % len(bank)])
    seen = set()
    out = []
    for p in picks:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def render_base(row: dict, titles: dict) -> str:
    title = title_for(row, titles)
    key = f"{row['fid']}/{row['slug']}"
    h = H(key)
    layout = h % 6
    steps_md = "\n".join(f"{i}. {s}" for i, s in enumerate(steps_of(row), 1))
    focus = row["focus"]
    focus_md = "\n".join(f"- {x}" for x in focus)
    teoria = row["teoria"].strip()
    pits = row["pits"].strip()
    detect = row["detect"].strip()
    mitigate = row["mitigate"].strip()
    evidence = row["evidence"].strip()
    refs = "\n".join(f"- {r}" for r in row["refs"])
    bank = pick_bank(row, 1 + (h % 2))
    bank_md = "\n\n".join(bank)
    fp = (row.get("fp") or "").strip()
    opsec = (row.get("opsec") or "").strip()
    meta = f"**{row['owasp']}** · `{row['mitre']}`"
    ex = example_block(row, None).rstrip()

    # layouts distintos — sem repetir foco dentro de nuance
    if layout == 0:
        return f"""# {title}

{meta}

## Contexto

{teoria}

## O que muda aqui

{focus_md}

## Como testo

{steps_md}

{ex}

## Campo

{bank_md}

{fp}

## Já me queimei

{pits}

## Blue

- Detectar: {detect}
- Fechar: {mitigate}

## Evidência

{evidence}

## Refs

{refs}
"""
    if layout == 1:
        return f"""# {title}

`{row['mitre']}`

## Por que importa

{teoria}

## Variante

{focus_md}

## Passo a passo

{steps_md}

{ex}

## Nota de operador

{bank_md}

## Armadilha

{pits}

{fp}

## Depois

Detecção — {detect}

Remediação — {mitigate}

No PDF — {evidence}

## Refs

{refs}
"""
    if layout == 2:
        return f"""# {title}

## Contexto

{teoria}

## Detalhe

{focus_md}

## Execução

{steps_md}

{ex}

## OpSec

{opsec}

## Cuidados

{pits}

## Fechamento

| | |
|---|---|
| Detecção | {detect} |
| Remediação | {mitigate} |
| Evidência | {evidence} |

## Refs

{refs}
"""
    if layout == 3:
        # mais curto
        return f"""# {title}

{meta}

{teoria}

**Variante:** {" ".join(focus)}

**Método**

{steps_md}

{ex}

**Freio:** {pits.split(chr(10))[0]}

{fp}

Detecto via: {detect}

Corrijo com: {mitigate}

Levo no report: {evidence}

Refs: {", ".join(row["refs"])}
"""
    if layout == 4:
        return f"""# {title}

## Leitura rápida

{teoria}

## Foco

{focus_md}

## Mãos na massa

{steps_md}

{ex}

{bank_md}

## Pitfall

{pits}

## Detecção / remediação

{detect}

→ {mitigate}

## Prova

{evidence}

## Refs

{refs}
"""
    # layout 5
    return f"""# {title}

{meta}

## Contexto

{teoria}

## Como eu faço

{steps_md}

{ex}

## Diferencial desta nota

{focus_md}

{fp}

## Onde já errei

{pits}

{bank_md}

## Entrega

- blue: {detect}
- fix: {mitigate}
- proof: {evidence}

## Refs

{refs}
"""


def render_angle(row: dict, titles: dict, angle: str) -> str:
    title = title_for(row, titles)
    h = H(f"{row['fid']}/{row['slug']}/{angle}")
    steps_md = "\n".join(f"{i}. {s}" for i, s in enumerate(steps_of(row), 1))
    focus = row["focus"]
    focus_md = "\n".join(f"- {x}" for x in focus)
    teoria = row["teoria"].strip()
    pits = row["pits"].strip()
    detect = row["detect"].strip()
    mitigate = row["mitigate"].strip()
    evidence = row["evidence"].strip()
    refs = "\n".join(f"- {r}" for r in row["refs"])
    bank = pick_bank(row, 1)[0]
    ex = example_block(row, angle).rstrip()
    # intros variadas por hash — sem clone de ângulo
    if angle == "detecção":
        intros = [
            f"Purple em {title}: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.",
            f"Gap de detecção em `{row['mitre']}` / {title}. PoC mínimo, telemetria ligada.",
            f"Se o SOC não vê {title}, o finding é de cobertura, não de ego ofensivo.",
        ]
        procs = [
            f"1. Janela combinada com blue (ou auto-lab).\n2. Telemetria mínima no ar.\n3. PoC **uma** vez.\n4. MTTD + qualidade do playbook.\n5. Silêncio → gap + esboço de regra amarrado a `{row['mitre']}`.",
            f"1. Confirmo log source relevante.\n2. Disparo o fluxo abaixo.\n3. Anoto alerta / ausência.\n4. Se silêncio, abro finding de detecção.",
            f"Combinar canal → executar → medir. Sem desligar controle pra 'passar'.",
        ]
        return f"""# {title} — detecção

{intros[h % 3]}

## Contexto

{teoria}

## Hipótese

{focus_md}

## Como corro o purple

{procs[h % 3]}

### PoC

{steps_md}

{ex}

## Sinal

{detect}

## Freio

{pits}

{bank}

## Evidência

{evidence}

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

{refs}
"""

    if angle == "lab":
        intros = [
            f"Lab só pra {title}. Se não reproduz isolado, não confio no finding de prod.",
            f"Sandbox throwaway — {title} sem ruído de cliente.",
            f"Critério: outro analista fecha sozinho com esta nota.",
        ]
        mounts = [
            "VM/conta throwaway na versão parecida.\nSnapshot antes.\nCleanup escrito antes de explorar.",
            "Ativo mínimo. Duas identidades se for authz.\nRestore point.",
            "Espelho do alvo. Sem WAF/EDR às vezes — anoto o delta.",
        ]
        return f"""# {title} — lab

{intros[h % 3]}

## Contexto

{teoria}

## Variante

{focus_md}

## Setup

{mounts[h % 3]}

## Fluxo

{steps_md}

{ex}

## Pitfall

{pits}

{bank}

## Prova do lab

{evidence}

## Refs

{refs}
"""

    if angle == "evidência":
        checks = [
            "- ROE cobre\n- ambiente/versão\n- identidade de teste\n- PoC redigido\n- impacto 2–3 frases\n- hotfix + estrutural\n- cleanup\n- MITRE/OWASP",
            "- pré-condição\n- request/comando\n- efeito de negócio\n- CVSS justificado\n- remediação\n- reteste path",
            "Sem pacote completo o finding vira pingue-pongue no reteste.",
        ]
        return f"""# {title} — evidência

Pacote pra {title} sobreviver peer review.

## Contexto

{teoria}

## O que precisa aparecer

{focus_md}

## Checklist

{checks[h % 3]}

## Mínimo que eu aceito

{evidence}

{ex}

## Remediação junto

{mitigate}

## Se purple

{detect}

## Armadilha

{pits}

## Refs

{refs}
"""

    if angle == "path":
        return f"""# {title} — path

{title} como pivô. Path curto > monte de finding isolado.

## Papel

{teoria}

## Por que pivota

{focus_md}

## Cadeia

1. Entrada (escopo)
2. Pivô: {title}
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

{steps_md}

{ex}

## Freio

{pits}

## No caminho

Detectar: {detect}

Remediar: {mitigate}

## Prova

{evidence}

{bank}

## Refs

{refs}
"""

    # hardening
    hfixes = [
        f"Hotfix: quebra a exploração direta de {title}.\nDetectivo: {detect}\nEstrutural: {mitigate}",
        f"1) Bloqueio imediato\n2) {detect}\n3) {mitigate}\nReteste com o mesmo PoC — critério: a prova desta variante falha.",
        f"Controle que fecha: {mitigate}\nSinal que deveria existir: {detect}",
    ]
    return f"""# {title} — hardening

Do PoC ao controle — {title}.

## Risco

{teoria}

## Controles desta variante

{focus_md}

## Camadas

{hfixes[h % 3]}

{ex}

## Armadilha

{pits}

## Antes/depois

{evidence}

Aceite de risco só por escrito, com prazo.

## Refs

{refs}
"""


def build_work(rows: list[dict]) -> list[tuple[dict, str | None]]:
    """380 bases + 620 ângulos equilibrados (124 cada) — mesma ordem do original."""
    bases: list[tuple[dict, str | None]] = [(r, None) for r in rows]
    need = TARGET - len(rows)
    per = need // len(ANGLES)
    rem = need % len(ANGLES)
    seen: set[tuple[str, str, str]] = set()
    angle_slots: list[tuple[dict, str]] = []
    cursor = 0
    for ai, (ang, _) in enumerate(ANGLES):
        n = per + (1 if ai < rem else 0)
        added = 0
        guard = 0
        while added < n and guard < len(rows) * 3:
            r = rows[cursor % len(rows)]
            cursor += 1
            guard += 1
            key = (r["fid"], r["slug"], ang)
            if key in seen:
                continue
            seen.add(key)
            angle_slots.append((r, ang))
            added += 1
    return (bases + [(r, a) for r, a in angle_slots])[:TARGET]


def load_seed() -> tuple[list[dict], dict]:
    rows = json.loads(SEED.read_text())
    titles = json.loads(TITLES.read_text()) if TITLES.exists() else {}
    return rows, titles


def build(out_root: Path) -> list[str]:
    """Renderiza as 1000 notas + índices sob out_root. Retorna os paths relativos."""
    rows, titles = load_seed()
    suf = {a: s for a, s in ANGLES}
    work = build_work(rows)

    out = out_root / "tecnicas"
    idx_dir = out_root / "indice"
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    if idx_dir.exists():
        shutil.rmtree(idx_dir)
    idx_dir.mkdir(parents=True)

    by_cat = {c: [] for c, _ in CATS}
    hashes: set[str] = set()
    written: list[str] = []

    for idx, (row, ang) in enumerate(work, 1):
        if ang is None:
            content = render_base(row, titles)
            suffix = ""
        else:
            content = render_angle(row, titles, ang)
            suffix = suf[ang]
        content = re.sub(r"\n{3,}", "\n\n", content).strip() + "\n"
        content = clean(content)

        digest = hashlib.sha256(content.encode()).hexdigest()
        n = 0
        while digest in hashes:
            n += 1
            content = content.rstrip() + f"\n\n_rev {n}_\n"
            digest = hashlib.sha256(content.encode()).hexdigest()
            if n > 8:
                break
        hashes.add(hashlib.sha256(content.encode()).hexdigest())

        fname = f"{idx:04d}-{row['fid']}-{row['slug']}{suffix}.md"  # suffix já inclui --
        folder = out / row["cat"]
        folder.mkdir(parents=True, exist_ok=True)
        (folder / fname).write_text(content, encoding="utf-8")
        written.append(f"tecnicas/{row['cat']}/{fname}")
        title_line = content.splitlines()[0].lstrip("# ").strip()
        by_cat[row["cat"]].append((idx, title_line, f"tecnicas/{row['cat']}/{fname}"))

    master = [
        "# Índice\n\n",
        "Caderno de pentest autorizado — **Alexandre Riuti Wada**.\n\n",
        "[Aviso](../DISCLAIMER.md)\n\n",
    ]
    for cat, name in CATS:
        master.append(f"- [{name}]({cat}.md)\n")
        lines = [f"# {name}\n\n"]
        for i, title, rel in by_cat[cat]:
            lines.append(f"- [{i:04d} — {title}](../{rel})\n")
        (idx_dir / f"{cat}.md").write_text("".join(lines), encoding="utf-8")
    (idx_dir / "README.md").write_text("".join(master), encoding="utf-8")

    assert len(list(out.rglob("*.md"))) == TARGET
    return written


ANGLE_SUFFIX_RE = re.compile(r"--(detecao|lab|evidencia|path|hardening)\.md$")


def key_of(rel: str) -> str:
    """Chave estável fid/slug[/ângulo] — ignora o número sequencial."""
    name = Path(rel).name[:-3]
    return name[5:] if re.match(r"^\d{4}-", name) else name


def check() -> int:
    """Gate de fidelidade: renderiza em tmp e compara com tecnicas/ por chave."""
    tmp = Path(tempfile.mkdtemp(prefix="caderno-check-"))
    build(tmp)

    current = {key_of(str(p.relative_to(ROOT / "tecnicas"))): p for p in (ROOT / "tecnicas").rglob("*.md")}
    rendered = {key_of(str(p.relative_to(tmp / "tecnicas"))): p for p in (tmp / "tecnicas").rglob("*.md")}

    missing = sorted(set(current) - set(rendered))
    extra = sorted(set(rendered) - set(current))
    if missing:
        print(f"ERRO: {len(missing)} notas atuais sem correspondente renderizado, ex.: {missing[:3]}")
    if extra:
        print(f"ERRO: {len(extra)} notas renderizadas a mais, ex.: {extra[:3]}")

    ratios: dict[str, float] = {}
    for k in sorted(set(current) & set(rendered)):
        a = current[k].read_text()
        b = rendered[k].read_text()
        ratios[k] = 1.0 if a == b else difflib.SequenceMatcher(None, a, b).ratio()

    vals = sorted(ratios.values())
    below = {k: v for k, v in ratios.items() if v < 0.90}
    p95 = vals[int(len(vals) * 0.95)] if vals else 0.0
    print(f"fidelidade: n={len(vals)} min={vals[0]:.4f} mediana={statistics.median(vals):.4f} p95={p95:.4f}")
    print(f"idênticos: {sum(1 for v in vals if v == 1.0)}/{len(vals)}")
    print(f"abaixo de 0.90: {len(below)}")
    for k, v in sorted(below.items(), key=lambda kv: kv[1])[:25]:
        print(f"  {v:.4f} {k}")
    if below:
        worst = min(below, key=below.get)
        a = current[worst].read_text().splitlines()
        b = rendered[worst].read_text().splitlines()
        print(f"--- diff exemplo ({worst}) ---")
        for ln in list(difflib.unified_diff(a, b, lineterm=""))[:40]:
            print(ln)

    audit_tmp = tmp / "_build"
    audit_tmp.mkdir()
    shutil.copy(HERE / "audit_anti_ia.py", audit_tmp / "audit_anti_ia.py")
    r = subprocess.run([sys.executable, str(audit_tmp / "audit_anti_ia.py")], cwd=tmp, capture_output=True, text=True)
    print("--- audit_anti_ia (notas renderizadas) ---")
    print(r.stdout.strip())
    if r.returncode != 0:
        print(r.stderr.strip())
    ok = not missing and not extra and not below and r.returncode == 0
    print("CHECK", "PASS" if ok else "FAIL", f"(tmp: {tmp})")
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="Renderiza o caderno a partir de _build/seed.json")
    ap.add_argument("--out", type=Path, default=ROOT, help="raiz de saída (default: repo)")
    ap.add_argument("--check", action="store_true", help="gate de fidelidade em diretório temporário")
    args = ap.parse_args()
    if args.check:
        return check()
    written = build(args.out.resolve())
    print("OK", len(written), "notas em", args.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
