# IDOR em WebSocket messages — path

IDOR em WebSocket messages como pivô. Path curto > monte de finding isolado.

## Papel

IDOR continua sendo o finding de maior ROI em APIs e apps móveis.
Ocorre quando o servidor confia em identificadores controlados pelo cliente (id, uuid, filename)
sem checagem de ownership/role no objeto. Na prática provo impacto com
leitura/escrita cross-tenant e encadeio com mass assignment ou export jobs.

## Por que pivota

- **Subscribe em canais de outro usuário** — muda ruído e o que entra no PDF.
- UUID opaco sem ownership check continua BOLA. Provo com dois subjects no mesmo object_id.

## Cadeia

1. Entrada (escopo)
2. Pivô: IDOR em WebSocket messages
3. Objetivo do ROE
4. Persistência só se pedido, com kill-switch

## Execução do pivô

1. Mapeio todos os IDs em requests (path, query, body, headers).
2. Crio duas contas de teste no escopo (A/B) e troco IDs.
3. Testo métodos HTTP alternativos (GET vs DELETE) e endpoints batch.
4. Avalio UUIDs previsíveis vs sequenciais; ainda assim testo ACL.
5. Quantifico impacto (PII, financial, admin actions) com evidência mínima necessária.

## Exemplo

```http
GET /api/v1/resources/usr_01HZX HTTP/1.1
Host: app.lab.local
Authorization: Bearer TOKEN_USER_B
# object_id de USER_A — se 200 com PII, BOLA (ws)
# tag bb04c6
```

## Freio

UUID não é autorização. GraphQL node IDs ofuscados também falham.
Cuidado com rate-limit e lockout ao enumerar.

## No caminho

Detectar: Access logs com object_id + subject; anomalias cross-tenant;
deny-by-default metrics.

Remediar: Checagem server-side de ownership em **todo** objeto;
testes automatizados de BOLA; IDs opacos sem sequential leak se desejável.

## Prova

Dois usuários, request diff, response mostrando dado de outro tenant (redigido).

Parâmetro é boundary: de onde veio o valor (cookie, claim, hidden) importa mais que o payload da vez.

## Refs

- OWASP API Top 10 API1
- WSTG-ATHZ-04
- PortSwigger Access Control