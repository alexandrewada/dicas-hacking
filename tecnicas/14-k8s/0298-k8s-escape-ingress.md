---
id: "0298"
categoria: "14-k8s"
familia: "k8s-escape"
slug: "ingress"
angulo: "base"
mitre: ""
owasp: ""
tags: ["14-k8s", "k8s-escape", "base"]
aliases: ["ingress misconfig", "ingress"]
---

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
# k8s ingress lab namespace
kubectl -n lab auth can-i --list --as=system:serviceaccount:lab:sa-ingress
kubectl -n lab get rolebinding,clusterrolebinding -o wide | head
# imds via pod: curl 169.254.169.254 — só lab; tag 1a0e49
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

- [Microsoft — Kubernetes attack matrix](https://microsoft.github.io/Threat-Matrix-for-Kubernetes/)
- [NSA/CISA — Kubernetes hardening](https://media.defense.gov/2022/Aug/29/2003064742/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

## Relacionadas

- [ingress misconfig — evidência](0678-k8s-escape-ingress--evidencia.md)
- [Token de ServiceAccount](0291-k8s-escape-sa-token.md)
- [RBAC wildcards](0292-k8s-escape-rbac.md)
- [Pod privileged](0293-k8s-escape-privileged.md)
- [cloud metadata from pod](0296-k8s-escape-imds.md)