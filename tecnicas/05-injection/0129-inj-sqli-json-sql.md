---
id: "0129"
categoria: "05-injection"
familia: "inj-sqli"
slug: "json-sql"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-sqli", "base", "t1190"]
aliases: ["JSON operators injection", "json-sql"]
---

# JSON operators injection

**A03 Injection** · `T1190`

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

**Variante:** **MySQL/PG JSON path.** Sem isso o playbook da família mente. Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

**Método**

1. Identifico sinks (search, sort, filters, JSON params).
2. Diferenciar numérico vs string; observe erros.
3. Boolean/time-based se cego; OOB se rede permite.
4. Confirmar DBMS; extrair só evidência mínima.
5. Avalio stacked queries e second-order.

## No lab ficou assim

```http
GET /items?id=1'+AND+1%3d1-- HTTP/1.1
Host: app.lab.local
Cookie: session=USER_A
# boolean mínimo json-sql; sem DROP — tag 447c8c
```

**Freio:** Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.

Já abri High demais em JSON operators injection por sintoma sem efeito. Cruzei com: WAF + DB anomaly (high row reads); prepared statement coverage. Sem side-effect, baixo.

Detecto via: WAF + DB anomaly (high row reads); prepared statement coverage.

Corrijo com: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.

Levo no report: Payload + response diferencial; amostra de dado de teste; query log se disponível.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [PortSwigger — SQL injection](https://portswigger.net/web-security/sql-injection)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [sqlmap — usage](https://sqlmap.org/)

## Relacionadas

- [JSON operators injection — lab](0509-inj-sqli-json-sql--lab.md)
- [JSON operators injection — hardening](0889-inj-sqli-json-sql--hardening.md)
- [MSSQL out-of-band](0124-inj-sqli-mssql-oob.md)
- [SQLi blind em MySQL](0122-inj-sqli-mysql-blind.md)
- [MySQL error-based](0121-inj-sqli-mysql-error.md)
- [polyglot SQL + NoSQL](0130-inj-sqli-nosqli-bridge.md)