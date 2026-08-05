---
id: "0318"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "ipc"
angulo: "base"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "base"]
aliases: ["app groups misuse", "ipc"]
---

# app groups misuse

`Mobile ATT&CK`

## Por que importa

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Variante

- Variante app groups misuse: trato separado da família `mobile-ios`.

## Passo a passo

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## No lab ficou assim

```bash
# iOS lab IPA — ipc
frida -U -f app.lab.ios -l enumerate_keychain.js
# url scheme: xcrun simctl openurl booted 'applab://ipc?t=7a1e07'
# ATS bypass só em build debug
```

## Nota de operador

Frida em build de teste ≠ pin quebrado na store. Deixo a nuance no report.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

Falso amigo em app groups misuse: UI/log gritam, impacto não. Exijo MDM policies.

## Depois

Detecção — MDM policies; ATS force; keychain audit.

Remediação — Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

No PDF — Artefato Keychain de teste; request API.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [OWASP MASTG — iOS](https://mas.owasp.org/MASTG/0x06a-Testing-IOS/)
- [Frida documentation](https://frida.re/docs/home/)

## Relacionadas

- [app groups misuse — evidência](0698-mobile-ios-ipc--evidencia.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [Keychain fraco](0311-mobile-ios-keychain.md)