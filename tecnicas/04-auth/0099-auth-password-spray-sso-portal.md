---
id: "0099"
categoria: "04-auth"
familia: "auth-password-spray"
slug: "sso-portal"
angulo: "base"
mitre: "T1110.003"
owasp: ""
tags: ["04-auth", "auth-password-spray", "base", "t1110.003"]
aliases: ["portal SSO custom", "sso-portal"]
---

# portal SSO custom

`T1110.003 Password Spraying`

## Por que importa

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## Variante

- Detalhe que pago pra ver: **Mensagens de erro diferenciais**.

## Passo a passo

1. Confirmar ROE: taxas, horários, contas canary.
2. Obter lista de usuários autorizada (não compre dumps ilegais).
3. Escolher 3–5 senhas contextuais (Estacao@Ano, Company123!).
4. Rotaciono lentamente; respeitar thresholds.
5. Reportar contas vulneráveis e ausência de MFA/Conditional Access.

## No lab ficou assim

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=22508c HTTP/1.1
Host: idp.lab.local
# fluxo sso-portal: capturar se redirect_uri fora do allowlist passa
```

## Nota de operador

MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.

## Armadilha

Spraying agressivo derruba contas legítimas — coordenação é obrigatória.
O365/Entra tem smart lockout; ajuste metodologia.

Já abri High demais em portal SSO custom por sintoma sem efeito. Cruzei com: Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage. Sem side-effect, baixo.

## Depois

Detecção — Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage.

Remediação — MFA obrigatório; ban lists de senha; CAPTCHA/risk-based; lockout inteligente.

No PDF — Taxa usada; contas comprometidas de teste; logs de detecção (se purple).

## Refs

- [MITRE ATT&CK T1110.003](https://attack.mitre.org/techniques/T1110/003/)
- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft — Password spray guidance](https://learn.microsoft.com/en-us/defender-for-identity/password-spray-alert)

## Relacionadas

- [portal SSO custom — detecção](0479-auth-password-spray-sso-portal--detecao.md)
- [portal SSO custom — path](0859-auth-password-spray-sso-portal--path.md)
- [IMAP/POP spraying](0097-auth-password-spray-imap.md)
- [Kerberos pre-auth spray](0095-auth-password-spray-kerberos.md)
- [SMTP AUTH legado](0096-auth-password-spray-legacy-smtp.md)
- [bypass de lockout por pool de IPs](0098-auth-password-spray-lockout-bypass.md)