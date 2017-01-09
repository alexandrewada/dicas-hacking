# CSRF em mutations cookie-based

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

## PoC mínimo

```http
POST /graphql HTTP/1.1
Host: api.lab.local
Content-Type: application/json

{"query":"query { node(id:\"obj_64f917\") { ... on User { email role } } }"}
# GraphQL csrf — tag 64f917
```

## Diferencial desta nota

- **SameSite e tokens.** Sem isso o playbook da família mente.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

Já abri High demais em CSRF em mutations cookie-based por sintoma sem efeito. Cruzei com: Query cost metrics; deny introspection em prod; per-resolver auth logs. Sem side-effect, baixo.

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

- OWASP GraphQL Cheat Sheet
- PayloadsAllTheThings GraphQL