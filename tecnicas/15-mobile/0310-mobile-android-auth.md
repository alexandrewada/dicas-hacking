---
id: "0310"
categoria: "15-mobile"
familia: "mobile-android"
slug: "auth"
angulo: "base"
mitre: "T1420"
owasp: ""
tags: ["15-mobile", "mobile-android", "base", "t1420"]
aliases: ["token em logcat", "auth"]
---

# token em logcat

**Mobile** · `T1420 / T1412 (mobile ATT&CK)`

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

**Variante:** Variante token em logcat: trato separado da família `mobile-android`.

**Método**

1. Mapeio apk (jadx) e superfícies exported.
2. Instrumentar com Frida **em device de teste**.
3. Avalio storage e logs.
4. Interceptar tráfego (com pinning bypass autorizado).
5. Testo backend com tokens do app.

## Exemplo

```bash
# mobile lab build — sem store production
adb shell am start -a android.intent.action.VIEW \
  -d 'app://lab/auth?token=TOKEN_LAB_527c9f'
# deep link / exported → token sink
```

**Freio:** Não publique apps modificados. Respeite store ToS e escopo.

Já abri High demais em token em logcat por sintoma sem efeito. Cruzei com: Mobile threat defense; RASP alerts; cert pinning telemetry. Sem side-effect, baixo.

Detecto via: Mobile threat defense; RASP alerts; cert pinning telemetry.

Corrijo com: Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.

Levo no report: Componente explorado; dado acessado; API finding correlato.

## Refs

- [MITRE ATT&CK T1420](https://attack.mitre.org/techniques/T1420/)
- [MITRE ATT&CK T1412](https://attack.mitre.org/techniques/T1412/)
- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [Frida documentation](https://frida.re/docs/home/)
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05b-Android-Security-Testing/)

## Relacionadas

- [token em logcat — evidência](0690-mobile-android-auth--evidencia.md)
- [backup enabled](0307-mobile-android-backup.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)
- [deeplink hijack](0304-mobile-android-deeplink.md)