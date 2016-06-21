# API móvel com IDs em JWT claims vs body — detecção

Gap de detecção em `T1078 Valid Accounts (abuso de sessão) / T1190` / API móvel com IDs em JWT claims vs body. PoC mínimo, telemetria ligada.

## Contexto

IDOR continua sendo o finding de maior ROI em APIs e apps móveis.
Ocorre quando o servidor confia em identificadores controlados pelo cliente (id, uuid, filename)
sem checagem de ownership/role no objeto. Na prática provo impacto com
leitura/escrita cross-tenant e encadeio com mass assignment ou export jobs.

## Hipótese

- **Claims mentem; body manda — valide servidor** — muda ruído e o que entra no PDF.
- UUID opaco sem ownership check continua BOLA. Provo com dois subjects no mesmo object_id.
- Testo verify path na lib real. Claim admin:true sem verify não é bypass.

## Como corro o purple

1. Confirmo log source relevante.
2. Disparo o fluxo abaixo.
3. Anoto alerta / ausência.
4. Se silêncio, abro finding de detecção.

### PoC

1. Mapeio todos os IDs em requests (path, query, body, headers).
2. Crio duas contas de teste no escopo (A/B) e troco IDs.
3. Testo métodos HTTP alternativos (GET vs DELETE) e endpoints batch.
4. Avalio UUIDs previsíveis vs sequenciais; ainda assim testo ACL.
5. Quantifico impacto (PII, financial, admin actions) com evidência mínima necessária.

## Exemplo

```text
access_log: user=USER_B resource=usr_01HZX owner=USER_A status=200
regra: deny quando subject != owner — tag 97a146 (mobile-api)
```

## Sinal

Access logs com object_id + subject; anomalias cross-tenant;
deny-by-default metrics.

## Freio

UUID não é autorização. GraphQL node IDs ofuscados também falham.
Cuidado com rate-limit e lockout ao enumerar.

WAF bypass só depois da prova de impacto. Senão vira discussão de tool com o blue.

## Evidência

Dois usuários, request diff, response mostrando dado de outro tenant (redigido).

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- OWASP API Top 10 API1
- WSTG-ATHZ-04
- PortSwigger Access Control