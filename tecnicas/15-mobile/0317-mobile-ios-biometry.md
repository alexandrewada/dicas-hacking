---
id: "0317"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "biometry"
angulo: "base"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "base"]
aliases: ["biometry bypass lab", "biometry"]
---

# biometry bypass lab

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Detalhe

- Se não validar **Local auth only**, a nota fica genérica.

## Execução

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## PoC mínimo

```bash
# iOS lab IPA — biometry
frida -U -f app.lab.ios -l enumerate_keychain.js
# url scheme: xcrun simctl openurl booted 'applab://biometry?t=c93ff3'
# ATS bypass só em build debug
```

## OpSec

Frida em build de teste ≠ pin quebrado na store. Deixo a nuance no report.

## Cuidados

Não contorne DRM de terceiros fora do escopo do app do cliente.

## Fechamento

| | |
|---|---|
| Detecção | MDM policies; ATS force; keychain audit. |
| Remediação | Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC. |
| Evidência | Artefato Keychain de teste; request API. |

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [OWASP MASTG — iOS](https://mas.owasp.org/MASTG/0x06a-Testing-IOS/)
- [Frida documentation](https://frida.re/docs/home/)

## Relacionadas

- [biometry bypass lab — evidência](0697-mobile-ios-biometry--evidencia.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [app groups misuse](0318-mobile-ios-ipc.md)
- [Keychain fraco](0311-mobile-ios-keychain.md)