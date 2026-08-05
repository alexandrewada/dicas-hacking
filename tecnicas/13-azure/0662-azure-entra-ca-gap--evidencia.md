---
id: "0662"
categoria: "13-azure"
familia: "azure-entra"
slug: "ca-gap"
angulo: "evidencia"
mitre: "T1078.004"
owasp: ""
tags: ["13-azure", "azure-entra", "evidencia", "t1078.004"]
aliases: ["Furos de Conditional Access", "ca-gap", "ca-gap-evidencia"]
---

# Furos de Conditional Access — evidência

Pacote pra Furos de Conditional Access sobreviver peer review.

## Contexto

Entra ID: app permissions excessivas, consent phishing, PRT abuse, Conditional Access gaps,
e roles privilegiadas. Road Tools / AADInternals / GraphRunner (autorizados) ajudam o mapa.
Foco em paths até Global Admin / privileged roles.

## O que precisa aparecer

- Se não validar **Legacy protocols**, a nota fica genérica.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Role path; app permission; prova em lab tenant se possível.

## No lab ficou assim

```text
--- evidência redigida ---
req: GET /…/10042 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (ca-gap)
hash_prova: f97523
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

- [Furos de Conditional Access](0282-azure-entra-ca-gap.md)
- [Illlicit consent grant](0281-azure-entra-consent.md)
- [PRT / primary refresh token](0283-azure-entra-prt.md)