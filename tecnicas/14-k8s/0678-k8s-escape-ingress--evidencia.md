# ingress misconfig — evidência

Pacote pra ingress misconfig sobreviver peer review.

## Contexto

Clusters mal configurados: SA tokens montados, RBAC permissivo, privileged pods,
docker.sock, e metadata cloud. Pentest k8s exige cuidado para não derrubar workloads.

## O que precisa aparecer

- Se não validar **Request smuggling/path**, a nota fica genérica.
- Token montado + bind cluster-admin. Prova: secrets get / exec.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

kubectl auth can-i; token redigido; PoC read secret.

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 7ac877

{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","owner":"USER_A","note":"redacted-ingress"}
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