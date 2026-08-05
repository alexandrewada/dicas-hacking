---
id: "0453"
categoria: "03-api"
familia: "api-graphql"
slug: "alias-bruteforce"
angulo: "detecao"
mitre: "T1190"
owasp: ""
tags: ["03-api", "api-graphql", "detecao", "t1190"]
aliases: ["aliases para bypass de rate limit", "alias-bruteforce", "alias-bruteforce-detecao"]
---

# aliases para bypass de rate limit — detecção

Gap de detecção em `T1190` / aliases para bypass de rate limit. PoC mínimo, telemetria ligada.

## Contexto

GraphQL centraliza a superfície: introspecção revela schema; queries aninhadas causam DoS;
mutations herdam falhas de authz; batching e aliases burla rate-limits. Teste expert combina
field suggestions, circular fragments e authorization em resolvers (não só no gateway).

## Hipótese

- **OTP/password guess.** Sem isso o playbook da família mente.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

## Como corro o purple

1. Confirmo log source relevante.
2. Disparo o fluxo abaixo.
3. Anoto alerta / ausência.
4. Se silêncio, abro finding de detecção.

### PoC

1. Tento introspecção e field suggestions.
2. Mapeio mutations sensíveis e testar authz por campo.
3. Avalio profundidade/complexidade (nested friends { friends }).
4. Batching/aliases para brute force e rate-limit bypass.
5. Verifico subscriptions e file uploads (multipart).

## Sinal / query

```text
graphql_complexity > budget OR node(id) cross-user 200
variant alias-bruteforce tag 3f72d3
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

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)
- [PayloadsAllTheThings — GraphQL](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection)

## Relacionadas

- [aliases para bypass de rate limit](0073-api-graphql-alias-bruteforce.md)
- [aliases para bypass de rate limit — path](0833-api-graphql-alias-bruteforce--path.md)
- [Automatic Persisted Queries abuse](0080-api-graphql-apq.md)
- [batch HTTP GraphQL](0075-api-graphql-batch.md)
- [CSRF em mutations cookie-based](0076-api-graphql-csrf.md)
- [diretivas custom perigosas](0079-api-graphql-directive.md)