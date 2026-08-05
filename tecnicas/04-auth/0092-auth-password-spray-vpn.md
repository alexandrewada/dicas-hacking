---
id: "0092"
categoria: "04-auth"
familia: "auth-password-spray"
slug: "vpn"
angulo: "base"
mitre: "T1110.003"
owasp: ""
tags: ["04-auth", "auth-password-spray", "base", "t1110.003"]
aliases: ["contra VPN SSL", "vpn"]
---

# contra VPN SSL

**A07 Identification and Authentication Failures** · `T1110.003 Password Spraying`

## Contexto

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## O que muda aqui

- **Frequente sem MFA** — muda ruído e o que entra no PDF.

## Como testo

1. Confirmar ROE: taxas, horários, contas canary.
2. Obter lista de usuários autorizada (não compre dumps ilegais).
3. Escolher 3–5 senhas contextuais (Estacao@Ano, Company123!).
4. Rotaciono lentamente; respeitar thresholds.
5. Reportar contas vulneráveis e ausência de MFA/Conditional Access.

## No lab ficou assim

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=ac693f HTTP/1.1
Host: idp.lab.local
# fluxo vpn: capturar se redirect_uri fora do allowlist passa
```

## Campo

MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.

Falso amigo em contra VPN SSL: UI/log gritam, impacto não. Exijo Alertas de auth failures distribuídos.

## Já me queimei

Spraying agressivo derruba contas legítimas — coordenação é obrigatória.
O365/Entra tem smart lockout; ajuste metodologia.

## Blue

- Detectar: Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage.
- Fechar: MFA obrigatório; ban lists de senha; CAPTCHA/risk-based; lockout inteligente.

## Evidência

Taxa usada; contas comprometidas de teste; logs de detecção (se purple).

## Refs

- [MITRE ATT&CK T1110.003](https://attack.mitre.org/techniques/T1110/003/)
- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft — Password spray guidance](https://learn.microsoft.com/en-us/defender-for-identity/password-spray-alert)

## Relacionadas

- [contra VPN SSL — detecção](0472-auth-password-spray-vpn--detecao.md)
- [contra VPN SSL — path](0852-auth-password-spray-vpn--path.md)
- [IMAP/POP spraying](0097-auth-password-spray-imap.md)
- [Kerberos pre-auth spray](0095-auth-password-spray-kerberos.md)
- [SMTP AUTH legado](0096-auth-password-spray-legacy-smtp.md)
- [bypass de lockout por pool de IPs](0098-auth-password-spray-lockout-bypass.md)