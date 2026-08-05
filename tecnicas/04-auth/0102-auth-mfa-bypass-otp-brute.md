---
id: "0102"
categoria: "04-auth"
familia: "auth-mfa-bypass"
slug: "otp-brute"
angulo: "base"
mitre: "T1621"
owasp: ""
tags: ["04-auth", "auth-mfa-bypass", "base", "t1621"]
aliases: ["OTP 6 dígitos sem rate limit", "otp-brute"]
---

# OTP 6 dígitos sem rate limit

## Leitura rápida

MFA mal desenhado falha por: endpoints legados sem MFA, códigos OTP bruteforçáveis,
flow skip (ativar MFA depois do session token), MFA fatigue (push bombing) e reuso de session.
Teste os fluxos OAuth/SAML completos, não só a UI de login.

## Foco

- Se não validar **Demonstre com limite seguro**, a nota fica genérica.
- Endpoint que emite sessão pós-senha sem 2º fator, ou recovery que reseta os dois.

## Mãos na massa

1. Enumero fluxos de auth (primary, secondary, remember-me, legacy).
2. Verifico se APIs aceitam senha sem segundo fator.
3. Testo force-enable MFA e race no enrollment.
4. Avalio push fatigue apenas com ROE e conta de teste.
5. Revisar backup codes e reset flows.

## Exemplo

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=496d74 HTTP/1.1
Host: idp.lab.local
# fluxo otp-brute: capturar se redirect_uri fora do allowlist passa
```

MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.

## Pitfall

Não bombardeie MFA de usuários reais. Fatigue é disruptivo.

## Detecção / remediação

Alertas de MFA deny spikes; number matching; risk-based policies.

→ Number matching; resist phishing (FIDO2); bloquear legacy auth; step-up auth.

## Prova

Fluxo sem MFA; HAR redigido; política Cond. Access ausente.

## Refs

- [MITRE ATT&CK T1621](https://attack.mitre.org/techniques/T1621/)
- [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)

## Relacionadas

- [OTP 6 dígitos sem rate limit — detecção](0482-auth-mfa-bypass-otp-brute--detecao.md)
- [OTP 6 dígitos sem rate limit — path](0862-auth-mfa-bypass-otp-brute--path.md)
- [backup codes em massa](0108-auth-mfa-bypass-backup-codes.md)
- [MFA fatigue (push bombing)](0104-auth-mfa-bypass-fatigue.md)
- [protocolos legados sem MFA](0101-auth-mfa-bypass-legacy-auth.md)
- [token sem amr/acr](0106-auth-mfa-bypass-oauth-skip.md)