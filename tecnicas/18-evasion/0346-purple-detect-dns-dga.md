---
id: "0346"
categoria: "18-evasion"
familia: "purple-detect"
slug: "dns-dga"
angulo: "base"
mitre: ""
owasp: ""
tags: ["18-evasion", "purple-detect", "base"]
aliases: ["DNS anomaly detection test", "dns-dga"]
---

# DNS anomaly detection test

**Purple Team** · `Detection engineering`

## Contexto

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## Como eu faço

1. Selecionar técnicas do escopo.
2. Garantir logging baseline (Sysmon/EDR/CloudTrail).
3. Executar PoC controlado.
4. Verifico alerta; classificar gap.
5. Entregar detection ideas (pseudo-rule).

## No lab ficou assim

```yaml
title: Purple dns-dga
logsource:
  product: windows
detection:
  selection:
    EventID: 1
    CommandLine|contains: '8736dd'
  condition: selection
# atomic dns-dga — uma execução limpa
```

## Diferencial desta nota

- Variante DNS anomaly detection test: trato separado da família `purple-detect`.

Antes de Critical em DNS anomaly detection test, confiro se a telemetria que eu cobraria reagiria — Métricas de cobertura ATT&CK; mean time to alert.

## Onde já errei

Não desabilito EDR para 'passar'. Documento bypass se no escopo.

Sigma/KQL amarrado ao MITRE da técnica — 'suspicious powershell' genérico não conta.

## Entrega

- blue: Métricas de cobertura ATT&CK; mean time to alert.
- fix: Fechar gaps com rules; data sources faltantes; tuning.
- proof: Matriz técnica→alerta; screenshots SIEM; recomendações.

## Refs

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [SigmaHQ rules](https://github.com/SigmaHQ/sigma)

## Relacionadas

- [DNS anomaly detection test — evidência](0726-purple-detect-dns-dga--evidencia.md)
- [Atomic Red Team na prática](0341-purple-detect-atomic.md)
- [canary tokens validation](0349-purple-detect-canary.md)
- [CloudTrail gaps](0345-purple-detect-cloudtrail.md)
- [EDR bypass discussion ética](0343-purple-detect-edr-bypass.md)