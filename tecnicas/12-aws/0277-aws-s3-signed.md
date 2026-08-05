---
id: "0277"
categoria: "12-aws"
familia: "aws-s3"
slug: "signed"
angulo: "base"
mitre: "T1530"
owasp: ""
tags: ["12-aws", "aws-s3", "base", "t1530"]
aliases: ["signed URL overbroad", "signed"]
---

# signed URL overbroad

**Cloud storage** · `T1530 Data from Cloud Storage`

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

**Variante:** Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

**Método**

1. Enumero buckets no escopo (não force wordlists gigantes em prod sem acordo).
2. Testo list/get públicos e authenticated cross-account.
3. Avalio website hosting e XSS stored.
4. Verifico object versioning e delete risks.
5. Reportar dados expostos com amostra redigida.

## No lab ficou assim

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_f936bf
aws s3api get-bucket-policy --bucket lab-bucket-signed --profile lab_f936bf
# seguro: Get*/List*; destrutivo (DeleteBucket) só em lab throwaway
# effective perms signed
```

**Freio:** Não baixe datasets inteiros de PII — evidência mínima.

signed URL overbroad: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: CloudTrail data events; Macie; public access block alerts.

Detecto via: CloudTrail data events; Macie; public access block alerts.

Corrijo com: Block Public Access; least privilege policies; encryption; access logs.

Levo no report: URL/policy; amostra redigida; screenshot console se fornecido.

## Refs

- [MITRE ATT&CK T1530](https://attack.mitre.org/techniques/T1530/)
- [AWS — S3 security best practices](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)
- [HackTricks — AWS S3](https://book.hacktricks.xyz/cloud-security/aws-security/aws-unauthenticated-enum-access/s3)

## Relacionadas

- [signed URL overbroad — evidência](0657-aws-s3-signed--evidencia.md)
- [ACL authenticated users](0273-aws-s3-acl.md)
- [access logs públicos](0279-aws-s3-logging.md)
- [bucket como malware host](0280-aws-s3-malware.md)
- [policy Principal *](0275-aws-s3-policy.md)