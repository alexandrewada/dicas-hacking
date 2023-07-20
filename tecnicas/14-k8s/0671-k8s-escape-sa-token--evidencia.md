# Token de ServiceAccount — evidência

Pacote pra Token de ServiceAccount sobreviver peer review.

## Contexto

Clusters mal configurados: SA tokens montados, RBAC permissivo, privileged pods,
docker.sock, e metadata cloud. Pentest k8s exige cuidado para não derrubar workloads.

## O que precisa aparecer

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

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 4b933d

{"id":"10042","owner":"USER_A","note":"redacted-sa-token"}
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

- Kubernetes Attack Matrix
- NSA/CISA k8s hardening