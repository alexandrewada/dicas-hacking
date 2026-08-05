---
id: "0080"
categoria: "03-api"
familia: "api-graphql"
slug: "apq"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["03-api", "api-graphql", "base", "t1190"]
aliases: ["Automatic Persisted Queries abuse", "apq"]
---

# Automatic Persisted Queries abuse

**API Top 10 / A01 Broken Access Control** · `T1190`

GraphQL centraliza a superfície: introspecção revela schema; queries aninhadas causam DoS;
mutations herdam falhas de authz; batching e aliases burla rate-limits. Teste expert combina
field suggestions, circular fragments e authorization em resolvers (não só no gateway).

**Variante:** Detalhe que pago pra ver: **Se mal implementado**. Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

**Método**

1. Tento introspecção e field suggestions.
2. Mapeio mutations sensíveis e testar authz por campo.
3. Avalio profundidade/complexidade (nested friends { friends }).
4. Batching/aliases para brute force e rate-limit bypass.
5. Verifico subscriptions e file uploads (multipart).

## No lab ficou assim

```http
POST /graphql HTTP/1.1
Host: api.lab.local
Content-Type: application/json

{"query":"query { node(id:\"a1b2c3d4-e5f6-7890-abcd-ef1234567890\") { ... on User { email role } } }"}
# GraphQL apq — tag de6696
```

**Freio:** Introspecção desabilitada não elimina schema leaks via erros.

Já abri High demais em Automatic Persisted Queries abuse por sintoma sem efeito. Cruzei com: Query cost metrics; deny introspection em prod; per-resolver auth logs. Sem side-effect, baixo.

Detecto via: Query cost metrics; deny introspection em prod; per-resolver auth logs.

Corrijo com: Disable introspection; query depth/cost limits; authz em cada resolver;
persisted queries.

Levo no report: Schema extrato (se permitido); prova de bypass authz; custo de query.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)
- [PayloadsAllTheThings — GraphQL](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection)

## Relacionadas

- [Automatic Persisted Queries abuse — detecção](0460-api-graphql-apq--detecao.md)
- [Automatic Persisted Queries abuse — path](0840-api-graphql-apq--path.md)
- [aliases para bypass de rate limit](0073-api-graphql-alias-bruteforce.md)
- [batch HTTP GraphQL](0075-api-graphql-batch.md)
- [CSRF em mutations cookie-based](0076-api-graphql-csrf.md)
- [diretivas custom perigosas](0079-api-graphql-directive.md)