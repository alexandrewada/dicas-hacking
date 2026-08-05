---
id: "0332"
categoria: "17-redteam"
familia: "rt-c2"
slug: "dns"
angulo: "base"
mitre: "T1071"
owasp: ""
tags: ["17-redteam", "rt-c2", "base", "t1071"]
aliases: ["DNS C2", "dns"]
---

# DNS C2

**Red Team** · `T1071 Application Layer Protocol`

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

**Variante:** **Somente se permitido** — muda ruído e o que entra no PDF.

**Método**

1. Definir canais permitidos (HTTPS, DNS, etc.).
2. Infra com segregação e burndown plan.
3. Payloads assinados apenas em alvos autorizados.
4. Telemetria mínima necessária para objetivos.
5. Desmobilizar infra ao final.

## Exemplo

```bash
# C2 lab — kill-switch e janela
curl -sk https://c2.lab.local/dns/beacon -H 'X-Session: 467cfa'
# só conta teste; sem persistência fora do ROE
```

**Freio:** Não uso infra de C2 criminal. Não aponte para fora do escopo.

DNS C2: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: CDN/proxy anomalies; beacon jitter patterns; JA3.

Detecto via: CDN/proxy anomalies; beacon jitter patterns; JA3.

Corrijo com: Allowlist egress; TLS inspection onde adequado; DNS control.

Levo no report: Diagrama de infra; IOCs entregues ao blue; timeline.

## Refs

- [MITRE ATT&CK T1071](https://attack.mitre.org/techniques/T1071/)
- [Red team ethics / ROE](https://attack.mitre.org/)
- [MITRE ATT&CK — Command and Control](https://attack.mitre.org/tactics/TA0011/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)

## Relacionadas

- [DNS C2 — evidência](0712-rt-c2-dns--evidencia.md)
- [debrief com SOC](0340-rt-c2-debrief.md)
- [domain fronting histórico](0333-rt-c2-domain-front.md)
- [exfil controlada de dados fake](0339-rt-c2-exfil.md)
- [HTTPS beaconing](0331-rt-c2-https.md)