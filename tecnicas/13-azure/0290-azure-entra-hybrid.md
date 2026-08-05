---
id: "0290"
categoria: "13-azure"
familia: "azure-entra"
slug: "hybrid"
angulo: "base"
mitre: ""
owasp: ""
tags: ["13-azure", "azure-entra", "base"]
aliases: ["hybrid identity abuse", "hybrid"]
---

# hybrid identity abuse

## Contexto

Entra ID: app permissions excessivas, consent phishing, PRT abuse, Conditional Access gaps,
e roles privilegiadas. Road Tools / AADInternals / GraphRunner (autorizados) ajudam o mapa.
Foco em paths até Global Admin / privileged roles.

## Detalhe

- Se não validar **AAD Connect**, a nota fica genérica.

## Execução

1. Enumero tenant (policy permitindo).
2. Mapeio apps, SPOs e permissions.
3. Testo CA gaps (legacy, locations).
4. Avalio consent e OAuth apps de teste.
5. Documento path e remediação.

## Exemplo

```bash
# Entra lab — Graph read mínimo
az login --service-principal -u APP_LAB -p PASS_LAB --tenant TENANT_LAB
az rest --method GET --url 'https://graph.microsoft.com/v1.0/me'
# variante hybrid tag be66bd
```

## OpSec

Graph com throttle. Sem spam de CA challenge em prod.

## Cuidados

Consent phishing a usuários reais exige ROE de SE.
Não mexo em produção GA sem change window.

## Fechamento

| | |
|---|---|
| Detecção | Entra audit logs; OAuth consent grants; CA insights. |
| Remediação | Admin consent workflows; CA strict; block legacy; PIM; app governance. |
| Evidência | Role path; app permission; prova em lab tenant se possível. |

## Refs

- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft Learn — Entra ID](https://learn.microsoft.com/en-us/entra/identity/)
- [MITRE ATT&CK T1078.004](https://attack.mitre.org/techniques/T1078/004/)

## Relacionadas

- [hybrid identity abuse — evidência](0670-azure-entra-hybrid--evidencia.md)
- [Illlicit consent grant](0281-azure-entra-consent.md)
- [PRT / primary refresh token](0283-azure-entra-prt.md)
- [Furos de Conditional Access](0282-azure-entra-ca-gap.md)