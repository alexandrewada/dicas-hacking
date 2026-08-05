---
id: "0283"
categoria: "13-azure"
familia: "azure-entra"
slug: "prt"
angulo: "base"
mitre: "T1078.004"
owasp: ""
tags: ["13-azure", "azure-entra", "base", "t1078.004"]
aliases: ["PRT / primary refresh token", "prt"]
---

# PRT / primary refresh token

**Cloud identity** · `T1078.004`

## Contexto

Entra ID: app permissions excessivas, consent phishing, PRT abuse, Conditional Access gaps,
e roles privilegiadas. Road Tools / AADInternals / GraphRunner (autorizados) ajudam o mapa.
Foco em paths até Global Admin / privileged roles.

## Como eu faço

1. Enumero tenant (policy permitindo).
2. Mapeio apps, SPOs e permissions.
3. Testo CA gaps (legacy, locations).
4. Avalio consent e OAuth apps de teste.
5. Documento path e remediação.

## No lab ficou assim

```bash
# PRT / Primary Refresh Token — só lab device
az account get-access-token --resource https://graph.microsoft.com
# NÃO extrair PRT de endpoint prod; tag 820c18
```

## Diferencial desta nota

- Se não validar **Device context**, a nota fica genérica.

PRT / primary refresh token: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Entra audit logs; OAuth consent grants; CA insights.

## Onde já errei

Consent phishing a usuários reais exige ROE de SE.
Não mexo em produção GA sem change window.

Entra: consent, PRT, CA e roles. Grafo de identity manda mais que NSG.

## Entrega

- blue: Entra audit logs; OAuth consent grants; CA insights.
- fix: Admin consent workflows; CA strict; block legacy; PIM; app governance.
- proof: Role path; app permission; prova em lab tenant se possível.

## Refs

- [MITRE ATT&CK T1078.004](https://attack.mitre.org/techniques/T1078/004/)
- [Microsoft Learn — Entra ID security](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-monitoring-health)
- [Microsoft Learn — Entra ID](https://learn.microsoft.com/en-us/entra/identity/)

## Relacionadas

- [PRT / primary refresh token — evidência](0663-azure-entra-prt--evidencia.md)
- [Illlicit consent grant](0281-azure-entra-consent.md)
- [Furos de Conditional Access](0282-azure-entra-ca-gap.md)
- [device code phishing (path)](0288-azure-entra-device-code.md)
- [implicit grant legado (path)](../04-auth/0114-auth-oauth-oidc-implicit.md)