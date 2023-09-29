# clipboard leaks

**Mobile** · `T1420 / T1412 (mobile ATT&CK)`

## Contexto

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## O que muda aqui

- Variante clipboard leaks: trato separado da família `mobile-android`.

## Como testo

1. Mapeio apk (jadx) e superfícies exported.
2. Instrumentar com Frida **em device de teste**.
3. Avalio storage e logs.
4. Interceptar tráfego (com pinning bypass autorizado).
5. Testo backend com tokens do app.

## Exemplo

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/clip?token=TOKEN_LAB_62de3a'
# deep link / exported → token sink
```

## Campo

Deep link / WebView / exported: intent até token sink é o ROI.

Falso amigo em clipboard leaks: UI/log gritam, impacto não. Exijo Mobile threat defense.

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