---
id: "0343"
categoria: "18-evasion"
familia: "purple-detect"
slug: "edr-bypass"
angulo: "base"
mitre: ""
owasp: ""
tags: ["18-evasion", "purple-detect", "base"]
aliases: ["EDR bypass discussion ética", "edr-bypass"]
---

# EDR bypass discussion ética

**Purple Team** · `Detection engineering`

## Contexto

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## O que muda aqui

- Detalhe que pago pra ver: **Sem malware crimeware**.

## Como testo

1. Selecionar técnicas do escopo.
2. Garantir logging baseline (Sysmon/EDR/CloudTrail).
3. Executar PoC controlado.
4. Verifico alerta; classificar gap.
5. Entregar detection ideas (pseudo-rule).

## PoC mínimo

```yaml
title: Purple edr-bypass
logsource:
  product: windows
detection:
  selection:
    EventID: 1
    CommandLine|contains: '5d5723'
  condition: selection
# atomic edr-bypass — uma execução limpa
```

## Campo

Uma execução limpa, telemetria ligada: alertou? Silêncio = finding de gap.

Falso amigo em EDR bypass discussion ética: UI/log gritam, impacto não. Exijo Métricas de cobertura ATT&CK.

## Já me queimei

Não desabilito EDR para 'passar'. Documento bypass se no escopo.

## Blue

- Detectar: Métricas de cobertura ATT&CK; mean time to alert.
- Fechar: Fechar gaps com rules; data sources faltantes; tuning.

## Evidência

Matriz técnica→alerta; screenshots SIEM; recomendações.

## Refs

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [SigmaHQ rules](https://github.com/SigmaHQ/sigma)

## Relacionadas

- [EDR bypass discussion ética — evidência](0723-purple-detect-edr-bypass--evidencia.md)
- [Atomic Red Team na prática](0341-purple-detect-atomic.md)
- [canary tokens validation](0349-purple-detect-canary.md)
- [CloudTrail gaps](0345-purple-detect-cloudtrail.md)
- [DNS anomaly detection test](0346-purple-detect-dns-dga.md)