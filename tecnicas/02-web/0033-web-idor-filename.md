---
id: "0033"
categoria: "02-web"
familia: "web-idor"
slug: "filename"
angulo: "base"
mitre: ""
owasp: "WSTG-ATHZ-04"
tags: ["02-web", "web-idor", "base"]
aliases: ["path traversal lógico em downloads", "filename"]
---

# path traversal lógico em downloads

## Leitura rápida

IDOR continua sendo o finding de maior ROI em APIs e apps móveis.
Ocorre quando o servidor confia em identificadores controlados pelo cliente (id, uuid, filename)
sem checagem de ownership/role no objeto. Na prática provo impacto com
leitura/escrita cross-tenant e encadeio com mass assignment ou export jobs.

## Foco

- Detalhe que pago pra ver: **Troca de filename/object key em storage**.
- UUID opaco sem ownership check continua BOLA. Provo com dois subjects no mesmo object_id.

## Mãos na massa

1. Mapeio todos os IDs em requests (path, query, body, headers).
2. Crio duas contas de teste no escopo (A/B) e troco IDs.
3. Testo métodos HTTP alternativos (GET vs DELETE) e endpoints batch.
4. Avalio UUIDs previsíveis vs sequenciais; ainda assim testo ACL.
5. Quantifico impacto (PII, financial, admin actions) com evidência mínima necessária.

## No lab ficou assim

```http
GET /api/v1/resources/a1b2c3d4-e5f6-7890-abcd-ef1234567890 HTTP/1.1
Host: app.lab.local
Authorization: Bearer TOKEN_USER_B
# object_id de USER_A — se 200 com PII, BOLA (filename)
# tag 99bbad
```

Impacto que eu aceito: ATO, cross-tenant, escrita privilegiada, RCE. Reflection sem sink útil vira Informational.

## Pitfall

UUID não é autorização. GraphQL node IDs ofuscados também falham.
Cuidado com rate-limit e lockout ao enumerar.

## Detecção / remediação

Access logs com object_id + subject; anomalias cross-tenant;
deny-by-default metrics.

→ Checagem server-side de ownership em **todo** objeto;
testes automatizados de BOLA; IDs opacos sem sequential leak se desejável.

## Prova

Dois usuários, request diff, response mostrando dado de outro tenant (redigido).

## Refs

- [WSTG-ATHZ-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [PortSwigger — Access control](https://portswigger.net/web-security/access-control)
- [OWASP API1 BOLA](https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/)

## Relacionadas

- [path traversal lógico em downloads — detecção](0413-web-idor-filename--detecao.md)
- [path traversal lógico em downloads — path](0793-web-idor-filename--path.md)
- [IDOR com IDs numéricos](0031-web-idor-numeric.md)
- [endpoints batch/export](0034-web-idor-batch.md)
- [BOLA em GraphQL](0035-web-idor-graphql.md)