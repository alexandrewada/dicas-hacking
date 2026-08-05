---
id: "0037"
categoria: "02-web"
familia: "web-idor"
slug: "ws"
angulo: "base"
mitre: ""
owasp: "WSTG-ATHZ-04"
tags: ["02-web", "web-idor", "base"]
aliases: ["IDOR em WebSocket messages", "ws"]
---

# IDOR em WebSocket messages

## Contexto

IDOR continua sendo o finding de maior ROI em APIs e apps móveis.
Ocorre quando o servidor confia em identificadores controlados pelo cliente (id, uuid, filename)
sem checagem de ownership/role no objeto. Na prática provo impacto com
leitura/escrita cross-tenant e encadeio com mass assignment ou export jobs.

## Detalhe

- **Subscribe em canais de outro usuário** — muda ruído e o que entra no PDF.
- UUID opaco sem ownership check continua BOLA. Provo com dois subjects no mesmo object_id.

## Execução

1. Mapeio todos os IDs em requests (path, query, body, headers).
2. Crio duas contas de teste no escopo (A/B) e troco IDs.
3. Testo métodos HTTP alternativos (GET vs DELETE) e endpoints batch.
4. Avalio UUIDs previsíveis vs sequenciais; ainda assim testo ACL.
5. Quantifico impacto (PII, financial, admin actions) com evidência mínima necessária.

## No lab ficou assim

```http
GET /api/v1/resources/10042 HTTP/1.1
Host: app.lab.local
Authorization: Bearer TOKEN_USER_B
# object_id de USER_A — se 200 com PII, BOLA (ws)
# tag 63e314
```

## OpSec

UUID não é autorização. GraphQL node IDs ofuscados também falham. Parâmetro é boundary: de onde veio o valor (cookie, claim, hidden) importa mais que o payload da vez.

## Cuidados

UUID não é autorização. GraphQL node IDs ofuscados também falham.
Cuidado com rate-limit e lockout ao enumerar.

## Fechamento

| | |
|---|---|
| Detecção | Access logs com object_id + subject; anomalias cross-tenant;
deny-by-default metrics. |
| Remediação | Checagem server-side de ownership em **todo** objeto;
testes automatizados de BOLA; IDs opacos sem sequential leak se desejável. |
| Evidência | Dois usuários, request diff, response mostrando dado de outro tenant (redigido). |

## Refs

- [WSTG-ATHZ-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Bypassing_Authorization_Schema)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [PortSwigger — Access control](https://portswigger.net/web-security/access-control)
- [OWASP API1 BOLA](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/)

## Relacionadas

- [IDOR em WebSocket messages — detecção](0417-web-idor-ws--detecao.md)
- [IDOR em WebSocket messages — path](0797-web-idor-ws--path.md)
- [IDOR com IDs numéricos](0031-web-idor-numeric.md)
- [endpoints batch/export](0034-web-idor-batch.md)
- [BOLA em GraphQL](0035-web-idor-graphql.md)