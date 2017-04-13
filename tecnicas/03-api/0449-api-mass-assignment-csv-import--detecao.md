# import CSV com colunas extras — detecção

Purple em import CSV com colunas extras: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

Frameworks que bindam JSON automaticamente permitem que o cliente defina campos privilegiados
(role, isAdmin, price, balance, verified). No teste, inspeciona DTOs, compara response de GET
com campos aceitos no PATCH e usa fuzzing de propriedades ocultas.

## Hipótese

- Se não validar **Batch privilege**, a nota fica genérica.
- GET do objeto vs PATCH com role/price/tenant_id. Gateway que stripa ≠ origin que aceita.

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1190 Exploit Public-Facing Application`.

### PoC

1. Capturo modelo de objeto via GET/OPTIONS/docs.
2. Reenvio PATCH/POST com campos extras (role, credits, organization_id).
3. Testo notações nested e JSON merge patch.
4. Verifico se campos read-only são honrados.
5. Encadeio com IDOR se object_id também for controlável.

## Exemplo

```text
audit: user USER_A patched protected fields role/tenant_id
expected deny — tag 4c26ea (csv-import)
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