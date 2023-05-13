# Application.ReadWrite.All paths — evidência

Pacote pra Application.ReadWrite.All paths sobreviver peer review.

## Contexto

Entra ID: app permissions excessivas, consent phishing, PRT abuse, Conditional Access gaps,
e roles privilegiadas. Road Tools / AADInternals / GraphRunner (autorizados) ajudam o mapa.
Foco em paths até Global Admin / privileged roles.

## O que precisa aparecer

- Variante Application.ReadWrite.All paths: trato separado da família `azure-entra`.

## Checklist

- pré-condição
- request/comando
- efeito de negócio
- CVSS justificado
- remediação
- reteste path

## Mínimo que eu aceito

Role path; app permission; prova em lab tenant se possível.

## No lab ficou assim

```http
HTTP/1.1 200 OK
Content-Type: application/json
X-Request-Id: ddaba4

{"id":"usr_01HZX","owner":"USER_A","note":"redacted-app-role"}
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

- MSFT Entra security
- RoadTools