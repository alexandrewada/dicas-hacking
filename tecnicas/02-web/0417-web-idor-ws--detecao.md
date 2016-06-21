# IDOR em WebSocket messages — detecção

Se o SOC não vê IDOR em WebSocket messages, o finding é de cobertura, não de ego ofensivo.

## Contexto

IDOR continua sendo o finding de maior ROI em APIs e apps móveis.
Ocorre quando o servidor confia em identificadores controlados pelo cliente (id, uuid, filename)
sem checagem de ownership/role no objeto. Na prática provo impacto com
leitura/escrita cross-tenant e encadeio com mass assignment ou export jobs.

## Hipótese

- **Subscribe em canais de outro usuário** — muda ruído e o que entra no PDF.
- UUID opaco sem ownership check continua BOLA. Provo com dois subjects no mesmo object_id.

## Como corro o purple

Combinar canal → executar → medir. Sem desligar controle pra 'passar'.

### PoC

1. Mapeio todos os IDs em requests (path, query, body, headers).
2. Crio duas contas de teste no escopo (A/B) e troco IDs.
3. Testo métodos HTTP alternativos (GET vs DELETE) e endpoints batch.
4. Avalio UUIDs previsíveis vs sequenciais; ainda assim testo ACL.
5. Quantifico impacto (PII, financial, admin actions) com evidência mínima necessária.

## Sinal / query

```text
access_log: user=USER_B resource=10042 owner=USER_A status=200
regra: deny quando subject != owner — tag f561ce (ws)
```

## Sinal

Access logs com object_id + subject; anomalias cross-tenant;
deny-by-default metrics.

## Freio

UUID não é autorização. GraphQL node IDs ofuscados também falham.
Cuidado com rate-limit e lockout ao enumerar.

Parâmetro é boundary: de onde veio o valor (cookie, claim, hidden) importa mais que o payload da vez.

## Evidência

Dois usuários, request diff, response mostrando dado de outro tenant (redigido).

Timestamp + identidade lab + query SIEM — ou declaração explícita de alerta que não veio.

## Refs

- OWASP API Top 10 API1
- WSTG-ATHZ-04
- PortSwigger Access Control