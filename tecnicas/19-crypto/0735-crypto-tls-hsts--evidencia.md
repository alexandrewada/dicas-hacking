# HSTS ausente — evidência

Pacote pra HSTS ausente sobreviver peer review.

## Contexto

TLS fraco (legacy protocols, cipher suites, certificate validation errors, pinning ausente
em mobile) ainda aparece. Inclua também cookie Secure flags e HSTS. Evito DoS com renegotiation floods.

## O que precisa aparecer

- Variante HSTS ausente: trato separado da família `crypto-tls`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

ssllabs-like summary; cipher list; exploitability note.

## Exemplo

```text
--- evidência redigida ---
req: GET /…/ORD-7781 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (hsts)
hash_prova: cf5835
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