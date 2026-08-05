---
id: "0267"
categoria: "12-aws"
familia: "aws-privesc"
slug: "s3"
angulo: "base"
mitre: "T1078.004"
owasp: ""
tags: ["12-aws", "aws-privesc", "base", "t1078.004"]
aliases: ["S3 policy confusion", "s3"]
---

# S3 policy confusion

`T1078.004 Cloud Accounts`

## Por que importa

Em AWS, privesc é grafo IAM: CreatePolicyVersion, AttachUserPolicy, PassRole+EC2,
Lambda update, roles assumíveis, e metadata SSRF. O expert usa enumerate-iam / CloudFox
e prova com ação mínima em conta sandbox do cliente.

## Variante

- **Account takeover data** — muda ruído e o que entra no PDF.
- Effective permissions: identity + resource + SCP/boundary. Wildcard Action+Resource no mesmo statement fede.
- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

## Passo a passo

1. Mapeio identidade atual (sts get-caller-identity).
2. Enumero permissões efetivas e roles.
3. Identifico paths conhecidos de privesc IAM.
4. Valido em sandbox; criar evidência reversível.
5. Recomendo SCP/permissions boundary.

## PoC mínimo

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_fa8486
aws s3api get-bucket-policy --bucket lab-bucket-s3 --profile lab_fa8486
# seguro: Get*/List*; destrutivo (DeleteBucket) só em lab throwaway
# effective perms s3
```

## Nota de operador

S3: PublicAccessBlock, bucket policy e ACL podem discordar — testo os três.

## Armadilha

Não crie backdoors permanentes. Cuidado com custos (instâncias grandes).

Já abri High demais em S3 policy confusion por sintoma sem efeito. Cruzei com: CloudTrail: iam:*, CreateUser, Attach*; GuardDuty. Sem side-effect, baixo.

## Depois

Detecção — CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.

Remediação — Least privilege; permissions boundaries; SCP; MFA delete; IMDS hop limit.

No PDF — Identidade inicial; API calls; identidade final; cleanup.

## Refs

- [MITRE ATT&CK T1078.004](https://attack.mitre.org/techniques/T1078/004/)
- [Rhino Security Labs — AWS privilege escalation](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [AWS IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## Relacionadas

- [S3 policy confusion — evidência](0647-aws-privesc-s3--evidencia.md)
- [Credencial via IMDS](0266-aws-privesc-imds.md)
- [PassRole + compute](0262-aws-privesc-passrole.md)
- [trust policy frouxa](0264-aws-privesc-assume-role.md)