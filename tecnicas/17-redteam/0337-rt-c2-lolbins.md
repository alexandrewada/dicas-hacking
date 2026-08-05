---
id: "0337"
categoria: "17-redteam"
familia: "rt-c2"
slug: "lolbins"
angulo: "base"
mitre: ""
owasp: ""
tags: ["17-redteam", "rt-c2", "base"]
aliases: ["LOLBins para living-off-land", "lolbins"]
---

# LOLBins para living-off-land

## Leitura rápida

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## Foco

- Se não validar **Detecção**, a nota fica genérica.

## Mãos na massa

1. Definir canais permitidos (HTTPS, DNS, etc.).
2. Infra com segregação e burndown plan.
3. Payloads assinados apenas em alvos autorizados.
4. Telemetria mínima necessária para objetivos.
5. Desmobilizar infra ao final.

## Sinal / query

```bash
# C2 lab — kill-switch e janela
curl -sk https://c2.lab.local/lolbins/beacon -H 'X-Session: 91c405'
# só conta teste; sem persistência fora do ROE
```

Timeline + decisões de não-exploração pesam no report.

## Pitfall

Não uso infra de C2 criminal. Não aponte para fora do escopo.

## Detecção / remediação

CDN/proxy anomalies; beacon jitter patterns; JA3.

→ Allowlist egress; TLS inspection onde adequado; DNS control.

## Prova

Diagrama de infra; IOCs entregues ao blue; timeline.

## Refs

- [Red team ethics / ROE](https://attack.mitre.org/)
- [MITRE ATT&CK — Command and Control](https://attack.mitre.org/tactics/TA0011/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)

## Relacionadas

- [LOLBins para living-off-land — evidência](0717-rt-c2-lolbins--evidencia.md)
- [debrief com SOC](0340-rt-c2-debrief.md)
- [DNS C2](0332-rt-c2-dns.md)
- [domain fronting histórico](0333-rt-c2-domain-front.md)
- [exfil controlada de dados fake](0339-rt-c2-exfil.md)