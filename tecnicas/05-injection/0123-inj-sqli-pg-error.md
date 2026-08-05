---
id: "0123"
categoria: "05-injection"
familia: "inj-sqli"
slug: "pg-error"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-sqli", "base", "t1190"]
aliases: ["PostgreSQL error/verbose", "pg-error"]
---

# PostgreSQL error/verbose

## Contexto

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Detalhe

- **Cast e XML functions.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

## Execução

1. Identifico sinks (search, sort, filters, JSON params).
2. Diferenciar numérico vs string; observe erros.
3. Boolean/time-based se cego; OOB se rede permite.
4. Confirmar DBMS; extrair só evidência mínima.
5. Avalio stacked queries e second-order.

## Sinal / query

```http
GET /items?id=1'+AND+1%3d1-- HTTP/1.1
Host: app.lab.local
Cookie: session=USER_A
# boolean mínimo pg-error; sem DROP — tag 10ec21
```

## OpSec

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE. Blind/time depois de error/boolean. Baseline de latência antes de claimar RCE.

## Cuidados

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

## Fechamento

| | |
|---|---|
| Detecção | WAF + DB anomaly (high row reads); prepared statement coverage. |
| Remediação | Parameterized queries; least privilege DB user; WAF; disable dangerous procs. |
| Evidência | Payload + response diferencial; amostra de dado de teste; query log se disponível. |

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [PortSwigger — SQL injection](https://portswigger.net/web-security/sql-injection)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [sqlmap — usage](https://sqlmap.org/)

## Relacionadas

- [PostgreSQL error/verbose — detecção](0503-inj-sqli-pg-error--detecao.md)
- [PostgreSQL error/verbose — hardening](0883-inj-sqli-pg-error--hardening.md)
- [JSON operators injection](0129-inj-sqli-json-sql.md)
- [MSSQL out-of-band](0124-inj-sqli-mssql-oob.md)
- [SQLi blind em MySQL](0122-inj-sqli-mysql-blind.md)
- [MySQL error-based](0121-inj-sqli-mysql-error.md)