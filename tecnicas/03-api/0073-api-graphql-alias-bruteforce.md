---
id: "0073"
categoria: "03-api"
familia: "api-graphql"
slug: "alias-bruteforce"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["03-api", "api-graphql", "base", "t1190"]
aliases: ["aliases para bypass de rate limit", "alias-bruteforce"]
---

# aliases para bypass de rate limit

## Contexto

GraphQL centraliza a superfície: introspecção revela schema; queries aninhadas causam DoS;
mutations herdam falhas de authz; batching e aliases burla rate-limits. Teste expert combina
field suggestions, circular fragments e authorization em resolvers (não só no gateway).

## Detalhe

- **OTP/password guess.** Sem isso o playbook da família mente.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

## Execução

1. Tento introspecção e field suggestions.
2. Mapeio mutations sensíveis e testar authz por campo.
3. Avalio profundidade/complexidade (nested friends { friends }).
4. Batching/aliases para brute force e rate-limit bypass.
5. Verifico subscriptions e file uploads (multipart).

## Sinal / query

```http
POST /graphql HTTP/1.1
Host: api.lab.local
Content-Type: application/json

{"query":"query { node(id:\"10042\") { ... on User { email role } } }"}
# GraphQL alias-bruteforce — tag 20b49e
```

## OpSec

Introspecção desabilitada não elimina schema leaks via erros.

## Cuidados

Introspecção desabilitada não elimina schema leaks via erros.
Não causo DoS destrutivo em produção — use limites acordados.

## Fechamento

| | |
|---|---|
| Detecção | Query cost metrics; deny introspection em prod; per-resolver auth logs. |
| Remediação | Disable introspection; query depth/cost limits; authz em cada resolver;
persisted queries. |
| Evidência | Schema extrato (se permitido); prova de bypass authz; custo de query. |

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)
- [PayloadsAllTheThings — GraphQL](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection)

## Relacionadas

- [aliases para bypass de rate limit — detecção](0453-api-graphql-alias-bruteforce--detecao.md)
- [aliases para bypass de rate limit — path](0833-api-graphql-alias-bruteforce--path.md)
- [Automatic Persisted Queries abuse](0080-api-graphql-apq.md)
- [batch HTTP GraphQL](0075-api-graphql-batch.md)
- [CSRF em mutations cookie-based](0076-api-graphql-csrf.md)
- [diretivas custom perigosas](0079-api-graphql-directive.md)