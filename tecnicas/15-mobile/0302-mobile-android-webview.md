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
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/webview?token=TOKEN_LAB_6d8372'
# deep link / exported → token sink
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

- OWASP MASVS/MASTG
- Frida docs