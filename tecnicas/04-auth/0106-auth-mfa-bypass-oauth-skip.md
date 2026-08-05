---
id: "0106"
categoria: "04-auth"
familia: "auth-mfa-bypass"
slug: "oauth-skip"
angulo: "base"
mitre: "T1621"
owasp: ""
tags: ["04-auth", "auth-mfa-bypass", "base", "t1621"]
aliases: ["token sem amr/acr", "oauth-skip"]
---

# token sem amr/acr

**A07** · `T1621 Multi-Factor Authentication Request Generation`

## Contexto

MFA mal desenhado falha por: endpoints legados sem MFA, códigos OTP bruteforçáveis,
flow skip (ativar MFA depois do session token), MFA fatigue (push bombing) e reuso de session.
Teste os fluxos OAuth/SAML completos, não só a UI de login.

## Como eu faço

1. Enumero fluxos de auth (primary, secondary, remember-me, legacy).
2. Verifico se APIs aceitam senha sem segundo fator.
3. Testo force-enable MFA e race no enrollment.
4. Avalio push fatigue apenas com ROE e conta de teste.
5. Revisar backup codes e reset flows.

## Exemplo

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=5e5576 HTTP/1.1
Host: idp.lab.local
# fluxo oauth-skip: capturar se redirect_uri fora do allowlist passa
```

## Diferencial desta nota

- Se não validar **Claims MFA ausentes**, a nota fica genérica.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.
- Endpoint que emite sessão pós-senha sem 2º fator, ou recovery que reseta os dois.

Já abri High demais em token sem amr/acr por sintoma sem efeito. Cruzei com: Alertas de MFA deny spikes; number matching; risk-based policies. Sem side-effect, baixo.

## Onde já errei

Não bombardeie MFA de usuários reais. Fatigue é disruptivo.

Spray/lockout só com acordo escrito e contas canário.

## Entrega

- blue: Alertas de MFA deny spikes; number matching; risk-based policies.
- fix: Number matching; resist phishing (FIDO2); bloquear legacy auth; step-up auth.
- proof: Fluxo sem MFA; HAR redigido; política Cond. Access ausente.

## Refs

- [MITRE ATT&CK T1621](https://attack.mitre.org/techniques/T1621/)
- [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)

## Relacionadas

- [token sem amr/acr — detecção](0486-auth-mfa-bypass-oauth-skip--detecao.md)
- [token sem amr/acr — path](0866-auth-mfa-bypass-oauth-skip--path.md)
- [backup codes em massa](0108-auth-mfa-bypass-backup-codes.md)
- [MFA fatigue (push bombing)](0104-auth-mfa-bypass-fatigue.md)
- [protocolos legados sem MFA](0101-auth-mfa-bypass-legacy-auth.md)
- [OTP 6 dígitos sem rate limit](0102-auth-mfa-bypass-otp-brute.md)
- [OAuth redirect_uri frouxo (path)](0111-auth-oauth-oidc-redirect.md)
- [tampering de role/admin (path)](../03-api/0086-api-jwt-claim-tamper.md)