# activity/service exported

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
  -d 'app://lab/exported?token=TOKEN_LAB_cc9a61'
# deep link / exported → token sink
```

## Diferencial desta nota

- **IPC abuse.** Sem isso o playbook da família mente.

Antes de Critical em activity/service exported, confiro se a telemetria que eu cobraria reagiria — Mobile threat defense; RASP alerts; cert pinning telemetry.

## Onde já errei

Não publique apps modificados. Respeite store ToS e escopo.

Deep link / WebView / exported: intent até token sink é o ROI.

## Entrega

- blue: Mobile threat defense; RASP alerts; cert pinning telemetry.
- fix: Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.
- proof: Componente explorado; dado acessado; API finding correlato.

## Refs

- OWASP MASVS/MASTG
- Frida docs