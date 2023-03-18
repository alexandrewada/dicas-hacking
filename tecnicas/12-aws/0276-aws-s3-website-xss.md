# static website XSS

## Contexto

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

## Detalhe

- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.
- Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

## Execução

1. Enumero buckets no escopo (não force wordlists gigantes em prod sem acordo).
2. Testo list/get públicos e authenticated cross-account.
3. Avalio website hosting e XSS stored.
4. Verifico object versioning e delete risks.
5. Reportar dados expostos com amostra redigida.

## Sinal / query

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_b3478e
aws s3api get-bucket-policy --bucket lab-bucket-website-xss --profile lab_b3478e
# effective perms website-xss
```

## OpSec

Identidade > rede. Role chain e policies antes de port scan de VPC.

## Cuidados

Não baixe datasets inteiros de PII — evidência mínima.

## Fechamento

| | |
|---|---|
| Detecção | CloudTrail data events; Macie; public access block alerts. |
| Remediação | Block Public Access; least privilege policies; encryption; access logs. |
| Evidência | URL/policy; amostra redigida; screenshot console se fornecido. |

## Refs

- AWS S3 security best practices