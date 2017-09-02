# implicit grant legado

**A01 / A07** · `T1528 Steal Application Access Token`

## Contexto

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## O que muda aqui

- Detalhe que pago pra ver: **Token no fragment**.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

## Como testo

1. Mapeio clients (public/confidential) e grants.
2. Testo redirect_uri variations (subdomain, query truncate, parse bugs).
3. Remover/alterar state e nonce.
4. Avalio code interception e reuse.
5. Verifico vazamento de tokens em browser history e mobile WebViews.

## Sinal / query

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=c925e4 HTTP/1.1
Host: idp.lab.local
# fluxo implicit: capturar se redirect_uri fora do allowlist passa
```

## Campo

Mint → store → use → revoke. Quebro o fluxo e testo cada perna.

Já abri High demais em implicit grant legado por sintoma sem efeito. Cruzei com: IdP logs de redirect mismatch; anomaly em consent; short-lived codes. Sem side-effect, baixo.

## Já me queimei

Não roube tokens de usuários reais. Use clients de teste do cliente.

## Blue

- Detectar: IdP logs de redirect mismatch; anomaly em consent; short-lived codes.
- Fechar: Allowlist estrita de redirect_uri; PKCE; state/nonce; rotacionar secrets;
evitar implicit grant.

## Evidência

PoC de redirect malicioso em client de teste; impacto no token.

## Refs

- RFC 6749
- RFC 8252
- OWASP OAuth