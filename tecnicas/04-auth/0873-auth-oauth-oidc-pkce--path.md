---
id: "0873"
categoria: "04-auth"
familia: "auth-oauth-oidc"
slug: "pkce"
angulo: "path"
mitre: "T1528"
owasp: ""
tags: ["04-auth", "auth-oauth-oidc", "path", "t1528"]
aliases: ["PKCE ausente em public client", "pkce", "pkce-path"]
---

# PKCE ausente em public client — path

PKCE ausente em public client como pivô. Path curto > monte de finding isolado.

## Papel

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## Por que pivota

- **Code interception.** Sem isso o playbook da família mente.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

## Cadeia

1. Entrada (escopo)
2. Pivô: PKCE ausente em public client
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Mapeio clients (public/confidential) e grants.
2. Testo redirect_uri variations (subdomain, query truncate, parse bugs).
3. Remover/alterar state e nonce.
4. Avalio code interception e reuse.
5. Verifico vazamento de tokens em browser history e mobile WebViews.

## No lab ficou assim

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=a6b001 HTTP/1.1
Host: idp.lab.local
# fluxo pkce: capturar se redirect_uri fora do allowlist passa
```

## Freio

Não roube tokens de usuários reais. Use clients de teste do cliente.

## No caminho

Detectar: IdP logs de redirect mismatch; anomaly em consent; short-lived codes.

Remediar: Allowlist estrita de redirect_uri; PKCE; state/nonce; rotacionar secrets;
evitar implicit grant.

## Prova

PoC de redirect malicioso em client de teste; impacto no token.

Mint → store → use → revoke. Quebro o fluxo e testo cada perna.

## Refs

- [MITRE ATT&CK T1528](https://attack.mitre.org/techniques/T1528/)
- [RFC 6749 — OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749)
- [RFC 8252 — OAuth for Native Apps](https://www.rfc-editor.org/rfc/rfc8252)
- [OWASP OAuth 2.0 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
- [PortSwigger — OAuth authentication](https://portswigger.net/web-security/oauth)

## Relacionadas

- [PKCE ausente em public client](0113-auth-oauth-oidc-pkce.md)
- [PKCE ausente em public client — detecção](0493-auth-oauth-oidc-pkce--detecao.md)
- [device authorization grant abuse](0119-auth-oauth-oidc-device-code.md)
- [implicit grant legado](0114-auth-oauth-oidc-implicit.md)
- [client_assertion fraca](0120-auth-oauth-oidc-jwt-client-auth.md)
- [mix-up attack (multi-IdP)](0116-auth-oauth-oidc-mixup.md)