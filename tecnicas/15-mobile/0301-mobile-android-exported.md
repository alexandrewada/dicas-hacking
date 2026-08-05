---
id: "0301"
categoria: "15-mobile"
familia: "mobile-android"
slug: "exported"
angulo: "base"
mitre: "T1420"
owasp: ""
tags: ["15-mobile", "mobile-android", "base", "t1420"]
aliases: ["activity/service exported", "exported"]
---

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
# Android lab build — sem store
adb shell dumpsys package app.lab | grep -A2 exported=true
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/exported?token=TOKEN_LAB_cc9a61'
# WebView: overrideUrlLoading → token sink
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

- [MITRE ATT&CK T1420](https://attack.mitre.org/techniques/T1420/)
- [MITRE ATT&CK T1412](https://attack.mitre.org/techniques/T1412/)
- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [Frida documentation](https://frida.re/docs/home/)
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05b-Android-Security-Testing/)

## Relacionadas

- [activity/service exported — evidência](0681-mobile-android-exported--evidencia.md)
- [token em logcat](0310-mobile-android-auth.md)
- [backup enabled](0307-mobile-android-backup.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)