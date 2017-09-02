# reset de senha que derruba MFA

## Leitura rápida

MFA mal desenhado falha por: endpoints legados sem MFA, códigos OTP bruteforçáveis,
flow skip (ativar MFA depois do session token), MFA fatigue (push bombing) e reuso de session.
Teste os fluxos OAuth/SAML completos, não só a UI de login.

## Foco

- **Account recovery abuse.** Sem isso o playbook da família mente.
- Endpoint que emite sessão pós-senha sem 2º fator, ou recovery que reseta os dois.

## Mãos na massa

1. Enumero fluxos de auth (primary, secondary, remember-me, legacy).
2. Verifico se APIs aceitam senha sem segundo fator.
3. Testo force-enable MFA e race no enrollment.
4. Avalio push fatigue apenas com ROE e conta de teste.
5. Revisar backup codes e reset flows.

## Exemplo

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=a3fc1d HTTP/1.1
Host: idp.lab.local
# fluxo reset-flow: capturar se redirect_uri fora do allowlist passa
```

Spray/lockout só com acordo escrito e contas canário.

## Pitfall

Não bombardeie MFA de usuários reais. Fatigue é disruptivo.

## Detecção / remediação

Alertas de MFA deny spikes; number matching; risk-based policies.

→ Number matching; resist phishing (FIDO2); bloquear legacy auth; step-up auth.

## Prova

Fluxo sem MFA; HAR redigido; política Cond. Access ausente.

## Refs

- OWASP MFA Cheat Sheet
- MITRE T1621