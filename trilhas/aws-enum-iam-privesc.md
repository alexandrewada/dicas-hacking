# AWS: enum → privesc IAM

Objetivo: a partir de enum de S3 / SSRF→IMDS / credencial fraca, chegar a uma cadeia de roles IAM (PassRole / AssumeRole / policy version) com evidência mínima — sem criar backdoor persistente fora do lab.

**Pré-condições:** conta AWS de engajamento ou role fornecida; CloudTrail no escopo de leitura; SSRF/IMDS só se o ROE cobrir metadata; criação de role/policy só em conta lab ou com rollback acordado.

[Índice](../indice/README.md) · [Trilhas](README.md)

## Cadeia

1. **Enum S3** — buckets públicos / listáveis no escopo (sem baixar PII em massa).
   - [0271 — S3 public list](../tecnicas/12-aws/0271-aws-s3-public-list.md) · [evidência](../tecnicas/12-aws/0651-aws-s3-public-list--evidencia.md)
   - [0272 — S3 public get](../tecnicas/12-aws/0272-aws-s3-public-get.md) · [evidência](../tecnicas/12-aws/0652-aws-s3-public-get--evidencia.md)
   - [0267 — privesc via S3](../tecnicas/12-aws/0267-aws-privesc-s3.md) · [evidência](../tecnicas/12-aws/0647-aws-privesc-s3--evidencia.md) (se o bucket carrega cred/config)

2. **SSRF → IMDS** — metadata de instância / role temporária (web ou XXE).
   - [0041 — SSRF IMDS](../tecnicas/02-web/0041-web-ssrf-imds.md) · [path](../tecnicas/02-web/0801-web-ssrf-imds--path.md) · [detecção](../tecnicas/02-web/0421-web-ssrf-imds--detecao.md)
   - [0172 — XXE → SSRF](../tecnicas/07-ssrf-xxe/0172-xxe-classic-ssrf.md) · [lab](../tecnicas/07-ssrf-xxe/0552-xxe-classic-ssrf--lab.md)
   - [0266 — privesc IMDS](../tecnicas/12-aws/0266-aws-privesc-imds.md) · [evidência](../tecnicas/12-aws/0646-aws-privesc-imds--evidencia.md)

3. **Cadeia IAM** — PassRole → Lambda/EC2 com role mais forte; AssumeRole cross-account/lab.
   - [0262 — PassRole](../tecnicas/12-aws/0262-aws-privesc-passrole.md) · [evidência](../tecnicas/12-aws/0642-aws-privesc-passrole--evidencia.md)
   - [0264 — AssumeRole](../tecnicas/12-aws/0264-aws-privesc-assume-role.md) · [evidência](../tecnicas/12-aws/0644-aws-privesc-assume-role--evidencia.md)
   - [0261 — policy version](../tecnicas/12-aws/0261-aws-privesc-policy-version.md) · [evidência](../tecnicas/12-aws/0641-aws-privesc-policy-version--evidencia.md)
   - [0263 — Lambda update](../tecnicas/12-aws/0263-aws-privesc-lambda-update.md) (se PassRole + updateFunctionCode estiver no path)

4. **Purple / CloudTrail** — fechar com o que o blue deveria ver.
   - [0345 — CloudTrail](../tecnicas/18-evasion/0345-purple-detect-cloudtrail.md) · [evidência](../tecnicas/18-evasion/0725-purple-detect-cloudtrail--evidencia.md)

## Freios OpSec / quando parar

- IMDS: só `latest/meta-data/iam/security-credentials/` o necessário; não exfiltro customer data do bucket.
- Não crio usuário IAM permanente nem access key de longa duração sem autorização escrita e plano de teardown.
- AssumeRole cross-account fora do lab: documento o trust policy, não assumo produção de terceiro.
- Paro se `iam:PassRole` + recurso privilegiado exigir write destrutivo — peço janela / conta sandbox.

## O que entra no relatório

- Bucket/URL SSRF + prova de role name (credencial mascarada; TTL curto).
- Edge IAM: policy statement exata (PassRole, AssumeRole, SetDefaultPolicyVersion).
- CloudTrail event IDs das ações de prova (Create*/Update* só se no ROE).
- Fix: IMDSv2 obrigatório, bucket policy, SCP, deny PassRole amplo, alertas CloudTrail.
- Teardown checklist se algo foi criado no engajamento.

[Índice](../indice/README.md)
