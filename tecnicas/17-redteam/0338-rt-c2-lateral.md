---
id: "0338"
categoria: "17-redteam"
familia: "rt-c2"
slug: "lateral"
angulo: "base"
mitre: "T1071"
owasp: ""
tags: ["17-redteam", "rt-c2", "base", "t1071"]
aliases: ["lateral com credenciais de engajamento", "lateral"]
---

# lateral com credenciais de engajamento

**Red Team** · `T1071 Application Layer Protocol`

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## Como eu faço

1. Definir canais permitidos (HTTPS, DNS, etc.).
2. Infra com segregação e burndown plan.
3. Payloads assinados apenas em alvos autorizados.
4. Telemetria mínima necessária para objetivos.
5. Desmobilizar infra ao final.

## No lab ficou assim

```bash
# C2 lab — kill-switch e janela
curl -sk https://c2.lab.local/lateral/beacon -H 'X-Session: 90dd28'
# só conta teste; sem persistência fora do ROE
```

## Diferencial desta nota

- Variante lateral com credenciais de engajamento: trato separado da família `rt-c2`.

Antes de Critical em lateral com credenciais de engajamento, confiro se a telemetria que eu cobraria reagiria — CDN/proxy anomalies; beacon jitter patterns; JA3.

## Onde já errei

Não uso infra de C2 criminal. Não aponte para fora do escopo.

Timeline + decisões de não-exploração pesam no report.

## Entrega

- blue: CDN/proxy anomalies; beacon jitter patterns; JA3.
- fix: Allowlist egress; TLS inspection onde adequado; DNS control.
- proof: Diagrama de infra; IOCs entregues ao blue; timeline.

## Refs

- [MITRE ATT&CK T1071](https://attack.mitre.org/techniques/T1071/)
- [Red team ethics / ROE](https://attack.mitre.org/)
- [MITRE ATT&CK — Command and Control](https://attack.mitre.org/tactics/TA0011/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)

## Relacionadas

- [lateral com credenciais de engajamento — evidência](0718-rt-c2-lateral--evidencia.md)
- [debrief com SOC](0340-rt-c2-debrief.md)
- [DNS C2](0332-rt-c2-dns.md)
- [domain fronting histórico](0333-rt-c2-domain-front.md)
- [exfil controlada de dados fake](0339-rt-c2-exfil.md)