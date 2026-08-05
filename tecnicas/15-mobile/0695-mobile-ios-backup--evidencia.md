---
id: "0695"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "backup"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "evidencia"]
aliases: ["itunes backup secrets", "backup", "backup-evidencia"]
---

# itunes backup secrets — evidência

Pacote pra itunes backup secrets sobreviver peer review.

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## O que precisa aparecer

- Variante itunes backup secrets: trato separado da família `mobile-ios`.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Artefato Keychain de teste; request API.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: c5b066

{"id":"usr_01HZX","owner":"USER_A","note":"redacted-backup"}
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

- [itunes backup secrets](0315-mobile-ios-backup.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)
- [Keychain fraco](0311-mobile-ios-keychain.md)