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

- MSFT Entra security
- RoadTools