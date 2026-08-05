---
id: "0352"
categoria: "19-crypto"
familia: "crypto-tls"
slug: "weak-cipher"
angulo: "base"
mitre: "T1573"
owasp: ""
tags: ["19-crypto", "crypto-tls", "base", "t1573"]
aliases: ["CBC/RC4/3DES", "weak-cipher"]
---

# CBC/RC4/3DES

**Crypto** · `T1573 Encrypted Channel (contexto) / misconfig`

TLS fraco (legacy protocols, cipher suites, certificate validation errors, pinning ausente
em mobile) ainda aparece. Inclua também cookie Secure flags e HSTS. Evito DoS com renegotiation floods.

**Variante:** RC4 ainda passa onde a policy AES existe no papel. Comparo etype do TGS com msDS-SupportedEncryptionTypes antes de chamar de hardenizado.

**Método**

1. Enumero protocolos/ciphers com ferramentas autorizadas.
2. Valido cadeia de certificados e hostname.
3. Testo HSTS / mixed content.
4. Avalio client auth mTLS se presente.
5. Priorizar findings exploráveis vs apenas score de SSL lab.

## No lab ficou assim

```bash
# TLS no host real do app — weak-cipher
echo | openssl s_client -connect TARGET.lab.local:8443 -tls1 2>&1 | head -20
# seguro: enum cipher; sem downgrade ativo contra usuários reais
nmap --script ssl-enum-ciphers -p 8443 TARGET.lab.local
# tag 7738fe
```

**Freio:** Não faço stress massivo em prod. POODLE-class é histórico — contextualize risco real.

Já abri High demais em CBC/RC4/3DES por sintoma sem efeito. Cruzei com: Certificate expiry monitoring; TLS policy sensors. Sem side-effect, baixo.

Detecto via: Certificate expiry monitoring; TLS policy sensors.

Corrijo com: TLS 1.2+; modern ciphers; HSTS; certificate automation; disable RSA key exchange.

Levo no report: ssllabs-like summary; cipher list; exploitability note.

## Refs

- [MITRE ATT&CK T1573](https://attack.mitre.org/techniques/T1573/)
- [OWASP Transport Layer Protection](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
- [Mozilla SSL Configuration Generator](https://ssl-config.mozilla.org/)

## Relacionadas

- [CBC/RC4/3DES — evidência](0732-crypto-tls-weak-cipher--evidencia.md)
- [hostname mismatch](0353-crypto-tls-cert-mismatch.md)
- [CRIME/BREACH context](0359-crypto-tls-compression.md)
- [Certificate Transparency gaps](0360-crypto-tls-ct.md)
- [cert expired/self-signed em prod](0354-crypto-tls-expired.md)