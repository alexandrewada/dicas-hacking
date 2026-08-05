---
id: "0320"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "webview"
angulo: "base"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "base"]
aliases: ["WKWebView issues", "webview"]
---

# WKWebView issues

**Mobile** · `Mobile ATT&CK`

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

**Variante:** Variante WKWebView issues: trato separado da família `mobile-ios`.

**Método**

1. Análise estática (class-dump/swift).
2. Runtime Frida/objection em lab.
3. Keychain e files na sandbox.
4. Tráfego e ATS.
5. Backend authz.

## Sinal / query

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/webview?token=TOKEN_LAB_b550e0'
# deep link / exported → token sink
```

**Freio:** Não contorne DRM de terceiros fora do escopo do app do cliente.

WKWebView issues: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: MDM policies; ATS force; keychain audit.

Detecto via: MDM policies; ATS force; keychain audit.

Corrijo com: Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

Levo no report: Artefato Keychain de teste; request API.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [OWASP MASTG — iOS](https://mas.owasp.org/MASTG/0x06b-iOS-Security-Testing/)
- [Frida documentation](https://frida.re/docs/home/)

## Relacionadas

- [WKWebView issues — evidência](0700-mobile-ios-webview--evidencia.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)