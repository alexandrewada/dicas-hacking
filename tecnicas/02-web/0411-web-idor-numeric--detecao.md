---
id: "0411"
categoria: "02-web"
familia: "web-idor"
slug: "numeric"
angulo: "detecao"
mitre: "T1078"
owasp: "WSTG-ATHZ-04"
tags: ["02-web", "web-idor", "detecao", "t1078"]
aliases: ["IDOR com IDs numéricos", "numeric", "numeric-detecao"]
---

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

- [MITRE ATT&CK T1078](https://attack.mitre.org/techniques/T1078/)
- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [WSTG-ATHZ-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Bypassing_Authorization_Schema)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [PortSwigger — Access control](https://portswigger.net/web-security/access-control)

## Relacionadas

- [IDOR com IDs numéricos](0031-web-idor-numeric.md)
- [IDOR com IDs numéricos — path](0791-web-idor-numeric--path.md)
- [endpoints batch/export](0034-web-idor-batch.md)
- [BOLA em GraphQL](0035-web-idor-graphql.md)
- [isAdmin/role elevation (path)](../03-api/0061-api-mass-assignment-role-flag.md)
- [tampering de role/admin (path)](../03-api/0086-api-jwt-claim-tamper.md)