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

- RFC 6749
- RFC 8252
- OWASP OAuth