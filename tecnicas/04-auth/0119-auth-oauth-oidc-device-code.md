# device authorization grant abuse

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

## Exemplo

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=c55b6e HTTP/1.1
Host: idp.lab.local
# fluxo device-code: capturar se redirect_uri fora do allowlist passa
```

## Diferencial desta nota

- **Phishing de código** — muda ruído e o que entra no PDF.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.

Já abri High demais em device authorization grant abuse por sintoma sem efeito. Cruzei com: IdP logs de redirect mismatch; anomaly em consent; short-lived codes. Sem side-effect, baixo.

## Onde já errei

Não roube tokens de usuários reais. Use clients de teste do cliente.

MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.

## Entrega

- blue: IdP logs de redirect mismatch; anomaly em consent; short-lived codes.
- fix: Allowlist estrita de redirect_uri; PKCE; state/nonce; rotacionar secrets;
evitar implicit grant.
- proof: PoC de redirect malicioso em client de teste; impacto no token.

## Refs

- RFC 6749
- RFC 8252
- OWASP OAuth