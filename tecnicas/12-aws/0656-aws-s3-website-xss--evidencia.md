---
id: "0656"
categoria: "12-aws"
familia: "aws-s3"
slug: "website-xss"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["12-aws", "aws-s3", "evidencia"]
aliases: ["static website XSS", "website-xss", "website-xss-evidencia"]
---

# static website XSS — evidência

Pacote pra static website XSS sobreviver peer review.

## Contexto

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

## O que precisa aparecer

- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.
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

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/ORD-7781 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (website-xss)
hash_prova: be9a6d
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

- [static website XSS](0276-aws-s3-website-xss.md)
- [ACL authenticated users](0273-aws-s3-acl.md)
- [access logs públicos](0279-aws-s3-logging.md)
- [bucket como malware host](0280-aws-s3-malware.md)
- [policy Principal *](0275-aws-s3-policy.md)