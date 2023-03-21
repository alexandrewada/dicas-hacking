# SSM SendCommand — evidência

Pacote pra SSM SendCommand sobreviver peer review.

## Contexto

Em AWS, privesc é grafo IAM: CreatePolicyVersion, AttachUserPolicy, PassRole+EC2,
Lambda update, roles assumíveis, e metadata SSRF. O expert usa enumerate-iam / CloudFox
e prova com ação mínima em conta sandbox do cliente.

## O que precisa aparecer

- **Lateral em instâncias** — muda ruído e o que entra no PDF.
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

```text
--- evidência redigida ---
req: GET /…/ORD-7781 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (ssm)
hash_prova: 6c6cc3
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