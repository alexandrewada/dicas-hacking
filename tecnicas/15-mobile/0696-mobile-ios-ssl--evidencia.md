---
id: "0696"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "ssl"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "evidencia"]
aliases: ["SSL kill switch lab", "ssl", "ssl-evidencia"]
---

# SSL kill switch lab — evidência

Pacote pra SSL kill switch lab sobreviver peer review.

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## O que precisa aparecer

- Variante SSL kill switch lab: trato separado da família `mobile-ios`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Artefato Keychain de teste; request API.

## Exemplo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 4ca607

{"id":"ORD-7781","owner":"USER_A","note":"redacted-ssl"}
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

- [SSL kill switch lab](0316-mobile-ios-ssl.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)