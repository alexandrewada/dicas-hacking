---
id: "0286"
categoria: "13-azure"
familia: "azure-entra"
slug: "b2b"
angulo: "base"
mitre: ""
owasp: ""
tags: ["13-azure", "azure-entra", "base"]
aliases: ["guest user escalation", "b2b"]
---

# guest user escalation

## Leitura rápida

Entra ID: app permissions excessivas, consent phishing, PRT abuse, Conditional Access gaps,
e roles privilegiadas. Road Tools / AADInternals / GraphRunner (autorizados) ajudam o mapa.
Foco em paths até Global Admin / privileged roles.

## Foco

- Variante guest user escalation: trato separado da família `azure-entra`.

## Mãos na massa

1. Enumero tenant (policy permitindo).
2. Mapeio apps, SPOs e permissions.
3. Testo CA gaps (legacy, locations).
4. Avalio consent e OAuth apps de teste.
5. Documento path e remediação.

## PoC mínimo

```bash
# Entra b2b — Graph read / role enum em tenant lab
az ad sp list --display-name 'APP_LAB' -o table
az rest --method GET --url 'https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments'
# tag f84588 — sem spam de CA challenge
```

Entra: consent, PRT, CA e roles. Grafo de identity manda mais que NSG.

## Pitfall

Consent phishing a usuários reais exige ROE de SE.
Não mexo em produção GA sem change window.

## Detecção / remediação

Entra audit logs; OAuth consent grants; CA insights.

→ Admin consent workflows; CA strict; block legacy; PIM; app governance.

## Prova

Role path; app permission; prova em lab tenant se possível.

## Refs

- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft Learn — Entra ID](https://learn.microsoft.com/en-us/entra/identity/)
- [MITRE ATT&CK T1078.004](https://attack.mitre.org/techniques/T1078/004/)

## Relacionadas

- [guest user escalation — evidência](0666-azure-entra-b2b--evidencia.md)
- [Illlicit consent grant](0281-azure-entra-consent.md)
- [PRT / primary refresh token](0283-azure-entra-prt.md)
- [Furos de Conditional Access](0282-azure-entra-ca-gap.md)