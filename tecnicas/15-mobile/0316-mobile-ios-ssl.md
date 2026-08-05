---
id: "0316"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "ssl"
angulo: "base"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "base"]
aliases: ["SSL kill switch lab", "ssl"]
---

# SSL kill switch lab

`Mobile ATT&CK`

## Por que importa

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Variante

- Variante SSL kill switch lab: trato separado da família `mobile-ios`.

## Passo a passo

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## Sinal / query

```bash
# iOS lab IPA — ssl
frida -U -f app.lab.ios -l enumerate_keychain.js
# url scheme: xcrun simctl openurl booted 'applab://ssl?t=eada08'
# ATS bypass só em build debug
```

## Nota de operador

Keystore vs SharedPreferences plaintext — backup flags entram com nuance.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

Antes de Critical em SSL kill switch lab, confiro se a telemetria que eu cobraria reagiria — MDM policies; ATS force; keychain audit.

## Depois

Detecção — MDM policies; ATS force; keychain audit.

Remediação — Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

No PDF — Artefato Keychain de teste; request API.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [OWASP MASTG — iOS](https://mas.owasp.org/MASTG/0x06b-iOS-Security-Testing/)
- [Frida documentation](https://frida.re/docs/home/)

## Relacionadas

- [SSL kill switch lab — evidência](0696-mobile-ios-ssl--evidencia.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)