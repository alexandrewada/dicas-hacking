# token sem amr/acr — path

token sem amr/acr como pivô. Path curto > monte de finding isolado.

## Papel

MFA mal desenhado falha por: endpoints legados sem MFA, códigos OTP bruteforçáveis,
flow skip (ativar MFA depois do session token), MFA fatigue (push bombing) e reuso de session.
Teste os fluxos OAuth/SAML completos, não só a UI de login.

## Por que pivota

- Se não validar **Claims MFA ausentes**, a nota fica genérica.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.
- Endpoint que emite sessão pós-senha sem 2º fator, ou recovery que reseta os dois.

## Cadeia

1. Entrada (escopo)
2. Pivô: token sem amr/acr
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Enumero fluxos de auth (primary, secondary, remember-me, legacy).
2. Verifico se APIs aceitam senha sem segundo fator.
3. Testo force-enable MFA e race no enrollment.
4. Avalio push fatigue apenas com ROE e conta de teste.
5. Revisar backup codes e reset flows.

## Sinal / query

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=a9c190 HTTP/1.1
Host: idp.lab.local
# fluxo oauth-skip: capturar se redirect_uri fora do allowlist passa
```

## Freio

Não bombardeie MFA de usuários reais. Fatigue é disruptivo.

## No caminho

Detectar: Alertas de MFA deny spikes; number matching; risk-based policies.

Remediar: Number matching; resist phishing (FIDO2); bloquear legacy auth; step-up auth.

## Prova

Fluxo sem MFA; HAR redigido; política Cond. Access ausente.

Spray/lockout só com acordo escrito e contas canário.

## Refs

- OWASP MFA Cheat Sheet
- MITRE T1621