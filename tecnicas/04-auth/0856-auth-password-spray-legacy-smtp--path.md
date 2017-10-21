# SMTP AUTH legado — path

SMTP AUTH legado como pivô. Path curto > monte de finding isolado.

## Papel

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## Por que pivota

- Detalhe que pago pra ver: **Autenticação de e-mail esquecida**.

## Cadeia

1. Entrada (escopo)
2. Pivô: SMTP AUTH legado
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
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=620784 HTTP/1.1
Host: idp.lab.local
# fluxo legacy-smtp: capturar se redirect_uri fora do allowlist passa
```

## Freio

Spraying agressivo derruba contas legítimas — coordenação é obrigatória.
O365/Entra tem smart lockout; ajuste metodologia.

## No caminho

Detectar: Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage.

Remediar: MFA obrigatório; ban lists de senha; CAPTCHA/risk-based; lockout inteligente.

## Prova

Taxa usada; contas comprometidas de teste; logs de detecção (se purple).

Mint → store → use → revoke. Quebro o fluxo e testo cada perna.

## Refs

- MITRE T1110.003
- Microsoft Password Spray guidance