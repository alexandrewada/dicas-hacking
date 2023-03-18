# KMS decrypt excessivo

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

## PoC mínimo

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_ca6e51
aws s3api get-bucket-policy --bucket lab-bucket-kms --profile lab_ca6e51
# effective perms kms
```

## Diferencial desta nota

- Effective permissions: identity + resource + SCP/boundary. Wildcard Action+Resource no mesmo statement fede.

Antes de Critical em KMS decrypt excessivo, confiro se a telemetria que eu cobraria reagiria — CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.

## Onde já errei

Não crie backdoors permanentes. Cuidado com custos (instâncias grandes).

S3: PublicAccessBlock, bucket policy e ACL podem discordar — testo os três.

## Entrega

- blue: CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.
- fix: Least privilege; permissions boundaries; SCP; MFA delete; IMDS hop limit.
- proof: Identidade inicial; API calls; identidade final; cleanup.

## Refs

- Rhino Security Labs AWS privesc
- MITRE Cloud