---
id: "0654"
categoria: "12-aws"
familia: "aws-s3"
slug: "takeover"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["12-aws", "aws-s3", "evidencia"]
aliases: ["Takeover de bucket DNS", "takeover", "takeover-evidencia"]
---

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

- [AWS — S3 security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
- [HackTricks — AWS S3](https://book.hacktricks.xyz/cloud-security/aws-security/aws-unauthenticated-enum-access/s3)

## Relacionadas

- [Takeover de bucket DNS](0274-aws-s3-takeover.md)
- [ACL authenticated users](0273-aws-s3-acl.md)
- [access logs públicos](0279-aws-s3-logging.md)
- [bucket como malware host](0280-aws-s3-malware.md)
- [policy Principal *](0275-aws-s3-policy.md)