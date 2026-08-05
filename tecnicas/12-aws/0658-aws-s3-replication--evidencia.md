---
id: "0658"
categoria: "12-aws"
familia: "aws-s3"
slug: "replication"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["12-aws", "aws-s3", "evidencia"]
aliases: ["replication para conta externa", "replication", "replication-evidencia"]
---

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

- [AWS — S3 security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
- [HackTricks — AWS S3](https://book.hacktricks.xyz/cloud-security/aws-security/aws-unauthenticated-enum-access/s3)

## Relacionadas

- [replication para conta externa](0278-aws-s3-replication.md)
- [ACL authenticated users](0273-aws-s3-acl.md)
- [access logs públicos](0279-aws-s3-logging.md)
- [bucket como malware host](0280-aws-s3-malware.md)
- [policy Principal *](0275-aws-s3-policy.md)