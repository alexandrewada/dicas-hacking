# autorização por campo

**API Top 10 / A01 Broken Access Control** · `T1190`

## Contexto

GraphQL centraliza a superfície: introspecção revela schema; queries aninhadas causam DoS;
mutations herdam falhas de authz; batching e aliases burla rate-limits. Teste expert combina
field suggestions, circular fragments e authorization em resolvers (não só no gateway).

## O que muda aqui

- **salary visível a user sem clearance.** Sem isso o playbook da família mente.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

## Como testo

1. Tento introspecção e field suggestions.
2. Mapeio mutations sensíveis e testar authz por campo.
3. Avalio profundidade/complexidade (nested friends { friends }).
4. Batching/aliases para brute force e rate-limit bypass.
5. Verifico subscriptions e file uploads (multipart).

## Exemplo

```http
POST /graphql HTTP/1.1
Host: api.lab.local
Content-Type: application/json

{"query":"query { node(id:\"usr_01HZX\") { ... on User { email role } } }"}
# GraphQL field-authz — tag 3fde81
```

## Campo

Começo pelo contrato real (OpenAPI/HAR/introspection), não pelo PDF de arquitetura.

Já abri High demais em autorização por campo por sintoma sem efeito. Cruzei com: Query cost metrics; deny introspection em prod; per-resolver auth logs. Sem side-effect, baixo.

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