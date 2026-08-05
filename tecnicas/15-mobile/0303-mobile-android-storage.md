---
id: "0303"
categoria: "15-mobile"
familia: "mobile-android"
slug: "storage"
angulo: "base"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-android", "base"]
aliases: ["storage world-readable", "storage"]
---

# storage world-readable

## Leitura rápida

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## Foco

- Variante storage world-readable: trato separado da família `mobile-android`.

## Mãos na massa

1. Mapeio apk (jadx) e superfícies exported.
2. Instrumentar com Frida **em device de teste**.
3. Avalio storage e logs.
4. Interceptar tráfego (com pinning bypass autorizado).
5. Testo backend com tokens do app.

## Sinal / query

```bash
# Android storage — build de teste
adb shell run-as app.lab ls shared_prefs/
adb backup -f bak_453090.ab app.lab # só lab build
frida -U -f app.lab -l bypass_pinning.js # NÃO em prod store
```

Frida em build de teste ≠ pin quebrado na store. Deixo a nuance no report.

## Pitfall

Não publique apps modificados. Respeite store ToS e escopo.

## Detecção / remediação

Mobile threat defense; RASP alerts; cert pinning telemetry.

→ Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.

## Prova

Componente explorado; dado acessado; API finding correlato.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [Frida documentation](https://frida.re/docs/home/)
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05a-Security-Testing-Android/)

## Relacionadas

- [storage world-readable — evidência](0683-mobile-android-storage--evidencia.md)
- [token em logcat](0310-mobile-android-auth.md)
- [backup enabled](0307-mobile-android-backup.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)