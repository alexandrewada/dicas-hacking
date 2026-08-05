---
id: "0334"
categoria: "17-redteam"
familia: "rt-c2"
slug: "redirector"
angulo: "base"
mitre: "T1071"
owasp: ""
tags: ["17-redteam", "rt-c2", "base", "t1071"]
aliases: ["redirectors e OPSEC", "redirector"]
---

# redirectors e OPSEC

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

## PoC mínimo

```bash
# C2 lab — kill-switch e janela
curl -sk https://c2.lab.local/redirector/beacon -H 'X-Session: 122547'
# só conta teste; sem persistência fora do ROE
```

## Diferencial desta nota

- Variante redirectors e OPSEC: trato separado da família `rt-c2`.

Já abri High demais em redirectors e OPSEC por sintoma sem efeito. Cruzei com: CDN/proxy anomalies; beacon jitter patterns; JA3. Sem side-effect, baixo.

## Onde já errei

Não uso infra de C2 criminal. Não aponte para fora do escopo.

C2/persistência com kill-switch e janela. Beacon sem objetivo é ego.

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

- [redirectors e OPSEC — evidência](0714-rt-c2-redirector--evidencia.md)
- [debrief com SOC](0340-rt-c2-debrief.md)
- [DNS C2](0332-rt-c2-dns.md)
- [domain fronting histórico](0333-rt-c2-domain-front.md)
- [exfil controlada de dados fake](0339-rt-c2-exfil.md)