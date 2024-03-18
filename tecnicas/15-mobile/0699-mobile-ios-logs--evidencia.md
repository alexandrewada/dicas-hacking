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

- OWASP MASTG iOS