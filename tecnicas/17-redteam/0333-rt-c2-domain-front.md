---
id: "0333"
categoria: "17-redteam"
familia: "rt-c2"
slug: "domain-front"
angulo: "base"
mitre: "T1071"
owasp: ""
tags: ["17-redteam", "rt-c2", "base", "t1071"]
aliases: ["domain fronting histórico", "domain-front"]
---

# domain fronting histórico

**Red Team** · `T1071 Application Layer Protocol`

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## O que muda aqui

- **Status atual/limites.** Sem isso o playbook da família mente.

## Como testo

1. Definir canais permitidos (HTTPS, DNS, etc.).
2. Infra com segregação e burndown plan.
3. Payloads assinados apenas em alvos autorizados.
4. Telemetria mínima necessária para objetivos.
5. Desmobilizar infra ao final.

## PoC mínimo

```bash
# C2 lab — kill-switch e janela
curl -sk https://c2.lab.local/domain-front/beacon -H 'X-Session: 8a0e6f'
# só conta teste; sem persistência fora do ROE
```

## Campo

C2/persistência com kill-switch e janela. Beacon sem objetivo é ego.

Falso amigo em domain fronting histórico: UI/log gritam, impacto não. Exijo CDN/proxy anomalies.

## Já me queimei

Não uso infra de C2 criminal. Não aponte para fora do escopo.

## Blue

- Detectar: CDN/proxy anomalies; beacon jitter patterns; JA3.
- Fechar: Allowlist egress; TLS inspection onde adequado; DNS control.

## Evidência

Diagrama de infra; IOCs entregues ao blue; timeline.

## Refs

- [MITRE ATT&CK T1071](https://attack.mitre.org/techniques/T1071/)
- [Red team ethics / ROE](https://attack.mitre.org/)
- [MITRE ATT&CK — Command and Control](https://attack.mitre.org/tactics/TA0011/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)

## Relacionadas

- [domain fronting histórico — evidência](0713-rt-c2-domain-front--evidencia.md)
- [debrief com SOC](0340-rt-c2-debrief.md)
- [DNS C2](0332-rt-c2-dns.md)
- [exfil controlada de dados fake](0339-rt-c2-exfil.md)
- [HTTPS beaconing](0331-rt-c2-https.md)