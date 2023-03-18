# SSM SendCommand

## Leitura rápida

Em AWS, privesc é grafo IAM: CreatePolicyVersion, AttachUserPolicy, PassRole+EC2,
Lambda update, roles assumíveis, e metadata SSRF. O expert usa enumerate-iam / CloudFox
e prova com ação mínima em conta sandbox do cliente.

## Foco

- **Lateral em instâncias** — muda ruído e o que entra no PDF.
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
aws sts get-caller-identity --profile lab_f049e9
aws s3api get-bucket-policy --bucket lab-bucket-ssm --profile lab_f049e9
# effective perms ssm
```

CloudTrail eventName + accessKeyId de teste + ARN. Screenshot da console sozinha não basta.

## Pitfall

Não crie backdoors permanentes. Cuidado com custos (instâncias grandes).

## Detecção / remediação

CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.

→ Least privilege; permissions boundaries; SCP; MFA delete; IMDS hop limit.

## Prova

Identidade inicial; API calls; identidade final; cleanup.

## Refs

- Rhino Security Labs AWS privesc
- MITRE Cloud