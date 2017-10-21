# mix-up attack (multi-IdP) — path

mix-up attack (multi-IdP) como pivô. Path curto > monte de finding isolado.

## Papel

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## Por que pivota

- **iss validation** — muda ruído e o que entra no PDF.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

## Cadeia

1. Entrada (escopo)
2. Pivô: mix-up attack (multi-IdP)
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Mapeio clients (public/confidential) e grants.
2. Testo redirect_uri variations (subdomain, query truncate, parse bugs).
3. Remover/alterar state e nonce.
4. Avalio code interception e reuse.
5. Verifico vazamento de tokens em browser history e mobile WebViews.

## Sinal / query

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=1e45c9 HTTP/1.1
Host: idp.lab.local
# fluxo mixup: capturar se redirect_uri fora do allowlist passa
```

## Freio

Não roube tokens de usuários reais. Use clients de teste do cliente.

## No caminho

Detectar: IdP logs de redirect mismatch; anomaly em consent; short-lived codes.

Remediar: Allowlist estrita de redirect_uri; PKCE; state/nonce; rotacionar secrets;
evitar implicit grant.

## Prova

PoC de redirect malicioso em client de teste; impacto no token.

MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.

## Refs

- RFC 6749
- RFC 8252
- OWASP OAuth