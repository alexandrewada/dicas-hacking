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
# effective perms assume-role
```

**Freio:** Não crie backdoors permanentes. Cuidado com custos (instâncias grandes).

Já abri High demais em trust policy frouxa por sintoma sem efeito. Cruzei com: CloudTrail: iam:*, CreateUser, Attach*; GuardDuty. Sem side-effect, baixo.

Detecto via: CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.

Corrijo com: Least privilege; permissions boundaries; SCP; MFA delete; IMDS hop limit.

Levo no report: Identidade inicial; API calls; identidade final; cleanup.

Refs: Rhino Security Labs AWS privesc, MITRE Cloud