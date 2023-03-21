# PassRole + compute — evidência

Pacote pra PassRole + compute sobreviver peer review.

## Contexto

Em AWS, privesc é grafo IAM: CreatePolicyVersion, AttachUserPolicy, PassRole+EC2,
Lambda update, roles assumíveis, e metadata SSRF. O expert usa enumerate-iam / CloudFox
e prova com ação mínima em conta sandbox do cliente.

## O que precisa aparecer

- Se não validar **EC2/Lambda/Glue**, a nota fica genérica.
- Effective permissions: identity + resource + SCP/boundary. Wildcard Action+Resource no mesmo statement fede.

## Checklist

- ROE cobre
- ambiente/versão
- identidade de teste
- PoC redigido
- impacto 2–3 frases
- hotfix + estrutural
- cleanup
- MITRE/OWASP

## Mínimo que eu aceito

Identidade inicial; API calls; identidade final; cleanup.

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 69fc56

{"id":"10042","owner":"USER_A","note":"redacted-passrole"}
# capturado como USER_B
```

## Remediação junto

Least privilege; permissions boundaries; SCP; MFA delete; IMDS hop limit.

## Se purple

CloudTrail: iam:*, CreateUser, Attach*; GuardDuty.

## Armadilha

Não crie backdoors permanentes. Cuidado com custos (instâncias grandes).

## Refs

- Rhino Security Labs AWS privesc
- MITRE Cloud