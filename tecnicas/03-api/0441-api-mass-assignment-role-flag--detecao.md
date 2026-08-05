---
id: "0441"
categoria: "03-api"
familia: "api-mass-assignment"
slug: "role-flag"
angulo: "detecao"
mitre: "T1190"
owasp: ""
tags: ["03-api", "api-mass-assignment", "detecao", "t1190"]
aliases: ["isAdmin/role elevation", "role-flag", "role-flag-detecao"]
---

# isAdmin/role elevation — detecção

Se o SOC não vê isAdmin/role elevation, o finding é de cobertura, não de ego ofensivo.

## Contexto

Frameworks que bindam JSON automaticamente permitem que o cliente defina campos privilegiados
(role, isAdmin, price, balance, verified). No teste, inspeciona DTOs, compara response de GET
com campos aceitos no PATCH e usa fuzzing de propriedades ocultas.

## Hipótese

- Detalhe que pago pra ver: **Impacto Critical típico**.
- GET do objeto vs PATCH com role/price/tenant_id. Gateway que stripa ≠ origin que aceita.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Capturo modelo de objeto via GET/OPTIONS/docs.
2. Reenvio PATCH/POST com campos extras (role, credits, organization_id).
3. Testo notações nested e JSON merge patch.
4. Verifico se campos read-only são honrados.
5. Encadeio com IDOR se object_id também for controlável.

## Sinal / query

```text
audit: user USER_A patched protected fields role/tenant_id
expected deny — tag 769659 (role-flag)
```

## Sinal

Schema validation rejects; alertas de propriedades desconhecidas.

## Freio

Documentação OpenAPI pode estar incompleta — fuzz mesmo assim.
Alguns gateways stripam campos; teste direto no origin se autorizado.

Começo pelo contrato real (OpenAPI/HAR/introspection), não pelo PDF de arquitetura.

## Evidência

Request com campo privilegiado; response provando alteração.

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [PortSwigger — Mass assignment](https://portswigger.net/web-security/access-control)
- [OWASP API3 BOPLA](https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/)

## Relacionadas

- [isAdmin/role elevation](0061-api-mass-assignment-role-flag.md)
- [isAdmin/role elevation — path](0821-api-mass-assignment-role-flag--path.md)
- [import CSV com colunas extras](0069-api-mass-assignment-csv-import.md)
- [GraphQL input objects](0067-api-mass-assignment-graphql-input.md)
- [JSON Merge Patch RFC 7396](0065-api-mass-assignment-json-merge.md)
- [nested JSON binding](0064-api-mass-assignment-nested.md)
- [IDOR com IDs numéricos (path)](../02-web/0031-web-idor-numeric.md)
- [scope elevation (path)](../04-auth/0118-auth-oauth-oidc-scope-escalation.md)