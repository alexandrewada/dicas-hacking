---
id: "0477"
categoria: "04-auth"
familia: "auth-password-spray"
slug: "imap"
angulo: "detecao"
mitre: "T1110.003"
owasp: ""
tags: ["04-auth", "auth-password-spray", "detecao", "t1110.003"]
aliases: ["IMAP/POP spraying", "imap", "imap-detecao"]
---

# IMAP/POP spraying — detecção

Purple em IMAP/POP spraying: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## Hipótese

- **Mesmo padrão, outro protocolo** — muda ruído e o que entra no PDF.

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
app=APP_LAB flow=imap tag=264f42
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
- [Microsoft — Compromised credentials alerts](https://learn.microsoft.com/en-us/defender-for-identity/compromised-credentials-alerts)

## Relacionadas

- [IMAP/POP spraying](0097-auth-password-spray-imap.md)
- [IMAP/POP spraying — path](0857-auth-password-spray-imap--path.md)
- [Kerberos pre-auth spray](0095-auth-password-spray-kerberos.md)
- [SMTP AUTH legado](0096-auth-password-spray-legacy-smtp.md)
- [bypass de lockout por pool de IPs](0098-auth-password-spray-lockout-bypass.md)
- [Password spray em Microsoft 365](0091-auth-password-spray-o365.md)