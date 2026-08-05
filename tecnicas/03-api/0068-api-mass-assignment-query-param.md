---
id: "0068"
categoria: "03-api"
familia: "api-mass-assignment"
slug: "query-param"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["03-api", "api-mass-assignment", "base", "t1190"]
aliases: ["HPP / mass assign via query", "query-param"]
---

# HPP / mass assign via query

**API3:2023 Broken Object Property Level Authorization** · `T1190 Exploit Public-Facing Application`

## Contexto

Frameworks que bindam JSON automaticamente permitem que o cliente defina campos privilegiados
(role, isAdmin, price, balance, verified). No teste, inspeciona DTOs, compara response de GET
com campos aceitos no PATCH e usa fuzzing de propriedades ocultas.

## O que muda aqui

- **Frameworks legados.** Sem isso o playbook da família mente.
- GET do objeto vs PATCH com role/price/tenant_id. Gateway que stripa ≠ origin que aceita.

## Como testo

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
# mass-assign query-param: GET depois e comparar role — tag 5e6c98
```

## Campo

403 no gateway com 200 no origin — path direto e Host conforme ROE.

Já abri High demais em HPP / mass assign via query por sintoma sem efeito. Cruzei com: Schema validation rejects; alertas de propriedades desconhecidas. Sem side-effect, baixo.

## Já me queimei

Documentação OpenAPI pode estar incompleta — fuzz mesmo assim.
Alguns gateways stripam campos; teste direto no origin se autorizado.

## Blue

- Detectar: Schema validation rejects; alertas de propriedades desconhecidas.
- Fechar: Allowlist de campos por endpoint; DTOs separados input/output; testes de contrato.

## Evidência

Request com campo privilegiado; response provando alteração.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [PortSwigger — Mass assignment](https://portswigger.net/web-security/access-control)
- [OWASP API3 BOPLA](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)

## Relacionadas

- [HPP / mass assign via query — detecção](0448-api-mass-assignment-query-param--detecao.md)
- [HPP / mass assign via query — path](0828-api-mass-assignment-query-param--path.md)
- [import CSV com colunas extras](0069-api-mass-assignment-csv-import.md)
- [GraphQL input objects](0067-api-mass-assignment-graphql-input.md)
- [JSON Merge Patch RFC 7396](0065-api-mass-assignment-json-merge.md)
- [nested JSON binding](0064-api-mass-assignment-nested.md)