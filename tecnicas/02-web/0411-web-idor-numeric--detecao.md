# IDOR com IDs numéricos — detecção

Gap de detecção em `T1078 Valid Accounts (abuso de sessão) / T1190` / IDOR com IDs numéricos. PoC mínimo, telemetria ligada.

## Contexto

IDOR continua sendo o finding de maior ROI em APIs e apps móveis.
Ocorre quando o servidor confia em identificadores controlados pelo cliente (id, uuid, filename)
sem checagem de ownership/role no objeto. Na prática provo impacto com
leitura/escrita cross-tenant e encadeio com mass assignment ou export jobs.

## Hipótese

- **Enumeração trivial; mostro amostra limitada no report.** Sem isso o playbook da família mente.
- UUID opaco sem ownership check continua BOLA. Provo com dois subjects no mesmo object_id.

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

## Sinal / query

```kusto
AppRequests
| where Url has '/api/v1/orders/'
| where UserId == 'USER_B' and OwnerId == 'USER_A'
| where ResultCode == 200
| project TimeGenerated, Url, UserId, OwnerId
// IDOR numeric 16e92f
```

## Sinal

Access logs com object_id + subject; anomalias cross-tenant;
deny-by-default metrics.

## Freio

UUID não é autorização. GraphQL node IDs ofuscados também falham.
Cuidado com rate-limit e lockout ao enumerar.

Impacto que eu aceito: ATO, cross-tenant, escrita privilegiada, RCE. Reflection sem sink útil vira Informational.

## Evidência

Dois usuários, request diff, response mostrando dado de outro tenant (redigido).

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- OWASP API Top 10 API1
- WSTG-ATHZ-04
- PortSwigger Access Control