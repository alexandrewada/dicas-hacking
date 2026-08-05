---
id: "0126"
categoria: "05-injection"
familia: "inj-sqli"
slug: "sqlite"
angulo: "base"
mitre: "T1190"
owasp: ""
tags: ["05-injection", "inj-sqli", "base", "t1190"]
aliases: ["SQLite em apps embarcadas", "sqlite"]
---

# SQLite em apps embarcadas

**A03 Injection** · `T1190`

## Contexto

SQLi permanece crítica quando ORMs são bypassados por concatenação, raw queries ou
procedimentos dinâmicos. O especialista escolhe a técnica certa por DBMS, minimiza carga
(exfil por chunks), e prova impacto (leitura de dados de teste / mapa de schema) sem dump destrutivo.

## Como eu faço

1. Identifico sinks (search, sort, filters, JSON params).
2. Diferenciar numérico vs string; observe erros.
3. Boolean/time-based se cego; OOB se rede permite.
4. Confirmar DBMS; extrair só evidência mínima.
5. Avalio stacked queries e second-order.

## Exemplo

```http
GET /items?id=1'+AND+1%3d1-- HTTP/1.1
Host: app.lab.local
Cookie: session=USER_A
# boolean mínimo sqlite; sem DROP — tag 294504
```

## Diferencial desta nota

- **Attached DB tricks.** Sem isso o playbook da família mente.
- Error/boolean/time/stacked — e se o DB user tem priv demais. xp_cmdshell é bônus.

Falso amigo em SQLite em apps embarcadas: UI/log gritam, impacto não. Exijo WAF + DB anomaly (high row reads).

## Onde já errei

Não drope tabelas. Evito `xp_cmdshell` salvo ROE de RCE.
WAF bypass é secundário à prova de impacto.

Payload destrutivo (DROP/shutdown) fica no lab. Em prod: boolean/read-only.

## Entrega

- blue: WAF + DB anomaly (high row reads); prepared statement coverage.
- fix: Parameterized queries; least privilege DB user; WAF; disable dangerous procs.
- proof: Payload + response diferencial; amostra de dado de teste; query log se disponível.

## Refs

- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/)
- [PortSwigger — SQL injection](https://portswigger.net/web-security/sql-injection)
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [sqlmap — usage](https://sqlmap.org/)

## Relacionadas

- [SQLite em apps embarcadas — lab](0506-inj-sqli-sqlite--lab.md)
- [SQLite em apps embarcadas — hardening](0886-inj-sqli-sqlite--hardening.md)
- [JSON operators injection](0129-inj-sqli-json-sql.md)
- [MSSQL out-of-band](0124-inj-sqli-mssql-oob.md)
- [SQLi blind em MySQL](0122-inj-sqli-mysql-blind.md)
- [MySQL error-based](0121-inj-sqli-mysql-error.md)