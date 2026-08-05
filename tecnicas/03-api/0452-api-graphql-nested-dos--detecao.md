---
id: "0452"
categoria: "03-api"
familia: "api-graphql"
slug: "nested-dos"
angulo: "detecao"
mitre: ""
owasp: ""
tags: ["03-api", "api-graphql", "detecao"]
aliases: ["DoS por aninhamento", "nested-dos", "nested-dos-detecao"]
---

# DoS por aninhamento — detecção

Se o SOC não vê DoS por aninhamento, o finding é de cobertura, não de ego ofensivo.

## Contexto

GraphQL centraliza a superfície: introspecção revela schema; queries aninhadas causam DoS;
mutations herdam falhas de authz; batching e aliases burla rate-limits. Teste expert combina
field suggestions, circular fragments e authorization em resolvers (não só no gateway).

## Hipótese

- **Demonstre com limite seguro.** Sem isso o playbook da família mente.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Tento introspecção e field suggestions.
2. Mapeio mutations sensíveis e testar authz por campo.
3. Avalio profundidade/complexidade (nested friends { friends }).
4. Batching/aliases para brute force e rate-limit bypass.
5. Verifico subscriptions e file uploads (multipart).

## Sinal / query

```text
graphql_complexity > budget OR node(id) cross-user 200
variant nested-dos tag acde7e
```

## Sinal

Query cost metrics; deny introspection em prod; per-resolver auth logs.

## Freio

Introspecção desabilitada não elimina schema leaks via erros.
Não causo DoS destrutivo em produção — use limites acordados.

Começo pelo contrato real (OpenAPI/HAR/introspection), não pelo PDF de arquitetura.

## Evidência

Schema extrato (se permitido); prova de bypass authz; custo de query.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)
- [PayloadsAllTheThings — GraphQL](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection)

## Relacionadas

- [DoS por aninhamento](0072-api-graphql-nested-dos.md)
- [DoS por aninhamento — path](0832-api-graphql-nested-dos--path.md)
- [aliases para bypass de rate limit](0073-api-graphql-alias-bruteforce.md)
- [Automatic Persisted Queries abuse](0080-api-graphql-apq.md)
- [batch HTTP GraphQL](0075-api-graphql-batch.md)
- [CSRF em mutations cookie-based](0076-api-graphql-csrf.md)