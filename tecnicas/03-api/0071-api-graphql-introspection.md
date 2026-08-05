---
id: "0071"
categoria: "03-api"
familia: "api-graphql"
slug: "introspection"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["03-api", "api-graphql", "base", "t1190"]
aliases: ["introspecção completa", "introspection"]
---

# introspecção completa

**API Top 10 / A01 Broken Access Control** · `T1190`

## Contexto

GraphQL centraliza a superfície: introspecção revela schema; queries aninhadas causam DoS;
mutations herdam falhas de authz; batching e aliases burla rate-limits. Teste expert combina
field suggestions, circular fragments e authorization em resolvers (não só no gateway).

## Como eu faço

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

{"query":"query { node(id:\"usr_01HZX\") { ... on User { email role } } }"}
# GraphQL introspection — tag d9a67e
```

## Diferencial desta nota

- Detalhe que pago pra ver: **Finding Medium/High conforme exposição**.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

introspecção completa: se não reproduz efeito (authz/dado/exec), não infla severidade. Referência de sinal: Query cost metrics; deny introspection em prod; per-resolver auth logs.

## Onde já errei

Introspecção desabilitada não elimina schema leaks via erros.
Não causo DoS destrutivo em produção — use limites acordados.

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Entrega

- blue: Query cost metrics; deny introspection em prod; per-resolver auth logs.
- fix: Disable introspection; query depth/cost limits; authz em cada resolver;
persisted queries.
- proof: Schema extrato (se permitido); prova de bypass authz; custo de query.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)
- [PayloadsAllTheThings — GraphQL](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection)

## Relacionadas

- [introspecção completa — detecção](0451-api-graphql-introspection--detecao.md)
- [introspecção completa — path](0831-api-graphql-introspection--path.md)
- [aliases para bypass de rate limit](0073-api-graphql-alias-bruteforce.md)
- [Automatic Persisted Queries abuse](0080-api-graphql-apq.md)
- [batch HTTP GraphQL](0075-api-graphql-batch.md)
- [CSRF em mutations cookie-based](0076-api-graphql-csrf.md)