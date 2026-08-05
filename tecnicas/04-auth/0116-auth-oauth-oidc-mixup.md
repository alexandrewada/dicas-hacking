---
id: "0116"
categoria: "04-auth"
familia: "auth-oauth-oidc"
slug: "mixup"
angulo: "base"
mitre: "T1528"
owasp: ""
tags: ["04-auth", "auth-oauth-oidc", "base", "t1528"]
aliases: ["mix-up attack (multi-IdP)", "mixup"]
---

# mix-up attack (multi-IdP)

## Contexto

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## Detalhe

- **iss validation** — muda ruído e o que entra no PDF.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

## Execução

1. Mapeio clients (public/confidential) e grants.
2. Testo redirect_uri variations (subdomain, query truncate, parse bugs).
3. Remover/alterar state e nonce.
4. Avalio code interception e reuse.
5. Verifico vazamento de tokens em browser history e mobile WebViews.

## No lab ficou assim

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=d1347d HTTP/1.1
Host: idp.lab.local
# fluxo mixup: capturar se redirect_uri fora do allowlist passa
```

## OpSec

MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.

## Cuidados

Não roube tokens de usuários reais. Use clients de teste do cliente.

## Fechamento

| | |
|---|---|
| Detecção | IdP logs de redirect mismatch; anomaly em consent; short-lived codes. |
| Remediação | Allowlist estrita de redirect_uri; PKCE; state/nonce; rotacionar secrets;
evitar implicit grant. |
| Evidência | PoC de redirect malicioso em client de teste; impacto no token. |

## Refs

- [MITRE ATT&CK T1528](https://attack.mitre.org/techniques/T1528/)
- [RFC 6749 — OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749)
- [RFC 8252 — OAuth for Native Apps](https://www.rfc-editor.org/rfc/rfc8252)
- [OWASP OAuth 2.0 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
- [PortSwigger — OAuth authentication](https://portswigger.net/web-security/oauth)

## Relacionadas

- [mix-up attack (multi-IdP) — detecção](0496-auth-oauth-oidc-mixup--detecao.md)
- [mix-up attack (multi-IdP) — path](0876-auth-oauth-oidc-mixup--path.md)
- [device authorization grant abuse](0119-auth-oauth-oidc-device-code.md)
- [implicit grant legado](0114-auth-oauth-oidc-implicit.md)
- [client_assertion fraca](0120-auth-oauth-oidc-jwt-client-auth.md)
- [PKCE ausente em public client](0113-auth-oauth-oidc-pkce.md)