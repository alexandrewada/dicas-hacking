# replication para conta externa

## Leitura rápida

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

## Foco

- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

## Mãos na massa

1. Enumero buckets no escopo (não force wordlists gigantes em prod sem acordo).
2. Testo list/get públicos e authenticated cross-account.
3. Avalio website hosting e XSS stored.
4. Verifico object versioning e delete risks.
5. Reportar dados expostos com amostra redigida.

## No lab ficou assim

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_130a67
aws s3api get-bucket-policy --bucket lab-bucket-replication --profile lab_130a67
# effective perms replication
```

Identidade > rede. Role chain e policies antes de port scan de VPC.

## Pitfall

Não baixe datasets inteiros de PII — evidência mínima.

## Detecção / remediação

CloudTrail data events; Macie; public access block alerts.

→ Block Public Access; least privilege policies; encryption; access logs.

## Prova

URL/policy; amostra redigida; screenshot console se fornecido.

## Refs

- AWS S3 security best practices