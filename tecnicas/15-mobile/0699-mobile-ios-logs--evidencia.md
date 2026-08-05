---
id: "0699"
categoria: "15-mobile"
familia: "mobile-ios"
slug: "logs"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["15-mobile", "mobile-ios", "evidencia"]
aliases: ["os_log secrets", "logs", "logs-evidencia"]
---

# os_log secrets — evidência

Pacote pra os_log secrets sobreviver peer review.

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## O que precisa aparecer

- Variante os_log secrets: trato separado da família `mobile-ios`.

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

```text
--- evidência redigida ---
req: GET /…/obj_ab849f Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (logs)
hash_prova: ab849f
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

- [os_log secrets](0319-mobile-ios-logs.md)
- [ATS exceptions](0312-mobile-ios-ats.md)
- [itunes backup secrets](0315-mobile-ios-backup.md)
- [biometry bypass lab](0317-mobile-ios-biometry.md)
- [app groups misuse](0318-mobile-ios-ipc.md)