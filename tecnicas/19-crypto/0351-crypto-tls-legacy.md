---
id: "0351"
categoria: "19-crypto"
familia: "crypto-tls"
slug: "legacy"
angulo: "base"
mitre: ""
owasp: ""
tags: ["19-crypto", "crypto-tls", "base"]
aliases: ["TLS 1.0/1.1 enabled", "legacy"]
---

# TLS 1.0/1.1 enabled

## Contexto

TLS fraco (legacy protocols, cipher suites, certificate validation errors, pinning ausente
em mobile) ainda aparece. Inclua também cookie Secure flags e HSTS. Evito DoS com renegotiation floods.

## Detalhe

- Variante TLS 1.0/1.1 enabled: trato separado da família `crypto-tls`.

## Execução

1. Enumero protocolos/ciphers com ferramentas autorizadas.
2. Valido cadeia de certificados e hostname.
3. Testo HSTS / mixed content.
4. Avalio client auth mTLS se presente.
5. Priorizar findings exploráveis vs apenas score de SSL lab.

## PoC mínimo

```bash
# TLS no host real do app — legacy
echo | openssl s_client -connect TARGET.lab.local:8443 -tls1 2>&1 | head -20
# seguro: enum cipher; sem downgrade ativo contra usuários reais
nmap --script ssl-enum-ciphers -p 8443 TARGET.lab.local
# tag 361ef1
```

## OpSec

Não faço stress massivo em prod. POODLE-class é histórico — contextualize risco real.

## Cuidados

Não faço stress massivo em prod. POODLE-class é histórico — contextualize risco real.

## Fechamento

| | |
|---|---|
| Detecção | Certificate expiry monitoring; TLS policy sensors. |
| Remediação | TLS 1.2+; modern ciphers; HSTS; certificate automation; disable RSA key exchange. |
| Evidência | ssllabs-like summary; cipher list; exploitability note. |

## Refs

- [OWASP Transport Layer Protection](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)

## Relacionadas

- [TLS 1.0/1.1 enabled — evidência](0731-crypto-tls-legacy--evidencia.md)
- [hostname mismatch](0353-crypto-tls-cert-mismatch.md)
- [CRIME/BREACH context](0359-crypto-tls-compression.md)
- [Certificate Transparency gaps](0360-crypto-tls-ct.md)
- [cert expired/self-signed em prod](0354-crypto-tls-expired.md)
- [CBC/RC4/3DES (path)](0352-crypto-tls-weak-cipher.md)
- [perfil TLS/JA3S (path)](../01-recon/0011-recon-http-fingerprint-tls-ja3.md)