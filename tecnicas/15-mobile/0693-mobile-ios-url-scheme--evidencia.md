# URL scheme hijack — evidência

Pacote pra URL scheme hijack sobreviver peer review.

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## O que precisa aparecer

- Variante URL scheme hijack: trato separado da família `mobile-ios`.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Artefato Keychain de teste; request API.

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/obj_8d54f1 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (url-scheme)
hash_prova: 8d54f1
```

## Remediação junto

Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

## Se purple

MDM policies; ATS force; keychain audit.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

## Refs

- OWASP MASTG iOS