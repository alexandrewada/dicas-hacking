---
id: "0479"
categoria: "04-auth"
familia: "auth-password-spray"
slug: "sso-portal"
angulo: "detecao"
mitre: "T1110.003"
owasp: ""
tags: ["04-auth", "auth-password-spray", "detecao", "t1110.003"]
aliases: ["portal SSO custom", "sso-portal", "sso-portal-detecao"]
---

# portal SSO custom — detecção

Gap de detecção em `T1110.003 Password Spraying` / portal SSO custom. PoC mínimo, telemetria ligada.

## Contexto

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## Hipótese

- Detalhe que pago pra ver: **Mensagens de erro diferenciais**.

## Como corro o purple

1. Confirmo log source relevante.
2. Disparo o fluxo abaixo.
3. Anoto alerta / ausência.
4. Se silêncio, abro finding de detecção.

### PoC

1. Confirmar ROE: taxas, horários, contas canary.
2. Obter lista de usuários autorizada (não compre dumps ilegais).
3. Escolher 3–5 senhas contextuais (Estacao@Ano, Company123!).
4. Rotaciono lentamente; respeitar thresholds.
5. Reportar contas vulneráveis e ausência de MFA/Conditional Access.

## Sinal / query

```text
Sign-in logs: unexpected redirect_uri OR MFA skipped for USER_A
app=APP_LAB flow=sso-portal tag=e2a8bf
```

## Sinal

Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage.

## Freio

Spraying agressivo derruba contas legítimas — coordenação é obrigatória.
O365/Entra tem smart lockout; ajuste metodologia.

MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.

## Evidência

Taxa usada; contas comprometidas de teste; logs de detecção (se purple).

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1110.003](https://attack.mitre.org/techniques/T1110/003/)
- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft — Password spray guidance](https://learn.microsoft.com/en-us/defender-for-identity/password-spray-alert)

## Relacionadas

- [portal SSO custom](0099-auth-password-spray-sso-portal.md)
- [portal SSO custom — path](0859-auth-password-spray-sso-portal--path.md)
- [IMAP/POP spraying](0097-auth-password-spray-imap.md)
- [Kerberos pre-auth spray](0095-auth-password-spray-kerberos.md)
- [SMTP AUTH legado](0096-auth-password-spray-legacy-smtp.md)
- [bypass de lockout por pool de IPs](0098-auth-password-spray-lockout-bypass.md)