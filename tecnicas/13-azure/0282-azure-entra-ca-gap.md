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
# Entra lab — Graph read mínimo
az login --service-principal -u APP_LAB -p PASS_LAB --tenant TENANT_LAB
az rest --method GET --url 'https://graph.microsoft.com/v1.0/me'
# variante ca-gap tag 8082be
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

- MSFT Entra security
- RoadTools