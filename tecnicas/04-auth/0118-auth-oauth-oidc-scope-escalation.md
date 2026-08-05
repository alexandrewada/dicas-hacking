---
id: "0118"
categoria: "04-auth"
familia: "auth-oauth-oidc"
slug: "scope-escalation"
angulo: "base"
mitre: "T1528"
owasp: ""
tags: ["04-auth", "auth-oauth-oidc", "base", "t1528"]
aliases: ["scope elevation", "scope-escalation"]
---

# scope elevation

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

## No lab ficou assim

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=604465 HTTP/1.1
Host: idp.lab.local
# fluxo scope-escalation: capturar se redirect_uri fora do allowlist passa
```

## Diferencial desta nota

- **Consent skip** — muda ruído e o que entra no PDF.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

scope elevation: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: IdP logs de redirect mismatch; anomaly em consent; short-lived codes.

## Onde já errei

Não roube tokens de usuários reais. Use clients de teste do cliente.

MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.

## Entrega

- blue: IdP logs de redirect mismatch; anomaly em consent; short-lived codes.
- fix: Allowlist estrita de redirect_uri; PKCE; state/nonce; rotacionar secrets;
evitar implicit grant.
- proof: PoC de redirect malicioso em client de teste; impacto no token.

## Refs

- [MITRE ATT&CK T1528](https://attack.mitre.org/techniques/T1528/)
- [RFC 6749 — OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749)
- [RFC 8252 — OAuth for Native Apps](https://www.rfc-editor.org/rfc/rfc8252)
- [OWASP OAuth 2.0 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
- [PortSwigger — OAuth authentication](https://portswigger.net/web-security/oauth)

## Relacionadas

- [scope elevation — detecção](0498-auth-oauth-oidc-scope-escalation--detecao.md)
- [scope elevation — hardening](0878-auth-oauth-oidc-scope-escalation--hardening.md)
- [device authorization grant abuse](0119-auth-oauth-oidc-device-code.md)
- [implicit grant legado](0114-auth-oauth-oidc-implicit.md)
- [client_assertion fraca](0120-auth-oauth-oidc-jwt-client-auth.md)
- [mix-up attack (multi-IdP)](0116-auth-oauth-oidc-mixup.md)