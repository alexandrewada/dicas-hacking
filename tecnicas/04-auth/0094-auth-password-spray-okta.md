---
id: "0094"
categoria: "04-auth"
familia: "auth-password-spray"
slug: "okta"
angulo: "base"
mitre: "T1110.003"
owasp: ""
tags: ["04-auth", "auth-password-spray", "base", "t1110.003"]
aliases: ["Okta/Auth0", "okta"]
---

# Okta/Auth0

**A07 Identification and Authentication Failures** · `T1110.003 Password Spraying`

## Contexto

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## Como eu faço

1. Confirmar ROE: taxas, horários, contas canary.
2. Obter lista de usuários autorizada (não compre dumps ilegais).
3. Escolher 3–5 senhas contextuais (Estacao@Ano, Company123!).
4. Rotaciono lentamente; respeitar thresholds.
5. Reportar contas vulneráveis e ausência de MFA/Conditional Access.

## No lab ficou assim

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=f4f86a HTTP/1.1
Host: idp.lab.local
# fluxo okta: capturar se redirect_uri fora do allowlist passa
```

## Diferencial desta nota

- Detalhe que pago pra ver: **Observe rate limits e bot detection**.

Já abri High demais em Okta/Auth0 por sintoma sem efeito. Cruzei com: Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage. Sem side-effect, baixo.

## Onde já errei

Spraying agressivo derruba contas legítimas — coordenação é obrigatória.
O365/Entra tem smart lockout; ajuste metodologia.

Mint → store → use → revoke. Quebro o fluxo e testo cada perna.

## Entrega

- blue: Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage.
- fix: MFA obrigatório; ban lists de senha; CAPTCHA/risk-based; lockout inteligente.
- proof: Taxa usada; contas comprometidas de teste; logs de detecção (se purple).

## Refs

- [MITRE ATT&CK T1110.003](https://attack.mitre.org/techniques/T1110/003/)
- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft — Password spray guidance](https://learn.microsoft.com/en-us/defender-for-identity/password-spray-alert)

## Relacionadas

- [Okta/Auth0 — detecção](0474-auth-password-spray-okta--detecao.md)
- [Okta/Auth0 — path](0854-auth-password-spray-okta--path.md)
- [IMAP/POP spraying](0097-auth-password-spray-imap.md)
- [Kerberos pre-auth spray](0095-auth-password-spray-kerberos.md)
- [SMTP AUTH legado](0096-auth-password-spray-legacy-smtp.md)
- [bypass de lockout por pool de IPs](0098-auth-password-spray-lockout-bypass.md)