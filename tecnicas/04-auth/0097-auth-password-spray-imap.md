---
id: "0097"
categoria: "04-auth"
familia: "auth-password-spray"
slug: "imap"
angulo: "base"
mitre: "T1110.003"
owasp: ""
tags: ["04-auth", "auth-password-spray", "base", "t1110.003"]
aliases: ["IMAP/POP spraying", "imap"]
---

# IMAP/POP spraying

## Leitura rápida

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## Foco

- **Mesmo padrão, outro protocolo** — muda ruído e o que entra no PDF.

## Mãos na massa

1. Confirmar ROE: taxas, horários, contas canary.
2. Obter lista de usuários autorizada (não compre dumps ilegais).
3. Escolher 3–5 senhas contextuais (Estacao@Ano, Company123!).
4. Rotaciono lentamente; respeitar thresholds.
5. Reportar contas vulneráveis e ausência de MFA/Conditional Access.

## No lab ficou assim

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=76fdb9 HTTP/1.1
Host: idp.lab.local
# fluxo imap: capturar se redirect_uri fora do allowlist passa
```

Mint → store → use → revoke. Quebro o fluxo e testo cada perna.

## Pitfall

Spraying agressivo derruba contas legítimas — coordenação é obrigatória.
O365/Entra tem smart lockout; ajuste metodologia.

## Detecção / remediação

Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage.

→ MFA obrigatório; ban lists de senha; CAPTCHA/risk-based; lockout inteligente.

## Prova

Taxa usada; contas comprometidas de teste; logs de detecção (se purple).

## Refs

- [MITRE ATT&CK T1110.003](https://attack.mitre.org/techniques/T1110/003/)
- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft — Password spray guidance](https://learn.microsoft.com/en-us/defender-for-identity/password-spray-alert)

## Relacionadas

- [IMAP/POP spraying — detecção](0477-auth-password-spray-imap--detecao.md)
- [IMAP/POP spraying — path](0857-auth-password-spray-imap--path.md)
- [Kerberos pre-auth spray](0095-auth-password-spray-kerberos.md)
- [SMTP AUTH legado](0096-auth-password-spray-legacy-smtp.md)
- [bypass de lockout por pool de IPs](0098-auth-password-spray-lockout-bypass.md)
- [Password spray em Microsoft 365](0091-auth-password-spray-o365.md)