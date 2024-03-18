# Keychain fraco — evidência

Pacote pra Keychain fraco sobreviver peer review.

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## O que precisa aparecer

- Variante Keychain accessibility fraca: trato separado da família `mobile-ios`.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Artefato Keychain de teste; request API.

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: 0c397d

{"id":"a1b2c3d4-e5f6-7890-abcd-ef1234567890","owner":"USER_A","note":"redacted-keychain"}
# capturado como USER_B
```

## Remediação junto

Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

## Se purple

MDM policies; ATS force; keychain audit.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

## Refs

- OWASP MASTG iOS