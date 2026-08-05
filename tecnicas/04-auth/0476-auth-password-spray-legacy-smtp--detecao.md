---
id: "0476"
categoria: "04-auth"
familia: "auth-password-spray"
slug: "legacy-smtp"
angulo: "detecao"
mitre: "T1110.003"
owasp: ""
tags: ["04-auth", "auth-password-spray", "detecao", "t1110.003"]
aliases: ["SMTP AUTH legado", "legacy-smtp", "legacy-smtp-detecao"]
---

# SMTP AUTH legado — detecção

Se o SOC não vê SMTP AUTH legado, o finding é de cobertura, não de ego ofensivo.

## Contexto

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## Hipótese

- Detalhe que pago pra ver: **Autenticação de e-mail esquecida**.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Confirmar ROE: taxas, horários, contas canary.
2. Obter lista de usuários autorizada (não compre dumps ilegais).
3. Escolher 3–5 senhas contextuais (Estacao@Ano, Company123!).
4. Rotaciono lentamente; respeitar thresholds.
5. Reportar contas vulneráveis e ausência de MFA/Conditional Access.

## Sinal / query

```text
Sign-in logs: unexpected redirect_uri OR MFA skipped for USER_A
app=APP_LAB flow=legacy-smtp tag=3a908d
```

## Sinal

Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage.

## Freio

Spraying agressivo derruba contas legítimas — coordenação é obrigatória.
O365/Entra tem smart lockout; ajuste metodologia.

Mint → store → use → revoke. Quebro o fluxo e testo cada perna.

## Evidência

Taxa usada; contas comprometidas de teste; logs de detecção (se purple).

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1110.003](https://attack.mitre.org/techniques/T1110/003/)
- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft — Password spray guidance](https://learn.microsoft.com/en-us/defender-for-identity/password-spray-alert)

## Relacionadas

- [SMTP AUTH legado](0096-auth-password-spray-legacy-smtp.md)
- [SMTP AUTH legado — path](0856-auth-password-spray-legacy-smtp--path.md)
- [IMAP/POP spraying](0097-auth-password-spray-imap.md)
- [Kerberos pre-auth spray](0095-auth-password-spray-kerberos.md)
- [bypass de lockout por pool de IPs](0098-auth-password-spray-lockout-bypass.md)
- [Password spray em Microsoft 365](0091-auth-password-spray-o365.md)