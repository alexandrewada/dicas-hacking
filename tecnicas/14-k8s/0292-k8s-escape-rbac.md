---
id: "0292"
categoria: "14-k8s"
familia: "k8s-escape"
slug: "rbac"
angulo: "base"
mitre: ""
owasp: ""
tags: ["14-k8s", "k8s-escape", "base"]
aliases: ["RBAC wildcards", "rbac"]
---

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
# k8s rbac lab namespace
kubectl -n lab auth can-i --list --as=system:serviceaccount:lab:sa-rbac
kubectl -n lab get rolebinding,clusterrolebinding -o wide | head
# imds via pod: curl 169.254.169.254 — só lab; tag aa4c97
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

- [Microsoft — Kubernetes attack matrix](https://microsoft.github.io/Threat-Matrix-for-Kubernetes/)
- [NSA/CISA — Kubernetes hardening](https://media.defense.gov/2022/Aug/29/2003064742/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

## Relacionadas

- [RBAC wildcards — evidência](0672-k8s-escape-rbac--evidencia.md)
- [Token de ServiceAccount](0291-k8s-escape-sa-token.md)
- [Pod privileged](0293-k8s-escape-privileged.md)
- [cloud metadata from pod](0296-k8s-escape-imds.md)