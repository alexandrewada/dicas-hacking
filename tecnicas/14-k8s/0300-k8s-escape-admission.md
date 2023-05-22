# bypass admission webhook

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
kubectl -n lab-225314 auth can-i --list --as=system:serviceaccount:lab:sa-admission
kubectl -n lab-225314 get secrets
# prova RBAC excessivo admission
```

## Diferencial desta nota

- Detalhe que pago pra ver: **Se fraco**.
- Token montado + bind cluster-admin. Prova: secrets get / exec.

Falso amigo em bypass admission webhook: UI/log gritam, impacto não. Exijo Audit API server.

## Onde já errei

Não delete namespaces. Privileged probes podem afetar nós.

privileged / hostPath / CAP_SYS_ADMIN — mostro node FS ou cred do node.

## Entrega

- blue: Audit API server; Falco/OPA alerts; admission controller denies.
- fix: Least privilege RBAC; disable automount; PSS restricted; network policies;
no privileged.
- proof: kubectl auth can-i; token redigido; PoC read secret.

## Refs

- Kubernetes Attack Matrix
- NSA/CISA k8s hardening