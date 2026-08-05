---
id: "0304"
categoria: "15-mobile"
familia: "mobile-android"
slug: "deeplink"
angulo: "base"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-android", "base"]
aliases: ["deeplink hijack", "deeplink"]
---

# deeplink hijack

## Contexto

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## Detalhe

- Variante deeplink hijack: trato separado da família `mobile-android`.

## Execução

1. Mapeio apk (jadx) e superfícies exported.
2. Instrumentar com Frida **em device de teste**.
3. Avalio storage e logs.
4. Interceptar tráfego (com pinning bypass autorizado).
5. Testo backend com tokens do app.

## Sinal / query

```bash
# Android lab build — sem store
adb shell dumpsys package app.lab | grep -A2 exported=true
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/deeplink?token=TOKEN_LAB_49f6dc'
# WebView: overrideUrlLoading → token sink
```

## OpSec

Deep link / WebView / exported: intent até token sink é o ROI.

## Cuidados

Não publique apps modificados. Respeite store ToS e escopo.

## Fechamento

| | |
|---|---|
| Detecção | Mobile threat defense; RASP alerts; cert pinning telemetry. |
| Remediação | Android Keystore; non-exported components; WebView harden; SSL pinning + reporting. |
| Evidência | Componente explorado; dado acessado; API finding correlato. |

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [Frida documentation](https://frida.re/docs/home/)
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05b-Android-Security-Testing/)

## Relacionadas

- [deeplink hijack — evidência](0684-mobile-android-deeplink--evidencia.md)
- [token em logcat](0310-mobile-android-auth.md)
- [backup enabled](0307-mobile-android-backup.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)
- [WebView XSS/bridge (path)](0302-mobile-android-webview.md)
- [storage world-readable (path)](0303-mobile-android-storage.md)