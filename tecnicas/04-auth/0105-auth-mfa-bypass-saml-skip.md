---
id: "0105"
categoria: "04-auth"
familia: "auth-mfa-bypass"
slug: "saml-skip"
angulo: "base"
mitre: "T1621"
owasp: ""
tags: ["04-auth", "auth-mfa-bypass", "base", "t1621"]
aliases: ["skip MFA em SAML secondary", "saml-skip"]
---

# skip MFA em SAML secondary

## Contexto

MFA mal desenhado falha por: endpoints legados sem MFA, códigos OTP bruteforçáveis,
flow skip (ativar MFA depois do session token), MFA fatigue (push bombing) e reuso de session.
Teste os fluxos OAuth/SAML completos, não só a UI de login.

## Detalhe

- Se não validar **ACS mal validado**, a nota fica genérica.
- redirect_uri, state/nonce, audience. Authorize → token → resource, hop a hop.
- Endpoint que emite sessão pós-senha sem 2º fator, ou recovery que reseta os dois.

## Execução

1. Enumero fluxos de auth (primary, secondary, remember-me, legacy).
2. Verifico se APIs aceitam senha sem segundo fator.
3. Testo force-enable MFA e race no enrollment.
4. Avalio push fatigue apenas com ROE e conta de teste.
5. Revisar backup codes e reset flows.

## PoC mínimo

```http
GET /oauth/authorize?client_id=APP_LAB&redirect_uri=https://evil.lab.local/cb&response_type=code&state=a6a5bc HTTP/1.1
Host: idp.lab.local
# fluxo saml-skip: capturar se redirect_uri fora do allowlist passa
```

## OpSec

Mint → store → use → revoke. Quebro o fluxo e testo cada perna.

## Cuidados

Não bombardeie MFA de usuários reais. Fatigue é disruptivo.

## Fechamento

| | |
|---|---|
| Detecção | Alertas de MFA deny spikes; number matching; risk-based policies. |
| Remediação | Number matching; resist phishing (FIDO2); bloquear legacy auth; step-up auth. |
| Evidência | Fluxo sem MFA; HAR redigido; política Cond. Access ausente. |

## Refs

- [MITRE ATT&CK T1621](https://attack.mitre.org/techniques/T1621/)
- [OWASP Multifactor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)

## Relacionadas

- [skip MFA em SAML secondary — detecção](0485-auth-mfa-bypass-saml-skip--detecao.md)
- [skip MFA em SAML secondary — path](0865-auth-mfa-bypass-saml-skip--path.md)
- [backup codes em massa](0108-auth-mfa-bypass-backup-codes.md)
- [MFA fatigue (push bombing)](0104-auth-mfa-bypass-fatigue.md)
- [protocolos legados sem MFA](0101-auth-mfa-bypass-legacy-auth.md)
- [token sem amr/acr](0106-auth-mfa-bypass-oauth-skip.md)