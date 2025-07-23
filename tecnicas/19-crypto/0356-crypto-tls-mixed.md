# mixed content

**Crypto** · `T1573 Encrypted Channel (contexto) / misconfig`

TLS fraco (legacy protocols, cipher suites, certificate validation errors, pinning ausente
em mobile) ainda aparece. Inclua também cookie Secure flags e HSTS. Evito DoS com renegotiation floods.

**Variante:** Variante mixed content: trato separado da família `crypto-tls`.

**Método**

1. Enumero protocolos/ciphers com ferramentas autorizadas.
2. Valido cadeia de certificados e hostname.
3. Testo HSTS / mixed content.
4. Avalio client auth mTLS se presente.
5. Priorizar findings exploráveis vs apenas score de SSL lab.

## PoC mínimo

```bash
# TLS no host real do app
nmap --script ssl-enum-ciphers -p 8443 TARGET.lab.local
echo | openssl s_client -connect TARGET.lab.local:8443 -tls1_0 2>&1 | head
# variante mixed tag 3938d8
```

**Freio:** Não faço stress massivo em prod. POODLE-class é histórico — contextualize risco real.

Já abri High demais em mixed content por sintoma sem efeito. Cruzei com: Certificate expiry monitoring; TLS policy sensors. Sem side-effect, baixo.

Detecto via: Certificate expiry monitoring; TLS policy sensors.

Corrijo com: TLS 1.2+; modern ciphers; HSTS; certificate automation; disable RSA key exchange.

Levo no report: ssllabs-like summary; cipher list; exploitability note.

Refs: OWASP Transport Layer Protection, Mozilla TLS guidelines