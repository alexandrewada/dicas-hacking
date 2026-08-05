---
id: "0114"
categoria: "04-auth"
familia: "auth-oauth-oidc"
slug: "implicit"
angulo: "base"
mitre: "T1528"
owasp: ""
tags: ["04-auth", "auth-oauth-oidc", "base", "t1528"]
aliases: ["implicit grant legado", "implicit"]
---

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

- [MITRE ATT&CK T1528](https://attack.mitre.org/techniques/T1528/)
- [RFC 6749 — OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749)
- [RFC 8252 — OAuth for Native Apps](https://www.rfc-editor.org/rfc/rfc8252)
- [OWASP OAuth 2.0 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
- [PortSwigger — OAuth authentication](https://portswigger.net/web-security/oauth)

## Relacionadas

- [implicit grant legado — detecção](0494-auth-oauth-oidc-implicit--detecao.md)
- [implicit grant legado — path](0874-auth-oauth-oidc-implicit--path.md)
- [device authorization grant abuse](0119-auth-oauth-oidc-device-code.md)
- [client_assertion fraca](0120-auth-oauth-oidc-jwt-client-auth.md)
- [mix-up attack (multi-IdP)](0116-auth-oauth-oidc-mixup.md)
- [PKCE ausente em public client](0113-auth-oauth-oidc-pkce.md)