# protocolos legados sem MFA

## Contexto

MFA mal desenhado falha por: endpoints legados sem MFA, códigos OTP bruteforçáveis,
flow skip (ativar MFA depois do session token), MFA fatigue (push bombing) e reuso de session.
Teste os fluxos OAuth/SAML completos, não só a UI de login.

## Detalhe

- Detalhe que pago pra ver: **IMAP/EWS/basic auth**.
- Endpoint que emite sessão pós-senha sem 2º fator, ou recovery que reseta os dois.

## Execução

1. Enumero fluxos de auth (primary, secondary, remember-me, legacy).
2. Verifico se APIs aceitam senha sem segundo fator.
3. Testo force-enable MFA e race no enrollment.
4. Avalio push fatigue apenas com ROE e conta de teste.
5. Revisar backup codes e reset flows.

## Sinal / query

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=54382b HTTP/1.1
Host: idp.lab.local
# fluxo legacy-auth: capturar se redirect_uri fora do allowlist passa
```

## OpSec

Não bombardeie MFA de usuários reais. Fatigue é disruptivo.

## Cuidados

Não bombardeie MFA de usuários reais. Fatigue é disruptivo.

## Fechamento

| | |
|---|---|
| Detecção | Alertas de MFA deny spikes; number matching; risk-based policies. |
| Remediação | Number matching; resist phishing (FIDO2); bloquear legacy auth; step-up auth. |
| Evidência | Fluxo sem MFA; HAR redigido; política Cond. Access ausente. |

## Refs

- OWASP MFA Cheat Sheet
- MITRE T1621