# payload staging ético — evidência

Pacote pra payload staging ético sobreviver peer review.

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## O que precisa aparecer

- **Code signing labs** — muda ruído e o que entra no PDF.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Diagrama de infra; IOCs entregues ao blue; timeline.

## PoC mínimo

```text
--- evidência redigida ---
req: GET /…/usr_01HZX Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (payload)
hash_prova: 065462
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