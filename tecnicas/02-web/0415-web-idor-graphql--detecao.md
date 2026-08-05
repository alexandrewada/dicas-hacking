---
id: "0415"
categoria: "02-web"
familia: "web-idor"
slug: "graphql"
angulo: "detecao"
mitre: "T1078"
owasp: "WSTG-ATHZ-04"
tags: ["02-web", "web-idor", "detecao", "t1078"]
aliases: ["BOLA em GraphQL", "graphql", "graphql-detecao"]
---

# BOLA em GraphQL — detecção

Se o SOC não vê BOLA em GraphQL, o finding é de cobertura, não de ego ofensivo.

## Contexto

IDOR continua sendo o finding de maior ROI em APIs e apps móveis.
Ocorre quando o servidor confia em identificadores controlados pelo cliente (id, uuid, filename)
sem checagem de ownership/role no objeto. Na prática provo impacto com
leitura/escrita cross-tenant e encadeio com mass assignment ou export jobs.

## Hipótese

- Detalhe que pago pra ver: **query node(id:) e aliases para exfil controlada**.
- UUID opaco sem ownership check continua BOLA. Provo com dois subjects no mesmo object_id.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Mapeio todos os IDs em requests (path, query, body, headers).
2. Crio duas contas de teste no escopo (A/B) e troco IDs.
3. Testo métodos HTTP alternativos (GET vs DELETE) e endpoints batch.
4. Avalio UUIDs previsíveis vs sequenciais; ainda assim testo ACL.
5. Quantifico impacto (PII, financial, admin actions) com evidência mínima necessária.

## Sinal / query

```text
access_log: user=USER_B resource=ORD-7781 owner=USER_A status=200
regra: deny quando subject != owner — tag 943b9a (graphql)
```

## Sinal

Access logs com object_id + subject; anomalias cross-tenant;
deny-by-default metrics.

## Freio

UUID não é autorização. GraphQL node IDs ofuscados também falham.
Cuidado com rate-limit e lockout ao enumerar.

WAF bypass só depois da prova de impacto. Senão vira discussão de tool com o blue.

## Evidência

Dois usuários, request diff, response mostrando dado de outro tenant (redigido).

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1078](https://attack.mitre.org/techniques/T1078/)
- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [WSTG-ATHZ-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [PortSwigger — Access control](https://portswigger.net/web-security/access-control)

## Relacionadas

- [BOLA em GraphQL](0035-web-idor-graphql.md)
- [BOLA em GraphQL — path](0795-web-idor-graphql--path.md)
- [IDOR com IDs numéricos](0031-web-idor-numeric.md)
- [endpoints batch/export](0034-web-idor-batch.md)
- [autorização por campo (path)](../03-api/0074-api-graphql-field-authz.md)
- [GraphQL input objects (path)](../03-api/0067-api-mass-assignment-graphql-input.md)