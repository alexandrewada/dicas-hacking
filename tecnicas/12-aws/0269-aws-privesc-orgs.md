# Organizations / SCP bypass gaps

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

## Sinal / query

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_c7d1ee
aws s3api get-bucket-policy --bucket lab-bucket-orgs --profile lab_c7d1ee
# effective perms orgs
```

## Campo

CloudTrail eventName + accessKeyId de teste + ARN. Screenshot da console sozinha não basta.

Organizations / SCP bypass gaps: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.

## Já me queimei

Não crie backdoors permanentes. Cuidado com custos (instâncias grandes).

## Blue

- Detectar: CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.
- Fechar: Least privilege; permissions boundaries; SCP; MFA delete; IMDS hop limit.

## Evidência

Identidade inicial; API calls; identidade final; cleanup.

## Refs

- Rhino Security Labs AWS privesc
- MITRE Cloud