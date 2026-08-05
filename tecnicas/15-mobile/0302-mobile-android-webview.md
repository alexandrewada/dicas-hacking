---
id: "0302"
categoria: "15-mobile"
familia: "mobile-android"
slug: "webview"
angulo: "base"
mitre: "T1420"
owasp: ""
tags: ["15-mobile", "mobile-android", "base", "t1420"]
aliases: ["WebView XSS/bridge", "webview"]
---

# WebView XSS/bridge

**Mobile** · `T1420 / T1412 (mobile ATT&CK)`

## Contexto

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## Como eu faço

1. Mapeio apk (jadx) e superfícies exported.
2. Instrumentar com Frida **em device de teste**.
3. Avalio storage e logs.
4. Interceptar tráfego (com pinning bypass autorizado).
5. Testo backend com tokens do app.

## No lab ficou assim

```bash
# Android lab build — sem store
adb shell dumpsys package app.lab | grep -A2 exported=true
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/webview?token=TOKEN_LAB_6d8372'
# WebView: overrideUrlLoading → token sink
```

## Diferencial desta nota

- Sink + contexto + cookie flags. Encadeio até ação autenticada ou token se HttpOnly falhar.

Falso amigo em WebView XSS/bridge: UI/log gritam, impacto não. Exijo Mobile threat defense.

## Onde já errei

Não publique apps modificados. Respeite store ToS e escopo.

Frida em build de teste ≠ pin quebrado na store. Deixo a nuance no report.

## Entrega

- blue: Mobile threat defense; RASP alerts; cert pinning telemetry.
- fix: Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.
- proof: Componente explorado; dado acessado; API finding correlato.

## Refs

- [MITRE ATT&CK T1420](https://attack.mitre.org/techniques/T1420/)
- [MITRE ATT&CK T1412](https://attack.mitre.org/techniques/T1412/)
- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [Frida documentation](https://frida.re/docs/home/)
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05a-Security-Testing-Android/)

## Relacionadas

- [WebView XSS/bridge — evidência](0682-mobile-android-webview--evidencia.md)
- [token em logcat](0310-mobile-android-auth.md)
- [backup enabled](0307-mobile-android-backup.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)