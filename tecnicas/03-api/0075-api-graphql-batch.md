# batch HTTP GraphQL

**API Top 10 / A01 Broken Access Control** · `T1190`

## Contexto

GraphQL centraliza a superfície: introspecção revela schema; queries aninhadas causam DoS;
mutations herdam falhas de authz; batching e aliases burla rate-limits. Teste expert combina
field suggestions, circular fragments e authorization em resolvers (não só no gateway).

## O que muda aqui

- Detalhe que pago pra ver: **Array de queries**.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

## Como testo

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

{"query":"query { node(id:\"obj_a9269c\") { ... on User { email role } } }"}
# GraphQL batch — tag a9269c
```

## Campo

403 no gateway com 200 no origin — path direto e Host conforme ROE.

Falso amigo em batch HTTP GraphQL: UI/log gritam, impacto não. Exijo Query cost metrics.

## Já me queimei

Introspecção desabilitada não elimina schema leaks via erros.
Não causo DoS destrutivo em produção — use limites acordados.

## Blue

- Detectar: Query cost metrics; deny introspection em prod; per-resolver auth logs.
- Fechar: Disable introspection; query depth/cost limits; authz em cada resolver;
persisted queries.

## Evidência

Schema extrato (se permitido); prova de bypass authz; custo de query.

## Refs

- OWASP GraphQL Cheat Sheet
- PayloadsAllTheThings GraphQL