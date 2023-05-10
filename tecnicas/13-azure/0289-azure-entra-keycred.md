# service principal key creds

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

## Sinal / query

```bash
# Entra lab — Graph read mínimo
az login --service-principal -u APP_LAB -p PASS_LAB --tenant TENANT_LAB
az rest --method GET --url 'https://graph.microsoft.com/v1.0/me'
# variante keycred tag f3985d
```

## Diferencial desta nota

- Variante service principal key creds: trato separado da família `azure-entra`.

Antes de Critical em service principal key creds, confiro se a telemetria que eu cobraria reagiria — Entra audit logs; OAuth consent grants; CA insights.

## Onde já errei

Consent phishing a usuários reais exige ROE de SE.
Não mexo em produção GA sem change window.

Managed identity com permissão ampla = local admin da cloud.

## Entrega

- blue: Entra audit logs; OAuth consent grants; CA insights.
- fix: Admin consent workflows; CA strict; block legacy; PIM; app governance.
- proof: Role path; app permission; prova em lab tenant se possível.

## Refs

- MSFT Entra security
- RoadTools