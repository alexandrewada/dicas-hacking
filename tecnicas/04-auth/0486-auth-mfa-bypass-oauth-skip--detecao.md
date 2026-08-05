---
id: "0486"
categoria: "04-auth"
familia: "auth-mfa-bypass"
slug: "oauth-skip"
angulo: "detecao"
mitre: "T1621"
owasp: ""
tags: ["04-auth", "auth-mfa-bypass", "detecao", "t1621"]
aliases: ["token sem amr/acr", "oauth-skip", "oauth-skip-detecao"]
---

# token sem amr/acr — detecção

Se o SOC não vê token sem amr/acr, o finding é de cobertura, não de ego ofensivo.

## Contexto

MFA mal desenhado falha por: endpoints legados sem MFA, códigos OTP bruteforçáveis,
flow skip (ativar MFA depois do session token), MFA fatigue (push bombing) e reuso de session.
Teste os fluxos OAuth/SAML completos, não só a UI de login.

## Hipótese

- Se não validar **Claims MFA ausentes**, a nota fica genérica.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.
- Endpoint que emite sessão pós-senha sem 2º fator, ou recovery que reseta os dois.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Enumero fluxos de auth (primary, secondary, remember-me, legacy).
2. Verifico se APIs aceitam senha sem segundo fator.
3. Testo force-enable MFA e race no enrollment.
4. Avalio push fatigue apenas com ROE e conta de teste.
5. Revisar backup codes e reset flows.

## Sinal / query

```text
Sign-in logs: unexpected redirect_uri OR MFA skipped for USER_A
app=APP_LAB flow=oauth-skip tag=5ead2b
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

- [token sem amr/acr](0106-auth-mfa-bypass-oauth-skip.md)
- [token sem amr/acr — path](0866-auth-mfa-bypass-oauth-skip--path.md)
- [backup codes em massa](0108-auth-mfa-bypass-backup-codes.md)
- [MFA fatigue (push bombing)](0104-auth-mfa-bypass-fatigue.md)
- [protocolos legados sem MFA](0101-auth-mfa-bypass-legacy-auth.md)
- [OTP 6 dígitos sem rate limit](0102-auth-mfa-bypass-otp-brute.md)
- [OAuth redirect_uri frouxo (path)](0111-auth-oauth-oidc-redirect.md)
- [tampering de role/admin (path)](../03-api/0086-api-jwt-claim-tamper.md)