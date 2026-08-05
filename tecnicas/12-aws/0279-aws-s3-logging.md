---
id: "0279"
categoria: "12-aws"
familia: "aws-s3"
slug: "logging"
angulo: "base"
mitre: "T1530"
owasp: ""
tags: ["12-aws", "aws-s3", "base", "t1530"]
aliases: ["access logs públicos", "logging"]
---

# access logs públicos

**Cloud storage** · `T1530 Data from Cloud Storage`

## Contexto

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

## O que muda aqui

- Se não validar **Meta-leak**, a nota fica genérica.
- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

## Como testo

1. Enumero buckets no escopo (não force wordlists gigantes em prod sem acordo).
2. Testo list/get públicos e authenticated cross-account.
3. Avalio website hosting e XSS stored.
4. Verifico object versioning e delete risks.
5. Reportar dados expostos com amostra redigida.

## Sinal / query

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_9705a7
aws s3api get-bucket-policy --bucket lab-bucket-logging --profile lab_9705a7
# seguro: Get*/List*; destrutivo (DeleteBucket) só em lab throwaway
# effective perms logging
```

## Campo

S3: PublicAccessBlock, bucket policy e ACL podem discordar — testo os três.

Já abri High demais em access logs públicos por sintoma sem efeito. Cruzei com: CloudTrail data events; Macie; public access block alerts. Sem side-effect, baixo.

## Já me queimei

Não baixe datasets inteiros de PII — evidência mínima.

## Blue

- Detectar: CloudTrail data events; Macie; public access block alerts.
- Fechar: Block Public Access; least privilege policies; encryption; access logs.

## Evidência

URL/policy; amostra redigida; screenshot console se fornecido.

## Refs

- [MITRE ATT&CK T1530](https://attack.mitre.org/techniques/T1530/)
- [AWS — S3 security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
- [HackTricks — AWS S3](https://book.hacktricks.xyz/cloud-security/aws-security/aws-unauthenticated-enum-access/s3)

## Relacionadas

- [access logs públicos — evidência](0659-aws-s3-logging--evidencia.md)
- [ACL authenticated users](0273-aws-s3-acl.md)
- [bucket como malware host](0280-aws-s3-malware.md)
- [policy Principal *](0275-aws-s3-policy.md)
- [S3 GetObject público](0272-aws-s3-public-get.md)