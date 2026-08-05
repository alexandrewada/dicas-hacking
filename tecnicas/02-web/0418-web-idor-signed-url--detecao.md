---
id: "0418"
categoria: "02-web"
familia: "web-idor"
slug: "signed-url"
angulo: "detecao"
mitre: "T1078"
owasp: "WSTG-ATHZ-04"
tags: ["02-web", "web-idor", "detecao", "t1078"]
aliases: ["abuso de signed URLs", "signed-url", "signed-url-detecao"]
---

# abuso de signed URLs — detecção

Purple em abuso de signed URLs: uma execução limpa. A pergunta é se alertou — não se o exploit 'passa'.

## Contexto

IDOR continua sendo o finding de maior ROI em APIs e apps móveis.
Ocorre quando o servidor confia em identificadores controlados pelo cliente (id, uuid, filename)
sem checagem de ownership/role no objeto. Na prática provo impacto com
leitura/escrita cross-tenant e encadeio com mass assignment ou export jobs.

## Hipótese

- Detalhe que pago pra ver: **Path manipulation pós-assinatura se canonicalização falha**.
- UUID opaco sem ownership check continua BOLA. Provo com dois subjects no mesmo object_id.

## Como corro o purple

1. Janela combinada com blue (ou auto-lab).
2. Telemetria mínima no ar.
3. PoC **uma** vez.
4. MTTD + qualidade do playbook.
5. Silêncio → gap + esboço de regra amarrado a `T1078 Valid Accounts (abuso de sessão) / T1190`.

### PoC

1. Mapeio todos os IDs em requests (path, query, body, headers).
2. Crio duas contas de teste no escopo (A/B) e troco IDs.
3. Testo métodos HTTP alternativos (GET vs DELETE) e endpoints batch.
4. Avalio UUIDs previsíveis vs sequenciais; ainda assim testo ACL.
5. Quantifico impacto (PII, financial, admin actions) com evidência mínima necessária.

## Sinal / query

```text
access_log: user=USER_B resource=a1b2c3d4-e5f6-7890-abcd-ef1234567890 owner=USER_A status=200
regra: deny quando subject != owner — tag 4463c2 (signed-url)
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

- [MITRE ATT&CK T1078](https://attack.mitre.org/techniques/T1078/)
- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [WSTG-ATHZ-04](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/02-Testing_for_Bypassing_Authorization_Schema)
- [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
- [PortSwigger — Access control](https://portswigger.net/web-security/access-control)

## Relacionadas

- [abuso de signed URLs](0038-web-idor-signed-url.md)
- [abuso de signed URLs — path](0798-web-idor-signed-url--path.md)
- [IDOR com IDs numéricos](0031-web-idor-numeric.md)
- [endpoints batch/export](0034-web-idor-batch.md)
- [BOLA em GraphQL](0035-web-idor-graphql.md)