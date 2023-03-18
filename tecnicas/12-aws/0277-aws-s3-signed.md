# signed URL overbroad

**Cloud storage** · `T1530 Data from Cloud Storage`

Buckets públicos, policies permissivas, ACLs legadas e signed URLs mal geradas
continuam a vazar dados. Teste também takeover de buckets referenciados (subdomain → S3).

**Variante:** Anon GetObject + role cross-account. Os três controles (Block/policy/ACL) podem mentir sozinhos.

**Método**

1. Enumero buckets no escopo (não force wordlists gigantes em prod sem acordo).
2. Testo list/get públicos e authenticated cross-account.
3. Avalio website hosting e XSS stored.
4. Verifico object versioning e delete risks.
5. Reportar dados expostos com amostra redigida.

## No lab ficou assim

```bash
# AWS lab — identidade de teste, sem wipe
aws sts get-caller-identity --profile lab_f936bf
aws s3api get-bucket-policy --bucket lab-bucket-signed --profile lab_f936bf
# effective perms signed
```

**Freio:** Não baixe datasets inteiros de PII — evidência mínima.

signed URL overbroad: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: CloudTrail data events; Macie; public access block alerts.

Detecto via: CloudTrail data events; Macie; public access block alerts.

Corrijo com: Block Public Access; least privilege policies; encryption; access logs.

Levo no report: URL/policy; amostra redigida; screenshot console se fornecido.

Refs: AWS S3 security best practices