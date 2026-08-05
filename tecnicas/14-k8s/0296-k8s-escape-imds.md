---
id: "0296"
categoria: "14-k8s"
familia: "k8s-escape"
slug: "imds"
angulo: "base"
mitre: ""
owasp: ""
tags: ["14-k8s", "k8s-escape", "base"]
aliases: ["cloud metadata from pod", "imds"]
---

# cloud metadata from pod

## Leitura rápida

Clusters mal configurados: SA tokens montados, RBAC permissivo, privileged pods,
docker.sock, e metadata cloud. Pentest k8s exige cuidado para não derrubar workloads.

## Foco

- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.
- Token montado + bind cluster-admin. Prova: secrets get / exec.

## Mãos na massa

1. Identifico se está em pod; ler SA token.
2. Enumero permissions (auth can-i).
3. Procurar secrets, pods privilegiados, hostPath.
4. Avalio escape controlado.
5. Reportar com namespace e objeto.

## Sinal / query

```bash
# k8s imds lab namespace
kubectl -n lab auth can-i --list --as=system:serviceaccount:lab:sa-imds
kubectl -n lab get rolebinding,clusterrolebinding -o wide | head
# imds via pod: curl 169.254.169.254 — só lab; tag e990a9
```

privileged / hostPath / CAP_SYS_ADMIN — mostro node FS ou cred do node.

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
- [AWS — Instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html)

## Relacionadas

- [cloud metadata from pod — evidência](0676-k8s-escape-imds--evidencia.md)
- [Token de ServiceAccount](0291-k8s-escape-sa-token.md)
- [RBAC wildcards](0292-k8s-escape-rbac.md)
- [Pod privileged](0293-k8s-escape-privileged.md)
- [Credencial via IMDS (path)](../12-aws/0266-aws-privesc-imds.md)
- [hostPath mount (path)](0294-k8s-escape-hostpath.md)