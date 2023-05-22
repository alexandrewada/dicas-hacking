# hostPath mount

**Containers** · `T1611 Escape to Host / T1078`

Clusters mal configurados: SA tokens montados, RBAC permissivo, privileged pods,
docker.sock, e metadata cloud. Pentest k8s exige cuidado para não derrubar workloads.

**Variante:** Token montado + bind cluster-admin. Prova: secrets get / exec.

**Método**

1. Identifico se está em pod; ler SA token.
2. Enumero permissions (auth can-i).
3. Procurar secrets, pods privilegiados, hostPath.
4. Avalio escape controlado.
5. Reportar com namespace e objeto.

## Sinal / query

```bash
# k8s lab namespace
kubectl -n lab-637707 auth can-i --list --as=system:serviceaccount:lab:sa-hostpath
kubectl -n lab-637707 get secrets
# prova RBAC excessivo hostpath
```

**Freio:** Não delete namespaces. Privileged probes podem afetar nós.

hostPath mount: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Audit API server; Falco/OPA alerts; admission controller denies.

Detecto via: Audit API server; Falco/OPA alerts; admission controller denies.

Corrijo com: Least privilege RBAC; disable automount; PSS restricted; network policies;
no privileged.

Levo no report: kubectl auth can-i; token redigido; PoC read secret.

Refs: Kubernetes Attack Matrix, NSA/CISA k8s hardening