---
id: "0685"
categoria: "15-mobile"
familia: "mobile-android"
slug: "pinning"
angulo: "evidencia"
mitre: "T1420"
owasp: ""
tags: ["15-mobile", "mobile-android", "evidencia", "t1420"]
aliases: ["pinning bypass lab", "pinning", "pinning-evidencia"]
---

# pinning bypass lab — evidência

Pacote pra pinning bypass lab sobreviver peer review.

## Contexto

Android: dados em SharedPreferences/SQLite sem encryption, exported components,
deeplinks, WebView JS bridges, certificate pinning bypass em lab, e API backend IDOR.
Foco em impacto em dados e auth, não só em root detection bypass cosmético.

## O que precisa aparecer

- **Para testar API** — muda ruído e o que entra no PDF.
- Bypass em debug build ≠ ausência de pin na store.

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
req: GET /…/10042 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (pinning)
hash_prova: 83ff9d
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
- [OWASP MASTG — Android](https://mas.owasp.org/MASTG/0x05a-Security-Testing-Android/)

## Relacionadas

- [pinning bypass lab](0305-mobile-android-pinning.md)
- [token em logcat](0310-mobile-android-auth.md)
- [backup enabled](0307-mobile-android-backup.md)
- [clipboard leaks](0308-mobile-android-clip.md)
- [crypto caseira fraca](0306-mobile-android-crypto.md)