# storage world-readable

## Leitura rápida

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## Foco

- Variante storage world-readable: trato separado da família `mobile-android`.

## Mãos na massa

1. Mapeio apk (jadx) e superfícies exported.
2. Instrumentar com Frida **em device de teste**.
3. Avalio storage e logs.
4. Interceptar tráfego (com pinning bypass autorizado).
5. Testo backend com tokens do app.

## Sinal / query

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/storage?token=TOKEN_LAB_453090'
# deep link / exported → token sink
```

Frida em build de teste ≠ pin quebrado na store. Deixo a nuance no report.

## Pitfall

Não publique apps modificados. Respeite store ToS e escopo.

## Detecção / remediação

Mobile threat defense; RASP alerts; cert pinning telemetry.

→ Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.

## Prova

Componente explorado; dado acessado; API finding correlato.

## Refs

- OWASP MASVS/MASTG
- Frida docs