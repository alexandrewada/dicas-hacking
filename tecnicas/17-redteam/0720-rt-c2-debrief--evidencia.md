# debrief com SOC — evidência

Pacote pra debrief com SOC sobreviver peer review.

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## O que precisa aparecer

- **Lições learned** — muda ruído e o que entra no PDF.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Diagrama de infra; IOCs entregues ao blue; timeline.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 424371

{"id":"usr_01HZX","owner":"USER_A","note":"redacted-debrief"}
# capturado como USER_B
```

## Remediação junto

Allowlist egress; TLS inspection onde adequado; DNS control.

## Se purple

CDN/proxy anomalies; beacon jitter patterns; JA3.

## Armadilha

Não uso infra de C2 criminal. Não aponte para fora do escopo.

## Refs

- Red Team Field Manual ethics
- MITRE C2