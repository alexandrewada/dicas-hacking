---
id: "0867"
categoria: "04-auth"
familia: "auth-mfa-bypass"
slug: "reset-flow"
angulo: "path"
mitre: "T1621"
owasp: ""
tags: ["04-auth", "auth-mfa-bypass", "path", "t1621"]
aliases: ["reset de senha que derruba MFA", "reset-flow", "reset-flow-path"]
---

# reset de senha que derruba MFA — path

reset de senha que derruba MFA como pivô. Path curto > monte de finding isolado.

## Papel

MFA mal desenhado falha por: endpoints legados sem MFA, códigos OTP bruteforçáveis,
flow skip (ativar MFA depois do session token), MFA fatigue (push bombing) e reuso de session.
Teste os fluxos OAuth/SAML completos, não só a UI de login.

## Por que pivota

- **Account recovery abuse.** Sem isso o playbook da família mente.
- Endpoint que emite sessão pós-senha sem 2º fator, ou recovery que reseta os dois.

## Cadeia

1. Entrada (escopo)
2. Pivô: reset de senha que derruba MFA
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Enumero fluxos de auth (primary, secondary, remember-me, legacy).
2. Verifico se APIs aceitam senha sem segundo fator.
3. Testo force-enable MFA e race no enrollment.
4. Avalio push fatigue apenas com ROE e conta de teste.
5. Revisar backup codes e reset flows.

## No lab ficou assim

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=47f2ab HTTP/1.1
Host: idp.lab.local
# fluxo reset-flow: capturar se redirect_uri fora do allowlist passa
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

- [MITRE ATT&CK T1621](https://attack.mitre.org/techniques/T1621/)
- [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)

## Relacionadas

- [reset de senha que derruba MFA](0107-auth-mfa-bypass-reset-flow.md)
- [reset de senha que derruba MFA — detecção](0487-auth-mfa-bypass-reset-flow--detecao.md)
- [backup codes em massa](0108-auth-mfa-bypass-backup-codes.md)
- [MFA fatigue (push bombing)](0104-auth-mfa-bypass-fatigue.md)
- [protocolos legados sem MFA](0101-auth-mfa-bypass-legacy-auth.md)
- [token sem amr/acr](0106-auth-mfa-bypass-oauth-skip.md)