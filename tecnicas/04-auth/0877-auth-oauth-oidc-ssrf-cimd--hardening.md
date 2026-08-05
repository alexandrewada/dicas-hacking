---
id: "0877"
categoria: "04-auth"
familia: "auth-oauth-oidc"
slug: "ssrf-cimd"
angulo: "hardening"
mitre: "T1528"
owasp: ""
tags: ["04-auth", "auth-oauth-oidc", "hardening", "t1528"]
aliases: ["SSRF em client registration", "ssrf-cimd", "ssrf-cimd-hardening"]
---

# SSRF em client registration — hardening

Do PoC ao controle — SSRF em client registration.

## Risco

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## Controles desta variante

- **Dynamic registration.** Sem isso o playbook da família mente.
- Mostro role/creds ou doc interno. Redirect trick só conta se mudar alcance real.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

## Camadas

Hotfix: quebra a exploração direta de SSRF em client registration.
Detectivo: IdP logs de redirect mismatch; anomaly em consent; short-lived codes.
Estrutural: Allowlist estrita de redirect_uri; PKCE; state/nonce; rotacionar secrets;
evitar implicit grant.

## No lab ficou assim

```bash
# verificação pós-hardening ssrf-cimd
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/ssrf-cimd/usr_01HZX \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 21de55
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

- [SSRF em client registration](0117-auth-oauth-oidc-ssrf-cimd.md)
- [SSRF em client registration — detecção](0497-auth-oauth-oidc-ssrf-cimd--detecao.md)
- [device authorization grant abuse](0119-auth-oauth-oidc-device-code.md)
- [implicit grant legado](0114-auth-oauth-oidc-implicit.md)
- [client_assertion fraca](0120-auth-oauth-oidc-jwt-client-auth.md)
- [mix-up attack (multi-IdP)](0116-auth-oauth-oidc-mixup.md)