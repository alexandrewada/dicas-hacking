# WKWebView issues — evidência

Pacote pra WKWebView issues sobreviver peer review.

## Contexto

iOS: Keychain accessibility, App Transport Security exceptions, jailbreak detection theater,
URL schemes, e backup artifacts. Teste em device jailbroken de lab quando necessário.

## O que precisa aparecer

- Variante WKWebView issues: trato separado da família `mobile-ios`.

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
req: GET /…/a1b2c3d4-e5f6-7890-abcd-ef1234567890 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (webview)
hash_prova: 9e3dbb
```

## Remediação junto

Correct Keychain accessibility; ATS; disable insecure schemes; secure IPC.

## Se purple

MDM policies; ATS force; keychain audit.

## Armadilha

Não contorne DRM de terceiros fora do escopo do app do cliente.

## Refs

- OWASP MASTG iOS