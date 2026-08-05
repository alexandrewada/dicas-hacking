---
id: "0263"
categoria: "12-aws"
familia: "aws-privesc"
slug: "lambda-update"
angulo: "base"
mitre: "T1078.004"
owasp: ""
tags: ["12-aws", "aws-privesc", "base", "t1078.004"]
aliases: ["UpdateFunctionCode", "lambda-update"]
---

# UpdateFunctionCode

**Cloud** · `T1078.004 Cloud Accounts`

## Contexto

Em AWS, privesc é grafo IAM: CreatePolicyVersion, AttachUserPolicy, PassRole+EC2,
Lambda update, roles assumíveis, e metadata SSRF. O expert usa enumerate-iam / CloudFox
e prova com ação mínima em conta sandbox do cliente.

## O que muda aqui

- Effective permissions: identity + resource + SCP/boundary. Wildcard Action+Resource no mesmo statement fede.

## Como testo

1. Mapeio identidade atual (sts get-caller-identity).
2. Enumero permissões efetivas e roles.
3. Identifico paths conhecidos de privesc IAM.
4. Valido em sandbox; criar evidência reversível.
5. Recomendo SCP/permissions boundary.

## No lab ficou assim

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_667d21
aws s3api get-bucket-policy --bucket lab-bucket-lambda-update --profile lab_667d21
# seguro: Get*/List*; destrutivo (DeleteBucket) só em lab throwaway
# effective perms lambda-update
```

## Campo

Identidade > rede. Role chain e policies antes de port scan de VPC.

Antes de Critical em UpdateFunctionCode, confiro se a telemetria que eu cobraria reagiria — CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.

## Já me queimei

Não crie backdoors permanentes. Cuidado com custos (instâncias grandes).

## Blue

- Detectar: CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.
- Fechar: Least privilege; permissions boundaries; SCP; MFA delete; IMDS hop limit.

## Evidência

Identidade inicial; API calls; identidade final; cleanup.

## Refs

- [MITRE ATT&CK T1078.004](https://attack.mitre.org/techniques/T1078/004/)
- [Rhino Security Labs — AWS privilege escalation](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [AWS IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## Relacionadas

- [UpdateFunctionCode — evidência](0643-aws-privesc-lambda-update--evidencia.md)
- [Credencial via IMDS](0266-aws-privesc-imds.md)
- [PassRole + compute](0262-aws-privesc-passrole.md)
- [trust policy frouxa](0264-aws-privesc-assume-role.md)