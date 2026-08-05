---
id: "0878"
categoria: "04-auth"
familia: "auth-oauth-oidc"
slug: "scope-escalation"
angulo: "hardening"
mitre: "T1528"
owasp: ""
tags: ["04-auth", "auth-oauth-oidc", "hardening", "t1528"]
aliases: ["scope elevation", "scope-escalation", "scope-escalation-hardening"]
---

# scope elevation — hardening

Do PoC ao controle — scope elevation.

## Risco

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## Controles desta variante

- **Consent skip** — muda ruído e o que entra no PDF.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

## Camadas

Controle que fecha: Allowlist estrita de redirect_uri; PKCE; state/nonce; rotacionar secrets;
evitar implicit grant.
Sinal que deveria existir: IdP logs de redirect mismatch; anomaly em consent; short-lived codes.

## No lab ficou assim

```bash
# verificação pós-hardening scope-escalation
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/scope-escalation/ORD-7781 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag aa9fe0
```

## Armadilha

Não roube tokens de usuários reais. Use clients de teste do cliente.

## Antes/depois

PoC de redirect malicioso em client de teste; impacto no token.

Aceite de risco só por escrito, com prazo.

## Refs

- [MITRE ATT&CK T1528](https://attack.mitre.org/techniques/T1528/)
- [RFC 6749 — OAuth 2.0](https://www.rfc-editor.org/rfc/rfc6749)
- [RFC 8252 — OAuth for Native Apps](https://www.rfc-editor.org/rfc/rfc8252)
- [OWASP OAuth 2.0 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
- [PortSwigger — OAuth authentication](https://portswigger.net/web-security/oauth)

## Relacionadas

- [scope elevation](0118-auth-oauth-oidc-scope-escalation.md)
- [scope elevation — detecção](0498-auth-oauth-oidc-scope-escalation--detecao.md)
- [device authorization grant abuse](0119-auth-oauth-oidc-device-code.md)
- [implicit grant legado](0114-auth-oauth-oidc-implicit.md)
- [client_assertion fraca](0120-auth-oauth-oidc-jwt-client-auth.md)
- [mix-up attack (multi-IdP)](0116-auth-oauth-oidc-mixup.md)