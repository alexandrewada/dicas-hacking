# PKCE ausente em public client

`T1528 Steal Application Access Token`

## Por que importa

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## Variante

- **Code interception.** Sem isso o playbook da família mente.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

## Passo a passo

1. Mapeio clients (public/confidential) e grants.
2. Testo redirect_uri variations (subdomain, query truncate, parse bugs).
3. Remover/alterar state e nonce.
4. Avalio code interception e reuse.
5. Verifico vazamento de tokens em browser history e mobile WebViews.

## PoC mínimo

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=5a95cc HTTP/1.1
Host: idp.lab.local
# fluxo pkce: capturar se redirect_uri fora do allowlist passa
```

## Nota de operador

Mint → store → use → revoke. Quebro o fluxo e testo cada perna.

## Armadilha

Não roube tokens de usuários reais. Use clients de teste do cliente.

Antes de Critical em PKCE ausente em public client, confiro se a telemetria que eu cobraria reagiria — IdP logs de redirect mismatch; anomaly em consent; short-lived codes.

## Depois

Detecção — IdP logs de redirect mismatch; anomaly em consent; short-lived codes.

Remediação — Allowlist estrita de redirect_uri; PKCE; state/nonce; rotacionar secrets;
evitar implicit grant.

No PDF — PoC de redirect malicioso em client de teste; impacto no token.

## Refs

- RFC 6749
- RFC 8252
- OWASP OAuth