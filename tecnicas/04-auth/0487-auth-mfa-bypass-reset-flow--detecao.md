---
id: "0487"
categoria: "04-auth"
familia: "auth-mfa-bypass"
slug: "reset-flow"
angulo: "detecao"
mitre: "T1621"
owasp: ""
tags: ["04-auth", "auth-mfa-bypass", "detecao", "t1621"]
aliases: ["reset de senha que derruba MFA", "reset-flow", "reset-flow-detecao"]
---

# reset de senha que derruba MFA — detecção

Gap de detecção em `T1621 Multi-Factor Authentication Request Generation` / reset de senha que derruba MFA. PoC mínimo, telemetria ligada.

## Contexto

MFA mal desenhado falha por: endpoints legados sem MFA, códigos OTP bruteforçáveis,
flow skip (ativar MFA depois do session token), MFA fatigue (push bombing) e reuso de session.
Teste os fluxos OAuth/SAML completos, não só a UI de login.

## Hipótese

- **Account recovery abuse.** Sem isso o playbook da família mente.
- Endpoint que emite sessão pós-senha sem 2º fator, ou recovery que reseta os dois.

## Como corro o purple

1. Confirmo log source relevante.
2. Disparo o fluxo abaixo.
3. Anoto alerta / ausência.
4. Se silêncio, abro finding de detecção.

### PoC

1. Enumero fluxos de auth (primary, secondary, remember-me, legacy).
2. Verifico se APIs aceitam senha sem segundo fator.
3. Testo force-enable MFA e race no enrollment.
4. Avalio push fatigue apenas com ROE e conta de teste.
5. Revisar backup codes e reset flows.

## Exemplo

```text
Sign-in logs: unexpected redirect_uri OR MFA skipped for USER_A
app=APP_LAB flow=reset-flow tag=8c9633
```

## Sinal

Alertas de MFA deny spikes; number matching; risk-based policies.

## Freio

Não bombardeie MFA de usuários reais. Fatigue é disruptivo.

Spray/lockout só com acordo escrito e contas canário.

## Evidência

Fluxo sem MFA; HAR redigido; política Cond. Access ausente.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1621](https://attack.mitre.org/techniques/T1621/)
- [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)

## Relacionadas

- [reset de senha que derruba MFA](0107-auth-mfa-bypass-reset-flow.md)
- [reset de senha que derruba MFA — path](0867-auth-mfa-bypass-reset-flow--path.md)
- [backup codes em massa](0108-auth-mfa-bypass-backup-codes.md)
- [MFA fatigue (push bombing)](0104-auth-mfa-bypass-fatigue.md)
- [protocolos legados sem MFA](0101-auth-mfa-bypass-legacy-auth.md)
- [token sem amr/acr](0106-auth-mfa-bypass-oauth-skip.md)