---
id: "0823"
categoria: "03-api"
familia: "api-mass-assignment"
slug: "tenant"
angulo: "path"
mitre: "T1190"
owasp: ""
tags: ["03-api", "api-mass-assignment", "path", "t1190"]
aliases: ["troca de organization_id", "tenant", "tenant-path"]
---

# troca de organization_id — path

troca de organization_id como pivô. Path curto > monte de finding isolado.

## Papel

Frameworks que bindam JSON automaticamente permitem que o cliente defina campos privilegiados
(role, isAdmin, price, balance, verified). No teste, inspeciona DTOs, compara response de GET
com campos aceitos no PATCH e usa fuzzing de propriedades ocultas.

## Por que pivota

- Detalhe que pago pra ver: **Cross-tenant**.
- GET do objeto vs PATCH com role/price/tenant_id. Gateway que stripa ≠ origin que aceita.

## Cadeia

1. Entrada (escopo)
2. Pivô: troca de organization_id
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Capturo modelo de objeto via GET/OPTIONS/docs.
2. Reenvio PATCH/POST com campos extras (role, credits, organization_id).
3. Testo notações nested e JSON merge patch.
4. Verifico se campos read-only são honrados.
5. Encadeio com IDOR se object_id também for controlável.

## Exemplo

```http
PATCH /api/v1/profile HTTP/1.1
Host: api.lab.local
Cookie: session=USER_A
Content-Type: application/json

{"displayName":"lab","role":"admin","tenant_id":"TENANT_B"}
# mass-assign tenant: GET depois e comparar role — tag b8045e
```

## Freio

Documentação OpenAPI pode estar incompleta — fuzz mesmo assim.
Alguns gateways stripam campos; teste direto no origin se autorizado.

## No caminho

Detectar: Schema validation rejects; alertas de propriedades desconhecidas.

Remediar: Allowlist de campos por endpoint; DTOs separados input/output; testes de contrato.

## Prova

Request com campo privilegiado; response provando alteração.

403 no gateway com 200 no origin — path direto e Host conforme ROE.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [PortSwigger — Mass assignment](https://portswigger.net/web-security/access-control)
- [OWASP API3 BOPLA](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)

## Relacionadas

- [troca de organization_id](0063-api-mass-assignment-tenant.md)
- [troca de organization_id — detecção](0443-api-mass-assignment-tenant--detecao.md)
- [import CSV com colunas extras](0069-api-mass-assignment-csv-import.md)
- [GraphQL input objects](0067-api-mass-assignment-graphql-input.md)
- [JSON Merge Patch RFC 7396](0065-api-mass-assignment-json-merge.md)
- [nested JSON binding](0064-api-mass-assignment-nested.md)
- [IDOR mesmo com UUID (path)](../02-web/0032-web-idor-uuid.md)
- [autorização por campo (path)](0074-api-graphql-field-authz.md)