# isAdmin/role elevation

`T1190 Exploit Public-Facing Application`

## Por que importa

Frameworks que bindam JSON automaticamente permitem que o cliente defina campos privilegiados
(role, isAdmin, price, balance, verified). No teste, inspeciona DTOs, compara response de GET
com campos aceitos no PATCH e usa fuzzing de propriedades ocultas.

## Variante

- Detalhe que pago pra ver: **Impacto Critical típico**.
- GET do objeto vs PATCH com role/price/tenant_id. Gateway que stripa ≠ origin que aceita.

## Passo a passo

1. Capturo modelo de objeto via GET/OPTIONS/docs.
2. Reenvio PATCH/POST com campos extras (role, credits, organization_id).
3. Testo notações nested e JSON merge patch.
4. Verifico se campos read-only são honrados.
5. Encadeio com IDOR se object_id também for controlável.

## PoC mínimo

```http
PATCH /api/v1/profile HTTP/1.1
Host: api.lab.local
Cookie: session=USER_A
Content-Type: application/json

{"displayName":"lab","role":"admin","tenant_id":"TENANT_B"}
# mass-assign role-flag: GET depois e comparar role — tag 323d0f
```

## Nota de operador

Começo pelo contrato real (OpenAPI/HAR/introspection), não pelo PDF de arquitetura.

## Armadilha

Documentação OpenAPI pode estar incompleta — fuzz mesmo assim.
Alguns gateways stripam campos; teste direto no origin se autorizado.

Antes de Critical em isAdmin/role elevation, confiro se a telemetria que eu cobraria reagiria — Schema validation rejects; alertas de propriedades desconhecidas.

## Depois

Detecção — Schema validation rejects; alertas de propriedades desconhecidas.

Remediação — Allowlist de campos por endpoint; DTOs separados input/output; testes de contrato.

No PDF — Request com campo privilegiado; response provando alteração.

## Refs

- OWASP API3
- PortSwigger Mass Assignment