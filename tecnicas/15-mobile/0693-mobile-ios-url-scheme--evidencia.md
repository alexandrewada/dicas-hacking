---
id: "0693"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "url-scheme"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "evidencia"]
aliases: ["URL scheme hijack", "url-scheme", "url-scheme-evidencia"]
---

# URL scheme hijack — evidência

Pacote pra URL scheme hijack sobreviver peer review.

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## O que precisa aparecer

- Variante URL scheme hijack: trato separado da família `mobile-ios`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Artefato Keychain de teste; request API.

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/obj_8d54f1 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (url-scheme)
hash_prova: 8d54f1
```

## Remediação junto

Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

## Se purple

MDM policies; ATS force; keychain audit.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [OWASP MASTG — iOS](https://mas.owasp.org/MASTG/0x06a-Testing-IOS/)
- [Frida documentation](https://frida.re/docs/home/)

## Relacionadas

- [URL scheme hijack](0313-mobile-ios-url-scheme.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)
- [Keychain fraco (path)](0311-mobile-ios-keychain.md)