---
id: "0657"
categoria: "12-aws"
familia: "aws-s3"
slug: "signed"
angulo: "evidencia"
mitre: "T1530"
owasp: ""
tags: ["12-aws", "aws-s3", "evidencia", "t1530"]
aliases: ["signed URL overbroad", "signed", "signed-evidencia"]
---

# signed URL overbroad — evidência

Pacote pra signed URL overbroad sobreviver peer review.

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

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 9e38dd

{"id":"usr_01HZX","owner":"USER_A","note":"redacted-signed"}
# capturado como USER_B
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

- [signed URL overbroad](0277-aws-s3-signed.md)
- [ACL authenticated users](0273-aws-s3-acl.md)
- [access logs públicos](0279-aws-s3-logging.md)
- [bucket como malware host](0280-aws-s3-malware.md)
- [policy Principal *](0275-aws-s3-policy.md)