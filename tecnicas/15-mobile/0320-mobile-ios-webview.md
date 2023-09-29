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

Refs: OWASP MASTG iOS