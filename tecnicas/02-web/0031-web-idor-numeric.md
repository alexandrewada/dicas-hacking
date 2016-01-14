# IDOR com IDs numéricos

**API1:2023 BOLA / A01 Broken Access Control** · `T1078 Valid Accounts (abuso de sessão) / T1190`

IDOR continua sendo o finding de maior ROI em APIs e apps móveis.
Ocorre quando o servidor confia em identificadores controlados pelo cliente (id, uuid, filename)
sem checagem de ownership/role no objeto. Na prática provo impacto com
leitura/escrita cross-tenant e encadeio com mass assignment ou export jobs.

**Variante:** **Enumeração trivial; mostro amostra limitada no report.** Sem isso o playbook da família mente. UUID opaco sem ownership check continua BOLA. Provo com dois subjects no mesmo object_id.

**Método**

1. Mapeio todos os IDs em requests (path, query, body, headers).
2. Crio duas contas de teste no escopo (A/B) e troco IDs.
3. Testo métodos HTTP alternativos (GET vs DELETE) e endpoints batch.
4. Avalio UUIDs previsíveis vs sequenciais; ainda assim testo ACL.
5. Quantifico impacto (PII, financial, admin actions) com evidência mínima necessária.

## Exemplo

```http
GET /api/v1/orders/10042 HTTP/1.1
Host: app.lab.local
Cookie: session=USER_B
# esperado: 403 — se 200 com dados de USER_A, BOLA
# variante numeric tag 13262b
```

**Freio:** UUID não é autorização. GraphQL node IDs ofuscados também falham.

Antes de Critical em IDs numéricos sequenciais, confiro se a telemetria que eu cobraria reagiria — Access logs com object_id + subject; anomalias cross-tenant; deny-by-default metrics.

Detecto via: Access logs com object_id + subject; anomalias cross-tenant;
deny-by-default metrics.

Corrijo com: Checagem server-side de ownership em **todo** objeto;
testes automatizados de BOLA; IDs opacos sem sequential leak se desejável.

Levo no report: Dois usuários, request diff, response mostrando dado de outro tenant (redigido).

Refs: OWASP API Top 10 API1, WSTG-ATHZ-04, PortSwigger Access Control