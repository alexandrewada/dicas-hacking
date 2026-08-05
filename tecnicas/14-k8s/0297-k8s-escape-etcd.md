---
id: "0297"
categoria: "14-k8s"
familia: "k8s-escape"
slug: "etcd"
angulo: "base"
mitre: "T1611"
owasp: ""
tags: ["14-k8s", "k8s-escape", "base", "t1611"]
aliases: ["etcd exposto", "etcd"]
---

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
# k8s etcd lab namespace
kubectl -n lab auth can-i --list --as=system:serviceaccount:lab:sa-etcd
kubectl -n lab get rolebinding,clusterrolebinding -o wide | head
# imds via pod: curl 169.254.169.254 — só lab; tag 5855e2
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

- [MITRE ATT&CK T1611](https://attack.mitre.org/techniques/T1611/)
- [MITRE ATT&CK T1078](https://attack.mitre.org/techniques/T1078/)
- [Microsoft — Kubernetes attack matrix](https://microsoft.github.io/Threat-Matrix-for-Kubernetes/)
- [NSA/CISA — Kubernetes hardening](https://media.defense.gov/2022/Aug/29/2003064742/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

## Relacionadas

- [etcd exposto — evidência](0677-k8s-escape-etcd--evidencia.md)
- [Token de ServiceAccount](0291-k8s-escape-sa-token.md)
- [RBAC wildcards](0292-k8s-escape-rbac.md)
- [Pod privileged](0293-k8s-escape-privileged.md)
- [cloud metadata from pod](0296-k8s-escape-imds.md)