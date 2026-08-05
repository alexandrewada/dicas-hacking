---
id: "0460"
categoria: "03-api"
familia: "api-graphql"
slug: "apq"
angulo: "detecao"
mitre: "T1190"
owasp: ""
tags: ["03-api", "api-graphql", "detecao", "t1190"]
aliases: ["Automatic Persisted Queries abuse", "apq", "apq-detecao"]
---

# Automatic Persisted Queries abuse — detecção

Purple em Automatic Persisted Queries abuse: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

GraphQL centraliza a superfície: introspecção revela schema; queries aninhadas causam DoS;
mutations herdam falhas de authz; batching e aliases burla rate-limits. Teste expert combina
field suggestions, circular fragments e authorization em resolvers (não só no gateway).

## Hipótese

- Detalhe que pago pra ver: **Se mal implementado**.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1190`.

### PoC

1. Tento introspecção e field suggestions.
2. Mapeio mutations sensíveis e testar authz por campo.
3. Avalio profundidade/complexidade (nested friends { friends }).
4. Batching/aliases para brute force e rate-limit bypass.
5. Verifico subscriptions e file uploads (multipart).

## Exemplo

```text
graphql_complexity > budget OR node(id) cross-user 200
variant apq tag 1eb88f
```

## Sinal

Query cost metrics; deny introspection em prod; per-resolver auth logs.

## Freio

Introspecção desabilitada não elimina schema leaks via erros.
Não causo DoS destrutivo em produção — use limites acordados.

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Evidência

Schema extrato (se permitido); prova de bypass authz; custo de query.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)
- [PayloadsAllTheThings — GraphQL](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/GraphQL%20Injection)

## Relacionadas

- [Automatic Persisted Queries abuse](0080-api-graphql-apq.md)
- [Automatic Persisted Queries abuse — path](0840-api-graphql-apq--path.md)
- [aliases para bypass de rate limit](0073-api-graphql-alias-bruteforce.md)
- [batch HTTP GraphQL](0075-api-graphql-batch.md)
- [CSRF em mutations cookie-based](0076-api-graphql-csrf.md)
- [diretivas custom perigosas](0079-api-graphql-directive.md)