---
id: "0313"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "url-scheme"
angulo: "base"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "base"]
aliases: ["URL scheme hijack", "url-scheme"]
---

# URL scheme hijack

**Mobile** · `Mobile ATT&CK`

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## O que muda aqui

- Variante URL scheme hijack: trato separado da família `mobile-ios`.

## Como testo

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## PoC mínimo

```bash
# iOS lab IPA — url-scheme
frida -U -f app.lab.ios -l enumerate_keychain.js
# url scheme: xcrun simctl openurl booted 'applab://url-scheme?t=1e2cd7'
# ATS bypass só em build debug
```

## Campo

Keystore vs SharedPreferences plaintext — backup flags entram com nuance.

URL scheme hijack: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: MDM policies; ATS force; keychain audit.

## Já me queimei

Não contorne DRM de terceiros fora do escopo do app do cliente.

## Blue

- Detectar: MDM policies; ATS force; keychain audit.
- Fechar: Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

## Evidência

Artefato Keychain de teste; request API.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [OWASP MASTG — iOS](https://mas.owasp.org/MASTG/0x06b-iOS-Security-Testing/)
- [Frida documentation](https://frida.re/docs/home/)

## Relacionadas

- [URL scheme hijack — evidência](0693-mobile-ios-url-scheme--evidencia.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)
- [Keychain fraco (path)](0311-mobile-ios-keychain.md)