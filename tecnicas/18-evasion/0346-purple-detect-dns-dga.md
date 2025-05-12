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

- MITRE ATT&CK
- Atomic Red Team