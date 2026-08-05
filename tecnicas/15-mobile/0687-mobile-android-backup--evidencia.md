---
id: "0687"
categoria: "15-mobile"
familia: "mobile-android"
slug: "backup"
angulo: "evidencia"
mitre: "T1420"
owasp: ""
tags: ["15-mobile", "mobile-android", "evidencia", "t1420"]
aliases: ["backup enabled", "backup", "backup-evidencia"]
---

# backup enabled — evidência

Pacote pra backup enabled sobreviver peer review.

## Contexto

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## O que precisa aparecer

- Detalhe que pago pra ver: **adb backup data**.

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

## PoC mínimo

```text
--- evidência redigida ---
req: GET /…/a1b2c3d4-e5f6-7890-abcd-ef1234567890 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (backup)
hash_prova: 10ef19
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

- [backup enabled](0307-mobile-android-backup.md)
- [token em logcat](0310-mobile-android-auth.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)
- [deeplink hijack](0304-mobile-android-deeplink.md)