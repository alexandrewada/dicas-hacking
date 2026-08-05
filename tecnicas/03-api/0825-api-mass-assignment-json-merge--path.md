---
id: "0825"
categoria: "03-api"
familia: "api-mass-assignment"
slug: "json-merge"
angulo: "path"
mitre: "T1190"
owasp: ""
tags: ["03-api", "api-mass-assignment", "path", "t1190"]
aliases: ["JSON Merge Patch RFC 7396", "json-merge", "json-merge-path"]
---

# JSON Merge Patch RFC 7396 — path

JSON Merge Patch RFC 7396 como pivô. Path curto > monte de finding isolado.

## Papel

Frameworks que bindam JSON automaticamente permitem que o cliente defina campos privilegiados
(role, isAdmin, price, balance, verified). No teste, inspeciona DTOs, compara response de GET
com campos aceitos no PATCH e usa fuzzing de propriedades ocultas.

## Por que pivota

- Se não validar **Null para deletar campos de segurança**, a nota fica genérica.
- GET do objeto vs PATCH com role/price/tenant_id. Gateway que stripa ≠ origin que aceita.

## Cadeia

1. Entrada (escopo)
2. Pivô: JSON Merge Patch RFC 7396
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

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
# mass-assign json-merge: GET depois e comparar role — tag dd0f59
```

## Freio

Documentação OpenAPI pode estar incompleta — fuzz mesmo assim.
Alguns gateways stripam campos; teste direto no origin se autorizado.

## No caminho

Detectar: Schema validation rejects; alertas de propriedades desconhecidas.

Remediar: Allowlist de campos por endpoint; DTOs separados input/output; testes de contrato.

## Prova

Request com campo privilegiado; response provando alteração.

Batch e webhook: ACL costuma autorizar o primeiro ID do array e ignorar o resto. Testo isso cedo.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [PortSwigger — Mass assignment](https://portswigger.net/web-security/access-control)
- [OWASP API3 BOPLA](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)

## Relacionadas

- [JSON Merge Patch RFC 7396](0065-api-mass-assignment-json-merge.md)
- [JSON Merge Patch RFC 7396 — detecção](0445-api-mass-assignment-json-merge--detecao.md)
- [import CSV com colunas extras](0069-api-mass-assignment-csv-import.md)
- [GraphQL input objects](0067-api-mass-assignment-graphql-input.md)
- [nested JSON binding](0064-api-mass-assignment-nested.md)
- [ORM update com map completo](0070-api-mass-assignment-orm-bind.md)