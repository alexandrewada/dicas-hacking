# etcd exposto

**Containers** · `T1611 Escape to Host / T1078`

## Contexto

Clusters mal configurados: SA tokens montados, RBAC permissivo, privileged pods,
docker.sock, e metadata cloud. Pentest k8s exige cuidado para não derrubar workloads.

## O que muda aqui

- Se não validar **Critical**, a nota fica genérica.
- Token montado + bind cluster-admin. Prova: secrets get / exec.

## Como testo

1. Identifico se está em pod; ler SA token.
2. Enumero permissions (auth can-i).
3. Procurar secrets, pods privilegiados, hostPath.
4. Avalio escape controlado.
5. Reportar com namespace e objeto.

## PoC mínimo

```bash
# k8s lab namespace
kubectl -n lab-5855e2 auth can-i --list --as=system:serviceaccount:lab:sa-etcd
kubectl -n lab-5855e2 get secrets
# prova RBAC excessivo etcd
```

## Campo

privileged / hostPath / CAP_SYS_ADMIN — mostro node FS ou cred do node.

Antes de Critical em etcd exposto, confiro se a telemetria que eu cobraria reagiria — Audit API server; Falco/OPA alerts; admission controller denies.

## Já me queimei

Não delete namespaces. Privileged probes podem afetar nós.

## Blue

- Detectar: Audit API server; Falco/OPA alerts; admission controller denies.
- Fechar: Least privilege RBAC; disable automount; PSS restricted; network policies;
no privileged.

## Evidência

kubectl auth can-i; token redigido; PoC read secret.

## Refs

- Kubernetes Attack Matrix
- NSA/CISA k8s hardening