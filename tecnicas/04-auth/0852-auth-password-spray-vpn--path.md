---
id: "0852"
categoria: "04-auth"
familia: "auth-password-spray"
slug: "vpn"
angulo: "path"
mitre: "T1110.003"
owasp: ""
tags: ["04-auth", "auth-password-spray", "path", "t1110.003"]
aliases: ["contra VPN SSL", "vpn", "vpn-path"]
---

# contra VPN SSL — path

contra VPN SSL como pivô. Path curto > monte de finding isolado.

## Papel

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## Por que pivota

- **Frequente sem MFA** — muda ruído e o que entra no PDF.

## Cadeia

1. Entrada (escopo)
2. Pivô: contra VPN SSL
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Confirmar ROE: taxas, horários, contas canary.
2. Obter lista de usuários autorizada (não compre dumps ilegais).
3. Escolher 3–5 senhas contextuais (Estacao@Ano, Company123!).
4. Rotaciono lentamente; respeitar thresholds.
5. Reportar contas vulneráveis e ausência de MFA/Conditional Access.

## No lab ficou assim

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=98e9ae HTTP/1.1
Host: idp.lab.local
# fluxo vpn: capturar se redirect_uri fora do allowlist passa
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
- [Microsoft — Password spray guidance](https://learn.microsoft.com/en-us/defender-for-identity/password-spray-alert)

## Relacionadas

- [contra VPN SSL](0092-auth-password-spray-vpn.md)
- [contra VPN SSL — detecção](0472-auth-password-spray-vpn--detecao.md)
- [IMAP/POP spraying](0097-auth-password-spray-imap.md)
- [Kerberos pre-auth spray](0095-auth-password-spray-kerberos.md)
- [SMTP AUTH legado](0096-auth-password-spray-legacy-smtp.md)
- [bypass de lockout por pool de IPs](0098-auth-password-spray-lockout-bypass.md)