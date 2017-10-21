# device authorization grant abuse — hardening

Do PoC ao controle — device authorization grant abuse.

## Risco

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## Controles desta variante

- **Phishing de código** — muda ruído e o que entra no PDF.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

## Camadas

Hotfix: quebra a exploração direta de device authorization grant abuse.
Detectivo: IdP logs de redirect mismatch; anomaly em consent; short-lived codes.
Estrutural: Allowlist estrita de redirect_uri; PKCE; state/nonce; rotacionar secrets;
evitar implicit grant.

## Exemplo

```bash
# verificação pós-hardening device-code
curl -sk -o /dev/null -w '%{http_code}\n' https://app.lab.local/device-code/ORD-7781 \
  -H 'Cookie: session=USER_B'
# esperado 403 — tag 98cf11
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