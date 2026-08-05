---
id: "0348"
categoria: "18-evasion"
familia: "purple-detect"
slug: "ransomware-sim"
angulo: "base"
mitre: ""
owasp: ""
tags: ["18-evasion", "purple-detect", "base"]
aliases: ["ransomware simulation safe", "ransomware-sim"]
---

# ransomware simulation safe

`Detection engineering`

## Por que importa

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## Variante

- **Somente lab.** Sem isso o playbook da família mente.

## Passo a passo

1. Selecionar técnicas do escopo.
2. Garantir logging baseline (Sysmon/EDR/CloudTrail).
3. Executar PoC controlado.
4. Verifico alerta; classificar gap.
5. Entregar detection ideas (pseudo-rule).

## Sinal / query

```yaml
title: Purple ransomware-sim
logsource:
  product: windows
detection:
  selection:
    EventID: 1
    CommandLine|contains: 'c89a12'
  condition: selection
# atomic ransomware-sim — uma execução limpa
```

## Nota de operador

Não desligo EDR pra passar. Bypass documentado é produto separado.

## Armadilha

Não desabilito EDR para 'passar'. Documento bypass se no escopo.

Já abri High demais em ransomware simulation safe por sintoma sem efeito. Cruzei com: Métricas de cobertura ATT&CK; mean time to alert. Sem side-effect, baixo.

## Depois

Detecção — Métricas de cobertura ATT&CK; mean time to alert.

Remediação — Fechar gaps com rules; data sources faltantes; tuning.

No PDF — Matriz técnica→alerta; screenshots SIEM; recomendações.

## Refs

- [MITRE ATT&CK](https://attack.mitre.org/)
- [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team)
- [SigmaHQ rules](https://github.com/SigmaHQ/sigma)

## Relacionadas

- [ransomware simulation safe — evidência](0728-purple-detect-ransomware-sim--evidencia.md)
- [Atomic Red Team na prática](0341-purple-detect-atomic.md)
- [canary tokens validation](0349-purple-detect-canary.md)
- [CloudTrail gaps](0345-purple-detect-cloudtrail.md)
- [DNS anomaly detection test](0346-purple-detect-dns-dga.md)