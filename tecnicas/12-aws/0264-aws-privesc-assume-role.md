---
id: "0264"
categoria: "12-aws"
familia: "aws-privesc"
slug: "assume-role"
angulo: "base"
mitre: "T1078.004"
owasp: ""
tags: ["12-aws", "aws-privesc", "base", "t1078.004"]
aliases: ["trust policy frouxa", "assume-role"]
---

# trust policy frouxa

**Cloud** · `T1078.004 Cloud Accounts`

Em AWS, privesc é grafo IAM: CreatePolicyVersion, AttachUserPolicy, PassRole+EC2,
Lambda update, roles assumíveis, e metadata SSRF. O expert usa enumerate-iam / CloudFox
e prova com ação mínima em conta sandbox do cliente.

**Variante:** Effective permissions: identity + resource + SCP/boundary. Wildcard Action+Resource no mesmo statement fede.

**Método**

1. Mapeio identidade atual (sts get-caller-identity).
2. Enumero permissões efetivas e roles.
3. Identifico paths conhecidos de privesc IAM.
4. Valido em sandbox; criar evidência reversível.
5. Recomendo SCP/permissions boundary.

## No lab ficou assim

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_964ee6
aws s3api get-bucket-policy --bucket lab-bucket-assume-role --profile lab_964ee6
# seguro: Get*/List*; destrutivo (DeleteBucket) só em lab throwaway
# effective perms assume-role
```

**Freio:** Não crie backdoors permanentes. Cuidado com custos (instâncias grandes).

Já abri High demais em trust policy frouxa por sintoma sem efeito. Cruzei com: CloudTrail: iam:*, CreateUser, Attach*; GuardDuty. Sem side-effect, baixo.

Detecto via: CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.

Corrijo com: Least privilege; permissions boundaries; SCP; MFA delete; IMDS hop limit.

Levo no report: Identidade inicial; API calls; identidade final; cleanup.

## Refs

- [MITRE ATT&CK T1078.004](https://attack.mitre.org/techniques/T1078/004/)
- [Rhino Security Labs — AWS privilege escalation](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [AWS IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## Relacionadas

- [trust policy frouxa — evidência](0644-aws-privesc-assume-role--evidencia.md)
- [Credencial via IMDS](0266-aws-privesc-imds.md)
- [PassRole + compute](0262-aws-privesc-passrole.md)