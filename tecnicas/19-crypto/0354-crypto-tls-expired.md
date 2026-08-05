---
id: "0354"
categoria: "19-crypto"
familia: "crypto-tls"
slug: "expired"
angulo: "base"
mitre: ""
owasp: ""
tags: ["19-crypto", "crypto-tls", "base"]
aliases: ["cert expired/self-signed em prod", "expired"]
---

# cert expired/self-signed em prod

## Leitura rápida

TLS fraco (legacy protocols, cipher suites, certificate validation errors, pinning ausente
em mobile) ainda aparece. Inclua também cookie Secure flags e HSTS. Evito DoS com renegotiation floods.

## Foco

- Variante cert expired/self-signed em prod: trato separado da família `crypto-tls`.

## Mãos na massa

1. Enumero protocolos/ciphers com ferramentas autorizadas.
2. Valido cadeia de certificados e hostname.
3. Testo HSTS / mixed content.
4. Avalio client auth mTLS se presente.
5. Priorizar findings exploráveis vs apenas score de SSL lab.

## PoC mínimo

```bash
# TLS expired
echo | openssl s_client -connect TARGET.lab.local:443 -servername WRONG.lab.local 2>&1 | grep -E 'verify|subject'
curl -skI https://TARGET.lab.local | grep -i strict-transport
# tag 27c860
```

Downgrade só com cliente vulnerável no escopo.

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

- [cert expired/self-signed em prod — evidência](0734-crypto-tls-expired--evidencia.md)
- [hostname mismatch](0353-crypto-tls-cert-mismatch.md)
- [CRIME/BREACH context](0359-crypto-tls-compression.md)
- [Certificate Transparency gaps](0360-crypto-tls-ct.md)
- [HSTS ausente](0355-crypto-tls-hsts.md)