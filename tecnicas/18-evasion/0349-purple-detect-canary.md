# canary tokens validation

## Contexto

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## Detalhe

- Variante canary tokens validation: trato separado da família `purple-detect`.

## Execução

1. Selecionar técnicas do escopo.
2. Garantir logging baseline (Sysmon/EDR/CloudTrail).
3. Executar PoC controlado.
4. Verifico alerta; classificar gap.
5. Entregar detection ideas (pseudo-rule).

## Exemplo

```yaml
title: Purple canary
logsource:
  product: windows
detection:
  selection:
    EventID: 1
    CommandLine|contains: '9efb3e'
  condition: selection
# atomic canary — uma execução limpa
```

## OpSec

Sigma/KQL amarrado ao MITRE da técnica — 'suspicious powershell' genérico não conta.

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