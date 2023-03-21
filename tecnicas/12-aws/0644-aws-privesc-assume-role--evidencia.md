# trust policy frouxa — evidência

Pacote pra trust policy frouxa sobreviver peer review.

## Contexto

Em AWS, privesc é grafo IAM: CreatePolicyVersion, AttachUserPolicy, PassRole+EC2,
Lambda update, roles assumíveis, e metadata SSRF. O expert usa enumerate-iam / CloudFox
e prova com ação mínima em conta sandbox do cliente.

## O que precisa aparecer

- Effective permissions: identity + resource + SCP/boundary. Wildcard Action+Resource no mesmo statement fede.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Identidade inicial; API calls; identidade final; cleanup.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 00a062

{"id":"10042","owner":"USER_A","note":"redacted-assume-role"}
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