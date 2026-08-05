---
id: "0109"
categoria: "04-auth"
familia: "auth-mfa-bypass"
slug: "sim-swap"
angulo: "base"
mitre: "T1621"
owasp: ""
tags: ["04-auth", "auth-mfa-bypass", "base", "t1621"]
aliases: ["sim swap como premissa", "sim-swap"]
---

# sim swap como premissa

**A07** · `T1621 Multi-Factor Authentication Request Generation`

## Contexto

MFA mal desenhado falha por: endpoints legados sem MFA, códigos OTP bruteforçáveis,
flow skip (ativar MFA depois do session token), MFA fatigue (push bombing) e reuso de session.
Teste os fluxos OAuth/SAML completos, não só a UI de login.

## O que muda aqui

- **Discuta impacto e detecção, sem executar fraude** — muda ruído e o que entra no PDF.
- Endpoint que emite sessão pós-senha sem 2º fator, ou recovery que reseta os dois.

## Como testo

1. Enumero fluxos de auth (primary, secondary, remember-me, legacy).
2. Verifico se APIs aceitam senha sem segundo fator.
3. Testo force-enable MFA e race no enrollment.
4. Avalio push fatigue apenas com ROE e conta de teste.
5. Revisar backup codes e reset flows.

## Exemplo

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=495d78 HTTP/1.1
Host: idp.lab.local
# fluxo sim-swap: capturar se redirect_uri fora do allowlist passa
```

## Campo

Spray/lockout só com acordo escrito e contas canário.

Antes de Critical em sim swap como premissa, confiro se a telemetria que eu cobraria reagiria — Alertas de MFA deny spikes; number matching; risk-based policies.

## Já me queimei

Não bombardeie MFA de usuários reais. Fatigue é disruptivo.

## Blue

- Detectar: Alertas de MFA deny spikes; number matching; risk-based policies.
- Fechar: Number matching; resist phishing (FIDO2); bloquear legacy auth; step-up auth.

## Evidência

Fluxo sem MFA; HAR redigido; política Cond. Access ausente.

## Refs

- [MITRE ATT&CK T1621](https://attack.mitre.org/techniques/T1621/)
- [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)

## Relacionadas

- [sim swap como premissa — detecção](0489-auth-mfa-bypass-sim-swap--detecao.md)
- [sim swap como premissa — path](0869-auth-mfa-bypass-sim-swap--path.md)
- [backup codes em massa](0108-auth-mfa-bypass-backup-codes.md)
- [MFA fatigue (push bombing)](0104-auth-mfa-bypass-fatigue.md)
- [protocolos legados sem MFA](0101-auth-mfa-bypass-legacy-auth.md)
- [token sem amr/acr](0106-auth-mfa-bypass-oauth-skip.md)