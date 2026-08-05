---
id: "0305"
categoria: "15-mobile"
familia: "mobile-android"
slug: "pinning"
angulo: "base"
mitre: "T1420"
owasp: ""
tags: ["15-mobile", "mobile-android", "base", "t1420"]
aliases: ["pinning bypass lab", "pinning"]
---

# pinning bypass lab

**Mobile** · `T1420 / T1412 (mobile ATT&CK)`

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

**Variante:** **Para testar API** — muda ruído e o que entra no PDF. Bypass em debug build ≠ ausência de pin na store.

**Método**

1. Mapeio apk (jadx) e superfícies exported.
2. Instrumentar com Frida **em device de teste**.
3. Avalio storage e logs.
4. Interceptar tráfego (com pinning bypass autorizado).
5. Testo backend com tokens do app.

## PoC mínimo

```bash
# Android pinning — build de teste
adb shell run-as app.lab ls shared_prefs/
adb backup -f bak_5cd37a.ab app.lab # só lab build
frida -U -f app.lab -l bypass_pinning.js # NÃO em prod store
```

**Freio:** Não publique apps modificados. Respeite store ToS e escopo.

Já abri High demais em pinning bypass lab por sintoma sem efeito. Cruzei com: Mobile threat defense; RASP alerts; cert pinning telemetry. Sem side-effect, baixo.

Detecto via: Mobile threat defense; RASP alerts; cert pinning telemetry.

Corrijo com: Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.

Levo no report: Componente explorado; dado acessado; API finding correlato.

## Refs

- [MITRE ATT&CK T1420](https://attack.mitre.org/techniques/T1420/)
- [MITRE ATT&CK T1412](https://attack.mitre.org/techniques/T1412/)
- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [Frida documentation](https://frida.re/docs/home/)
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05a-Security-Testing-Android/)

## Relacionadas

- [pinning bypass lab — evidência](0685-mobile-android-pinning--evidencia.md)
- [token em logcat](0310-mobile-android-auth.md)
- [backup enabled](0307-mobile-android-backup.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)