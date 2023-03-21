# replication para conta externa — evidência

Pacote pra replication para conta externa sobreviver peer review.

## Contexto

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

## O que precisa aparecer

- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

URL/policy; amostra redigida; screenshot console se fornecido.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: b7cd7f

{"id":"ORD-7781","owner":"USER_A","note":"redacted-replication"}
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