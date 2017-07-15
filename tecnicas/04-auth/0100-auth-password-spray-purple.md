# exercício purple team

## Leitura rápida

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## Foco

- Se não validar **Meça tempo até alerta SOC**, a nota fica genérica.

## Mãos na massa

1. Confirmar ROE: taxas, horários, contas canary.
2. Obter lista de usuários autorizada (não compre dumps ilegais).
3. Escolher 3–5 senhas contextuais (Estacao@Ano, Company123!).
4. Rotaciono lentamente; respeitar thresholds.
5. Reportar contas vulneráveis e ausência de MFA/Conditional Access.

## PoC mínimo

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=ad999a HTTP/1.1
Host: idp.lab.local
# fluxo purple: capturar se redirect_uri fora do allowlist passa
```

Spray/lockout só com acordo escrito e contas canário.

## Pitfall

Spraying agressivo derruba contas legítimas — coordenação é obrigatória.
O365/Entra tem smart lockout; ajuste metodologia.

## Detecção / remediação

Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage.

→ MFA obrigatório; ban lists de senha; CAPTCHA/risk-based; lockout inteligente.

## Prova

Taxa usada; contas comprometidas de teste; logs de detecção (se purple).

## Refs

- MITRE T1110.003
- Microsoft Password Spray guidance