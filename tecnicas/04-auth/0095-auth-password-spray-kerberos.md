---
id: "0095"
categoria: "04-auth"
familia: "auth-password-spray"
slug: "kerberos"
angulo: "base"
mitre: "T1110.003"
owasp: ""
tags: ["04-auth", "auth-password-spray", "base", "t1110.003"]
aliases: ["Kerberos pre-auth spray", "kerberos"]
---

# Kerberos pre-auth spray

**A07 Identification and Authentication Failures** · `T1110.003 Password Spraying`

## Contexto

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## O que muda aqui

- **Evito massivos TERRORS sem acordo** — muda ruído e o que entra no PDF.
- DONT_REQ_PREAUTH = AS-REP roast sem SPN. Confirmo UAC no LDAP e limito amostra.

## Como testo

1. Confirmar ROE: taxas, horários, contas canary.
2. Obter lista de usuários autorizada (não compre dumps ilegais).
3. Escolher 3–5 senhas contextuais (Estacao@Ano, Company123!).
4. Rotaciono lentamente; respeitar thresholds.
5. Reportar contas vulneráveis e ausência de MFA/Conditional Access.

## Exemplo

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=684058 HTTP/1.1
Host: idp.lab.local
# fluxo kerberos: capturar se redirect_uri fora do allowlist passa
```

## Campo

MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.

Kerberos pre-auth spray: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage.

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

- [Kerberos pre-auth spray — detecção](0475-auth-password-spray-kerberos--detecao.md)
- [Kerberos pre-auth spray — path](0855-auth-password-spray-kerberos--path.md)
- [IMAP/POP spraying](0097-auth-password-spray-imap.md)
- [SMTP AUTH legado](0096-auth-password-spray-legacy-smtp.md)
- [bypass de lockout por pool de IPs](0098-auth-password-spray-lockout-bypass.md)
- [Password spray em Microsoft 365](0091-auth-password-spray-o365.md)