# ingress misconfig

## Contexto

Clusters mal configurados: SA tokens montados, RBAC permissivo, privileged pods,
docker.sock, e metadata cloud. Pentest k8s exige cuidado para não derrubar workloads.

## Detalhe

- Se não validar **Request smuggling/path**, a nota fica genérica.
- Token montado + bind cluster-admin. Prova: secrets get / exec.

## Execução

1. Identifico se está em pod; ler SA token.
2. Enumero permissions (auth can-i).
3. Procurar secrets, pods privilegiados, hostPath.
4. Avalio escape controlado.
5. Reportar com namespace e objeto.

## No lab ficou assim

```bash
# k8s lab namespace
kubectl -n lab-1a0e49 auth can-i --list --as=system:serviceaccount:lab:sa-ingress
kubectl -n lab-1a0e49 get secrets
# prova RBAC excessivo ingress
```

## OpSec

SA token + RBAC excessivo. Leio RoleBinding antes de kubectl bomb.

## Cuidados

Não delete namespaces. Privileged probes podem afetar nós.

## Fechamento

| | |
|---|---|
| Detecção | Audit API server; Falco/OPA alerts; admission controller denies. |
| Remediação | Least privilege RBAC; disable automount; PSS restricted; network policies;
no privileged. |
| Evidência | kubectl auth can-i; token redigido; PoC read secret. |

## Refs

- Kubernetes Attack Matrix
- NSA/CISA k8s hardening