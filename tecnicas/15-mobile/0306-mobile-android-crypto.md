---
id: "0306"
categoria: "15-mobile"
familia: "mobile-android"
slug: "crypto"
angulo: "base"
mitre: "T1420"
owasp: ""
tags: ["15-mobile", "mobile-android", "base", "t1420"]
aliases: ["crypto caseira fraca", "crypto"]
---

# crypto caseira fraca

**Mobile** · `T1420 / T1412 (mobile ATT&CK)`

## Contexto

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## O que muda aqui

- Se não validar **ECB, hardcoded keys**, a nota fica genérica.

## Como testo

1. Mapeio apk (jadx) e superfícies exported.
2. Instrumentar com Frida **em device de teste**.
3. Avalio storage e logs.
4. Interceptar tráfego (com pinning bypass autorizado).
5. Testo backend com tokens do app.

## Exemplo

```bash
# Android crypto — build de teste
adb shell run-as app.lab ls shared_prefs/
adb backup -f bak_a0eba8.ab app.lab # só lab build
frida -U -f app.lab -l bypass_pinning.js # NÃO em prod store
```

## Campo

Deep link / WebView / exported: intent até token sink é o ROI.

Já abri High demais em crypto caseira fraca por sintoma sem efeito. Cruzei com: Mobile threat defense; RASP alerts; cert pinning telemetry. Sem side-effect, baixo.

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

- [crypto caseira fraca — evidência](0686-mobile-android-crypto--evidencia.md)
- [token em logcat](0310-mobile-android-auth.md)
- [backup enabled](0307-mobile-android-backup.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [deeplink hijack](0304-mobile-android-deeplink.md)