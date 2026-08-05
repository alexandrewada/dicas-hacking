---
id: "0471"
categoria: "04-auth"
familia: "auth-password-spray"
slug: "o365"
angulo: "detecao"
mitre: "T1110.003"
owasp: ""
tags: ["04-auth", "auth-password-spray", "detecao", "t1110.003"]
aliases: ["Password spray em Microsoft 365", "o365", "o365-detecao"]
---

# Password spray em Microsoft 365 — detecção

Purple em Password spray em Microsoft 365: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## Hipótese

- Se não validar **Endpoint legacy auth é o alvo clássico**, a nota fica genérica.

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1110.003 Password Spraying`.

### PoC

1. Confirmar ROE: taxas, horários, contas canary.
2. Obter lista de usuários autorizada (não compre dumps ilegais).
3. Escolher 3–5 senhas contextuais (Estacao@Ano, Company123!).
4. Rotaciono lentamente; respeitar thresholds.
5. Reportar contas vulneráveis e ausência de MFA/Conditional Access.

## Sinal / query

```text
Sign-in logs: unexpected redirect_uri OR MFA skipped for USER_A
app=APP_LAB flow=o365 tag=729017
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
- [Microsoft — Compromised credentials alerts](https://learn.microsoft.com/en-us/defender-for-identity/compromised-credentials-alerts)

## Relacionadas

- [Password spray em Microsoft 365](0091-auth-password-spray-o365.md)
- [Password spray em Microsoft 365 — path](0851-auth-password-spray-o365--path.md)
- [IMAP/POP spraying](0097-auth-password-spray-imap.md)
- [Kerberos pre-auth spray](0095-auth-password-spray-kerberos.md)
- [SMTP AUTH legado](0096-auth-password-spray-legacy-smtp.md)
- [bypass de lockout por pool de IPs](0098-auth-password-spray-lockout-bypass.md)
- [MFA fatigue (push bombing) (path)](0104-auth-mfa-bypass-fatigue.md)
- [Furos de Conditional Access (path)](../13-azure/0282-azure-entra-ca-gap.md)