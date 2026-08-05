---
id: "0282"
categoria: "13-azure"
familia: "azure-entra"
slug: "ca-gap"
angulo: "base"
mitre: "T1078.004"
owasp: ""
tags: ["13-azure", "azure-entra", "base", "t1078.004"]
aliases: ["Furos de Conditional Access", "ca-gap"]
---

# Furos de Conditional Access

**Cloud identity** · `T1078.004`

## Contexto

Entra ID: app permissions excessivas, consent phishing, PRT abuse, Conditional Access gaps,
e roles privilegiadas. Road Tools / AADInternals / GraphRunner (autorizados) ajudam o mapa.
Foco em paths até Global Admin / privileged roles.

## O que muda aqui

- Se não validar **Legacy protocols**, a nota fica genérica.

## Como testo

1. Enumero tenant (policy permitindo).
2. Mapeio apps, SPOs e permissions.
3. Testo CA gaps (legacy, locations).
4. Avalio consent e OAuth apps de teste.
5. Documento path e remediação.

## No lab ficou assim

```bash
# Entra ca-gap — Graph read / role enum em tenant lab
az ad sp list --display-name 'APP_LAB' -o table
az rest --method GET --url 'https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments'
# tag 8082be — sem spam de CA challenge
```

## Campo

Managed identity com permissão ampla = local admin da cloud.

Já abri High demais em Conditional Access gaps por sintoma sem efeito. Cruzei com: Entra audit logs; OAuth consent grants; CA insights. Sem side-effect, baixo.

## Já me queimei

Consent phishing a usuários reais exige ROE de SE.
Não mexo em produção GA sem change window.

## Blue

- Detectar: Entra audit logs; OAuth consent grants; CA insights.
- Fechar: Admin consent workflows; CA strict; block legacy; PIM; app governance.

## Evidência

Role path; app permission; prova em lab tenant se possível.

## Refs

- [MITRE ATT&CK T1078.004](https://attack.mitre.org/techniques/T1078/004/)
- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft Learn — Entra ID](https://learn.microsoft.com/en-us/entra/identity/)

## Relacionadas

- [Furos de Conditional Access — evidência](0662-azure-entra-ca-gap--evidencia.md)
- [Illlicit consent grant](0281-azure-entra-consent.md)
- [PRT / primary refresh token](0283-azure-entra-prt.md)