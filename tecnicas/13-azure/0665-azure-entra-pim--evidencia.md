---
id: "0665"
categoria: "13-azure"
familia: "azure-entra"
slug: "pim"
angulo: "evidencia"
mitre: ""
owasp: ""
tags: ["13-azure", "azure-entra", "evidencia"]
aliases: ["PIM misconfig", "pim", "pim-evidencia"]
---

# PIM misconfig — evidência

Pacote pra PIM misconfig sobreviver peer review.

## Contexto

Entra ID: app permissions excessivas, consent phishing, PRT abuse, Conditional Access gaps,
e roles privilegiadas. Road Tools / AADInternals / GraphRunner (autorizados) ajudam o mapa.
Foco em paths até Global Admin / privileged roles.

## O que precisa aparecer

- **Permanent privs** — muda ruído e o que entra no PDF.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Role path; app permission; prova em lab tenant se possível.

## Exemplo

```text
--- evidência redigida ---
req: GET /…/ORD-7781 Cookie=USER_B
res: 200 body_len=412 fields=[email,role] # PII mascarada
impacto: leitura cross-user (pim)
hash_prova: 08e6d7
```

## Remediação junto

Admin consent workflows; CA strict; block legacy; PIM; app governance.

## Se purple

Entra audit logs; OAuth consent grants; CA insights.

## Armadilha

Consent phishing a usuários reais exige ROE de SE.
Não mexo em produção GA sem change window.

## Refs

- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft Learn — Entra ID](https://learn.microsoft.com/en-us/entra/identity/)
- [MITRE ATT&CK T1078.004](https://attack.mitre.org/techniques/T1078/004/)

## Relacionadas

- [PIM misconfig](0285-azure-entra-pim.md)
- [Illlicit consent grant](0281-azure-entra-consent.md)
- [PRT / primary refresh token](0283-azure-entra-prt.md)
- [Furos de Conditional Access](0282-azure-entra-ca-gap.md)