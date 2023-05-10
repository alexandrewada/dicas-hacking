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
# Entra lab — Graph read mínimo
az login --service-principal -u APP_LAB -p PASS_LAB --tenant TENANT_LAB
az rest --method GET --url 'https://graph.microsoft.com/v1.0/me'
# variante device-code tag b881bf
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

- MSFT Entra security
- RoadTools