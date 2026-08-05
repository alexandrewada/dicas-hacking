---
id: "0270"
categoria: "12-aws"
familia: "aws-privesc"
slug: "federated"
angulo: "base"
mitre: "T1078.004"
owasp: ""
tags: ["12-aws", "aws-privesc", "base", "t1078.004"]
aliases: ["federation / role confusion", "federated"]
---

# federation / role confusion

**Cloud** · `T1078.004 Cloud Accounts`

## Contexto

Em AWS, privesc é grafo IAM: CreatePolicyVersion, AttachUserPolicy, PassRole+EC2,
Lambda update, roles assumíveis, e metadata SSRF. O expert usa enumerate-iam / CloudFox
e prova com ação mínima em conta sandbox do cliente.

## Como eu faço

1. Mapeio identidade atual (sts get-caller-identity).
2. Enumero permissões efetivas e roles.
3. Identifico paths conhecidos de privesc IAM.
4. Valido em sandbox; criar evidência reversível.
5. Recomendo SCP/permissions boundary.

## Exemplo

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_767faa
aws s3api get-bucket-policy --bucket lab-bucket-federated --profile lab_767faa
# seguro: Get*/List*; destrutivo (DeleteBucket) só em lab throwaway
# effective perms federated
```

## Diferencial desta nota

- Effective permissions: identity + resource + SCP/boundary. Wildcard Action+Resource no mesmo statement fede.

Já abri High demais em federation / role confusion por sintoma sem efeito. Cruzei com: CloudTrail: iam:*, CreateUser, Attach*; GuardDuty. Sem side-effect, baixo.

## Onde já errei

Não crie backdoors permanentes. Cuidado com custos (instâncias grandes).

CloudTrail eventName + accessKeyId de teste + ARN. Screenshot da console sozinha não basta.

## Entrega

- blue: CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.
- fix: Least privilege; permissions boundaries; SCP; MFA delete; IMDS hop limit.
- proof: Identidade inicial; API calls; identidade final; cleanup.

## Refs

- [MITRE ATT&CK T1078.004](https://attack.mitre.org/techniques/T1078/004/)
- [Rhino Security Labs — AWS privilege escalation](https://rhinosecuritylabs.com/aws/aws-privilege-escalation-methods-mitigation/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [AWS IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## Relacionadas

- [federation / role confusion — evidência](0650-aws-privesc-federated--evidencia.md)
- [Credencial via IMDS](0266-aws-privesc-imds.md)
- [PassRole + compute](0262-aws-privesc-passrole.md)
- [trust policy frouxa](0264-aws-privesc-assume-role.md)