# ACL authenticated users

`T1530 Data from Cloud Storage`

## Por que importa

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

## Variante

- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.
- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

## Passo a passo

1. Enumero buckets no escopo (não force wordlists gigantes em prod sem acordo).
2. Testo list/get públicos e authenticated cross-account.
3. Avalio website hosting e XSS stored.
4. Verifico object versioning e delete risks.
5. Reportar dados expostos com amostra redigida.

## Exemplo

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_bde188
aws s3api get-bucket-policy --bucket lab-bucket-acl --profile lab_bde188
# effective perms acl
```

## Nota de operador

Identidade > rede. Role chain e policies antes de port scan de VPC.

## Armadilha

Não baixe datasets inteiros de PII — evidência mínima.

ACL authenticated users: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: CloudTrail data events; Macie; public access block alerts.

## Depois

Detecção — CloudTrail data events; Macie; public access block alerts.

Remediação — Block Public Access; least privilege policies; encryption; access logs.

No PDF — URL/policy; amostra redigida; screenshot console se fornecido.

## Refs

- AWS S3 security best practices