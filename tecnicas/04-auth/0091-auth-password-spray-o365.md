# Password spray em Microsoft 365

## Contexto

Spraying testa poucas senhas comuns contra muitos usuários para evitar lockout.
Em pentest, deve ser **rate-limitado**, com lista aprovada e monitoramento conjunto ao blue team.
O valor está em demonstrar ausência de MFA, lockout inconsistente e telemetria cega.

## Detalhe

- Se não validar **Endpoint legacy auth é o alvo clássico**, a nota fica genérica.

## Execução

1. Confirmar ROE: taxas, horários, contas canary.
2. Obter lista de usuários autorizada (não compre dumps ilegais).
3. Escolher 3–5 senhas contextuais (Estacao@Ano, Company123!).
4. Rotaciono lentamente; respeitar thresholds.
5. Reportar contas vulneráveis e ausência de MFA/Conditional Access.

## PoC mínimo

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=73709d HTTP/1.1
Host: idp.lab.local
# fluxo o365: capturar se redirect_uri fora do allowlist passa
```

## OpSec

MFA bypass de verdade completa o fator sem o segundo. UI skip sem backend não é finding de auth.

## Cuidados

Spraying agressivo derruba contas legítimas — coordenação é obrigatória.
O365/Entra tem smart lockout; ajuste metodologia.

## Fechamento

| | |
|---|---|
| Detecção | Alertas de auth failures distribuídos; impossible spray patterns; MFA coverage. |
| Remediação | MFA obrigatório; ban lists de senha; CAPTCHA/risk-based; lockout inteligente. |
| Evidência | Taxa usada; contas comprometidas de teste; logs de detecção (se purple). |

## Refs

- MITRE T1110.003
- Microsoft Password Spray guidance