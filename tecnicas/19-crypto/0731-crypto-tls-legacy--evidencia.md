---
id: "0731"
categoria: "19-crypto"
familia: "crypto-tls"
slug: "legacy"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["19-crypto", "crypto-tls", "evidencia"]
aliases: ["TLS 1.0/1.1 enabled", "legacy", "legacy-evidencia"]
---

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

- [OWASP Transport Layer Protection](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)

## Relacionadas

- [TLS 1.0/1.1 enabled](0351-crypto-tls-legacy.md)
- [hostname mismatch](0353-crypto-tls-cert-mismatch.md)
- [CRIME/BREACH context](0359-crypto-tls-compression.md)
- [Certificate Transparency gaps](0360-crypto-tls-ct.md)
- [cert expired/self-signed em prod](0354-crypto-tls-expired.md)
- [CBC/RC4/3DES (path)](0352-crypto-tls-weak-cipher.md)
- [perfil TLS/JA3S (path)](../01-recon/0011-recon-http-fingerprint-tls-ja3.md)