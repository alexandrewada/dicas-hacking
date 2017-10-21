# PKCE ausente em public client — detecção

Gap de detecção em `T1528 Steal Application Access Token` / PKCE ausente em public client. PoC mínimo, telemetria ligada.

## Contexto

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## Hipótese

- **Code interception.** Sem isso o playbook da família mente.
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

## Exemplo

```text
Sign-in logs: unexpected redirect_uri OR MFA skipped for USER_A
app=APP_LAB flow=pkce tag=146379
```

## Sinal

IdP logs de redirect mismatch; anomaly em consent; short-lived codes.

## Freio

Não roube tokens de usuários reais. Use clients de teste do cliente.

Mint → store → use → revoke. Quebro o fluxo e testo cada perna.

## Evidência

PoC de redirect malicioso em client de teste; impacto no token.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- RFC 6749
- RFC 8252
- OWASP OAuth