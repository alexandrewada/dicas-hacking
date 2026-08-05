---
id: "0717"
categoria: "17-redteam"
familia: "rt-c2"
slug: "lolbins"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["17-redteam", "rt-c2", "evidencia"]
aliases: ["LOLBins para living-off-land", "lolbins", "lolbins-evidencia"]
---

# LOLBins para living-off-land — evidência

Pacote pra LOLBins para living-off-land sobreviver peer review.

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## O que precisa aparecer

- Se não validar **Detecção**, a nota fica genérica.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Diagrama de infra; IOCs entregues ao blue; timeline.

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 569ac1

{"id":"usr_01HZX","owner":"USER_A","note":"redacted-lolbins"}
# capturado como USER_B
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

- [LOLBins para living-off-land](0337-rt-c2-lolbins.md)
- [debrief com SOC](0340-rt-c2-debrief.md)
- [DNS C2](0332-rt-c2-dns.md)
- [domain fronting histórico](0333-rt-c2-domain-front.md)
- [exfil controlada de dados fake](0339-rt-c2-exfil.md)