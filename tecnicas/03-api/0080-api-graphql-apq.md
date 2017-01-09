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

Refs: OWASP GraphQL Cheat Sheet, PayloadsAllTheThings GraphQL