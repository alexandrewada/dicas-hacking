# device remember fraco — detecção

Gap de detecção em `T1621 Multi-Factor Authentication Request Generation` / device remember fraco. PoC mínimo, telemetria ligada.

## Contexto

MFA mal desenhado falha por: endpoints legados sem MFA, códigos OTP bruteforçáveis,
flow skip (ativar MFA depois do session token), MFA fatigue (push bombing) e reuso de session.
Teste os fluxos OAuth/SAML completos, não só a UI de login.

## Hipótese

- **Cookie previsível/longo.** Sem isso o playbook da família mente.
- Endpoint que emite sessão pós-senha sem 2º fator, ou recovery que reseta os dois.

## Como corro o purple

1. Confirmo log source relevante.
2. Disparo o fluxo abaixo.
3. Anoto alerta / ausência.
4. Se silêncio, abro finding de detecção.

### PoC

1. Enumero fluxos de auth (primary, secondary, remember-me, legacy).
2. Verifico se APIs aceitam senha sem segundo fator.
3. Testo force-enable MFA e race no enrollment.
4. Avalio push fatigue apenas com ROE e conta de teste.
5. Revisar backup codes e reset flows.

## Sinal / query

```text
Sign-in logs: unexpected redirect_uri OR MFA skipped for USER_A
app=APP_LAB flow=remember-device tag=47e33f
```

## Sinal

Alertas de MFA deny spikes; number matching; risk-based policies.

## Freio

Não bombardeie MFA de usuários reais. Fatigue é disruptivo.

Spray/lockout só com acordo escrito e contas canário.

## Evidência

Fluxo sem MFA; HAR redigido; política Cond. Access ausente.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- OWASP MFA Cheat Sheet
- MITRE T1621