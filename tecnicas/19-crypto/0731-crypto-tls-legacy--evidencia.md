# TLS 1.0/1.1 enabled — evidência

Pacote pra TLS 1.0/1.1 enabled sobreviver peer review.

## Contexto

TLS fraco (legacy protocols, cipher suites, certificate validation errors, pinning ausente
em mobile) ainda aparece. Inclua também cookie Secure flags e HSTS. Evito DoS com renegotiation floods.

## O que precisa aparecer

- Variante TLS 1.0/1.1 enabled: trato separado da família `crypto-tls`.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

ssllabs-like summary; cipher list; exploitability note.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 845b3b

{"id":"usr_01HZX","owner":"USER_A","note":"redacted-legacy"}
# capturado como USER_B
```

## Remediação junto

TLS 1.2+; modern ciphers; HSTS; certificate automation; disable RSA key exchange.

## Se purple

Certificate expiry monitoring; TLS policy sensors.

## Armadilha

Não faço stress massivo em prod. POODLE-class é histórico — contextualize risco real.

## Refs

- OWASP Transport Layer Protection
- Mozilla TLS guidelines