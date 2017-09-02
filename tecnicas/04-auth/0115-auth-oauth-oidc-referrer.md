# leak via Referer

**A01 / A07** · `T1528 Steal Application Access Token`

## Contexto

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## Como eu faço

1. Mapeio clients (public/confidential) e grants.
2. Testo redirect_uri variations (subdomain, query truncate, parse bugs).
3. Remover/alterar state e nonce.
4. Avalio code interception e reuse.
5. Verifico vazamento de tokens em browser history e mobile WebViews.

## Exemplo

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=7c599b HTTP/1.1
Host: idp.lab.local
# fluxo referrer: capturar se redirect_uri fora do allowlist passa
```

## Diferencial desta nota

- Detalhe que pago pra ver: **HTTPS→HTTP ou HTML injection**.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

Falso amigo em leak via Referer: UI/log gritam, impacto não. Exijo IdP logs de redirect mismatch.

## Onde já errei

Não roube tokens de usuários reais. Use clients de teste do cliente.

Mint → store → use → revoke. Quebro o fluxo e testo cada perna.

## Entrega

- blue: IdP logs de redirect mismatch; anomaly em consent; short-lived codes.
- fix: Allowlist estrita de redirect_uri; PKCE; state/nonce; rotacionar secrets;
evitar implicit grant.
- proof: PoC de redirect malicioso em client de teste; impacto no token.

## Refs

- RFC 6749
- RFC 8252
- OWASP OAuth