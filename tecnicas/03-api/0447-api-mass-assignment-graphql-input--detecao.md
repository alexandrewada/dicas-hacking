# GraphQL input objects — detecção

Gap de detecção em `T1190 Exploit Public-Facing Application` / GraphQL input objects. PoC mínimo, telemetria ligada.

## Contexto

Frameworks que bindam JSON automaticamente permitem que o cliente defina campos privilegiados
(role, isAdmin, price, balance, verified). No teste, inspeciona DTOs, compara response de GET
com campos aceitos no PATCH e usa fuzzing de propriedades ocultas.

## Hipótese

- Detalhe que pago pra ver: **Campos sensíveis no input type**.
- GET do objeto vs PATCH com role/price/tenant_id. Gateway que stripa ≠ origin que aceita.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

## Como corro o purple

1. Confirmo log source relevante.
2. Disparo o fluxo abaixo.
3. Anoto alerta / ausência.
4. Se silêncio, abro finding de detecção.

### PoC

1. Capturo modelo de objeto via GET/OPTIONS/docs.
2. Reenvio PATCH/POST com campos extras (role, credits, organization_id).
3. Testo notações nested e JSON merge patch.
4. Verifico se campos read-only são honrados.
5. Encadeio com IDOR se object_id também for controlável.

## Sinal / query

```text
audit: user USER_A patched protected fields role/tenant_id
expected deny — tag 2b0161 (graphql-input)
```

## Sinal

Schema validation rejects; alertas de propriedades desconhecidas.

## Freio

Documentação OpenAPI pode estar incompleta — fuzz mesmo assim.
Alguns gateways stripam campos; teste direto no origin se autorizado.

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Evidência

Request com campo privilegiado; response provando alteração.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- OWASP API3
- PortSwigger Mass Assignment