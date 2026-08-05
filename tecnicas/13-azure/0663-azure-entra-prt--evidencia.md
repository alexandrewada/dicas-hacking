---
id: "0663"
categoria: "13-azure"
familia: "azure-entra"
slug: "prt"
angulo: "evidencia"
mitre: "T1078.004"
owasp: ""
tags: ["13-azure", "azure-entra", "evidencia", "t1078.004"]
aliases: ["PRT / primary refresh token", "prt", "prt-evidencia"]
---

# PRT / primary refresh token — evidência

Pacote pra PRT / primary refresh token sobreviver peer review.

## Contexto

Entra ID: app permissions excessivas, consent phishing, PRT abuse, Conditional Access gaps,
e roles privilegiadas. Road Tools / AADInternals / GraphRunner (autorizados) ajudam o mapa.
Foco em paths até Global Admin / privileged roles.

## O que precisa aparecer

- Se não validar **Device context**, a nota fica genérica.

## Checklist

Sem pacote completo o finding vira pingue-pongue no reteste.

## Mínimo que eu aceito

Role path; app permission; prova em lab tenant se possível.

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/a1b2c3d4-e5f6-7890-abcd-ef1234567890 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (prt)
hash_prova: b2c4c6
```

## Remediação junto

Admin consent workflows; CA strict; block legacy; PIM; app governance.

## Se purple

Entra audit logs; OAuth consent grants; CA insights.

## Armadilha

Consent phishing a usuários reais exige ROE de SE.
Não mexo em produção GA sem change window.

## Refs

- [MITRE ATT&CK T1078.004](https://attack.mitre.org/techniques/T1078/004/)
- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft Learn — Entra ID](https://learn.microsoft.com/en-us/entra/identity/)

## Relacionadas

- [PRT / primary refresh token](0283-azure-entra-prt.md)
- [Illlicit consent grant](0281-azure-entra-consent.md)
- [Furos de Conditional Access](0282-azure-entra-ca-gap.md)
- [device code phishing (path)](0288-azure-entra-device-code.md)
- [implicit grant legado (path)](../04-auth/0114-auth-oauth-oidc-implicit.md)