---
id: "0851"
categoria: "04-auth"
familia: "auth-password-spray"
slug: "o365"
angulo: "path"
mitre: "T1110.003"
owasp: ""
tags: ["04-auth", "auth-password-spray", "path", "t1110.003"]
aliases: ["Password spray em Microsoft 365", "o365", "o365-path"]
---

# Password spray em Microsoft 365 — path

Password spray em Microsoft 365 como pivô. Path curto > monte de finding isolado.

## Papel

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## Por que pivota

- Se não validar **Endpoint legacy auth é o alvo clássico**, a nota fica genérica.

## Cadeia

1. Entrada (escopo)
2. Pivô: Password spray em Microsoft 365
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Confirmar ROE: taxas, horários, contas canary.
2. Obter lista de usuários autorizada (não compre dumps ilegais).
3. Escolher 3–5 senhas contextuais (Estacao@Ano, Company123!).
4. Rotaciono lentamente; respeitar thresholds.
5. Reportar contas vulneráveis e ausência de MFA/Conditional Access.

## PoC mínimo

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=f64357 HTTP/1.1
Host: idp.lab.local
# fluxo o365: capturar se redirect_uri fora do allowlist passa
```

## Freio

Spraying agressivo derruba contas legítimas — coordenação é obrigatória.
O365/Entra tem smart lockout; ajuste metodologia.

## No caminho

Detectar: Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage.

Remediar: MFA obrigatório; ban lists de senha; CAPTCHA/risk-based; lockout inteligente.

## Prova

Taxa usada; contas comprometidas de teste; logs de detecção (se purple).

MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.

## Refs

- [MITRE ATT&CK T1110.003](https://attack.mitre.org/techniques/T1110/003/)
- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft — Compromised credentials alerts](https://learn.microsoft.com/en-us/defender-for-identity/compromised-credentials-alerts)

## Relacionadas

- [Password spray em Microsoft 365](0091-auth-password-spray-o365.md)
- [Password spray em Microsoft 365 — detecção](0471-auth-password-spray-o365--detecao.md)
- [IMAP/POP spraying](0097-auth-password-spray-imap.md)
- [Kerberos pre-auth spray](0095-auth-password-spray-kerberos.md)
- [SMTP AUTH legado](0096-auth-password-spray-legacy-smtp.md)
- [bypass de lockout por pool de IPs](0098-auth-password-spray-lockout-bypass.md)
- [MFA fatigue (push bombing) (path)](0104-auth-mfa-bypass-fatigue.md)
- [Furos de Conditional Access (path)](../13-azure/0282-azure-entra-ca-gap.md)