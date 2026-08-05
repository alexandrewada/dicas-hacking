---
id: "0315"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "backup"
angulo: "base"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "base"]
aliases: ["itunes backup secrets", "backup"]
---

# itunes backup secrets

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Detalhe

- Variante itunes backup secrets: trato separado da família `mobile-ios`.

## Execução

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## Exemplo

```bash
# iOS lab IPA — backup
frida -U -f app.lab.ios -l enumerate_keychain.js
# url scheme: xcrun simctl openurl booted 'applab://backup?t=50e593'
# ATS bypass só em build debug
```

## OpSec

Não contorne DRM de terceiros fora do escopo do app do cliente. Frida em build de teste ≠ pin quebrado na store. Deixo a nuance no report.

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

- [itunes backup secrets — evidência](0695-mobile-ios-backup--evidencia.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)
- [Keychain fraco](0311-mobile-ios-keychain.md)