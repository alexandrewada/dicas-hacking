---
id: "0319"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "logs"
angulo: "base"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "base"]
aliases: ["os_log secrets", "logs"]
---

# os_log secrets

`Mobile ATT&CK`

## Por que importa

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## Variante

- Variante os_log secrets: trato separado da família `mobile-ios`.

## Passo a passo

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## Exemplo

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/logs?token=TOKEN_LAB_1f4b79'
# deep link / exported → token sink
```

## Nota de operador

Deep link / WebView / exported: intent até token sink é o ROI.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

Já abri High demais em os_log secrets por sintoma sem efeito. Cruzei com: MDM policies; ATS force; keychain audit. Sem side-effect, baixo.

## Depois

Detecção — MDM policies; ATS force; keychain audit.

Remediação — Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

No PDF — Artefato Keychain de teste; request API.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [OWASP MASTG — iOS](https://mas.owasp.org/MASTG/0x06a-Testing-IOS/)
- [Frida documentation](https://frida.re/docs/home/)

## Relacionadas

- [os_log secrets — evidência](0699-mobile-ios-logs--evidencia.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)