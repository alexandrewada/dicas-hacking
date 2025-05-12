# Atomic Red Team na prática — evidência

Pacote pra Atomic Red Team na prática sobreviver peer review.

## Contexto

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## O que precisa aparecer

- Variante Atomic Red Team mapping: trato separado da família `purple-detect`.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Matriz técnica→alerta; screenshots SIEM; recomendações.

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: e65918

{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","owner":"USER_A","note":"redacted-atomic"}
# capturado como USER_B
```

## Remediação junto

Fechar gaps com rules; data sources faltantes; tuning.

## Se purple

Métricas de cobertura ATT&CK; mean time to alert.

## Armadilha

Não desabilito EDR para 'passar'. Documento bypass se no escopo.

## Refs

- MITRE ATT&CK
- Atomic Red Team