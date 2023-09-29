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
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/deeplink?token=TOKEN_LAB_49f6dc'
# deep link / exported → token sink
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

- OWASP MASVS/MASTG
- Frida docs