---
id: "0307"
categoria: "15-mobile"
familia: "mobile-android"
slug: "backup"
angulo: "base"
mitre: "T1420"
owasp: ""
tags: ["15-mobile", "mobile-android", "base", "t1420"]
aliases: ["backup enabled", "backup"]
---

# backup enabled

`T1420 / T1412 (mobile ATT&CK)`

## Por que importa

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## Variante

- Detalhe que pago pra ver: **adb backup data**.

## Passo a passo

1. Mapeio apk (jadx) e superfícies exported.
2. Instrumentar com Frida **em device de teste**.
3. Avalio storage e logs.
4. Interceptar tráfego (com pinning bypass autorizado).
5. Testo backend com tokens do app.

## Exemplo

```bash
# Android backup — build de teste
adb shell run-as app.lab ls shared_prefs/
adb backup -f bak_4a3c18.ab app.lab # só lab build
frida -U -f app.lab -l bypass_pinning.js # NÃO em prod store
```

## Nota de operador

Frida em build de teste ≠ pin quebrado na store. Deixo a nuance no report.

## Armadilha

Não publique apps modificados. Respeite store ToS e escopo.

Falso amigo em backup enabled: UI/log gritam, impacto não. Exijo Mobile threat defense.

## Depois

Detecção — Mobile threat defense; RASP alerts; cert pinning telemetry.

Remediação — Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.

No PDF — Componente explorado; dado acessado; API finding correlato.

## Refs

- [MITRE ATT&CK T1420](https://attack.mitre.org/techniques/T1420/)
- [MITRE ATT&CK T1412](https://attack.mitre.org/techniques/T1412/)
- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [Frida documentation](https://frida.re/docs/home/)
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05b-Android-Security-Testing/)

## Relacionadas

- [backup enabled — evidência](0687-mobile-android-backup--evidencia.md)
- [token em logcat](0310-mobile-android-auth.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)
- [deeplink hijack](0304-mobile-android-deeplink.md)