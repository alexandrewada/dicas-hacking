---
id: "0672"
categoria: "14-k8s"
familia: "k8s-escape"
slug: "rbac"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["14-k8s", "k8s-escape", "evidencia"]
aliases: ["RBAC wildcards", "rbac", "rbac-evidencia"]
---

# RBAC wildcards — evidência

Pacote pra RBAC wildcards sobreviver peer review.

## Contexto

Clusters mal configurados: SA tokens montados, RBAC permissivo, privileged pods,
docker.sock, e metadata cloud. Pentest k8s exige cuidado para não derrubar workloads.

## O que precisa aparecer

- Se não validar **verbs * resources ***, a nota fica genérica.
- Token montado + bind cluster-admin. Prova: secrets get / exec.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

kubectl auth can-i; token redigido; PoC read secret.

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 452c36

{"id":"ORD-7781","owner":"USER_A","note":"redacted-rbac"}
# capturado como USER_B
```

## Remediação junto

Least privilege RBAC; disable automount; PSS restricted; network policies;
no privileged.

## Se purple

Audit API server; Falco/OPA alerts; admission controller denies.

## Armadilha

Não delete namespaces. Privileged probes podem afetar nós.

## Refs

- [Microsoft — Kubernetes attack matrix](https://microsoft.github.io/Threat-Matrix-for-Kubernetes/)
- [NSA/CISA — Kubernetes hardening](https://media.defense.gov/2022/Aug/29/2003064742/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

## Relacionadas

- [RBAC wildcards](0292-k8s-escape-rbac.md)
- [Token de ServiceAccount](0291-k8s-escape-sa-token.md)
- [Pod privileged](0293-k8s-escape-privileged.md)
- [cloud metadata from pod](0296-k8s-escape-imds.md)