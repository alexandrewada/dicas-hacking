---
id: "0718"
categoria: "17-redteam"
familia: "rt-c2"
slug: "lateral"
angulo: "evidencia"
mitre: "T1071"
owasp: ""
tags: ["17-redteam", "rt-c2", "evidencia", "t1071"]
aliases: ["lateral com credenciais de engajamento", "lateral", "lateral-evidencia"]
---

# lateral com credenciais de engajamento — evidência

Pacote pra lateral com credenciais de engajamento sobreviver peer review.

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## O que precisa aparecer

- Variante lateral com credenciais de engajamento: trato separado da família `rt-c2`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Diagrama de infra; IOCs entregues ao blue; timeline.

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: a1d327

{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","owner":"USER_A","note":"redacted-lateral"}
# capturado como USER_B
```

## Remediação junto

Allowlist egress; TLS inspection onde adequado; DNS control.

## Se purple

CDN/proxy anomalies; beacon jitter patterns; JA3.

## Armadilha

Não uso infra de C2 criminal. Não aponte para fora do escopo.

## Refs

- [MITRE ATT&CK T1071](https://attack.mitre.org/techniques/T1071/)
- [Red team ethics / ROE](https://attack.mitre.org/)
- [MITRE ATT&CK — Command and Control](https://attack.mitre.org/tactics/TA0011/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)

## Relacionadas

- [lateral com credenciais de engajamento](0338-rt-c2-lateral.md)
- [debrief com SOC](0340-rt-c2-debrief.md)
- [DNS C2](0332-rt-c2-dns.md)
- [domain fronting histórico](0333-rt-c2-domain-front.md)
- [exfil controlada de dados fake](0339-rt-c2-exfil.md)