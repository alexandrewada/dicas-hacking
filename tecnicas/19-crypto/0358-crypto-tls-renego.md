# renegotiation issues

## Leitura rápida

TLS fraco (legacy protocols, cipher suites, certificate validation errors, pinning ausente
em mobile) ainda aparece. Inclua também cookie Secure flags e HSTS. Evito DoS com renegotiation floods.

## Foco

- Detalhe que pago pra ver: **Histórico/contextual**.

## Mãos na massa

1. Enumero protocolos/ciphers com ferramentas autorizadas.
2. Valido cadeia de certificados e hostname.
3. Testo HSTS / mixed content.
4. Avalio client auth mTLS se presente.
5. Priorizar findings exploráveis vs apenas score de SSL lab.

## No lab ficou assim

```bash
# TLS no host real do app
nmap --script ssl-enum-ciphers -p 8443 TARGET.lab.local
echo | openssl s_client -connect TARGET.lab.local:8443 -tls1_0 2>&1 | head
# variante renego tag c54e99
```

TLS no stack real do app, não só ssllabs no apex.

## Pitfall

Não faço stress massivo em prod. POODLE-class é histórico — contextualize risco real.

## Detecção / remediação

Certificate expiry monitoring; TLS policy sensors.

→ TLS 1.2+; modern ciphers; HSTS; certificate automation; disable RSA key exchange.

## Prova

ssllabs-like summary; cipher list; exploitability note.

## Refs

- OWASP Transport Layer Protection
- Mozilla TLS guidelines