---
id: "0711"
categoria: "17-redteam"
familia: "rt-c2"
slug: "https"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["17-redteam", "rt-c2", "evidencia"]
aliases: ["HTTPS beaconing", "https", "https-evidencia"]
---

# HTTPS beaconing — evidência

Pacote pra HTTPS beaconing sobreviver peer review.

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## O que precisa aparecer

- **Jitter e CDN front.** Sem isso o playbook da família mente.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Diagrama de infra; IOCs entregues ao blue; timeline.

## PoC mínimo

```text
--- evidência redigida ---
req: GET /…/a1b2c3d4-e5f6-7890-abcd-ef1234567890 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (https)
hash_prova: 1b0921
```

## Remediação junto

Allowlist egress; TLS inspection onde adequado; DNS control.

## Se purple

CDN/proxy anomalies; beacon jitter patterns; JA3.

## Armadilha

Não uso infra de C2 criminal. Não aponte para fora do escopo.

## Refs

- [Red team ethics / ROE](https://attack.mitre.org/)
- [MITRE ATT&CK — Command and Control](https://attack.mitre.org/tactics/TA0011/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)

## Relacionadas

- [HTTPS beaconing](0331-rt-c2-https.md)
- [debrief com SOC](0340-rt-c2-debrief.md)
- [DNS C2](0332-rt-c2-dns.md)
- [domain fronting histórico](0333-rt-c2-domain-front.md)
- [exfil controlada de dados fake](0339-rt-c2-exfil.md)
- [sugerir regra Sigma (path)](../18-evasion/0344-purple-detect-sigma.md)
- [Kill-switch de C2 (path)](0335-rt-c2-killswitch.md)