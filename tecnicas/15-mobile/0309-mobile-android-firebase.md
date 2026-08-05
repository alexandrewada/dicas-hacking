---
id: "0309"
categoria: "15-mobile"
familia: "mobile-android"
slug: "firebase"
angulo: "base"
mitre: "T1420"
owasp: ""
tags: ["15-mobile", "mobile-android", "base", "t1420"]
aliases: ["Firebase aberto", "firebase"]
---

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

- [MITRE ATT&CK T1420](https://attack.mitre.org/techniques/T1420/)
- [MITRE ATT&CK T1412](https://attack.mitre.org/techniques/T1412/)
- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [Frida documentation](https://frida.re/docs/home/)
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05a-Security-Testing-Android/)

## Relacionadas

- [Firebase aberto — evidência](0689-mobile-android-firebase--evidencia.md)
- [token em logcat](0310-mobile-android-auth.md)
- [backup enabled](0307-mobile-android-backup.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)