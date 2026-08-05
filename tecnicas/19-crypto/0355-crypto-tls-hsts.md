---
id: "0355"
categoria: "19-crypto"
familia: "crypto-tls"
slug: "hsts"
angulo: "base"
mitre: "T1573"
owasp: ""
tags: ["19-crypto", "crypto-tls", "base", "t1573"]
aliases: ["HSTS ausente", "hsts"]
---

# HSTS ausente

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

## Sinal / query

```bash
# TLS hsts
echo | openssl s_client -connect TARGET.lab.local:8443 -servername WRONG.lab.local 2>&1 | grep -E 'verify|subject'
curl -skI https://TARGET.lab.local | grep -i strict-transport
# tag 315d8a
```

## Diferencial desta nota

- Variante HSTS ausente: trato separado da família `crypto-tls`.

Antes de Critical em HSTS ausente, confiro se a telemetria que eu cobraria reagiria — Certificate expiry monitoring; TLS policy sensors.

## Onde já errei

Não faço stress massivo em prod. POODLE-class é histórico — contextualize risco real.

TLS no stack real do app, não só ssllabs no apex.

## Entrega

- blue: Certificate expiry monitoring; TLS policy sensors.
- fix: TLS 1.2+; modern ciphers; HSTS; certificate automation; disable RSA key exchange.
- proof: ssllabs-like summary; cipher list; exploitability note.

## Refs

- [MITRE ATT&CK T1573](https://attack.mitre.org/techniques/T1573/)
- [OWASP Transport Layer Protection](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)

## Relacionadas

- [HSTS ausente — evidência](0735-crypto-tls-hsts--evidencia.md)
- [hostname mismatch](0353-crypto-tls-cert-mismatch.md)
- [CRIME/BREACH context](0359-crypto-tls-compression.md)
- [Certificate Transparency gaps](0360-crypto-tls-ct.md)
- [cert expired/self-signed em prod](0354-crypto-tls-expired.md)