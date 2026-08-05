---
id: "0341"
categoria: "18-evasion"
familia: "purple-detect"
slug: "atomic"
angulo: "base"
mitre: ""
owasp: ""
tags: ["18-evasion", "purple-detect", "base"]
aliases: ["Atomic Red Team na prática", "atomic"]
---

# Atomic Red Team na prática

`Detection engineering`

## Por que importa

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## Variante

- Variante Atomic Red Team mapping: trato separado da família `purple-detect`.

## Passo a passo

1. Selecionar técnicas do escopo.
2. Garantir logging baseline (Sysmon/EDR/CloudTrail).
3. Executar PoC controlado.
4. Verifico alerta; classificar gap.
5. Entregar detection ideas (pseudo-rule).

## Exemplo

```yaml
title: Purple atomic
logsource:
  product: windows
detection:
  selection:
    EventID: 1
    CommandLine|contains: 'a6361e'
  condition: selection
# atomic atomic — uma execução limpa
```

## Nota de operador

Sigma/KQL amarrado ao MITRE da técnica — 'suspicious powershell' genérico não conta.

## Armadilha

Não desabilito EDR para 'passar'. Documento bypass se no escopo.

Atomic Red Team mapping: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Métricas de cobertura ATT&CK; mean time to alert.

## Depois

Detecção — Métricas de cobertura ATT&CK; mean time to alert.

Remediação — Fechar gaps com rules; data sources faltantes; tuning.

No PDF — Matriz técnica→alerta; screenshots SIEM; recomendações.

## Refs

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [SigmaHQ rules](https://github.com/SigmaHQ/sigma)

## Relacionadas

- [Atomic Red Team na prática — evidência](0721-purple-detect-atomic--evidencia.md)
- [canary tokens validation](0349-purple-detect-canary.md)
- [CloudTrail gaps](0345-purple-detect-cloudtrail.md)
- [DNS anomaly detection test](0346-purple-detect-dns-dga.md)
- [EDR bypass discussion ética](0343-purple-detect-edr-bypass.md)
- [sugerir regra Sigma (path)](0344-purple-detect-sigma.md)
- [Sysmon coverage gaps (path)](0342-purple-detect-sysmon.md)