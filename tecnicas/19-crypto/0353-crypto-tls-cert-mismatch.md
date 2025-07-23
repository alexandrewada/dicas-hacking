# hostname mismatch

**Crypto** · `T1573 Encrypted Channel (contexto) / misconfig`

## Contexto

TLS fraco (legacy protocols, cipher suites, certificate validation errors, pinning ausente
em mobile) ainda aparece. Inclua também cookie Secure flags e HSTS. Evito DoS com renegotiation floods.

## Como eu faço

1. Enumero protocolos/ciphers com ferramentas autorizadas.
2. Valido cadeia de certificados e hostname.
3. Testo HSTS / mixed content.
4. Avalio client auth mTLS se presente.
5. Priorizar findings exploráveis vs apenas score de SSL lab.

## No lab ficou assim

```bash
# TLS no host real do app
nmap --script ssl-enum-ciphers -p 443 TARGET.lab.local
echo | openssl s_client -connect TARGET.lab.local:443 -tls1_0 2>&1 | head
# variante cert-mismatch tag 958c8e
```

## Diferencial desta nota

- Variante hostname mismatch: trato separado da família `crypto-tls`.

Falso amigo em hostname mismatch: UI/log gritam, impacto não. Exijo Certificate expiry monitoring.

## Onde já errei

Não faço stress massivo em prod. POODLE-class é histórico — contextualize risco real.

TLS no stack real do app, não só ssllabs no apex.

## Entrega

- blue: Certificate expiry monitoring; TLS policy sensors.
- fix: TLS 1.2+; modern ciphers; HSTS; certificate automation; disable RSA key exchange.
- proof: ssllabs-like summary; cipher list; exploitability note.

## Refs

- OWASP Transport Layer Protection
- Mozilla TLS guidelines