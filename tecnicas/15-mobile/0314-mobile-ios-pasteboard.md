---
id: "0314"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "pasteboard"
angulo: "base"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "base"]
aliases: ["UIPasteboard leaks", "pasteboard"]
---

# UIPasteboard leaks

`Mobile ATT&CK`

## Por que importa

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Variante

- Variante UIPasteboard leaks: trato separado da família `mobile-ios`.

## Passo a passo

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## No lab ficou assim

```bash
# iOS lab IPA — pasteboard
frida -U -f app.lab.ios -l enumerate_keychain.js
# url scheme: xcrun simctl openurl booted 'applab://pasteboard?t=0da6c0'
# ATS bypass só em build debug
```

## Nota de operador

Deep link / WebView / exported: intent até token sink é o ROI.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

Antes de Critical em UIPasteboard leaks, confiro se a telemetria que eu cobraria reagiria — MDM policies; ATS force; keychain audit.

## Depois

Detecção — MDM policies; ATS force; keychain audit.

Remediação — Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

No PDF — Artefato Keychain de teste; request API.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [OWASP MASTG — iOS](https://mas.owasp.org/MASTG/0x06b-iOS-Security-Testing/)
- [Frida documentation](https://frida.re/docs/home/)

## Relacionadas

- [UIPasteboard leaks — evidência](0694-mobile-ios-pasteboard--evidencia.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)