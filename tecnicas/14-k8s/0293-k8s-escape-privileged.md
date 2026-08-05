---
id: "0293"
categoria: "14-k8s"
familia: "k8s-escape"
slug: "privileged"
angulo: "base"
mitre: "T1611"
owasp: ""
tags: ["14-k8s", "k8s-escape", "base", "t1611"]
aliases: ["Pod privileged", "privileged"]
---

# Pod privileged

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

## Exemplo

```bash
# privileged/hostPath — lab only
kubectl -n lab-68ebe0 auth can-i create pods --as=system:serviceaccount:lab:sa-privileged
kubectl -n lab-68ebe0 get psp,validatingadmissionpolicy 2>/dev/null | head
# lab only: pod privileged + hostPath / (não aplicar em prod)
# kubectl run probe-privileged --image=busybox --privileged — tag 68ebe0
```

## Diferencial desta nota

- Se não validar **Host escape**, a nota fica genérica.
- Token montado + bind cluster-admin. Prova: secrets get / exec.
- Leitura de host FS ou create privilegiado. Cosmético de namespace não fecha.

privileged pod: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Audit API server; Falco/OPA alerts; admission controller denies.

## Onde já errei

Não delete namespaces. Privileged probes podem afetar nós.

privileged / hostPath / CAP_SYS_ADMIN — mostro node FS ou cred do node.

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

- [Pod privileged — evidência](0673-k8s-escape-privileged--evidencia.md)
- [Token de ServiceAccount](0291-k8s-escape-sa-token.md)
- [RBAC wildcards](0292-k8s-escape-rbac.md)
- [cloud metadata from pod](0296-k8s-escape-imds.md)