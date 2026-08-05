---
id: "0285"
categoria: "13-azure"
familia: "azure-entra"
slug: "pim"
angulo: "base"
mitre: ""
owasp: ""
tags: ["13-azure", "azure-entra", "base"]
aliases: ["PIM misconfig", "pim"]
---

# PIM misconfig

## Leitura rápida

Entra ID: app permissions excessivas, consent phishing, PRT abuse, Conditional Access gaps,
e roles privilegiadas. Road Tools / AADInternals / GraphRunner (autorizados) ajudam o mapa.
Foco em paths até Global Admin / privileged roles.

## Foco

- **Permanent privs** — muda ruído e o que entra no PDF.

## Mãos na massa

1. Enumero tenant (policy permitindo).
2. Mapeio apps, SPOs e permissions.
3. Testo CA gaps (legacy, locations).
4. Avalio consent e OAuth apps de teste.
5. Documento path e remediação.

## PoC mínimo

```bash
# Entra pim — Graph read / role enum em tenant lab
az ad sp list --display-name 'APP_LAB' -o table
az rest --method GET --url 'https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments'
# tag e289eb — sem spam de CA challenge
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

- [PIM misconfig — evidência](0665-azure-entra-pim--evidencia.md)
- [Illlicit consent grant](0281-azure-entra-consent.md)
- [PRT / primary refresh token](0283-azure-entra-prt.md)
- [Furos de Conditional Access](0282-azure-entra-ca-gap.md)