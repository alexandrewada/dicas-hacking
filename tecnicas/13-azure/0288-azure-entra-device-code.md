---
id: "0288"
categoria: "13-azure"
familia: "azure-entra"
slug: "device-code"
angulo: "base"
mitre: ""
owasp: ""
tags: ["13-azure", "azure-entra", "base"]
aliases: ["device code phishing", "device-code"]
---

# device code phishing

## Leitura rápida

Entra ID: app permissions excessivas, consent phishing, PRT abuse, Conditional Access gaps,
e roles privilegiadas. Road Tools / AADInternals / GraphRunner (autorizados) ajudam o mapa.
Foco em paths até Global Admin / privileged roles.

## Foco

- Detalhe que pago pra ver: **SE ROE**.

## Mãos na massa

1. Enumero tenant (policy permitindo).
2. Mapeio apps, SPOs e permissions.
3. Testo CA gaps (legacy, locations).
4. Avalio consent e OAuth apps de teste.
5. Documento path e remediação.

## Exemplo

```bash
# Entra device-code — Graph read / role enum em tenant lab
az ad sp list --display-name 'APP_LAB' -o table
az rest --method GET --url 'https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments'
# tag b881bf — sem spam de CA challenge
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

- [device code phishing — evidência](0668-azure-entra-device-code--evidencia.md)
- [Illlicit consent grant](0281-azure-entra-consent.md)
- [PRT / primary refresh token](0283-azure-entra-prt.md)
- [Furos de Conditional Access](0282-azure-entra-ca-gap.md)