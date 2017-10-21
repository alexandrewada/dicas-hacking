# device authorization grant abuse — detecção

Se o SOC não vê device authorization grant abuse, o finding é de cobertura, não de ego ofensivo.

## Contexto

Falhas clássicas: redirect_uri frouxo, mixed HTTP, state/nonce ausentes, code replay,
token leak em referrer/logs, e confusão de client secreto vs público. Em 2024+ foco também
em PKCE obrigatório, DPoP e sender-constraining.

## Hipótese

- **Phishing de código** — muda ruído e o que entra no PDF.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Mapeio clients (public/confidential) e grants.
2. Testo redirect_uri variations (subdomain, query truncate, parse bugs).
3. Remover/alterar state e nonce.
4. Avalio code interception e reuse.
5. Verifico vazamento de tokens em browser history e mobile WebViews.

## Sinal / query

```text
Sign-in logs: unexpected redirect_uri OR MFA skipped for USER_A
app=APP_LAB flow=device-code tag=93adb2
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

- RFC 6749
- RFC 8252
- OWASP OAuth