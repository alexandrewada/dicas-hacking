---
id: "0299"
categoria: "14-k8s"
familia: "k8s-escape"
slug: "supply"
angulo: "base"
mitre: "T1611"
owasp: ""
tags: ["14-k8s", "k8s-escape", "base", "t1611"]
aliases: ["imagem maliciosa no registry interno", "supply"]
---

# imagem maliciosa no registry interno

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

## No lab ficou assim

```bash
# k8s lab namespace
kubectl -n lab-548991 auth can-i --list --as=system:serviceaccount:lab:sa-supply
kubectl -n lab-548991 get secrets
# prova RBAC excessivo supply
```

**Freio:** Não delete namespaces. Privileged probes podem afetar nós.

Já abri High demais em imagem maliciosa no registry interno por sintoma sem efeito. Cruzei com: Audit API server; Falco/OPA alerts; admission controller denies. Sem side-effect, baixo.

Detecto via: Audit API server; Falco/OPA alerts; admission controller denies.

Corrijo com: Least privilege RBAC; disable automount; PSS restricted; network policies;
no privileged.

Levo no report: kubectl auth can-i; token redigido; PoC read secret.

## Refs

- [MITRE ATT&CK T1611](https://attack.mitre.org/techniques/T1611/)
- [MITRE ATT&CK T1078](https://attack.mitre.org/techniques/T1078/)
- [Microsoft — Kubernetes attack matrix](https://microsoft.github.io/Threat-Matrix-for-Kubernetes/)
- [NSA/CISA — Kubernetes hardening](https://media.defense.gov/2022/Aug/29/2003064742/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

## Relacionadas

- [imagem maliciosa no registry interno — evidência](0679-k8s-escape-supply--evidencia.md)
- [Token de ServiceAccount](0291-k8s-escape-sa-token.md)
- [RBAC wildcards](0292-k8s-escape-rbac.md)
- [Pod privileged](0293-k8s-escape-privileged.md)
- [cloud metadata from pod](0296-k8s-escape-imds.md)