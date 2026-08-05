---
id: "0880"
categoria: "04-auth"
familia: "auth-oauth-oidc"
slug: "jwt-client-auth"
angulo: "hardening"
mitre: "T1528"
owasp: ""
tags: ["04-auth", "auth-oauth-oidc", "hardening", "t1528"]
aliases: ["client_assertion fraca", "jwt-client-auth", "jwt-client-auth-hardening"]
---

# client_assertion fraca — hardening

Do PoC ao controle — client_assertion fraca.

## Risco

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## Controles desta variante

- Se não validar **Chave reutilizada**, a nota fica genérica.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

## Camadas

1) Bloqueio imediato
2) IdP logs de redirect mismatch; anomaly em consent; short-lived codes.
3) Allowlist estrita de redirect_uri; PKCE; state/nonce; rotacionar secrets;
evitar implicit grant.
Reteste com o mesmo PoC — critério: a prova desta variante falha.

## Exemplo

```bash
# verificação pós-hardening jwt-client-auth
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/jwt-client-auth/ORD-7781 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 732912
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

- [client_assertion fraca](0120-auth-oauth-oidc-jwt-client-auth.md)
- [client_assertion fraca — detecção](0500-auth-oauth-oidc-jwt-client-auth--detecao.md)
- [device authorization grant abuse](0119-auth-oauth-oidc-device-code.md)
- [implicit grant legado](0114-auth-oauth-oidc-implicit.md)
- [mix-up attack (multi-IdP)](0116-auth-oauth-oidc-mixup.md)
- [PKCE ausente em public client](0113-auth-oauth-oidc-pkce.md)