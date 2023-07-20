# hostPath mount — evidência

Pacote pra hostPath mount sobreviver peer review.

## Contexto

Clusters mal configurados: SA tokens montados, RBAC permissivo, privileged pods,
docker.sock, e metadata cloud. Pentest k8s exige cuidado para não derrubar workloads.

## O que precisa aparecer

- Token montado + bind cluster-admin. Prova: secrets get / exec.

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

kubectl auth can-i; token redigido; PoC read secret.

## Exemplo

```text
--- evidência redigida ---
req: GET /…/usr_01HZX Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (hostpath)
hash_prova: dd8ff1
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