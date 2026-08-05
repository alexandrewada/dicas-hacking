---
id: "0861"
categoria: "04-auth"
familia: "auth-mfa-bypass"
slug: "legacy-auth"
angulo: "path"
mitre: "T1621"
owasp: ""
tags: ["04-auth", "auth-mfa-bypass", "path", "t1621"]
aliases: ["protocolos legados sem MFA", "legacy-auth", "legacy-auth-path"]
---

# protocolos legados sem MFA — path

protocolos legados sem MFA como pivô. Path curto > monte de finding isolado.

## Papel

MFA mal desenhado falha por: endpoints legados sem MFA, códigos OTP bruteforçáveis,
flow skip (ativar MFA depois do session token), MFA fatigue (push bombing) e reuso de session.
Teste os fluxos OAuth/SAML completos, não só a UI de login.

## Por que pivota

- Detalhe que pago pra ver: **IMAP/EWS/basic auth**.
- Endpoint que emite sessão pós-senha sem 2º fator, ou recovery que reseta os dois.

## Cadeia

1. Entrada (escopo)
2. Pivô: protocolos legados sem MFA
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
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=fb621d HTTP/1.1
Host: idp.lab.local
# fluxo legacy-auth: capturar se redirect_uri fora do allowlist passa
```

## Freio

Não bombardeie MFA de usuários reais. Fatigue é disruptivo.

## No caminho

Detectar: Alertas de MFA deny spikes; number matching; risk-based policies.

Remediar: Number matching; resist phishing (FIDO2); bloquear legacy auth; step-up auth.

## Prova

Fluxo sem MFA; HAR redigido; política Cond. Access ausente.

Mint → store → use → revoke. Quebro o fluxo e testo cada perna.

## Refs

- [MITRE ATT&CK T1621](https://attack.mitre.org/techniques/T1621/)
- [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)

## Relacionadas

- [protocolos legados sem MFA](0101-auth-mfa-bypass-legacy-auth.md)
- [protocolos legados sem MFA — detecção](0481-auth-mfa-bypass-legacy-auth--detecao.md)
- [backup codes em massa](0108-auth-mfa-bypass-backup-codes.md)
- [MFA fatigue (push bombing)](0104-auth-mfa-bypass-fatigue.md)
- [token sem amr/acr](0106-auth-mfa-bypass-oauth-skip.md)
- [OTP 6 dígitos sem rate limit](0102-auth-mfa-bypass-otp-brute.md)