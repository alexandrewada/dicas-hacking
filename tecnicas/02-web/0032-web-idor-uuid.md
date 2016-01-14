# IDOR mesmo com UUID

**API1:2023 BOLA / A01 Broken Access Control** · `T1078 Valid Accounts (abuso de sessão) / T1190`

## Contexto

IDOR continua sendo o finding de maior ROI em APIs e apps móveis.
Ocorre quando o servidor confia em identificadores controlados pelo cliente (id, uuid, filename)
sem checagem de ownership/role no objeto. Na prática provo impacto com
leitura/escrita cross-tenant e encadeio com mass assignment ou export jobs.

## Como eu faço

1. Mapeio todos os IDs em requests (path, query, body, headers).
2. Crio duas contas de teste no escopo (A/B) e troco IDs.
3. Testo métodos HTTP alternativos (GET vs DELETE) e endpoints batch.
4. Avalio UUIDs previsíveis vs sequenciais; ainda assim testo ACL.
5. Quantifico impacto (PII, financial, admin actions) com evidência mínima necessária.

## PoC mínimo

```http
GET /api/v1/resources/10042 HTTP/1.1
Host: app.lab.local
Authorization: Bearer TOKEN_USER_B
# object_id de USER_A — se 200 com PII, BOLA (uuid)
# tag 5326b3
```

## Diferencial desta nota

- **Prove que opacidade ≠ autorização.** Sem isso o playbook da família mente.
- Exporto shortest path até tier0 com o edge exato. Sem isso a remediação vira 'olha o BloodHound'.
- UUID opaco sem ownership check continua BOLA. Provo com dois subjects no mesmo object_id.

Falso amigo em UUIDs com falha de ACL: UI/log gritam, impacto não. Exijo Access logs com object_id + subject.

## Onde já errei

UUID não é autorização. GraphQL node IDs ofuscados também falham.
Cuidado com rate-limit e lockout ao enumerar.

WAF bypass só depois da prova de impacto. Senão vira discussão de tool com o blue.

## Entrega

- blue: Access logs com object_id + subject; anomalias cross-tenant;
deny-by-default metrics.
- fix: Checagem server-side de ownership em **todo** objeto;
testes automatizados de BOLA; IDs opacos sem sequential leak se desejável.
- proof: Dois usuários, request diff, response mostrando dado de outro tenant (redigido).

## Refs

- OWASP API Top 10 API1
- WSTG-ATHZ-04
- PortSwigger Access Control