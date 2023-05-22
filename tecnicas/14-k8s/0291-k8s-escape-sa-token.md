# Token de ServiceAccount

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

## PoC mínimo

```bash
# k8s lab namespace
kubectl -n lab-cb307a auth can-i --list --as=system:serviceaccount:lab:sa-sa-token
kubectl -n lab-cb307a get secrets
# prova RBAC excessivo sa-token
```

**Freio:** Não delete namespaces. Privileged probes podem afetar nós.

Antes de Critical em service account token abuse, confiro se a telemetria que eu cobraria reagiria — Audit API server; Falco/OPA alerts; admission controller denies.

Detecto via: Audit API server; Falco/OPA alerts; admission controller denies.

Corrijo com: Least privilege RBAC; disable automount; PSS restricted; network policies;
no privileged.

Levo no report: kubectl auth can-i; token redigido; PoC read secret.

Refs: Kubernetes Attack Matrix, NSA/CISA k8s hardening