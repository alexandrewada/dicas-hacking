# Takeover de bucket DNS — evidência

Pacote pra Takeover de bucket DNS sobreviver peer review.

## Contexto

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

## O que precisa aparecer

- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.
- Recurso claimável + prova de controle (arquivo/challenge). Sem claim, não é Critical.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

URL/policy; amostra redigida; screenshot console se fornecido.

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 89d747

{"id":"obj_89d747","owner":"USER_A","note":"redacted-takeover"}
# capturado como USER_B
```

## Remediação junto

Block Public Access; least privilege policies; encryption; access logs.

## Se purple

CloudTrail data events; Macie; public access block alerts.

## Armadilha

Não baixe datasets inteiros de PII — evidência mínima.

## Refs

- AWS S3 security best practices