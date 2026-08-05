---
id: "0350"
categoria: "18-evasion"
familia: "purple-detect"
slug: "score"
angulo: "base"
mitre: ""
owasp: ""
tags: ["18-evasion", "purple-detect", "base"]
aliases: ["scoring de maturidade SOC", "score"]
---

# scoring de maturidade SOC

**Purple Team** · `Detection engineering`

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

**Variante:** Variante scoring de maturidade SOC: trato separado da família `purple-detect`.

**Método**

1. Selecionar técnicas do escopo.
2. Garantir logging baseline (Sysmon/EDR/CloudTrail).
3. Executar PoC controlado.
4. Verifico alerta; classificar gap.
5. Entregar detection ideas (pseudo-rule).

## Sinal / query

```yaml
title: Purple score
logsource:
  product: windows
detection:
  selection:
    EventID: 1
    CommandLine|contains: '8f3ec1'
  condition: selection
# atomic score — uma execução limpa
```

**Freio:** Não desabilito EDR para 'passar'. Documento bypass se no escopo.

Já abri High demais em scoring de maturidade SOC por sintoma sem efeito. Cruzei com: Métricas de cobertura ATT&CK; mean time to alert. Sem side-effect, baixo.

Detecto via: Métricas de cobertura ATT&CK; mean time to alert.

Corrijo com: Fechar gaps com rules; data sources faltantes; tuning.

Levo no report: Matriz técnica→alerta; screenshots SIEM; recomendações.

## Refs

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [SigmaHQ rules](https://github.com/SigmaHQ/sigma)

## Relacionadas

- [scoring de maturidade SOC — evidência](0730-purple-detect-score--evidencia.md)
- [Atomic Red Team na prática](0341-purple-detect-atomic.md)
- [canary tokens validation](0349-purple-detect-canary.md)
- [CloudTrail gaps](0345-purple-detect-cloudtrail.md)
- [DNS anomaly detection test](0346-purple-detect-dns-dga.md)