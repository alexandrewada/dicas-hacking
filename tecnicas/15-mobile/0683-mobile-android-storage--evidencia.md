---
id: "0683"
categoria: "15-mobile"
familia: "mobile-android"
slug: "storage"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-android", "evidencia"]
aliases: ["storage world-readable", "storage", "storage-evidencia"]
---

# storage world-readable — evidência

Pacote pra storage world-readable sobreviver peer review.

## Contexto

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## O que precisa aparecer

- Variante storage world-readable: trato separado da família `mobile-android`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Componente explorado; dado acessado; API finding correlato.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 74b37e

{"id":"obj_74b37e","owner":"USER_A","note":"redacted-storage"}
# capturado como USER_B
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
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05b-Android-Security-Testing/)

## Relacionadas

- [storage world-readable](0303-mobile-android-storage.md)
- [token em logcat](0310-mobile-android-auth.md)
- [backup enabled](0307-mobile-android-backup.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)