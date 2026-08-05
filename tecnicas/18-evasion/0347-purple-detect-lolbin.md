---
id: "0347"
categoria: "18-evasion"
familia: "purple-detect"
slug: "lolbin"
angulo: "base"
mitre: ""
owasp: ""
tags: ["18-evasion", "purple-detect", "base"]
aliases: ["LOLBin detection", "lolbin"]
---

# LOLBin detection

**Purple Team** · `Detection engineering`

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

**Variante:** Variante LOLBin detection: trato separado da família `purple-detect`.

**Método**

1. Selecionar técnicas do escopo.
2. Garantir logging baseline (Sysmon/EDR/CloudTrail).
3. Executar PoC controlado.
4. Verifico alerta; classificar gap.
5. Entregar detection ideas (pseudo-rule).

## No lab ficou assim

```yaml
title: Purple lolbin
logsource:
  product: windows
detection:
  selection:
    EventID: 1
    CommandLine|contains: '71dbfa'
  condition: selection
# atomic lolbin — uma execução limpa
```

**Freio:** Não desabilito EDR para 'passar'. Documento bypass se no escopo.

Falso amigo em LOLBin detection: UI/log gritam, impacto não. Exijo Métricas de cobertura ATT&CK.

Detecto via: Métricas de cobertura ATT&CK; mean time to alert.

Corrijo com: Fechar gaps com rules; data sources faltantes; tuning.

Levo no report: Matriz técnica→alerta; screenshots SIEM; recomendações.

## Refs

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [SigmaHQ rules](https://github.com/SigmaHQ/sigma)

## Relacionadas

- [LOLBin detection — evidência](0727-purple-detect-lolbin--evidencia.md)
- [Atomic Red Team na prática](0341-purple-detect-atomic.md)
- [canary tokens validation](0349-purple-detect-canary.md)
- [CloudTrail gaps](0345-purple-detect-cloudtrail.md)
- [DNS anomaly detection test](0346-purple-detect-dns-dga.md)