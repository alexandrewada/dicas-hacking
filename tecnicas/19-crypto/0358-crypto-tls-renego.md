---
id: "0358"
categoria: "19-crypto"
familia: "crypto-tls"
slug: "renego"
angulo: "base"
mitre: ""
owasp: ""
tags: ["19-crypto", "crypto-tls", "base"]
aliases: ["renegotiation issues", "renego"]
---

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
# TLS no host real do app — renego
echo | openssl s_client -connect TARGET.lab.local:8443 -tls1 2>&1 | head -20
# seguro: enum cipher; sem downgrade ativo contra usuários reais
nmap --script ssl-enum-ciphers -p 8443 TARGET.lab.local
# tag c54e99
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

- [OWASP Transport Layer Protection](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)

## Relacionadas

- [renegotiation issues — evidência](0738-crypto-tls-renego--evidencia.md)
- [hostname mismatch](0353-crypto-tls-cert-mismatch.md)
- [CRIME/BREACH context](0359-crypto-tls-compression.md)
- [Certificate Transparency gaps](0360-crypto-tls-ct.md)
- [cert expired/self-signed em prod](0354-crypto-tls-expired.md)