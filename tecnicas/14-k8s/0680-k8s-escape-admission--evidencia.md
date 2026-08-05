---
id: "0680"
categoria: "14-k8s"
familia: "k8s-escape"
slug: "admission"
angulo: "evidencia"
mitre: "T1611"
owasp: ""
tags: ["14-k8s", "k8s-escape", "evidencia", "t1611"]
aliases: ["bypass admission webhook", "admission", "admission-evidencia"]
---

# bypass admission webhook — evidência

Pacote pra bypass admission webhook sobreviver peer review.

## Contexto

Clusters mal configurados: SA tokens montados, RBAC permissivo, privileged pods,
docker.sock, e metadata cloud. Pentest k8s exige cuidado para não derrubar workloads.

## O que precisa aparecer

- Detalhe que pago pra ver: **Se fraco**.
- Token montado + bind cluster-admin. Prova: secrets get / exec.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

kubectl auth can-i; token redigido; PoC read secret.

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/usr_01HZX Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (admission)
hash_prova: e174d5
```

## Remediação junto

Least privilege RBAC; disable automount; PSS restricted; network policies;
no privileged.

## Se purple

Audit API server; Falco/OPA alerts; admission controller denies.

## Armadilha

Não delete namespaces. Privileged probes podem afetar nós.

## Refs

- [MITRE ATT&CK T1611](https://attack.mitre.org/techniques/T1611/)
- [MITRE ATT&CK T1078](https://attack.mitre.org/techniques/T1078/)
- [Microsoft — Kubernetes attack matrix](https://microsoft.github.io/Threat-Matrix-for-Kubernetes/)
- [NSA/CISA — Kubernetes hardening](https://media.defense.gov/2022/Aug/29/2003064742/-1/-1/0/CTR_KUBERNETES_HARDENING_GUIDANCE_1.2_20220829.PDF)

## Relacionadas

- [bypass admission webhook](0300-k8s-escape-admission.md)
- [Token de ServiceAccount](0291-k8s-escape-sa-token.md)
- [RBAC wildcards](0292-k8s-escape-rbac.md)
- [Pod privileged](0293-k8s-escape-privileged.md)
- [cloud metadata from pod](0296-k8s-escape-imds.md)