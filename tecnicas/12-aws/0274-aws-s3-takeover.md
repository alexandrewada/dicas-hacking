---
id: "0274"
categoria: "12-aws"
familia: "aws-s3"
slug: "takeover"
angulo: "base"
mitre: ""
owasp: ""
tags: ["12-aws", "aws-s3", "base"]
aliases: ["Takeover de bucket DNS", "takeover"]
---

# Takeover de bucket DNS

## Contexto

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

## Detalhe

- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.
- Recurso claimável + prova de controle (arquivo/challenge). Sem claim, não é Critical.

## Execução

1. Enumero buckets no escopo (não force wordlists gigantes em prod sem acordo).
2. Testo list/get públicos e authenticated cross-account.
3. Avalio website hosting e XSS stored.
4. Verifico object versioning e delete risks.
5. Reportar dados expostos com amostra redigida.

## Sinal / query

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_a1e41f
aws s3api get-bucket-policy --bucket lab-bucket-takeover --profile lab_a1e41f
# seguro: Get*/List*; destrutivo (DeleteBucket) só em lab throwaway
# effective perms takeover
```

## OpSec

Não baixe datasets inteiros de PII — evidência mínima. CloudTrail eventName + accessKeyId de teste + ARN. Screenshot da console sozinha não basta.

## Cuidados

Não baixe datasets inteiros de PII — evidência mínima.

## Fechamento

| | |
|---|---|
| Detecção | CloudTrail data events; Macie; public access block alerts. |
| Remediação | Block Public Access; least privilege policies; encryption; access logs. |
| Evidência | URL/policy; amostra redigida; screenshot console se fornecido. |

## Refs

- [AWS — S3 security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
- [HackTricks — AWS S3](https://book.hacktricks.xyz/cloud-security/aws-security/aws-unauthenticated-enum-access/s3)

## Relacionadas

- [Takeover de bucket DNS — evidência](0654-aws-s3-takeover--evidencia.md)
- [ACL authenticated users](0273-aws-s3-acl.md)
- [access logs públicos](0279-aws-s3-logging.md)
- [bucket como malware host](0280-aws-s3-malware.md)
- [policy Principal *](0275-aws-s3-policy.md)