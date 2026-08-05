---
id: "0688"
categoria: "15-mobile"
familia: "mobile-android"
slug: "clip"
angulo: "evidencia"
mitre: "T1420"
owasp: ""
tags: ["15-mobile", "mobile-android", "evidencia", "t1420"]
aliases: ["clipboard leaks", "clip", "clip-evidencia"]
---

# clipboard leaks — evidência

Pacote pra clipboard leaks sobreviver peer review.

## Contexto

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## O que precisa aparecer

- Variante clipboard leaks: trato separado da família `mobile-android`.

## Checklist

- ROE cobre
- ambiente/versão
- identidade de teste
- PoC redigido
- impacto 2–3 frases
- hotfix + estrutural
- cleanup
- MITRE/OWASP

## Mínimo que eu aceito

Componente explorado; dado acessado; API finding correlato.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 2ad066

{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","owner":"USER_A","note":"redacted-clip"}
# capturado como USER_B
```

## Remediação junto

Android Keystore; non-exported components; WebView harden; SSL pinning + reporting.

## Se purple

Mobile threat defense; RASP alerts; cert pinning telemetry.

## Armadilha

Não publique apps modificados. Respeite store ToS e escopo.

## Refs

- [MITRE ATT&CK T1420](https://attack.mitre.org/techniques/T1420/)
- [MITRE ATT&CK T1412](https://attack.mitre.org/techniques/T1412/)
- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [Frida documentation](https://frida.re/docs/home/)
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05b-Android-Security-Testing/)

## Relacionadas

- [clipboard leaks](0308-mobile-android-clip.md)
- [token em logcat](0310-mobile-android-auth.md)
- [backup enabled](0307-mobile-android-backup.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)
- [deeplink hijack](0304-mobile-android-deeplink.md)