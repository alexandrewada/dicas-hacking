---
id: "0262"
categoria: "12-aws"
familia: "aws-privesc"
slug: "passrole"
angulo: "base"
mitre: ""
owasp: ""
tags: ["12-aws", "aws-privesc", "base"]
aliases: ["PassRole + compute", "passrole"]
---

# PassRole + compute

## Leitura rápida

Em AWS, privesc é grafo IAM: CreatePolicyVersion, AttachUserPolicy, PassRole+EC2,
Lambda update, roles assumíveis, e metadata SSRF. O expert usa enumerate-iam / CloudFox
e prova com ação mínima em conta sandbox do cliente.

## Foco

- Se não validar **EC2/Lambda/Glue**, a nota fica genérica.
- Effective permissions: identity + resource + SCP/boundary. Wildcard Action+Resource no mesmo statement fede.

## Mãos na massa

1. Mapeio identidade atual (sts get-caller-identity).
2. Enumero permissões efetivas e roles.
3. Identifico paths conhecidos de privesc IAM.
4. Valido em sandbox; criar evidência reversível.
5. Recomendo SCP/permissions boundary.

## PoC mínimo

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_c3e21f
aws s3api get-bucket-policy --bucket lab-bucket-passrole --profile lab_c3e21f
# seguro: Get*/List*; destrutivo (DeleteBucket) só em lab throwaway
# effective perms passrole
```

Identidade > rede. Role chain e policies antes de port scan de VPC.

## Pitfall

Não crie backdoors permanentes. Cuidado com custos (instâncias grandes).

## Detecção / remediação

CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.

→ Least privilege; permissions boundaries; SCP; MFA delete; IMDS hop limit.

## Prova

Identidade inicial; API calls; identidade final; cleanup.

## Refs

- [Rhino Security Labs — AWS privilege escalation](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [AWS IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## Relacionadas

- [PassRole + compute — evidência](0642-aws-privesc-passrole--evidencia.md)
- [Credencial via IMDS](0266-aws-privesc-imds.md)
- [trust policy frouxa](0264-aws-privesc-assume-role.md)
- [UpdateFunctionCode (path)](0263-aws-privesc-lambda-update.md)
- [ACL authenticated users (path)](0273-aws-s3-acl.md)