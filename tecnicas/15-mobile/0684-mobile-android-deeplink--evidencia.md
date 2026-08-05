---
id: "0684"
categoria: "15-mobile"
familia: "mobile-android"
slug: "deeplink"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-android", "evidencia"]
aliases: ["deeplink hijack", "deeplink", "deeplink-evidencia"]
---

# deeplink hijack — evidência

Pacote pra deeplink hijack sobreviver peer review.

## Contexto

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## O que precisa aparecer

- Variante deeplink hijack: trato separado da família `mobile-android`.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Componente explorado; dado acessado; API finding correlato.

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/obj_fd4f8c Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (deeplink)
hash_prova: fd4f8c
```

## Remediação junto

Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.

## Se purple

Mobile threat defense; RASP alerts; cert pinning telemetry.

## Armadilha

Não publique apps modificados. Respeite store ToS e escopo.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [Frida documentation](https://frida.re/docs/home/)
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05a-Security-Testing-Android/)

## Relacionadas

- [deeplink hijack](0304-mobile-android-deeplink.md)
- [token em logcat](0310-mobile-android-auth.md)
- [backup enabled](0307-mobile-android-backup.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)
- [WebView XSS/bridge (path)](0302-mobile-android-webview.md)
- [storage world-readable (path)](0303-mobile-android-storage.md)