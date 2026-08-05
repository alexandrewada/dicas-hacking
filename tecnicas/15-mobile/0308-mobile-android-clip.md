---
id: "0308"
categoria: "15-mobile"
familia: "mobile-android"
slug: "clip"
angulo: "base"
mitre: "T1420"
owasp: ""
tags: ["15-mobile", "mobile-android", "base", "t1420"]
aliases: ["clipboard leaks", "clip"]
---

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
# Android clip — build de teste
adb shell run-as app.lab ls shared_prefs/
adb backup -f bak_62de3a.ab app.lab # só lab build
frida -U -f app.lab -l bypass_pinning.js # NÃO em prod store
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

- [MITRE ATT&CK T1420](https://attack.mitre.org/techniques/T1420/)
- [MITRE ATT&CK T1412](https://attack.mitre.org/techniques/T1412/)
- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [Frida documentation](https://frida.re/docs/home/)
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05b-Android-Security-Testing/)

## Relacionadas

- [clipboard leaks — evidência](0688-mobile-android-clip--evidencia.md)
- [token em logcat](0310-mobile-android-auth.md)
- [backup enabled](0307-mobile-android-backup.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)
- [deeplink hijack](0304-mobile-android-deeplink.md)