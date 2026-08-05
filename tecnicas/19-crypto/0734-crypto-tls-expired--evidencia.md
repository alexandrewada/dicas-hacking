---
id: "0734"
categoria: "19-crypto"
familia: "crypto-tls"
slug: "expired"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["19-crypto", "crypto-tls", "evidencia"]
aliases: ["cert expired/self-signed em prod", "expired", "expired-evidencia"]
---

# cert expired/self-signed em prod — evidência

Pacote pra cert expired/self-signed em prod sobreviver peer review.

## Contexto

TLS fraco (legacy protocols, cipher suites, certificate validation errors, pinning ausente
em mobile) ainda aparece. Inclua também cookie Secure flags e HSTS. Evito DoS com renegotiation floods.

## O que precisa aparecer

- Variante cert expired/self-signed em prod: trato separado da família `crypto-tls`.

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

ssllabs-like summary; cipher list; exploitability note.

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 24cf46

{"id":"obj_24cf46","owner":"USER_A","note":"redacted-expired"}
# capturado como USER_B
```

## Remediação junto

TLS 1.2+; modern ciphers; HSTS; certificate automation; disable RSA key exchange.

## Se purple

Certificate expiry monitoring; TLS policy sensors.

## Armadilha

Não faço stress massivo em prod. POODLE-class é histórico — contextualize risco real.

## Refs

- [OWASP Transport Layer Protection](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)

## Relacionadas

- [cert expired/self-signed em prod](0354-crypto-tls-expired.md)
- [hostname mismatch](0353-crypto-tls-cert-mismatch.md)
- [CRIME/BREACH context](0359-crypto-tls-compression.md)
- [Certificate Transparency gaps](0360-crypto-tls-ct.md)
- [HSTS ausente](0355-crypto-tls-hsts.md)