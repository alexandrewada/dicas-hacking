# batch HTTP GraphQL — path

batch HTTP GraphQL como pivô. Path curto > monte de finding isolado.

## Papel

GraphQL centraliza a superfície: introspecção revela schema; queries aninhadas causam DoS;
mutations herdam falhas de authz; batching e aliases burla rate-limits. Teste expert combina
field suggestions, circular fragments e authorization em resolvers (não só no gateway).

## Por que pivota

- Detalhe que pago pra ver: **Array de queries**.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

## Cadeia

1. Entrada (escopo)
2. Pivô: batch HTTP GraphQL
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

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
# GraphQL batch — tag b2e407
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

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Refs

- OWASP GraphQL Cheat Sheet
- PayloadsAllTheThings GraphQL