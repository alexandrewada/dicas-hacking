# docker.sock no pod

**Containers** · `T1611 Escape to Host / T1078`

## Contexto

Clusters mal configurados: SA tokens montados, RBAC permissivo, privileged pods,
docker.sock, e metadata cloud. Pentest k8s exige cuidado para não derrubar workloads.

## Como eu faço

1. Identifico se está em pod; ler SA token.
2. Enumero permissions (auth can-i).
3. Procurar secrets, pods privilegiados, hostPath.
4. Avalio escape controlado.
5. Reportar com namespace e objeto.

## Sinal / query

```bash
# k8s lab namespace
kubectl -n lab-5e44ca auth can-i --list --as=system:serviceaccount:lab:sa-docker-sock
kubectl -n lab-5e44ca get secrets
# prova RBAC excessivo docker-sock
```

## Diferencial desta nota

- Token montado + bind cluster-admin. Prova: secrets get / exec.
- Leitura de host FS ou create privilegiado. Cosmético de namespace não fecha.

Já abri High demais em docker.sock montado por sintoma sem efeito. Cruzei com: Audit API server; Falco/OPA alerts; admission controller denies. Sem side-effect, baixo.

## Onde já errei

Não delete namespaces. Privileged probes podem afetar nós.

SA token + RBAC excessivo. Leio RoleBinding antes de kubectl bomb.

## Entrega

- blue: Audit API server; Falco/OPA alerts; admission controller denies.
- fix: Least privilege RBAC; disable automount; PSS restricted; network policies;
no privileged.
- proof: kubectl auth can-i; token redigido; PoC read secret.

## Refs

- Kubernetes Attack Matrix
- NSA/CISA k8s hardening