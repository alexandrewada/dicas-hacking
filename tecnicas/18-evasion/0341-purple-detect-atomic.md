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

- MITRE ATT&CK
- Atomic Red Team