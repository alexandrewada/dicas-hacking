---
id: "0651"
categoria: "12-aws"
familia: "aws-s3"
slug: "public-list"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["12-aws", "aws-s3", "evidencia"]
aliases: ["ListBucket público", "public-list", "public-list-evidencia"]
---

# ListBucket público — evidência

Pacote pra ListBucket público sobreviver peer review.

## Contexto

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

## O que precisa aparecer

- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

## Checklist

- ROE cobre
- ambiente/versão
- identidade de teste
- PoC redigido
- impacto 2–3 frases
- hotfix + estrutural
- cleanup
- MITRE/OWASP

## Mínimo que eu aceito

URL/policy; amostra redigida; screenshot console se fornecido.

## PoC mínimo

```text
--- evidência redigida ---
req: GET /…/obj_9d08c2 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (public-list)
hash_prova: 9d08c2
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

- [ListBucket público](0271-aws-s3-public-list.md)
- [ACL authenticated users](0273-aws-s3-acl.md)
- [access logs públicos](0279-aws-s3-logging.md)
- [bucket como malware host](0280-aws-s3-malware.md)
- [policy Principal *](0275-aws-s3-policy.md)