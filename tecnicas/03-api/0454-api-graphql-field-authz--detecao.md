# autorização por campo — detecção

Se o SOC não vê autorização por campo, o finding é de cobertura, não de ego ofensivo.

## Contexto

GraphQL centraliza a superfície: introspecção revela schema; queries aninhadas causam DoS;
mutations herdam falhas de authz; batching e aliases burla rate-limits. Teste expert combina
field suggestions, circular fragments e authorization em resolvers (não só no gateway).

## Hipótese

- **salary visível a user sem clearance.** Sem isso o playbook da família mente.
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
variant field-authz tag 985a72
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

- OWASP GraphQL Cheat Sheet
- PayloadsAllTheThings GraphQL