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

- OWASP MASTG iOS