# Sysmon coverage gaps

## Contexto

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## Detalhe

- Variante Sysmon coverage gaps: trato separado da família `purple-detect`.

## Execução

1. Selecionar técnicas do escopo.
2. Garantir logging baseline (Sysmon/EDR/CloudTrail).
3. Executar PoC controlado.
4. Verifico alerta; classificar gap.
5. Entregar detection ideas (pseudo-rule).

## No lab ficou assim

```yaml
title: Purple sysmon
logsource:
  product: windows
detection:
  selection:
    EventID: 1
    CommandLine|contains: 'e6550b'
  condition: selection
# atomic sysmon — uma execução limpa
```

## OpSec

Não desabilito EDR para 'passar'. Documento bypass se no escopo. Uma execução limpa, telemetria ligada: alertou? Silêncio = finding de gap.

## Cuidados

Não desabilito EDR para 'passar'. Documento bypass se no escopo.

## Fechamento

| | |
|---|---|
| Detecção | Métricas de cobertura ATT&CK; mean time to alert. |
| Remediação | Fechar gaps com rules; data sources faltantes; tuning. |
| Evidência | Matriz técnica→alerta; screenshots SIEM; recomendações. |

## Refs

- MITRE ATT&CK
- Atomic Red Team