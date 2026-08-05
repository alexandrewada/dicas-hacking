---
id: "0740"
categoria: "19-crypto"
familia: "crypto-tls"
slug: "ct"
angulo: "evidencia"
mitre: "T1573"
owasp: ""
tags: ["19-crypto", "crypto-tls", "evidencia", "t1573"]
aliases: ["Certificate Transparency gaps", "ct", "ct-evidencia"]
---

# Certificate Transparency gaps — evidência

Pacote pra Certificate Transparency gaps sobreviver peer review.

## Contexto

TLS fraco (legacy protocols, cipher suites, certificate validation errors, pinning ausente
em mobile) ainda aparece. Inclua também cookie Secure flags e HSTS. Evito DoS com renegotiation floods.

## O que precisa aparecer

- Variante Certificate Transparency gaps: trato separado da família `crypto-tls`.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

ssllabs-like summary; cipher list; exploitability note.

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/a1b2c3d4-e5f6-7890-abcd-ef1234567890 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (ct)
hash_prova: b24f5a
```

## Remediação junto

TLS 1.2+; modern ciphers; HSTS; certificate automation; disable RSA key exchange.

## Se purple

Certificate expiry monitoring; TLS policy sensors.

## Armadilha

Não faço stress massivo em prod. POODLE-class é histórico — contextualize risco real.

## Refs

- [MITRE ATT&CK T1573](https://attack.mitre.org/techniques/T1573/)
- [OWASP Transport Layer Protection](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)

## Relacionadas

- [Certificate Transparency gaps](0360-crypto-tls-ct.md)
- [hostname mismatch](0353-crypto-tls-cert-mismatch.md)
- [CRIME/BREACH context](0359-crypto-tls-compression.md)
- [cert expired/self-signed em prod](0354-crypto-tls-expired.md)
- [HSTS ausente](0355-crypto-tls-hsts.md)