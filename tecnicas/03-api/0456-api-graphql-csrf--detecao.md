# CSRF em mutations cookie-based — detecção

Gap de detecção em `T1190` / CSRF em mutations cookie-based. PoC mínimo, telemetria ligada.

## Contexto

GraphQL centraliza a superfície: introspecção revela schema; queries aninhadas causam DoS;
mutations herdam falhas de authz; batching e aliases burla rate-limits. Teste expert combina
field suggestions, circular fragments e authorization em resolvers (não só no gateway).

## Hipótese

- **SameSite e tokens.** Sem isso o playbook da família mente.
- SameSite ajuda; não substitui token em API cookie-based. State change cross-site com sessão válida.
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

## Exemplo

```text
graphql_complexity > budget OR node(id) cross-user 200
variant csrf tag 8d7cb5
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

- OWASP GraphQL Cheat Sheet
- PayloadsAllTheThings GraphQL