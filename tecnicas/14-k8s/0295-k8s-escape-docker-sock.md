---
id: "0295"
categoria: "14-k8s"
familia: "k8s-escape"
slug: "docker-sock"
angulo: "base"
mitre: "T1611"
owasp: ""
tags: ["14-k8s", "k8s-escape", "base", "t1611"]
aliases: ["docker.sock no pod", "docker-sock"]
---

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
# k8s docker-sock lab namespace
kubectl -n lab auth can-i --list --as=system:serviceaccount:lab:sa-docker-sock
kubectl -n lab get rolebinding,clusterrolebinding -o wide | head
# imds via pod: curl 169.254.169.254 — só lab; tag 5e44ca
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

- [MITRE ATT&CK T1611](https://attack.mitre.org/techniques/T1611/)
- [MITRE ATT&CK T1078](https://attack.mitre.org/techniques/T1078/)
- [Microsoft — Kubernetes attack matrix](https://microsoft.github.io/Threat-Matrix-for-Kubernetes/)
- [NSA/CISA — Kubernetes hardening](https://media.defense.gov/2022/Aug/29/2003064742/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

## Relacionadas

- [docker.sock no pod — evidência](0675-k8s-escape-docker-sock--evidencia.md)
- [Token de ServiceAccount](0291-k8s-escape-sa-token.md)
- [RBAC wildcards](0292-k8s-escape-rbac.md)
- [Pod privileged](0293-k8s-escape-privileged.md)
- [cloud metadata from pod](0296-k8s-escape-imds.md)