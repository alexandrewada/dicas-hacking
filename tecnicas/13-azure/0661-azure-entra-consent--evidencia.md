---
id: "0661"
categoria: "13-azure"
familia: "azure-entra"
slug: "consent"
angulo: "evidencia"
mitre: "T1078.004"
owasp: ""
tags: ["13-azure", "azure-entra", "evidencia", "t1078.004"]
aliases: ["Illlicit consent grant", "consent", "consent-evidencia"]
---

# Illlicit consent grant — evidência

Pacote pra Illlicit consent grant sobreviver peer review.

## Contexto

Entra ID: app permissions excessivas, consent phishing, PRT abuse, Conditional Access gaps,
e roles privilegiadas. Road Tools / AADInternals / GraphRunner (autorizados) ajudam o mapa.
Foco em paths até Global Admin / privileged roles.

## O que precisa aparecer

- **App de teste** — muda ruído e o que entra no PDF.

## Checklist

- ROE cobre
- ambiente/versão
- identidade de teste
- PoC redigido
- impacto 2–3 frases
- hotfix + estrutural
- cleanup
- MITRE/OWASP

## Mínimo que eu aceito

Role path; app permission; prova em lab tenant se possível.

## PoC mínimo

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: cd6b56

{"id":"10042","owner":"USER_A","note":"redacted-consent"}
# capturado como USER_B
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

- [Illlicit consent grant](0281-azure-entra-consent.md)
- [PRT / primary refresh token](0283-azure-entra-prt.md)
- [Furos de Conditional Access](0282-azure-entra-ca-gap.md)
- [Application.ReadWrite.All paths (path)](0284-azure-entra-app-role.md)