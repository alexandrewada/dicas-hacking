---
id: "0498"
categoria: "04-auth"
familia: "auth-oauth-oidc"
slug: "scope-escalation"
angulo: "detecao"
mitre: "T1528"
owasp: ""
tags: ["04-auth", "auth-oauth-oidc", "detecao", "t1528"]
aliases: ["scope elevation", "scope-escalation", "scope-escalation-detecao"]
---

# scope elevation — detecção

Gap de detecção em `T1528 Steal Application Access Token` / scope elevation. PoC mínimo, telemetria ligada.

## Contexto

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## Hipótese

- **Consent skip** — muda ruído e o que entra no PDF.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

## Como corro o purple

1. Confirmo log source relevante.
2. Disparo o fluxo abaixo.
3. Anoto alerta / ausência.
4. Se silêncio, abro finding de detecção.

### PoC

1. Mapeio clients (public/confidential) e grants.
2. Testo redirect_uri variations (subdomain, query truncate, parse bugs).
3. Remover/alterar state e nonce.
4. Avalio code interception e reuse.
5. Verifico vazamento de tokens em browser history e mobile WebViews.

## Sinal / query

```text
Sign-in logs: unexpected redirect_uri OR MFA skipped for USER_A
app=APP_LAB flow=scope-escalation tag=9a2a3f
```

## Sinal

IdP logs de redirect mismatch; anomaly em consent; short-lived codes.

## Freio

Não roube tokens de usuários reais. Use clients de teste do cliente.

MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.

## Evidência

PoC de redirect malicioso em client de teste; impacto no token.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1528](https://attack.mitre.org/techniques/T1528/)
- [RFC 6749 — OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749)
- [RFC 8252 — OAuth for Native Apps](https://www.rfc-editor.org/rfc/rfc8252)
- [OWASP OAuth 2.0 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
- [PortSwigger — OAuth authentication](https://portswigger.net/web-security/oauth)

## Relacionadas

- [scope elevation](0118-auth-oauth-oidc-scope-escalation.md)
- [scope elevation — hardening](0878-auth-oauth-oidc-scope-escalation--hardening.md)
- [device authorization grant abuse](0119-auth-oauth-oidc-device-code.md)
- [implicit grant legado](0114-auth-oauth-oidc-implicit.md)
- [client_assertion fraca](0120-auth-oauth-oidc-jwt-client-auth.md)
- [mix-up attack (multi-IdP)](0116-auth-oauth-oidc-mixup.md)