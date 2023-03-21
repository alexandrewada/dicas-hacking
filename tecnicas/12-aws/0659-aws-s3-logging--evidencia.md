# access logs públicos — evidência

Pacote pra access logs públicos sobreviver peer review.

## Contexto

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

## O que precisa aparecer

- Se não validar **Meta-leak**, a nota fica genérica.
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

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: e7ddb2

{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","owner":"USER_A","note":"redacted-logging"}
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