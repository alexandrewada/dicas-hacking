---
id: "0035"
categoria: "02-web"
familia: "web-idor"
slug: "graphql"
angulo: "base"
mitre: "T1078"
owasp: "WSTG-ATHZ-04"
tags: ["02-web", "web-idor", "base", "t1078"]
aliases: ["BOLA em GraphQL", "graphql"]
---

# BOLA em GraphQL

**API1:2023 BOLA / A01 Broken Access Control** · `T1078 Valid Accounts (abuso de sessão) / T1190`

## Contexto

IDOR continua sendo o finding de maior ROI em APIs e apps móveis.
Ocorre quando o servidor confia em identificadores controlados pelo cliente (id, uuid, filename)
sem checagem de ownership/role no objeto. Na prática provo impacto com
leitura/escrita cross-tenant e encadeio com mass assignment ou export jobs.

## O que muda aqui

- Detalhe que pago pra ver: **query node(id:) e aliases para exfil controlada**.
- UUID opaco sem ownership check continua BOLA. Provo com dois subjects no mesmo object_id.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

## Como testo

1. Mapeio todos os IDs em requests (path, query, body, headers).
2. Crio duas contas de teste no escopo (A/B) e troco IDs.
3. Testo métodos HTTP alternativos (GET vs DELETE) e endpoints batch.
4. Avalio UUIDs previsíveis vs sequenciais; ainda assim testo ACL.
5. Quantifico impacto (PII, financial, admin actions) com evidência mínima necessária.

## PoC mínimo

```http
GET /api/v1/resources/ORD-7781 HTTP/1.1
Host: app.lab.local
Authorization: Bearer TOKEN_USER_B
# object_id de USER_A — se 200 com PII, BOLA (graphql)
# tag 4538b2
```

## Campo

WAF bypass só depois da prova de impacto. Senão vira discussão de tool com o blue.

Falso amigo em BOLA em GraphQL nodes: UI/log gritam, impacto não. Exijo Access logs com object_id + subject.

## Já me queimei

UUID não é autorização. GraphQL node IDs ofuscados também falham.
Cuidado com rate-limit e lockout ao enumerar.

## Blue

- Detectar: Access logs com object_id + subject; anomalias cross-tenant;
deny-by-default metrics.
- Fechar: Checagem server-side de ownership em **todo** objeto;
testes automatizados de BOLA; IDs opacos sem sequential leak se desejável.

## Evidência

Dois usuários, request diff, response mostrando dado de outro tenant (redigido).

## Refs

- [MITRE ATT&CK T1078](https://attack.mitre.org/techniques/T1078/)
- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [WSTG-ATHZ-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Bypassing_Authorization_Schema)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [PortSwigger — Access control](https://portswigger.net/web-security/access-control)

## Relacionadas

- [BOLA em GraphQL — detecção](0415-web-idor-graphql--detecao.md)
- [BOLA em GraphQL — path](0795-web-idor-graphql--path.md)
- [IDOR com IDs numéricos](0031-web-idor-numeric.md)
- [endpoints batch/export](0034-web-idor-batch.md)
- [autorização por campo (path)](../03-api/0074-api-graphql-field-authz.md)
- [GraphQL input objects (path)](../03-api/0067-api-mass-assignment-graphql-input.md)