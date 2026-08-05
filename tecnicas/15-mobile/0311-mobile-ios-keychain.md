---
id: "0311"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "keychain"
angulo: "base"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "base"]
aliases: ["Keychain fraco", "keychain"]
---

# Keychain fraco

**Mobile** · `Mobile ATT&CK`

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Como eu faço

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## No lab ficou assim

```bash
# iOS lab IPA — keychain
frida -U -f app.lab.ios -l enumerate_keychain.js
# url scheme: xcrun simctl openurl booted 'applab://keychain?t=8693d8'
# ATS bypass só em build debug
```

## Diferencial desta nota

- Variante Keychain accessibility fraca: trato separado da família `mobile-ios`.

Falso amigo em Keychain accessibility fraca: UI/log gritam, impacto não. Exijo MDM policies.

## Onde já errei

Não contorne DRM de terceiros fora do escopo do app do cliente.

Keystore vs SharedPreferences plaintext — backup flags entram com nuance.

## Entrega

- blue: MDM policies; ATS force; keychain audit.
- fix: Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.
- proof: Artefato Keychain de teste; request API.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [OWASP MASTG — iOS](https://mas.owasp.org/MASTG/0x06a-Testing-IOS/)
- [Frida documentation](https://frida.re/docs/home/)

## Relacionadas

- [Keychain fraco — evidência](0691-mobile-ios-keychain--evidencia.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)