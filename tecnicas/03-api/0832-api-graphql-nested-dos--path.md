---
id: "0832"
categoria: "03-api"
familia: "api-graphql"
slug: "nested-dos"
angulo: "path"
mitre: ""
owasp: ""
tags: ["03-api", "api-graphql", "path"]
aliases: ["DoS por aninhamento", "nested-dos", "nested-dos-path"]
---

# DoS por aninhamento — path

DoS por aninhamento como pivô. Path curto > monte de finding isolado.

## Papel

GraphQL centraliza a superfície: introspecção revela schema; queries aninhadas causam DoS;
mutations herdam falhas de authz; batching e aliases burla rate-limits. Teste expert combina
field suggestions, circular fragments e authorization em resolvers (não só no gateway).

## Por que pivota

- **Demonstre com limite seguro.** Sem isso o playbook da família mente.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

## Cadeia

1. Entrada (escopo)
2. Pivô: DoS por aninhamento
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Tento introspecção e field suggestions.
2. Mapeio mutations sensíveis e testar authz por campo.
3. Avalio profundidade/complexidade (nested friends { friends }).
4. Batching/aliases para brute force e rate-limit bypass.
5. Verifico subscriptions e file uploads (multipart).

## PoC mínimo

```http
POST /graphql HTTP/1.1
Host: api.lab.local
Content-Type: application/json

{"query":"query { node(id:\"10042\") { ... on User { email role } } }"}
# GraphQL nested-dos — tag dad61f
```

## Freio

Introspecção desabilitada não elimina schema leaks via erros.
Não causo DoS destrutivo em produção — use limites acordados.

## No caminho

Detectar: Query cost metrics; deny introspection em prod; per-resolver auth logs.

Remediar: Disable introspection; query depth/cost limits; authz em cada resolver;
persisted queries.

## Prova

Schema extrato (se permitido); prova de bypass authz; custo de query.

Começo pelo contrato real (OpenAPI/HAR/introspection), não pelo PDF de arquitetura.

## Refs

- [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)
- [PayloadsAllTheThings — GraphQL](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection)

## Relacionadas

- [DoS por aninhamento](0072-api-graphql-nested-dos.md)
- [DoS por aninhamento — detecção](0452-api-graphql-nested-dos--detecao.md)
- [aliases para bypass de rate limit](0073-api-graphql-alias-bruteforce.md)
- [Automatic Persisted Queries abuse](0080-api-graphql-apq.md)
- [batch HTTP GraphQL](0075-api-graphql-batch.md)
- [CSRF em mutations cookie-based](0076-api-graphql-csrf.md)