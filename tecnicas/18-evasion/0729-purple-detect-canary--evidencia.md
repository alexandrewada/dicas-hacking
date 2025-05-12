# canary tokens validation — evidência

Pacote pra canary tokens validation sobreviver peer review.

## Contexto

Purple team de qualidade executa técnicas com telemetria pré-combinada e mede
cobertura (True Positive, gap, alerta que não veio). O entregável de valor é a
matriz ATT&CK + evidência de alerta — não apenas a execução do payload.

## O que precisa aparecer

- Variante canary tokens validation: trato separado da família `purple-detect`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Matriz técnica→alerta; screenshots SIEM; recomendações.

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 741e51

{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","owner":"USER_A","note":"redacted-canary"}
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