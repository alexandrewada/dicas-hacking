# redirectors e OPSEC — evidência

Pacote pra redirectors e OPSEC sobreviver peer review.

## Contexto

C2 em red team deve priorizar ROE, kill-switch, allowlists de beacon e evitar
impacto em disponibilidade. OpSec inclui metadados de infraestrutura, categorificação de domínios
e alinhamento com detection goals do purple team.

## O que precisa aparecer

- Variante redirectors e OPSEC: trato separado da família `rt-c2`.

## Checklist

- ROE cobre
- ambiente/versão
- identidade de teste
- PoC redigido
- impacto 2–3 frases
- hotfix + estrutural
- cleanup
- MITRE/OWASP

## Mínimo que eu aceito

Diagrama de infra; IOCs entregues ao blue; timeline.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: e7b9a2

{"id":"10042","owner":"USER_A","note":"redacted-redirector"}
# capturado como USER_B
```

## Remediação junto

Allowlist egress; TLS inspection onde adequado; DNS control.

## Se purple

CDN/proxy anomalies; beacon jitter patterns; JA3.

## Armadilha

Não uso infra de C2 criminal. Não aponte para fora do escopo.

## Refs

- Red Team Field Manual ethics
- MITRE C2