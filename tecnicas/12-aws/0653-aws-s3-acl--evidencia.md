---
id: "0653"
categoria: "12-aws"
familia: "aws-s3"
slug: "acl"
angulo: "evidencia"
mitre: "T1530"
owasp: ""
tags: ["12-aws", "aws-s3", "evidencia", "t1530"]
aliases: ["ACL authenticated users", "acl", "acl-evidencia"]
---

# ACL authenticated users — evidência

Pacote pra ACL authenticated users sobreviver peer review.

## Contexto

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

## O que precisa aparecer

- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.
- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

URL/policy; amostra redigida; screenshot console se fornecido.

## Exemplo

```text
--- evidência redigida ---
req: GET /…/a1b2c3d4-e5f6-7890-abcd-ef1234567890 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (acl)
hash_prova: d6edac
```

## Remediação junto

Block Public Access; least privilege policies; encryption; access logs.

## Se purple

CloudTrail data events; Macie; public access block alerts.

## Armadilha

Não baixe datasets inteiros de PII — evidência mínima.

## Refs

- [MITRE ATT&CK T1530](https://attack.mitre.org/techniques/T1530/)
- [AWS — S3 security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
- [HackTricks — AWS S3](https://book.hacktricks.xyz/cloud-security/aws-security/aws-unauthenticated-enum-access/s3)

## Relacionadas

- [ACL authenticated users](0273-aws-s3-acl.md)
- [access logs públicos](0279-aws-s3-logging.md)
- [bucket como malware host](0280-aws-s3-malware.md)
- [policy Principal *](0275-aws-s3-policy.md)
- [S3 GetObject público](0272-aws-s3-public-get.md)