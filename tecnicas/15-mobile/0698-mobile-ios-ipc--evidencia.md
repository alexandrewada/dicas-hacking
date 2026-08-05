---
id: "0698"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "ipc"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "evidencia"]
aliases: ["app groups misuse", "ipc", "ipc-evidencia"]
---

# app groups misuse — evidência

Pacote pra app groups misuse sobreviver peer review.

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## O que precisa aparecer

- Variante app groups misuse: trato separado da família `mobile-ios`.

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

Artefato Keychain de teste; request API.

## PoC mínimo

```text
--- evidência redigida ---
req: GET /…/10042 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (ipc)
hash_prova: b1b596
```

## Remediação junto

Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

## Se purple

MDM policies; ATS force; keychain audit.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [OWASP MASTG — iOS](https://mas.owasp.org/MASTG/0x06b-iOS-Security-Testing/)
- [Frida documentation](https://frida.re/docs/home/)

## Relacionadas

- [app groups misuse](0318-mobile-ios-ipc.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [Keychain fraco](0311-mobile-ios-keychain.md)