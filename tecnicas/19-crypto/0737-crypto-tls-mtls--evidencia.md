# mTLS misconfig — evidência

Pacote pra mTLS misconfig sobreviver peer review.

## Contexto

TLS fraco (legacy protocols, cipher suites, certificate validation errors, pinning ausente
em mobile) ainda aparece. Inclua também cookie Secure flags e HSTS. Evito DoS com renegotiation floods.

## O que precisa aparecer

- Detalhe que pago pra ver: **Client cert bypass**.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

ssllabs-like summary; cipher list; exploitability note.

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: f26f65

{"id":"usr_01HZX","owner":"USER_A","note":"redacted-mtls"}
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