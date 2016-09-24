# JSON Merge Patch RFC 7396

**API3:2023 Broken Object Property Level Authorization** · `T1190 Exploit Public-Facing Application`

## Contexto

Frameworks que bindam JSON automaticamente permitem que o cliente defina campos privilegiados
(role, isAdmin, price, balance, verified). No teste, inspeciona DTOs, compara response de GET
com campos aceitos no PATCH e usa fuzzing de propriedades ocultas.

## Como eu faço

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
# mass-assign json-merge: GET depois e comparar role — tag f6cd12
```

## Diferencial desta nota

- Se não validar **Null para deletar campos de segurança**, a nota fica genérica.
- GET do objeto vs PATCH com role/price/tenant_id. Gateway que stripa ≠ origin que aceita.

Falso amigo em JSON Merge Patch RFC 7396: UI/log gritam, impacto não. Exijo Schema validation rejects.

## Onde já errei

Documentação OpenAPI pode estar incompleta — fuzz mesmo assim.
Alguns gateways stripam campos; teste direto no origin se autorizado.

Batch e webhook: ACL costuma autorizar o primeiro ID do array e ignorar o resto. Testo isso cedo.

## Entrega

- blue: Schema validation rejects; alertas de propriedades desconhecidas.
- fix: Allowlist de campos por endpoint; DTOs separados input/output; testes de contrato.
- proof: Request com campo privilegiado; response provando alteração.

## Refs

- OWASP API3
- PortSwigger Mass Assignment