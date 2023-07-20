# cloud metadata from pod — evidência

Pacote pra cloud metadata from pod sobreviver peer review.

## Contexto

Clusters mal configurados: SA tokens montados, RBAC permissivo, privileged pods,
docker.sock, e metadata cloud. Pentest k8s exige cuidado para não derrubar workloads.

## O que precisa aparecer

- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.
- Token montado + bind cluster-admin. Prova: secrets get / exec.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

kubectl auth can-i; token redigido; PoC read secret.

## Exemplo

```text
--- evidência redigida ---
req: GET /…/a1b2c3d4-e5f6-7890-abcd-ef1234567890 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (imds)
hash_prova: 5f44fb
```

## Remediação junto

Least privilege RBAC; disable automount; PSS restricted; network policies;
no privileged.

## Se purple

Audit API server; Falco/OPA alerts; admission controller denies.

## Armadilha

Não delete namespaces. Privileged probes podem afetar nós.

## Refs

- Kubernetes Attack Matrix
- NSA/CISA k8s hardening