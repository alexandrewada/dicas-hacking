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

- RFC 6749
- RFC 8252
- OWASP OAuth