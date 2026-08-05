---
id: "0692"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "ats"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "evidencia"]
aliases: ["ATS exceptions", "ats", "ats-evidencia"]
---

# ATS exceptions — evidência

Pacote pra ATS exceptions sobreviver peer review.

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## O que precisa aparecer

- Variante ATS exceptions: trato separado da família `mobile-ios`.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Artefato Keychain de teste; request API.

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 339d83

{"id":"ORD-7781","owner":"USER_A","note":"redacted-ats"}
# capturado como USER_B
```

## Remediação junto

Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

## Se purple

MDM policies; ATS force; keychain audit.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

## Refs

- [OWASP MASTG](https://mas.owasp.org/MASTG/)
- [OWASP MASTG — iOS](https://mas.owasp.org/MASTG/0x06b-iOS-Security-Testing/)
- [Frida documentation](https://frida.re/docs/home/)

## Relacionadas

- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)
- [Keychain fraco](0311-mobile-ios-keychain.md)