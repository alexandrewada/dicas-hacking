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

- MITRE T1110.003
- Microsoft Password Spray guidance