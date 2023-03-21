# federation / role confusion — evidência

Pacote pra federation / role confusion sobreviver peer review.

## Contexto

Em AWS, privesc é grafo IAM: CreatePolicyVersion, AttachUserPolicy, PassRole+EC2,
Lambda update, roles assumíveis, e metadata SSRF. O expert usa enumerate-iam / CloudFox
e prova com ação mínima em conta sandbox do cliente.

## O que precisa aparecer

- Effective permissions: identity + resource + SCP/boundary. Wildcard Action+Resource no mesmo statement fede.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Identidade inicial; API calls; identidade final; cleanup.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: c8cc02

{"id":"ORD-7781","owner":"USER_A","note":"redacted-federated"}
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