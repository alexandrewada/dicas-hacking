# Illlicit consent grant

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

## Exemplo

```bash
# Entra lab — Graph read mínimo
az login --service-principal -u APP_LAB -p PASS_LAB --tenant TENANT_LAB
az rest --method GET --url 'https://graph.microsoft.com/v1.0/me'
# variante consent tag c1c3b4
```

## Diferencial desta nota

- **App de teste** — muda ruído e o que entra no PDF.

Falso amigo em illicit consent grant: UI/log gritam, impacto não. Exijo Entra audit logs.

## Onde já errei

Consent phishing a usuários reais exige ROE de SE.
Não mexo em produção GA sem change window.

Graph com throttle. Sem spam de CA challenge em prod.

## Entrega

- blue: Entra audit logs; OAuth consent grants; CA insights.
- fix: Admin consent workflows; CA strict; block legacy; PIM; app governance.
- proof: Role path; app permission; prova em lab tenant se possível.

## Refs

- MSFT Entra security
- RoadTools