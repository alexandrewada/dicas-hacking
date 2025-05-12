# sugerir regra Sigma

**Purple Team** · `Detection engineering`

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

**Variante:** Detalhe que pago pra ver: **Entrega defensiva**.

**Método**

1. Selecionar técnicas do escopo.
2. Garantir logging baseline (Sysmon/EDR/CloudTrail).
3. Executar PoC controlado.
4. Verifico alerta; classificar gap.
5. Entregar detection ideas (pseudo-rule).

## Sinal / query

```yaml
title: Purple sigma
logsource:
  product: windows
detection:
  selection:
    EventID: 1
    CommandLine|contains: '467e67'
  condition: selection
# atomic sigma — uma execução limpa
```

**Freio:** Não desabilito EDR para 'passar'. Documento bypass se no escopo.

Falso amigo em sugerir regra Sigma: UI/log gritam, impacto não. Exijo Métricas de cobertura ATT&CK.

Detecto via: Métricas de cobertura ATT&CK; mean time to alert.

Corrijo com: Fechar gaps com rules; data sources faltantes; tuning.

Levo no report: Matriz técnica→alerta; screenshots SIEM; recomendações.

Refs: MITRE ATT&CK, Atomic Red Team