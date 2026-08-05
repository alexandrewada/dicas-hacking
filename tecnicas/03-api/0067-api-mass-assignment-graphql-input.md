---
id: "0067"
categoria: "03-api"
familia: "api-mass-assignment"
slug: "graphql-input"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["03-api", "api-mass-assignment", "base", "t1190"]
aliases: ["GraphQL input objects", "graphql-input"]
---

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

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [PortSwigger — Mass assignment](https://portswigger.net/web-security/access-control)
- [OWASP API3 BOPLA](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)

## Relacionadas

- [GraphQL input objects — detecção](0447-api-mass-assignment-graphql-input--detecao.md)
- [GraphQL input objects — path](0827-api-mass-assignment-graphql-input--path.md)
- [import CSV com colunas extras](0069-api-mass-assignment-csv-import.md)
- [JSON Merge Patch RFC 7396](0065-api-mass-assignment-json-merge.md)
- [nested JSON binding](0064-api-mass-assignment-nested.md)
- [ORM update com map completo](0070-api-mass-assignment-orm-bind.md)