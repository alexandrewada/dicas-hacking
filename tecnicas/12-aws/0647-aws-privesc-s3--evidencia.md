---
id: "0647"
categoria: "12-aws"
familia: "aws-privesc"
slug: "s3"
angulo: "evidencia"
mitre: "T1078.004"
owasp: ""
tags: ["12-aws", "aws-privesc", "evidencia", "t1078.004"]
aliases: ["S3 policy confusion", "s3", "s3-evidencia"]
---

# S3 policy confusion — evidência

Pacote pra S3 policy confusion sobreviver peer review.

## Contexto

Em AWS, privesc é grafo IAM: CreatePolicyVersion, AttachUserPolicy, PassRole+EC2,
Lambda update, roles assumíveis, e metadata SSRF. O expert usa enumerate-iam / CloudFox
e prova com ação mínima em conta sandbox do cliente.

## O que precisa aparecer

- **Account takeover data** — muda ruído e o que entra no PDF.
- Effective permissions: identity + resource + SCP/boundary. Wildcard Action+Resource no mesmo statement fede.
- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Identidade inicial; API calls; identidade final; cleanup.

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/a1b2c3d4-e5f6-7890-abcd-ef1234567890 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (s3)
hash_prova: 5f318b
```

## Remediação junto

Least privilege; permissions boundaries; SCP; MFA delete; IMDS hop limit.

## Se purple

CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.

## Armadilha

Não crie backdoors permanentes. Cuidado com custos (instâncias grandes).

## Refs

- [MITRE ATT&CK T1078.004](https://attack.mitre.org/techniques/T1078/004/)
- [Rhino Security Labs — AWS privilege escalation](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [AWS IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## Relacionadas

- [S3 policy confusion](0267-aws-privesc-s3.md)
- [Credencial via IMDS](0266-aws-privesc-imds.md)
- [PassRole + compute](0262-aws-privesc-passrole.md)
- [trust policy frouxa](0264-aws-privesc-assume-role.md)