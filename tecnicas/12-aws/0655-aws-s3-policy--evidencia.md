---
id: "0655"
categoria: "12-aws"
familia: "aws-s3"
slug: "policy"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["12-aws", "aws-s3", "evidencia"]
aliases: ["policy Principal *", "policy", "policy-evidencia"]
---

# policy Principal * — evidência

Pacote pra policy Principal * sobreviver peer review.

## Contexto

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

## O que precisa aparecer

- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

URL/policy; amostra redigida; screenshot console se fornecido.

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 6e8ee5

{"id":"10042","owner":"USER_A","note":"redacted-policy"}
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

- [policy Principal *](0275-aws-s3-policy.md)
- [ACL authenticated users](0273-aws-s3-acl.md)
- [access logs públicos](0279-aws-s3-logging.md)
- [bucket como malware host](0280-aws-s3-malware.md)
- [S3 GetObject público](0272-aws-s3-public-get.md)