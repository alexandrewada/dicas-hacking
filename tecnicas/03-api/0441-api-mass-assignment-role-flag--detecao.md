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

- OWASP API3
- PortSwigger Mass Assignment