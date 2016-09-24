# GraphQL input objects

## Leitura rápida

Frameworks que bindam JSON automaticamente permitem que o cliente defina campos privilegiados
(role, isAdmin, price, balance, verified). No teste, inspeciona DTOs, compara response de GET
com campos aceitos no PATCH e usa fuzzing de propriedades ocultas.

## Foco

- Detalhe que pago pra ver: **Campos sensíveis no input type**.
- GET do objeto vs PATCH com role/price/tenant_id. Gateway que stripa ≠ origin que aceita.
- Batching, cost, IDOR em node(id). Introspection off não mata BOLA.

## Mãos na massa

1. Capturo modelo de objeto via GET/OPTIONS/docs.
2. Reenvio PATCH/POST com campos extras (role, credits, organization_id).
3. Testo notações nested e JSON merge patch.
4. Verifico se campos read-only são honrados.
5. Encadeio com IDOR se object_id também for controlável.

## No lab ficou assim

```http
PATCH /api/v1/profile HTTP/1.1
Host: api.lab.local
Cookie: session=USER_A
Content-Type: application/json

{"displayName":"lab","role":"admin","tenant_id":"TENANT_B"}
# mass-assign graphql-input: GET depois e comparar role — tag cb5184
```

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Pitfall

Documentação OpenAPI pode estar incompleta — fuzz mesmo assim.
Alguns gateways stripam campos; teste direto no origin se autorizado.

## Detecção / remediação

Schema validation rejects; alertas de propriedades desconhecidas.

→ Allowlist de campos por endpoint; DTOs separados input/output; testes de contrato.

## Prova

Request com campo privilegiado; response provando alteração.

## Refs

- OWASP API3
- PortSwigger Mass Assignment