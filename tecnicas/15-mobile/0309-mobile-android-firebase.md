# Firebase aberto

**Mobile** · `T1420 / T1412 (mobile ATT&CK)`

## Contexto

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## O que muda aqui

- Variante Firebase misconfig: trato separado da família `mobile-android`.

## Como testo

1. Mapeio apk (jadx) e superfícies exported.
2. Instrumentar com Frida **em device de teste**.
3. Avalio storage e logs.
4. Interceptar tráfego (com pinning bypass autorizado).
5. Testo backend com tokens do app.

## Sinal / query

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/firebase?token=TOKEN_LAB_8addca'
# deep link / exported → token sink
```

## Campo

Deep link / WebView / exported: intent até token sink é o ROI.

Antes de Critical em Firebase misconfig, confiro se a telemetria que eu cobraria reagiria — Mobile threat defense; RASP alerts; cert pinning telemetry.

## Já me queimei

Não publique apps modificados. Respeite store ToS e escopo.

## Blue

- Detectar: Mobile threat defense; RASP alerts; cert pinning telemetry.
- Fechar: Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.

## Evidência

Componente explorado; dado acessado; API finding correlato.

## Refs

- OWASP MASVS/MASTG
- Frida docs