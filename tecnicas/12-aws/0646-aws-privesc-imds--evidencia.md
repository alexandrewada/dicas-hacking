# Credencial via IMDS — evidência

Pacote pra Credencial via IMDS sobreviver peer review.

## Contexto

Em AWS, privesc é grafo IAM: CreatePolicyVersion, AttachUserPolicy, PassRole+EC2,
Lambda update, roles assumíveis, e metadata SSRF. O expert usa enumerate-iam / CloudFox
e prova com ação mínima em conta sandbox do cliente.

## O que precisa aparecer

- **Via SSRF.** Sem isso o playbook da família mente.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.
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

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: b63624

{"id":"10042","owner":"USER_A","note":"redacted-imds"}
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