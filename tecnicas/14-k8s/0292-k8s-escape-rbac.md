# RBAC wildcards

## Leitura rápida

Clusters mal configurados: SA tokens montados, RBAC permissivo, privileged pods,
docker.sock, e metadata cloud. Pentest k8s exige cuidado para não derrubar workloads.

## Foco

- Se não validar **verbs * resources ***, a nota fica genérica.
- Token montado + bind cluster-admin. Prova: secrets get / exec.

## Mãos na massa

1. Identifico se está em pod; ler SA token.
2. Enumero permissions (auth can-i).
3. Procurar secrets, pods privilegiados, hostPath.
4. Avalio escape controlado.
5. Reportar com namespace e objeto.

## Exemplo

```bash
# k8s lab namespace
kubectl -n lab-aa4c97 auth can-i --list --as=system:serviceaccount:lab:sa-rbac
kubectl -n lab-aa4c97 get secrets
# prova RBAC excessivo rbac
```

SA token + RBAC excessivo. Leio RoleBinding antes de kubectl bomb.

## Pitfall

Não delete namespaces. Privileged probes podem afetar nós.

## Detecção / remediação

Audit API server; Falco/OPA alerts; admission controller denies.

→ Least privilege RBAC; disable automount; PSS restricted; network policies;
no privileged.

## Prova

kubectl auth can-i; token redigido; PoC read secret.

## Refs

- Kubernetes Attack Matrix
- NSA/CISA k8s hardening