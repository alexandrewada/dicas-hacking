---
id: "0312"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "ats"
angulo: "base"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "base"]
aliases: ["ATS exceptions", "ats"]
---

# ATS exceptions

**Mobile** · `Mobile ATT&CK`

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## O que muda aqui

- Variante ATS exceptions: trato separado da família `mobile-ios`.

## Como testo

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## Exemplo

```bash
# iOS lab IPA — ats
frida -U -f app.lab.ios -l enumerate_keychain.js
# url scheme: xcrun simctl openurl booted 'applab://ats?t=456056'
# ATS bypass só em build debug
```

## Campo

Keystore vs SharedPreferences plaintext — backup flags entram com nuance.

ATS exceptions: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: MDM policies; ATS force; keychain audit.

## Já me queimei

Não contorne DRM de terceiros fora do escopo do app do cliente.

## Blue

- Detectar: MDM policies; ATS force; keychain audit.
- Fechar: Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

## Evidência

Artefato Keychain de teste; request API.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [OWASP MASTG — iOS](https://mas.owasp.org/MASTG/0x06a-Testing-IOS/)
- [Frida documentation](https://frida.re/docs/home/)

## Relacionadas

- [ATS exceptions — evidência](0692-mobile-ios-ats--evidencia.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)
- [Keychain fraco](0311-mobile-ios-keychain.md)